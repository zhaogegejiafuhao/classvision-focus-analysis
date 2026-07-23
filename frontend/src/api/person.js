import api from './index'

/** 人员列表（支持 role/keyword 等过滤参数） */
export function listPersons(params = {}, opts = {}) {
  return api.get('/persons', { params, ...opts })
}

/** 注册新人员 */
export function registerPerson(payload) {
  return api.post('/persons/register', payload)
}

/** 获取人员详情 */
export function getPerson(personId) {
  return api.get(`/persons/${personId}`)
}

/** 更新人员信息 */
export function updatePerson(personId, payload) {
  return api.put(`/persons/${personId}`, payload)
}

/** 删除人员 */
export function deletePerson(personId) {
  return api.delete(`/persons/${personId}`)
}

/** 人脸匹配（单张） */
export function matchPerson(payload) {
  return api.post('/persons/match', payload)
}

/** 人脸批量匹配 */
export function batchMatchPerson(payload) {
  return api.post('/persons/batch-match', payload)
}
