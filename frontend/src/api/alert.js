import api from './index'

/** 获取教学预警列表 */
export function getAlerts(params = {}) {
  return api.get('/alerts', { params })
}
