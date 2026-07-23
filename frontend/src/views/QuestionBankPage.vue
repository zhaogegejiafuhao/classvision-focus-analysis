<template>
  <div class="cv-page">
    <a-page-header title="题库管理" sub-title="管理和复用题目">
      <template #extra>
        <a-button type="primary" @click="showCreateModal = true">添加题目</a-button>
        <a-button @click="showComposeModal = true" style="margin-left: 8px">组卷</a-button>
      </template>
    </a-page-header>

    <a-card :loading="loading">
      <a-space style="margin-bottom: 16px">
        <a-select v-model:value="filterType" style="width: 120px" allow-clear placeholder="题型" @change="fetchQuestions">
          <a-select-option value="single">单选</a-select-option>
          <a-select-option value="multi">多选</a-select-option>
          <a-select-option value="judge">判断</a-select-option>
          <a-select-option value="fill">填空</a-select-option>
          <a-select-option value="essay">简答</a-select-option>
        </a-select>
        <a-select v-model:value="filterCategory" style="width: 120px" allow-clear placeholder="分类" @change="fetchQuestions">
          <a-select-option v-for="c in categories" :key="c" :value="c">{{ c }}</a-select-option>
        </a-select>
        <a-select v-model:value="filterDifficulty" style="width: 100px" allow-clear placeholder="难度" @change="fetchQuestions">
          <a-select-option v-for="d in 5" :key="d" :value="d">{{ d }}星</a-select-option>
        </a-select>
        <a-tag v-if="selectedCount > 0" color="blue" style="margin-left: 8px">已选 {{ selectedCount }} 题（用于组卷）</a-tag>
      </a-space>

      <a-table :columns="columns" :data-source="questions" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'type'">
            <a-tag>{{ getTypeText(record.type) }}</a-tag>
          </template>
          <template v-else-if="column.key === 'difficulty'">
            <span v-for="i in record.difficulty" :key="i" style="color: #faad14">★</span>
          </template>
          <template v-else-if="column.key === 'selected'">
            <a-checkbox v-model:checked="selectedIds[record.id]" />
          </template>
          <template v-else-if="column.key === 'action'">
            <a-popconfirm title="确定删除？" @confirm="handleDeleteQuestion(record.id)">
              <a-button type="link" danger size="small">删除</a-button>
            </a-popconfirm>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 添加题目弹窗 -->
    <a-modal v-model:open="showCreateModal" title="添加题目到题库" @ok="createQuestion" :confirm-loading="submitting" width="600px">
      <a-form :label-col="{ span: 4 }">
        <a-form-item label="题型">
          <a-select v-model:value="form.type">
            <a-select-option value="single">单选题</a-select-option>
            <a-select-option value="multi">多选题</a-select-option>
            <a-select-option value="judge">判断题</a-select-option>
            <a-select-option value="fill">填空题</a-select-option>
            <a-select-option value="essay">简答题</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="题目内容"><a-textarea v-model:value="form.content" :rows="3" /></a-form-item>
        <a-form-item v-if="form.type === 'single' || form.type === 'multi'" label="选项">
          <div v-for="(opt, i) in form.options" :key="i" style="margin-bottom: 8px">
            <a-input v-model:value="form.options[i]" :placeholder="`选项${i + 1}`" style="width: 85%" />
            <a-button type="link" danger size="small" @click="form.options.splice(i, 1)">删除</a-button>
          </div>
          <a-button type="dashed" size="small" @click="form.options.push('')">添加选项</a-button>
        </a-form-item>
        <a-form-item label="正确答案"><a-input v-model:value="form.answer" /></a-form-item>
        <a-form-item label="分值"><a-input-number v-model:value="form.score" :min="1" :max="100" /></a-form-item>
        <a-form-item label="分类"><a-input v-model:value="form.category" placeholder="如：数学、英语" /></a-form-item>
        <a-form-item label="标签"><a-input v-model:value="form.tags" placeholder="逗号分隔，如：基础,重点" /></a-form-item>
        <a-form-item label="难度">
          <a-rate v-model:value="form.difficulty" :count="5" />
        </a-form-item>
      </a-form>
    </a-modal>

    <!-- 组卷弹窗 -->
    <a-modal v-model:open="showComposeModal" title="从题库组卷" @ok="composeExam" :confirm-loading="composing" width="600px">
      <a-form :label-col="{ span: 4 }">
        <a-form-item label="考试标题" required><a-input v-model:value="composeForm.title" /></a-form-item>
        <a-form-item label="关联课堂">
          <a-select v-model:value="composeForm.classroom_id" allow-clear placeholder="选择课堂" style="width: 100%">
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="考试时长"><a-input-number v-model:value="composeForm.duration" :min="10" :max="180" addon-after="分钟" /></a-form-item>
        <a-form-item label="已选题目">{{ selectedCount }} 题</a-form-item>
        <a-divider>随机抽题</a-divider>
        <a-form-item label="抽题分类">
          <a-select v-model:value="composeForm.random_category" allow-clear placeholder="不限" style="width: 100%">
            <a-select-option v-for="c in categories" :key="c" :value="c">{{ c }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="抽题难度">
          <a-select v-model:value="composeForm.random_difficulty" allow-clear placeholder="不限" style="width: 100%">
            <a-select-option v-for="d in 5" :key="d" :value="d">{{ d }}星</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="抽题数量"><a-input-number v-model:value="composeForm.random_count" :min="0" :max="50" /></a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import { listQuestionBank, createQuestionBankItem, deleteQuestionBankItem, getQuestionBankCategories, composeExamFromBank } from '@/api/questionBank'
import { listClassrooms } from '@/api/classroom'

const router = useRouter()
const questions = ref([])
const categories = ref([])
const classrooms = ref([])
const loading = ref(false)
const submitting = ref(false)
const composing = ref(false)
const showCreateModal = ref(false)
const showComposeModal = ref(false)
const filterType = ref(null)
const filterCategory = ref(null)
const filterDifficulty = ref(null)
const selectedIds = reactive({})

const form = ref({ type: 'single', content: '', options: ['', '', '', ''], answer: '', score: 10, category: '', tags: '', difficulty: 1 })
const composeForm = ref({ title: '', classroom_id: null, duration: 60, random_category: null, random_difficulty: null, random_count: 0 })

const selectedCount = computed(() => Object.values(selectedIds).filter(Boolean).length)
const selectedQuestionIds = computed(() => Object.entries(selectedIds).filter(([, v]) => v).map(([k]) => parseInt(k)))

const columns = [
  { key: 'selected', title: '组卷选题', width: 80 },
  { key: 'type', title: '题型', width: 80 },
  { key: 'content', title: '内容', dataIndex: 'content', ellipsis: true },
  { key: 'category', title: '分类', dataIndex: 'category', width: 100 },
  { key: 'difficulty', title: '难度', width: 100 },
  { key: 'score', title: '分值', dataIndex: 'score', width: 60 },
  { key: 'action', title: '操作', width: 80 },
]

async function fetchQuestions() {
  loading.value = true
  try {
    const params = {}
    if (filterType.value) params.type = filterType.value
    if (filterCategory.value) params.category = filterCategory.value
    if (filterDifficulty.value) params.difficulty = filterDifficulty.value
    const res = await listQuestionBank(params)
    questions.value = res.data
  } catch { /* global error handler */ } finally { loading.value = false }
}

async function fetchCategories() {
  try { const res = await getQuestionBankCategories(); categories.value = res.data } catch { /* ignore */ }
}

async function fetchClassrooms() {
  try { const res = await listClassrooms(); classrooms.value = res.data } catch { /* ignore */ }
}

async function createQuestion() {
  if (!form.value.content.trim()) { message.error('请输入题目内容'); return }
  submitting.value = true
  try {
    await createQuestionBankItem({
      type: form.value.type,
      content: form.value.content,
      options: (form.value.type === 'single' || form.value.type === 'multi') ? form.value.options.filter(o => o.trim()) : null,
      answer: form.value.answer,
      score: form.value.score,
      category: form.value.category || null,
      tags: form.value.tags || null,
      difficulty: form.value.difficulty,
    })
    message.success('题目已添加到题库')
    showCreateModal.value = false
    form.value = { type: 'single', content: '', options: ['', '', '', ''], answer: '', score: 10, category: '', tags: '', difficulty: 1 }
    fetchQuestions()
    fetchCategories()
  } catch { /* global error handler */ } finally { submitting.value = false }
}

async function handleDeleteQuestion(id) {
  try { await deleteQuestionBankItem(id); message.success('删除成功'); fetchQuestions() } catch { /* global error handler */ }
}

async function composeExam() {
  if (!composeForm.value.title.trim()) { message.error('请输入考试标题'); return }
  if (selectedCount.value === 0 && !composeForm.value.random_count) { message.error('请选择题目或设置随机抽题'); return }
  composing.value = true
  try {
    const payload = {
      title: composeForm.value.title,
      classroom_id: composeForm.value.classroom_id,
      duration: composeForm.value.duration,
      question_ids: selectedQuestionIds.value,
    }
    if (composeForm.value.random_count > 0) {
      payload.random_config = { count: composeForm.value.random_count }
      if (composeForm.value.random_category) payload.random_config.category = composeForm.value.random_category
      if (composeForm.value.random_difficulty) payload.random_config.difficulty = composeForm.value.random_difficulty
    }
    const res = await composeExamFromBank(payload)
    message.success(`组卷成功，共${res.data.question_count}题`)
    showComposeModal.value = false
    router.push(`/exams/${res.data.exam_id}`)
  } catch { /* global error handler */ } finally { composing.value = false }
}

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

onMounted(() => { fetchQuestions(); fetchCategories(); fetchClassrooms() })
</script>
