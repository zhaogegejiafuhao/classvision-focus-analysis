import api from './index'

/** 生成相似练习题（不持久化） */
export function generateSimilarQuestions(data) {
  return api.post('/similar-questions/generate', data, { timeout: 60000 })
}

/** 获取模型路由统计 */
export function getModelRouterStats() {
  return api.get('/similar-questions/model-router/stats', { _skipGlobalError: true })
}

/** 已持久化相似题列表 */
export function listSimilarQuestions(params = {}) {
  return api.get('/similar-questions/list', {
    params: {
      student_id: params.studentId,
      status: params.status,
      page: params.page || 1,
      page_size: params.pageSize || 20,
    },
  })
}

/** 获取单条已持久化相似题详情 */
export function getSimilarQuestionDetail(similarId) {
  return api.get(`/similar-questions/${similarId}`, { _skipGlobalError: true })
}

/** 提交相似题练习答案 */
export function submitSimilarAnswer(similarId, answerText) {
  return api.post(`/similar-questions/${similarId}/submit`, {
    answer_text: answerText,
  }, { timeout: 120000 })
}
