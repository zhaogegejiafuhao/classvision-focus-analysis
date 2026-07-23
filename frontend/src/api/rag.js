import api from './index'

/** RAG 服务状态（静默预取，失败不弹错误） */
export function getRagStatus(opts = {}) {
  return api.get('/rag/status', { _skipGlobalError: true, ...opts })
}

/** RAG 查询（同步响应） */
export function queryRag(payload) {
  return api.post('/rag/query', payload)
}

/** RAG 流式查询（返回 SSE stream，需自行处理 response） */
export function queryRagStream(payload) {
  return api.post('/rag/query/stream', payload)
}

/** 上传文档到知识库（multipart/form-data，需设 headers） */
export function uploadRagDocument(formData, opts = {}) {
  return api.post('/rag/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 300000,
    ...opts,
  })
}

/** 获取知识库文档列表（静默预取，失败不弹错误） */
export function listRagDocuments(opts = {}) {
  return api.get('/rag/documents', { _skipGlobalError: true, ...opts })
}

/** 更新文档元数据（如标题/标签） */
export function updateRagDocument(documentId, payload, opts = {}) {
  return api.put(`/rag/documents/${documentId}`, null, { params: payload, ...opts })
}

/** 删除知识库文档 */
export function deleteRagDocument(documentId) {
  return api.delete(`/rag/documents/${documentId}`)
}

/** 重建知识库索引 */
export function rebuildRagIndex() {
  return api.post('/rag/rebuild')
}

/** 获取文档分块列表（静默预取，失败不弹错误） */
export function listRagDocumentChunks(documentId, opts = {}) {
  return api.get(`/rag/documents/${documentId}/chunks`, { _skipGlobalError: true, ...opts })
}

/** 预览文档分块效果 */
export function previewRagChunk(payload) {
  return api.post('/rag/chunk-preview', payload)
}

/** 获取索引历史记录 */
export function getRagIndexHistory() {
  return api.post('/rag/index/history')
}

/** 获取会话列表（静默预取，失败不弹错误） */
export function listRagConversations(opts = {}) {
  return api.get('/rag/conversations', { _skipGlobalError: true, ...opts })
}

/** 创建新会话 */
export function createRagConversation(payload) {
  return api.post('/rag/conversations', payload)
}

/** 获取会话消息列表（静默预取，失败不弹错误） */
export function listRagConversationMessages(convId, opts = {}) {
  return api.get(`/rag/conversations/${convId}/messages`, { _skipGlobalError: true, ...opts })
}

/** 删除会话 */
export function deleteRagConversation(convId) {
  return api.delete(`/rag/conversations/${convId}`)
}

/** 在会话中查询（对话式 RAG） */
export function queryRagConversation(payload) {
  return api.post('/rag/conversations/query', payload)
}
