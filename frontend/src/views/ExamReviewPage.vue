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
import { ref, reactive, computed, watch, onMounted, onUnmounted } from 'vue'
import { message, Modal } from 'ant-design-vue'
import { useRoute, useRouter } from 'vue-router'
import {
  ReloadOutlined,
  CheckOutlined,
  ExportOutlined,
  BarChartOutlined,
  TeamOutlined,
} from '@ant-design/icons-vue'
import {
  getExamReviewData,
  confirmAnswer,
  submitExamReview,
  regradeSubmission,
  exportReviewReport,
  getReviewStats,
  batchConfirmReview,
} from '@/api/exam'
import LatexText from '@/components/LatexText.vue'

const route = useRoute()
const router = useRouter()
const examId = route.params.id

const reviewData = ref(null)
const loading = ref(false)
const submitting = ref(false)
const regrading = ref(false)
const currentQuestionId = ref(null)
const confirmingIds = reactive({})  // answer_id -> loading

// 教师评分输入
const teacherScores = reactive({})  // answer_id -> score
const teacherComments = reactive({})  // answer_id -> comment

let pollTimer = null

// === 计算属性 ===
const currentQuestion = computed(() => {
  if (!reviewData.value || !currentQuestionId.value) return null
  return reviewData.value.questions.find(q => q.question_id === currentQuestionId.value)
})

const currentIndex = computed(() => {
  if (!reviewData.value || !currentQuestionId.value) return -1
  return reviewData.value.questions.findIndex(q => q.question_id === currentQuestionId.value)
})

const reviewProgressPct = computed(() => {
  if (!reviewData.value) return 0
  const { confirmed, total } = reviewData.value.review_progress
  return total > 0 ? Math.round((confirmed / total) * 100) : 0
})

const hasAiGradingSubmissions = computed(() => {
  if (!reviewData.value) return false
  // 检查是否有 ai_status 为 pending/processing/failed 的答案
  return reviewData.value.questions.some(q =>
    q.answers.some(a => ['pending', 'processing', 'failed'].includes(a.ai_status) && !a.teacher_confirmed)
  )
})

const currentQuestionHasAiScore = computed(() => {
  if (!currentQuestion.value) return false
  return currentQuestion.value.answers.some(a => a.ai_score != null && !a.teacher_confirmed)
})

const canSaveCurrentQuestion = computed(() => {
  if (!currentQuestion.value) return false
  return currentQuestion.value.answers.some(a =>
    teacherScores[a.answer_id] != null && !a.teacher_confirmed
  )
})

const canSubmitAll = computed(() => {
  if (!reviewData.value) return false
  return reviewData.value.questions.some(q =>
    q.answers.some(a => !a.teacher_confirmed && teacherScores[a.answer_id] != null)
  )
})

// === 方法 ===
async function fetchReviewData() {
  loading.value = true
  try {
    const res = await getExamReviewData(examId)
    reviewData.value = res.data
    // 默认选第一题
    if (res.data.questions.length && !currentQuestionId.value) {
      currentQuestionId.value = res.data.questions[0].question_id
    }
    // 初始化教师评分输入
    for (const q of res.data.questions) {
      for (const a of q.answers) {
        if (teacherScores[a.answer_id] == null) {
          // 已确认的用 teacher_score，未确认的预填 ai_score
          teacherScores[a.answer_id] = a.teacher_confirmed
            ? a.teacher_score
            : (a.ai_score ?? null)
        }
        if (teacherComments[a.answer_id] == null) {
          teacherComments[a.answer_id] = a.teacher_comment || ''
        }
      }
    }
    // 若有 AI 批改中的题，启动轮询
    maybeStartPolling()
  } catch (e) {
    const msg = e?.response?.data?.detail || '获取审核数据失败'
    message.error(msg)
  } finally {
    loading.value = false
  }
}

function maybeStartPolling() {
  if (!reviewData.value) return
  const hasProcessing = reviewData.value.questions.some(q =>
    q.answers.some(a => a.ai_status === 'pending' || a.ai_status === 'processing')
  )
  if (hasProcessing && !pollTimer) {
    pollTimer = setTimeout(async () => {
      pollTimer = null
      await fetchReviewData()
    }, 3000)
  }
}

function refreshData() {
  fetchReviewData()
}

function selectQuestion(qid) {
  currentQuestionId.value = qid
}

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

function getTypeColor(type) {
  return { essay: 'orange', fill: 'blue' }[type] || 'default'
}

function getQuestionConfirmedCount(q) {
  return q.answers.filter(a => a.teacher_confirmed).length
}

function getQuestionPendingCount(q) {
  return q.answers.filter(a => !a.teacher_confirmed).length
}

function adoptAiScore(ans) {
  if (ans.ai_score == null) {
    message.warning('AI 分数不存在')
    return
  }
  teacherScores[ans.answer_id] = ans.ai_score
}

function adoptAllAiScoreForQuestion() {
  if (!currentQuestion.value) return
  let count = 0
  for (const a of currentQuestion.value.answers) {
    if (!a.teacher_confirmed && a.ai_score != null) {
      teacherScores[a.answer_id] = a.ai_score
      count++
    }
  }
  if (count > 0) {
    message.success(`已采用 ${count} 个 AI 分数，请点击"确认"或"提交全部审核"`)
  } else {
    message.info('没有可采用的 AI 分数')
  }
}

async function confirmSingle(ans) {
  const score = teacherScores[ans.answer_id]
  if (score == null) {
    message.warning('请先填入分数')
    return
  }
  confirmingIds[ans.answer_id] = true
  try {
    await confirmAnswer(ans.submission_id, ans.answer_id, {
      teacher_score: score,
      teacher_comment: teacherComments[ans.answer_id] || null,
      adopt_ai_score: false,
    })
    message.success(`已确认 ${ans.student_name} 的答案`)
    await fetchReviewData()
  } catch (e) {
    const msg = e?.response?.data?.detail || '确认失败'
    message.error(msg)
  } finally {
    confirmingIds[ans.answer_id] = false
  }
}

async function unconfirmSingle(ans) {
  // 通过设置为 false 实现"撤销确认"——前端标记，最终提交时按当前 teacher_score 重新写
  // 简化处理：仅在前端标记为未确认，下次保存时再次确认即可
  // 实际后端没有"撤销确认"接口，这里通过刷新数据恢复
  Modal.confirm({
    title: '撤销确认？',
    content: '撤销后需要重新确认。是否继续？',
    onOk: async () => {
      // 这里简化：仅刷新数据，已确认的题仍保持已确认状态
      // 真正的撤销需要后端支持
      message.info('请通过"重新 AI 批改"或后端操作撤销')
    },
  })
}

async function saveCurrentQuestionAndNext() {
  if (!currentQuestion.value) return
  // 收集当前题目所有未确认的答案
  const items = []
  for (const a of currentQuestion.value.answers) {
    if (!a.teacher_confirmed && teacherScores[a.answer_id] != null) {
      items.push({
        answer_id: a.answer_id,
        teacher_score: teacherScores[a.answer_id],
        teacher_comment: teacherComments[a.answer_id] || null,
      })
    }
  }
  if (!items.length) {
    message.warning('没有可保存的评分')
    return
  }
  submitting.value = true
  try {
    await submitExamReview(examId, items)
    message.success(`已保存 ${items.length} 个评分`)
    await fetchReviewData()
    // 自动跳到下一题
    const nextIdx = currentIndex.value + 1
    if (nextIdx < reviewData.value.questions.length) {
      currentQuestionId.value = reviewData.value.questions[nextIdx].question_id
    }
  } catch (e) {
    const msg = e?.response?.data?.detail || '保存失败'
    message.error(msg)
  } finally {
    submitting.value = false
  }
}

async function submitAllReview() {
  if (!reviewData.value) return
  // 收集所有未确认的答案
  const items = []
  for (const q of reviewData.value.questions) {
    for (const a of q.answers) {
      if (!a.teacher_confirmed && teacherScores[a.answer_id] != null) {
        items.push({
          answer_id: a.answer_id,
          teacher_score: teacherScores[a.answer_id],
          teacher_comment: teacherComments[a.answer_id] || null,
        })
      }
    }
  }
  if (!items.length) {
    message.warning('没有可提交的评分')
    return
  }
  Modal.confirm({
    title: '提交全部审核？',
    content: `将提交 ${items.length} 个评分，提交后对应提交将锁定为"已批改"状态。`,
    okText: '确定提交',
    cancelText: '取消',
    onOk: async () => {
      submitting.value = true
      try {
        await submitExamReview(examId, items)
        message.success(`已提交 ${items.length} 个评分`)
        await fetchReviewData()
      } catch (e) {
        const msg = e?.response?.data?.detail || '提交失败'
        message.error(msg)
      } finally {
        submitting.value = false
      }
    },
  })
}

async function regradeAllPending() {
  // 逐个 submission 重新批改（仅未确认的）
  if (!reviewData.value) return
  regrading.value = true
  try {
    const submissionIds = new Set()
    for (const q of reviewData.value.questions) {
      for (const a of q.answers) {
        if (['pending', 'processing', 'failed'].includes(a.ai_status) && !a.teacher_confirmed) {
          submissionIds.add(a.submission_id)
        }
      }
    }
    let successCount = 0
    for (const sid of submissionIds) {
      try {
        await regradeSubmission(sid)
        successCount++
      } catch (e) {
        // 忽略单个失败
      }
    }
    message.success(`已对 ${successCount} 个提交触发重新批改`)
    // 启动轮询
    setTimeout(() => fetchReviewData(), 2000)
  } finally {
    regrading.value = false
  }
}

// ═══ 扩展功能：导出审核报告 ═══
const exporting = ref(false)

async function handleExportReport() {
  exporting.value = true
  try {
    const res = await exportReviewReport(examId)
    // 创建 Blob 并触发下载
    const blob = new Blob([res.data], { type: 'text/html' })
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `review_report_${examId}.html`
    link.click()
    window.URL.revokeObjectURL(url)
    message.success('报告已导出')
  } catch (e) {
    const msg = e?.response?.data?.detail || '导出失败'
    message.error(msg)
  } finally {
    exporting.value = false
  }
}

// ═══ 扩展功能：审核统计仪表盘 ═══
const showStatsDrawer = ref(false)
const statsLoading = ref(false)
const statsData = ref(null)

// 题目统计表格列配置
const questionStatsColumns = [
  { key: 'question_id', title: '题目', dataIndex: 'question_id', width: 70 },
  { key: 'confirmed', title: '已确认', dataIndex: 'confirmed', width: 70 },
  { key: 'ai_avg', title: 'AI 均分', dataIndex: 'ai_avg', width: 80 },
  { key: 'teacher_avg', title: '教师均分', dataIndex: 'teacher_avg', width: 80 },
  { key: 'deviation_avg', title: '偏差', dataIndex: 'deviation_avg', width: 70 },
  { key: 'needs_review', title: '需审核', dataIndex: 'needs_review', width: 70 },
]

// 监听抽屉打开时自动加载数据
watch(showStatsDrawer, async (val) => {
  if (val && !statsData.value) {
    await fetchStatsData()
  }
})

async function fetchStatsData() {
  statsLoading.value = true
  try {
    const res = await getReviewStats(examId)
    statsData.value = res.data
  } catch (e) {
    const msg = e?.response?.data?.detail || '获取统计数据失败'
    message.error(msg)
  } finally {
    statsLoading.value = false
  }
}

// ═══ 扩展功能：批量确认增强 ═══
const showBatchModal = ref(false)
const batchLoading = ref(false)
const batchForm = reactive({
  mode: 'question',
  question_id: null,
  submission_id: null,
  status_filter: 'needs_review',
  adopt_ai_score: true,
})

// 所有提交列表（去重）
const allSubmissions = computed(() => {
  if (!reviewData.value) return []
  const seen = new Map()
  for (const q of reviewData.value.questions) {
    for (const a of q.answers) {
      if (!seen.has(a.submission_id)) {
        seen.set(a.submission_id, {
          submission_id: a.submission_id,
          student_name: a.student_name,
        })
      }
    }
  }
  return Array.from(seen.values())
})

function filterSubmissionOption(input, option) {
  return option.children?.[0]?.children?.toLowerCase().includes(input.toLowerCase())
}

async function handleBatchConfirm() {
  // 校验
  if (batchForm.mode === 'question' && !batchForm.question_id) {
    message.warning('请选择题目')
    return
  }
  if (batchForm.mode === 'submission' && !batchForm.submission_id) {
    message.warning('请选择学生提交')
    return
  }
  if (batchForm.mode === 'status' && !batchForm.status_filter) {
    message.warning('请选择状态筛选条件')
    return
  }

  batchLoading.value = true
  try {
    const payload = {
      mode: batchForm.mode,
      adopt_ai_score: batchForm.adopt_ai_score,
    }
    if (batchForm.mode === 'question') {
      payload.question_id = batchForm.question_id
    } else if (batchForm.mode === 'submission') {
      payload.submission_id = batchForm.submission_id
    } else if (batchForm.mode === 'status') {
      payload.status_filter = batchForm.status_filter
    }

    const res = await batchConfirmReview(examId, payload)
    message.success(`已确认 ${res.data.confirmed_count} 个答案（影响 ${res.data.affected_submissions} 个提交）`)
    showBatchModal.value = false
    // 刷新数据
    await fetchReviewData()
  } catch (e) {
    const msg = e?.response?.data?.detail || '批量确认失败'
    message.error(msg)
  } finally {
    batchLoading.value = false
  }
}

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

onMounted(fetchReviewData)

onUnmounted(() => {
  if (pollTimer) clearTimeout(pollTimer)
})
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
