import api from './index'

/**
 * 课堂列表（教师看自己创建的，学生看加入的）
 * @param {Object} [params] - 查询参数（如 status 等）
 * @param {Object} [opts] - 额外 axios 配置（如 { _skipGlobalError: true } 用于静默预取）
 */
export function listClassrooms(params = {}, opts = {}) {
  return api.get('/classrooms', { params, ...opts })
}

/** 创建课堂 */
export function createClassroom(payload) {
  return api.post('/classrooms', payload)
}

/** 课堂详情（含统计概览） */
export function getClassroom(classroomId) {
  return api.get(`/classrooms/${classroomId}`)
}

/** 更新课堂信息 */
export function updateClassroom(classroomId, payload) {
  return api.put(`/classrooms/${classroomId}`, payload)
}

/** 删除课堂 */
export function deleteClassroom(classroomId) {
  return api.delete(`/classrooms/${classroomId}`)
}

/** 结束直播课堂（body=null 显式传，避免 FastAPI 路由签名报错；timeout 放宽到 30s 防长连接卡死） */
export function endClassroom(classroomId) {
  return api.put(`/classrooms/${classroomId}/end`, null, { timeout: 30000 })
}

/** 我加入的课堂列表（学生端用） */
export function listMyClassrooms() {
  return api.get('/classrooms/my')
}

/** 公开课堂列表（学生端搜索可加入的课堂） */
export function listPublicClassrooms(params = {}) {
  return api.get('/classrooms/public', { params })
}

/** 通过邀请码加入课堂 */
export function joinClassroomByCode(payload) {
  return api.post('/classrooms/join', payload)
}

/** 通过课堂 ID 直接加入（公开课堂） */
export function joinClassroomById(classroomId) {
  return api.post(`/classrooms/join/${classroomId}`)
}

/** 课堂聊天历史（首次进入/刷新时拉取，404 不弹全局错误以便组件显示空状态） */
export function getChatHistory(classroomId) {
  return api.get(`/classrooms/${classroomId}/chat/history`, { _skipGlobalError: true })
}

/** 导出完整聊天记录为 Markdown（返回 Blob，供前端触发下载） */
export function exportChat(classroomId) {
  return api.get(`/classrooms/${classroomId}/chat/export`, { responseType: 'blob' })
}
