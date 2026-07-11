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

          <!-- 考场模式：风险分布饼图 + 时间线 + 风险记录 -->
          <template v-if="classroom.exam_mode">
            <a-row :gutter="16" style="margin-bottom: 16px">
              <a-col :span="12">
                <a-card title="风险等级分布">
                  <div ref="riskChartEl" style="width: 100%; height: 300px" />
                </a-card>
              </a-col>
              <a-col :span="12">
                <a-card title="风险趋势时间线">
                  <div ref="riskTimelineEl" style="width: 100%; height: 300px" />
                </a-card>
              </a-col>
            </a-row>

            <a-card title="作弊风险详情" style="margin-bottom: 16px">
              <template #extra>
                <a-select v-model:value="riskFilter" style="width: 120px" allow-clear placeholder="风险等级" @change="loadExamRisks">
                  <a-select-option value="high">高风险</a-select-option>
                  <a-select-option value="medium">中风险</a-select-option>
                  <a-select-option value="low">低风险</a-select-option>
                </a-select>
              </template>
              <a-table
                :columns="riskColumns"
                :data-source="examRisks"
                :loading="riskLoading"
                row-key="id"
                size="small"
                :pagination="{ pageSize: 10, showSizeChanger: true }"
              >
                <template #bodyCell="{ column, record }">
                  <template v-if="column.key === 'risk_level'">
                    <a-tag :color="record.risk_level === 'high' ? 'red' : record.risk_level === 'medium' ? 'orange' : 'green'">
                      {{ { low: '低风险', medium: '中风险', high: '高风险' }[record.risk_level] || record.risk_level }}
                    </a-tag>
                  </template>
                  <template v-if="column.key === 'cheating_object_nearby'">
                    <a-tag :color="record.cheating_object_nearby ? 'red' : 'green'">
                      {{ record.cheating_object_nearby ? '检测到' : '无' }}
                    </a-tag>
                  </template>
                  <template v-if="column.key === 'gaze_deviation_duration'">
                    {{ record.gaze_deviation_duration.toFixed(1) }}s
                  </template>
                  <template v-if="column.key === 'head_down_duration'">
                    {{ record.head_down_duration.toFixed(1) }}s
                  </template>
                  <template v-if="column.key === 'timestamp'">
                    {{ new Date(record.timestamp).toLocaleString('zh-CN') }}
                  </template>
                </template>
              </a-table>
            </a-card>

            <!-- 高风险学生汇总 -->
            <a-card title="高风险学生汇总" style="margin-bottom: 16px" v-if="highRiskSummary.length > 0">
              <a-row :gutter="16">
                <a-col :span="8" v-for="item in highRiskSummary" :key="item.student_id">
                  <a-card size="small" style="margin-bottom: 8px" :style="{ borderLeft: item.risk_level === 'high' ? '3px solid #cf1322' : item.risk_level === 'medium' ? '3px solid #fa8c16' : '3px solid #52c41a' }">
                    <a-statistic :title="item.student_name" :value="item.total_events" suffix="次风险事件" />
                    <div style="margin-top: 8px">
                      <a-tag v-if="item.has_cheating_object" color="red">疑似作弊物品</a-tag>
                      <a-tag color="orange">视线偏移 {{ item.total_gaze.toFixed(1) }}s</a-tag>
                      <a-tag color="purple">低头 {{ item.total_head_down.toFixed(1) }}s</a-tag>
                      <a-tag color="blue">转头 {{ item.total_head_turn }}次</a-tag>
                    </div>
                  </a-card>
                </a-col>
              </a-row>
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
        title="添加学生到课堂"
        @ok="handleAddStudent"
        :confirm-loading="addStudentSaving"
        ok-text="添加"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="选择已注册人员" v-if="availablePersons.length > 0">
            <a-select
              v-model:value="addStudentForm.person_id"
              placeholder="选择已注册学生加入课堂"
              show-search
              :filter-option="filterPerson"
              allow-clear
              style="width: 100%"
            >
              <a-select-option v-for="p in availablePersons" :key="p.id" :value="p.id">
                {{ p.name }} ({{ p.username || 'ID:' + p.id }})
              </a-select-option>
            </a-select>
          </a-form-item>
          <a-alert v-else message="暂无可添加的已注册学生，请先到人员管理页面注册" type="info" show-icon style="margin-bottom: 12px" />
          <a-divider v-if="addStudentForm.person_id">或手动填写</a-divider>
          <a-form-item label="跟踪ID" :required="!addStudentForm.person_id">
            <a-input-number v-model:value="addStudentForm.track_id" :min="1" style="width: 100%" :disabled="!!addStudentForm.person_id" />
          </a-form-item>
          <a-form-item label="姓名">
            <a-input v-model:value="addStudentForm.name" placeholder="可选，选择已注册人员时自动填充" />
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
const riskTimelineEl = ref(null)
const heatmapEl = ref(null)

// 考试风险记录
const examRisks = ref([])
const riskLoading = ref(false)
const riskFilter = ref(undefined)
const riskColumns = [
  { title: '学生', dataIndex: 'student_name', key: 'student_name', width: 100 },
  { title: '风险等级', key: 'risk_level', width: 100 },
  { title: '视线偏移时长', key: 'gaze_deviation_duration', width: 120 },
  { title: '低头时长', key: 'head_down_duration', width: 100 },
  { title: '转头次数', dataIndex: 'head_turn_events', key: 'head_turn_events', width: 100 },
  { title: '作弊物品', key: 'cheating_object_nearby', width: 100 },
  { title: '注意力', dataIndex: 'attention_score', key: 'attention_score', width: 80 },
  { title: '时间', key: 'timestamp', width: 180 },
]

const highRiskSummary = computed(() => {
  if (!examRisks.value.length) return []
  const map = {}
  for (const r of examRisks.value) {
    if (!map[r.student_id]) {
      map[r.student_id] = {
        student_id: r.student_id,
        student_name: r.student_name,
        total_events: 0,
        total_gaze: 0,
        total_head_down: 0,
        total_head_turn: 0,
        has_cheating_object: false,
        risk_level: 'low',
      }
    }
    const item = map[r.student_id]
    item.total_events += 1
    item.total_gaze += r.gaze_deviation_duration || 0
    item.total_head_down += r.head_down_duration || 0
    item.total_head_turn += r.head_turn_events || 0
    if (r.cheating_object_nearby) item.has_cheating_object = true
    if (r.risk_level === 'high' || (r.risk_level === 'medium' && item.risk_level !== 'high')) {
      item.risk_level = r.risk_level
    }
  }
  return Object.values(map)
    .filter(m => m.total_events > 0 && (m.risk_level === 'high' || m.risk_level === 'medium' || m.has_cheating_object))
    .sort((a, b) => b.total_events - a.total_events)
})

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
const addStudentForm = ref({ track_id: 1, name: '', person_id: null })
const availablePersons = ref([])

function filterPerson(input, option) {
  const label = option.children?.[0]?.children?.[0] || ''
  return label.toLowerCase().includes(input.toLowerCase())
}

function openAddStudent() {
  const maxTrackId = students.value.length > 0
    ? Math.max(...students.value.map(s => s.track_id || 0)) + 1
    : 1
  addStudentForm.value = { track_id: maxTrackId, name: '', person_id: null }
  addStudentOpen.value = true
  loadAvailablePersons()
}

async function loadAvailablePersons() {
  try {
    const res = await api.get('/persons', { params: { role: 'student' } })
    // 过滤掉已在课堂中的学生
    const existingPersonIds = new Set(students.value.map(s => s.person_id).filter(Boolean))
    availablePersons.value = (res.data || []).filter(p => !existingPersonIds.has(p.id))
  } catch {
    availablePersons.value = []
  }
}

async function handleAddStudent() {
  addStudentSaving.value = true
  try {
    const payload = {
      classroom_id: Number(classroomId),
      track_id: addStudentForm.value.track_id,
      name: addStudentForm.value.name || null,
    }
    if (addStudentForm.value.person_id) {
      payload.person_id = addStudentForm.value.person_id
      // 自动填充姓名
      const person = availablePersons.value.find(p => p.id === addStudentForm.value.person_id)
      if (person && !payload.name) payload.name = person.name
    }
    await api.post(`/classrooms/${classroomId}/students`, payload)
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

async function loadExamRisks() {
  if (!classroom.value?.exam_mode) return
  riskLoading.value = true
  try {
    const params = {}
    if (riskFilter.value) params.risk_level = riskFilter.value
    const res = await api.get(`/classrooms/${classroomId}/exam-risks`, { params })
    examRisks.value = res.data || []
  } catch {
    examRisks.value = []
  } finally {
    riskLoading.value = false
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

      // 加载风险记录并绘制风险时间线
      await loadExamRisks()
      await nextTick()
      if (riskTimelineEl.value && examRisks.value.length > 0) {
        const riskTimelineChart = echarts.init(riskTimelineEl.value)
        // 按时间排序的风险记录
        const sortedRisks = [...examRisks.value].sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp))
        const timeLabels = sortedRisks.map(r => new Date(r.timestamp).toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' }))
        // 按学生分组
        const studentNames = [...new Set(sortedRisks.map(r => r.student_name))]
        const series = studentNames.map(name => ({
          name,
          type: 'line',
          data: sortedRisks.map(r => r.student_name === name ? (r.risk_level === 'high' ? 3 : r.risk_level === 'medium' ? 2 : 1) : null),
          connectNulls: false,
          symbolSize: 6,
        }))
        riskTimelineChart.setOption({
          tooltip: {
            trigger: 'item',
            formatter: (p) => `${p.seriesName}<br/>${p.axisValue}: ${['', '低风险', '中风险', '高风险'][p.value] || '未知'}`
          },
          legend: { bottom: 0, type: 'scroll' },
          grid: { top: 20, bottom: 50, left: 50, right: 20 },
          xAxis: { type: 'category', data: timeLabels },
          yAxis: {
            type: 'value',
            min: 0,
            max: 3,
            interval: 1,
            axisLabel: { formatter: v => ['', '低', '中', '高'][v] || '' }
          },
          series,
        })
      }
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
