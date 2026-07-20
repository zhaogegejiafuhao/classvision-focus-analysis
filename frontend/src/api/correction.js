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
