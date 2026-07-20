<template>
  <div class="paper-summary-card">
    <a-card :bordered="false" class="summary-card">
      <!-- 顶部：学生 + 总分 -->
      <div class="summary-header">
        <div class="student-info">
          <UserOutlined />
          <span class="student-name">{{ studentName || '未知学生' }}</span>
          <a-tag color="default">提交ID: {{ submissionId || '-' }}</a-tag>
        </div>
        <div class="score-display">
          <div class="score-number" :class="scoreClass">{{ totalScore }}</div>
          <div class="score-max">/ {{ maxScore }}</div>
        </div>
      </div>

      <!-- 中部：4 个统计卡片 -->
      <a-row :gutter="12" class="stat-row">
        <a-col :span="6">
          <div class="stat-card stat-total">
            <div class="stat-value">{{ summary.total_questions || 0 }}</div>
            <div class="stat-label">总题数</div>
          </div>
        </a-col>
        <a-col :span="6">
          <div class="stat-card stat-correct">
            <div class="stat-value">{{ summary.correct_count || 0 }}</div>
            <div class="stat-label">正确</div>
          </div>
        </a-col>
        <a-col :span="6">
          <div class="stat-card stat-wrong">
            <div class="stat-value">{{ summary.wrong_count || 0 }}</div>
            <div class="stat-label">错误</div>
          </div>
        </a-col>
        <a-col :span="6">
          <div class="stat-card stat-ungraded">
            <div class="stat-value">{{ summary.ungraded_count || 0 }}</div>
            <div class="stat-label">未批改</div>
          </div>
        </a-col>
      </a-row>

      <!-- 正确率横条 -->
      <div class="accuracy-bar-wrap">
        <div class="accuracy-label">
          <span>正确率</span>
          <span class="accuracy-value">{{ ((summary.accuracy || 0) * 100).toFixed(1) }}%</span>
        </div>
        <a-progress
          :percent="Math.round((summary.accuracy || 0) * 100)"
          :stroke-color="accuracyColor"
          :show-info="false"
          size="small"
        />
      </div>

      <!-- 按题型分组 -->
      <div v-if="byTypeList.length" class="by-type-section">
        <div class="section-title">按题型分组</div>
        <div v-for="t in byTypeList" :key="t.type" class="by-type-row">
          <div class="by-type-label">
            <a-tag :color="typeColor(t.type)" size="small">{{ typeLabel(t.type) }}</a-tag>
            <span class="by-type-count">{{ t.correct }}/{{ t.total }} 正确</span>
          </div>
          <div class="by-type-bar">
            <a-progress
              :percent="t.total ? Math.round((t.correct / t.total) * 100) : 0"
              :stroke-color="t.total && t.correct === t.total ? '#16a34a' : '#3751FE'"
              :show-info="false"
              size="small"
            />
          </div>
          <div class="by-type-score">{{ t.score.toFixed(1) }}/{{ t.max_score.toFixed(1) }} 分</div>
        </div>
      </div>
    </a-card>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { UserOutlined } from '@ant-design/icons-vue'

const props = defineProps({
  studentName: { type: String, default: '' },
  submissionId: { type: [Number, String], default: '' },
  totalScore: { type: Number, default: 0 },
  maxScore: { type: Number, default: 0 },
  summary: { type: Object, default: () => ({}) },
})

const scoreClass = computed(() => {
  if (!props.maxScore) return ''
  const ratio = props.totalScore / props.maxScore
  if (ratio >= 0.85) return 'excellent'
  if (ratio >= 0.6) return 'good'
  return 'need-improve'
})

const accuracyColor = computed(() => {
  const acc = props.summary.accuracy || 0
  if (acc >= 0.85) return '#16a34a'
  if (acc >= 0.6) return '#3751FE'
  return '#fa8c16'
})

const byTypeList = computed(() => {
  const byType = props.summary.by_type || {}
  return Object.entries(byType).map(([type, data]) => ({
    type,
    total: data.total || 0,
    correct: data.correct || 0,
    wrong: data.wrong || 0,
    score: data.score || 0,
    max_score: data.max_score || 0,
  }))
})

function typeLabel(type) {
  const m = { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '大题' }
  return m[type] || type
}

function typeColor(type) {
  const m = { single: 'blue', multi: 'cyan', judge: 'geekblue', fill: 'orange', essay: 'purple' }
  return m[type] || 'default'
}
</script>

<style scoped>
.summary-card {
  border-radius: 12px;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  margin-bottom: 16px;
}

.summary-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 12px;
  border-bottom: 1px dashed #e8e8e8;
  margin-bottom: 12px;
}

.student-info {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #1a1a2e;
}

.student-name {
  font-weight: 600;
  font-size: 15px;
}

.score-display {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.score-number {
  font-size: 36px;
  font-weight: 700;
  color: #1a1a2e;
  line-height: 1;
}

.score-number.excellent { color: #16a34a; }
.score-number.good { color: #3751FE; }
.score-number.need-improve { color: #ef4444; }

.score-max {
  font-size: 18px;
  color: #888;
  font-weight: 500;
}

.stat-row {
  margin-bottom: 12px;
}

.stat-card {
  text-align: center;
  padding: 12px 8px;
  border-radius: 8px;
  background: #fafafa;
}

.stat-total { background: rgba(55, 81, 254, 0.06); }
.stat-correct { background: rgba(22, 163, 74, 0.06); }
.stat-wrong { background: rgba(239, 68, 68, 0.06); }
.stat-ungraded { background: rgba(250, 140, 22, 0.06); }

.stat-value {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a2e;
  line-height: 1.2;
}

.stat-label {
  font-size: 12px;
  color: #888;
  margin-top: 2px;
}

.accuracy-bar-wrap {
  margin-bottom: 12px;
}

.accuracy-label {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #666;
  margin-bottom: 4px;
}

.accuracy-value {
  font-weight: 600;
  color: #1a1a2e;
}

.by-type-section {
  margin-top: 8px;
}

.section-title {
  font-size: 13px;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 8px;
}

.by-type-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
  font-size: 12px;
}

.by-type-label {
  width: 130px;
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 0;
}

.by-type-count {
  color: #888;
  font-size: 11px;
}

.by-type-bar {
  flex: 1;
}

.by-type-score {
  width: 90px;
  text-align: right;
  color: #555;
  font-size: 12px;
  flex-shrink: 0;
}
</style>
