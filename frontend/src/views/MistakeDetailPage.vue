<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="错题详情"
      @back="() => $router.push('/mistake-book')"
      style="padding: 0 0 16px 0"
    />

    <a-spin :spinning="loading">
      <!-- 原题 + 标准答案 -->
      <a-card title="原题" :bordered="false" class="detail-card">
        <template v-if="detail.homework_title" #extra>
          <a-tag color="blue">{{ detail.homework_title }}</a-tag>
        </template>
        <a-descriptions :column="1" bordered size="small">
          <a-descriptions-item label="题目">
            {{ detail.question_text || '-' }}
          </a-descriptions-item>
          <a-descriptions-item label="标准答案">
            <div class="answer-text">{{ detail.standard_answer || '暂无' }}</div>
          </a-descriptions-item>
        </a-descriptions>
      </a-card>

      <!-- 学生答案 + 批改详情 -->
      <a-card title="批改详情" :bordered="false" class="detail-card">
        <a-descriptions :column="2" bordered size="small">
          <a-descriptions-item label="得分">
            <span :class="scoreClass">
              {{ detail.score }} / {{ detail.max_score }}
            </span>
          </a-descriptions-item>
          <a-descriptions-item label="错因">
            <a-tag v-if="detail.error_type" :color="errorTagColor(detail.error_type)">
              {{ detail.error_type }}
            </a-tag>
            <span v-else>-</span>
          </a-descriptions-item>
          <a-descriptions-item label="错因分析" :span="2">
            {{ detail.error_cause || '-' }}
          </a-descriptions-item>
          <a-descriptions-item label="知识点" :span="2">
            <a-tag v-for="kp in (detail.knowledge_points || [])" :key="kp" color="blue">{{ kp }}</a-tag>
            <span v-if="!(detail.knowledge_points || []).length">-</span>
          </a-descriptions-item>
        </a-descriptions>

        <!-- 学生答案 -->
        <a-divider orientation="left">学生答案</a-divider>
        <div class="answer-text">{{ detail.student_answer_ocr || '暂无学生作答内容' }}</div>

        <!-- 批改评语 -->
        <a-divider orientation="left">批改评语</a-divider>
        <div class="answer-text">{{ detail.comment || '暂无评语' }}</div>

        <!-- 评分细则（折叠） -->
        <a-collapse v-if="detail.rubric || detail.grading" ghost style="margin-top: 12px">
          <a-collapse-panel key="rubric" header="评分细则与批改步骤">
            <pre v-if="detail.rubric" class="json-pre">{{ JSON.stringify(detail.rubric, null, 2) }}</pre>
            <pre v-if="detail.grading" class="json-pre">{{ JSON.stringify(detail.grading, null, 2) }}</pre>
          </a-collapse-panel>
        </a-collapse>
      </a-card>

      <!-- 订正历史时间线 -->
      <a-card title="订正历史" :bordered="false" class="detail-card">
        <a-empty v-if="!(detail.correction_records || []).length" description="暂无订正记录" />
        <a-timeline v-else>
          <a-timeline-item
            v-for="cr in detail.correction_records"
            :key="cr.correction_id"
            :color="cr.improved ? 'green' : 'red'"
          >
            <div>
              <b>订正 #{{ cr.correction_id }}</b>
              <span style="margin-left: 12px">
                得分：<span :class="cr.improved ? 'score-good' : 'score-bad'">
                  {{ cr.correction_score }} / {{ detail.max_score }}
                </span>
              </span>
              <a-tag v-if="cr.improved" color="success" style="margin-left: 8px">进步</a-tag>
              <a-tag v-else color="error" style="margin-left: 8px">未进步</a-tag>
            </div>
            <div class="text-muted" style="font-size: 12px">
              {{ formatDate(cr.created_at) }} | 原始分 {{ cr.original_score }}
            </div>
          </a-timeline-item>
        </a-timeline>
      </a-card>

      <!-- 操作按钮 -->
      <div style="margin-top: 16px; text-align: center">
        <a-button type="primary" @click="$router.push('/correction')">
          去订正
        </a-button>
        <a-tooltip title="阶段2启用：从错题一键生成相似变式题">
          <a-button type="default" disabled style="margin-left: 12px">
            生成相似题（即将上线）
          </a-button>
        </a-tooltip>
      </div>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { message } from 'ant-design-vue'
import { getMistakeDetail } from '@/api/correction'

const route = useRoute()
const loading = ref(false)
const detail = ref({})

const scoreClass = computed(() => {
  const { score, max_score } = detail.value
  if (!max_score || max_score <= 0) return 'text-muted'
  const ratio = score / max_score
  if (ratio >= 0.8) return 'score-good'
  if (ratio >= 0.5) return 'score-mid'
  return 'score-bad'
})

async function loadDetail() {
  const gradingId = route.params.id
  if (!gradingId) return
  loading.value = true
  try {
    const res = await getMistakeDetail(gradingId)
    detail.value = res.data
  } catch (e) {
    message.error('加载错题详情失败')
  } finally {
    loading.value = false
  }
}

function errorTagColor(errorType) {
  const map = {
    '计算粗心': 'orange',
    '概念混淆': 'red',
    '审题不清': 'purple',
    '辅助线缺失': 'cyan',
    '逻辑跳步': 'geekblue',
    '知识缺失': 'volcano',
  }
  return map[errorType] || 'default'
}

function formatDate(dt) {
  if (!dt) return '-'
  try {
    const d = new Date(dt)
    return d.toLocaleDateString('zh-CN', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' })
  } catch {
    return dt
  }
}

onMounted(() => {
  loadDetail()
})
</script>

<style scoped>
.detail-card {
  border-radius: 12px;
  margin-bottom: 16px;
}
.answer-text {
  white-space: pre-wrap;
  line-height: 1.8;
  color: #333;
}
.json-pre {
  background: #f5f5f5;
  padding: 12px;
  border-radius: 8px;
  font-size: 12px;
  max-height: 300px;
  overflow: auto;
}
.score-good { color: #52c41a; font-weight: 600; }
.score-mid { color: #faad14; font-weight: 600; }
.score-bad { color: #ff4d4f; font-weight: 600; }
.text-muted { color: #999; }
</style>
