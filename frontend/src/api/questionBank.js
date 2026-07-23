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

/** 从题库组卷（生成考试） */
export function composeExamFromBank(payload) {
  return api.post('/question-bank/compose-exam', payload)
}
