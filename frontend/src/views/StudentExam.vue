<template>
  <div class="cv-page">
    <a-page-header title="我的考试" sub-title="查看和参加考试" />

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="exams" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'status'">
            <a-tag v-if="record.my_status === 'graded'" color="green">已批改</a-tag>
            <a-tag v-else-if="record.my_status === 'submitted'" color="blue">已提交</a-tag>
            <a-tag v-else-if="record.my_status === 'in_progress'" color="orange">进行中</a-tag>
            <a-tag v-else color="default">未开始</a-tag>
          </template>
          <template v-else-if="column.key === 'action'">
            <a-button v-if="record.my_status === 'graded'" type="link" size="small" @click="viewResult(record.id)">查看成绩</a-button>
            <a-button v-else-if="record.my_status === 'in_progress'" type="primary" size="small" @click="takeExam(record.id)">继续答题</a-button>
            <a-button v-else-if="!record.my_status" type="primary" size="small" @click="confirmStartExam(record)">开始考试</a-button>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 答题弹窗 -->
    <a-modal v-model:open="showExamModal" :title="examDetail?.title" width="800px" :footer="null" :maskClosable="false" :closable="examSubmitted">
      <div v-if="examDetail && !examSubmitted">
        <div style="margin-bottom: 16px; display: flex; justify-content: space-between">
          <span>共 {{ examDetail.questions.length }} 题，总分 {{ examDetail.total_score }} 分</span>
          <span v-if="timeLeft" :style="{ color: timeLeft < 300 ? '#ff4d4f' : '#999' }">剩余时间：{{ formatCountdown(timeLeft) }}</span>
        </div>

        <div v-for="(q, i) in examDetail.questions" :key="q.id" style="margin-bottom: 24px; padding: 16px; background: #fafafa; border-radius: 8px">
          <div style="font-weight: bold; margin-bottom: 12px">
            {{ i + 1 }}. [{{ getTypeText(q.type) }}] {{ q.content }}（{{ q.score }}分）
          </div>

          <!-- 单选题 -->
          <a-radio-group v-if="q.type === 'single'" v-model:value="answers[q.id]" style="width: 100%">
            <a-radio v-for="(opt, oi) in q.options" :key="oi" :value="String(oi)" style="display: block; margin-bottom: 8px">
              {{ String.fromCharCode(65 + oi) }}. {{ opt }}
            </a-radio>
          </a-radio-group>

          <!-- 多选题 -->
          <a-checkbox-group v-else-if="q.type === 'multi'" v-model:value="multiAnswers[q.id]" style="width: 100%">
            <a-checkbox v-for="(opt, oi) in q.options" :key="oi" :value="String(oi)" style="display: block; margin-bottom: 8px">
              {{ String.fromCharCode(65 + oi) }}. {{ opt }}
            </a-checkbox>
          </a-checkbox-group>

          <!-- 判断题 -->
          <a-radio-group v-else-if="q.type === 'judge'" v-model:value="answers[q.id]">
            <a-radio value="true">正确</a-radio>
            <a-radio value="false">错误</a-radio>
          </a-radio-group>

          <!-- 填空题 -->
          <a-input v-else-if="q.type === 'fill'" v-model:value="answers[q.id]" placeholder="请输入答案" />

          <!-- 简答题 -->
          <a-textarea v-else-if="q.type === 'essay'" v-model:value="answers[q.id]" placeholder="请输入答案" :rows="4" />
        </div>

        <a-button type="primary" size="large" block @click="submitExam" :loading="submitting">
          提交考试
        </a-button>
      </div>

      <!-- 提交成功 -->
      <div v-if="examSubmitted" style="text-align: center; padding: 40px 0">
        <a-result status="success" title="考试已提交" :sub-title="submitResult.score != null ? `您的得分：${submitResult.score} 分` : '等待教师批改简答题'">
          <template #extra>
            <a-button type="primary" @click="showExamModal = false">返回</a-button>
          </template>
        </a-result>
      </div>
    </a-modal>

    <!-- 成绩查看弹窗 -->
    <a-modal v-model:open="showResultModal" title="考试成绩" width="700px" :footer="null">
      <div v-if="submissionDetail">
        <a-descriptions bordered size="small" :column="1">
          <a-descriptions-item label="考试">{{ submissionDetail.exam_title }}</a-descriptions-item>
          <a-descriptions-item label="得分">{{ submissionDetail.score ?? '待批改' }}</a-descriptions-item>
        </a-descriptions>

        <div style="margin-top: 16px">
          <div v-for="ans in submissionDetail.answers" :key="ans.question_id" style="margin-bottom: 12px; padding: 12px; background: #fafafa; border-radius: 4px">
            <div><strong>{{ ans.question_content }}</strong></div>
            <div style="margin-top: 4px">你的答案：{{ ans.student_answer }}</div>
            <div v-if="ans.correct_answer != null" style="margin-top: 4px">正确答案：{{ ans.correct_answer }}</div>
            <div style="margin-top: 4px">
              <a-tag :color="ans.is_correct ? 'green' : 'red'">{{ ans.is_correct ? '正确' : '错误' }}</a-tag>
              <span style="margin-left: 8px">{{ ans.score ?? 0 }}分</span>
            </div>
          </div>
        </div>
      </div>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { message, Modal } from 'ant-design-vue'
import api from '../api'
import dayjs from 'dayjs'

const exams = ref([])
const examDetail = ref(null)
const loading = ref(false)
const submitting = ref(false)
const showExamModal = ref(false)
const showResultModal = ref(false)
const examSubmitted = ref(false)
const submissionDetail = ref(null)
const submitResult = ref({})
const answers = reactive({})
const multiAnswers = reactive({})
const timeLeft = ref(null)
let timer = null

const columns = [
  { key: 'title', title: '考试', dataIndex: 'title' },
  { key: 'classroom_name', title: '课堂', dataIndex: 'classroom_name' },
  { key: 'duration', title: '时长', dataIndex: 'duration' },
  { key: 'total_score', title: '总分', dataIndex: 'total_score' },
  { key: 'status', title: '状态' },
  { key: 'action', title: '操作' },
]

function confirmStartExam(record) {
  Modal.confirm({
    title: '确认开始考试？',
    content: `考试「${record.title}」时长 ${record.duration} 分钟，开始后请保持页面不关闭。`,
    okText: '开始考试',
    cancelText: '取消',
    onOk: () => takeExam(record.id),
  })
}

async function fetchExams() {
  loading.value = true
  try {
    const res = await api.get('/exams/assigned')
    exams.value = res.data
  } catch (e) {
    message.error('获取考试列表失败')
  } finally {
    loading.value = false
  }
}

async function takeExam(id) {
  try {
    const startRes = await api.post(`/exams/${id}/start`)
    const detailRes = await api.get(`/exams/${id}`)
    examDetail.value = detailRes.data

    // 尝试从 localStorage 恢复答案
    const saved = localStorage.getItem(`exam_answers_${id}`)
    if (saved) {
      try {
        const parsed = JSON.parse(saved)
        Object.keys(answers).forEach(k => delete answers[k])
        Object.keys(multiAnswers).forEach(k => delete multiAnswers[k])
        if (parsed.answers) Object.assign(answers, parsed.answers)
        if (parsed.multiAnswers) Object.assign(multiAnswers, parsed.multiAnswers)
      } catch { /* ignore */ }
    } else {
      Object.keys(answers).forEach(k => delete answers[k])
      Object.keys(multiAnswers).forEach(k => delete multiAnswers[k])
    }
    examSubmitted.value = false

    // 设置倒计时
    const duration = examDetail.value.duration * 60
    const savedTime = localStorage.getItem(`exam_timeleft_${id}`)
    timeLeft.value = savedTime ? parseInt(savedTime) : duration
    timer = setInterval(() => {
      timeLeft.value--
      // 自动保存进度
      localStorage.setItem(`exam_timeleft_${id}`, String(timeLeft.value))
      localStorage.setItem(`exam_answers_${id}`, JSON.stringify({ answers: { ...answers }, multiAnswers: { ...multiAnswers } }))
      if (timeLeft.value <= 0) {
        clearInterval(timer)
        submitExam()
      }
    }, 1000)

    showExamModal.value = true

    // 防作弊：请求全屏
    try {
      const el = document.documentElement
      if (el.requestFullscreen) el.requestFullscreen()
    } catch { /* ignore */ }
  } catch (e) {
    message.error(e.response?.data?.detail || '开始考试失败')
  }
}

async function submitExam() {
  submitting.value = true
  if (timer) clearInterval(timer)
  
  try {
    const answerList = []
    for (const q of examDetail.value.questions) {
      let content = ''
      if (q.type === 'multi') {
        content = (multiAnswers[q.id] || []).sort().join(',')
      } else {
        content = answers[q.id] || ''
      }
      answerList.push({ question_id: q.id, content })
    }
    
    const res = await api.post(`/exams/${examDetail.value.id}/submit`, answerList)
    submitResult.value = res.data
    examSubmitted.value = true
    // 清除保存的答案
    localStorage.removeItem(`exam_answers_${examDetail.value.id}`)
    localStorage.removeItem(`exam_timeleft_${examDetail.value.id}`)
    // 退出全屏
    try { if (document.fullscreenElement) document.exitFullscreen() } catch { /* ignore */ }
    fetchExams()
  } catch (e) {
    message.error('提交失败')
  } finally {
    submitting.value = false
  }
}

async function viewResult(id) {
  try {
    const res = await api.get(`/exams/my-result/${id}`)
    if (!res.data.submitted) {
      message.info('未找到提交记录')
      return
    }
    submissionDetail.value = res.data
    showResultModal.value = true
  } catch (e) {
    message.error('获取成绩失败')
  }
}

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

function formatCountdown(seconds) {
  const m = Math.floor(seconds / 60)
  const s = seconds % 60
  return `${m}分${s}秒`
}

onUnmounted(() => {
  if (timer) clearInterval(timer)
})

onMounted(fetchExams)
</script>