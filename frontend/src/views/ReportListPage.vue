<template>
  <div class="report-page">
    <div class="page-header-wrap">
      <a-page-header :title="pageTitle" :sub-title="subtitleText" style="padding: 0 0 16px 0" />
      <a-button @click="loadData" :loading="loading">刷新数据</a-button>
    </div>

    <a-spin :spinning="loading && classrooms.length === 0">
      <a-skeleton v-if="loading && classrooms.length === 0" active :paragraph="{ rows: 4 }" />
      <template v-else>
      <a-row :gutter="16" style="margin-bottom: 24px">
        <a-col :xs="12" :sm="6">
          <a-card>
            <a-statistic title="总课堂数" :value="classrooms.length" />
          </a-card>
        </a-col>
        <a-col :xs="12" :sm="6">
          <a-card>
            <a-statistic title="平均注意力" :value="overallAvgAttention" suffix="%" :value-style="{ color: overallAvgAttention >= 60 ? '#3f8600' : '#cf1322' }" />
          </a-card>
        </a-col>
        <a-col :xs="12" :sm="6">
          <a-card>
            <a-statistic title="总学生数" :value="totalStudents" />
          </a-card>
        </a-col>
        <a-col :xs="12" :sm="6">
          <a-card>
            <a-statistic title="已生成报告" :value="reportsCount" />
          </a-card>
        </a-col>
      </a-row>

      <h3 class="section-title">课堂注意力详情</h3>

      <a-empty v-if="filteredClassrooms.length === 0" description="暂无课堂数据" style="margin: 60px 0" />

      <a-list v-else item-layout="vertical" :data-source="filteredClassrooms" :split="true">
        <template #renderItem="{ item: c }">
          <a-list-item>
            <a-card hoverable size="small" @click="toggleExpand(c.id)" style="cursor: pointer">
              <div class="card-header-row">
                <div class="card-header-left">
                  <a-badge :status="statusBadge(c)" />
                  <div>
                    <span class="card-title-text">{{ c.name }}</span>
                    <span class="card-meta-text">{{ c.teacher || '未知教师' }} · {{ formatDuration(c.duration) }}</span>
                  </div>
                </div>
                <div class="card-header-right">
                  <a-tag :color="attentionColor(c.avg_attention)">
                    {{ Math.round(c.avg_attention || 0) }}% · {{ attentionLabel(c.avg_attention) }}
                  </a-tag>
                  <a-button type="text" size="small">
                    <template #icon>
                      <DownOutlined :class="{ 'expand-rotated': expandedId === c.id }" />
                    </template>
                  </a-button>
                </div>
              </div>
            </a-card>

            <div v-if="expandedId === c.id" class="card-detail-area">
              <a-spin :spinning="detailLoading">
                <template v-if="detailData[c.id] && detailData[c.id].length > 0">
                  <a-row :gutter="16" style="margin-bottom: 16px">
                    <a-col :span="6"><a-statistic title="学生人数" :value="detailData[c.id].length" /></a-col>
                    <a-col :span="6"><a-statistic title="平均注意力" :value="avgStudentAttention(detailData[c.id])" suffix="%" /></a-col>
                    <a-col :span="6"><a-statistic title="低头次数" :value="totalHeadDown(detailData[c.id])" /></a-col>
                    <a-col :span="6"><a-statistic title="疲劳眨眼" :value="totalBlinks(detailData[c.id])" /></a-col>
                  </a-row>

                  <div v-if="currentRole !== 'student'" style="margin-bottom: 16px">
                    <h4 class="detail-section-title">学生注意力排行</h4>
                    <div v-for="s in sortedStudents(detailData[c.id])" :key="s.id" class="student-row">
                      <span class="student-name-text">{{ s.name || `学生${s.track_id}` }}</span>
                      <a-progress
                        :percent="Math.min(100, Math.round(s.avg_attention || 0))"
                        :stroke-color="attentionProgressColor(s.avg_attention)"
                        :show-info="true"
                        size="small"
                        style="flex: 1; margin: 0 12px"
                      />
                      <a-tag v-if="s.risk_level && s.risk_level !== 'low'" :color="riskColor(s.risk_level)" size="small">
                        {{ riskLabel(s.risk_level) }}
                      </a-tag>
                    </div>
                  </div>

                  <div class="report-actions">
                    <a-button
                      v-if="!reportData[c.id]"
                      type="primary"
                      @click="generateReport(c.id)"
                      :loading="reportGenerating[c.id]"
                    >
                      <template #icon><FileTextOutlined /></template>
                      生成 AI 报告
                    </a-button>
                    <a-space v-else>
                      <a-popconfirm
                        title="确定重新生成报告？将覆盖当前报告内容。"
                        @confirm="generateReport(c.id, true)"
                      >
                        <a-button type="primary" :loading="reportGenerating[c.id]">
                          <template #icon><ReloadOutlined /></template>
                          重新生成报告
                        </a-button>
                      </a-popconfirm>
                      <a-popconfirm
                        v-if="canManageReport"
                        title="确定删除该报告？"
                        @confirm="deleteReport(c.id)"
                      >
                        <a-button danger size="small">
                          <template #icon><DeleteOutlined /></template>
                          删除报告
                        </a-button>
                      </a-popconfirm>
                    </a-space>
                  </div>

                  <a-card v-if="reportData[c.id]" title="AI 分析报告" size="small" style="margin-top: 16px">
                    <div class="markdown-body" v-html="renderedReport(c.id)"></div>
                  </a-card>
                  <a-alert
                    v-else-if="reportError[c.id]"
                    :message="reportError[c.id]"
                    type="error"
                    show-icon
                    style="margin-top: 16px"
                  />
                </template>
                <a-empty v-else description="暂无学生数据" style="margin: 20px 0" />
              </a-spin>
            </div>
          </a-list-item>
        </template>
      </a-list>
      </template>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, reactive } from 'vue'
import { useUserStore } from '@/stores/user'
import api from '@/api'
import { message } from 'ant-design-vue'
import { DownOutlined, FileTextOutlined, ReloadOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import MarkdownIt from 'markdown-it'

const md = new MarkdownIt({ html: false, breaks: true, linkify: true })

const userStore = useUserStore()
const canManageReport = computed(() => ['teacher', 'admin'].includes(userStore.role))
const currentRole = computed(() => userStore.role || 'teacher')

const loading = ref(false)
const classrooms = ref([])
const expandedId = ref(null)
const detailLoading = ref(false)
const detailData = reactive({})
const reportData = reactive({})
const reportError = reactive({})
const reportGenerating = reactive({})

const pageTitle = computed(() => '注意力报告')

const subtitleText = computed(() => {
  if (currentRole.value === 'student') return '查看你在各课堂的注意力表现'
  if (currentRole.value === 'admin') return '全局注意力数据分析与 AI 报告'
  return '查看课堂学生的注意力表现与 AI 分析'
})

const filteredClassrooms = computed(() => classrooms.value)

const overallAvgAttention = computed(() => {
  if (classrooms.value.length === 0) return 0
  const sum = classrooms.value.reduce((acc, c) => acc + (c.avg_attention || 0), 0)
  return Math.round(sum / classrooms.value.length)
})

const totalStudents = computed(() => {
  const ids = new Set()
  Object.values(detailData).forEach(list => list.forEach(s => ids.add(s.id)))
  return ids.size || classrooms.value.reduce((acc, c) => acc + (c.total_students || 0), 0)
})

const reportsCount = computed(() => Object.keys(reportData).length)

function renderedReport(id) {
  const raw = reportData[id]
  if (!raw) return ''
  return md.render(raw)
}

async function loadData() {
  loading.value = true
  try {
    const res = await api.get('/classrooms')
    classrooms.value = res.data || []
  } catch (e) {
    message.error('加载课堂数据失败')
  } finally {
    loading.value = false
  }
}

async function toggleExpand(classroomId) {
  if (expandedId.value === classroomId) {
    expandedId.value = null
    return
  }
  expandedId.value = classroomId
  if (!detailData[classroomId]) {
    detailLoading.value = true
    try {
      const res = await api.get(`/classrooms/${classroomId}/students`)
      detailData[classroomId] = res.data || []
    } catch (e) {
      detailData[classroomId] = []
    } finally {
      detailLoading.value = false
    }
    const rep = await api.get(`/classrooms/${classroomId}/report`).catch(() => null)
    if (rep && rep.data) {
      reportData[classroomId] = rep.data.content
    }
  }
}

async function generateReport(classroomId, force = false) {
  if (reportData[classroomId] && !force) return
  reportGenerating[classroomId] = true
  reportError[classroomId] = ''
  try {
    const url = force
      ? `/classrooms/${classroomId}/report?force=true`
      : `/classrooms/${classroomId}/report`
    const res = await api.post(url)
    if (res.data && res.data.content) {
      reportData[classroomId] = res.data.content
      message.success(force ? '报告已重新生成' : '报告生成成功')
    }
  } catch (e) {
    reportError[classroomId] = e.response?.data?.detail || '报告生成失败，请稍后重试'
    message.error('报告生成失败')
  } finally {
    reportGenerating[classroomId] = false
  }
}

async function deleteReport(classroomId) {
  try {
    await api.delete(`/classrooms/${classroomId}/report`)
    delete reportData[classroomId]
    message.success('报告已删除')
  } catch (e) {
    const detail = e.response?.data?.detail || '删除失败'
    message.error(detail)
  }
}

function statusBadge(c) {
  if (c.ended_at) return 'default'
  if (c.started_at) return 'processing'
  return 'warning'
}

function attentionColor(val) {
  if (val >= 75) return 'success'
  if (val >= 50) return 'warning'
  return 'error'
}

function attentionProgressColor(val) {
  if (val >= 75) return '#52c41a'
  if (val >= 50) return '#faad14'
  return '#ff4d4f'
}

function attentionLabel(val) {
  if (val >= 75) return '良好'
  if (val >= 50) return '一般'
  return '偏低'
}

function riskColor(level) {
  if (level === 'high') return 'red'
  if (level === 'medium') return 'orange'
  return 'default'
}

function riskLabel(level) {
  if (level === 'high') return '高风险'
  if (level === 'medium') return '中风险'
  return ''
}

function formatDuration(seconds) {
  if (!seconds) return '0分钟'
  const mins = Math.floor(seconds / 60)
  if (mins < 60) return `${mins}分钟`
  const hours = Math.floor(mins / 60)
  return `${hours}小时${mins % 60}分钟`
}

function avgStudentAttention(students) {
  if (!students || students.length === 0) return 0
  return Math.round(students.reduce((acc, s) => acc + (s.avg_attention || 0), 0) / students.length)
}

function totalHeadDown(students) {
  return (students || []).reduce((acc, s) => acc + (s.head_down_count || 0), 0)
}

function totalBlinks(students) {
  return (students || []).reduce((acc, s) => acc + (s.blink_count || 0), 0)
}

function sortedStudents(students) {
  return [...(students || [])].sort((a, b) => (b.avg_attention || 0) - (a.avg_attention || 0))
}

onMounted(() => { loadData() })
</script>

<style scoped>
.report-page {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  max-width: 1200px;
  margin: 0 auto;
}

.page-header-wrap {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.section-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 16px;
}

.card-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.card-title-text {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a2e;
  display: block;
}

.card-meta-text {
  font-size: 12px;
  color: #8c8c8c;
}

.card-header-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

.expand-rotated {
  transform: rotate(180deg);
  transition: transform 0.2s;
}

.card-detail-area {
  padding: 16px 0 8px 0;
}

.detail-section-title {
  font-size: 14px;
  font-weight: 600;
  color: #475569;
  margin-bottom: 12px;
}

.student-row {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
}

.student-name-text {
  width: 100px;
  font-size: 13px;
  color: #475569;
  flex-shrink: 0;
}

.report-actions {
  margin-top: 16px;
}

.markdown-body {
  font-size: 14px;
  line-height: 1.7;
  color: var(--cv-text-secondary);
}

.markdown-body :deep(h1),
.markdown-body :deep(h2),
.markdown-body :deep(h3),
.markdown-body :deep(h4) {
  font-weight: 600;
  margin: 16px 0 8px 0;
  color: var(--cv-text-primary);
}

.markdown-body :deep(h1) { font-size: 20px; }
.markdown-body :deep(h2) { font-size: 17px; }
.markdown-body :deep(h3) { font-size: 15px; }
.markdown-body :deep(h4) { font-size: 14px; }

.markdown-body :deep(ul),
.markdown-body :deep(ol) {
  padding-left: 20px;
  margin: 8px 0;
}

.markdown-body :deep(li) {
  margin: 4px 0;
}

.markdown-body :deep(strong) {
  font-weight: 600;
  color: var(--cv-text-primary);
}

.markdown-body :deep(blockquote) {
  border-left: 3px solid var(--cv-color-primary);
  padding: 8px 16px;
  margin: 12px 0;
  background: var(--cv-bg-page);
  border-radius: 0 6px 6px 0;
  color: var(--cv-text-tertiary);
  font-size: 13px;
}

.markdown-body :deep(p) {
  margin: 8px 0;
}

.markdown-body :deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
  font-size: 13px;
}

.markdown-body :deep(th),
.markdown-body :deep(td) {
  border: 1px solid var(--cv-border-base);
  padding: 8px 12px;
  text-align: left;
}

.markdown-body :deep(th) {
  background: var(--cv-bg-page);
  font-weight: 600;
  color: var(--cv-text-primary);
}

.markdown-body :deep(tr:nth-child(2n)) {
  background: var(--cv-bg-subtle);
}

.markdown-body :deep(code) {
  background: var(--cv-bg-page);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--cv-color-primary);
}

.markdown-body :deep(pre) {
  background: var(--cv-bg-page);
  padding: 12px 16px;
  border-radius: var(--cv-radius-base);
  overflow-x: auto;
  margin: 12px 0;
}

.markdown-body :deep(pre code) {
  background: none;
  padding: 0;
  color: var(--cv-text-secondary);
}

.markdown-body :deep(hr) {
  border: none;
  border-top: 1px solid var(--cv-border-light);
  margin: 16px 0;
}

.markdown-body :deep(a) {
  color: var(--cv-color-primary);
  text-decoration: none;
}

.markdown-body :deep(a:hover) {
  text-decoration: underline;
}
</style>
