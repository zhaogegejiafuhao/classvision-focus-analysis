<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 18px; font-weight: bold; cursor: pointer" @click="$router.push('/')">
        ClassVision 课眼智析
      </span>
      <a-button type="link" style="color: #fff" @click="$router.push('/classrooms')">返回列表</a-button>
    </a-layout-header>
    <a-layout-content style="padding: 24px">
      <a-spin :spinning="loading">
        <template v-if="classroom">
          <a-page-header :title="classroom.name" :sub-title="`${classroom.teacher} · ${classroom.duration}分钟${classroom.exam_mode ? ' · 考场模式' : ''}`" />

          <a-row :gutter="16" style="margin-bottom: 16px">
            <a-col :span="6">
              <a-card><a-statistic title="总人数" :value="classroom.total_students" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="平均注意力" :value="classroom.avg_attention" suffix="/100" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="低头人次" :value="classroom.stats?.head_down_count || 0" :value-style="{ color: '#cf1322' }" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="疲劳人次" :value="classroom.stats?.fatigue_count || 0" :value-style="{ color: '#722ed1' }" /></a-card>
            </a-col>
          </a-row>

          <!-- 出席情况 -->
          <a-card title="出席情况" style="margin-bottom: 16px">
            <a-row :gutter="16">
              <a-col :span="6">
                <a-statistic title="已识别" :value="attendance.identified_count" :value-style="{ color: '#52c41a' }" />
              </a-col>
              <a-col :span="6">
                <a-statistic title="未识别" :value="attendance.unidentified_count" :value-style="{ color: '#faad14' }" />
              </a-col>
              <a-col :span="6">
                <a-statistic title="缺席（已注册）" :value="attendance.absent_count" :value-style="{ color: '#cf1322' }" />
              </a-col>
              <a-col :span="6">
                <a-button type="link" @click="showAttendanceModal = true">查看详情</a-button>
              </a-col>
            </a-row>
          </a-card>

          <!-- 考场模式：风险分布饼图 -->
          <template v-if="classroom.exam_mode">
            <a-card title="风险等级分布" style="margin-bottom: 16px">
              <div ref="riskChartEl" style="width: 100%; height: 300px" />
            </a-card>
          </template>
          <!-- 普通模式：注意力趋势 -->
          <template v-else>
            <a-card title="注意力趋势" style="margin-bottom: 16px">
              <div ref="timelineEl" style="width: 100%; height: 300px" />
            </a-card>
          </template>

          <!-- 热力图 -->
          <a-card title="学生注意力热力图" style="margin-bottom: 16px">
            <a-alert message="热力图显示每个学生在不同时间段的注意力分布，颜色越绿表示注意力越高" type="info" show-icon style="margin-bottom: 12px" />
            <div ref="heatmapEl" style="width: 100%; height: 400px" />
          </a-card>

          <a-row :gutter="16">
            <a-col :span="12">
              <a-card title="学生列表">
                <a-table :columns="studentCols" :data-source="students" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'risk_level'">
                      <a-tag :color="record.risk_level === 'high' ? 'red' : record.risk_level === 'medium' ? 'orange' : 'green'">
                        {{ { low: '低风险', medium: '中风险', high: '高风险' }[record.risk_level] || '低风险' }}
                      </a-tag>
                    </template>
                  </template>
                </a-table>
              </a-card>
            </a-col>
            <a-col :span="12">
              <!-- AI 报告 -->
              <a-card title="AI 课堂分析报告">
                <div v-if="report">
                  <div v-html="renderMarkdown(report?.content)" style="max-height: 300px; overflow-y: auto" />
                  <a-typography-text type="secondary">
                    生成时间：{{ new Date(report.created_at).toLocaleString('zh-CN') }}
                  </a-typography-text>
                </div>
                <a-empty v-else description="尚未生成报告">
                  <a-button type="primary" @click="genReport" :loading="genLoading">生成报告</a-button>
                </a-empty>
              </a-card>

              <!-- 对话区域 -->
              <a-card title="AI 智能对话" style="margin-top: 16px">
                <a-alert
                  message="AI 已接入知识库（RAG），自动检索相关文档辅助回答，您可以追问细节或请求更多建议"
                  type="info"
                  show-icon
                  style="margin-bottom: 12px"
                />
                <!-- 对话历史 -->
                <div v-if="chatMessages.length > 0" style="max-height: 400px; overflow-y: auto; margin-bottom: 16px">
                  <div v-for="msg in chatMessages" :key="msg.id" style="margin-bottom: 12px">
                    <a-tag :color="msg.role === 'user' ? 'blue' : 'green'">
                      {{ msg.role === 'user' ? '用户' : 'AI' }}
                    </a-tag>
                    <span style="margin-left: 8px; font-size: 12px; color: #999">
                      {{ new Date(msg.timestamp).toLocaleTimeString('zh-CN') }}
                    </span>
                    <div style="margin-top: 4px; padding: 8px; background: #f5f5f5; border-radius: 4px">
                      <div v-if="msg.streaming && !msg.content" style="color: #999">
                        <a-spin size="small" /> 正在检索知识库并生成回答...
                      </div>
                      <div class="markdown-body" v-html="renderMarkdown(msg.content)" />
                      <span v-if="msg.streaming && msg.content" class="streaming-cursor">▌</span>
                    </div>
                  </div>
                </div>
                <a-empty v-else description="暂无对话记录" style="margin-bottom: 16px" />

                <!-- 输入框 -->
                <a-space style="width: 100%">
                  <a-input
                    v-model:value="chatInput"
                    placeholder="输入问题，如：为什么疲劳人次这么高？"
                    style="flex: 1"
                    :disabled="chatLoading"
                  />
                  <a-button type="primary" @click="sendChat" :loading="chatLoading" :disabled="!chatInput.trim()">
                    发送
                  </a-button>
                </a-space>

                <!-- 下载按钮 -->
                <a-space style="margin-top: 12px">
                  <a-button @click="downloadMarkdown" :disabled="chatMessages.length === 0 && !report">
                    下载完整报告（含对话记录）
                  </a-button>
                </a-space>
              </a-card>
            </a-col>
          </a-row>
        </template>
      </a-spin>

      <!-- 出席详情弹窗 -->
      <a-modal v-model:open="showAttendanceModal" title="出席详情" width="800px" :footer="null">
        <a-tabs>
          <a-tab-pane key="identified" tab="已识别">
            <a-table :data-source="attendance.identified" :columns="[
              { title: '姓名', dataIndex: 'name' },
              { title: '平均注意力', dataIndex: 'avg_attention' },
            ]" row-key="student_id" size="small" />
          </a-tab-pane>
          <a-tab-pane key="unidentified" tab="未识别">
            <a-table :data-source="attendance.unidentified" :columns="[
              { title: '跟踪ID', dataIndex: 'track_id' },
              { title: '平均注意力', dataIndex: 'avg_attention' },
            ]" row-key="student_id" size="small" />
          </a-tab-pane>
          <a-tab-pane key="absent" tab="缺席（已注册）">
            <a-table :data-source="attendance.absent" :columns="[
              { title: '姓名', dataIndex: 'name' },
            ]" row-key="id" size="small" />
          </a-tab-pane>
        </a-tabs>
      </a-modal>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import * as echarts from 'echarts'
import axios from 'axios'
import { marked } from 'marked'

const route = useRoute()
const classroomId = route.params.id

const classroom = ref(null)
const students = ref([])
const report = ref(null)
const loading = ref(true)
const genLoading = ref(false)
const timelineEl = ref(null)
const riskChartEl = ref(null)
const heatmapEl = ref(null)

// 出席情况
const attendance = ref({
  identified_count: 0,
  unidentified_count: 0,
  absent_count: 0,
  identified: [],
  unidentified: [],
  absent: [],
})
const showAttendanceModal = ref(false)

// 对话相关
const chatMessages = ref([])
const chatInput = ref('')
const chatLoading = ref(false)

const studentCols = computed(() => {
  const base = [
    { title: '姓名', dataIndex: 'name', key: 'name' },
    { title: '平均注意力', dataIndex: 'avg_attention', key: 'avg_attention' },
    { title: '低头人次', dataIndex: 'head_down_count', key: 'head_down_count' },
    { title: '眨眼次数', dataIndex: 'blink_count', key: 'blink_count' },
  ]
  if (classroom.value?.exam_mode) {
    base.push({ title: '风险等级', dataIndex: 'risk_level', key: 'risk_level' })
  }
  return base
})

function renderMarkdown(text) {
  if (!text) return ''
  return marked.parse(text, { breaks: true })
}

async function genReport() {
  genLoading.value = true
  try {
    const res = await axios.post(`/api/classrooms/${classroomId}/report`)
    report.value = res.data
  } finally {
    genLoading.value = false
  }
}

async function loadChatHistory() {
  try {
    const res = await axios.get(`/api/classrooms/${classroomId}/chat/history`)
    chatMessages.value = res.data || []
  } catch {
    chatMessages.value = []
  }
}

async function loadAttendance() {
  try {
    const res = await axios.get(`/api/classrooms/${classroomId}/attendance`)
    attendance.value = res.data
  } catch {
    // 忽略错误
  }
}

async function loadHeatmap() {
  try {
    const res = await axios.get(`/api/classrooms/${classroomId}/heatmap`)
    if (res.data.time_labels.length === 0) return

    const chart = echarts.init(heatmapEl.value)
    const heatmapSeriesData = []
    res.data.heatmap_data.forEach((row, yIndex) => {
      row.data.forEach((value, xIndex) => {
        heatmapSeriesData.push([xIndex, yIndex, value])
      })
    })

    chart.setOption({
      tooltip: {
        position: 'top',
        formatter: (params) => {
          const student = res.data.heatmap_data[params.data[1]]
          const time = res.data.time_labels[params.data[0]]
          return `${student.student_name}<br/>时间: ${time}<br/>注意力: ${params.data[2]}`
        },
      },
      grid: { top: 50, bottom: 30, left: 100, right: 20 },
      xAxis: {
        type: 'category',
        data: res.data.time_labels,
        splitArea: { show: true },
      },
      yAxis: {
        type: 'category',
        data: res.data.heatmap_data.map(d => d.student_name),
        splitArea: { show: true },
      },
      visualMap: {
        min: 0,
        max: 100,
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        bottom: 0,
        inRange: {
          color: ['#cf1322', '#faad14', '#52c41a'],
        },
      },
      series: [{
        type: 'heatmap',
        data: heatmapSeriesData,
        label: { show: false },
        emphasis: {
          itemStyle: { shadowBlur: 10, shadowColor: 'rgba(0, 0, 0, 0.5)' },
        },
      }],
    })
  } catch {
    // 忽略错误
  }
}

async function sendChat() {
  if (!chatInput.value.trim()) return
  const userText = chatInput.value
  chatInput.value = ''

  // 先展示用户消息
  chatMessages.value.push({
    id: 'tmp-user-' + Date.now(),
    role: 'user',
    content: userText,
    timestamp: new Date().toISOString(),
  })
  // AI 占位消息，逐字填充
  chatMessages.value.push({
    id: 'tmp-ai-' + Date.now(),
    role: 'assistant',
    content: '',
    timestamp: new Date().toISOString(),
    streaming: true,
  })
  const aiIdx = chatMessages.value.length - 1
  chatLoading.value = true

  try {
    const resp = await fetch(`/api/classrooms/${classroomId}/chat/stream`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: userText }),
    })
    if (!resp.ok) throw new Error('HTTP ' + resp.status)
    const reader = resp.body.getReader()
    const decoder = new TextDecoder()
    let buffer = ''
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      buffer += decoder.decode(value, { stream: true })
      const lines = buffer.split('\n')
      buffer = lines.pop()
      for (const line of lines) {
        if (!line.startsWith('data: ')) continue
        let data
        try { data = JSON.parse(line.slice(6)) } catch { continue }
        if (data.delta) {
          chatMessages.value[aiIdx].content += data.delta
        }
        if (data.done) {
          chatMessages.value[aiIdx].id = data.id
          chatMessages.value[aiIdx].streaming = false
        }
        if (data.error) {
          chatMessages.value[aiIdx].content += '\n\n[生成失败: ' + data.error + ']'
          chatMessages.value[aiIdx].streaming = false
        }
      }
    }
  } catch (e) {
    chatMessages.value[aiIdx].content += '\n\n[请求失败: ' + e.message + ']'
    chatMessages.value[aiIdx].streaming = false
    console.error('对话失败', e)
  } finally {
    chatLoading.value = false
  }
}

async function downloadMarkdown() {
  try {
    const res = await axios.get(`/api/classrooms/${classroomId}/chat/export`, {
      responseType: 'blob',
    })
    const blob = new Blob([res.data], { type: 'text/markdown' })
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `${classroom.value?.name || '课堂'}_完整分析报告.md`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  } catch (e) {
    console.error('下载失败', e)
  }
}

onMounted(async () => {
  try {
    const [classRes, studentRes, timelineRes] = await Promise.all([
      axios.get(`/api/classrooms/${classroomId}`),
      axios.get(`/api/classrooms/${classroomId}/students`),
      axios.get(`/api/classrooms/${classroomId}/timeline`),
    ])
    classroom.value = classRes.data
    students.value = studentRes.data

    await nextTick()

    if (classRes.data.exam_mode) {
      const rd = classRes.data.stats?.risk_distribution || {}
      const riskChart = echarts.init(riskChartEl.value)
      riskChart.setOption({
        tooltip: { trigger: 'item' },
        legend: { bottom: 0 },
        series: [{
          type: 'pie',
          radius: ['40%', '70%'],
          data: [
            { value: rd.low || 0, name: '低风险', itemStyle: { color: '#52c41a' } },
            { value: rd.medium || 0, name: '中风险', itemStyle: { color: '#fa8c16' } },
            { value: rd.high || 0, name: '高风险', itemStyle: { color: '#cf1322' } },
          ],
        }],
      })
    } else {
      const chart = echarts.init(timelineEl.value)
      chart.setOption({
        grid: { top: 20, bottom: 30, left: 50, right: 20 },
        xAxis: { type: 'category', data: timelineRes.data.map(d => d.timestamp) },
        yAxis: { type: 'value', max: 100, min: 0, name: '注意力' },
        series: [{
          type: 'line', data: timelineRes.data.map(d => d.avg_attention),
          smooth: true, areaStyle: { opacity: 0.2 }, itemStyle: { color: '#1890ff' },
        }],
      })
    }

    // 加载热力图
    await loadHeatmap()

    // 加载出席情况
    await loadAttendance()

    try {
      const reportRes = await axios.get(`/api/classrooms/${classroomId}/report`)
      report.value = reportRes.data
    } catch { /* 报告未生成 */ }

    // 加载对话历史
    await loadChatHistory()
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.markdown-body :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 8px 0;
}
.markdown-body :deep(th),
.markdown-body :deep(td) {
  border: 1px solid #d9d9d9;
  padding: 6px 12px;
  text-align: left;
}
.markdown-body :deep(pre) {
  background: #f0f0f0;
  padding: 12px;
  border-radius: 4px;
  overflow-x: auto;
}
.markdown-body :deep(code) {
  background: #f0f0f0;
  padding: 2px 4px;
  border-radius: 3px;
  font-family: Consolas, Monaco, monospace;
  font-size: 0.9em;
}
.markdown-body :deep(pre code) {
  background: none;
  padding: 0;
}
.streaming-cursor {
  display: inline-block;
  animation: blink 1s step-end infinite;
  color: #52c41a;
  font-weight: bold;
}
@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}
</style>