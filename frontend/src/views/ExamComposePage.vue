<template>
  <div class="cv-page exam-compose-page">
    <a-page-header title="智能组卷" sub-title="AI 智能组卷 / 人工选题组卷" style="padding-bottom: 12px">
      <template #extra>
        <a-button type="primary" @click="showTemplateModal = true">
          <template #icon><PlusOutlined /></template>
          创建模板
        </a-button>
      </template>
    </a-page-header>

    <div class="compose-layout">
      <!-- ====== 左侧：工作区 ====== -->
      <div class="compose-left">
        <a-tabs v-model:activeKey="activeTab" size="large">
          <!-- ── AI 组卷 Tab ── -->
          <a-tab-pane key="ai" tab="🤖 AI 智能组卷">
            <!-- Phase 1: 输入需求 -->
            <div v-if="!aiResult" class="ai-compose-panel">
              <a-form layout="vertical">
                <a-form-item label="描述你的组卷需求">
                  <a-textarea
                    v-model:value="aiForm.prompt"
                    :rows="4"
                    placeholder="例如：高数期中，5道单选3道大题，覆盖极限和积分，难度中等偏上"
                  />
                </a-form-item>
                <a-row :gutter="16">
                  <a-col :span="8">
                    <a-form-item label="试卷模板（可选）">
                      <a-select v-model:value="aiForm.template_id" allow-clear placeholder="选择模板" style="width: 100%">
                        <a-select-option v-for="t in templates" :key="t.id" :value="t.id">
                          {{ t.name }}
                          <a-tag v-if="t.is_builtin" color="blue" style="margin-left: 4px; font-size: 10px">内置</a-tag>
                        </a-select-option>
                      </a-select>
                    </a-form-item>
                  </a-col>
                  <a-col :span="8">
                    <a-form-item label="出题场景（可选）">
                      <a-select v-model:value="aiForm.scene" allow-clear placeholder="选择场景" style="width: 100%">
                        <a-select-option value="sync">同步教学</a-select-option>
                        <a-select-option value="quiz">阶段测试</a-select-option>
                        <a-select-option value="midterm">期中考试</a-select-option>
                        <a-select-option value="final">期末考试</a-select-option>
                        <a-select-option value="contest">竞赛模拟</a-select-option>
                      </a-select>
                    </a-form-item>
                  </a-col>
                  <a-col :span="8">
                    <a-form-item label="关联课堂（可选）">
                      <a-select v-model:value="aiForm.classroom_id" allow-clear placeholder="选择课堂" style="width: 100%">
                        <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
                      </a-select>
                    </a-form-item>
                  </a-col>
                </a-row>
                <a-form-item label="考试标题（可选，AI可自动生成）">
                  <a-input v-model:value="aiForm.title" placeholder="如：高一数学期中考试" />
                </a-form-item>
                <a-button type="primary" size="large" block :loading="aiComposing" @click="handleAICompose" style="margin-top: 8px">
                  <template #icon><ThunderboltOutlined /></template>
                  智能组卷
                </a-button>
                <p v-if="aiComposing" style="text-align: center; color: #999; margin-top: 8px; font-size: 13px">
                  🤖 AI 正在为你智能组卷，请耐心等待（约 10-30 秒）...
                </p>
              </a-form>
            </div>

            <!-- Phase 2: 审核确认面板 -->
            <div v-if="aiResult" class="ai-review-panel">
              <!-- 试卷概览 -->
              <div class="review-overview">
                <a-row :gutter="16" align="middle">
                  <a-col :span="16">
                    <h3 style="margin: 0">{{ aiResult.title }}</h3>
                    <p style="margin: 4px 0 0; color: #888; font-size: 13px">
                      {{ aiResult.question_count }} 题 · AI建议总分 {{ aiReviewTotalScore }} 分 · 状态：草稿（待审核）
                    </p>
                  </a-col>
                  <a-col :span="8" style="text-align: right">
                    <a-space>
                      <a-button @click="resetAICompose">重新组卷</a-button>
                      <a-button type="primary" @click="handlePublishAIExam" :loading="publishing">
                        <template #icon><CheckOutlined /></template>
                        确认发布
                      </a-button>
                    </a-space>
                  </a-col>
                </a-row>
              </div>

              <!-- 难度分布概览 -->
              <div class="difficulty-overview">
                <span class="diff-label">难度分布：</span>
                <span v-for="d in aiDifficultyDistribution" :key="d.level" class="diff-bar-seg" :style="{ width: d.percent + '%', background: d.color }">
                  {{ d.label }} {{ d.count }}题
                </span>
              </div>

              <!-- 逐题审核列表 -->
              <div class="review-questions">
                <div v-for="(q, idx) in aiReviewQuestions" :key="idx" class="review-question-item">
                  <div class="review-q-header">
                    <span class="review-q-order">{{ idx + 1 }}</span>
                    <a-tag :color="getTypeColor(q.type)" size="small">{{ getTypeText(q.type) }}</a-tag>
                    <a-tag v-if="q.source" :color="q.source === 'AI生成' ? 'orange' : 'green'" size="small">{{ q.source }}</a-tag>
                    <span v-for="i in (q.difficulty || 2)" :key="i" style="color: #faad14; font-size: 10px">★</span>
                    <span v-if="q.category" class="review-q-category">{{ q.category }}</span>
                  </div>
                  <div class="review-q-content">
                    <div :class="{ 'content-expanded': q.expanded }">
                      <LatexText :content="q.content" />
                    </div>
                    <a-button type="link" size="small" @click="q.expanded = !q.expanded">
                      {{ q.expanded ? '收起' : '展开全文' }}
                    </a-button>
                  </div>
                  <div v-if="q.expanded && q.options" class="review-q-options">
                    <div v-for="(opt, oi) in q.options" :key="oi" class="review-q-option"><LatexText :content="opt" /></div>
                  </div>
                  <div v-if="q.expanded && q.analysis" class="review-q-analysis">
                    <span class="analysis-label">解析：</span><LatexText :content="q.analysis" />
                  </div>
                  <div class="review-q-actions">
                    <div class="review-q-score">
                      <span class="score-label">分值</span>
                      <a-input-number v-model:value="q.scoreOverride" :min="1" :max="100" size="small" style="width: 64px" />
                      <span class="score-hint">（建议 {{ q.suggested_score || q.score }} 分）</span>
                    </div>
                    <a-space size="small">
                      <a-button size="small" @click="handleSwapAIQuestion(idx)" :loading="q.swapping">
                        <template #icon><SwapOutlined /></template>
                        换一题
                      </a-button>
                      <a-button size="small" danger @click="removeAIQuestion(idx)">
                        <template #icon><DeleteOutlined /></template>
                        删除
                      </a-button>
                    </a-space>
                  </div>
                </div>
              </div>

              <!-- 换题候选弹窗 -->
              <a-modal
                v-model:open="showSwapModal"
                title="选择替换题目"
                width="700px"
                :footer="null"
              >
                <div v-if="swapCandidates.length === 0" style="text-align: center; padding: 24px; color: #999">
                  暂无候选题目，请调整筛选条件
                </div>
                <div v-else class="swap-candidates-list">
                  <div v-for="c in swapCandidates" :key="c.id" class="swap-candidate-item" @click="selectSwapCandidate(c)">
                    <div class="swap-candidate-left">
                      <a-tag :color="getTypeColor(c.type)" size="small">{{ getTypeText(c.type) }}</a-tag>
                      <span v-for="i in (c.difficulty || 2)" :key="i" style="color: #faad14; font-size: 10px">★</span>
                      <LatexText :content="c.content" />
                    </div>
                    <div class="swap-candidate-right">
                      <span style="color: #3751FE; font-weight: 600">{{ c.score }}分</span>
                      <a-tag v-if="c.source" :color="c.source === 'AI生成' ? 'orange' : 'green'" size="small">{{ c.source }}</a-tag>
                    </div>
                  </div>
                </div>
              </a-modal>
            </div>
          </a-tab-pane>

          <!-- ── 人工组卷 Tab ── -->
          <a-tab-pane key="manual" tab="📝 人工组卷">
            <div class="manual-compose-panel">
              <!-- 操作提示 -->
              <a-alert v-if="questions.length > 0" type="info" show-icon style="margin-bottom: 12px">
                <template #message>
                  在下方表格中勾选题目，然后点击「加入已选」按钮添加到右侧已选列表
                </template>
              </a-alert>

              <!-- 筛选栏 -->
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

              <!-- 题库表格 -->
              <a-table
                :columns="questionColumns"
                :data-source="questions"
                row-key="id"
                size="small"
                :pagination="{ pageSize: 10, showSizeChanger: false }"
                :row-selection="{
                  selectedRowKeys: manualSelectedIds,
                  onChange: onManualSelectChange,
                }"
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
          </a-tab-pane>
        </a-tabs>
      </div>

      <!-- ====== 右侧：模板 + 已选 + 配置 ====== -->
      <div class="compose-right">
        <!-- 模板信息卡片 -->
        <a-card size="small" class="template-card">
          <template #title>
            <span>📋 试卷模板</span>
          </template>
          <template #extra>
            <a-button type="link" size="small" @click="showTemplateModal = true">
              <template #icon><PlusOutlined /></template>
              新建
            </a-button>
          </template>
          <a-select
            v-model:value="selectedTemplateId"
            allow-clear
            placeholder="选择模板（可选，软约束）"
            style="width: 100%"
            @change="onTemplateChange"
          >
            <a-select-option v-for="t in templates" :key="t.id" :value="t.id">
              <span>{{ t.name }}</span>
              <a-tag v-if="t.is_builtin" color="blue" style="margin-left: 6px; font-size: 10px">内置</a-tag>
            </a-select-option>
          </a-select>

          <template v-if="currentTemplate">
            <div class="template-info">
              <div class="template-row">
                <span class="label">总分</span>
                <span class="value">{{ currentTemplate.total_score }} 分</span>
              </div>
              <div class="template-row">
                <span class="label">时长</span>
                <span class="value">{{ currentTemplate.duration }} 分钟</span>
              </div>
              <div v-if="currentTemplate.description" class="template-desc">{{ currentTemplate.description }}</div>
            </div>
            <div class="template-structure">
              <div v-for="(sec, i) in (currentTemplate.structure || [])" :key="i" class="structure-row">
                <a-tag size="small">{{ getTypeText(sec.type) }}</a-tag>
                <span class="structure-count">{{ sec.count }}题 × {{ sec.score_per }}分</span>
                <span v-if="sec.knowledge && sec.knowledge.length" class="structure-knowledge">
                  {{ sec.knowledge.join('、') }}
                </span>
              </div>
            </div>
            <div class="template-actions">
              <a-button
                v-if="!currentTemplate.is_builtin"
                type="link"
                danger
                size="small"
                @click="handleDeleteTemplate(currentTemplate.id)"
              >
                删除此模板
              </a-button>
            </div>
          </template>
        </a-card>

        <!-- 已选题目列表（题型分组） -->
        <a-card size="small" class="selected-card">
          <template #title>
            <span>📝 试题篮</span>
          </template>
          <template #extra>
            <span class="selected-stats">{{ selectedQuestions.length }} 题 · {{ selectedTotalScore }} 分</span>
          </template>

          <div v-if="selectedQuestions.length === 0" class="empty-selected">
            <div class="empty-icon">📋</div>
            <div class="empty-text">暂无题目</div>
            <div class="empty-hint">请从左侧题库中勾选并加入</div>
          </div>
          <div v-else>
            <!-- 按题型分组 -->
            <div v-for="group in selectedQuestionGroups" :key="group.type" class="selected-group">
              <div class="selected-group-header">
                <a-tag :color="getTypeColor(group.type)" size="small">{{ getTypeText(group.type) }}</a-tag>
                <span class="selected-group-count">{{ group.items.length }}题 · {{ group.totalScore }}分</span>
              </div>
              <div v-for="(item, idx) in group.items" :key="item.id" class="selected-item">
                <div class="selected-item-left">
                  <span class="selected-order">{{ item.globalIndex }}</span>
                  <LatexText :content="item.content" class="selected-content" />
                </div>
                <div class="selected-item-right">
                  <a-input-number
                    v-model:value="item.scoreOverride"
                    :min="1"
                    :max="100"
                    size="small"
                    style="width: 60px"
                  />
                  <span class="score-unit">分</span>
                  <a-button type="text" size="small" @click="moveSelectedUp(item.globalIndex)" :disabled="item.globalIndex <= 1">
                    <template #icon><UpOutlined /></template>
                  </a-button>
                  <a-button type="text" size="small" @click="moveSelectedDown(item.globalIndex)" :disabled="item.globalIndex >= selectedQuestions.length">
                    <template #icon><DownOutlined /></template>
                  </a-button>
                  <a-button type="text" danger size="small" @click="removeSelected(item.globalIndex - 1)" class="remove-btn">
                    <template #icon><CloseOutlined /></template>
                  </a-button>
                </div>
              </div>
            </div>

            <!-- 总分警告 -->
            <div v-if="selectedTotalScore !== (currentTemplate?.total_score || 0) && currentTemplate" class="score-warning-bar">
              <a-alert type="warning" show-icon :message="`当前总分 ${selectedTotalScore} 分与模板设定 ${currentTemplate.total_score} 分不一致`" style="margin-top: 8px" />
            </div>
          </div>

          <div v-if="selectedQuestions.length > 0" class="selected-footer">
            <a-button type="link" danger size="small" @click="clearSelected">清空已选</a-button>
          </div>
        </a-card>

        <!-- 考试配置 -->
        <a-card size="small" class="config-card">
          <template #title>
            <span>⚙️ 考试配置</span>
          </template>
          <a-form layout="vertical" size="small">
            <a-form-item label="考试标题" required>
              <a-input v-model:value="examConfig.title" placeholder="输入考试标题" />
            </a-form-item>
            <a-row :gutter="12">
              <a-col :span="14">
                <a-form-item label="关联课堂">
                  <a-select v-model:value="examConfig.classroom_id" allow-clear placeholder="选择课堂" style="width: 100%">
                    <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
                  </a-select>
                </a-form-item>
              </a-col>
              <a-col :span="10">
                <a-form-item label="时长(分钟)">
                  <a-input-number v-model:value="examConfig.duration" :min="10" :max="180" style="width: 100%" />
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

    <!-- ====== 创建模板弹窗 ====== -->
    <a-modal
      v-model:open="showTemplateModal"
      title="创建自定义试卷模板"
      @ok="handleCreateTemplate"
      :confirm-loading="creatingTemplate"
      width="680px"
    >
      <a-form :label-col="{ span: 4 }" :wrapper-col="{ span: 18 }">
        <a-form-item label="模板名称" required>
          <a-input v-model:value="templateForm.name" placeholder="如：期中考试模板" />
        </a-form-item>
        <a-form-item label="说明">
          <a-textarea v-model:value="templateForm.description" :rows="2" placeholder="模板用途描述" />
        </a-form-item>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="总分" :label-col="{ span: 8 }">
              <a-input-number v-model:value="templateForm.total_score" :min="10" :max="500" style="width: 100%" />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="时长" :label-col="{ span: 8 }">
              <a-input-number v-model:value="templateForm.duration" :min="10" :max="180" addon-after="分钟" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-divider>题型结构</a-divider>
        <div v-for="(sec, idx) in templateForm.structure" :key="idx" class="template-section-row">
          <a-row :gutter="8" align="middle">
            <a-col :span="6">
              <a-select v-model:value="sec.type" style="width: 100%">
                <a-select-option value="single">单选题</a-select-option>
                <a-select-option value="multi">多选题</a-select-option>
                <a-select-option value="judge">判断题</a-select-option>
                <a-select-option value="fill">填空题</a-select-option>
                <a-select-option value="essay">简答题</a-select-option>
              </a-select>
            </a-col>
            <a-col :span="4">
              <a-input-number v-model:value="sec.count" :min="1" :max="50" style="width: 100%" placeholder="数量" />
            </a-col>
            <a-col :span="4">
              <a-input-number v-model:value="sec.score_per" :min="1" :max="100" style="width: 100%" placeholder="每题分" />
            </a-col>
            <a-col :span="7">
              <a-input v-model:value="sec.knowledgeStr" placeholder="知识点（逗号分隔）" />
            </a-col>
            <a-col :span="3">
              <a-rate v-model:value="sec.difficulty" :count="5" style="font-size: 14px" />
            </a-col>
          </a-row>
          <div class="section-row-actions">
            <a-button type="link" danger size="small" @click="templateForm.structure.splice(idx, 1)">删除此行</a-button>
          </div>
        </div>
        <a-button type="dashed" block @click="addTemplateSection">
          <template #icon><PlusOutlined /></template>
          添加题型
        </a-button>
        <div v-if="templateForm.structure.length" class="estimated-score">
          预计总分：<span :class="{ 'score-warning': templateEstimatedScore !== templateForm.total_score }">{{ templateEstimatedScore }}</span> 分
          <span v-if="templateEstimatedScore !== templateForm.total_score" class="score-hint">（与设定总分 {{ templateForm.total_score }} 不一致）</span>
        </div>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import {
  ThunderboltOutlined, PlusOutlined, CloseOutlined, CheckOutlined,
  SwapOutlined, DeleteOutlined, UpOutlined, DownOutlined
} from '@ant-design/icons-vue'
import {
  listExamTemplates, createExamTemplate, deleteExamTemplate,
  aiComposeExam, previewExam, publishExam,
  swapQuestion, swapQuestionCandidates
} from '@/api/examTemplate'
import {
  listQuestionBank, composeExamFromBank, getQuestionBankCategories,
  getQuestionBankTags
} from '@/api/questionBank'
import { listClassrooms } from '@/api/classroom'
import LatexText from '@/components/LatexText.vue'

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
const aiResult = ref(null)  // { exam_id, title, question_count, total_score, questions }
const publishing = ref(false)

// AI 审核中的题目列表（可编辑分值、换题、删除）
const aiReviewQuestions = ref([])
const showSwapModal = ref(false)
const swapCandidates = ref([])
const swapTargetIndex = ref(-1)  // 当前正在换题的题目索引

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

// 按题型分组展示
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

// ── 方法 ──

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

function getTypeColor(type) {
  return { single: 'blue', multi: 'purple', judge: 'green', fill: 'orange', essay: 'red' }[type] || 'default'
}

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
    // 知识点标签筛选：前端先获取所有题目再过滤
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
    // 将出题场景加入 prompt
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

    // 构建审核题目列表（深拷贝，每题可编辑分值）
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
  // 重新编号
  aiReviewQuestions.value.forEach((q, i) => { q.order = i + 1 })
}

// ── AI 组卷智能换题 ──
async function handleSwapAIQuestion(idx) {
  const q = aiReviewQuestions.value[idx]
  q.swapping = true
  swapTargetIndex.value = idx

  // 获取所有当前题目的 bank_id 作为排除列表
  const excludeIds = aiReviewQuestions.value
    .filter(item => item.bank_id && item !== q)
    .map(item => item.bank_id)

  try {
    const payload = {
      question_id: q.bank_id || 0,
      exclude_ids: excludeIds,
    }

    // 当 bank_id 为空时，附带题目元数据让后端能匹配类似题
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
      // 提示匹配级别
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
  // 替换题目（保留原分值）
  aiReviewQuestions.value[idx] = {
    ...candidate,
    order: oldQ.order,
    scoreOverride: oldQ.scoreOverride,  // 保留教师设定的分值
    suggested_score: candidate.score,
    expanded: false,
    swapping: false,
  }

  showSwapModal.value = false
  message.success('换题成功')
}

// ── AI 组卷发布 ──
async function handlePublishAIExam() {
  if (!aiResult.value) return
  publishing.value = true
  try {
    const scoreOverrides = {}
    const removeIds = []
    // 遍历审核后的题目，构建 score_overrides
    for (const q of aiReviewQuestions.value) {
      if (q.scoreOverride !== q.score && q.scoreOverride !== q.suggested_score) {
        // 需要获取 Question 表的 id（而非 bank_id）
        // AI 组卷后题目已入库为 Question，但返回中只有 bank_id
        // 这里暂用 bank_id 作为 key，publish API 会处理
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
  // 重新编号
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
</script>

<style scoped>
.exam-compose-page {
  padding: 0 24px 24px;
}

.compose-layout {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.compose-left {
  flex: 3;
  min-width: 0;
  background: #fff;
  border-radius: 10px;
  padding: 20px 24px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
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

/* AI 组卷面板 */
.ai-compose-panel {
  max-width: 640px;
}

/* AI 审核确认面板 */
.ai-review-panel {
  margin-top: 0;
}

.review-overview {
  padding: 12px 16px;
  background: linear-gradient(135deg, #f0f5ff 0%, #e8f4f8 100%);
  border-radius: 8px;
  margin-bottom: 12px;
}

.difficulty-overview {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-bottom: 12px;
  background: #f8f9fc;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
}

.diff-label {
  color: #666;
  font-weight: 500;
  flex-shrink: 0;
}

.diff-bar-seg {
  text-align: center;
  font-size: 11px;
  color: #fff;
  padding: 2px 4px;
  border-radius: 3px;
  min-width: 40px;
}

/* 逐题审核 */
.review-questions {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.review-question-item {
  padding: 12px 14px;
  background: #fff;
  border: 1px solid #eef0f5;
  border-radius: 8px;
  transition: border-color 0.2s;
}

.review-question-item:hover {
  border-color: #3751FE;
}

.review-q-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 6px;
}

.review-q-order {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #3751FE;
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
}

.review-q-category {
  color: #888;
  font-size: 12px;
}

.review-q-content {
  font-size: 13px;
  color: #333;
  margin-bottom: 6px;
}

.content-expanded {
  white-space: pre-wrap;
}

.review-q-options {
  margin: 6px 0;
  padding: 6px 10px;
  background: #f8f9fc;
  border-radius: 4px;
}

.review-q-option {
  font-size: 12px;
  color: #555;
  padding: 2px 0;
}

.review-q-analysis {
  font-size: 12px;
  color: #666;
  padding: 4px 8px;
  background: #fffbe6;
  border-radius: 4px;
  margin: 4px 0;
}

.analysis-label {
  color: #fa8c16;
  font-weight: 500;
}

.review-q-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 6px;
}

.review-q-score {
  display: flex;
  align-items: center;
  gap: 4px;
}

.score-label {
  color: #666;
  font-size: 13px;
}

.score-hint {
  color: #aaa;
  font-size: 11px;
}

/* 换题候选弹窗 */
.swap-candidates-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.swap-candidate-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  background: #f8f9fc;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.2s;
  border: 1px solid #eef0f5;
}

.swap-candidate-item:hover {
  background: #e8f4f8;
  border-color: #3751FE;
}

.swap-candidate-left {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
}

.swap-candidate-right {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}

/* 人工组卷面板 */
.filter-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

/* 模板卡片 */
.template-card :deep(.ant-card-body) {
  padding: 12px 14px;
}

.template-card :deep(.ant-card-head) {
  min-height: 36px;
  padding: 0 14px;
}

.template-card :deep(.ant-card-head-title) {
  padding: 8px 0;
  font-size: 13px;
}

.template-info {
  margin-top: 10px;
}

.template-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
  font-size: 13px;
}

.template-row .label {
  color: #999;
  width: 36px;
  flex-shrink: 0;
}

.template-row .value {
  color: #333;
  font-weight: 500;
}

.template-desc {
  font-size: 12px;
  color: #888;
  margin-top: 4px;
  line-height: 1.4;
}

.template-structure {
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px dashed #e8e8e8;
}

.structure-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
  font-size: 12px;
}

.structure-count {
  color: #555;
  font-weight: 500;
}

.structure-knowledge {
  color: #aaa;
  font-size: 11px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 120px;
}

.template-actions {
  margin-top: 6px;
}

/* 已选题目卡片（题型分组） */
.selected-card :deep(.ant-card-body) {
  padding: 10px 14px;
  max-height: 380px;
  overflow-y: auto;
}

.selected-card :deep(.ant-card-head) {
  min-height: 36px;
  padding: 0 14px;
}

.selected-card :deep(.ant-card-head-title) {
  padding: 8px 0;
  font-size: 13px;
}

.selected-stats {
  font-size: 12px;
  color: #3751FE;
  font-weight: 600;
}

.empty-selected {
  text-align: center;
  padding: 16px 0;
}

.empty-icon {
  font-size: 28px;
  margin-bottom: 6px;
}

.empty-text {
  font-size: 13px;
  color: #999;
  font-weight: 500;
}

.empty-hint {
  font-size: 11px;
  color: #ccc;
  margin-top: 2px;
}

.selected-group {
  margin-bottom: 8px;
}

.selected-group-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
  padding-bottom: 4px;
  border-bottom: 1px dashed #e8e8e8;
}

.selected-group-count {
  color: #555;
  font-size: 12px;
  font-weight: 500;
}

.selected-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4px 8px;
  background: #f8f9fc;
  border-radius: 6px;
  border: 1px solid #eef0f5;
  transition: background 0.15s;
  margin-bottom: 3px;
}

.selected-item:hover {
  background: #f0f2fa;
}

.selected-item-left {
  display: flex;
  align-items: center;
  gap: 6px;
  min-width: 0;
  flex: 1;
}

.selected-order {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #3751FE;
  color: #fff;
  font-size: 10px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.selected-content {
  font-size: 12px;
  color: #333;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 130px;
}

.selected-item-right {
  display: flex;
  align-items: center;
  gap: 2px;
  flex-shrink: 0;
}

.score-unit {
  font-size: 11px;
  color: #aaa;
}

.remove-btn {
  padding: 0 4px !important;
}

.score-warning-bar {
  margin-top: 6px;
}

.selected-footer {
  margin-top: 6px;
  padding-top: 6px;
  border-top: 1px solid #f0f0f0;
  text-align: right;
}

/* 考试配置卡片 */
.config-card :deep(.ant-card-body) {
  padding: 12px 14px;
}

.config-card :deep(.ant-card-head) {
  min-height: 36px;
  padding: 0 14px;
}

.config-card :deep(.ant-card-head-title) {
  padding: 8px 0;
  font-size: 13px;
}

/* 创建模板弹窗 */
.template-section-row {
  margin-bottom: 10px;
  padding: 10px 12px;
  background: #fafbfc;
  border-radius: 6px;
  border: 1px solid #f0f0f0;
}

.section-row-actions {
  margin-top: 4px;
  text-align: right;
}

.estimated-score {
  margin-top: 10px;
  font-size: 13px;
  color: #666;
}

.estimated-score .score-warning {
  color: #fa8c16;
  font-weight: 600;
}

.score-hint {
  color: #fa8c16;
  font-size: 12px;
}

/* 响应式 */
@media (max-width: 1024px) {
  .compose-layout {
    flex-direction: column;
  }

  .compose-right {
    max-width: 100%;
    width: 100%;
    position: static;
  }
}

.q-content-cell {
  max-height: 60px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  line-height: 1.4;
  font-size: 13px;
}
</style>
