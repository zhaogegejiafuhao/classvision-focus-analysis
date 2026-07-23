import api from './index'

/** 教学计划列表 */
export function listTeachingPlans() {
  return api.get('/teaching-plans')
}

/** 创建教学计划 */
export function createTeachingPlan(payload) {
  return api.post('/teaching-plans', payload)
}

/** 更新教学计划 */
export function updateTeachingPlan(planId, payload) {
  return api.put(`/teaching-plans/${planId}`, payload)
}

/** 删除教学计划 */
export function deleteTeachingPlan(planId) {
  return api.delete(`/teaching-plans/${planId}`)
}
