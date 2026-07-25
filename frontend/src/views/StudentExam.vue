<template>
  <div class="cv-page">
    <a-page-header title="我的考试" sub-title="查看和参加考试" />

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="exams" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'exam_type'">
            <a-tag :color="record.exam_type === 'paper' ? '#722ed1' : '#1890ff'">
              {{ record.exam_type === 'paper' ? '📝 笔试' : '💻 机试' }}
            </a-tag>
          </template>
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
    <a-modal
      v-model:open="showExamModal"
      :title="examDetail?.title"
      width="900px"
      :footer="null"
      :maskClosable="false"
      :closable="examSubmitted"
      :destroyOnClose="true"
    >
      <div v-if="examDetail && !examSubmitted" class="exam-taking">
        <!-- 顶部信息栏 -->
        <div class="exam-topbar">
          <div class="exam-topbar-left">
            <a-tag :color="examDetail.exam_type === 'paper' ? '#722ed1' : '#1890ff'">
              {{ examDetail.exam_type === 'paper' ? '📝 笔试' : '💻 机试' }}
            </a-tag>
            <span>共 {{ examDetail.questions.length }} 题，总分 {{ examDetail.total_score }} 分</span>
          </div>
          <div class="exam-topbar-right">
            <span v-if="cameraActive" class="camera-status">
              <span class="camera-dot"></span> 监控中
              <a-badge v-if="violationCount > 0" :count="viulationCount" :overflow-count="99" style="margin-left: 4px" />
            </span>
            <span v-if="timeLeft" class="countdown" :class="{ 'countdown-urgent': timeLeft < 300 }">
              ⏱ {{ formatCountdown(timeLeft) }}
            </span>
          </div>
        </div>

        <!-- 笔试提示 -->
        <a-alert
          v-if="examDetail.exam_type === 'paper'"
          type="warning"
          show-icon
          style="margin-bottom: 12px"
          message="笔试模式：请对每道题拍照上传答案，系统同时启动摄像头作弊检测"
        />

        <!-- 题目列表 -->
        <div class="exam-questions">
          <div v-for="(q, i) in examDetail.questions" :key="q.id" class="exam-question-card">
            <div class="question-header">
              <span class="question-index">{{ i + 1 }}.</span>
              <a-tag size="small">{{ getTypeText(q.type) }}</a-tag>
              <LatexText :content="q.content" class="question-content" />
              <span class="question-score">（{{ q.score }}分）</span>
            </div>

            <!-- ═══ 单选题 ═══ -->
            <template v-if="q.type === 'single'">
              <a-radio-group v-model:value="answers[q.id]" style="width: 100%">
                <a-radio v-for="(opt, oi) in q.options" :key="oi" :value="String(oi)" style="display: block; margin-bottom: 8px">
                  {{ String.fromCharCode(65 + oi) }}. <LatexText :content="opt" />
                </a-radio>
              </a-radio-group>
              <!-- 笔试：必须上传答案照片 -->
              <AnswerImageUpload
                v-if="examDetail.exam_type === 'paper'"
                v-model:imageUrls="answerImages[q.id]"
                :required="true"
              />
            </template>

            <!-- ═══ 多选题 ═══ -->
            <template v-else-if="q.type === 'multi'">
              <a-checkbox-group v-model:value="multiAnswers[q.id]" style="width: 100%">
                <a-checkbox v-for="(opt, oi) in q.options" :key="oi" :value="String(oi)" style="display: block; margin-bottom: 8px">
                  {{ String.fromCharCode(65 + oi) }}. <LatexText :content="opt" />
                </a-checkbox>
              </a-checkbox-group>
              <AnswerImageUpload
                v-if="examDetail.exam_type === 'paper'"
                v-model:imageUrls="answerImages[q.id]"
                :required="true"
              />
            </template>

            <!-- ═══ 判断题 ═══ -->
            <template v-else-if="q.type === 'judge'">
              <a-radio-group v-model:value="answers[q.id]">
                <a-radio value="true">正确</a-radio>
                <a-radio value="false">错误</a-radio>
              </a-radio-group>
              <AnswerImageUpload
                v-if="examDetail.exam_type === 'paper'"
                v-model:imageUrls="answerImages[q.id]"
                :required="true"
              />
            </template>

            <!-- ═══ 填空题 ═══ -->
            <template v-else-if="q.type === 'fill'">
              <a-input
                v-model:value="answers[q.id]"
                :placeholder="isPaperExam ? '（可选）可在此输入答案' : '请输入答案'"
                :style="isPaperExam ? 'opacity: 0.7' : ''"
              />
              <AnswerImageUpload
                v-model:imageUrls="answerImages[q.id]"
                :required="isPaperExam"
              />
            </template>

            <!-- ═══ 简答题 ═══ -->
            <template v-else-if="q.type === 'essay'">
              <a-textarea
                v-model:value="answers[q.id]"
                :placeholder="isPaperExam ? '（可选）可在此输入答案' : '请输入答案'"
                :rows="4"
                :style="isPaperExam ? 'opacity: 0.7' : ''"
              />
              <AnswerImageUpload
                v-model:imageUrls="answerImages[q.id]"
                :required="isPaperExam"
              />
            </template>
          </div>
        </div>

        <!-- 提交按钮 -->
        <div class="exam-submit-area">
          <a-button type="primary" size="large" block @click="handleSubmitExam" :loading="submitting" :disabled="!canSubmit">
            提交考试
          </a-button>
          <p v-if="isPaperExam && !canSubmit" class="submit-hint">
            ⚠️ 笔试模式下，每道题必须上传至少一张答案照片
          </p>
        </div>
      </div>

      <!-- 提交成功 -->
      <div v-if="examSubmitted" style="text-align: center; padding: 40px 0">
        <a-result status="success" title="考试已提交">
          <template #subTitle>
            <div v-if="submitResult.score != null">
              您的得分：{{ submitResult.score }} 分
            </div>
            <div v-else-if="submissionStatus === 'graded'">
              您的得分：{{ finalScore }} 分
            </div>
            <div v-else>
              <a-spin size="small" />
              <span style="margin-left: 8px">批改中，请耐心等待...</span>
            </div>
          </template>
          <template #extra>
            <a-button type="primary" @click="closeExamModal">返回</a-button>
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
            <div><strong><LatexText :content="ans.question_content" /></strong></div>
            <div style="margin-top: 4px">你的答案：{{ formatAnswer(ans.student_answer, ans.question_type) }}</div>
            <!-- 显示图片答案 -->
            <div v-if="ans.image_urls && ans.image_urls.length" style="margin-top: 6px">
              <span style="color: #999; font-size: 12px">图片答案：</span>
              <a-image-preview-group>
                <a-image v-for="(url, idx) in ans.image_urls" :key="idx" :src="url" :width="80" :height="60" style="border-radius: 4px; object-fit: cover; margin-right: 4px" />
              </a-image-preview-group>
            </div>
            <div v-if="ans.correct_answer != null" style="margin-top: 4px">正确答案：{{ formatAnswer(ans.correct_answer, ans.question_type) }}</div>
            <div style="margin-top: 4px">
              <a-tag :color="ans.is_correct ? 'green' : 'red'">{{ ans.is_correct ? '正确' : '错误' }}</a-tag>
              <span style="margin-left: 8px">{{ ans.score ?? 0 }}分</span>
            </div>
          </div>
        </div>
      </div>
    </a-modal>

    <!-- 浮动摄像头监控窗口 -->
    <div v-if="showExamModal && !examSubmitted && cameraActive" class="camera-float" @click="toggleCameraExpand">
      <video ref="cameraVideoRef" autoplay muted playsinline style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px" />
      <div class="camera-float-badge">
        <span class="camera-dot"></span>
        <span v-if="violationCount > 0" class="violation-count">{{ violationCount }}</span>
        <span v-else>监控中</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { message, Modal } from 'ant-design-vue'
import { listAssignedExams, getExam, startExam, submitExam, getMyExamResult } from '@/api/exam'
import { useExamCamera } from '@/composables/useExamCamera'
import AnswerImageUpload from '@/components/AnswerImageUpload.vue'
import LatexText from '@/components/LatexText.vue'

// ── 基础数据 ──
const exams = ref([])
const examDetail = ref(null)
const loading = ref(false)
const submitting = ref(false)
const showExamModal = ref(false)
const showResultModal = ref(false)
const examSubmitted = ref(false)
const submissionDetail = ref(null)
const submitResult = ref({})
const submissionStatus = ref('')  // ai_grading / ai_graded / graded
const finalScore = ref(null)
let statusTimer = null
const answers = reactive({})
const multiAnswers = reactive({})
const answerImages = reactive({})  // { [questionId]: [url1, url2, ...] }
const timeLeft = ref(null)
let timer = null

// ── 摄像头 ──
const currentExamId = ref(null)
const currentClassroomId = ref(null)
const { cameraActive, violationCount, violations, startCamera, stopCamera } = useExamCamera(
  computed(() => currentClassroomId.value),
  computed(() => currentExamId.value),
)
const cameraVideoRef = ref(null)

// ── 计算属性 ──
const isPaperExam = computed(() => examDetail.value?.exam_type === 'paper')

const canSubmit = computed(() => {
  if (!examDetail.value) return false
  if (isPaperExam.value) {
    // 笔试模式：每道题必须上传至少一张图片
    return examDetail.value.questions.every(q => {
      const images = answerImages[q.id] || []
      return images.length > 0
    })
  }
  return true
})

const columns = [
  { key: 'title', title: '考试', dataIndex: 'title' },
  { key: 'classroom_name', title: '课堂', dataIndex: 'classroom_name' },
  { key: 'exam_type', title: '类型' },
  { key: 'duration', title: '时长', dataIndex: 'duration' },
  { key: 'total_score', title: '总分', dataIndex: 'total_score' },
  { key: 'status', title: '状态' },
  { key: 'action', title: '操作' },
]

// ── 方法 ──

function confirmStartExam(record) {
  const typeHint = record.exam_type === 'paper' ? '（笔试模式，需要拍照上传答案）' : ''
  Modal.confirm({
    title: '确认开始考试？',
    content: `考试「${record.title}」时长 ${record.duration} 分钟${typeHint}，开始后将启动摄像头监控，请保持页面不关闭。`,
    okText: '开始考试',
    cancelText: '取消',
    onOk: () => takeExam(record.id, record.classroom_id),
  })
}

async function fetchExams() {
  loading.value = true
  try {
    const res = await listAssignedExams()
    exams.value = res.data
  } catch (e) {
    message.error('获取考试列表失败')
  } finally {
    loading.value = false
  }
}

async function takeExam(id, classroomId) {
  try {
    const startRes = await startExam(id)
    const detailRes = await getExam(id)
    examDetail.value = detailRes.data

    // 设置摄像头参数
    currentExamId.value = id
    currentClassroomId.value = classroomId || detailRes.data.classroom_id

    // 尝试从 localStorage 恢复答案
    const saved = localStorage.getItem(`exam_answers_${id}`)
    if (saved) {
      try {
        const parsed = JSON.parse(saved)
        Object.keys(answers).forEach(k => delete answers[k])
        Object.keys(multiAnswers).forEach(k => delete multiAnswers[k])
        Object.keys(answerImages).forEach(k => delete answerImages[k])
        if (parsed.answers) Object.assign(answers, parsed.answers)
        if (parsed.multiAnswers) Object.assign(multiAnswers, parsed.multiAnswers)
        if (parsed.answerImages) Object.assign(answerImages, parsed.answerImages)
      } catch { /* ignore */ }
    } else {
      Object.keys(answers).forEach(k => delete answers[k])
      Object.keys(multiAnswers).forEach(k => delete multiAnswers[k])
      Object.keys(answerImages).forEach(k => delete answerImages[k])
      // 初始化每题的图片数组
      for (const q of examDetail.value.questions) {
        answerImages[q.id] = []
      }
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
      localStorage.setItem(`exam_answers_${id}`, JSON.stringify({
        answers: { ...answers },
        multiAnswers: { ...multiAnswers },
        answerImages: { ...answerImages },
      }))
      if (timeLeft.value <= 0) {
        clearInterval(timer)
        handleSubmitExam()
      }
    }, 1000)

    showExamModal.value = true

    // 启动摄像头
    await nextTick()
    if (cameraVideoRef.value) {
      startCamera(cameraVideoRef.value)
    }

    // 防作弊：请求全屏
    try {
      const el = document.documentElement
      if (el.requestFullscreen) el.requestFullscreen()
    } catch { /* ignore */ }
  } catch (e) {
    message.error(e.response?.data?.detail || '开始考试失败')
  }
}

async function handleSubmitExam() {
  submitting.value = true
  if (timer) clearInterval(timer)

  // 笔试模式检查
  if (isPaperExam.value && !canSubmit.value) {
    message.error('笔试模式下，每道题必须上传至少一张答案照片')
    submitting.value = false
    return
  }

  try {
    const answerList = []
    for (const q of examDetail.value.questions) {
      let content = ''
      if (q.type === 'multi') {
        content = (multiAnswers[q.id] || []).sort().join(',')
      } else {
        content = answers[q.id] || ''
      }
      const images = answerImages[q.id] || []
      answerList.push({
        question_id: q.id,
        content,
        image_urls: images,
      })
    }

    const res = await submitExam(examDetail.value.id, answerList)
    submitResult.value = res.data
    examSubmitted.value = true

    // 清除保存的答案
    localStorage.removeItem(`exam_answers_${examDetail.value.id}`)
    localStorage.removeItem(`exam_timeleft_${examDetail.value.id}`)

    // 停止摄像头
    stopCamera()

    // 退出全屏
    try { if (document.fullscreenElement) document.exitFullscreen() } catch { /* ignore */ }
    fetchExams()

    // 含主观题时启动轮询，等待 AI 批改 + 教师审核
    if (res.data.has_subjective) {
      submissionStatus.value = 'ai_grading'
      pollSubmissionStatus(examDetail.value.id)
    }
  } catch (e) {
    message.error('提交失败')
  } finally {
    submitting.value = false
  }
}

async function pollSubmissionStatus(examId) {
  try {
    const res = await getMyExamResult(examId)
    if (res.data && res.data.submitted) {
      submissionStatus.value = res.data.status
      if (res.data.status === 'graded') {
        finalScore.value = res.data.score
        if (statusTimer) {
          clearTimeout(statusTimer)
          statusTimer = null
        }
        return
      }
    }
    statusTimer = setTimeout(() => pollSubmissionStatus(examId), 3000)
  } catch (e) {
    // 静默重试
    statusTimer = setTimeout(() => pollSubmissionStatus(examId), 5000)
  }
}

function closeExamModal() {
  showExamModal.value = false
  stopCamera()
  if (statusTimer) {
    clearTimeout(statusTimer)
    statusTimer = null
  }
}

async function viewResult(id) {
  try {
    const res = await getMyExamResult(id)
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

function formatAnswer(answer, questionType) {
  if (!answer && answer !== 0) return '（未作答）'
  const str = String(answer).trim()
  if (!str) return '（未作答）'
  if (questionType === 'single') {
    if (/^\d+$/.test(str)) return String.fromCharCode(65 + parseInt(str))
    return str
  }
  if (questionType === 'multi') {
    return str.split(',').map(s => { const t = s.trim(); return /^\d+$/.test(t) ? String.fromCharCode(65 + parseInt(t)) : t }).join(',')
  }
  if (questionType === 'judge') {
    return str.toLowerCase() === 'true' ? '正确' : '错误'
  }
  return str
}

function formatCountdown(seconds) {
  const m = Math.floor(seconds / 60)
  const s = seconds % 60
  return `${m}分${s}秒`
}

function toggleCameraExpand() {
  // 预留：点击浮动窗口可放大/缩小
}

// 监听弹窗关闭时停止摄像头
watch(showExamModal, (val) => {
  if (!val && cameraActive.value) {
    stopCamera()
  }
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
  if (statusTimer) clearTimeout(statusTimer)
  if (cameraActive.value) stopCamera()
})

onMounted(fetchExams)
</script>

<style scoped>
.exam-taking {
  max-height: 70vh;
  overflow-y: auto;
}

.exam-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  padding: 8px 12px;
  background: #f0f2f5;
  border-radius: 8px;
}

.exam-topbar-left {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
}

.exam-topbar-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.camera-status {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #52c41a;
}

.camera-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #52c41a;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.4; }
  100% { opacity: 1; }
}

.countdown {
  font-size: 14px;
  font-weight: 600;
  color: #999;
  font-variant-numeric: tabular-nums;
}

.countdown-urgent {
  color: #ff4d4f;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.exam-questions {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.exam-question-card {
  padding: 16px;
  background: #fafafa;
  border-radius: 8px;
  border: 1px solid #f0f0f0;
  transition: border-color 0.2s;
}

.exam-question-card:hover {
  border-color: #d9d9d9;
}

.question-header {
  display: flex;
  align-items: baseline;
  gap: 6px;
  margin-bottom: 12px;
  font-weight: bold;
}

.question-index {
  font-size: 15px;
}

.question-content {
  flex: 1;
}

.question-score {
  color: #3751FE;
  font-size: 13px;
  white-space: nowrap;
}

.exam-submit-area {
  margin-top: 20px;
}

.submit-hint {
  text-align: center;
  color: #ff4d4f;
  font-size: 13px;
  margin-top: 8px;
}

/* 浮动摄像头窗口 */
.camera-float {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 180px;
  height: 135px;
  background: #000;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  z-index: 1000;
  cursor: pointer;
  border: 2px solid #52c41a;
}

.camera-float-badge {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.6);
  color: #fff;
  font-size: 11px;
  padding: 2px 8px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.camera-float-badge .camera-dot {
  width: 6px;
  height: 6px;
}

.violation-count {
  background: #ff4d4f;
  color: #fff;
  border-radius: 10px;
  padding: 0 6px;
  font-size: 11px;
  font-weight: bold;
}
</style>
