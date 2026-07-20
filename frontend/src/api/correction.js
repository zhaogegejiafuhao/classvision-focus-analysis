import api from './index'

/** 学生提交订正（后端会调用LLM重新批改，超时放宽到5分钟） */
export function submitCorrection(data) {
  return api.post('/correction/submit', data, { timeout: 300000 })
}

/** 获取订正前后对比 */
export function getCorrectionComparison(correctionId) {
  return api.get(`/correction/comparison/${correctionId}`)
}

/** 获取分层个性化订正任务 */
export function getPersonalizedCorrection(studentId, analysisType = 'math') {
  return api.post('/correction/personalized', null, {
    params: { student_id: studentId, analysis_type: analysisType },
  })
}

/** 错题本列表（学生角色：自动按当前用户过滤；教师/管理员：可指定 student_id） */
export function listMistakes(params = {}) {
  return api.get('/correction/list', {
    params: {
      student_id: params.studentId,
      kp: params.kp,
      page: params.page || 1,
      page_size: params.pageSize || 20,
    },
  })
}

/** 错题详情：聚合原题+批改+订正历史 */
export function getMistakeDetail(gradingId) {
  return api.get(`/correction/${gradingId}`)
}

/** 从错题一键生成相似题并持久化 */
export function generateSimilarFromMistake(gradingId, data = {}) {
  return api.post(`/correction/${gradingId}/generate-similar`, {
    count: data.count || 3,
    tier: data.tier || '中等生',
  }, { timeout: 120000 })
}
