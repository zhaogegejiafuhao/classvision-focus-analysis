<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header title="我的批改" sub-title="AI批改详情·订正练习·知识巩固" />

    <a-spin :spinning="pageLoading">
      <a-card>
        <a-table
          :columns="columns"
          :data-source="submissions"
          row-key="id"
          :pagination="{ pageSize: 10 }"
          size="middle"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'title'">
              <span style="font-weight: 500">{{ record.homework_title }}</span>
            </template>
            <template v-else-if="column.key === 'submitted_at'">
              {{ record.submitted_at ? formatTime(record.submitted_at) : '-' }}
            </template>
            <template v-else-if="column.key === 'score'">
              <template v-if="record.score != null">
                <span :style="{ color: record.score >= (record.max_score * 0.6) ? '#52c41a' : '#ff4d4f', fontWeight: 600 }">
                  {{ record.score }}
                </span>
                <span style="color: #999"> / {{ record.max_score }}</span>
              </template>
              <a-tag v-else color="default">未批改</a-tag>
            </template>
            <template v-else-if="column.key === 'status'">
              <a-tag v-if="record.status === 'graded'" color="green">已批改</a-tag>
              <a-tag v-else-if="record.status === 'corrected'" color="blue">已订正</a-tag>
              <a-tag v-else-if="record.status === 'submitted'" color="orange">待批改</a-tag>
              <a-tag v-else color="default">{{ record.status }}</a-tag>
            </template>
            <template v-else-if="column.key === 'action'">
              <a-button
                type="primary"
                size="small"
                ghost
                @click="openDrawer(record)"
                :disabled="record.status !== 'graded' && record.status !== 'corrected'"
              >
                查看详情
              </a-button>
            </template>
          </template>
        </a-table>

        <a-empty v-if="submissions.length === 0 && !pageLoading" description="暂无提交记录" style="margin-top: 40px" />
      </a-card>
    </a-spin>

    <!-- 批改详情抽屉 -->
    <a-drawer
      v-model:open="drawerVisible"
      :title="drawerTitle"
      width="720"
      :destroy-on-close="true"
      placement="right"
    >
      <a-spin :spinning="drawerLoading">
        <template v-if="gradingData">
          <!-- Step 0: 识别 — 学生答案 -->
          <GradingStepReveal :step-index="0" :current-step-index="currentStep" title="识别">
            <div class="student-answer-text">
              <div class="answer-label">学生作答：</div>
              <div class="answer-content">{{ gradingData.student_answer || gradingData.ocr_text || '（无文本内容）' }}</div>
            </div>
          </GradingStepReveal>

          <!-- Step 1: 判断 — 错因标签 -->
          <GradingStepReveal :step-index="1" :current-step-index="currentStep" title="判断">
            <ErrorCauseTag
              :error-type="gradingData.error_type"
              :error-cause="gradingData.error_cause"
              :knowledge-points="gradingData.knowledge_points || []"
            />
            <div v-if="!gradingData.error_type && !gradingData.error_cause" class="no-error-hint">
              <a-tag color="green">作答正确，无需错因分析</a-tag>
            </div>
          </GradingStepReveal>

          <!-- Step 2: 量规 — RubricTable -->
          <GradingStepReveal :step-index="2" :current-step-index="currentStep" title="量规">
            <RubricTable
              :rubric-steps="gradingData.rubric_steps || gradingData.rubric?.steps || []"
              :grading-steps="gradingData.grading_steps || gradingData.steps || []"
            />
          </GradingStepReveal>

          <!-- Step 3: 评分 — ScoreCounter + ConfidenceBadge + comment -->
          <GradingStepReveal :step-index="3" :current-step-index="currentStep" title="评分">
            <div class="score-section">
              <ScoreCounter
                :target-score="gradingData.total_score ?? gradingData.score ?? 0"
                :max-score="gradingData.max_score ?? 100"
              />
              <ConfidenceBadge
                :confidence="gradingData.confidence ?? 0.85"
                style="margin-left: 16px"
              />
            </div>
            <div v-if="gradingData.comment || gradingData.feedback" class="grading-comment">
              <div class="comment-label">AI评语：</div>
              <div class="comment-text">{{ gradingData.comment || gradingData.feedback }}</div>
            </div>
          </GradingStepReveal>

          <!-- 订正区 -->
          <a-divider orientation="left">订正区</a-divider>

          <template v-if="currentSubmission?.status === 'corrected' && currentSubmission?.correction_id">
            <CorrectionComparison :correction-id="currentSubmission.correction_id" />
          </template>
          <template v-else-if="gradingData.total_score != null && gradingData.total_score < (gradingData.max_score ?? 100)">
            <CorrectionForm
              :submission-id="currentSubmission.id"
              @submitted="onCorrectionSubmitted"
            />
          </template>
          <template v-else>
            <a-alert type="info" message="满分作答，无需订正" show-icon />
          </template>

          <!-- 相似练习 -->
          <template v-if="hasErrorForSimilarQuestions">
            <a-divider orientation="left">相似练习</a-divider>
            <SimilarQuestionPanel
              :question="gradingData.question || currentSubmission?.homework_title || ''"
              :knowledge-points="gradingData.knowledge_points || []"
              :error-type="gradingData.error_cause || gradingData.error_type || ''"
              :standard-answer="gradingData.standard_answer || ''"
            />
            <div style="margin-top: 12px; text-align: center">
              <a-button type="link" @click="goMistakeDetail">
                在错题本中查看详情 →
              </a-button>
            </div>
          </template>
        </template>

        <a-empty v-else-if="!drawerLoading" description="暂无批改数据" />
      </a-spin>
    </a-drawer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '@/api'
import { getGradingResult } from '@/api/grading'
import { submitCorrection, getCorrectionComparison, getPersonalizedCorrection } from '@/api/correction'
import { generateSimilarQuestions } from '@/api/similarQuestions'
import GradingStepReveal from '@/components/ai-grading/GradingStepReveal.vue'
import ScoreCounter from '@/components/ai-grading/ScoreCounter.vue'
import ConfidenceBadge from '@/components/ai-grading/ConfidenceBadge.vue'
import RubricTable from '@/components/ai-grading/RubricTable.vue'
import ErrorCauseTag from '@/components/ai-grading/ErrorCauseTag.vue'
import CorrectionForm from '@/components/correction/CorrectionForm.vue'
import CorrectionComparison from '@/components/correction/CorrectionComparison.vue'
import SimilarQuestionPanel from '@/components/similar-questions/SimilarQuestionPanel.vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import '@/assets/styles/ai-grading-animations.css'

const router = useRouter()

// ===== 页面数据 =====
const pageLoading = ref(false)
const submissions = ref([])
const myPersonId = ref(null)

// ===== 表格列 =====
const columns = [
  { key: 'title', title: '作业标题', dataIndex: 'homework_title', ellipsis: true },
  { key: 'submitted_at', title: '提交时间', dataIndex: 'submitted_at', width: 170 },
  { key: 'score', title: '分数', width: 120 },
  { key: 'status', title: '状态', dataIndex: 'status', width: 100 },
  { key: 'action', title: '操作', width: 100 },
]

// ===== 抽屉状态 =====
const drawerVisible = ref(false)
const drawerLoading = ref(false)
const currentSubmission = ref(null)
const gradingData = ref(null)
const currentStep = ref(-1)

const drawerTitle = computed(() => {
  if (!currentSubmission.value) return '批改详情'
  return `${currentSubmission.value.homework_title || '作业'} — 批改详情`
})

// 是否有错因/知识点可供推荐相似题
const hasErrorForSimilarQuestions = computed(() => {
  if (!gradingData.value) return false
  const kp = gradingData.value.knowledge_points
  const et = gradingData.value.error_type || gradingData.value.error_cause
  return (kp && kp.length > 0) || !!et
})

// ===== 数据获取 =====
async function fetchSubmissions() {
  pageLoading.value = true
  try {
    // 获取当前用户
    const userStr = localStorage.getItem('user')
    if (userStr) {
      const user = JSON.parse(userStr)
      myPersonId.value = user.id
    }
    if (!myPersonId.value) return

    // 获取分配给学生的作业列表
    const hwRes = await api.get('/homework/assigned').catch(() => ({ data: [] }))
    const homeworks = hwRes.data || []

    // 对每个作业获取提交状态
    const allSubmissions = []
    for (const hw of homeworks) {
      try {
        const subRes = await api.get(`/homework/my-submissions/${hw.id}`).catch(() => null)
        if (subRes?.data?.submitted) {
          const sub = subRes.data.submission
          allSubmissions.push({
            id: sub.id,
            homework_id: hw.id,
            homework_title: hw.title,
            submitted_at: sub.submitted_at,
            score: sub.score,
            max_score: hw.total_score || 100,
            status: sub.status,
            content: sub.content,
            correction_id: sub.correction_id || null,
          })
        }
      } catch {
        // 跳过该作业
      }
    }

    submissions.value = allSubmissions
  } catch (e) {
    message.error('获取提交列表失败')
  } finally {
    pageLoading.value = false
  }
}

// ===== 打开抽屉 =====
async function openDrawer(record) {
  currentSubmission.value = record
  gradingData.value = null
  currentStep.value = -1
  drawerVisible.value = true
  drawerLoading.value = true

  try {
    const res = await getGradingResult(record.id)
    gradingData.value = res.data

    // 逐步揭示动画：[0, 800, 1600, 2400]ms
    const delays = [0, 800, 1600, 2400]
    delays.forEach((delay, step) => {
      setTimeout(() => {
        currentStep.value = step
      }, delay)
    })
  } catch (e) {
    message.error('获取批改详情失败')
  } finally {
    drawerLoading.value = false
  }
}

// ===== 订正提交回调 =====
function onCorrectionSubmitted() {
  message.success('订正已提交，请等待二次批改')
  // 刷新提交列表
  fetchSubmissions()
}

// 跳转到错题详情
function goMistakeDetail() {
  if (gradingData.value?.id) {
    router.push(`/mistake-book/${gradingData.value.id}`)
  }
}

// ===== 工具函数 =====
function formatTime(time) {
  if (!time) return ''
  const d = new Date(time)
  if (isNaN(d.getTime())) return time
  const pad = (n) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`
}

// ===== 初始化 =====
onMounted(fetchSubmissions)
</script>

<style scoped>
.student-answer-text {
  padding: 8px 0;
}

.answer-label {
  font-size: 13px;
  color: #666;
  font-weight: 500;
  margin-bottom: 6px;
}

.answer-content {
  font-size: 14px;
  line-height: 1.8;
  color: #333;
  white-space: pre-wrap;
  padding: 10px 12px;
  background: #f9f9fb;
  border-radius: 6px;
  border-left: 3px solid #3751FE;
}

.no-error-hint {
  padding: 4px 0;
}

.score-section {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  padding: 8px 0;
}

.grading-comment {
  margin-top: 12px;
  padding: 10px 12px;
  background: #f6ffed;
  border-radius: 6px;
  border: 1px solid #b7eb8f;
}

.comment-label {
  font-size: 13px;
  color: #52c41a;
  font-weight: 600;
  margin-bottom: 4px;
}

.comment-text {
  font-size: 14px;
  line-height: 1.7;
  color: #333;
  white-space: pre-wrap;
}
</style>