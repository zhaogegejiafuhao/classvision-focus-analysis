<template>
  <div class="cv-page" style="max-width: 1400px">
      <a-spin :spinning="loading">
        <a-skeleton v-if="loading && !classroom" active :paragraph="{ rows: 4 }" />
        <template v-if="classroom">
          <div class="page-header-wrap">
            <a-page-header :title="classroom.name" :sub-title="`${classroom.teacher} · ${classroom.duration}分钟`" style="padding: 0 0 16px 0" />
            <a-space v-if="canEditOrDelete || canManage">
              <a-button v-if="canManage && classroom.ended_at && !report" @click="genReport()" :loading="genLoading">
                <template #icon><FileTextOutlined /></template>
                生成报告
              </a-button>
              <a-button v-if="!classroom.ended_at && canManage" type="primary" @click="$router.push(`/live/${classroomId}`)">
                <template #icon><VideoCameraOutlined /></template>
                {{ classroom.started_at ? '进入课堂检测' : '开始课堂' }}
              </a-button>
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

          <!-- 注意力趋势 -->
          <a-card title="注意力趋势" style="margin-bottom: 16px">
            <div ref="timelineEl" style="width: 100%; height: 300px" />
          </a-card>

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
              <!-- AI 报告：无报告时不显示 -->
              <a-card v-if="report" title="AI 课堂分析报告">
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
                <div ref="chatContainerRef" v-if="chatMessages.length > 0" class="chat-container">
                  <div v-for="msg in chatMessages" :key="msg.id" :class="['chat-msg', msg.role === 'user' ? 'chat-msg-user' : 'chat-msg-ai']">
                    <div v-if="msg.role === 'assistant'" class="chat-avatar">🤖</div>
                    <div class="chat-bubble-wrap">
                      <div :class="['chat-bubble', msg.role === 'user' ? 'bubble-user' : 'bubble-ai']">
                        <div v-if="msg.streaming && !msg.content" class="chat-loading">
                          <span class="dot-pulse"></span>
                          <span class="dot-pulse"></span>
                          <span class="dot-pulse"></span>
                          <span class="loading-text">{{ msg.loadingStage || 'AI 正在思考...' }}</span>
                        </div>
                        <div class="markdown-body" v-html="renderMarkdown(msg.content)" />
                        <span v-if="msg.streaming && msg.content" class="streaming-cursor">▌</span>
                      </div>
                      <div class="chat-meta">
                        <span class="chat-time">{{ new Date(msg.timestamp).toLocaleTimeString('zh-CN') }}</span>
                        <span v-if="msg.elapsed" class="chat-elapsed">{{ msg.elapsed }}</span>
                        <a-button v-if="msg.error" type="link" size="small" @click="retryChat(msg)">重试</a-button>
                      </div>
                    </div>
                    <div v-if="msg.role === 'user'" class="chat-avatar">👤</div>
                  </div>
                </div>
                <a-empty v-else description="暂无对话记录" style="margin-bottom: 16px" />

                <!-- 输入框 -->
                <div style="margin-bottom: 8px">
                  <a-radio-group v-model:value="chatMode" size="small" :disabled="chatLoading">
                    <a-radio-button value="fast">⚡ 快速回答</a-radio-button>
                    <a-radio-button value="deep">🧠 深度思考</a-radio-button>
                  </a-radio-group>
                  <span style="margin-left: 12px; font-size: 12px; color: #999">
                    {{ chatMode === 'fast'
                      ? '约 20-70 秒 | qwen3:4b 思考模式'
                      : '约 35-90 秒 | qwen3:4b 思考模式 + Reranker'
                    }}
                  </span>
                </div>
                <div class="chat-input-area">
                  <a-textarea
                    v-model:value="chatInput"
                    placeholder="输入问题，如：为什么疲劳人次这么高？（Enter 发送，Shift+Enter 换行）"
                    :auto-size="{ minRows: 1, maxRows: 4 }"
                    :disabled="chatLoading"
                    @keydown.enter.exact.prevent="sendChat()"
                  />
                  <a-button type="primary" @click="sendChat()" :loading="chatLoading" :disabled="!chatInput.trim()">
                    发送
                  </a-button>
                </div>

                <!-- 下载按钮 -->
                <a-space style="margin-top: 12px">
                  <a-button @click="downloadMarkdown" :disabled="chatMessages.length === 0 && !report">
                    下载完整报告（含对话记录）
                  </a-button>
                </a-space>
              </a-card>
            </a-col>
          </a-row>

          <!-- 教学模块 Tab -->
          <a-card title="教学活动" style="margin-top: 16px" v-if="canManage">
            <a-tabs v-model:activeKey="teachingTab">
              <a-tab-pane key="homework" tab="作业">
                <a-table :columns="hwColumns" :data-source="classHomeworks" row-key="id" size="small" :loading="hwLoading">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'status'">
                      <a-tag :color="{ open: 'blue', closed: 'gray' }[record.status] || 'default'">{{ { open: '进行中', closed: '已截止' }[record.status] || record.status }}</a-tag>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <a-button type="link" size="small" @click="$router.push(`/homework/${record.id}`)">详情</a-button>
                    </template>
                  </template>
                </a-table>
                <a-button type="primary" size="small" style="margin-top: 8px" @click="$router.push('/homework')">管理作业</a-button>
              </a-tab-pane>
              <a-tab-pane key="exam" tab="考试">
                <a-table :columns="examColumns" :data-source="classExams" row-key="id" size="small" :loading="examLoading">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'status'">
                      <a-tag :color="{ draft: 'default', published: 'blue', closed: 'gray' }[record.status] || 'default'">{{ { draft: '草稿', published: '已发布', closed: '已结束' }[record.status] || record.status }}</a-tag>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <a-button type="link" size="small" @click="$router.push(`/exams/${record.id}`)">详情</a-button>
                    </template>
                  </template>
                </a-table>
                <a-button type="primary" size="small" style="margin-top: 8px" @click="$router.push('/exams')">管理考试</a-button>
              </a-tab-pane>
              <a-tab-pane key="checkin" tab="签到">
                <a-table :columns="checkinColumns" :data-source="classCheckins" row-key="id" size="small" :loading="checkinLoading">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'status'">
                      <a-tag :color="record.status === 'active' ? 'green' : 'gray'">{{ record.status === 'active' ? '进行中' : '已结束' }}</a-tag>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <a-button type="link" size="small" @click="$router.push(`/checkin/${record.id}`)">详情</a-button>
                    </template>
                  </template>
                </a-table>
                <a-button type="primary" size="small" style="margin-top: 8px" @click="$router.push('/checkin')">管理签到</a-button>
              </a-tab-pane>
              <a-tab-pane key="materials" tab="课件">
                <a-list :data-source="classMaterials" :loading="materialLoading" size="small">
                  <template #renderItem="{ item }">
                    <a-list-item>
                      <a-list-item-meta>
                        <template #title>{{ item.title }}</template>
                        <template #description>{{ item.file_name }} · {{ formatFileSize(item.file_size) }}</template>
                      </a-list-item-meta>
                      <template #actions>
                        <a-button type="link" size="small" @click="downloadMaterial(item)">下载</a-button>
                      </template>
                    </a-list-item>
                  </template>
                  <template #footer>
                    <a-button type="primary" size="small" @click="$router.push('/materials')">管理课件</a-button>
                  </template>
                </a-list>
                <a-empty v-if="classMaterials.length === 0 && !materialLoading" description="暂无课件" />
              </a-tab-pane>
            </a-tabs>
          </a-card>
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
          <a-form-item label="课序号">
            <a-input v-model:value="editClassroomForm.course_code" placeholder="例如：CS101" />
          </a-form-item>
          <a-form-item label="公开">
            <a-switch v-model:checked="editClassroomForm.is_public" checked-children="公开" un-checked-children="私有" />
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
  PlusOutlined, ReloadOutlined, VideoCameraOutlined, FileTextOutlined,
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

// 教学模块 Tab
const teachingTab = ref('homework')
const classHomeworks = ref([])
const classExams = ref([])
const classCheckins = ref([])
const hwLoading = ref(false)
const examLoading = ref(false)
const checkinLoading = ref(false)
const classMaterials = ref([])
const materialLoading = ref(false)

const hwColumns = [
  { key: 'title', title: '标题', dataIndex: 'title' },
  { key: 'status', title: '状态' },
  { key: 'submission_count', title: '提交数', dataIndex: 'submission_count' },
  { key: 'action', title: '操作' },
]
const examColumns = [
  { key: 'title', title: '标题', dataIndex: 'title' },
  { key: 'status', title: '状态' },
  { key: 'question_count', title: '题目数', dataIndex: 'question_count' },
  { key: 'action', title: '操作' },
]
const checkinColumns = [
  { key: 'type', title: '类型', dataIndex: 'type' },
  { key: 'status', title: '状态' },
  { key: 'checked_count', title: '已签到', dataIndex: 'checked_count' },
  { key: 'action', title: '操作' },
]

async function loadTeachingData() {
  if (!canManage.value) return
  hwLoading.value = true
  examLoading.value = true
  checkinLoading.value = true
  materialLoading.value = true
  try {
    const [hwRes, examRes, checkinRes, matRes] = await Promise.all([
      api.get('/homework', { params: { classroom_id: classroomId } }).catch(() => ({ data: [] })),
      api.get('/exams', { params: { classroom_id: classroomId } }).catch(() => ({ data: [] })),
      api.get('/checkin/sessions', { params: { classroom_id: classroomId } }).catch(() => ({ data: [] })),
      api.get('/materials', { params: { classroom_id: classroomId } }).catch(() => ({ data: [] })),
    ])
    classHomeworks.value = hwRes.data
    classExams.value = examRes.data
    classCheckins.value = checkinRes.data
    classMaterials.value = matRes.data
  } catch {
    // ignore
  } finally {
    hwLoading.value = false
    examLoading.value = false
    checkinLoading.value = false
    materialLoading.value = false
  }
}

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
const chatContainerRef = ref(null)
// 对话模式：fast=快速回答（关闭 HyDE/Multi-Query，~10-20s），deep=深度思考（启用，~40-84s）
const chatMode = ref('fast')

function scrollChatToBottom() {
  nextTick(() => {
    const el = chatContainerRef.value
    if (el) el.scrollTop = el.scrollHeight
  })
}

const studentCols = computed(() => {
  const base = [
    { title: '姓名', dataIndex: 'name', key: 'name' },
    { title: '平均注意力', dataIndex: 'avg_attention', key: 'avg_attention' },
    { title: '低头人次', dataIndex: 'head_down_count', key: 'head_down_count' },
    { title: '眨眼次数', dataIndex: 'blink_count', key: 'blink_count' },
  ]
  if (canManage.value) {
    base.push({ title: '操作', key: 'action' })
  }
  return base
})

function renderMarkdown(text) {
  if (!text || typeof text !== 'string') return ''
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
const editClassroomForm = ref({ name: '', teacher: '', course_code: '', is_public: true })

function openEditClassroom() {
  editClassroomForm.value = {
    name: classroom.value.name || '',
    teacher: classroom.value.teacher || '',
    course_code: classroom.value.course_code || '',
    is_public: classroom.value.is_public !== false,
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
    scrollChatToBottom()
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

async function sendChat(retryText) {
  const userText = retryText || chatInput.value.trim()
  if (!userText) return
  if (!retryText) chatInput.value = ''

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
    loadingStage: chatMode.value === 'deep' ? '正在检索知识库...' : 'AI 正在思考...',
  })
  const aiIdx = chatMessages.value.length - 1
  chatLoading.value = true
  scrollChatToBottom()
  const t0 = Date.now()
  let receivedDone = false

  // 加载阶段轮询
  const stageTimer = setInterval(() => {
    const elapsed = (Date.now() - t0) / 1000
    const msg = chatMessages.value[aiIdx]
    if (!msg.streaming) return
    if (msg.content) {
      msg.loadingStage = ''
    } else if (chatMode.value === 'deep') {
      if (elapsed > 30) msg.loadingStage = '正在生成回答...'
      else if (elapsed > 15) msg.loadingStage = '正在深度检索知识库...'
    } else {
      if (elapsed > 20) msg.loadingStage = '正在生成回答...'
    }
  }, 5000)

  try {
    const token = userStore.token || localStorage.getItem('token') || ''
    const resp = await fetch(`/api/classrooms/${classroomId}/chat/stream`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ content: userText, mode: chatMode.value }),
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
          chatMessages.value[aiIdx].loadingStage = ''
          scrollChatToBottom()
        }
        if (data.done) {
          receivedDone = true
          const elapsed = ((Date.now() - t0) / 1000).toFixed(1)
          chatMessages.value[aiIdx].id = data.id
          chatMessages.value[aiIdx].streaming = false
          chatMessages.value[aiIdx].elapsed = `耗时 ${elapsed}s`
          scrollChatToBottom()
        }
        if (data.error) {
          receivedDone = true
          chatMessages.value[aiIdx].content = '[生成失败: ' + data.error + ']'
          chatMessages.value[aiIdx].streaming = false
          chatMessages.value[aiIdx].error = true
        }
      }
    }
    // 流异常中断：没有收到 done/error 但流结束了
    if (!receivedDone) {
      chatMessages.value[aiIdx].content = chatMessages.value[aiIdx].content || '[连接中断，请点击重试]'
      chatMessages.value[aiIdx].streaming = false
      chatMessages.value[aiIdx].error = true
      message.warning('连接中断，可点击重试')
    }
  } catch (e) {
    chatMessages.value[aiIdx].content = '[请求失败: ' + e.message + ']'
    chatMessages.value[aiIdx].streaming = false
    chatMessages.value[aiIdx].error = true
    message.error('对话请求失败，可点击重试')
  } finally {
    clearInterval(stageTimer)
    chatLoading.value = false
  }
}

function retryChat(msg) {
  const userMsgs = chatMessages.value.filter(m => m.role === 'user')
  const lastUserMsg = userMsgs[userMsgs.length - 1]
  if (!lastUserMsg) return
  const idx = chatMessages.value.indexOf(msg)
  if (idx >= 0) chatMessages.value.splice(idx, 1)
  sendChat(lastUserMsg.content)
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

    await loadHeatmap()
    await loadAttendance()
    await loadTeachingData()

function formatFileSize(bytes) {
  if (!bytes) return '0B'
  if (bytes < 1024) return bytes + 'B'
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + 'KB'
  return (bytes / 1048576).toFixed(1) + 'MB'
}

function downloadMaterial(record) {
  window.open(`/api/materials/${record.id}/download`, '_blank')
}

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

/* 聊天容器 */
.chat-container {
  max-height: 450px;
  overflow-y: auto;
  margin-bottom: 16px;
  scroll-behavior: smooth;
  padding: 4px;
}

/* 消息行 */
.chat-msg {
  display: flex;
  align-items: flex-start;
  margin-bottom: 16px;
  gap: 8px;
}
.chat-msg-user {
  flex-direction: row-reverse;
}
.chat-msg-ai {
  flex-direction: row;
}

/* 头像 */
.chat-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
  background: #f0f0f0;
}

/* 气泡容器 */
.chat-bubble-wrap {
  max-width: 75%;
  display: flex;
  flex-direction: column;
}
.chat-msg-user .chat-bubble-wrap {
  align-items: flex-end;
}
.chat-msg-ai .chat-bubble-wrap {
  align-items: flex-start;
}

/* 气泡 */
.chat-bubble {
  padding: 10px 14px;
  border-radius: 12px;
  word-break: break-word;
  line-height: 1.6;
}
.bubble-user {
  background: #1890ff;
  color: #fff;
  border-bottom-right-radius: 4px;
}
.bubble-ai {
  background: #f5f5f5;
  color: #333;
  border-bottom-left-radius: 4px;
}
.bubble-user .markdown-body {
  color: #fff;
}

/* 元数据 */
.chat-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 4px;
  font-size: 11px;
}
.chat-time {
  color: #bbb;
}
.chat-elapsed {
  color: #999;
  background: #f5f5f5;
  padding: 1px 6px;
  border-radius: 8px;
}

/* 加载动画 */
.chat-loading {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #999;
}
.dot-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #1890ff;
  animation: dotPulse 1.4s infinite ease-in-out;
}
.dot-pulse:nth-child(2) {
  animation-delay: 0.2s;
}
.dot-pulse:nth-child(3) {
  animation-delay: 0.4s;
}
.loading-text {
  margin-left: 6px;
  font-size: 13px;
}
@keyframes dotPulse {
  0%, 80%, 100% {
    transform: scale(0.6);
    opacity: 0.4;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}

/* 输入框区域 */
.chat-input-area {
  display: flex;
  gap: 8px;
  align-items: flex-end;
}
.chat-input-area .ant-input {
  flex: 1;
}
</style>
