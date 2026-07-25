<template>
  <div class="step-compose-manual">
    <div class="compose-layout">
      <!-- 左侧：题库筛选 + 表格 -->
      <div class="compose-left">
        <a-alert v-if="questions.length > 0" type="info" show-icon style="margin-bottom: 12px">
          <template #message>在下方表格中勾选题目，然后点击「加入已选」按钮添加到右侧试题篮</template>
        </a-alert>

        <div class="filter-bar">
          <a-select v-model:value="filterType" style="width: 110px" allow-clear placeholder="题型" @change="fetchQuestions">
            <a-select-option value="single">单选</a-select-option>
            <a-select-option value="multi">多选</a-select-option>
            <a-select-option value="judge">判断</a-select-option>
            <a-select-option value="fill">填空</a-select-option>
            <a-select-option value="essay">简答</a-select-option>
          </a-select>
          <a-select v-model:value="filterCategory" style="width: 130px" allow-clear placeholder="分类" @change="fetchQuestions">
            <a-select-option v-for="c in categories" :key="c" :value="c">{{ c }}</a-select-option>
          </a-select>
          <a-select v-model:value="filterTags" style="width: 150px" allow-clear mode="multiple" placeholder="知识点标签" @change="fetchQuestions" :max-tag-count="2">
            <a-select-option v-for="t in allTags" :key="t" :value="t">{{ t }}</a-select-option>
          </a-select>
          <a-select v-model:value="filterDifficulty" style="width: 100px" allow-clear placeholder="难度" @change="fetchQuestions">
            <a-select-option v-for="d in 5" :key="d" :value="d">{{ d }}星</a-select-option>
          </a-select>
          <a-input-search v-model:value="filterKeyword" placeholder="关键词搜索" style="width: 180px" @search="fetchQuestions" />
          <a-button type="primary" :disabled="manualSelectedCount === 0" @click="addToSelected">
            <template #icon><PlusOutlined /></template>
            加入已选{{ manualSelectedCount > 0 ? `（${manualSelectedCount} 题）` : '' }}
          </a-button>
        </div>

        <a-table
          :columns="questionColumns"
          :data-source="questions"
          row-key="id"
          size="small"
          :pagination="{ pageSize: 10, showSizeChanger: false }"
          :row-selection="{ selectedRowKeys: manualSelectedIds, onChange: onManualSelectChange }"
          :loading="questionsLoading"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'type'">
              <a-tag>{{ getTypeText(record.type) }}</a-tag>
            </template>
            <template v-else-if="column.key === 'content'">
              <LatexText :content="record.content" class="q-content-cell" />
            </template>
            <template v-else-if="column.key === 'difficulty'">
              <span v-for="i in record.difficulty" :key="i" style="color: #faad14">★</span>
            </template>
            <template v-else-if="column.key === 'score'">
              <span style="font-weight: 600; color: #3751FE">{{ record.score }}</span>
            </template>
          </template>
        </a-table>
      </div>

      <!-- 右侧：试题篮 + 组卷按钮 -->
      <div class="compose-right">
        <QuestionBasket
          :questions="selectedQuestions"
          :template-score="currentTemplateScore"
          @remove="removeSelected"
          @move-up="moveSelectedUp"
          @move-down="moveSelectedDown"
          @clear="clearSelected"
        />

        <a-card size="small" class="config-card">
          <template #title><span>⚙️ 考试配置</span></template>
          <a-form layout="vertical" size="small">
            <a-form-item label="考试标题" required>
              <a-input v-model:value="store.title" placeholder="输入考试标题" />
            </a-form-item>
            <a-row :gutter="12">
              <a-col :span="14">
                <a-form-item label="关联课堂">
                  <a-select v-model:value="store.classroomId" allow-clear placeholder="选择课堂" style="width: 100%">
                    <a-select-option v-for="c in store.classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
                  </a-select>
                </a-form-item>
              </a-col>
              <a-col :span="10">
                <a-form-item label="时长(分钟)">
                  <a-input-number v-model:value="store.duration" :min="10" :max="180" style="width: 100%" />
                </a-form-item>
              </a-col>
            </a-row>
            <a-button
              type="primary"
              block
              :disabled="selectedQuestions.length === 0"
              :loading="composing"
              @click="handleManualCompose"
              size="large"
            >
              确认组卷（{{ selectedQuestions.length }} 题 / {{ selectedTotalScore }} 分）
            </a-button>
          </a-form>
        </a-card>
      </div>
    </div>

    <div class="step-actions" style="margin-top: 16px">
      <a-button @click="goBack">上一步</a-button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import { PlusOutlined } from '@ant-design/icons-vue'
import { useExamComposeStore } from '@/stores/examCompose'
import { listQuestionBank, composeExamFromBank, getQuestionBankCategories, getQuestionBankTags } from '@/api/questionBank'
import { previewExam } from '@/api/examTemplate'
import LatexText from '@/components/LatexText.vue'
import QuestionBasket from '@/components/exam-compose/QuestionBasket.vue'

const router = useRouter()
const store = useExamComposeStore()

// 题库数据
const questions = ref([])
const questionsLoading = ref(false)
const categories = ref([])
const allTags = ref([])
const filterType = ref(null)
const filterCategory = ref(null)
const filterTags = ref([])
const filterDifficulty = ref(null)
const filterKeyword = ref(null)
const manualSelectedIds = ref([])
const selectedQuestions = ref([])
const composing = ref(false)

const manualSelectedCount = computed(() => manualSelectedIds.value.length)
const selectedTotalScore = computed(() => selectedQuestions.value.reduce((sum, q) => sum + (q.scoreOverride || q.score), 0))

const currentTemplateScore = computed(() => {
  if (!store.templateId) return 0
  const tmpl = store.templates.find(t => t.id === store.templateId)
  return tmpl ? tmpl.total_score : 0
})

const questionColumns = [
  { key: 'type', title: '题型', width: 80 },
  { key: 'content', title: '内容', dataIndex: 'content', width: 300 },
  { key: 'category', title: '分类', dataIndex: 'category', width: 100, ellipsis: true },
  { key: 'difficulty', title: '难度', width: 90 },
  { key: 'score', title: '分值', dataIndex: 'score', width: 70, align: 'right' },
]

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

async function fetchQuestions() {
  questionsLoading.value = true
  try {
    const params = {}
    if (filterType.value) params.type = filterType.value
    if (filterCategory.value) params.category = filterCategory.value
    if (filterDifficulty.value) params.difficulty = filterDifficulty.value
    if (filterKeyword.value) params.keyword = filterKeyword.value
    const res = await listQuestionBank(params)
    let filtered = res.data
    if (filterTags.value && filterTags.value.length > 0) {
      filtered = filtered.filter(q => {
        const qTags = (q.tags || '').toLowerCase()
        return filterTags.value.some(t => qTags.includes(t.toLowerCase()))
      })
    }
    questions.value = filtered
  } catch { /* ignore */ } finally {
    questionsLoading.value = false
  }
}

async function fetchCategories() {
  try {
    const res = await getQuestionBankCategories()
    categories.value = res.data
  } catch { /* ignore */ }
}

async function fetchTags() {
  try {
    const res = await getQuestionBankTags()
    allTags.value = res.data
  } catch { /* ignore */ }
}

function onManualSelectChange(keys) {
  manualSelectedIds.value = keys
}

function addToSelected() {
  const existingIds = new Set(selectedQuestions.value.map(q => q.id))
  let addedCount = 0
  for (const qid of manualSelectedIds.value) {
    if (existingIds.has(qid)) continue
    const q = questions.value.find(item => item.id === qid)
    if (q) {
      selectedQuestions.value.push({
        id: q.id, type: q.type,
        content: q.content.length > 50 ? q.content.substring(0, 50) + '...' : q.content,
        category: q.category, difficulty: q.difficulty,
        score: q.score, scoreOverride: q.score,
        globalIndex: selectedQuestions.value.length + 1,
      })
      addedCount++
    }
  }
  if (addedCount > 0) message.success(`已添加 ${addedCount} 题`)
  manualSelectedIds.value = []
}

function removeSelected(idx) {
  selectedQuestions.value.splice(idx, 1)
  selectedQuestions.value.forEach((q, i) => { q.globalIndex = i + 1 })
}

function moveSelectedUp(globalIdx) {
  if (globalIdx <= 1) return
  const idx = globalIdx - 1
  const prev = selectedQuestions.value[idx - 1]
  selectedQuestions.value[idx - 1] = selectedQuestions.value[idx]
  selectedQuestions.value[idx] = prev
  selectedQuestions.value.forEach((q, i) => { q.globalIndex = i + 1 })
}

function moveSelectedDown(globalIdx) {
  if (globalIdx >= selectedQuestions.value.length) return
  const idx = globalIdx - 1
  const next = selectedQuestions.value[idx + 1]
  selectedQuestions.value[idx + 1] = selectedQuestions.value[idx]
  selectedQuestions.value[idx] = next
  selectedQuestions.value.forEach((q, i) => { q.globalIndex = i + 1 })
}

function clearSelected() {
  selectedQuestions.value = []
}

async function handleManualCompose() {
  if (selectedQuestions.value.length === 0) {
    message.error('请先选择题目')
    return
  }
  if (!store.title.trim()) {
    message.error('请输入考试标题')
    return
  }
  composing.value = true
  try {
    const questionIds = selectedQuestions.value.map(q => q.id)
    const scoreOverrides = {}
    for (const q of selectedQuestions.value) {
      if (q.scoreOverride !== q.score) scoreOverrides[q.id] = q.scoreOverride
    }
    const payload = {
      title: store.title,
      classroom_id: store.classroomId || null,
      duration: store.duration,
      question_ids: questionIds,
      score_overrides: Object.keys(scoreOverrides).length > 0 ? scoreOverrides : null,
      template_id: store.templateId || null,
      exam_type: store.examType,
    }
    const res = await composeExamFromBank(payload)
    const exam_id = res.data.exam_id

    // 获取完整题目列表供审核
    const previewRes = await previewExam(exam_id)
    store.setManualResult(exam_id, previewRes.data.questions)

    message.success(`组卷成功！共 ${res.data.question_count} 题，请审核确认`)
    // 自动跳转到审核页
    store.setStep(2)
    router.push('/exam-compose/review')
  } catch (e) {
    message.error('组卷失败，请重试')
  } finally {
    composing.value = false
  }
}

function goBack() {
  store.setStep(0)
  router.push('/exam-compose')
}

onMounted(() => {
  fetchQuestions()
  fetchCategories()
  fetchTags()
})
</script>

<style scoped>
.step-compose-manual {
  padding: 0 8px;
}
.compose-layout {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}
.compose-left {
  flex: 3;
  min-width: 0;
}
.compose-right {
  flex: 2;
  min-width: 320px;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  position: sticky;
  top: 72px;
}
.filter-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}
.config-card :deep(.ant-card-body) { padding: 12px 14px; }
.config-card :deep(.ant-card-head) { min-height: 36px; padding: 0 14px; }
.config-card :deep(.ant-card-head-title) { padding: 8px 0; font-size: 13px; }
.q-content-cell {
  max-height: 60px; overflow: hidden;
  display: -webkit-box; -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; line-height: 1.4; font-size: 13px;
}
@media (max-width: 1024px) {
  .compose-layout { flex-direction: column; }
  .compose-right { max-width: 100%; width: 100%; position: static; }
}
</style>
