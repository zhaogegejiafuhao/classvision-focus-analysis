<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="AI作文批改"
      sub-title="四维评分·智能归因·精准指导"
      style="padding: 0 0 16px 0"
    />

    <a-row :gutter="24">
      <!-- 左列：批改设置 -->
      <a-col :span="10">
        <a-card title="批改设置" :bordered="false" class="settings-card">
          <a-form layout="vertical">
            <a-form-item label="作文题目" required>
              <a-textarea
                v-model:value="form.question"
                :rows="3"
                placeholder="输入作文题目..."
                show-count
                :maxlength="2000"
              />
            </a-form-item>

            <a-form-item label="写作要求">
              <a-textarea
                v-model:value="form.standardAnswer"
                :rows="2"
                placeholder="输入写作要求（可选）..."
                show-count
                :maxlength="1000"
              />
            </a-form-item>

            <a-row :gutter="16">
              <a-col :span="12">
                <a-form-item label="满分值">
                  <a-input-number
                    :value="100"
                    disabled
                    style="width: 100%"
                  />
                </a-form-item>
              </a-col>
              <a-col :span="12">
                <a-form-item label="提交ID">
                  <a-input-number
                    v-model:value="form.submissionId"
                    :min="1"
                    style="width: 100%"
                    placeholder="学生提交ID"
                  />
                </a-form-item>
              </a-col>
            </a-row>

            <a-form-item label="学生作答">
              <DualInputPanel v-model="inputData" />
            </a-form-item>

            <a-form-item>
              <a-button
                type="primary"
                block
                size="large"
                :loading="gradingStore.isGrading"
                @click="handleGrade"
              >
                <template #icon><ThunderboltOutlined /></template>
                开始批改
              </a-button>
            </a-form-item>
          </a-form>
        </a-card>
      </a-col>

      <!-- 右列：批改结果 -->
      <a-col :span="14">
        <!-- 无结果占位 -->
        <a-card v-if="!result && !gradingStore.isGrading" :bordered="false" class="result-card result-empty">
          <a-empty description="提交作文题目与学生作答后，点击「开始批改」" />
        </a-card>

        <!-- 批改中骨架 -->
        <div v-else-if="gradingStore.isGrading && !result" class="result-steps">
          <a-card :bordered="false" class="result-card">
            <a-skeleton active :paragraph="{ rows: 6 }" :title="true" />
          </a-card>
        </div>

        <!-- 批改结果展示 -->
        <div v-else-if="result" class="result-steps">
          <!-- 总分展示 -->
          <a-card :bordered="false" size="small" style="margin-bottom: 16px; text-align: center" class="cv-dimension-reveal">
            <div style="font-size: 14px; color: #888; margin-bottom: 4px">综合得分</div>
            <ScoreCounter
              :target-score="result.suggested_score || 0"
              :max-score="result.max_score || 100"
              :duration="1500"
            />
            <a-tag v-if="result.model_key" color="blue" style="margin-top: 8px">
              模型: {{ result.model_key }}
            </a-tag>
          </a-card>

          <!-- 四维评分卡片 -->
          <a-row :gutter="16" style="margin-bottom: 16px">
            <a-col
              v-for="(dim, idx) in essayDimensions"
              :key="dim.key"
              :span="6"
            >
              <a-card
                size="small"
                :class="['cv-dimension-reveal']"
                :style="{ animationDelay: (idx + 1) * 100 + 'ms' }"
              >
                <div class="dimension-header">{{ dim.name }}（{{ dim.maxScore }}分）</div>
                <ScoreCounter
                  :target-score="dimensions[dim.key]?.score || 0"
                  :max-score="dim.maxScore"
                  :duration="1200"
                />
                <div class="dimension-comment">{{ dimensions[dim.key]?.comment || '—' }}</div>
              </a-card>
            </a-col>
          </a-row>

          <!-- 四维雷达图 -->
          <a-card title="维度雷达图" :bordered="false" size="small" style="margin-bottom: 16px">
            <div
              ref="radarChartRef"
              style="height: 300px"
              class="cv-radar-spin-in"
            />
          </a-card>

          <!-- OCR 低置信度警告 -->
          <a-alert
            v-if="result.confidence < 0.6"
            type="warning"
            show-icon
            style="margin-bottom: 16px"
            message="识别置信度较低"
            description="手写内容识别置信度低于60%，评分结果可能存在偏差，建议人工复核。"
          />

          <!-- 错因归因 -->
          <a-card title="错因归因" :bordered="false" size="small" style="margin-bottom: 16px">
            <ErrorCauseTag
              :error-cause="result.grading?.primary_error_cause || ''"
              :knowledge-points="result.grading?.knowledge_points || []"
            />
          </a-card>

          <!-- 总体评语 -->
          <a-card title="总体评语" :bordered="false" size="small" style="margin-bottom: 16px">
            <a-tag
              v-if="result.grading?.primary_error_cause && result.grading.primary_error_cause !== 'none'"
              color="orange"
              class="cv-tag-pop"
              style="margin-bottom: 8px"
            >
              主要问题：{{ result.grading.primary_error_cause }}
            </a-tag>
            <a-typography-paragraph
              style="font-size: 14px; white-space: pre-wrap; line-height: 1.8"
              class="cv-line-appear"
            >
              {{ result.grading?.overall_comment || result.comment || '暂无评语' }}
            </a-typography-paragraph>
          </a-card>

          <!-- 置信度标识 -->
          <div style="margin-bottom: 16px">
            <ConfidenceBadge :confidence="result.confidence || 0" />
            <a-tag v-if="result.model_key" color="default" style="margin-left: 8px">
              {{ result.model_key }}
            </a-tag>
          </div>

          <!-- 操作按钮 -->
          <a-space>
            <a-button type="primary" @click="handleConfirm">
              确认评分
            </a-button>
            <a-button @click="handleAdjust">
              调整分数
            </a-button>
          </a-space>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onBeforeUnmount, nextTick, watch, computed } from 'vue'
import { useGradingStore } from '@/stores/grading'
import { aiGrade, confirmGrading } from '@/api/grading'
import DualInputPanel from '@/components/ai-grading/DualInputPanel.vue'
import GradingStepReveal from '@/components/ai-grading/GradingStepReveal.vue'
import ScoreCounter from '@/components/ai-grading/ScoreCounter.vue'
import ConfidenceBadge from '@/components/ai-grading/ConfidenceBadge.vue'
import ErrorCauseTag from '@/components/ai-grading/ErrorCauseTag.vue'
import * as echarts from 'echarts'
import { message } from 'ant-design-vue'
import { ThunderboltOutlined } from '@ant-design/icons-vue'
import '@/assets/styles/ai-grading-animations.css'

const gradingStore = useGradingStore()

// ---- 表单数据 ----
const form = reactive({
  question: '',
  standardAnswer: '',
  submissionId: null,
})

const inputData = reactive({
  imageBase64: '',
  textContent: '',
})

// ---- 作文四维配置 ----
const essayDimensions = [
  { key: 'content', name: '内容', maxScore: 40 },
  { key: 'structure', name: '结构', maxScore: 20 },
  { key: 'language', name: '语言', maxScore: 25 },
  { key: 'handwriting', name: '书写', maxScore: 15 },
]

// ---- 批改结果 ----
const result = ref(null)

const dimensions = computed(() => result.value?.grading?.dimensions || {})

const ocrText = computed(() => {
  if (!result.value) return ''
  return result.value.ocr_text || result.value.recognized_text || ''
})

// ---- 雷达图 ----
const radarChartRef = ref(null)
let chartInstance = null
let resizeObserver = null

function initRadarChart() {
  if (!radarChartRef.value || !result.value) return

  // 销毁旧实例
  disposeChart()

  const dims = result.value.grading?.dimensions || {}
  const dimNames = ['内容', '结构', '语言', '书写']
  const dimKeys = ['content', 'structure', 'language', 'handwriting']

  chartInstance = echarts.init(radarChartRef.value)
  chartInstance.setOption({
    animationDuration: 1200,
    animationEasing: 'elasticOut',
    radar: {
      indicator: dimNames.map((name, i) => ({
        name,
        max: [40, 20, 25, 15][i],
      })),
      shape: 'circle',
      splitNumber: 4,
      axisName: {
        color: '#555',
        fontSize: 13,
        fontWeight: 500,
      },
      splitArea: {
        areaStyle: {
          color: ['rgba(55, 81, 254, 0.02)', 'rgba(55, 81, 254, 0.04)', 'rgba(55, 81, 254, 0.06)', 'rgba(55, 81, 254, 0.08)'],
        },
      },
    },
    series: [{
      type: 'radar',
      data: [{
        value: dimKeys.map(k => dims[k]?.score || 0),
        animationDelay: (idx) => idx * 100,
        areaStyle: { opacity: 0.2 },
        lineStyle: { color: '#3751FE', width: 2 },
        itemStyle: { color: '#3751FE' },
        symbol: 'circle',
        symbolSize: 6,
      }],
    }],
  })
}

function disposeChart() {
  if (chartInstance) {
    chartInstance.dispose()
    chartInstance = null
  }
}

function setupResizeObserver() {
  if (resizeObserver) resizeObserver.disconnect()
  if (!radarChartRef.value) return

  resizeObserver = new ResizeObserver(() => {
    if (chartInstance) {
      chartInstance.resize()
    }
  })
  resizeObserver.observe(radarChartRef.value)
}

// 当结果变化时初始化雷达图
watch(result, async (val) => {
  if (val) {
    await nextTick()
    initRadarChart()
    setupResizeObserver()
  }
}, { deep: false })

onBeforeUnmount(() => {
  disposeChart()
  if (resizeObserver) {
    resizeObserver.disconnect()
    resizeObserver = null
  }
})

// ---- 批改逻辑 ----
async function handleGrade() {
  if (!form.question.trim()) {
    message.warning('请输入作文题目')
    return
  }
  if (!inputData.imageBase64 && !inputData.textContent.trim()) {
    message.warning('请上传学生作答图片或粘贴文本')
    return
  }

  gradingStore.startGrading()
  result.value = null

  try {
    const payload = {
      question: form.question,
      standard_answer: form.standardAnswer,
      total_score: 100,
      subject_type: 'essay',
      submission_id: form.submissionId || null,
      image_base64: inputData.imageBase64 || undefined,
      // 把用户粘贴的文本答案传给后端（后端优先使用此字段作为学生答案）
      student_text: inputData.textContent?.trim() || undefined,
    }

    const res = await aiGrade(payload)
    result.value = res.data || res
    gradingStore.setResult(result.value)
    message.success('批改完成')
  } catch (e) {
    const errMsg = e?.response?.data?.detail || e?.message || '批改失败，请稍后重试'
    message.error(errMsg)
    gradingStore.reset()
  }
}

// ---- 确认评分 ----
async function handleConfirm() {
  if (!result.value?.id) {
    message.warning('无批改结果可确认')
    return
  }

  try {
    await confirmGrading(result.value.id)
    message.success('评分已确认')
  } catch (e) {
    message.error('确认失败：' + (e?.response?.data?.detail || e?.message || '未知错误'))
  }
}

// ---- 调整分数 ----
function handleAdjust() {
  message.info('分数调整功能开发中，可手动修改后重新提交')
}
</script>

<style scoped>
.settings-card {
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
}

.result-card {
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
}

.result-empty {
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-steps {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.dimension-header {
  font-size: 13px;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 4px;
}

.dimension-comment {
  font-size: 12px;
  color: #888;
  margin-top: 4px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
