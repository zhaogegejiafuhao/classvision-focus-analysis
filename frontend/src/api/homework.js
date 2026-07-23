import api from './index'

/** 作业列表（教师按 classroom_id/status 过滤；opts 用于静默预取场景） */
export function listHomework(params = {}, opts = {}) {
  return api.get('/homework', { params, ...opts })
}

/** 创建作业 */
export function createHomework(payload) {
  return api.post('/homework', payload)
}

/** 学生端：我待完成的作业列表（静默预取，失败不弹错误） */
export function listAssignedHomework(opts = {}) {
  return api.get('/homework/assigned', { _skipGlobalError: true, ...opts })
}

/** 作业详情（含题目、附件等） */
export function getHomework(homeworkId) {
  return api.get(`/homework/${homeworkId}`)
}

/** 更新作业（含关闭：payload 传 { status: 'closed' }） */
export function updateHomework(homeworkId, payload) {
  return api.put(`/homework/${homeworkId}`, payload)
}

/** 删除作业 */
export function deleteHomework(homeworkId) {
  return api.delete(`/homework/${homeworkId}`)
}

/** 作业的所有提交列表（教师批改用，静默预取失败不弹错误） */
export function listHomeworkSubmissions(homeworkId, opts = {}) {
  return api.get(`/homework/${homeworkId}/submissions`, { _skipGlobalError: true, ...opts })
}

/** 教师批改某次提交（payload 含各题分数、评语等） */
export function gradeSubmission(submissionId, payload) {
  return api.post(`/homework/submissions/${submissionId}/grade`, payload)
}

/** 学生提交作业（payload 含答案、附件等） */
export function submitHomework(homeworkId, payload) {
  return api.post(`/homework/${homeworkId}/submit`, payload)
}

/** 学生查看自己某次作业的提交（静默预取，未提交时 404 不弹错误） */
export function getMySubmission(homeworkId, opts = {}) {
  return api.get(`/homework/my-submissions/${homeworkId}`, { _skipGlobalError: true, ...opts })
}

/** 教师退回学生提交并附反馈 */
export function returnSubmission(submissionId, payload) {
  return api.post(`/homework/submissions/${submissionId}/return`, payload)
}

/** 学生申请作业延期（payload 含 homework_id、reason、new_deadline 等） */
export function createExtension(payload) {
  return api.post('/homework/extensions', payload)
}
