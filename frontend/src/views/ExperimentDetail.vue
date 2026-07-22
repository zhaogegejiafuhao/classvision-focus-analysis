<template>
  <div class="exp-detail">
    <a-spin :spinning="loading">
      <a-page-header :title="experiment?.title" @back="() => $router.back()">
        <template #extra>
          <a-space>
            <a-tag v-if="experiment">{{ experiment.status === 'open' ? '进行中' : '已关闭' }}</a-tag>
            <a-button v-if="userStore.role === 'student'" type="primary" @click="showSubmit = true">提交报告</a-button>
          </a-space>
        </template>
      </a-page-header>

      <div style="padding: 0 24px 24px">
        <a-row :gutter="16">
          <a-col :span="12">
            <a-card title="实验信息" size="small">
              <p><b>描述：</b>{{ experiment?.description || '无' }}</p>
              <p><b>要求：</b>{{ experiment?.requirements || '无' }}</p>
              <p><b>总分：</b>{{ experiment?.total_score }}</p>
              <p><b>截止：</b>{{ experiment?.deadline ? dayjs(experiment.deadline).format('YYYY-MM-DD HH:mm') : '无' }}</p>
            </a-card>
          </a-col>
          <a-col :span="12">
            <a-card v-if="userStore.role === 'teacher'" title="学生提交" size="small">
              <a-table :columns="reportColumns" :data-source="reports" row-key="id" size="small" :pagination="{ pageSize: 10 }">
                <template #bodyCell="{ column, record }">
                  <template v-if="column.key === 'status'">
                    <a-tag :color="statusColor(record.status)">{{ statusText(record.status) }}</a-tag>
                  </template>
                  <template v-else-if="column.key === 'action'">
                    <a-button type="link" size="small" @click="showGrade(record)">批改</a-button>
                    <a-button v-if="record.file_name" type="link" size="small" @click="downloadFile(record.id)">下载</a-button>
                  </template>
                </template>
              </a-table>
            </a-card>
            <a-card v-else title="我的提交" size="small">
              <p v-if="!myReport">尚未提交</p>
              <div v-else>
                <p><b>状态：</b><a-tag :color="statusColor(myReport.status)">{{ statusText(myReport.status) }}</a-tag></p>
                <p><b>得分：</b>{{ myReport.score ?? '-' }} / {{ experiment?.total_score }}</p>
                <p><b>反馈：</b>{{ myReport.feedback || '无' }}</p>
                <p v-if="myReport.file_name"><b>附件：</b><a @click="downloadFile(myReport.id)">{{ myReport.file_name }}</a></p>
              </div>
            </a-card>
          </a-col>
        </a-row>
      </div>
    </a-spin>

    <a-modal v-model:open="showSubmit" title="提交实验报告" @ok="submitReport" :confirm-loading="submitting">
      <a-form layout="vertical">
        <a-form-item label="报告内容">
          <a-textarea v-model:value="submitForm.content" :rows="5" />
        </a-form-item>
        <a-form-item label="附件">
          <a-upload :before-upload="(f) => { submitForm.file = f; return false }" :max-count="1">
            <a-button>选择文件</a-button>
          </a-upload>
        </a-form-item>
      </a-form>
    </a-modal>

    <a-modal v-model:open="showGradeModal" title="批改实验报告" @ok="gradeReport" :confirm-loading="grading">
      <a-form layout="vertical">
        <a-form-item label="得分" required>
          <a-input-number v-model:value="gradeForm.score" :min="0" :max="experiment?.total_score || 100" />
        </a-form-item>
        <a-form-item label="反馈">
          <a-textarea v-model:value="gradeForm.feedback" :rows="3" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { message } from 'ant-design-vue'
import dayjs from 'dayjs'
import api from '@/api'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const userStore = useUserStore()
const expId = route.params.id
const experiment = ref()
const reports = ref([])
const myReport = ref()
const loading = ref(false)
const showSubmit = ref(false)
const submitting = ref(false)
const submitForm = ref({ content: '', file: null })
const showGradeModal = ref(false)
const grading = ref(false)
const gradeForm = ref({ score: 0, feedback: '' })
const currentReport = ref()

const reportColumns = [
  { title: '学生', dataIndex: 'student_name', key: 'student_name' },
  { title: '状态', key: 'status' },
  { title: '得分', dataIndex: 'score', key: 'score', customRender: ({ text }) => text ?? '-' },
  { title: '提交时间', dataIndex: 'submitted_at', key: 'submitted_at', customRender: ({ text }) => text ? dayjs(text).format('YYYY-MM-DD HH:mm') : '-' },
  { title: '操作', key: 'action' },
]

function statusColor(s) { return { submitted: 'blue', graded: 'green', returned: 'orange' }[s] || 'default' }
function statusText(s) { return { submitted: '待批改', graded: '已批改', returned: '已退回' }[s] || s }

async function fetchData() {
  loading.value = true
  try {
    const [expRes, repRes] = await Promise.all([
      api.get(`/experiments/${expId}`),
      api.get(`/experiments/${expId}/reports`, { _skipGlobalError: true }),
    ])
    experiment.value = expRes.data
    reports.value = repRes.data
    if (userStore.role === 'student') {
      myReport.value = repRes.data.find(r => r.student_id === userStore.user?.id)
    }
  } catch (e) {
    message.error('加载失败')
  } finally {
    loading.value = false
  }
}

async function submitReport() {
  submitting.value = true
  try {
    const formData = new FormData()
    formData.append('content', submitForm.value.content)
    if (submitForm.value.file) formData.append('file', submitForm.value.file)
    await api.post(`/experiments/${expId}/submit`, formData, { headers: { 'Content-Type': 'multipart/form-data' } })
    message.success('提交成功')
    showSubmit.value = false
    submitForm.value = { content: '', file: null }
    fetchData()
  } catch (e) {
    message.error('提交失败')
  } finally {
    submitting.value = false
  }
}

function showGrade(record) {
  currentReport.value = record
  gradeForm.value = { score: record.score || 0, feedback: record.feedback || '' }
  showGradeModal.value = true
}

async function gradeReport() {
  grading.value = true
  try {
    await api.post(`/experiments/reports/${currentReport.value.id}/grade`, gradeForm.value)
    message.success('批改成功')
    showGradeModal.value = false
    fetchData()
  } catch (e) {
    message.error('批改失败')
  } finally {
    grading.value = false
  }
}

function downloadFile(reportId) {
  window.open(`/api/experiments/reports/${reportId}/download`, '_blank')
}

onMounted(fetchData)
</script>
