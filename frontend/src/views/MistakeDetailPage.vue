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
        <a-button type="primary" @click="goCorrection">
          去订正
        </a-button>
        <a-button type="default" style="margin-left: 12px" @click="showGenerateModal = true">
          生成相似题
        </a-button>
        <a-button type="default" style="margin-left: 12px" @click="$router.push('/my-similar-questions')">
          查看相似题
        </a-button>
      </div>

      <!-- 生成相似题弹窗 -->
      <a-modal
        v-model:open="showGenerateModal"
        title="生成相似变式题"
        @ok="handleGenerate"
        :confirm-loading="generating"
        ok-text="开始生成"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="学生分层">
            <a-select v-model:value="generateForm.tier" placeholder="选择分层策略">
              <a-select-option value="优等生">优等生（根源变式）</a-select-option>
              <a-select-option value="中等生">中等生（同类变式）</a-select-option>
              <a-select-option value="学困生">学困生（基础铺垫）</a-select-option>
            </a-select>
          </a-form-item>
          <a-form-item label="生成数量">
            <a-input-number v-model:value="generateForm.count" :min="1" :max="10" style="width: 100%" />
          </a-form-item>
        </a-form>
      </a-modal>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { getMistakeDetail, generateSimilarFromMistake } from '@/api/correction'

const route = useRoute()
const router = useRouter()
const loading = ref(false)
const detail = ref({})
const showGenerateModal = ref(false)
const generating = ref(false)
const generateForm = ref({ tier: '中等生', count: 3 })

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

function goCorrection() {
  // 传递 submission_id 和来源信息，订正完成后可跳回
  const query = {}
  if (detail.value.submission_id) query.submission_id = detail.value.submission_id
  if (route.params.id) query.from_grading_id = route.params.id
  router.push({ path: '/correction', query })
}

async function handleGenerate() {
  const gradingId = route.params.id
  if (!gradingId) return
  generating.value = true
  try {
    const res = await generateSimilarFromMistake(gradingId, generateForm.value)
    showGenerateModal.value = false
    message.success(`已生成 ${res.data.generated} 道相似题`)
  } catch (e) {
    message.error('生成相似题失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    generating.value = false
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
