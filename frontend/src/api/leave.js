import api from './index'

/** 请假列表（支持 classroom_id/status 等过滤） */
export function listLeaves(params = {}) {
  return api.get('/leaves', { params })
}

/** 提交请假申请 */
export function createLeave(payload) {
  return api.post('/leaves', payload)
}

/** 审批请假（approve/reject） */
export function reviewLeave(leaveId, payload) {
  return api.post(`/leaves/${leaveId}/review`, payload)
}
