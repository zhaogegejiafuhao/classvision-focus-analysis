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
              <a-button @click="chunkPreviewOpen = true">
                分块调试
              </a-button>
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
            <template #extra>
              <a-switch
                v-model:checked="conversationMode"
                checked-children="对话"
                un-checked-children="单轮"
                @change="onModeChange"
              />
            </template>

            <!-- 单轮模式 -->
            <template v-if="!conversationMode">
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
                      :header="`来源 ${i+1}: ${chunk.source}${chunk.page ? ' 第' + chunk.page + '页' : ''} (相似度: ${(chunk.rerank_score || chunk.rrf_score || chunk.score || 0).toFixed(3)})`"
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
            </template>

            <!-- 多轮对话模式 -->
            <template v-else>
              <a-alert
                message="多轮对话模式：AI 会记住上下文，支持追问。追问不会重新检索，直接基于上文回答。"
                type="info"
                show-icon
                style="margin-bottom: 16px"
              />

              <!-- 会话列表 -->
              <div style="margin-bottom: 12px">
                <a-space style="width: 100%">
                  <a-select
                    v-model:value="currentConvId"
                    style="flex: 1"
                    placeholder="选择对话或新建"
                    allow-clear
                    @change="onConvChange"
                  >
                    <a-select-option v-for="c in conversations" :key="c.id" :value="c.id">
                      {{ c.title }} ({{ c.message_count }}条)
                    </a-select-option>
                  </a-select>
                  <a-button @click="newConversation" :disabled="queryLoading">
                    <template #icon><PlusOutlined /></template>
                    新对话
                  </a-button>
                  <a-popconfirm v-if="currentConvId" title="确定删除此对话？" @confirm="deleteConversation">
                    <a-button danger :disabled="queryLoading">
                      <template #icon><DeleteOutlined /></template>
                    </a-button>
                  </a-popconfirm>
                </a-space>
              </div>

              <!-- 对话消息列表 -->
              <div class="conv-messages" ref="convMessagesEl">
                <a-empty v-if="convMessages.length === 0" description="开始新的对话" style="padding: 40px 0" />
                <div
                  v-for="msg in convMessages"
                  :key="msg.id"
                  :class="['conv-msg', msg.role === 'user' ? 'conv-msg-user' : 'conv-msg-assistant']"
                >
                  <div class="conv-msg-role">
                    <a-tag :color="msg.role === 'user' ? 'blue' : 'green'">
                      {{ msg.role === 'user' ? '我' : 'AI' }}
                    </a-tag>
                    <a-tag v-if="msg.is_followup" color="orange" style="font-size: 11px">追问</a-tag>
                  </div>
                  <div v-html="renderMarkdown(msg.content)" class="conv-msg-content" />
                </div>
                <div v-if="queryLoading" class="conv-msg conv-msg-assistant">
                  <div class="conv-msg-role"><a-tag color="green">AI</a-tag></div>
                  <div class="conv-msg-content"><a-spin size="small" /> 正在思考...</div>
                </div>
              </div>

              <!-- 输入框 -->
              <a-space style="width: 100%; margin-top: 12px">
                <a-input
                  v-model:value="question"
                  placeholder="输入问题，支持追问（如：那怎么应用？、再详细说说）"
                  style="flex: 1"
                  :disabled="queryLoading"
                  @pressEnter="queryConversation"
                />
                <a-button type="primary" @click="queryConversation" :loading="queryLoading" :disabled="!question.trim()">
                  发送
                </a-button>
              </a-space>
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

      <!-- 分块预览调试工具 -->
      <a-drawer
        v-model:open="chunkPreviewOpen"
        title="分块预览调试"
        placement="right"
        width="680"
      >
        <a-space direction="vertical" style="width: 100%">
          <a-alert message="粘贴 Markdown/纯文本片段，预览分块效果。不写入数据库/索引，可安全对比多套配置。" type="info" show-icon />

          <a-form layout="inline" style="margin: 8px 0">
            <a-form-item label="策略">
              <a-select v-model:value="chunkPreviewStrategy" style="width: 160px">
                <a-select-option value="auto">auto（自动择优）</a-select-option>
                <a-select-option value="heading">heading（标题分块）</a-select-option>
                <a-select-option value="heuristic">heuristic（启发式）</a-select-option>
                <a-select-option value="legacy">legacy（递归分块）</a-select-option>
              </a-select>
            </a-form-item>
            <a-form-item>
              <a-button type="primary" @click="runChunkPreview" :loading="chunkPreviewLoading">运行预览</a-button>
            </a-form-item>
          </a-form>

          <a-textarea
            v-model:value="chunkPreviewText"
            placeholder="粘贴待测试文本（最大 64KB）..."
            :auto-size="{ minRows: 6, maxRows: 12 }"
            style="font-family: monospace; font-size: 13px"
          />

          <!-- 预览结果 -->
          <template v-if="chunkPreviewResult">
            <!-- 配置摘要 -->
            <a-card title="当前配置" size="small">
              <a-descriptions :column="2" size="small">
                <a-descriptions-item label="生效策略">
                  <a-tag color="blue">{{ chunkPreviewResult.strategy }}</a-tag>
                  <span style="font-size: 12px; color: #999">{{ chunkPreviewResult.strategy_source }}</span>
                </a-descriptions-item>
                <a-descriptions-item label="总分块数">
                  <a-statistic :value="chunkPreviewResult.total_chunks" :value-style="{ fontSize: '18px' }" />
                </a-descriptions-item>
                <a-descriptions-item label="分块大小">{{ chunkPreviewResult.config?.chunk_size }} 字符</a-descriptions-item>
                <a-descriptions-item label="重叠度">{{ chunkPreviewResult.config?.chunk_overlap }} 字符</a-descriptions-item>
                <a-descriptions-item label="父子分块">
                  <a-tag :color="chunkPreviewResult.config?.parent_child_enabled ? 'green' : 'default'">
                    {{ chunkPreviewResult.config?.parent_child_enabled ? '已开启' : '未开启' }}
                  </a-tag>
                </a-descriptions-item>
                <a-descriptions-item label="Token上限">{{ chunkPreviewResult.config?.embedding_token_limit || '关闭' }}</a-descriptions-item>
              </a-descriptions>
            </a-card>

            <!-- 统计信息 -->
            <a-card title="分块统计" size="small">
              <a-row :gutter="16">
                <a-col :span="6"><a-statistic title="平均字符" :value="chunkPreviewResult.stats?.avg_chars" /></a-col>
                <a-col :span="6"><a-statistic title="最小" :value="chunkPreviewResult.stats?.min_chars" /></a-col>
                <a-col :span="6"><a-statistic title="最大" :value="chunkPreviewResult.stats?.max_chars" /></a-col>
                <a-col :span="6"><a-statistic title="标准差" :value="chunkPreviewResult.stats?.std_chars" /></a-col>
              </a-row>
            </a-card>

            <!-- 父子分块统计 -->
            <a-card v-if="chunkPreviewResult.parent_child" title="父子分块预览" size="small">
              <a-row :gutter="16" style="margin-bottom: 12px">
                <a-col :span="6"><a-statistic title="父分块" :value="chunkPreviewResult.parent_child.parent_count" /></a-col>
                <a-col :span="6"><a-statistic title="子分块" :value="chunkPreviewResult.parent_child.child_count" /></a-col>
                <a-col :span="6"><a-statistic title="父平均字符" :value="chunkPreviewResult.parent_child.parent_avg_chars" /></a-col>
                <a-col :span="6"><a-statistic title="子平均字符" :value="chunkPreviewResult.parent_child.child_avg_chars" /></a-col>
              </a-row>
              <a-collapse size="small">
                <a-collapse-panel v-for="p in chunkPreviewResult.parent_child.parents" :key="p.index" :header="`父分块 #${p.index + 1} (${p.chars}字符)`">
                  <div style="font-size: 13px; white-space: pre-wrap; line-height: 1.6; max-height: 150px; overflow-y: auto; background: #fafafa; padding: 8px; border-radius: 4px">{{ p.content_preview }}</div>
                </a-collapse-panel>
              </a-collapse>
            </a-card>

            <!-- 文档结构信号 -->
            <a-card title="文档结构信号" size="small">
              <a-row :gutter="8">
                <a-col v-for="(val, key) in chunkPreviewResult.signals" :key="key" :span="4">
                  <a-statistic :title="key" :value="typeof val === 'number' ? (Number.isInteger(val) ? val : val.toFixed(3)) : val" :value-style="{ fontSize: '16px' }" />
                </a-col>
              </a-row>
            </a-card>

            <!-- 分块详情 -->
            <a-card title="分块详情" size="small">
              <a-collapse size="small">
                <a-collapse-panel
                  v-for="chunk in chunkPreviewResult.chunks"
                  :key="chunk.index"
                  :header="`块 #${chunk.index + 1} (${chunk.chars}字符${chunk.page ? ' 第' + chunk.page + '页' : ''})`"
                >
                  <div style="font-size: 13px; white-space: pre-wrap; line-height: 1.6; max-height: 200px; overflow-y: auto; background: #fafafa; padding: 8px; border-radius: 4px">{{ chunk.content }}</div>
                </a-collapse-panel>
              </a-collapse>
            </a-card>
          </template>
        </a-space>
      </a-drawer>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import { getRagStatus, listRagDocuments, uploadRagDocument, updateRagDocument, deleteRagDocument, rebuildRagIndex, listRagDocumentChunks, previewRagChunk, getRagIndexHistory, listRagConversations, listRagConversationMessages, deleteRagConversation, queryRagConversation } from '@/api/rag'
import { useUserStore } from '@/stores/user'
import MarkdownIt from 'markdown-it'
import { message } from 'ant-design-vue'
import { InfoCircleOutlined, EditOutlined, DeleteOutlined, PlusOutlined } from '@ant-design/icons-vue'

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

// 多轮对话
const conversationMode = ref(false)
const conversations = ref([])
const currentConvId = ref(null)
const convMessages = ref([])
const convMessagesEl = ref(null)

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

// 分块预览调试工具
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

onMounted(async () => {
  await loadStatus()
  await loadDocuments()
})

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

/* 多轮对话样式 */
.conv-messages {
  max-height: 500px;
  overflow-y: auto;
  padding: 8px;
  background: var(--cv-bg-page);
  border-radius: 8px;
}
.conv-msg {
  margin-bottom: 16px;
}
.conv-msg-role {
  margin-bottom: 4px;
}
.conv-msg-content {
  padding: 10px 14px;
  border-radius: 8px;
  line-height: 1.7;
  font-size: 14px;
}
.conv-msg-user .conv-msg-content {
  background: var(--cv-color-primary);
  color: white;
  margin-left: 40px;
}
.conv-msg-assistant .conv-msg-content {
  background: white;
  border: 1px solid #e8e8e8;
  margin-right: 40px;
}
.conv-msg-content :deep(p) {
  margin: 6px 0;
}
.conv-msg-content :deep(ul),
.conv-msg-content :deep(ol) {
  padding-left: 20px;
  margin: 6px 0;
}
.conv-msg-content :deep(code) {
  background: rgba(0,0,0,0.06);
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 13px;
}
.conv-msg-user .conv-msg-content :deep(code) {
  background: rgba(255,255,255,0.2);
}
</style>
