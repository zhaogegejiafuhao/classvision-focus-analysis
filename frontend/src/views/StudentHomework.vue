<template>
  <div class="cv-page">
    <a-page-header title="我的作业" sub-title="查看和提交作业" />

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="homeworks" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'title'">
            <a @click="goDetail(record.id)">{{ record.title }}</a>
          </template>
          <template v-else-if="column.key === 'deadline'">
            <span :class="{ 'deadline-passed': isDeadlinePassed(record.deadline) }">
              {{ record.deadline ? formatTime(record.deadline) : '无截止时间' }}
            </span>
          </template>
          <template v-else-if="column.key === 'status'">
            <a-tag v-if="record.my_status === 'graded'" color="green">已批改</a-tag>
            <a-tag v-else-if="record.my_status === 'submitted'" color="blue">已提交</a-tag>
            <a-tag v-else-if="record.my_status === 'returned'" color="orange">已退回</a-tag>
            <a-tag v-else-if="isDeadlinePassed(record.deadline)" color="red">已截止</a-tag>
            <a-tag v-else color="orange">待提交</a-tag>
          </template>
          <template v-else-if="column.key === 'action'">
            <a-button type="link" size="small" @click="goDetail(record.id)">查看</a-button>
            <a-button v-if="!isDeadlinePassed(record.deadline) && record.my_status !== 'graded'" type="link" size="small" @click="showExtModal(record)">申请延期</a-button>
          </template>
          <template v-else-if="column.key === 'score'">
            <span v-if="record.my_score != null">{{ record.my_score }} / {{ record.total_score }}</span>
            <span v-else>-</span>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 作业详情/提交弹窗 -->
    <a-modal v-model:open="showDetailModal" :title="currentHomework?.title" width="700px" :footer="null">
      <div v-if="currentHomework">
        <a-descriptions bordered size="small" :column="1">
          <a-descriptions-item label="描述">{{ currentHomework.description || '无' }}</a-descriptions-item>
          <a-descriptions-item label="教师">{{ currentHomework.teacher_name }}</a-descriptions-item>
          <a-descriptions-item label="截止时间">{{ currentHomework.deadline ? formatTime(currentHomework.deadline) : '无' }}</a-descriptions-item>
          <a-descriptions-item label="总分">{{ currentHomework.total_score }}分</a-descriptions-item>
        </a-descriptions>

        <!-- 已提交状态 -->
        <div v-if="mySubmission.submitted" style="margin-top: 16px">
          <a-alert v-if="mySubmission.submission.status === 'graded'" type="success" :message="`得分：${mySubmission.submission.score} / ${currentHomework.total_score}`" style="margin-bottom: 8px" />
          <div v-if="mySubmission.submission.feedback" style="margin-top: 8px; padding: 8px; background: #f6ffed; border-radius: 4px">
            <strong>教师评语：</strong>{{ mySubmission.submission.feedback }}
          </div>
          <div style="margin-top: 8px">
            <strong>我的提交：</strong>
            <div style="padding: 8px; background: #f5f5f5; border-radius: 4px; margin-top: 4px; white-space: pre-wrap">{{ mySubmission.submission.content }}</div>
          </div>

          <!-- AI批改详情区域 -->
          <template v-if="mySubmission.submission.status === 'graded' && mySubmission.gradingResult">
            <a-divider>AI批改详情</a-divider>
            <CorrectionForm
              v-if="!mySubmission.correctionSubmitted"
              :submission-id="mySubmission.submission.id"
              @submitted="onCorrectionSubmitted"
            />
            <CorrectionComparison
              v-else-if="mySubmission.correctionId"
              :correction-id="mySubmission.correctionId"
            />
            <SimilarQuestionPanel
              v-if="mySubmission.gradingResult.knowledge_points?.length || mySubmission.gradingResult.error_cause"
              :question="currentHomework.title"
              :knowledge-points="mySubmission.gradingResult.knowledge_points || []"
              :error-type="mySubmission.gradingResult.error_cause || mySubmission.gradingResult.error_type || ''"
            />
          </template>
        </div>

        <!-- 提交表单 -->
        <div v-if="!mySubmission.submitted || (mySubmission.submitted && mySubmission.submission.status === 'submitted')" style="margin-top: 16px">
          <a-divider>提交作业</a-divider>
          <a-textarea v-model:value="submitContent" placeholder="输入作业内容..." :rows="6" />
          <a-button type="primary" @click="handleSubmitHomework" :loading="submitting" style="margin-top: 8px" :disabled="isDeadlinePassed(currentHomework.deadline)">
            {{ mySubmission.submitted ? '重新提交' : '提交作业' }}
          </a-button>
          <span v-if="isDeadlinePassed(currentHomework.deadline)" style="margin-left: 8px; color: #ff4d4f">已过截止时间</span>
        </div>
      </div>
    </a-modal>

    <!-- 延期申请弹窗 -->
    <a-modal v-model:open="extModalVisible" title="申请作业延期" @ok="submitExtension" :confirm-loading="extSubmitting">
      <a-form layout="vertical">
        <a-form-item label="延期至" required>
          <a-date-picker v-model:value="extForm.requested_deadline" show-time style="width: 100%" />
        </a-form-item>
        <a-form-item label="申请原因" required>
          <a-textarea v-model:value="extForm.reason" :rows="3" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import dayjs from 'dayjs'
import { listAssignedHomework, getMySubmission, submitHomework, createExtension } from '@/api/homework'
import { getGradingResult } from '@/api/grading'
import CorrectionForm from '@/components/correction/CorrectionForm.vue'
import CorrectionComparison from '@/components/correction/CorrectionComparison.vue'
import SimilarQuestionPanel from '@/components/similar-questions/SimilarQuestionPanel.vue'

const homeworks = ref([])
const loading = ref(false)
const submitting = ref(false)
const showDetailModal = ref(false)
const currentHomework = ref(null)
const mySubmission = ref({ submitted: false })
const submitContent = ref('')

const columns = [
  { key: 'title', title: '标题', dataIndex: 'title' },
  { key: 'teacher_name', title: '教师', dataIndex: 'teacher_name' },
  { key: 'deadline', title: '截止时间', dataIndex: 'deadline' },
  { key: 'status', title: '状态' },
  { key: 'score', title: '得分' },
  { key: 'action', title: '操作' },
]

const extModalVisible = ref(false)
const extForm = ref({ homework_id: null, reason: '', requested_deadline: null })
const extSubmitting = ref(false)

function showExtModal(record) {
  extForm.value = { homework_id: record.id, reason: '', requested_deadline: null }
  extModalVisible.value = true
}

async function submitExtension() {
  if (!extForm.value.reason || !extForm.value.requested_deadline) {
    message.warning('请填写完整')
    return
  }
  extSubmitting.value = true
  try {
    await createExtension({
      homework_id: extForm.value.homework_id,
      reason: extForm.value.reason,
      requested_deadline: extForm.value.requested_deadline.toISOString(),
    })
    message.success('延期申请已提交')
    extModalVisible.value = false
  } catch (e) {
    message.error('提交失败')
  } finally {
    extSubmitting.value = false
  }
}

async function fetchHomeworks() {
  loading.value = true
  try {
    const res = await listAssignedHomework()
    // 获取每个作业的提交状态
    homeworks.value = await Promise.all(res.data.map(async hw => {
      try {
        const subRes = await getMySubmission(hw.id)
        const myStatus = subRes.data.submitted ? subRes.data.submission.status : null
        const myScore = subRes.data.submitted ? subRes.data.submission.score : null
        return { ...hw, my_status: myStatus, my_score: myScore }
      } catch {
        return { ...hw, my_status: null, my_score: null }
      }
    }))
  } catch (e) {
    message.error('获取作业列表失败')
  } finally {
    loading.value = false
  }
}

async function goDetail(id) {
  const hw = homeworks.value.find(h => h.id === id)
  if (!hw) return
  currentHomework.value = hw
  submitContent.value = ''

  // 获取提交状态
  try {
    const res = await getMySubmission(id)
    mySubmission.value = res.data
    if (res.data.submitted) {
      submitContent.value = res.data.submission.content
      // 如果已批改，获取AI批改结果
      if (res.data.submission.status === 'graded') {
        try {
          const gradingRes = await getGradingResult(res.data.submission.id)
          mySubmission.value.gradingResult = gradingRes.data
        } catch { /* 批改结果获取失败不影响主流程 */ }
      }
    }
  } catch {
    mySubmission.value = { submitted: false }
  }

  showDetailModal.value = true
}

async function handleSubmitHomework() {
  if (!submitContent.value.trim()) {
    message.error('请输入作业内容')
    return
  }
  submitting.value = true
  try {
    await submitHomework(currentHomework.value.id, {
      content: submitContent.value,
    })
    message.success('提交成功')
    showDetailModal.value = false
    fetchHomeworks()
  } catch (e) {
    message.error(e.response?.data?.detail || '提交失败')
  } finally {
    submitting.value = false
  }
}

function formatTime(time) {
  return dayjs(time).format('YYYY-MM-DD HH:mm')
}

function isDeadlinePassed(deadline) {
  return deadline && dayjs(deadline).isBefore(dayjs())
}

function onCorrectionSubmitted() {
  message.success('订正已提交，请等待二次批改')
  mySubmission.value.correctionSubmitted = true
  // 关闭弹窗并刷新
  showDetailModal.value = false
  fetchHomeworks()
}

onMounted(fetchHomeworks)
</script>

<style scoped>
.deadline-passed {
  color: #ff4d4f;
}
</style>
