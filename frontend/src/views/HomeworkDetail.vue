<template>
  <div class="cv-page">
    <a-page-header :title="homework?.title || '作业详情'" @back="() => $router.push('/homework')">
      <template #subTitle>
        <a-tag v-if="homework" :color="getStatusColor(homework.status)">{{ getStatusText(homework.status) }}</a-tag>
      </template>
      <template #extra>
        <a-button @click="editHomework">编辑</a-button>
        <a-button type="primary" @click="closeHomework" v-if="homework?.status === 'open'">截止作业</a-button>
      </template>
    </a-page-header>

    <a-spin :spinning="loading">
      <a-row :gutter="16">
        <!-- 左侧：作业信息 -->
        <a-col :span="8">
          <a-card title="作业信息" size="small">
            <p><strong>描述：</strong></p>
            <p>{{ homework?.description || '无' }}</p>
            <p><strong>课堂：</strong>{{ homework?.classroom_name || '全体学生' }}</p>
            <p><strong>截止时间：</strong>{{ homework?.deadline ? formatTime(homework.deadline) : '无' }}</p>
            <p><strong>总分：</strong>{{ homework?.total_score }}分</p>
            <p><strong>提交数：</strong>{{ homework?.submission_count }}份</p>
          </a-card>
        </a-col>

        <!-- 右侧：提交列表 -->
        <a-col :span="16">
          <a-card title="学生提交" size="small">
            <a-table :columns="submissionColumns" :data-source="submissions" row-key="id" size="small">
              <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'status'">
                  <a-tag :color="getSubmissionColor(record.status)">{{ getSubmissionText(record.status) }}</a-tag>
                </template>
                <template v-else-if="column.key === 'score'">
                  {{ record.score ?? '-' }} / {{ homework?.total_score }}
                </template>
                <template v-else-if="column.key === 'action'">
                  <a-button type="link" size="small" @click="showGradeModal(record)">批改</a-button>
                  <a-button type="link" size="small" danger @click="handleReturnSubmission(record)">打回</a-button>
                </template>
              </template>
            </a-table>
          </a-card>
        </a-col>
      </a-row>
    </a-spin>

    <!-- 编辑弹窗 -->
    <a-modal v-model:open="editModalVisible" title="编辑作业" @ok="submitEdit" :confirm-loading="editSaving">
      <a-form layout="vertical">
        <a-form-item label="标题">
          <a-input v-model:value="editForm.title" />
        </a-form-item>
        <a-form-item label="描述">
          <a-textarea v-model:value="editForm.description" :rows="4" />
        </a-form-item>
        <a-form-item label="截止时间">
          <a-date-picker v-model:value="editForm.deadline" show-time style="width: 100%" />
        </a-form-item>
        <a-form-item label="总分">
          <a-input-number v-model:value="editForm.total_score" :min="1" />
        </a-form-item>
      </a-form>
    </a-modal>

    <!-- 批改弹窗 -->
    <a-modal v-model:open="gradeModalVisible" :title="`批改 - ${currentSubmission?.student_name || ''}`" @ok="submitGrade" :confirm-loading="grading">
      <template #footer>
        <a-button @click="gradeModalVisible = false">取消</a-button>
        <a-button v-if="hasNextSubmission" @click="submitGradeAndNext" :loading="grading">批改并下一位</a-button>
        <a-button type="primary" @click="submitGrade" :loading="grading">提交</a-button>
      </template>
      <a-form :label-col="{ span: 4 }">
        <a-form-item label="学生">
          {{ currentSubmission?.student_name }}
        </a-form-item>
        <a-form-item label="提交内容">
          <div class="submission-content">{{ currentSubmission?.content || '无内容' }}</div>
        </a-form-item>
        <a-form-item label="分数" required>
          <a-input-number v-model:value="gradeForm.score" :min="0" :max="homework?.total_score" style="width: 120px" />
          <span style="margin-left: 8px">/ {{ homework?.total_score }}分</span>
        </a-form-item>
        <a-form-item label="评语">
          <a-textarea v-model:value="gradeForm.feedback" placeholder="填写评语（可选）" :rows="3" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRoute, useRouter } from 'vue-router'
import { getHomework, updateHomework, listHomeworkSubmissions, gradeSubmission, returnSubmission } from '@/api/homework'
import dayjs from 'dayjs'

const route = useRoute()
const router = useRouter()
const homeworkId = route.params.id

const homework = ref(null)
const submissions = ref([])
const loading = ref(false)
const grading = ref(false)
const gradeModalVisible = ref(false)
const currentSubmission = ref(null)

const gradeForm = ref({
  score: 0,
  feedback: '',
})

const submissionColumns = [
  { key: 'student_name', title: '学生', dataIndex: 'student_name' },
  { key: 'submitted_at', title: '提交时间', dataIndex: 'submitted_at' },
  { key: 'status', title: '状态', dataIndex: 'status' },
  { key: 'score', title: '分数' },
  { key: 'action', title: '操作' },
]

async function fetchHomework() {
  loading.value = true
  try {
    const res = await getHomework(homeworkId)
    homework.value = res.data
  } catch (e) {
    message.error('获取作业失败')
  } finally {
    loading.value = false
  }
}

async function fetchSubmissions() {
  try {
    const res = await listHomeworkSubmissions(homeworkId)
    submissions.value = res.data.map(s => ({
      ...s,
      submitted_at: formatTime(s.submitted_at),
    }))
  } catch (e) {
    // 忽略
  }
}

async function closeHomework() {
  try {
    await updateHomework(homeworkId, { status: 'closed' })
    message.success('作业已截止')
    fetchHomework()
  } catch (e) {
    message.error('操作失败')
  }
}

const editModalVisible = ref(false)
const editSaving = ref(false)
const editForm = ref({ title: '', description: '', deadline: null, total_score: 100 })

function editHomework() {
  if (!homework.value) return
  editForm.value = {
    title: homework.value.title,
    description: homework.value.description,
    deadline: homework.value.deadline ? dayjs(homework.value.deadline) : null,
    total_score: homework.value.total_score,
  }
  editModalVisible.value = true
}

async function submitEdit() {
  editSaving.value = true
  try {
    const payload = {
      title: editForm.value.title,
      description: editForm.value.description,
      deadline: editForm.value.deadline ? editForm.value.deadline.toISOString() : null,
      total_score: editForm.value.total_score,
    }
    await updateHomework(homeworkId, payload)
    message.success('作业已更新')
    editModalVisible.value = false
    fetchHomework()
  } catch (e) {
    message.error('更新失败')
  } finally {
    editSaving.value = false
  }
}

function showGradeModal(submission) {
  currentSubmission.value = submission
  gradeForm.value = {
    score: submission.score || 0,
    feedback: submission.feedback || '',
  }
  gradeModalVisible.value = true
}

async function submitGrade() {
  if (gradeForm.value.score === null) {
    message.error('请输入分数')
    return
  }
  grading.value = true
  try {
    await gradeSubmission(currentSubmission.value.id, {
      score: gradeForm.value.score,
      feedback: gradeForm.value.feedback,
    })
    message.success('批改成功')
    gradeModalVisible.value = false
    fetchSubmissions()
  } catch (e) {
    message.error('批改失败')
  } finally {
    grading.value = false
  }
}

const hasNextSubmission = computed(() => {
  if (!submissions.value || !currentSubmission.value) return false
  const idx = submissions.value.findIndex(s => s.id === currentSubmission.value.id)
  return idx >= 0 && idx < submissions.value.length - 1
})

async function submitGradeAndNext() {
  if (gradeForm.value.score === null) {
    message.error('请输入分数')
    return
  }
  grading.value = true
  try {
    await gradeSubmission(currentSubmission.value.id, {
      score: gradeForm.value.score,
      feedback: gradeForm.value.feedback,
    })
    message.success('批改成功')
    // 自动切换到下一位未批改的提交
    await fetchSubmissions()
    const idx = submissions.value.findIndex(s => s.id === currentSubmission.value.id)
    const nextSub = submissions.value.slice(idx + 1).find(s => s.status === 'submitted')
    if (nextSub) {
      showGradeModal(nextSub)
    } else {
      gradeModalVisible.value = false
      message.info('已全部批改完毕')
    }
  } catch (e) {
    message.error('批改失败')
  } finally {
    grading.value = false
  }
}

function formatTime(time) {
  return dayjs(time).format('YYYY-MM-DD HH:mm')
}

function getStatusColor(status) {
  return { open: 'blue', closed: 'gray', archived: 'default' }[status] || 'default'
}

function getStatusText(status) {
  return { open: '进行中', closed: '已截止', archived: '已归档' }[status] || status
}

function getSubmissionColor(status) {
  return { submitted: 'blue', graded: 'green', returned: 'orange' }[status] || 'default'
}

function getSubmissionText(status) {
  return { submitted: '待批改', graded: '已批改', returned: '已退回' }[status] || status
}

async function handleReturnSubmission(record) {
  const feedback = window.prompt('请输入打回反馈：', '请重做')
  if (feedback === null) return
  try {
    await returnSubmission(record.id, { feedback })
    message.success('已打回，学生可重新提交')
    fetchSubmissions()
  } catch (e) {
    message.error('打回失败')
  }
}

onMounted(() => {
  fetchHomework()
  fetchSubmissions()
})
</script>

<style scoped>
.submission-content {
  max-height: 200px;
  overflow-y: auto;
  padding: 8px;
  background: #f5f5f5;
  border-radius: 4px;
  white-space: pre-wrap;
}
</style>