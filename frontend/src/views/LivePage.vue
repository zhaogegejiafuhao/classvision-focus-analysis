<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 18px; font-weight: bold">
        实时检测 — {{ classroomName }}
      </span>
      <a-space>
        <a-tag v-if="violationCount > 0" color="red" style="font-size: 13px; padding: 2px 10px">
          ⚠️ 违规 {{ violationCount }} 次
        </a-tag>
        <a-popconfirm title="确定结束当前课堂？" @confirm="endClass" ok-text="确定" cancel-text="取消">
          <a-button type="primary" danger :loading="endLoading">结束课堂</a-button>
        </a-popconfirm>
      </a-space>
    </a-layout-header>
    <a-layout-content style="padding: 16px">
      <a-row :gutter="16">
        <a-col :span="16">
          <a-card title="实时画面" :bordered="false">
            <div style="position: relative; background: #000; border-radius: 8px; overflow: hidden">
              <video ref="video" autoplay playsinline style="width: 100%; display: block" />
              <canvas ref="canvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%" />
            </div>
            <a-space style="margin-top: 16px">
              <a-button type="primary" @click="startCamera">开启摄像头</a-button>
              <a-button @click="stopCamera" :disabled="!isStreaming">停止</a-button>
              <a-upload :before-upload="handleUpload" accept="video/*" :show-upload-list="false">
                <a-button>上传视频</a-button>
              </a-upload>
            </a-space>
          </a-card>
        </a-col>
        <a-col :span="8">
          <!-- 注意力看板 -->
          <a-card title="注意力看板" :bordered="false">
            <a-statistic title="检测人数" :value="faceCount" />
            <a-statistic title="平均注意力" :value="avgAttention" suffix="/100" style="margin-top: 16px" />
            <a-row :gutter="8" style="margin-top: 16px">
              <a-col :span="8">
                <a-statistic title="低头" :value="headDownCount" :value-style="{ color: '#cf1322' }" />
              </a-col>
              <a-col :span="8">
                <a-statistic title="转头" :value="headTurnCount" :value-style="{ color: '#fa8c16' }" />
              </a-col>
              <a-col :span="8">
                <a-statistic title="疲劳" :value="fatigueCount" :value-style="{ color: '#722ed1' }" />
              </a-col>
            </a-row>
            <div ref="chartEl" style="width: 100%; height: 200px; margin-top: 16px" />
          </a-card>

          <!-- 违规记录面板 -->
          <a-card title="⚠️ 违规记录" :bordered="false" style="margin-top: 12px">
            <div v-if="cheatingEvents.length === 0" style="text-align: center; padding: 12px; color: #999">
              暂无违规事件
            </div>
            <div v-else class="violation-list">
              <div v-for="(evt, idx) in displayViolations" :key="evt.timestamp + evt.track_id" class="violation-item">
                <div class="violation-header">
                  <a-tag :color="evt.violation_type === 'GAZE_DEVIATION' ? 'orange' : 'red'" size="small">
                    {{ evt.violation_type === 'GAZE_DEVIATION' ? '视线偏离' : '持续低头' }}
                  </a-tag>
                  <span class="violation-track">ID:{{ evt.track_id }}</span>
                  <span class="violation-time">{{ formatTime(evt.timestamp) }}</span>
                </div>
                <div class="violation-scores">
                  <span>视线: {{ evt.gaze_score?.toFixed(0) }}</span>
                  <span>姿态: {{ evt.pose_score?.toFixed(0) }}</span>
                </div>
                <a-image
                  v-if="evt.image_path"
                  :src="evt.image_path"
                  :width="80"
                  :height="60"
                  style="border-radius: 4px; margin-top: 4px"
                  :preview="true"
                />
              </div>
            </div>
          </a-card>
        </a-col>
      </a-row>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import * as echarts from 'echarts'
import { getClassroom, endClassroom } from '@/api/classroom'
import { generateClassroomReport } from '@/api/stats'

const route = useRoute()
const router = useRouter()
const classroomId = route.params.id
const classroomName = ref('')

const video = ref(null)
const canvas = ref(null)
const chartEl = ref(null)
const faceCount = ref(0)
const avgAttention = ref(0)
const headDownCount = ref(0)
const headTurnCount = ref(0)
const fatigueCount = ref(0)

// 违规事件（限制最多保留 50 条，防止内存泄漏）
const MAX_VIOLATIONS = 50
const cheatingEvents = ref([])
const violationCount = ref(0)
const displayViolations = computed(() => cheatingEvents.value.slice(-20).reverse())

let ws = null
let chart = null
let stream = null
let timelineData = []
let lastSendTime = 0
// 💡 优化：发送间隔从200ms改为100ms (10 FPS)，让画面更流畅
// 后端有 frame_seq%30 的保存节流和 %2 的违规检测节流，能承受更高帧率
const SEND_INTERVAL = 100

// 复用 canvas 避免每帧创建新对象（修复内存泄漏）
let _sendCanvas = null
let _sendCtx = null
let _drawLoopTimer = null

const isStreaming = ref(false)
const endLoading = ref(false)

onMounted(async () => {
  const res = await getClassroom(classroomId)
  classroomName.value = res.data.name

  chart = echarts.init(chartEl.value)
  chart.setOption({
    title: { text: '注意力趋势', textStyle: { fontSize: 13 } },
    grid: { top: 30, bottom: 20, left: 40, right: 10 },
    xAxis: { type: 'category', data: [] },
    yAxis: { type: 'value', max: 100, min: 0 },
    series: [{ type: 'line', data: [], smooth: true, areaStyle: { opacity: 0.15 }, itemStyle: { color: '#1890ff' } }],
  })

  // 加载历史违规记录
  loadCheatingRecords()
})

onUnmounted(() => {
  stopCamera()
  if (chart) chart.dispose()
  // 释放发送用 canvas
  _sendCanvas = null
  _sendCtx = null
})

async function loadCheatingRecords() {
  try {
    const res = await fetch(`/api/cheating_records/${classroomId}`)
    if (res.ok) {
      const records = await res.json()
      cheatingEvents.value = records.slice(-MAX_VIOLATIONS)
      violationCount.value = records.length
    }
  } catch {
    // ignore
  }
}

function formatTime(ts) {
  if (!ts) return ''
  try {
    const d = new Date(ts)
    return d.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
  } catch {
    return ts
  }
}

function startCamera() {
  navigator.mediaDevices.getUserMedia({ video: { width: 1280, height: 720 } })
    .then(s => {
      stream = s
      isStreaming.value = true
      video.value.srcObject = s
      video.value.play()
      connectWS()
      drawLoop()
    })
}

function stopCamera() {
  if (_drawLoopTimer) clearTimeout(_drawLoopTimer)
  _drawLoopTimer = null
  if (stream) stream.getTracks().forEach(t => t.stop())
  stream = null
  isStreaming.value = false
  if (ws) ws.close()
  ws = null
}

function handleUpload(file) {
  const url = URL.createObjectURL(file)
  video.value.src = url
  isStreaming.value = true
  video.value.onloadeddata = () => {
    connectWS()
    drawLoop()
  }
  video.value.play()
  return false
}

function connectWS() {
  const proto = location.protocol === 'https:' ? 'wss' : 'ws'
  ws = new WebSocket(`${proto}://${location.host}/ws/video?classroom_id=${classroomId}`)
  ws.onmessage = (e) => {
    const data = JSON.parse(e.data)

    faceCount.value = data.count

    if (data.faces.length > 0) {
      const avg = data.faces.reduce((s, f) => s + f.attention_score, 0) / data.faces.length
      avgAttention.value = Math.round(avg)
      headDownCount.value = data.faces.filter(f => Math.abs(f.pose?.pitch || 0) > 15).length
      headTurnCount.value = data.faces.filter(f => Math.abs(f.pose?.yaw || 0) > 20).length
      fatigueCount.value = data.faces.filter(f => f.fatigue?.is_blinking).length
    }
    drawResults(data.faces)
    updateChart(data)

    // 处理违规事件（限制数组长度）
    if (data.cheating_events && data.cheating_events.length > 0) {
      for (const evt of data.cheating_events) {
        cheatingEvents.value.push(evt)
        violationCount.value++
      }
      // 裁剪到最大长度，防止内存泄漏
      if (cheatingEvents.value.length > MAX_VIOLATIONS) {
        cheatingEvents.value = cheatingEvents.value.slice(-MAX_VIOLATIONS)
      }
    }
  }
}

function drawResults(faces) {
  const ctx = canvas.value.getContext('2d')
  canvas.value.width = video.value.videoWidth
  canvas.value.height = video.value.videoHeight
  ctx.clearRect(0, 0, canvas.value.width, canvas.value.height)

  faces.forEach(face => {
    const [x1, y1, x2, y2] = face.bbox
    const score = face.attention_score

    ctx.strokeStyle = score > 60 ? '#00ff00' : score > 30 ? '#ffaa00' : '#ff0000'
    ctx.lineWidth = 2
    ctx.strokeRect(x1, y1, x2 - x1, y2 - y1)
    ctx.fillStyle = ctx.strokeStyle
    ctx.font = '20px Arial'
    ctx.fillText(`ID:${face.track_id} ${score.toFixed(0)}分`, x1, y1 - 5)
  })
}

function updateChart(data) {
  const label = new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
  const value = avgAttention.value
  timelineData.push({ label, value })
  if (timelineData.length > 60) timelineData.shift()

  chart.setOption({
    xAxis: { data: timelineData.map(d => d.label) },
    series: [{ data: timelineData.map(d => d.value) }],
  })
}

function drawLoop() {
  if (!video.value.videoWidth) {
    _drawLoopTimer = setTimeout(drawLoop, 50)
    return
  }
  const now = performance.now()
  if (ws && ws.readyState === WebSocket.OPEN && now - lastSendTime >= SEND_INTERVAL) {
    // 关键：检查 WebSocket 发送缓冲区，如果有积压则跳过发送
    if (ws.bufferedAmount > 50000) {
      // 缓冲区积压超过 50KB，说明后端处理慢，跳过本帧
      _drawLoopTimer = setTimeout(drawLoop, 100)
      return
    }

    lastSendTime = now

    // 保持原始分辨率，确保画质清晰
    if (!_sendCanvas || _sendCanvas.width !== video.value.videoWidth) {
      _sendCanvas = document.createElement('canvas')
      _sendCanvas.width = video.value.videoWidth
      _sendCanvas.height = video.value.videoHeight
      _sendCtx = _sendCanvas.getContext('2d')
    }
    _sendCtx.drawImage(video.value, 0, 0)
    // 💡 优化：JPEG 质量从0.7降到0.5，减少传输量（人脸检测不依赖画质）
    ws.send(JSON.stringify({ frame: _sendCanvas.toDataURL('image/jpeg', 0.5).split(',')[1] }))
  }
  // requestAnimationFrame 保持实时性，但 bufferedAmount 检查防止积压
  requestAnimationFrame(drawLoop)
}

async function endClass() {
  endLoading.value = true
  try {
    // 先关闭 WebSocket，让后端完成 DB 保存
    stopCamera()
    // 等待 2 秒，确保后端的异步保存任务全部完成写入 DB
    await new Promise(resolve => setTimeout(resolve, 2000))

    await endClassroom(classroomId)
    generateClassroomReport(classroomId, { skipGlobalError: true }).catch(() => {})
    router.push(`/classrooms/${classroomId}`)
  } catch (e) {
    const detail = e.response?.data?.detail || ''
    if (detail.includes('已结束')) {
      stopCamera()
      router.push(`/classrooms/${classroomId}`)
    } else {
      console.error('结束课堂失败', e)
      alert('结束课堂失败: ' + (detail || e.message))
    }
  } finally {
    endLoading.value = false
  }
}
</script>

<style scoped>
.violation-list {
  max-height: 300px;
  overflow-y: auto;
}

.violation-item {
  padding: 8px;
  margin-bottom: 6px;
  background: #fff2f0;
  border: 1px solid #ffccc7;
  border-radius: 6px;
  font-size: 13px;
}

.violation-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}

.violation-track {
  color: #666;
  font-weight: 500;
}

.violation-time {
  color: #999;
  font-size: 11px;
  margin-left: auto;
}

.violation-scores {
  color: #888;
  font-size: 12px;
  display: flex;
  gap: 12px;
}
</style>
