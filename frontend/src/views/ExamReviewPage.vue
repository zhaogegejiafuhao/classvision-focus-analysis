<template>
  <div class="cv-page exam-review-page">
    <a-page-header :title="`${reviewData?.exam_title || '考试'} - AI 审核`" @back="() => $router.push(`/exams/${examId}`)">
      <template #subTitle>
        <a-tag v-if="reviewData" color="blue">总分 {{ reviewData.exam_total_score }} 分</a-tag>
        <a-tag v-if="reviewData">提交 {{ reviewData.total_submissions }} 份</a-tag>
      </template>
      <template #extra>
        <a-space>
          <a-button @click="refreshData" :loading="loading">
            <template #icon><ReloadOutlined /></template>
            刷新
          </a-button>
          <a-button @click="handleExportReport" :loading="exporting">
            <template #icon><ExportOutlined /></template>
            导出报告
          </a-button>
          <a-button @click="showStatsDrawer = true" :loading="statsLoading">
            <template #icon><BarChartOutlined /></template>
            统计仪表盘
          </a-button>
          <a-button @click="showBatchModal = true">
            <template #icon><TeamOutlined /></template>
            批量确认
          </a-button>
          <a-popconfirm
            v-if="hasAiGradingSubmissions"
            title="确定重新 AI 批改所有未确认的题？"
            @confirm="regradeAllPending"
          >
            <a-button :loading="regrading">
              <template #icon><ReloadOutlined /></template>
              重新 AI 批改
            </a-button>
          </a-popconfirm>
          <a-button type="primary" @click="submitAllReview" :loading="submitting" :disabled="!canSubmitAll">
            提交全部审核
          </a-button>
        </a-space>
      </template>
    </a-page-header>

    <!-- 整体进度 -->
    <a-card v-if="reviewData" size="small" style="margin: 0 24px 16px">
      <a-row :gutter="16">
        <a-col :span="6">
          <a-statistic title="审核进度" :value="reviewData.review_progress.confirmed" :suffix="`/ ${reviewData.review_progress.total}`" />
        </a-col>
        <a-col :span="6">
          <a-statistic title="AI 批改中" :value="reviewData.status_counts.ai_grading" />
        </a-col>
        <a-col :span="6">
          <a-statistic title="待审核" :value="reviewData.status_counts.ai_graded" />
        </a-col>
        <a-col :span="6">
          <a-statistic title="已锁定" :value="reviewData.status_counts.graded" value-style="{ color: '#52c41a' }" />
        </a-col>
      </a-row>
      <a-progress
        :percent="reviewProgressPct"
        :status="reviewProgressPct === 100 ? 'success' : 'active'"
        style="margin-top: 12px"
      />
    </a-card>

    <a-spin :spinning="loading">
      <div v-if="reviewData && reviewData.questions.length" class="review-body">
        <!-- 左侧：题目列表 -->
        <div class="question-sidebar">
          <a-card title="题目列表" size="small">
            <a-list :data-source="reviewData.questions" :split="false">
              <template #renderItem="{ item, index }">
                <a-list-item
                  :class="['question-item', { active: currentQuestionId === item.question_id }]"
                  @click="selectQuestion(item.question_id)"
                >
                  <a-list-item-meta>
                    <template #title>
                      <span>第 {{ index + 1 }} 题</span>
                      <a-tag :color="getTypeColor(item.question_type)" size="small" style="margin-left: 8px">
                        {{ getTypeText(item.question_type) }}
                      </a-tag>
                      <span style="color: #999; margin-left: 8px">({{ item.max_score }}分)</span>
                    </template>
                    <template #description>
                      <a-badge
                        :count="getQuestionPendingCount(item)"
                        :overflow-count="99"
                        :offset="[6, 0]"
                        :number-style="{ backgroundColor: '#ff4d4f' }"
                      >
                        <span style="font-size: 12px">
                          已确认 {{ getQuestionConfirmedCount(item) }} / {{ item.answers.length }}
                        </span>
                      </a-badge>
                    </template>
                  </a-list-item-meta>
                </a-list-item>
              </template>
            </a-list>
          </a-card>
        </div>

        <!-- 右侧：当前题目的所有学生答案（横向卡片） -->
        <div class="answer-area">
          <div v-if="currentQuestion" class="question-header">
            <h3>
              第 {{ currentIndex + 1 }} 题
              <a-tag :color="getTypeColor(currentQuestion.question_type)">{{ getTypeText(currentQuestion.question_type) }}</a-tag>
              <span style="color: #999; font-weight: normal">（{{ currentQuestion.max_score }} 分）</span>
            </h3>
            <div class="question-content">
              <LatexText :content="currentQuestion.question_content" />
            </div>
            <div class="standard-answer">
              <span style="color: #52c41a">标准答案：</span>
              <LatexText :content="currentQuestion.standard_answer || '（无）'" />
            </div>

            <div class="question-actions">
              <a-button
                type="primary"
                ghost
                size="small"
                @click="adoptAllAiScoreForQuestion"
                :disabled="!currentQuestionHasAiScore"
              >
                <template #icon><CheckOutlined /></template>
                一键采用本页所有 AI 分
              </a-button>
              <a-button
                type="primary"
                size="small"
                @click="saveCurrentQuestionAndNext"
                :disabled="!canSaveCurrentQuestion"
              >
                保存并下一题
              </a-button>
            </div>
          </div>

          <!-- 学生答案横向卡片网格 -->
          <div v-if="currentQuestion" class="answer-grid">
            <div
              v-for="ans in currentQuestion.answers"
              :key="ans.answer_id"
              :class="['answer-card', {
                'needs-review': ans.needs_review,
                'confirmed': ans.teacher_confirmed,
                'failed': ans.ai_status === 'failed',
              }]"
            >
              <div class="card-header">
                <a-avatar size="small" style="background-color: #1890ff">{{ ans.student_name?.charAt(0) }}</a-avatar>
                <span class="student-name">{{ ans.student_name }}</span>
                <a-tag v-if="ans.teacher_confirmed" color="green" size="small">已确认</a-tag>
                <a-tag v-else-if="ans.ai_status === 'graded'" color="blue" size="small">待审核</a-tag>
                <a-tag v-else-if="ans.ai_status === 'processing'" color="orange" size="small">批改中</a-tag>
                <a-tag v-else-if="ans.ai_status === 'pending'" color="default" size="small">等待中</a-tag>
                <a-tag v-else-if="ans.ai_status === 'failed'" color="red" size="small">失败</a-tag>
                <a-tag v-if="ans.needs_review" color="red" size="small">需重点审核</a-tag>
              </div>

              <!-- 学生答案文本 -->
              <div v-if="ans.content" class="student-answer">
                <span style="color: #999; font-size: 12px">学生答案：</span>
                <div style="white-space: pre-wrap; padding: 6px; background: #fafafa; border-radius: 4px; margin-top: 4px; max-height: 150px; overflow-y: auto">
                  {{ ans.content }}
                </div>
              </div>

              <!-- 学生答案图片 -->
              <div v-if="ans.image_urls && ans.image_urls.length" class="student-images">
                <span style="color: #999; font-size: 12px">图片答案：</span>
                <a-image-preview-group style="margin-top: 4px">
                  <a-image
                    v-for="(url, idx) in ans.image_urls"
                    :key="idx"
                    :src="url"
                    :width="80"
                    :height="60"
                    style="border-radius: 4px; object-fit: cover; margin-right: 4px"
                  />
                </a-image-preview-group>
              </div>

              <!-- OCR 文本（可折叠） -->
              <a-collapse v-if="ans.ocr_text" :bordered="false" size="small" style="margin-top: 8px">
                <a-collapse-panel key="ocr" header="OCR 识别文本">
                  <div style="white-space: pre-wrap; font-size: 12px; max-height: 120px; overflow-y: auto">
                    {{ ans.ocr_text }}
                  </div>
                  <div v-if="ans.ocr_confidence" style="color: #999; margin-top: 4px">
                    OCR 置信度: {{ (ans.ocr_confidence * 100).toFixed(1) }}%
                  </div>
                </a-collapse-panel>
              </a-collapse>

              <!-- AI 批改结果 -->
              <div v-if="ans.ai_status === 'graded'" class="ai-result">
                <div class="ai-score-row">
                  <a-tag color="blue">AI 建议</a-tag>
                  <strong :style="{ color: ans.needs_review ? '#ff4d4f' : '#52c41a' }">
                    {{ ans.ai_score }}
                  </strong>
                  <span style="color: #999">/ {{ currentQuestion.max_score }} 分</span>
                  <ConfidenceBadge :confidence="ans.ai_confidence || 0.85" />
                  <a-tag v-if="ans.ai_model_key" color="cyan" size="small">{{ ans.ai_model_key }}</a-tag>
                </div>
                <div v-if="ans.ai_comment" class="ai-comment">
                  <span style="color: #999; font-size: 12px">AI 评语：</span>
                  <div style="padding: 6px; background: #f6f8fa; border-radius: 4px; margin-top: 4px; font-size: 12px; max-height: 100px; overflow-y: auto">
                    {{ ans.ai_comment }}
                  </div>
                </div>
                <!-- 评分细则 -->
                <a-collapse v-if="ans.ai_grading?.steps?.length" :bordered="false" size="small" style="margin-top: 8px">
                  <a-collapse-panel key="rubric" header="查看评分细则">
                    <div v-for="(step, idx) in ans.ai_grading.steps" :key="idx" style="font-size: 12px; margin-bottom: 4px; padding: 4px; background: #fafafa; border-radius: 2px">
                      <a-tag :color="step.correct ? 'green' : 'red'" size="small">{{ step.correct ? '✓' : '✗' }}</a-tag>
                      <span>{{ step.content }}</span>
                      <span style="float: right">{{ step.score }} 分</span>
                    </div>
                  </a-collapse-panel>
                </a-collapse>
              </div>

              <!-- 失败提示 -->
              <div v-else-if="ans.ai_status === 'failed'" class="ai-failed">
                <a-alert type="error" :message="`AI 批改失败：${ans.ai_error || '未知错误'}`" banner style="margin-top: 8px" />
              </div>

              <!-- 教师评分区 -->
              <div class="teacher-grade-area">
                <a-form layout="inline" size="small">
                  <a-form-item label="给分">
                    <a-input-number
                      v-model:value="teacherScores[ans.answer_id]"
                      :min="0"
                      :max="currentQuestion.max_score"
                      :step="0.5"
                      style="width: 80px"
                      :disabled="ans.teacher_confirmed"
                    />
                  </a-form-item>
                  <a-form-item>
                    <a-button
                      size="small"
                      type="link"
                      @click="adoptAiScore(ans)"
                      :disabled="ans.teacher_confirmed || ans.ai_score == null"
                    >
                      采用 AI 分
                    </a-button>
                  </a-form-item>
                  <a-form-item v-if="!ans.teacher_confirmed">
                    <a-button
                      size="small"
                      type="primary"
                      @click="confirmSingle(ans)"
                      :loading="confirmingIds[ans.answer_id]"
                    >
                      确认
                    </a-button>
                  </a-form-item>
                  <a-form-item v-else>
                    <a-button size="small" type="link" danger @click="unconfirmSingle(ans)">
                      撤销确认
                    </a-button>
                  </a-form-item>
                </a-form>
                <a-textarea
                  v-model:value="teacherComments[ans.answer_id]"
                  placeholder="教师评语（可选）"
                  :rows="1"
                  size="small"
                  style="margin-top: 4px"
                  :disabled="ans.teacher_confirmed"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 空状态 -->
      <a-empty v-else-if="!loading" description="暂无审核数据" style="padding: 60px">
        <template #image>
          <a-icon component="{{null}}" />
        </template>
      </a-empty>
    </a-spin>

    <!-- ═══ 统计仪表盘抽屉 ═══ -->
    <a-drawer
      v-model:open="showStatsDrawer"
      title="📊 审核统计仪表盘"
      :width="640"
      :destroyOnClose="true"
    >
      <a-spin :spinning="statsLoading">
        <template v-if="statsData">
          <!-- 整体进度 -->
          <a-card title="整体进度" size="small" style="margin-bottom: 16px">
            <a-row :gutter="16">
              <a-col :span="8">
                <a-statistic title="主观题答案" :value="statsData.total_subjective_answers" />
              </a-col>
              <a-col :span="8">
                <a-statistic title="已确认" :value="statsData.confirmed_answers" :value-style="{ color: '#52c41a' }" />
              </a-col>
              <a-col :span="8">
                <a-statistic title="需重点审核" :value="statsData.needs_review_count" :value-style="{ color: '#ff4d4f' }" />
              </a-col>
            </a-row>
            <a-progress
              :percent="statsData.confirm_progress_pct"
              :status="statsData.confirm_progress_pct >= 99.9 ? 'success' : 'active'"
              style="margin-top: 12px"
            />
          </a-card>

          <!-- AI vs 教师评分对比 -->
          <a-card title="AI 与教师评分对比" size="small" style="margin-bottom: 16px">
            <a-row :gutter="16">
              <a-col :span="8">
                <a-statistic title="AI 平均分" :value="statsData.ai_avg_score" :precision="1" />
              </a-col>
              <a-col :span="8">
                <a-statistic
                  title="教师平均分"
                  :value="statsData.teacher_avg_score"
                  :precision="1"
                  :value-style="{ color: '#52c41a' }"
                />
              </a-col>
              <a-col :span="8">
                <a-statistic
                  title="平均偏差"
                  :value="statsData.avg_deviation"
                  :precision="2"
                  :value-style="statsData.avg_deviation != null && Math.abs(statsData.avg_deviation) > 2 ? { color: '#ff4d4f' } : {}"
                />
              </a-col>
            </a-row>
          </a-card>

          <!-- 置信度分布 -->
          <a-card title="AI 置信度分布" size="small" style="margin-bottom: 16px">
            <template v-if="statsData.confidence_dist">
              <a-row :gutter="16">
                <a-col :span="8">
                  <a-statistic title="高 (≥85%)" :value="statsData.confidence_dist.high" :value-style="{ color: '#52c41a' }" />
                </a-col>
                <a-col :span="8">
                  <a-statistic title="中 (60-85%)" :value="statsData.confidence_dist.medium" :value-style="{ color: '#fa8c16' }" />
                </a-col>
                <a-col :span="8">
                  <a-statistic title="低 (<60%)" :value="statsData.confidence_dist.low" :value-style="{ color: '#ff4d4f' }" />
                </a-col>
              </a-row>
              <!-- 可视化条 -->
              <div style="display: flex; height: 20px; border-radius: 4px; overflow: hidden; margin-top: 12px">
                <div
                  v-if="statsData.confidence_dist.high"
                  :style="{ flex: statsData.confidence_dist.high, background: '#52c41a' }"
                  :title="`高置信度 ${statsData.confidence_dist.high}`"
                />
                <div
                  v-if="statsData.confidence_dist.medium"
                  :style="{ flex: statsData.confidence_dist.medium, background: '#fa8c16' }"
                  :title="`中置信度 ${statsData.confidence_dist.medium}`"
                />
                <div
                  v-if="statsData.confidence_dist.low"
                  :style="{ flex: statsData.confidence_dist.low, background: '#ff4d4f' }"
                  :title="`低置信度 ${statsData.confidence_dist.low}`"
                />
              </div>
            </template>
            <a-empty v-else description="暂无数据" image="simple" style="padding: 12px" />
          </a-card>

          <!-- 教师修正分布 -->
          <a-card title="教师修正分布" size="small" style="margin-bottom: 16px">
            <template v-if="statsData.deviation_dist">
              <a-row :gutter="16">
                <a-col :span="8">
                  <a-statistic title="无修正 (<0.5)" :value="statsData.deviation_dist.no_change" />
                </a-col>
                <a-col :span="8">
                  <a-statistic title="微调 (0.5-3)" :value="statsData.deviation_dist.minor" :value-style="{ color: '#fa8c16' }" />
                </a-col>
                <a-col :span="8">
                  <a-statistic title="大幅修正 (>3)" :value="statsData.deviation_dist.major" :value-style="{ color: '#ff4d4f' }" />
                </a-col>
              </a-row>
              <div style="display: flex; height: 20px; border-radius: 4px; overflow: hidden; margin-top: 12px">
                <div
                  v-if="statsData.deviation_dist.no_change"
                  :style="{ flex: statsData.deviation_dist.no_change, background: '#52c41a' }"
                />
                <div
                  v-if="statsData.deviation_dist.minor"
                  :style="{ flex: statsData.deviation_dist.minor, background: '#fa8c16' }"
                />
                <div
                  v-if="statsData.deviation_dist.major"
                  :style="{ flex: statsData.deviation_dist.major, background: '#ff4d4f' }"
                />
              </div>
            </template>
            <a-empty v-else description="暂无数据" image="simple" style="padding: 12px" />
          </a-card>

          <!-- 各题统计 -->
          <a-card title="各题维度统计" size="small">
            <a-table
              v-if="statsData.question_stats && statsData.question_stats.length"
              :data-source="statsData.question_stats"
              :columns="questionStatsColumns"
              row-key="question_id"
              size="small"
              :pagination="false"
            >
              <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'question_id'">
                  第 {{ statsData.question_stats.findIndex(q => q.question_id === record.question_id) + 1 }} 题
                </template>
                <template v-else-if="column.key === 'ai_avg'">
                  <span style="color: #1890ff">{{ record.ai_avg ?? '-' }}</span>
                </template>
                <template v-else-if="column.key === 'teacher_avg'">
                  <span style="color: #52c41a">{{ record.teacher_avg ?? '-' }}</span>
                </template>
                <template v-else-if="column.key === 'deviation_avg'">
                  <span :style="{ color: record.deviation_avg != null && Math.abs(record.deviation_avg) > 2 ? '#ff4d4f' : '#666' }">
                    {{ record.deviation_avg ?? '-' }}
                  </span>
                </template>
                <template v-else-if="column.key === 'needs_review'">
                  <a-tag v-if="record.needs_review > 0" color="red">{{ record.needs_review }}</a-tag>
                  <span v-else>0</span>
                </template>
              </template>
            </a-table>
            <a-empty v-else description="暂无题目统计" image="simple" style="padding: 12px" />
          </a-card>
        </template>
      </a-spin>
    </a-drawer>

    <!-- ═══ 批量确认弹窗 ═══ -->
    <a-modal
      v-model:open="showBatchModal"
      title="🔧 批量确认"
      :confirm-loading="batchLoading"
      @ok="handleBatchConfirm"
      ok-text="确认执行"
      cancel-text="取消"
      :width="520"
    >
      <a-form layout="vertical">
        <a-form-item label="筛选模式">
          <a-radio-group v-model:value="batchForm.mode">
            <a-radio-button value="question">按题目</a-radio-button>
            <a-radio-button value="submission">按提交</a-radio-button>
            <a-radio-button value="status">按状态</a-radio-button>
          </a-radio-group>
        </a-form-item>

        <a-form-item v-if="batchForm.mode === 'question'" label="选择题目">
          <a-select
            v-model:value="batchForm.question_id"
            placeholder="选择要确认的题目"
            allow-clear
            style="width: 100%"
          >
            <a-select-option
              v-for="(q, idx) in reviewData?.questions || []"
              :key="q.question_id"
              :value="q.question_id"
            >
              第 {{ idx + 1 }} 题 ({{ getTypeText(q.question_type) }}，{{ q.answers.length }} 人作答)
            </a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item v-if="batchForm.mode === 'submission'" label="选择学生提交">
          <a-select
            v-model:value="batchForm.submission_id"
            placeholder="选择要确认的学生"
            allow-clear
            show-search
            :filter-option="filterSubmissionOption"
            style="width: 100%"
          >
            <a-select-option
              v-for="sub in allSubmissions"
              :key="sub.submission_id"
              :value="sub.submission_id"
            >
              {{ sub.student_name }}（提交 #{{ sub.submission_id }}）
            </a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item v-if="batchForm.mode === 'status'" label="状态筛选">
          <a-select v-model:value="batchForm.status_filter" style="width: 100%">
            <a-select-option value="needs_review">仅需重点审核</a-select-option>
            <a-select-option value="unconfirmed">所有未确认</a-select-option>
            <a-select-option value="all">全部（含已确认）</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item label="评分策略">
          <a-radio-group v-model:value="batchForm.adopt_ai_score">
            <a-radio :value="true">采用 AI 分数</a-radio>
            <a-radio :value="false">自定义分数</a-radio>
          </a-radio-group>
        </a-form-item>
      </a-form>

      <a-alert
        v-if="batchForm.adopt_ai_score"
        type="info"
        show-icon
        message="将采用 AI 建议分数作为最终成绩，无 AI 分的答案会被跳过"
        style="margin-top: 8px"
      />
    </a-modal>
  </div>
</template>

<script setup>
import {
  ReloadOutlined,
  CheckOutlined,
  ExportOutlined,
  BarChartOutlined,
  TeamOutlined,
} from '@ant-design/icons-vue'
import LatexText from '@/components/LatexText.vue'
import { useExamReview } from '@/composables/useExamReview'

const {
  // 核心数据
  examId,
  reviewData, loading, submitting, regrading,
  currentQuestionId, confirmingIds,
  teacherScores, teacherComments,
  // 计算属性
  currentQuestion, currentIndex, reviewProgressPct,
  hasAiGradingSubmissions, currentQuestionHasAiScore,
  canSaveCurrentQuestion, canSubmitAll, allSubmissions,
  // 数据加载
  refreshData,
  // UI 辅助
  selectQuestion, getTypeText, getTypeColor,
  getQuestionConfirmedCount, getQuestionPendingCount,
  adoptAiScore, adoptAllAiScoreForQuestion,
  // 确认 / 保存 / 提交
  confirmSingle, unconfirmSingle, saveCurrentQuestionAndNext,
  submitAllReview, regradeAllPending,
  // 导出报告
  exporting, handleExportReport,
  // 统计仪表盘
  showStatsDrawer, statsLoading, statsData,
  questionStatsColumns,
  // 批量确认
  showBatchModal, batchLoading, batchForm,
  filterSubmissionOption, handleBatchConfirm,
} = useExamReview()

// 置信度 Badge 子组件
const ConfidenceBadge = {
  props: ['confidence'],
  template: `
    <a-tag :color="badgeColor" size="small">
      置信度 {{ (confidence * 100).toFixed(0) }}%
    </a-tag>
  `,
  computed: {
    badgeColor() {
      if (this.confidence >= 0.9) return 'green'
      if (this.confidence >= 0.7) return 'blue'
      if (this.confidence >= 0.5) return 'orange'
      return 'red'
    },
  },
}
</script>

<style scoped>
.exam-review-page {
  min-height: 100vh;
  background: #f0f2f5;
}

.review-body {
  display: flex;
  gap: 16px;
  padding: 0 24px 24px;
}

.question-sidebar {
  width: 280px;
  flex-shrink: 0;
}

.question-item {
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 4px;
  transition: all 0.2s;
}

.question-item:hover {
  background: #f0f9ff;
}

.question-item.active {
  background: #e6f7ff;
  border-left: 3px solid #1890ff;
}

.answer-area {
  flex: 1;
  min-width: 0;
}

.question-header {
  background: #fff;
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 16px;
  border-left: 4px solid #1890ff;
}

.question-content {
  margin: 8px 0;
  padding: 8px;
  background: #fafafa;
  border-radius: 4px;
  font-size: 14px;
}

.standard-answer {
  margin-top: 8px;
  font-size: 13px;
  padding: 6px;
  background: #f6ffed;
  border-radius: 4px;
  border: 1px solid #b7eb8f;
}

.question-actions {
  margin-top: 12px;
  display: flex;
  gap: 8px;
}

.answer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 16px;
}

.answer-card {
  background: #fff;
  border-radius: 8px;
  padding: 12px;
  border: 1px solid #e8e8e8;
  transition: all 0.2s;
}

.answer-card.needs-review {
  border-color: #ff4d4f;
  box-shadow: 0 0 0 2px rgba(255, 77, 79, 0.1);
}

.answer-card.confirmed {
  border-color: #52c41a;
  background: #f6ffed;
}

.answer-card.failed {
  border-color: #ff4d4f;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}

.student-name {
  font-weight: 500;
  margin-right: auto;
}

.student-answer,
.student-images {
  margin-top: 8px;
}

.ai-result {
  margin-top: 10px;
  padding: 8px;
  background: #f0f9ff;
  border-radius: 4px;
  border: 1px solid #d6e4ff;
}

.ai-score-row {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.ai-comment {
  margin-top: 6px;
}

.ai-failed {
  margin-top: 8px;
}

.teacher-grade-area {
  margin-top: 10px;
  padding: 8px;
  background: #fafafa;
  border-radius: 4px;
  border: 1px dashed #d9d9d9;
}
</style>
