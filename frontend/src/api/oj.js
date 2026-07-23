import api from './index'

/** OJ 健康检查（静默预取，失败不弹错误） */
export function getOjHealth(opts = {}) {
  return api.get('/oj/health', { _skipGlobalError: true, ...opts })
}

/** 代码运行（提交代码并获取执行结果） */
export function runCode(payload) {
  return api.post('/oj/run', payload)
}

/** 题目列表 */
export function listOjProblems(params = {}) {
  return api.get('/oj/problems', { params })
}

/** 题目详情 */
export function getOjProblem(problemId) {
  return api.get(`/oj/problems/${problemId}`)
}

/** 创建题目 */
export function createOjProblem(payload) {
  return api.post('/oj/problems', payload)
}

/** 更新题目 */
export function updateOjProblem(problemId, payload) {
  return api.put(`/oj/problems/${problemId}`, payload)
}

/** 删除题目 */
export function deleteOjProblem(problemId) {
  return api.delete(`/oj/problems/${problemId}`)
}

/** 提交代码判题 */
export function submitOjSolution(payload) {
  return api.post('/oj/submit', payload)
}

/** 提交记录列表 */
export function listOjSubmissions(params = {}) {
  return api.get('/oj/submissions', { params })
}

/** 提交记录详情 */
export function getOjSubmission(submissionId) {
  return api.get(`/oj/submissions/${submissionId}`)
}
