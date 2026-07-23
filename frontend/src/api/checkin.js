import api from './index'

/** 创建签到会话 */
export function createCheckinSession(payload) {
  return api.post('/checkin/sessions', payload)
}

/** 签到会话列表（教师端） */
export function listCheckinSessions(params = {}) {
  return api.get('/checkin/sessions', { params })
}

/** 签到会话详情 */
export function getCheckinSession(sessionId) {
  return api.get(`/checkin/sessions/${sessionId}`)
}

/** 关闭签到会话 */
export function closeCheckinSession(sessionId) {
  return api.post(`/checkin/sessions/${sessionId}/close`)
}

/** 获取签到会话的考勤记录（静默预取，失败不弹错误） */
export function listCheckinAttendances(sessionId, opts = {}) {
  return api.get(`/checkin/sessions/${sessionId}/attendances`, { _skipGlobalError: true, ...opts })
}

/** 导出签到会话考勤为文件（返回 Blob） */
export function exportCheckinSession(sessionId) {
  return api.get(`/checkin/sessions/${sessionId}/export`, { responseType: 'blob' })
}

/** 获取当前活跃签到会话（可选 classroom_id 过滤） */
export function getActiveCheckin(params = {}) {
  return api.get('/checkin/active', { params })
}

/** 学生提交签到 */
export function submitCheckin(payload) {
  return api.post('/checkin/submit', payload)
}

/** 学生签到历史（静默预取场景可用 opts） */
export function getCheckinHistory(opts = {}) {
  return api.get('/checkin/history', opts)
}
