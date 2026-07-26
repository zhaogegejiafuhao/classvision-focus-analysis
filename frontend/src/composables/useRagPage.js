/**
 * RAG 知识库页面业务逻辑（从 RagPage.vue 抽取）
 *
 * 包含：知识库状态/文档管理、单轮问答（流式）、多轮对话、分块调试预览、文档编辑。
 * 暴露所有模板所需的状态、计算属性和方法。
 */
import { ref, computed, onMounted, nextTick } from 'vue'
import {
  getRagStatus,
  listRagDocuments,
  uploadRagDocument,
  updateRagDocument,
  deleteRagDocument,
  rebuildRagIndex,
  listRagDocumentChunks,
  previewRagChunk,
  getRagIndexHistory,
  listRagConversations,
  listRagConversationMessages,
  deleteRagConversation,
  queryRagConversation,
} from '@/api/rag'
import { useUserStore } from '@/stores/user'
import MarkdownIt from 'markdown-it'
import { message } from 'ant-design-vue'

const md = new MarkdownIt({ html: false, breaks: true, linkify: true })

export function useRagPage() {
  const userStore = useUserStore()
  const currentRole = computed(() => userStore.role || 'student')
  const currentUserId = computed(() => userStore.user?.id)

  // ===== 知识库状态 =====
  const ragStatus = ref({})
  const documents = ref([])
  const uploadVisibility = ref(currentRole.value === 'student' ? 'private' : 'public')

  // ===== 单轮问答 =====
  const question = ref('')
  const ragResult = ref(null)
  const uploadLoading = ref(false)
  const queryLoading = ref(false)
  const indexLoading = ref(false)
  const queryHistory = ref([])

  const quickQuestions = [
    'OpenCV 是什么？有哪些主要模块？',
    '人脸检测的原理是什么？',
    '什么是计算机视觉？有哪些应用场景？',
    '如何进行相机标定？',
  ]

  // ===== 多轮对话 =====
  const conversationMode = ref(false)
  const conversations = ref([])
  const currentConvId = ref(null)
  const convMessages = ref([])
  const convMessagesEl = ref(null)

  // ===== 表格列 =====
  const docColumns = computed(() => [
    { title: '文件名', dataIndex: 'filename', key: 'filename', ellipsis: true },
    { title: '可见性', dataIndex: 'visibility', key: 'visibility', width: 80 },
    { title: '上传者', dataIndex: 'uploader_name', key: 'uploader', width: 80 },
    { title: '文本块', dataIndex: 'total_chunks', key: 'total_chunks', width: 60 },
    { title: '状态', dataIndex: 'indexed', key: 'indexed', width: 60 },
    { title: '上传时间', dataIndex: 'created_at', key: 'created_at', width: 140 },
    { title: '操作', key: 'action', width: 100 },
  ])

  // ===== 工具函数 =====
  function visColor(v) {
    if (v === 'public') return 'green'
    if (v === 'staff') return 'blue'
    return 'orange'
  }

  function visLabel(v) {
    if (v === 'public') return '公开'
    if (v === 'staff') return '同行可见'
    return '私有'
  }

  function canDelete(record) {
    return currentRole.value === 'admin' || record.uploaded_by === currentUserId.value
  }

  function renderMarkdown(text) {
    if (!text) return ''
    return md.render(text)
  }

  // ===== 数据加载 =====
  async function loadStatus() {
    try {
      const res = await getRagStatus()
      ragStatus.value = res.data
    } catch {
      ragStatus.value = { total_vectors: 0 }
    }
  }

  async function loadDocuments() {
    try {
      const res = await listRagDocuments()
      documents.value = res.data || []
    } catch {
      documents.value = []
    }
  }

  // ===== 文档上传 =====
  async function handleUpload(file) {
    uploadLoading.value = true
    const formData = new FormData()
    formData.append('file', file)
    formData.append('visibility', uploadVisibility.value)

    try {
      const res = await uploadRagDocument(formData)
      message.success(`上传成功，已索引 ${res.data.total_chunks} 个文本块（${visLabel(res.data.visibility)}）`)
      await loadDocuments()
      await loadStatus()
    } catch (e) {
      message.error('上传失败: ' + (e.response?.data?.detail || e.message))
    } finally {
      uploadLoading.value = false
    }

    return false
  }

  // ===== 单轮流式查询 =====
  async function queryRag() {
    if (!question.value.trim()) return
    const currentQuestion = question.value
    queryLoading.value = true
    ragResult.value = {
      answer: '',
      sources: [],
      retrieved_chunks: [],
      streaming: true,
    }

    try {
      const token = userStore.token || localStorage.getItem('token') || ''
      const resp = await fetch('/api/rag/query/stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ question: currentQuestion, top_k: 5 }),
      })
      if (!resp.ok) throw new Error('HTTP ' + resp.status)
      const reader = resp.body.getReader()
      const decoder = new TextDecoder()
      let buffer = ''
      while (true) {
        const { done, value } = await reader.read()
        if (done) break
        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split('\n')
        buffer = lines.pop()
        for (const line of lines) {
          if (!line.startsWith('data: ')) continue
          let data
          try { data = JSON.parse(line.slice(6)) } catch { continue }
          if (data.type === 'meta') {
            ragResult.value.sources = data.sources || []
            ragResult.value.retrieved_chunks = data.retrieved_chunks || []
          } else if (data.type === 'delta') {
            ragResult.value.answer += data.delta
          } else if (data.type === 'done') {
            ragResult.value.answer = data.content || ragResult.value.answer
            ragResult.value.streaming = false
          } else if (data.type === 'error') {
            ragResult.value.answer = '生成失败: ' + data.error
            ragResult.value.streaming = false
          }
        }
      }
      if (ragResult.value.answer) {
        queryHistory.value.unshift({
          question: currentQuestion,
          answer: ragResult.value.answer,
        })
        if (queryHistory.value.length > 20) queryHistory.value.pop()
      }
    } catch (e) {
      message.error('查询失败: ' + e.message)
      ragResult.value = null
    } finally {
      queryLoading.value = false
    }
  }

  function clearHistory() {
    queryHistory.value = []
    message.success('已清空历史问答')
  }

  async function indexHistory() {
    indexLoading.value = true
    try {
      const res = await getRagIndexHistory()
      message.success(`已索引 ${res.data.total_chunks} 个历史数据文本块`)
      await loadStatus()
    } catch (e) {
      message.error('索引失败: ' + (e.response?.data?.detail || e.message))
    } finally {
      indexLoading.value = false
    }
  }

  async function deleteDoc(docId) {
    try {
      await deleteRagDocument(docId)
      message.success('文档已删除')
      await loadDocuments()
      await loadStatus()
    } catch (e) {
      message.error('删除失败: ' + (e.response?.data?.detail || e.message))
    }
  }

  const rebuildLoading = ref(false)
  async function rebuildIndex() {
    rebuildLoading.value = true
    try {
      const res = await rebuildRagIndex()
      message.success(`重建完成：${res.data.documents} 个文档，${res.data.chunks} 个文本块`)
      await loadDocuments()
      await loadStatus()
    } catch (e) {
      message.error('重建失败: ' + (e.response?.data?.detail || e.message))
    } finally {
      rebuildLoading.value = false
    }
  }

  // ===== 分块预览调试 =====
  const chunkPreviewOpen = ref(false)
  const chunkPreviewText = ref('')
  const chunkPreviewStrategy = ref('auto')
  const chunkPreviewLoading = ref(false)
  const chunkPreviewResult = ref(null)

  async function runChunkPreview() {
    if (!chunkPreviewText.value.trim()) {
      message.warning('请先输入待测试文本')
      return
    }
    chunkPreviewLoading.value = true
    chunkPreviewResult.value = null
    try {
      const res = await previewRagChunk({
        text: chunkPreviewText.value,
        strategy: chunkPreviewStrategy.value === 'auto' ? null : chunkPreviewStrategy.value,
      })
      chunkPreviewResult.value = res.data
    } catch (e) {
      message.error('预览失败: ' + (e.response?.data?.detail || e.message))
    } finally {
      chunkPreviewLoading.value = false
    }
  }

  // ===== 文档预览 =====
  const previewVisible = ref(false)
  const previewLoading = ref(false)
  const previewData = ref(null)
  async function previewDoc(docId) {
    previewVisible.value = true
    previewLoading.value = true
    previewData.value = null
    try {
      const res = await listRagDocumentChunks(docId)
      previewData.value = res.data
    } catch (e) {
      message.error('加载失败: ' + (e.response?.data?.detail || e.message))
    } finally {
      previewLoading.value = false
    }
  }

  // ===== 编辑文档 =====
  const editDocOpen = ref(false)
  const editDocSaving = ref(false)
  const editDocForm = ref({ id: null, filename: '', visibility: 'private' })

  function openEditDoc(record) {
    editDocForm.value = {
      id: record.id,
      filename: record.filename,
      visibility: record.visibility || 'private',
    }
    editDocOpen.value = true
  }

  async function handleEditDoc() {
    editDocSaving.value = true
    try {
      const params = { filename: editDocForm.value.filename, visibility: editDocForm.value.visibility }
      await updateRagDocument(editDocForm.value.id, params)
      message.success('文档已更新')
      editDocOpen.value = false
      await loadDocuments()
    } catch (e) {
      message.error('更新失败: ' + (e.response?.data?.detail || e.message))
    } finally {
      editDocSaving.value = false
    }
  }

  // ===== 多轮对话方法 =====
  function onModeChange(checked) {
    if (checked) {
      loadConversations()
    } else {
      convMessages.value = []
      currentConvId.value = null
    }
  }

  async function loadConversations() {
    try {
      const res = await listRagConversations()
      conversations.value = res.data || []
    } catch {
      conversations.value = []
    }
  }

  function newConversation() {
    currentConvId.value = null
    convMessages.value = []
    question.value = ''
  }

  async function onConvChange(convId) {
    if (!convId) {
      convMessages.value = []
      return
    }
    try {
      const res = await listRagConversationMessages(convId)
      convMessages.value = res.data || []
      await nextTick()
      scrollToBottom()
    } catch {
      convMessages.value = []
    }
  }

  async function deleteConversation() {
    if (!currentConvId.value) return
    try {
      await deleteRagConversation(currentConvId.value)
      message.success('对话已删除')
      currentConvId.value = null
      convMessages.value = []
      await loadConversations()
    } catch (e) {
      message.error('删除失败')
    }
  }

  async function queryConversation() {
    if (!question.value.trim()) return
    const currentQuestion = question.value
    queryLoading.value = true

    // 先在 UI 显示用户消息
    convMessages.value.push({
      id: 'temp-' + Date.now(),
      role: 'user',
      content: currentQuestion,
      is_followup: false,
    })
    question.value = ''
    await nextTick()
    scrollToBottom()

    try {
      const res = await queryRagConversation({
        question: currentQuestion,
        conversation_id: currentConvId.value,
        top_k: 5,
      })

      // 添加 assistant 回答
      convMessages.value.push({
        id: res.data.message_id,
        role: 'assistant',
        content: res.data.answer,
        is_followup: res.data.is_followup,
      })

      // 更新当前会话 ID（新对话首次查询时会分配）
      if (!currentConvId.value) {
        currentConvId.value = res.data.conversation_id
      }
      await loadConversations()
      await nextTick()
      scrollToBottom()
    } catch (e) {
      message.error('查询失败: ' + (e.response?.data?.detail || e.message))
    } finally {
      queryLoading.value = false
    }
  }

  function scrollToBottom() {
    if (convMessagesEl.value) {
      convMessagesEl.value.scrollTop = convMessagesEl.value.scrollHeight
    }
  }

  // ===== 初始化 =====
  onMounted(async () => {
    await loadStatus()
    await loadDocuments()
  })

  return {
    // 用户态
    currentRole,
    // 知识库状态
    ragStatus,
    documents,
    uploadVisibility,
    // 单轮问答
    question,
    ragResult,
    uploadLoading,
    queryLoading,
    indexLoading,
    rebuildLoading,
    queryHistory,
    quickQuestions,
    docColumns,
    // 多轮对话
    conversationMode,
    conversations,
    currentConvId,
    convMessages,
    convMessagesEl,
    // 分块预览
    chunkPreviewOpen,
    chunkPreviewText,
    chunkPreviewStrategy,
    chunkPreviewLoading,
    chunkPreviewResult,
    // 文档预览
    previewVisible,
    previewLoading,
    previewData,
    // 编辑文档
    editDocOpen,
    editDocSaving,
    editDocForm,
    // 工具
    visColor,
    visLabel,
    canDelete,
    renderMarkdown,
    // 数据加载
    loadStatus,
    loadDocuments,
    // 文档操作
    handleUpload,
    deleteDoc,
    rebuildIndex,
    indexHistory,
    previewDoc,
    openEditDoc,
    handleEditDoc,
    // 单轮问答
    queryRag,
    clearHistory,
    // 分块预览
    runChunkPreview,
    // 多轮对话
    onModeChange,
    newConversation,
    onConvChange,
    deleteConversation,
    queryConversation,
  }
}
