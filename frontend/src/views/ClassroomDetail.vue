<template>
  <div class="cv-page" style="max-width: 1400px">
      <a-spin :spinning="loading">
        <a-skeleton v-if="loading && !classroom" active :paragraph="{ rows: 4 }" />
        <template v-if="classroom">
          <div class="page-header-wrap">
            <a-page-header :title="classroom.name" :sub-title="`${classroom.teacher} · ${classroom.duration}分钟${classroom.exam_mode ? ' · 考场模式' : ''}`" style="padding: 0 0 16px 0" />
            <a-space v-if="canEditOrDelete || canManage">
              <a-button v-if="!classroom.ended_at && canManage" @click="endClassroom" :loading="endLoading">
                <template #icon><CheckCircleOutlined /></template>
                结束课堂
              </a-button>
              <a-button v-if="canEditOrDelete" @click="openEditClassroom">
                <template #icon><EditOutlined /></template>
                编辑课堂
              </a-button>
              <a-popconfirm v-if="canEditOrDelete" title="确定删除该课堂？将同时删除所有关联数据（学生、记录、报告等）。" @confirm="deleteClassroom">
                <a-button danger>
                  <template #icon><DeleteOutlined /></template>
                  删除课堂
                </a-button>
              </a-popconfirm>
            </a-space>
          </div>

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
                <template #extra>
                  <a-button v-if="canManage" type="primary" size="small" @click="openAddStudent">
                    <template #icon><PlusOutlined /></template>
                    添加学生
                  </a-button>
                </template>
                <a-table :columns="studentCols" :data-source="students" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'risk_level'">
                      <a-tag :color="record.risk_level === 'high' ? 'red' : record.risk_level === 'medium' ? 'orange' : 'green'">
                        {{ { low: '低风险', medium: '中风险', high: '高风险' }[record.risk_level] || '低风险' }}
                      </a-tag>
                    </template>
                    <template v-if="column.key === 'action'">
                      <a-space>
                        <a-button type="link" size="small" @click="openEditStudent(record)">编辑</a-button>
                        <a-popconfirm title="确定删除该学生？将同时删除其注意力记录。" @confirm="deleteStudent(record.id)">
                          <a-button type="link" danger size="small">删除</a-button>
                        </a-popconfirm>
                      </a-space>
                    </template>
                  </template>
                </a-table>
              </a-card>
            </a-col>
            <a-col :span="12">
              <!-- AI 报告 -->
              <a-card title="AI 课堂分析报告">
                <template #extra>
                  <a-space v-if="report && canManage" size="small">
                    <a-popconfirm title="确定重新生成报告？将覆盖当前内容。" @confirm="genReport(true)">
                      <a-button type="link" size="small" :loading="genLoading">
                        <template #icon><ReloadOutlined /></template>
                        重新生成
                      </a-button>
                    </a-popconfirm>
                    <a-popconfirm title="确定删除该报告？" @confirm="deleteReport">
                      <a-button type="link" danger size="small">
                        <template #icon><DeleteOutlined /></template>
                        删除
                      </a-button>
                    </a-popconfirm>
                  </a-space>
                </template>
                <div v-if="report">
                  <div v-html="renderMarkdown(report?.content)" style="max-height: 300px; overflow-y: auto" />
                  <a-typography-text type="secondary">
                    生成时间：{{ new Date(report.created_at).toLocaleString('zh-CN') }}
                  </a-typography-text>
                </div>
                <a-empty v-else description="尚未生成报告">
                  <a-button v-if="canManage" type="primary" @click="genReport()" :loading="genLoading">生成报告</a-button>
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
        <a-empty v-else-if="!loading" description="课堂不存在" />
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

      <!-- 编辑课堂弹窗 -->
      <a-modal
        v-model:open="editClassroomOpen"
        title="编辑课堂信息"
        @ok="handleEditClassroom"
        :confirm-loading="editClassroomSaving"
        ok-text="保存"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="课堂名称">
            <a-input v-model:value="editClassroomForm.name" />
          </a-form-item>
          <a-form-item label="教师">
            <a-input v-model:value="editClassroomForm.teacher" />
          </a-form-item>
          <a-form-item label="考场模式">
            <a-switch v-model:checked="editClassroomForm.exam_mode" />
          </a-form-item>
        </a-form>
      </a-modal>

      <!-- 添加学生弹窗 -->
      <a-modal
        v-model:open="addStudentOpen"
        title="添加学生"
        @ok="handleAddStudent"
        :confirm-loading="addStudentSaving"
        ok-text="添加"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="跟踪ID" required>
            <a-input-number v-model:value="addStudentForm.track_id" :min="1" style="width: 100%" />
          </a-form-item>
          <a-form-item label="姓名">
            <a-input v-model:value="addStudentForm.name" placeholder="可选" />
          </a-form-item>
        </a-form>
      </a-modal>

      <!-- 编辑学生弹窗 -->
      <a-modal
        v-model:open="editStudentOpen"
        title="编辑学生"
        @ok="handleEditStudent"
        :confirm-loading="editStudentSaving"
        ok-text="保存"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="姓名">
            <a-input v-model:value="editStudentForm.name" />
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import * as echarts from 'echarts'
import api from '@/api'
import { message } from 'ant-design-vue'
import MarkdownIt from 'markdown-it'
import {
  CheckCircleOutlined, EditOutlined, DeleteOutlined,
  PlusOutlined, ReloadOutlined,
} from '@ant-design/icons-vue'

const md = new MarkdownIt({ html: false, breaks: true, linkify: true })

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const classroomId = route.params.id

const canManage = computed(() => ['teacher', 'admin'].includes(userStore.role))
const canEditOrDelete = computed(() => {
  if (!classroom.value) return false
  if (userStore.role === 'admin') return true
  return classroom.value.teacher_person_id === userStore.user?.id
})

const classroom = ref(null)
const students = ref([])
const report = ref(null)
const loading = ref(true)
const genLoading = ref(false)
const endLoading = ref(false)
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
  if (canManage.value) {
    base.push({ title: '操作', key: 'action' })
  }
  return base
})

function renderMarkdown(text) {
  if (!text) return ''
  return md.render(text)
}

// ===== 课堂操作 =====
async function endClassroom() {
  endLoading.value = true
  try {
    await api.put(`/classrooms/${classroomId}/end`)
    message.success('课堂已结束')
    await loadClassroom()
  } catch (e) {
    message.error(e.response?.data?.detail || '结束课堂失败')
  } finally {
    endLoading.value = false
  }
}

async function deleteClassroom() {
  try {
    await api.delete(`/classrooms/${classroomId}`)
    message.success('课堂已删除')
    router.push('/classrooms')
  } catch (e) {
    message.error(e.response?.data?.detail || '删除课堂失败')
  }
}

// 编辑课堂
const editClassroomOpen = ref(false)
const editClassroomSaving = ref(false)
const editClassroomForm = ref({ name: '', teacher: '', exam_mode: false })

function openEditClassroom() {
  editClassroomForm.value = {
    name: classroom.value.name || '',
    teacher: classroom.value.teacher || '',
    exam_mode: classroom.value.exam_mode || false,
  }
  editClassroomOpen.value = true
}

async function handleEditClassroom() {
  editClassroomSaving.value = true
  try {
    await api.put(`/classrooms/${classroomId}`, editClassroomForm.value)
    message.success('课堂信息已更新')
    editClassroomOpen.value = false
    await loadClassroom()
  } catch (e) {
    message.error(e.response?.data?.detail || '更新失败')
  } finally {
    editClassroomSaving.value = false
  }
}

// ===== 学生管理 =====
const addStudentOpen = ref(false)
const addStudentSaving = ref(false)
const addStudentForm = ref({ track_id: 1, name: '' })

function openAddStudent() {
  const maxTrackId = students.value.length > 0
    ? Math.max(...students.value.map(s => s.track_id || 0)) + 1
    : 1
  addStudentForm.value = { track_id: maxTrackId, name: '' }
  addStudentOpen.value = true
}

async function handleAddStudent() {
  addStudentSaving.value = true
  try {
    await api.post(`/classrooms/${classroomId}/students`, {
      classroom_id: Number(classroomId),
      track_id: addStudentForm.value.track_id,
      name: addStudentForm.value.name || null,
    })
    message.success('学生已添加')
    addStudentOpen.value = false
    await loadStudents()
  } catch (e) {
    message.error(e.response?.data?.detail || '添加学生失败')
  } finally {
    addStudentSaving.value = false
  }
}

const editStudentOpen = ref(false)
const editStudentSaving = ref(false)
const editStudentForm = ref({ id: null, name: '' })

function openEditStudent(record) {
  editStudentForm.value = { id: record.id, name: record.name || '' }
  editStudentOpen.value = true
}

async function handleEditStudent() {
  editStudentSaving.value = true
  try {
    await api.put(`/classrooms/${classroomId}/students/${editStudentForm.value.id}`, {
      name: editStudentForm.value.name,
    })
    message.success('学生信息已更新')
    editStudentOpen.value = false
    await loadStudents()
  } catch (e) {
    message.error(e.response?.data?.detail || '更新学生失败')
  } finally {
    editStudentSaving.value = false
  }
}

async function deleteStudent(studentId) {
  try {
    await api.delete(`/classrooms/${classroomId}/students/${studentId}`)
    message.success('学生已删除')
    await loadStudents()
  } catch (e) {
    message.error(e.response?.data?.detail || '删除学生失败')
  }
}

// ===== 报告操作 =====
async function genReport(force = false) {
  genLoading.value = true
  try {
    const url = force
      ? `/classrooms/${classroomId}/report?force=true`
      : `/classrooms/${classroomId}/report`
    const res = await api.post(url)
    report.value = res.data
    message.success(force ? '报告已重新生成' : '报告生成成功')
  } catch (e) {
    message.error(e.response?.data?.detail || '报告生成失败')
  } finally {
    genLoading.value = false
  }
}

async function deleteReport() {
  try {
    await api.delete(`/classrooms/${classroomId}/report`)
    report.value = null
    message.success('报告已删除')
  } catch (e) {
    message.error(e.response?.data?.detail || '删除报告失败')
  }
}

// ===== 数据加载 =====
async function loadClassroom() {
  try {
    const res = await api.get(`/classrooms/${classroomId}`)
    classroom.value = res.data
  } catch (e) {
    message.error('加载课堂信息失败')
  }
}

async function loadStudents() {
  try {
    const res = await api.get(`/classrooms/${classroomId}/students`)
    students.value = res.data
  } catch (e) {
    message.error('加载学生列表失败')
  }
}

async function loadChatHistory() {
  try {
    const res = await api.get(`/classrooms/${classroomId}/chat/history`)
    chatMessages.value = res.data || []
  } catch {
    chatMessages.value = []
  }
}

async function loadAttendance() {
  try {
    const res = await api.get(`/classrooms/${classroomId}/attendance`)
    attendance.value = res.data
  } catch {
    // 忽略
  }
}

async function loadHeatmap() {
  try {
    const res = await api.get(`/classrooms/${classroomId}/heatmap`)
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
    // 忽略
  }
}

async function sendChat() {
  if (!chatInput.value.trim()) return
  const userText = chatInput.value
  chatInput.value = ''

  chatMessages.value.push({
    id: 'tmp-user-' + Date.now(),
    role: 'user',
    content: userText,
    timestamp: new Date().toISOString(),
  })
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
    const token = userStore.token || localStorage.getItem('token') || ''
    const resp = await fetch(`/api/classrooms/${classroomId}/chat/stream`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
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
    message.error('对话请求失败')
  } finally {
    chatLoading.value = false
  }
}

async function downloadMarkdown() {
  try {
    const res = await api.get(`/classrooms/${classroomId}/chat/export`, {
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
    message.error('下载报告失败')
  }
}

onMounted(async () => {
  try {
    const [classRes, studentRes, timelineRes] = await Promise.all([
      api.get(`/classrooms/${classroomId}`),
      api.get(`/classrooms/${classroomId}/students`),
      api.get(`/classrooms/${classroomId}/timeline`),
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

    await loadHeatmap()
    await loadAttendance()

    try {
      const reportRes = await api.get(`/classrooms/${classroomId}/report`)
      report.value = reportRes.data
    } catch { /* 报告未生成 */ }

    await loadChatHistory()
  } catch (e) {
    message.error('加载课堂数据失败')
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.page-header-wrap {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.markdown-body {
  font-size: 14px;
  line-height: 1.7;
  color: var(--cv-text-secondary, #475569);
}

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
