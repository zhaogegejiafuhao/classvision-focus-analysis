<template>
  <div class="cv-page" style="max-width: 1400px">
      <a-typography-title :level="3" style="margin-bottom: 16px">RAG 知识库</a-typography-title>
      <a-row :gutter="16">
        <!-- 左侧：知识库管理 -->
        <a-col :span="10">
          <!-- 知识库状态 -->
          <a-card title="知识库状态" style="margin-bottom: 16px">
            <a-row :gutter="16">
              <a-col :span="8">
                <a-statistic title="向量数量" :value="ragStatus.total_vectors || 0" :value-style="{ color: '#3751FE' }" />
              </a-col>
              <a-col :span="8">
                <a-statistic title="向量维度" :value="ragStatus.dimension || 384" />
              </a-col>
              <a-col :span="8">
                <a-statistic title="可见文档" :value="documents.length" />
              </a-col>
            </a-row>
            <template #extra>
              <a-typography-text type="secondary">{{ ragStatus.model || '-' }}</a-typography-text>
            </template>
          </a-card>

          <!-- 文档管理 -->
          <a-card title="文档管理">
            <!-- 上传区域 -->
            <div style="margin-bottom: 16px">
              <a-space direction="vertical" style="width: 100%">
                <a-row :gutter="8" align="middle">
                  <a-col flex="auto">
                    <a-upload
                      :before-upload="handleUpload"
                      accept=".pdf,.txt,.md,.docx,.pptx"
                      :show-upload-list="false"
                    >
                      <a-button type="primary" :loading="uploadLoading">
                        上传文档（PDF/Word/PPT/TXT/MD）
                      </a-button>
                    </a-upload>
                  </a-col>
                  <a-col flex="200px">
                    <a-select v-model:value="uploadVisibility" style="width: 100%">
                      <a-select-option value="public" :disabled="currentRole === 'student'">
                        <a-tag color="green" style="margin: 0">公开</a-tag>
                        <span style="font-size: 12px; margin-left: 4px">所有用户可见</span>
                      </a-select-option>
                      <a-select-option value="staff" :disabled="currentRole === 'student'">
                        <a-tag color="blue" style="margin: 0">同行可见</a-tag>
                        <span style="font-size: 12px; margin-left: 4px">教师+管理员</span>
                      </a-select-option>
                      <a-select-option value="private">
                        <a-tag color="orange" style="margin: 0">私有</a-tag>
                        <span style="font-size: 12px; margin-left: 4px">仅自己</span>
                      </a-select-option>
                    </a-select>
                  </a-col>
                </a-row>
                <a-typography-text type="secondary" style="font-size: 12px">
                  <InfoCircleOutlined /> 可见性说明：公开=学生也能查看检索；同行可见=仅教师/管理员；私有=仅自己
                </a-typography-text>
              </a-space>
            </div>

            <a-space style="margin-bottom: 12px">
              <a-button @click="indexHistory" :loading="indexLoading">
                索引历史课堂数据
              </a-button>
              <a-popconfirm title="确定从数据库重建索引？" @confirm="rebuildIndex">
                <a-button :loading="rebuildLoading">重建索引</a-button>
              </a-popconfirm>
            </a-space>

            <a-table :columns="docColumns" :data-source="documents" row-key="id" size="small" :pagination="{ pageSize: 5 }">
              <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'visibility'">
                  <a-tag :color="visColor(record.visibility)">
                    {{ visLabel(record.visibility) }}
                  </a-tag>
                </template>
                <template v-if="column.key === 'uploader'">
                  {{ record.uploader_name || '未知' }}
                </template>
                <template v-if="column.key === 'indexed'">
                  <a-tag :color="record.indexed ? 'green' : 'red'">
                    {{ record.indexed ? '已索引' : '未索引' }}
                  </a-tag>
                </template>
                <template v-if="column.key === 'created_at'">
                  {{ new Date(record.created_at).toLocaleString('zh-CN') }}
                </template>
                <template v-if="column.key === 'action'">
                  <a-button type="link" size="small" @click="previewDoc(record.id)">预览</a-button>
                  <a-dropdown>
                    <a-button type="link" size="small">更多</a-button>
                    <template #overlay>
                      <a-menu>
                        <a-menu-item @click="openEditDoc(record)">
                          <EditOutlined /> 编辑可见性
                        </a-menu-item>
                        <a-menu-item v-if="canDelete(record)" danger @click="deleteDoc(record.id)">
                          <DeleteOutlined /> 删除
                        </a-menu-item>
                      </a-menu>
                    </template>
                  </a-dropdown>
                </template>
              </template>
            </a-table>
          </a-card>

          <a-drawer
            v-model:open="previewVisible"
            :title="previewData?.document?.filename || '文档预览'"
            placement="right"
            width="600"
          >
            <a-spin :spinning="previewLoading">
              <div v-if="previewData">
                <a-alert
                  :message="`共 ${previewData.document.total_chunks} 个文本块`"
                  type="info"
                  style="margin-bottom: 16px"
                />
                <div
                  v-for="chunk in previewData.chunks"
                  :key="chunk.index"
                  style="margin-bottom: 12px; padding: 12px; background: #fafafa; border-radius: 4px; border-left: 3px solid var(--cv-color-primary)"
                >
                  <div style="font-size: 12px; color: #999; margin-bottom: 4px">块 #{{ chunk.index + 1 }}</div>
                  <div style="white-space: pre-wrap; line-height: 1.6; font-size: 14px">{{ chunk.content }}</div>
                </div>
              </div>
            </a-spin>
          </a-drawer>
        </a-col>

        <!-- 右侧：问答区域 -->
        <a-col :span="14">
          <a-card title="知识库问答">
            <a-alert
              message="输入问题，AI 将从你可见的知识库文档中检索相关内容并生成回答。"
              type="info"
              show-icon
              style="margin-bottom: 16px"
            />

            <!-- 快捷问题 -->
            <div style="margin-bottom: 16px">
              <a-typography-text type="secondary" style="margin-right: 8px">快捷提问：</a-typography-text>
              <a-tag
                v-for="q in quickQuestions"
                :key="q"
                style="cursor: pointer; margin-bottom: 4px"
                @click="question = q; queryRag()"
              >
                {{ q }}
              </a-tag>
            </div>

            <!-- 输入框 -->
            <a-space style="width: 100%; margin-bottom: 16px">
              <a-input
                v-model:value="question"
                placeholder="输入问题，如：什么是计算机视觉？如何提高学生注意力？"
                style="flex: 1"
                :disabled="queryLoading"
                @pressEnter="queryRag"
              />
              <a-button type="primary" @click="queryRag" :loading="queryLoading" :disabled="!question.trim()">
                查询
              </a-button>
            </a-space>

            <!-- 回答结果 -->
            <template v-if="ragResult">
              <a-card title="AI 回答" style="margin-bottom: 16px" :bordered="false" class="rag-answer-card">
                <div v-if="ragResult.streaming && !ragResult.answer" style="color: #999; padding: 8px 0">
                  <a-spin size="small" /> 正在检索知识库并生成回答...
                </div>
                <div v-html="renderMarkdown(ragResult.answer)" style="white-space: pre-wrap; line-height: 1.8" />
                <span v-if="ragResult.streaming && ragResult.answer" class="streaming-cursor">▌</span>
              </a-card>

              <!-- 参考来源 -->
              <a-card title="参考来源" size="small">
                <a-empty v-if="!ragResult.retrieved_chunks || ragResult.retrieved_chunks.length === 0" description="无可见的参考来源" />
                <a-collapse v-else>
                  <a-collapse-panel
                    v-for="(chunk, i) in ragResult.retrieved_chunks"
                    :key="i"
                    :header="`来源 ${i+1}: ${chunk.source} (相似度: ${chunk.score.toFixed(3)})`"
                  >
                    <div style="padding: 8px; background: #f5f5f5; border-radius: 4px; max-height: 200px; overflow-y: auto; font-size: 13px; line-height: 1.6">
                      {{ chunk.content }}
                    </div>
                  </a-collapse-panel>
                </a-collapse>
              </a-card>
            </template>

            <!-- 历史问答 -->
            <template v-if="queryHistory.length > 0 && !ragResult">
              <a-divider>
                <a-space>
                  <span>历史问答</span>
                  <a-button type="link" size="small" danger @click="clearHistory">清空历史</a-button>
                </a-space>
              </a-divider>
              <a-list :data-source="queryHistory.slice(0, 5)" size="small">
                <template #renderItem="{ item }">
                  <a-list-item style="cursor: pointer" @click="question = item.question; queryRag()">
                    <a-list-item-meta>
                      <template #title>{{ item.question }}</template>
                      <template #description>{{ item.answer.substring(0, 80) }}...</template>
                    </a-list-item-meta>
                  </a-list-item>
                </template>
              </a-list>
            </template>
          </a-card>
        </a-col>
      </a-row>

      <!-- 编辑文档可见性弹窗 -->
      <a-modal
        v-model:open="editDocOpen"
        title="编辑文档"
        @ok="handleEditDoc"
        :confirm-loading="editDocSaving"
        ok-text="保存"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="文件名">
            <a-input v-model:value="editDocForm.filename" />
          </a-form-item>
          <a-form-item label="可见性">
            <a-select v-model:value="editDocForm.visibility">
              <a-select-option value="public" :disabled="currentRole === 'student'">
                <a-tag color="green" style="margin: 0">公开</a-tag> 所有用户可见
              </a-select-option>
              <a-select-option value="staff" :disabled="currentRole === 'student'">
                <a-tag color="blue" style="margin: 0">同行可见</a-tag> 教师+管理员
              </a-select-option>
              <a-select-option value="private">
                <a-tag color="orange" style="margin: 0">私有</a-tag> 仅自己
              </a-select-option>
            </a-select>
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '@/api'
import { useUserStore } from '@/stores/user'
import MarkdownIt from 'markdown-it'
import { message } from 'ant-design-vue'
import { InfoCircleOutlined, EditOutlined, DeleteOutlined } from '@ant-design/icons-vue'

const md = new MarkdownIt({ html: false, breaks: true, linkify: true })
const userStore = useUserStore()
const currentRole = computed(() => userStore.role || 'student')
const currentUserId = computed(() => userStore.user?.id)

const ragStatus = ref({})
const documents = ref([])
const question = ref('')
const ragResult = ref(null)
const uploadLoading = ref(false)
const queryLoading = ref(false)
const indexLoading = ref(false)
const queryHistory = ref([])
const uploadVisibility = ref(currentRole.value === 'student' ? 'private' : 'public')

const quickQuestions = [
  'OpenCV 是什么？有哪些主要模块？',
  '人脸检测的原理是什么？',
  '什么是计算机视觉？有哪些应用场景？',
  '如何进行相机标定？',
]

const docColumns = computed(() => {
  const cols = [
    { title: '文件名', dataIndex: 'filename', key: 'filename', ellipsis: true },
    { title: '可见性', dataIndex: 'visibility', key: 'visibility', width: 80 },
    { title: '上传者', dataIndex: 'uploader_name', key: 'uploader', width: 80 },
    { title: '文本块', dataIndex: 'total_chunks', key: 'total_chunks', width: 60 },
    { title: '状态', dataIndex: 'indexed', key: 'indexed', width: 60 },
    { title: '上传时间', dataIndex: 'created_at', key: 'created_at', width: 140 },
    { title: '操作', key: 'action', width: 100 },
  ]
  return cols
})

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

async function loadStatus() {
  try {
    const res = await api.get('/rag/status')
    ragStatus.value = res.data
  } catch {
    ragStatus.value = { total_vectors: 0 }
  }
}

async function loadDocuments() {
  try {
    const res = await api.get('/rag/documents')
    documents.value = res.data || []
  } catch {
    documents.value = []
  }
}

async function handleUpload(file) {
  uploadLoading.value = true
  const formData = new FormData()
  formData.append('file', file)
  formData.append('visibility', uploadVisibility.value)

  try {
    const res = await api.post('/rag/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
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
    const res = await api.post('/rag/index/history')
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
    await api.delete(`/rag/documents/${docId}`)
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
    const res = await api.post('/rag/rebuild')
    message.success(`重建完成：${res.data.documents} 个文档，${res.data.chunks} 个文本块`)
    await loadDocuments()
    await loadStatus()
  } catch (e) {
    message.error('重建失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    rebuildLoading.value = false
  }
}

const previewVisible = ref(false)
const previewLoading = ref(false)
const previewData = ref(null)
async function previewDoc(docId) {
  previewVisible.value = true
  previewLoading.value = true
  previewData.value = null
  try {
    const res = await api.get(`/rag/documents/${docId}/chunks`)
    previewData.value = res.data
  } catch (e) {
    message.error('加载失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    previewLoading.value = false
  }
}

// 编辑文档
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
    await api.put(`/rag/documents/${editDocForm.value.id}`, null, { params })
    message.success('文档已更新')
    editDocOpen.value = false
    await loadDocuments()
  } catch (e) {
    message.error('更新失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    editDocSaving.value = false
  }
}

onMounted(async () => {
  await loadStatus()
  await loadDocuments()
})
</script>

<style scoped>
.rag-answer-card {
  background: var(--cv-bg-subtle);
}
.rag-answer-card :deep(h1),
.rag-answer-card :deep(h2),
.rag-answer-card :deep(h3),
.rag-answer-card :deep(h4) {
  font-weight: 600;
  margin: 12px 0 8px 0;
  color: var(--cv-text-primary);
}
.rag-answer-card :deep(h1) { font-size: 18px; }
.rag-answer-card :deep(h2) { font-size: 16px; }
.rag-answer-card :deep(h3) { font-size: 15px; }
.rag-answer-card :deep(h4) { font-size: 14px; }
.rag-answer-card :deep(p) {
  margin: 8px 0;
}
.rag-answer-card :deep(ul),
.rag-answer-card :deep(ol) {
  padding-left: 20px;
  margin: 8px 0;
}
.rag-answer-card :deep(li) {
  margin: 4px 0;
}
.rag-answer-card :deep(strong) {
  font-weight: 600;
  color: var(--cv-text-primary);
}
.rag-answer-card :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 12px 0;
  font-size: 13px;
}
.rag-answer-card :deep(th),
.rag-answer-card :deep(td) {
  border: 1px solid var(--cv-border-base);
  padding: 8px 12px;
  text-align: left;
}
.rag-answer-card :deep(th) {
  background: var(--cv-bg-page);
  font-weight: 600;
  color: var(--cv-text-primary);
}
.rag-answer-card :deep(tr:nth-child(2n)) {
  background: var(--cv-bg-subtle);
}
.rag-answer-card :deep(pre) {
  background: var(--cv-bg-page);
  padding: 12px 16px;
  border-radius: var(--cv-radius-base);
  overflow-x: auto;
  margin: 12px 0;
}
.rag-answer-card :deep(code) {
  background: var(--cv-bg-page);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--cv-color-primary);
}
.rag-answer-card :deep(pre code) {
  background: none;
  padding: 0;
  color: var(--cv-text-secondary);
}
.rag-answer-card :deep(blockquote) {
  border-left: 3px solid var(--cv-color-primary);
  padding: 8px 16px;
  margin: 12px 0;
  background: var(--cv-bg-page);
  border-radius: 0 6px 6px 0;
  color: var(--cv-text-tertiary);
  font-size: 13px;
}
.rag-answer-card :deep(a) {
  color: var(--cv-color-primary);
  text-decoration: none;
}
.rag-answer-card :deep(a:hover) {
  text-decoration: underline;
}
.streaming-cursor {
  display: inline-block;
  animation: blink 1s step-end infinite;
  color: var(--cv-color-primary);
  font-weight: bold;
}
@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}
</style>
