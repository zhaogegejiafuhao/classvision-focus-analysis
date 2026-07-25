import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useExamComposeStore = defineStore('examCompose', () => {
  // ── 步骤控制 ──
  const currentStep = ref(0)           // 0-2（3步流程）
  const method = ref(null)             // 'ai' | 'manual' | null

  // ── 基本信息（步骤1） ──
  const title = ref('')
  const classroomId = ref(null)
  const templateId = ref(null)
  const duration = ref(90)
  const examType = ref('computer')  // 'computer' | 'paper'

  // ── 组卷结果 ──
  const examId = ref(null)             // 组卷后生成的考试 ID
  const aiResult = ref(null)           // AI 组卷返回的完整结果（含 exam_id, title, question_count 等）

  // ── 审核题目列表（步骤4） ──
  const reviewQuestions = ref([])      // 可编辑分值、换题、删除

  // ── 公共数据（课堂/模板列表） ──
  const templates = ref([])
  const classrooms = ref([])

  // ── 换题数据 ──
  const showSwapModal = ref(false)
  const swapCandidates = ref([])
  const swapTargetIndex = ref(-1)

  // ── 计算属性 ──
  const reviewTotalScore = computed(() =>
    reviewQuestions.value.reduce((sum, q) => sum + (q.scoreOverride || q.score), 0)
  )

  const reviewQuestionCount = computed(() => reviewQuestions.value.length)

  const canNextStep = computed(() => {
    switch (currentStep.value) {
      case 0: return !!method.value && !!title.value.trim()
      case 1: return !!examId.value
      case 2: return reviewQuestions.value.length > 0
      default: return true
    }
  })

  const difficultyDistribution = computed(() => {
    const dist = {}
    for (const q of reviewQuestions.value) {
      const d = q.difficulty || 2
      dist[d] = (dist[d] || 0) + 1
    }
    const total = reviewQuestions.value.length || 1
    const colors = { 1: '#52c41a', 2: '#73d13d', 3: '#faad14', 4: '#ff7a45', 5: '#ff4d4f' }
    const labels = { 1: '简单', 2: '较易', 3: '中等', 4: '较难', 5: '困难' }
    return Object.entries(dist).sort((a, b) => a[0] - b[0]).map(([level, count]) => ({
      level: Number(level),
      count,
      percent: Math.round(count / total * 100),
      color: colors[level] || '#ccc',
      label: labels[level] || `${level}星`,
    }))
  })

  // ── 方法 ──
  function setStep(step) {
    currentStep.value = step
  }

  function setMethod(m) {
    method.value = m
  }

  function reset() {
    currentStep.value = 0
    method.value = null
    title.value = ''
    classroomId.value = null
    templateId.value = null
    duration.value = 90
    examType.value = 'computer'
    examId.value = null
    aiResult.value = null
    reviewQuestions.value = []
    showSwapModal.value = false
    swapCandidates.value = []
    swapTargetIndex.value = -1
  }

  // AI 组卷成功后设置数据
  function setAIResult(result) {
    aiResult.value = result
    examId.value = result.exam_id
    reviewQuestions.value = result.questions.map(q => ({
      ...q,
      scoreOverride: q.suggested_score || q.score,
      expanded: false,
      swapping: false,
    }))
  }

  // 人工组卷成功后设置数据
  function setManualResult(exam_id, questions) {
    examId.value = exam_id
    reviewQuestions.value = questions.map(q => ({
      ...q,
      scoreOverride: q.score,
      suggested_score: q.score,
      expanded: false,
      swapping: false,
    }))
  }

  // 删除审核题目
  function removeReviewQuestion(idx) {
    reviewQuestions.value.splice(idx, 1)
    reviewQuestions.value.forEach((q, i) => { q.order = i + 1 })
  }

  // 换题替换
  function replaceReviewQuestion(idx, newQ) {
    const oldQ = reviewQuestions.value[idx]
    reviewQuestions.value[idx] = {
      ...newQ,
      order: oldQ.order,
      scoreOverride: oldQ.scoreOverride,
      suggested_score: newQ.score,
      expanded: false,
      swapping: false,
    }
  }

  // 收集审核修改，供发布 API 使用
  function collectPublishPayload() {
    const scoreOverrides = {}
    for (const q of reviewQuestions.value) {
      if (q.scoreOverride !== q.score && q.scoreOverride !== q.suggested_score) {
        // 使用 Question 表的 id（而非 bank_id）
        scoreOverrides[q.id] = q.scoreOverride
      }
    }
    return {
      score_overrides: Object.keys(scoreOverrides).length > 0 ? scoreOverrides : null,
      remove_question_ids: null,
      swap_questions: null,
      title: title.value || null,
      duration: duration.value || null,
      exam_type: examType.value,
    }
  }

  return {
    currentStep, method, title, classroomId, templateId, duration, examType,
    examId, aiResult, reviewQuestions,
    templates, classrooms,
    showSwapModal, swapCandidates, swapTargetIndex,
    reviewTotalScore, reviewQuestionCount, canNextStep, difficultyDistribution,
    setStep, setMethod, reset,
    setAIResult, setManualResult,
    removeReviewQuestion, replaceReviewQuestion,
    collectPublishPayload,
  }
})
