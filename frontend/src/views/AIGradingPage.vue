<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="AI数学批改"
      sub-title="智能识别·过程评分·错因归因"
      style="padding: 0 0 16px 0"
    />

    <a-row :gutter="24">
      <!-- 左列：批改设置 -->
      <a-col :span="10">
        <GradingSetupPanel
          :form="form"
          :input-data="inputData"
          question-label="题目"
          question-placeholder="输入数学题目..."
          standard-answer-label="标准答案"
          standard-answer-placeholder="输入标准答案（可选）..."
          :total-score-editable="true"
          :loading="gradingStore.isGrading"
          @grade="handleGrade"
        />
      </a-col>

      <!-- 右列：批改结果 -->
      <a-col :span="14">
        <!-- 无结果占位 -->
        <a-card v-if="!gradingStore.gradingResult && !gradingStore.isGrading" :bordered="false" class="result-card result-empty">
          <a-empty description="提交题目与学生作答后，点击「开始批改」" />
        </a-card>

        <!-- 批改中 / 结果展示 -->
        <div v-else class="result-steps">
          <!-- 步骤 0：识别 -->
          <GradingStepReveal
            :step-index="0"
            :current-step-index="gradingStore.currentStepIndex"
            title="识别"
          >
            <div class="step-ocr-content">
              <template v-if="gradingStore.gradingResult">
                <a-typography-paragraph
                  v-if="ocrText"
                  class="cv-line-appear"
                  style="font-size: 15px; white-space: pre-wrap"
                >
                  {{ ocrText }}
                </a-typography-paragraph>
                <a-empty v-else description="未识别到文本内容" :image="simpleImage" />
              </template>
            </div>
          </GradingStepReveal>

          <!-- 步骤 1：判断 -->
          <GradingStepReveal
            :step-index="1"
            :current-step-index="gradingStore.currentStepIndex"
            title="判断"
          >
            <ErrorCauseTag
              v-if="gradingStore.gradingResult"
              :error-type="gradingStore.gradingResult.grading?.error_type || ''"
              :error-cause="gradingStore.gradingResult.grading?.error_cause || ''"
              :knowledge-points="gradingStore.gradingResult.grading?.knowledge_points || []"
            />
          </GradingStepReveal>

          <!-- 步骤 2：量规 -->
          <GradingStepReveal
            :step-index="2"
            :current-step-index="gradingStore.currentStepIndex"
            title="量规"
          >
            <RubricTable
              v-if="gradingStore.gradingResult"
              :rubric-steps="gradingStore.gradingResult.rubric?.steps || []"
              :grading-steps="gradingStore.gradingResult.grading?.steps || []"
            />
          </GradingStepReveal>

          <!-- 步骤 3：评分 -->
          <GradingStepReveal
            :step-index="3"
            :current-step-index="gradingStore.currentStepIndex"
            title="评分"
          >
            <div v-if="gradingStore.gradingResult" class="score-section">
              <div class="score-row">
                <ScoreCounter
                  :target-score="gradingStore.gradingResult.suggested_score"
                  :max-score="gradingStore.gradingResult.max_score"
                />
                <ConfidenceBadge :confidence="gradingStore.gradingResult.confidence ?? 0.85" />
              </div>

              <a-typography-paragraph
                v-if="gradingStore.gradingResult.comment"
                class="cv-line-appear comment-text"
                style="animation-delay: 200ms"
              >
                {{ gradingStore.gradingResult.comment }}
              </a-typography-paragraph>

              <!-- 操作按钮 -->
              <div class="action-row cv-line-appear" style="animation-delay: 400ms">
                <a-space>
                  <a-button
                    type="primary"
                    :loading="confirmLoading"
                    @click="handleConfirm"
                  >
                    <template #icon><CheckOutlined /></template>
                    确认评分
                  </a-button>
                  <a-button @click="showAdjust = true">
                    <template #icon><EditOutlined /></template>
                    调整分数
                  </a-button>
                </a-space>

                <div v-if="showAdjust" class="adjust-input" style="margin-top: 12px">
                  <a-space>
                    <a-input-number
                      v-model:value="adjustedScore"
                      :min="0"
                      :max="gradingStore.gradingResult.max_score"
                      :step="0.5"
                      style="width: 120px"
                    />
                    <a-button
                      type="primary"
                      size="small"
                      :loading="confirmLoading"
                      @click="handleAdjust"
                    >
                      提交调整
                    </a-button>
                    <a-button size="small" @click="showAdjust = false">取消</a-button>
                  </a-space>
                </div>
              </div>
            </div>
          </GradingStepReveal>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { Empty } from 'ant-design-vue'
import { message } from 'ant-design-vue'
import { CheckOutlined, EditOutlined } from '@ant-design/icons-vue'

import { useGradingStore } from '@/stores/grading'
import { aiGrade, confirmGrading } from '@/api/grading'

import GradingSetupPanel from '@/components/ai-grading/GradingSetupPanel.vue'
import GradingStepReveal from '@/components/ai-grading/GradingStepReveal.vue'
import ScoreCounter from '@/components/ai-grading/ScoreCounter.vue'
import ConfidenceBadge from '@/components/ai-grading/ConfidenceBadge.vue'
import RubricTable from '@/components/ai-grading/RubricTable.vue'
import ErrorCauseTag from '@/components/ai-grading/ErrorCauseTag.vue'

import '@/assets/styles/ai-grading-animations.css'

const simpleImage = Empty.PRESENTED_IMAGE_SIMPLE

const gradingStore = useGradingStore()

// ---------- 表单状态 ----------
const form = reactive({
  question: '',
  standardAnswer: '',
  totalScore: 10,
  submissionId: null,
})

const inputData = ref({
  imageBase64: '',
  textContent: '',
})

// ---------- 操作状态 ----------
const confirmLoading = ref(false)
const showAdjust = ref(false)
const adjustedScore = ref(null)

// ---------- 计算属性 ----------
const ocrText = computed(() => {
  const result = gradingStore.gradingResult
  if (!result) return ''
  // 优先展示 grading.steps 拼接的识别文本，其次展示 student_answer 字段
  if (result.grading?.steps?.length) {
    return result.grading.steps.map((s) => s.text || s.description || '').filter(Boolean).join('\n')
  }
  return result.student_answer || inputData.value.textContent || ''
})

const resultId = computed(() => gradingStore.gradingResult?.result_id ?? gradingStore.gradingResult?.id ?? null)

// ---------- 核心逻辑 ----------
async function handleGrade() {
  // 校验
  if (!form.question.trim()) {
    message.warning('请输入题目内容')
    return
  }
  if (!inputData.value.imageBase64 && !inputData.value.textContent.trim()) {
    message.warning('请上传学生手写图片或粘贴答案文本')
    return
  }

  gradingStore.startGrading()

  try {
    const data = {
      submission_id: form.submissionId || null,
      question: form.question,
      standard_answer: form.standardAnswer,
      total_score: form.totalScore,
      subject_type: 'math',
      image_base64: undefined,
      student_text: undefined,
    }

    if (inputData.value.imageBase64) {
      data.image_base64 = inputData.value.imageBase64
    }
    // 把用户粘贴的文本答案传给后端（后端优先使用此字段作为学生答案）
    if (inputData.value.textContent.trim()) {
      data.student_text = inputData.value.textContent.trim()
    }

    const res = await aiGrade(data)
    gradingStore.setResult(res.data)

    // 重置调整状态
    showAdjust.value = false
    adjustedScore.value = res.data.suggested_score
  } catch (err) {
    gradingStore.reset()
    const errMsg = err?.response?.data?.detail || err?.message || '批改请求失败'
    message.error(errMsg)
  }
}

async function handleConfirm() {
  if (!resultId.value) {
    message.warning('无批改结果可确认')
    return
  }
  confirmLoading.value = true
  try {
    await confirmGrading(resultId.value)
    message.success('批改结果已确认')
  } catch (err) {
    const errMsg = err?.response?.data?.detail || err?.message || '确认失败'
    message.error(errMsg)
  } finally {
    confirmLoading.value = false
  }
}

async function handleAdjust() {
  if (!resultId.value) {
    message.warning('无批改结果可调整')
    return
  }
  if (adjustedScore.value === null || adjustedScore.value === undefined) {
    message.warning('请输入调整后的分数')
    return
  }
  confirmLoading.value = true
  try {
    await confirmGrading(resultId.value, adjustedScore.value)
    message.success(`分数已调整为 ${adjustedScore.value} 分`)
    showAdjust.value = false
  } catch (err) {
    const errMsg = err?.response?.data?.detail || err?.message || '调整失败'
    message.error(errMsg)
  } finally {
    confirmLoading.value = false
  }
}
</script>

<style scoped>
.settings-card,
.result-card {
  border-radius: 12px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
}

.result-empty {
  min-height: 360px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-steps {
  /* 步骤卡片之间由 GradingStepReveal 自带 margin 控制间距 */
}

.step-ocr-content {
  padding: 4px 0;
}

.score-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.score-row {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.comment-text {
  padding: 10px 14px;
  background: #f6f8fa;
  border-radius: 8px;
  font-size: 14px;
  color: #333;
  line-height: 1.7;
  white-space: pre-wrap;
  margin: 0;
}

.action-row {
  margin-top: 4px;
}

.adjust-input {
  padding: 8px 12px;
  background: #fafafa;
  border-radius: 8px;
  border: 1px dashed #d9d9d9;
}
</style>