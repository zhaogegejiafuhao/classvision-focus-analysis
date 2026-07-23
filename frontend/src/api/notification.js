import api from './index'

/** 通知列表 */
export function listNotifications() {
  return api.get('/notifications')
}

/** 未读通知数量（静默预取，失败不弹错误） */
export function getUnreadCount(opts = {}) {
  return api.get('/notifications/unread-count', { _skipGlobalError: true, ...opts })
}

/** 创建通知 */
export function createNotification(payload) {
  return api.post('/notifications', payload)
}

/** 标记单条通知已读 */
export function readNotification(notificationId) {
  return api.post(`/notifications/${notificationId}/read`)
}

/** 标记全部通知已读 */
export function readAllNotifications() {
  return api.post('/notifications/read-all')
}

/** 删除通知 */
export function deleteNotification(notificationId) {
  return api.delete(`/notifications/${notificationId}`)
}
