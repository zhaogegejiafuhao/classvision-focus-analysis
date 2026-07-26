/**
 * 考试审核页业务逻辑（从 ExamReviewPage.vue 抽取）
 *
 * 涵盖：审核数据加载/轮询、教师评分/确认/提交、重新 AI 批改、
 * 导出报告、统计仪表盘、批量确认。
 */
import { ref, reactive, computed, watch, onMounted, onUnmounted } from 'vue'
import { message, Modal } from 'ant-design-vue'
import { useRoute } from 'vue-router'
import {
  getExamReviewData,
  confirmAnswer,
  submitExamReview,
  regradeSubmission,
  exportReviewReport,
  getReviewStats,
  batchConfirmReview,
} from '@/api/exam'

export function useExamReview() {
  const route = useRoute()
  const examId = route.params.id

  // ===== 核心数据 =====
  const reviewData = ref(null)
  const loading = ref(false)
  const submitting = ref(false)
  const regrading = ref(false)
  const currentQuestionId = ref(null)
  const confirmingIds = reactive({})  // answer_id -> loading

  // 教师评分输入
  const teacherScores = reactive({})  // answer_id -> score
  const teacherComments = reactive({})  // answer_id -> comment

  let pollTimer = null

  // ===== 计算属性 =====
  const currentQuestion = computed(() => {
    if (!reviewData.value || !currentQuestionId.value) return null
    return reviewData.value.questions.find(q => q.question_id === currentQuestionId.value)
  })

  const currentIndex = computed(() => {
    if (!reviewData.value || !currentQuestionId.value) return -1
    return reviewData.value.questions.findIndex(q => q.question_id === currentQuestionId.value)
  })

  const reviewProgressPct = computed(() => {
    if (!reviewData.value) return 0
    const { confirmed, total } = reviewData.value.review_progress
    return total > 0 ? Math.round((confirmed / total) * 100) : 0
  })

  const hasAiGradingSubmissions = computed(() => {
    if (!reviewData.value) return false
    // 检查是否有 ai_status 为 pending/processing/failed 的答案
    return reviewData.value.questions.some(q =>
      q.answers.some(a => ['pending', 'processing', 'failed'].includes(a.ai_status) && !a.teacher_confirmed)
    )
  })

  const currentQuestionHasAiScore = computed(() => {
    if (!currentQuestion.value) return false
    return currentQuestion.value.answers.some(a => a.ai_score != null && !a.teacher_confirmed)
  })

  const canSaveCurrentQuestion = computed(() => {
    if (!currentQuestion.value) return false
    return currentQuestion.value.answers.some(a =>
      teacherScores[a.answer_id] != null && !a.teacher_confirmed
    )
  })

  const canSubmitAll = computed(() => {
    if (!reviewData.value) return false
    return reviewData.value.questions.some(q =>
      q.answers.some(a => !a.teacher_confirmed && teacherScores[a.answer_id] != null)
    )
  })

  // 所有提交列表（去重）
  const allSubmissions = computed(() => {
    if (!reviewData.value) return []
    const seen = new Map()
    for (const q of reviewData.value.questions) {
      for (const a of q.answers) {
        if (!seen.has(a.submission_id)) {
          seen.set(a.submission_id, {
            submission_id: a.submission_id,
            student_name: a.student_name,
          })
        }
      }
    }
    return Array.from(seen.values())
  })

  // ===== 数据加载与轮询 =====
  async function fetchReviewData() {
    loading.value = true
    try {
      const res = await getExamReviewData(examId)
      reviewData.value = res.data
      // 默认选第一题
      if (res.data.questions.length && !currentQuestionId.value) {
        currentQuestionId.value = res.data.questions[0].question_id
      }
      // 初始化教师评分输入
      for (const q of res.data.questions) {
        for (const a of q.answers) {
          if (teacherScores[a.answer_id] == null) {
            // 已确认的用 teacher_score，未确认的预填 ai_score
            teacherScores[a.answer_id] = a.teacher_confirmed
              ? a.teacher_score
              : (a.ai_score ?? null)
          }
          if (teacherComments[a.answer_id] == null) {
            teacherComments[a.answer_id] = a.teacher_comment || ''
          }
        }
      }
      // 若有 AI 批改中的题，启动轮询
      maybeStartPolling()
    } catch (e) {
      const msg = e?.response?.data?.detail || '获取审核数据失败'
      message.error(msg)
    } finally {
      loading.value = false
    }
  }

  function maybeStartPolling() {
    if (!reviewData.value) return
    const hasProcessing = reviewData.value.questions.some(q =>
      q.answers.some(a => a.ai_status === 'pending' || a.ai_status === 'processing')
    )
    if (hasProcessing && !pollTimer) {
      pollTimer = setTimeout(async () => {
        pollTimer = null
        await fetchReviewData()
      }, 3000)
    }
  }

  function refreshData() {
    fetchReviewData()
  }

  // ===== UI 辅助 =====
  function selectQuestion(qid) {
    currentQuestionId.value = qid
  }

  function getTypeText(type) {
    return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
  }

  function getTypeColor(type) {
    return { essay: 'orange', fill: 'blue' }[type] || 'default'
  }

  function getQuestionConfirmedCount(q) {
    return q.answers.filter(a => a.teacher_confirmed).length
  }

  function getQuestionPendingCount(q) {
    return q.answers.filter(a => !a.teacher_confirmed).length
  }

  function adoptAiScore(ans) {
    if (ans.ai_score == null) {
      message.warning('AI 分数不存在')
      return
    }
    teacherScores[ans.answer_id] = ans.ai_score
  }

  function adoptAllAiScoreForQuestion() {
    if (!currentQuestion.value) return
    let count = 0
    for (const a of currentQuestion.value.answers) {
      if (!a.teacher_confirmed && a.ai_score != null) {
        teacherScores[a.answer_id] = a.ai_score
        count++
      }
    }
    if (count > 0) {
      message.success(`已采用 ${count} 个 AI 分数，请点击"确认"或"提交全部审核"`)
    } else {
      message.info('没有可采用的 AI 分数')
    }
  }

  // ===== 确认 / 保存 / 提交 =====
  async function confirmSingle(ans) {
    const score = teacherScores[ans.answer_id]
    if (score == null) {
      message.warning('请先填入分数')
      return
    }
    confirmingIds[ans.answer_id] = true
    try {
      await confirmAnswer(ans.submission_id, ans.answer_id, {
        teacher_score: score,
        teacher_comment: teacherComments[ans.answer_id] || null,
        adopt_ai_score: false,
      })
      message.success(`已确认 ${ans.student_name} 的答案`)
      await fetchReviewData()
    } catch (e) {
      const msg = e?.response?.data?.detail || '确认失败'
      message.error(msg)
    } finally {
      confirmingIds[ans.answer_id] = false
    }
  }

  async function unconfirmSingle(ans) {
    // 通过设置为 false 实现"撤销确认"——前端标记，最终提交时按当前 teacher_score 重新写
    // 简化处理：仅在前端标记为未确认，下次保存时再次确认即可
    // 实际后端没有"撤销确认"接口，这里通过刷新数据恢复
    Modal.confirm({
      title: '撤销确认？',
      content: '撤销后需要重新确认。是否继续？',
      onOk: async () => {
        // 这里简化：仅刷新数据，已确认的题仍保持已确认状态
        // 真正的撤销需要后端支持
        message.info('请通过"重新 AI 批改"或后端操作撤销')
      },
    })
  }

  async function saveCurrentQuestionAndNext() {
    if (!currentQuestion.value) return
    // 收集当前题目所有未确认的答案
    const items = []
    for (const a of currentQuestion.value.answers) {
      if (!a.teacher_confirmed && teacherScores[a.answer_id] != null) {
        items.push({
          answer_id: a.answer_id,
          teacher_score: teacherScores[a.answer_id],
          teacher_comment: teacherComments[a.answer_id] || null,
        })
      }
    }
    if (!items.length) {
      message.warning('没有可保存的评分')
      return
    }
    submitting.value = true
    try {
      await submitExamReview(examId, items)
      message.success(`已保存 ${items.length} 个评分`)
      await fetchReviewData()
      // 自动跳到下一题
      const nextIdx = currentIndex.value + 1
      if (nextIdx < reviewData.value.questions.length) {
        currentQuestionId.value = reviewData.value.questions[nextIdx].question_id
      }
    } catch (e) {
      const msg = e?.response?.data?.detail || '保存失败'
      message.error(msg)
    } finally {
      submitting.value = false
    }
  }

  async function submitAllReview() {
    if (!reviewData.value) return
    // 收集所有未确认的答案
    const items = []
    for (const q of reviewData.value.questions) {
      for (const a of q.answers) {
        if (!a.teacher_confirmed && teacherScores[a.answer_id] != null) {
          items.push({
            answer_id: a.answer_id,
            teacher_score: teacherScores[a.answer_id],
            teacher_comment: teacherComments[a.answer_id] || null,
          })
        }
      }
    }
    if (!items.length) {
      message.warning('没有可提交的评分')
      return
    }
    Modal.confirm({
      title: '提交全部审核？',
      content: `将提交 ${items.length} 个评分，提交后对应提交将锁定为"已批改"状态。`,
      okText: '确定提交',
      cancelText: '取消',
      onOk: async () => {
        submitting.value = true
        try {
          await submitExamReview(examId, items)
          message.success(`已提交 ${items.length} 个评分`)
          await fetchReviewData()
        } catch (e) {
          const msg = e?.response?.data?.detail || '提交失败'
          message.error(msg)
        } finally {
          submitting.value = false
        }
      },
    })
  }

  async function regradeAllPending() {
    // 逐个 submission 重新批改（仅未确认的）
    if (!reviewData.value) return
    regrading.value = true
    try {
      const submissionIds = new Set()
      for (const q of reviewData.value.questions) {
        for (const a of q.answers) {
          if (['pending', 'processing', 'failed'].includes(a.ai_status) && !a.teacher_confirmed) {
            submissionIds.add(a.submission_id)
          }
        }
      }
      let successCount = 0
      for (const sid of submissionIds) {
        try {
          await regradeSubmission(sid)
          successCount++
        } catch (e) {
          // 忽略单个失败
        }
      }
      message.success(`已对 ${successCount} 个提交触发重新批改`)
      // 启动轮询
      setTimeout(() => fetchReviewData(), 2000)
    } finally {
      regrading.value = false
    }
  }

  // ===== 导出审核报告 =====
  const exporting = ref(false)

  async function handleExportReport() {
    exporting.value = true
    try {
      const res = await exportReviewReport(examId)
      // 创建 Blob 并触发下载
      const blob = new Blob([res.data], { type: 'text/html' })
      const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `review_report_${examId}.html`
      link.click()
      window.URL.revokeObjectURL(url)
      message.success('报告已导出')
    } catch (e) {
      const msg = e?.response?.data?.detail || '导出失败'
      message.error(msg)
    } finally {
      exporting.value = false
    }
  }

  // ===== 审核统计仪表盘 =====
  const showStatsDrawer = ref(false)
  const statsLoading = ref(false)
  const statsData = ref(null)

  // 题目统计表格列配置
  const questionStatsColumns = [
    { key: 'question_id', title: '题目', dataIndex: 'question_id', width: 70 },
    { key: 'confirmed', title: '已确认', dataIndex: 'confirmed', width: 70 },
    { key: 'ai_avg', title: 'AI 均分', dataIndex: 'ai_avg', width: 80 },
    { key: 'teacher_avg', title: '教师均分', dataIndex: 'teacher_avg', width: 80 },
    { key: 'deviation_avg', title: '偏差', dataIndex: 'deviation_avg', width: 70 },
    { key: 'needs_review', title: '需审核', dataIndex: 'needs_review', width: 70 },
  ]

  // 监听抽屉打开时自动加载数据
  watch(showStatsDrawer, async (val) => {
    if (val && !statsData.value) {
      await fetchStatsData()
    }
  })

  async function fetchStatsData() {
    statsLoading.value = true
    try {
      const res = await getReviewStats(examId)
      statsData.value = res.data
    } catch (e) {
      const msg = e?.response?.data?.detail || '获取统计数据失败'
      message.error(msg)
    } finally {
      statsLoading.value = false
    }
  }

  // ===== 批量确认 =====
  const showBatchModal = ref(false)
  const batchLoading = ref(false)
  const batchForm = reactive({
    mode: 'question',
    question_id: null,
    submission_id: null,
    status_filter: 'needs_review',
    adopt_ai_score: true,
  })

  function filterSubmissionOption(input, option) {
    return option.children?.[0]?.children?.toLowerCase().includes(input.toLowerCase())
  }

  async function handleBatchConfirm() {
    // 校验
    if (batchForm.mode === 'question' && !batchForm.question_id) {
      message.warning('请选择题目')
      return
    }
    if (batchForm.mode === 'submission' && !batchForm.submission_id) {
      message.warning('请选择学生提交')
      return
    }
    if (batchForm.mode === 'status' && !batchForm.status_filter) {
      message.warning('请选择状态筛选条件')
      return
    }

    batchLoading.value = true
    try {
      const payload = {
        mode: batchForm.mode,
        adopt_ai_score: batchForm.adopt_ai_score,
      }
      if (batchForm.mode === 'question') {
        payload.question_id = batchForm.question_id
      } else if (batchForm.mode === 'submission') {
        payload.submission_id = batchForm.submission_id
      } else if (batchForm.mode === 'status') {
        payload.status_filter = batchForm.status_filter
      }

      const res = await batchConfirmReview(examId, payload)
      message.success(`已确认 ${res.data.confirmed_count} 个答案（影响 ${res.data.affected_submissions} 个提交）`)
      showBatchModal.value = false
      // 刷新数据
      await fetchReviewData()
    } catch (e) {
      const msg = e?.response?.data?.detail || '批量确认失败'
      message.error(msg)
    } finally {
      batchLoading.value = false
    }
  }

  // ===== 生命周期 =====
  onMounted(fetchReviewData)

  onUnmounted(() => {
    if (pollTimer) clearTimeout(pollTimer)
  })

  return {
    // 核心数据
    examId,
    reviewData, loading, submitting, regrading,
    currentQuestionId, confirmingIds,
    teacherScores, teacherComments,
    // 计算属性
    currentQuestion, currentIndex, reviewProgressPct,
    hasAiGradingSubmissions, currentQuestionHasAiScore,
    canSaveCurrentQuestion, canSubmitAll, allSubmissions,
    // 数据加载
    refreshData,
    // UI 辅助
    selectQuestion, getTypeText, getTypeColor,
    getQuestionConfirmedCount, getQuestionPendingCount,
    adoptAiScore, adoptAllAiScoreForQuestion,
    // 确认 / 保存 / 提交
    confirmSingle, unconfirmSingle, saveCurrentQuestionAndNext,
    submitAllReview, regradeAllPending,
    // 导出报告
    exporting, handleExportReport,
    // 统计仪表盘
    showStatsDrawer, statsLoading, statsData,
    questionStatsColumns,
    // 批量确认
    showBatchModal, batchLoading, batchForm,
    filterSubmissionOption, handleBatchConfirm,
  }
}
