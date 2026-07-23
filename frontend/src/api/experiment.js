import api from './index'

/** 实验列表（支持 classroom_id 等过滤） */
export function listExperiments(params = {}) {
  return api.get('/experiments', { params })
}

/** 创建实验 */
export function createExperiment(payload) {
  return api.post('/experiments', payload)
}

/** 实验详情 */
export function getExperiment(experimentId) {
  return api.get(`/experiments/${experimentId}`)
}

/** 删除实验 */
export function deleteExperiment(experimentId) {
  return api.delete(`/experiments/${experimentId}`)
}

/** 实验报告列表（静默预取，失败不弹错误） */
export function listExperimentReports(experimentId, opts = {}) {
  return api.get(`/experiments/${experimentId}/reports`, { _skipGlobalError: true, ...opts })
}

/** 学生提交实验报告（multipart/form-data） */
export function submitExperimentReport(experimentId, formData) {
  return api.post(`/experiments/${experimentId}/submit`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
}

/** 教师批改实验报告 */
export function gradeExperimentReport(reportId, payload) {
  return api.post(`/experiments/reports/${reportId}/grade`, payload)
}

/** 退回实验报告 */
export function returnExperimentReport(reportId, payload) {
  return api.post(`/experiments/reports/${reportId}/return`, payload)
}

/** 下载实验报告 */
export function downloadExperimentReport(reportId) {
  return api.get(`/experiments/reports/${reportId}/download`)
}
