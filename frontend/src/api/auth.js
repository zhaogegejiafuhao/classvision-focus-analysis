import api from './index'

/** 注册新用户 */
export function register(payload) {
  return api.post('/auth/register', payload)
}

/** 修改密码 */
export function changePassword(payload) {
  return api.post('/auth/change-password', payload)
}
