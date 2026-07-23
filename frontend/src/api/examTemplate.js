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

/** AI 智能组卷（自然语言描述 → 自动匹配题库 + LLM 补题） */
export function aiComposeExam(payload) {
  return api.post('/question-bank/ai-compose', payload)
}
