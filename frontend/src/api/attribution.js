import api from './index'

/** 知识归因分析 */
export function analyzeKnowledge(data) {
  return api.post('/attribution/analyze', data, { timeout: 60000 })
}

/** 获取学生学情报告 */
export function getStudentReport(studentId) {
  return api.get(`/attribution/report/${studentId}`)
}

/** 获取雷达图数据 */
export function getRadarData(studentId, analysisType = 'math') {
  return api.get(`/attribution/radar/${studentId}`, { params: { analysis_type: analysisType } })
}

/** 获取知识图谱结构 */
export function getKnowledgeGraph(analysisType = 'math') {
  return api.get('/attribution/graph', { params: { analysis_type: analysisType } })
}

/** 学生身份：获取自己关联的 Student 记录列表（自动反查 student_id） */
export function getMyStudentInfo() {
  return api.get('/attribution/me/student-info')
}

/** 教师身份：获取指定课堂的学生列表（用于归因分析下拉选择） */
export function listStudentsForAnalysis(classroomId) {
  return api.get(`/attribution/classrooms/${classroomId}/students-for-analysis`)
}
