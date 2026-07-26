/**
 * 智能组卷业务逻辑 Composable
 *
 * 从 ExamComposePage.vue 抽取，包含：
 * - AI 组卷流程（生成、审核、换题、发布）
 * - 人工组卷流程（筛选、选题、组卷）
 * - 模板管理（创建、删除）
 * - 考试配置
 */
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import {
  listExamTemplates, createExamTemplate, deleteExamTemplate,
  aiComposeExam, publishExam,
  swapQuestionCandidates,
} from '@/api/examTemplate'
import {
  listQuestionBank, composeExamFromBank, getQuestionBankCategories,
  getQuestionBankTags,
} from '@/api/questionBank'
import { listClassrooms } from '@/api/classroom'

export function useExamCompose() {
  const router = useRouter()

  // ── 公共数据 ──
  const templates = ref([])
  const classrooms = ref([])
  const categories = ref([])
  const allTags = ref([])
  const selectedTemplateId = ref(null)

  const currentTemplate = computed(() => {
    if (!selectedTemplateId.value) return null
    return templates.value.find(t => t.id === selectedTemplateId.value) || null
  })

  // ── Tab 状态 ──
  const activeTab = ref('ai')

  // ── AI 组卷 ──
  const aiForm = ref({
    prompt: '',
    template_id: null,
    scene: null,
    classroom_id: null,
    title: '',
  })
  const aiComposing = ref(false)
  const aiResult = ref(null)
  const publishing = ref(false)

  const aiReviewQuestions = ref([])
  const showSwapModal = ref(false)
  const swapCandidates = ref([])
  const swapTargetIndex = ref(-1)

  const aiReviewTotalScore = computed(() => {
    return aiReviewQuestions.value.reduce((sum, q) => sum + (q.scoreOverride || q.score), 0)
  })

  const aiDifficultyDistribution = computed(() => {
    const dist = {}
    for (const q of aiReviewQuestions.value) {
      const d = q.difficulty || 2
      dist[d] = (dist[d] || 0) + 1
    }
    const total = aiReviewQuestions.value.length || 1
    const colors = { 1: '#52c41a', 2: '#73d13d', 3: '#faad14', 4: '#ff7a45', 5: '#ff4d4f' }
    const labels = { 1: '简单', 2: '较易', 3: '中等', 4: '较难', 5: '困难' }
    return Object.entries(dist).sort((a, b) => a[0] - b[0]).map(([level, count]) => ({
      level: Number(level),
      count,
      percent: Math.round(count / total * 100),
      color: colors[level] || '#ccc',
      label: labels[level] || `${level}星`,
    }))
  })

  // ── 人工组卷 ──
  const questions = ref([])
  const questionsLoading = ref(false)
  const filterType = ref(null)
  const filterCategory = ref(null)
  const filterTags = ref([])
  const filterDifficulty = ref(null)
  const filterKeyword = ref(null)
  const manualSelectedIds = ref([])

  const manualSelectedCount = computed(() => manualSelectedIds.value.length)

  const questionColumns = [
    { key: 'type', title: '题型', width: 80 },
    { key: 'content', title: '内容', dataIndex: 'content', width: 300 },
    { key: 'category', title: '分类', dataIndex: 'category', width: 100, ellipsis: true },
    { key: 'difficulty', title: '难度', width: 90 },
    { key: 'score', title: '分值', dataIndex: 'score', width: 70, align: 'right' },
  ]

  // ── 已选题目 ──
  const selectedQuestions = ref([])
  const composing = ref(false)

  const selectedTotalScore = computed(() => {
    return selectedQuestions.value.reduce((sum, q) => sum + (q.scoreOverride || q.score), 0)
  })

  const selectedQuestionGroups = computed(() => {
    const typeOrder = ['single', 'multi', 'judge', 'fill', 'essay']
    const groups = {}
    let globalIdx = 1
    for (const q of selectedQuestions.value) {
      q.globalIndex = globalIdx++
      if (!groups[q.type]) {
        groups[q.type] = { type: q.type, items: [], totalScore: 0 }
      }
      groups[q.type].items.push(q)
      groups[q.type].totalScore += (q.scoreOverride || q.score)
    }
    return typeOrder.filter(t => groups[t]).map(t => groups[t])
  })

  // ── 考试配置 ──
  const examConfig = ref({
    title: '',
    classroom_id: null,
    duration: 90,
  })

  // ── 创建模板 ──
  const showTemplateModal = ref(false)
  const creatingTemplate = ref(false)
  const templateForm = ref({
    name: '',
    description: '',
    total_score: 100,
    duration: 90,
    structure: [{ type: 'single', count: 10, score_per: 5, knowledgeStr: '', difficulty: 2 }],
  })

  const templateEstimatedScore = computed(() => {
    return templateForm.value.structure.reduce((sum, s) => sum + (s.count || 0) * (s.score_per || 0), 0)
  })

  // ── 工具方法 ──

  function getTypeText(type) {
    return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
  }

  function getTypeColor(type) {
    return { single: 'blue', multi: 'purple', judge: 'green', fill: 'orange', essay: 'red' }[type] || 'default'
  }

  // ── 数据获取 ──

  async function fetchTemplates() {
    try {
      const res = await listExamTemplates()
      templates.value = res.data
    } catch { /* ignore */ }
  }

  async function fetchClassrooms() {
    try {
      const res = await listClassrooms()
      classrooms.value = res.data
    } catch { /* ignore */ }
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

  function onTemplateChange(templateId) {
    if (templateId) {
      const tmpl = templates.value.find(t => t.id === templateId)
      if (tmpl) {
        examConfig.value.duration = tmpl.duration
        aiForm.value.template_id = templateId
      }
    }
  }

  // ── AI 组卷 ──

  async function handleAICompose() {
    if (!aiForm.value.prompt.trim()) {
      message.error('请输入组卷需求描述')
      return
    }
    aiComposing.value = true
    aiResult.value = null
    aiReviewQuestions.value = []
    try {
      let prompt = aiForm.value.prompt
      if (aiForm.value.scene) {
        const sceneMap = { sync: '同步教学', quiz: '阶段测试', midterm: '期中考试', final: '期末考试', contest: '竞赛模拟' }
        prompt = `[${sceneMap[aiForm.value.scene] || aiForm.value.scene}] ${prompt}`
      }
      const payload = {
        prompt,
        template_id: aiForm.value.template_id || selectedTemplateId.value || null,
        classroom_id: aiForm.value.classroom_id || null,
        title: aiForm.value.title || '',
      }
      const res = await aiComposeExam(payload)
      aiResult.value = res.data
      aiReviewQuestions.value = res.data.questions.map(q => ({
        ...q,
        scoreOverride: q.suggested_score || q.score,
        expanded: false,
        swapping: false,
      }))
      message.success(`AI 组卷成功！共 ${res.data.question_count} 题，请审核后发布`)
    } catch (e) {
      const msg = e?.response?.data?.detail || 'AI 组卷失败，请检查 LLM 配置后重试'
      message.error(msg)
    } finally {
      aiComposing.value = false
    }
  }

  function resetAICompose() {
    aiResult.value = null
    aiReviewQuestions.value = []
  }

  function removeAIQuestion(idx) {
    aiReviewQuestions.value.splice(idx, 1)
    aiReviewQuestions.value.forEach((q, i) => { q.order = i + 1 })
  }

  async function handleSwapAIQuestion(idx) {
    const q = aiReviewQuestions.value[idx]
    q.swapping = true
    swapTargetIndex.value = idx

    const excludeIds = aiReviewQuestions.value
      .filter(item => item.bank_id && item !== q)
      .map(item => item.bank_id)

    try {
      const payload = {
        question_id: q.bank_id || 0,
        exclude_ids: excludeIds,
      }

      if (!q.bank_id) {
        payload.question_type = q.type
        payload.question_difficulty = q.difficulty
        payload.question_category = q.category
        payload.question_tags = q.tags
        payload.question_content = q.content
      }

      const res = await swapQuestionCandidates(payload)
      swapCandidates.value = res.data.candidates || []

      if (swapCandidates.value.length === 0) {
        message.warning('没有找到合适的替换题，请先向题库中添加更多同类型题目')
      } else {
        const matchLevel = res.data.match_level
        if (matchLevel >= 3) {
          message.info(`已放宽筛选条件，找到 ${swapCandidates.value.length} 道候选题（匹配级别 ${matchLevel}/4）`)
        }
        showSwapModal.value = true
      }
    } catch (e) {
      const msg = e?.response?.data?.detail || '换题请求失败'
      message.error(msg)
    } finally {
      q.swapping = false
    }
  }

  function selectSwapCandidate(candidate) {
    const idx = swapTargetIndex.value
    if (idx < 0 || idx >= aiReviewQuestions.value.length) return

    const oldQ = aiReviewQuestions.value[idx]
    aiReviewQuestions.value[idx] = {
      ...candidate,
      order: oldQ.order,
      scoreOverride: oldQ.scoreOverride,
      suggested_score: candidate.score,
      expanded: false,
      swapping: false,
    }

    showSwapModal.value = false
    message.success('换题成功')
  }

  async function handlePublishAIExam() {
    if (!aiResult.value) return
    publishing.value = true
    try {
      const scoreOverrides = {}
      for (const q of aiReviewQuestions.value) {
        if (q.scoreOverride !== q.score && q.scoreOverride !== q.suggested_score) {
          scoreOverrides[q.bank_id] = q.scoreOverride
        }
      }

      const payload = {
        score_overrides: Object.keys(scoreOverrides).length > 0 ? scoreOverrides : null,
        remove_question_ids: null,
        swap_questions: null,
      }

      const res = await publishExam(aiResult.value.exam_id, payload)
      message.success(`考试发布成功！${res.data.question_count} 题 / ${res.data.total_score} 分`)
      router.push(`/exams/${res.data.exam_id}`)
    } catch (e) {
      const msg = e?.response?.data?.detail || '发布失败'
      message.error(msg)
    } finally {
      publishing.value = false
    }
  }

  // ── 人工组卷 ──

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
          id: q.id,
          type: q.type,
          content: q.content.length > 50 ? q.content.substring(0, 50) + '...' : q.content,
          category: q.category,
          difficulty: q.difficulty,
          score: q.score,
          scoreOverride: q.score,
          globalIndex: selectedQuestions.value.length + 1,
        })
        addedCount++
      }
    }
    if (addedCount > 0) {
      message.success(`已添加 ${addedCount} 题`)
    }
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
    if (!examConfig.value.title.trim()) {
      message.error('请输入考试标题')
      return
    }
    composing.value = true
    try {
      const questionIds = selectedQuestions.value.map(q => q.id)
      const scoreOverrides = {}
      for (const q of selectedQuestions.value) {
        if (q.scoreOverride !== q.score) {
          scoreOverrides[q.id] = q.scoreOverride
        }
      }
      const payload = {
        title: examConfig.value.title,
        classroom_id: examConfig.value.classroom_id || null,
        duration: examConfig.value.duration,
        question_ids: questionIds,
        score_overrides: Object.keys(scoreOverrides).length > 0 ? scoreOverrides : null,
        template_id: selectedTemplateId.value || null,
      }
      const res = await composeExamFromBank(payload)
      message.success(`组卷成功！共 ${res.data.question_count} 题`)
      router.push(`/exams/${res.data.exam_id}`)
    } catch (e) {
      message.error('组卷失败，请重试')
    } finally {
      composing.value = false
    }
  }

  // ── 模板管理 ──

  function addTemplateSection() {
    templateForm.value.structure.push({
      type: 'single',
      count: 5,
      score_per: 5,
      knowledgeStr: '',
      difficulty: 2,
    })
  }

  async function handleCreateTemplate() {
    if (!templateForm.value.name.trim()) {
      message.error('请输入模板名称')
      return
    }
    if (templateForm.value.structure.length === 0) {
      message.error('请至少添加一个题型')
      return
    }
    creatingTemplate.value = true
    try {
      const structure = templateForm.value.structure.map(s => ({
        type: s.type,
        count: s.count,
        score_per: s.score_per,
        knowledge: s.knowledgeStr ? s.knowledgeStr.split(/[,，]/).map(k => k.trim()).filter(Boolean) : [],
        difficulty: s.difficulty,
      }))
      await createExamTemplate({
        name: templateForm.value.name,
        description: templateForm.value.description,
        total_score: templateForm.value.total_score,
        duration: templateForm.value.duration,
        structure,
      })
      message.success('模板创建成功')
      showTemplateModal.value = false
      templateForm.value = {
        name: '',
        description: '',
        total_score: 100,
        duration: 90,
        structure: [{ type: 'single', count: 10, score_per: 5, knowledgeStr: '', difficulty: 2 }],
      }
      fetchTemplates()
    } catch (e) {
      message.error('创建模板失败')
    } finally {
      creatingTemplate.value = false
    }
  }

  async function handleDeleteTemplate(templateId) {
    try {
      await deleteExamTemplate(templateId)
      message.success('模板已删除')
      if (selectedTemplateId.value === templateId) {
        selectedTemplateId.value = null
      }
      fetchTemplates()
    } catch (e) {
      message.error('删除模板失败')
    }
  }

  // ── 初始化 ──
  onMounted(() => {
    fetchTemplates()
    fetchClassrooms()
    fetchCategories()
    fetchTags()
    fetchQuestions()
  })

  return {
    // 公共数据
    templates, classrooms, categories, allTags,
    selectedTemplateId, currentTemplate,
    // Tab
    activeTab,
    // AI 组卷
    aiForm, aiComposing, aiResult, publishing,
    aiReviewQuestions, showSwapModal, swapCandidates,
    aiReviewTotalScore, aiDifficultyDistribution,
    handleAICompose, resetAICompose, removeAIQuestion,
    handleSwapAIQuestion, selectSwapCandidate, handlePublishAIExam,
    // 人工组卷
    questions, questionsLoading, filterType, filterCategory,
    filterTags, filterDifficulty, filterKeyword,
    manualSelectedIds, manualSelectedCount, questionColumns,
    fetchQuestions, onManualSelectChange, addToSelected,
    // 已选题目
    selectedQuestions, composing, selectedTotalScore,
    selectedQuestionGroups, removeSelected,
    moveSelectedUp, moveSelectedDown, clearSelected, handleManualCompose,
    // 考试配置
    examConfig, onTemplateChange,
    // 模板管理
    showTemplateModal, creatingTemplate, templateForm,
    templateEstimatedScore, addTemplateSection,
    handleCreateTemplate, handleDeleteTemplate,
    // 工具
    getTypeText, getTypeColor,
  }
}
