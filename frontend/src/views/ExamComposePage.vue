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
import {
  ThunderboltOutlined, PlusOutlined, CloseOutlined, CheckOutlined,
  SwapOutlined, DeleteOutlined, UpOutlined, DownOutlined
} from '@ant-design/icons-vue'
import LatexText from '@/components/LatexText.vue'
import { useExamCompose } from '@/composables/useExamCompose'

// 业务逻辑全部由 composable 管理
const {
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
} = useExamCompose()
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
