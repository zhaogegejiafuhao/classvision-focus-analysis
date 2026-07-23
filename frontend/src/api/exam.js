import api from './index'

/** 考试列表（教师按 classroom_id 过滤；opts 用于静默预取场景） */
export function listExams(params = {}, opts = {}) {
  return api.get('/exams', { params, ...opts })
}

/** 创建考试（返回含题目结构的 ExamDetail） */
export function createExam(payload) {
  return api.post('/exams', payload)
}

/** 学生端：我待参加的考试列表（静默预取，失败不弹错误） */
export function listAssignedExams(opts = {}) {
  return api.get('/exams/assigned', { _skipGlobalError: true, ...opts })
}

/** 考试详情（含题目列表） */
export function getExam(examId) {
  return api.get(`/exams/${examId}`)
}

/** 发布考试（学生端可见） */
export function publishExam(examId) {
  return api.post(`/exams/${examId}/publish`)
}

/** 删除考试 */
export function deleteExam(examId) {
  return api.delete(`/exams/${examId}`)
}

/** 结束考试（停止作答） */
export function closeExam(examId) {
  return api.post(`/exams/${examId}/close`)
}

/** 添加考试题目（payload 含题干、选项、答案、分值等） */
export function addExamQuestion(examId, payload) {
  return api.post(`/exams/${examId}/questions`, payload)
}

/** 考试的所有提交列表（教师批改用，静默预取失败不弹错误） */
export function listExamSubmissions(examId, opts = {}) {
  return api.get(`/exams/${examId}/submissions`, { _skipGlobalError: true, ...opts })
}

/** 考试统计（均分、分布等，静默预取失败不弹错误） */
export function getExamStats(examId, opts = {}) {
  return api.get(`/exams/${examId}/stats`, { _skipGlobalError: true, ...opts })
}

/** 学生开始考试（返回题目、倒计时等） */
export function startExam(examId) {
  return api.post(`/exams/${examId}/start`)
}

/** 学生提交考试答案（answers 为答案数组，直接作为 body） */
export function submitExam(examId, answers) {
  return api.post(`/exams/${examId}/submit`, answers)
}

/** 学生查看自己的考试结果（静默预取，未出分时 404 不弹错误） */
export function getMyExamResult(examId, opts = {}) {
  return api.get(`/exams/my-result/${examId}`, { _skipGlobalError: true, ...opts })
}

/** 教师批改某次提交的主观题答案（payload 含各题分数、评语） */
export function gradeExamAnswers(submissionId, payload) {
  return api.post(`/exams/submissions/${submissionId}/grade-answers`, payload)
}

/** 获取某次考试提交的详情（含学生答案、批改结果） */
export function getExamSubmission(submissionId) {
  return api.get(`/exams/submissions/${submissionId}`)
}

/** 导出考试完整报告为文件（返回 Blob，供前端触发下载） */
export function exportExam(examId) {
  return api.get(`/exams/${examId}/export`, { responseType: 'blob' })
}

/** 生成考试报告（班级维度：均分、及格率、每题正确率、AI 分析） */
export function generateExamReport(examId) {
  return api.post(`/exams/${examId}/report`)
}

/** 学生个人考试报告（分数、错题、薄弱知识点、与班级对比） */
export function getStudentExamReport(examId) {
  return api.get(`/exams/${examId}/student-report`)
}
