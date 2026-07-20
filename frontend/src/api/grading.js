import api from './index'

/** AI批改单题（后端LLM批改+降级链可能耗时2-3分钟，超时设为300s） */
export function aiGrade(data) {
  return api.post('/grading/grade', data, { timeout: 300000 })
}

/** 批量批改 */
export function batchGrade(homeworkId) {
  return api.post('/grading/batch', null, { params: { homework_id: homeworkId }, timeout: 600000 })
}

/** 获取批改结果 */
export function getGradingResult(submissionId) {
  return api.get(`/grading/result/${submissionId}`)
}

/** 教师确认/修正批改结果 */
export function confirmGrading(resultId, confirmedScore = null) {
  return api.post(`/grading/confirm/${resultId}`, { confirmed_score: confirmedScore })
}

/** 单独OCR识别 */
export function ocrRecognize(imageBase64) {
  return api.post('/grading/ocr', { image_base64: imageBase64 }, { timeout: 60000 })
}
