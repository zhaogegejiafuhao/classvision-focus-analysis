<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 18px; font-weight: bold">
        {{ isExamMode ? '考场监控' : '实时检测' }} — {{ classroomName }}
      </span>
      <a-space>
        <a-button type="primary" danger @click="endClass" :disabled="!isStreaming">结束课堂</a-button>
      </a-space>
    </a-layout-header>
    <a-layout-content style="padding: 16px">
      <a-alert
        v-if="highRiskAlertVisible"
        type="error"
        show-icon
        closable
        :message="`高风险预警: 学生 ID ${highRiskTrackIds.join(', ')} 存在持续异常行为`"
        style="margin-bottom: 12px"
        @close="highRiskAlertVisible = false"
      />
      <a-row :gutter="16">
        <a-col :span="16">
          <a-card :title="isExamMode ? '考场画面' : '实时画面'" :bordered="false">
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
          <!-- 考场模式看板 -->
          <template v-if="isExamMode">
            <a-card title="考场风险看板" :bordered="false">
              <a-statistic title="检测人数" :value="faceCount" />
              <a-row :gutter="8" style="margin-top: 16px">
                <a-col :span="8">
                  <a-statistic title="低风险" :value="lowRiskCount" :value-style="{ color: '#52c41a' }" />
                </a-col>
                <a-col :span="8">
                  <a-statistic title="中风险" :value="mediumRiskCount" :value-style="{ color: '#fa8c16' }" />
                </a-col>
                <a-col :span="8">
                  <a-statistic title="高风险" :value="highRiskCount" :value-style="{ color: '#cf1322' }" />
                </a-col>
              </a-row>
              <div ref="chartEl" style="width: 100%; height: 200px; margin-top: 16px" />
            </a-card>
          </template>
          <!-- 普通模式看板 -->
          <template v-else>
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
          </template>
        </a-col>
      </a-row>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import * as echarts from 'echarts'
import axios from 'axios'

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

const isExamMode = ref(false)
const lowRiskCount = ref(0)
const mediumRiskCount = ref(0)
const highRiskCount = ref(0)
const highRiskAlertVisible = ref(false)
const highRiskTrackIds = ref([])
const lastAlertTime = ref({})

let ws = null
let chart = null
let stream = null
let timelineData = []
let lastSendTime = 0
const SEND_INTERVAL = 200

const isStreaming = ref(false)

onMounted(async () => {
  const res = await axios.get(`/api/classrooms/${classroomId}`)
  classroomName.value = res.data.name
  isExamMode.value = res.data.exam_mode || false

  chart = echarts.init(chartEl.value)
  chart.setOption({
    title: { text: isExamMode.value ? '风险趋势' : '注意力趋势', textStyle: { fontSize: 13 } },
    grid: { top: 30, bottom: 20, left: 40, right: 10 },
    xAxis: { type: 'category', data: [] },
    yAxis: { type: 'value', max: isExamMode.value ? undefined : 100, min: 0 },
    series: [{ type: 'line', data: [], smooth: true, areaStyle: { opacity: 0.15 }, itemStyle: { color: isExamMode.value ? '#ff4d4f' : '#1890ff' } }],
  })
})

onUnmounted(() => {
  stopCamera()
  if (chart) chart.dispose()
})

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
    isExamMode.value = data.exam_mode || false

    if (isExamMode.value) {
      const risks = data.faces.map(f => f.exam_risk?.risk_level || 'low')
      lowRiskCount.value = risks.filter(r => r === 'low').length
      mediumRiskCount.value = risks.filter(r => r === 'medium').length
      highRiskCount.value = risks.filter(r => r === 'high').length

      // 高风险弹窗（5秒内同一 ID 不重复）
      const now = Date.now()
      const highIds = data.faces
        .filter(f => f.exam_risk?.risk_level === 'high')
        .map(f => f.track_id)
        .filter(id => !lastAlertTime.value[id] || now - lastAlertTime.value[id] > 5000)
      if (highIds.length > 0) {
        highRiskTrackIds.value = highIds
        highRiskAlertVisible.value = true
        highIds.forEach(id => { lastAlertTime.value[id] = now })
        setTimeout(() => { highRiskAlertVisible.value = false }, 5000)
      }
    } else if (data.faces.length > 0) {
      const avg = data.faces.reduce((s, f) => s + f.attention_score, 0) / data.faces.length
      avgAttention.value = Math.round(avg)
      headDownCount.value = data.faces.filter(f => Math.abs(f.pose?.pitch || 0) > 15).length
      headTurnCount.value = data.faces.filter(f => Math.abs(f.pose?.yaw || 0) > 20).length
      fatigueCount.value = data.faces.filter(f => f.fatigue?.is_blinking).length
    }
    drawResults(data.faces)
    updateChart(data)
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

    if (isExamMode.value && face.exam_risk) {
      const risk = face.exam_risk.risk_level
      const riskColors = { low: '#52c41a', medium: '#fa8c16', high: '#cf1322' }
      const riskLabels = { low: '低风险', medium: '中风险', high: '高风险' }
      ctx.strokeStyle = riskColors[risk] || '#52c41a'
      ctx.lineWidth = risk === 'high' ? 4 : 2
      ctx.strokeRect(x1, y1, x2 - x1, y2 - y1)
      ctx.fillStyle = riskColors[risk]
      ctx.font = '20px Arial'
      ctx.fillText(`ID:${face.track_id} ${riskLabels[risk]}`, x1, y1 - 5)
    } else {
      ctx.strokeStyle = score > 60 ? '#00ff00' : score > 30 ? '#ffaa00' : '#ff0000'
      ctx.lineWidth = 2
      ctx.strokeRect(x1, y1, x2 - x1, y2 - y1)
      ctx.fillStyle = ctx.strokeStyle
      ctx.font = '20px Arial'
      ctx.fillText(`ID:${face.track_id} ${score.toFixed(0)}分`, x1, y1 - 5)
    }
  })
}

function updateChart(data) {
  const label = new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
  const value = isExamMode.value ? highRiskCount.value : avgAttention.value
  timelineData.push({ label, value })
  if (timelineData.length > 60) timelineData.shift()

  chart.setOption({
    xAxis: { data: timelineData.map(d => d.label) },
    series: [{ data: timelineData.map(d => d.value) }],
  })
}

function drawLoop() {
  if (!video.value.videoWidth) {
    requestAnimationFrame(drawLoop)
    return
  }
  const now = performance.now()
  if (ws && ws.readyState === WebSocket.OPEN && now - lastSendTime >= SEND_INTERVAL) {
    lastSendTime = now
    const c = document.createElement('canvas')
    c.width = video.value.videoWidth
    c.height = video.value.videoHeight
    c.getContext('2d').drawImage(video.value, 0, 0)
    ws.send(JSON.stringify({ frame: c.toDataURL('image/jpeg', 0.7).split(',')[1] }))
  }
  requestAnimationFrame(drawLoop)
}

async function endClass() {
  await axios.put(`/api/classrooms/${classroomId}/end`)
  stopCamera()
  router.push(`/classrooms/${classroomId}`)
}
</script>
