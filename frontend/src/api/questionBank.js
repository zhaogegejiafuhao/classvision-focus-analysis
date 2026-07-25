import api from './index'

/** 题库题目列表（支持 category/classroom_id 等过滤） */
export function listQuestionBank(params = {}) {
  return api.get('/question-bank', { params })
}

/** 创建题库题目 */
export function createQuestionBankItem(payload) {
  return api.post('/question-bank', payload)
}

/** 删除题库题目 */
export function deleteQuestionBankItem(questionId) {
  return api.delete(`/question-bank/${questionId}`)
}

/** 获取题目分类列表 */
export function getQuestionBankCategories() {
  return api.get('/question-bank/categories')
}

/** 获取题库知识点标签列表 */
export function getQuestionBankTags() {
  return api.get('/question-bank/tags')
}

/** 从题库组卷（生成考试） */
export function composeExamFromBank(payload) {
  return api.post('/question-bank/compose-exam', payload)
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
