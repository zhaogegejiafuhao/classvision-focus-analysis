import api from './index'

/** 获取成绩配置（权重等，静默预取，失败不弹错误） */
export function getGradeConfig(classroomId, opts = {}) {
  return api.get(`/grades/config/${classroomId}`, { _skipGlobalError: true, ...opts })
}

/** 设置成绩配置（权重等） */
export function setGradeConfig(classroomId, payload) {
  return api.post(`/grades/config/${classroomId}`, payload)
}

/** 获取成绩报告（静默预取，失败不弹错误） */
export function getGradeReport(classroomId, opts = {}) {
  return api.get(`/grades/report/${classroomId}`, { _skipGlobalError: true, ...opts })
}

/** 更新平时成绩 */
export function updateUsualScore(classroomId, personId, payload) {
  return api.put(`/grades/usual-score/${classroomId}/${personId}`, payload)
}

/** 获取成绩趋势（静默预取，失败不弹错误） */
export function getGradeTrend(studentId, opts = {}) {
  return api.get(`/grades/trend/${studentId}`, { _skipGlobalError: true, ...opts })
}
