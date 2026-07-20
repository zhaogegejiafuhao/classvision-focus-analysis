import api from './index'

/** 生成相似练习题 */
export function generateSimilarQuestions(data) {
  return api.post('/similar-questions/generate', data, { timeout: 60000 })
}

/** 获取模型路由统计 */
export function getModelRouterStats() {
  return api.get('/similar-questions/model-router/stats')
}
