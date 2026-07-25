<template>
  <div class="step-review">
    <div v-if="!store.examId || store.reviewQuestions.length === 0" class="no-data">
      <a-result status="warning" title="暂无审核数据" sub-title="请先完成组卷操作后再进入审核">
        <template #extra>
          <a-button type="primary" @click="goBackCompose">返回组卷操作</a-button>
        </template>
      </a-result>
    </div>

    <div v-else class="review-panel">
      <!-- 试卷概览 -->
      <div class="review-overview">
        <a-row :gutter="16" align="middle">
          <a-col :span="14">
            <h3 style="margin: 0">{{ store.title || '组卷' }}</h3>
            <p style="margin: 4px 0 0; color: #888; font-size: 13px">
              {{ store.reviewQuestionCount }} 题 · 总分 {{ store.reviewTotalScore }} 分 · 时长 {{ store.duration }} 分钟
            </p>
          </a-col>
          <a-col :span="10" style="text-align: right">
            <a-space>
              <a-button @click="goBackCompose">重新组卷</a-button>
              <a-button @click="handleExportPDF">
                <template #icon><ExportOutlined /></template>
                导出试卷
              </a-button>
              <a-popconfirm
                title="发布后学生将收到考试通知，确定发布？"
                @confirm="handlePublish"
                ok-text="确定发布"
                cancel-text="取消"
              >
                <a-button type="primary" :loading="publishing">
                  <template #icon><SendOutlined /></template>
                  确认发布
                </a-button>
              </a-popconfirm>
            </a-space>
          </a-col>
        </a-row>
      </div>

      <!-- 难度分布 -->
      <DifficultyBar :questions="store.reviewQuestions" />

      <!-- 批量分值设置 -->
      <div class="batch-score-bar">
        <span class="batch-label">批量设置分值：</span>
        <a-select v-model:value="batchScoreType" style="width: 100px" size="small">
          <a-select-option value="single">单选题</a-select-option>
          <a-select-option value="multi">多选题</a-select-option>
          <a-select-option value="judge">判断题</a-select-option>
          <a-select-option value="fill">填空题</a-select-option>
          <a-select-option value="essay">简答题</a-select-option>
          <a-select-option value="all">所有题型</a-select-option>
        </a-select>
        <span class="batch-each">每题</span>
        <a-input-number v-model:value="batchScoreValue" :min="1" :max="100" size="small" style="width: 70px" />
        <span class="batch-unit">分</span>
        <a-button size="small" type="primary" @click="applyBatchScore">应用</a-button>
      </div>

      <!-- 逐题审核列表 -->
      <div class="review-questions">
        <div v-for="(q, idx) in store.reviewQuestions" :key="idx" class="review-question-item">
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
            <div v-for="(opt, oi) in q.options" :key="oi" class="review-q-option">
              <span class="opt-prefix">{{ String.fromCharCode(65 + oi) }}.</span>
              <LatexText :content="opt" />
            </div>
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
              <a-button size="small" @click="handleSwapQuestion(idx)" :loading="q.swapping">
                <template #icon><SwapOutlined /></template>
                换一题
              </a-button>
              <a-button size="small" danger @click="store.removeReviewQuestion(idx)">
                <template #icon><DeleteOutlined /></template>
                删除
              </a-button>
            </a-space>
          </div>
        </div>
      </div>

      <!-- 总分汇总 -->
      <div class="review-summary">
        <a-descriptions bordered size="small" :column="3">
          <a-descriptions-item label="题目数">{{ store.reviewQuestionCount }}</a-descriptions-item>
          <a-descriptions-item label="总分">{{ store.reviewTotalScore }} 分</a-descriptions-item>
          <a-descriptions-item label="考试时长">{{ store.duration }} 分钟</a-descriptions-item>
        </a-descriptions>
      </div>

      <!-- 底部操作 -->
      <div class="review-bottom-actions">
        <a-button @click="goBackCompose">返回组卷</a-button>
        <a-space>
          <a-button @click="handleExportPDF">
            <template #icon><ExportOutlined /></template>
            导出试卷
          </a-button>
          <a-popconfirm
            title="发布后学生将收到考试通知，确定发布？"
            @confirm="handlePublish"
            ok-text="确定发布"
            cancel-text="取消"
          >
            <a-button type="primary" :loading="publishing">
              <template #icon><SendOutlined /></template>
              确认发布
            </a-button>
          </a-popconfirm>
        </a-space>
      </div>
    </div>

    <!-- 换题候选弹窗 -->
    <SwapQuestionModal
      :open="store.showSwapModal"
      :candidates="store.swapCandidates"
      @update:open="store.showSwapModal = $event"
      @select="selectSwapCandidate"
    />

    <!-- 发布成功弹窗 -->
    <a-modal v-model:open="showPublishSuccess" title="发布成功" :footer="null" width="420px">
      <a-result status="success" :title="`考试发布成功！${publishInfo.questionCount} 题 / ${publishInfo.totalScore} 分`" sub-title="已通知关联课堂的学生">
        <template #extra>
          <a-space>
            <a-button type="primary" @click="goExamDetail">查看考试详情</a-button>
            <a-button @click="goExamList">返回考试列表</a-button>
            <a-button @click="handleNewCompose">继续组卷</a-button>
          </a-space>
        </template>
      </a-result>
    </a-modal>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { SwapOutlined, DeleteOutlined, ExportOutlined, SendOutlined } from '@ant-design/icons-vue'
import { useExamComposeStore } from '@/stores/examCompose'
import { swapQuestionCandidates, publishExam } from '@/api/examTemplate'
import { exportExamPaper } from '@/api/exam'
import LatexText from '@/components/LatexText.vue'
import DifficultyBar from '@/components/exam-compose/DifficultyBar.vue'
import SwapQuestionModal from '@/components/exam-compose/SwapQuestionModal.vue'

const router = useRouter()
const store = useExamComposeStore()

const publishing = ref(false)
const showPublishSuccess = ref(false)
const publishInfo = ref({ questionCount: 0, totalScore: 0 })

// 批量分值设置
const batchScoreType = ref('single')
const batchScoreValue = ref(5)

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

function getTypeColor(type) {
  return { single: 'blue', multi: 'purple', judge: 'green', fill: 'orange', essay: 'red' }[type] || 'default'
}

function applyBatchScore() {
  const targetType = batchScoreType.value
  const newScore = batchScoreValue.value
  let count = 0
  for (const q of store.reviewQuestions) {
    if (targetType === 'all' || q.type === targetType) {
      q.scoreOverride = newScore
      count++
    }
  }
  if (count > 0) {
    message.success(`已将 ${count} 题${targetType === 'all' ? '' : getTypeText(targetType)}的分值设为 ${newScore} 分`)
  } else {
    message.warning('没有找到对应题型的题目')
  }
}

async function handleSwapQuestion(idx) {
  const q = store.reviewQuestions[idx]
  q.swapping = true
  store.swapTargetIndex = idx
  const excludeIds = store.reviewQuestions
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
    store.swapCandidates = res.data.candidates || []
    if (store.swapCandidates.length === 0) {
      message.warning('没有找到合适的替换题，请先向题库中添加更多同类型题目')
    } else {
      const matchLevel = res.data.match_level
      if (matchLevel >= 3) {
        message.info(`已放宽筛选条件，找到 ${store.swapCandidates.length} 道候选题（匹配级别 ${matchLevel}/4）`)
      }
      store.showSwapModal = true
    }
  } catch (e) {
    const msg = e?.response?.data?.detail || '换题请求失败'
    message.error(msg)
  }
  finally { q.swapping = false }
}

function selectSwapCandidate(candidate) {
  const idx = store.swapTargetIndex
  if (idx < 0 || idx >= store.reviewQuestions.length) return
  store.replaceReviewQuestion(idx, candidate)
  store.showSwapModal = false
  message.success('换题成功')
}

async function handleExportPDF() {
  try {
    const res = await exportExamPaper(store.examId)
    const blob = new Blob([res.data], { type: 'text/html' })
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `试卷_${store.examId}.html`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  } catch (e) {
    message.error('导出试卷失败')
  }
}

async function handlePublish() {
  publishing.value = true
  try {
    const payload = store.collectPublishPayload()
    const res = await publishExam(store.examId, payload)
    publishInfo.value = {
      questionCount: res.data.question_count,
      totalScore: res.data.total_score,
    }
    showPublishSuccess.value = true
  } catch (e) {
    const msg = e?.response?.data?.detail || '发布失败'
    message.error(msg)
  } finally {
    publishing.value = false
  }
}

function goExamDetail() {
  router.push(`/exams/${store.examId}`)
}

function goExamList() {
  router.push('/exams')
}

function handleNewCompose() {
  store.reset()
  router.push('/exam-compose')
}

function goBackCompose() {
  store.setStep(1)
  router.push('/exam-compose/compose')
}
</script>

<style scoped>
.step-review { padding: 0 8px; }
.no-data { text-align: center; padding: 24px; }
.review-overview {
  padding: 12px 16px;
  background: linear-gradient(135deg, #f0f5ff 0%, #e8f4f8 100%);
  border-radius: 8px;
  margin-bottom: 12px;
}
.batch-score-bar {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 12px; background: #fffbe6;
  border-radius: 6px; margin-bottom: 12px;
  font-size: 13px; border: 1px solid #ffe58f;
}
.batch-label { color: #666; font-weight: 500; }
.batch-each { color: #555; }
.batch-unit { color: #555; }
.review-questions { display: flex; flex-direction: column; gap: 8px; }
.review-question-item {
  padding: 12px 14px; background: #fff;
  border: 1px solid #eef0f5; border-radius: 8px;
  transition: border-color 0.2s;
}
.review-question-item:hover { border-color: #3751FE; }
.review-q-header { display: flex; align-items: center; gap: 6px; margin-bottom: 6px; }
.review-q-order {
  width: 20px; height: 20px; border-radius: 50%;
  background: #3751FE; color: #fff; font-size: 11px; font-weight: 600;
  display: flex; align-items: center; justify-content: center;
}
.review-q-category { color: #888; font-size: 12px; }
.review-q-content { font-size: 13px; color: #333; margin-bottom: 6px; }
.content-expanded { white-space: pre-wrap; }
.review-q-options { margin: 6px 0; padding: 6px 10px; background: #f8f9fc; border-radius: 4px; }
.review-q-option { font-size: 12px; color: #555; padding: 2px 0; display: flex; align-items: baseline; gap: 2px; }
.opt-prefix { color: #3751FE; font-weight: 600; flex-shrink: 0; }
.review-q-analysis { font-size: 12px; color: #666; padding: 4px 8px; background: #fffbe6; border-radius: 4px; margin: 4px 0; }
.analysis-label { color: #fa8c16; font-weight: 500; }
.review-q-actions { display: flex; justify-content: space-between; align-items: center; margin-top: 6px; }
.review-q-score { display: flex; align-items: center; gap: 4px; }
.score-label { color: #666; font-size: 13px; }
.score-hint { color: #aaa; font-size: 11px; }
.review-summary { margin-top: 16px; }
.review-bottom-actions {
  margin-top: 16px; padding-top: 16px;
  border-top: 1px solid #f0f0f0;
  display: flex; justify-content: space-between; align-items: center;
}
</style>
