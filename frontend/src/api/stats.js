import api from './index'

/**
 * 首页仪表盘聚合（按角色返回不同维度的统计计数与近期活动）
 * @param {Object} [opts] - 额外 axios 配置（如 { _skipGlobalError: true } 用于静默预取）
 */
export function getDashboard(opts = {}) {
  return api.get('/dashboard', opts)
}

/** 课堂时间线（按分钟聚合的注意力曲线，用于 ClassroomDetail 顶部活动流） */
export function getClassroomTimeline(classroomId) {
  return api.get(`/classrooms/${classroomId}/timeline`)
}

/** 课堂注意力热力图（学生 × 时间段矩阵，404/空数据不弹错误） */
export function getClassroomHeatmap(classroomId) {
  return api.get(`/classrooms/${classroomId}/heatmap`, { _skipGlobalError: true })
}

/** 课堂考勤统计（已识别/未识别/缺勤，404/空数据不弹错误） */
export function getClassroomAttendance(classroomId) {
  return api.get(`/classrooms/${classroomId}/attendance`, { _skipGlobalError: true })
}

/**
 * 课堂学生列表（用于学生管理表格、报告学生选择）
 * @param {Object} [opts] - 额外 axios 配置（如 { _skipGlobalError: true } 用于静默预取）
 */
export function listClassroomStudents(classroomId, opts = {}) {
  return api.get(`/classrooms/${classroomId}/students`, opts)
}

/** 添加学生到课堂（含已注册人员绑定/邀请注册两种模式，payload 由组件决定） */
export function addClassroomStudent(classroomId, payload) {
  return api.post(`/classrooms/${classroomId}/students`, payload)
}

/** 修改课堂中某学生信息（座位号、备注等） */
export function updateClassroomStudent(classroomId, studentId, payload) {
  return api.put(`/classrooms/${classroomId}/students/${studentId}`, payload)
}

/** 从课堂移除学生 */
export function removeClassroomStudent(classroomId, studentId) {
  return api.delete(`/classrooms/${classroomId}/students/${studentId}`)
}

/**
 * 生成/重新生成课堂 AI 报告
 * @param {number} classroomId
 * @param {Object} [opts]
 * @param {boolean} [opts.force=false] - true 时强制重新生成（覆盖现有报告）
 * @param {boolean} [opts.skipGlobalError=false] - LivePage 静默触发时设为 true，避免轮询失败弹错误
 */
export function generateClassroomReport(classroomId, { force = false, skipGlobalError = false } = {}) {
  return api.post(`/classrooms/${classroomId}/report`, null, {
    params: force ? { force: true } : undefined,
    _skipGlobalError: skipGlobalError,
  })
}

/** 获取已生成的课堂报告（404 时不弹错误，组件据此显示"未生成"状态） */
export function getClassroomReport(classroomId) {
  return api.get(`/classrooms/${classroomId}/report`, { _skipGlobalError: true })
}

/** 删除课堂报告 */
export function deleteClassroomReport(classroomId) {
  return api.delete(`/classrooms/${classroomId}/report`)
}

/** 课堂考试风险预警（缺考/低分集中/作弊嫌疑，404/空数据不弹错误） */
export function getClassroomExamRisks(classroomId, params = {}) {
  return api.get(`/classrooms/${classroomId}/exam-risks`, { params, _skipGlobalError: true })
}

/** 学生个人：我的注意力历史（学生端 StudentReport 用，404 不弹错误） */
export function getMyAttentionHistory() {
  return api.get('/me/attention-history', { _skipGlobalError: true })
}

/** 学生行为画像（教师端 StudentBehavior 用，404 不弹错误） */
export function getStudentBehavior(studentId) {
  return api.get(`/students/${studentId}/behavior`, { _skipGlobalError: true })
}
