import api from './index'

/** 资料列表（支持 classroom_id 等过滤） */
export function listMaterials(params = {}) {
  return api.get('/materials', { params })
}

/** 上传资料（multipart/form-data） */
export function uploadMaterial(formData) {
  return api.post('/materials/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
}

/** 下载资料 */
export function downloadMaterial(materialId) {
  return api.get(`/materials/${materialId}/download`)
}

/** 删除资料 */
export function deleteMaterial(materialId) {
  return api.delete(`/materials/${materialId}`)
}
