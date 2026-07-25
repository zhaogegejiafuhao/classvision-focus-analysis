import api from './index'

// ===== 试卷模板 =====

/** 获取试卷模板列表 */
export function listExamTemplates() {
  return api.get('/exam-templates')
}

/** 创建自定义试卷模板 */
export function createExamTemplate(payload) {
  return api.post('/exam-templates', payload)
}

/** 删除自定义模板 */
export function deleteExamTemplate(templateId) {
  return api.delete(`/exam-templates/${templateId}`)
}

// ===== AI 智能组卷 =====

/** AI 智能组卷（自然语言描述 → 自动匹配题库 + LLM 补题）— 120s 超时 */
export function aiComposeExam(payload) {
  return api.post('/question-bank/ai-compose', payload, { timeout: 120000 })
}

// ===== 考试审核与发布 =====

/** 获取 draft 考试的完整预览 */
export function previewExam(examId) {
  return api.get(`/exams/${examId}/preview`)
}

/** 将 draft 考试发布（教师审核确认后调用） */
export function publishExam(examId, payload) {
  return api.post(`/exams/${examId}/publish`, payload)
}

// ===== 智能换题 =====

/** 智能换题：随机返回一道替换题 */
export function swapQuestion(payload) {
  return api.post('/question-bank/swap-question', payload)
}

/** 智能换题：返回多道候选题供教师选择 */
export function swapQuestionCandidates(payload) {
  return api.post('/question-bank/swap-question-candidates', payload)
}
