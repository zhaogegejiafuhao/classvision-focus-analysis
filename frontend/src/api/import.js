import api from './index'

/** 获取部门列表 */
export function listDepartments() {
  return api.get('/import/departments')
}

/** 创建部门（name/type 通过 query string 传递） */
export function createDepartment(params) {
  return api.post('/import/departments', null, { params })
}

/** 删除部门 */
export function deleteDepartment(departmentId) {
  return api.delete(`/import/departments/${departmentId}`)
}

/** 下载导入模板 */
export function getImportTemplate() {
  return api.get('/import/template')
}

/** Excel 批量导入人员（multipart/form-data） */
export function importExcel(role, formData) {
  return api.post(`/import/excel?role=${role}`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
}

/** CSV 批量导入人员 */
export function importCsv(role, data) {
  return api.post(`/import/csv?role=${role}`, data)
}

/** 导出导入错误报告 */
export function exportImportErrors(payload) {
  return api.post('/import/export-errors', payload)
}
