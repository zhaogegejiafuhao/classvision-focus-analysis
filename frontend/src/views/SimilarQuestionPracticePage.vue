<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="相似题练习"
      @back="() => $router.push('/my-similar-questions')"
      style="padding: 0 0 16px 0"
    />

    <a-spin :spinning="loading">
      <!-- 题目 -->
      <a-card title="题目" :bordered="false" class="detail-card">
        <template #extra>
          <a-tag :color="variantColor(detail.variant_type)">{{ detail.variant_type }}</a-tag>
          <a-tag>{{ detail.difficulty }}</a-tag>
        </template>
        <div class="question-text">{{ detail.question_text || '加载中...' }}</div>

        <!-- 标准答案（折叠） -->
        <a-collapse ghost style="margin-top: 12px">
          <a-collapse-panel key="answer" header="查看标准答案">
            <div class="answer-text">{{ detail.standard_answer || '暂无' }}</div>
          </a-collapse-panel>
        </a-collapse>
      </a-card>

      <!-- 作答区 -->
      <a-card title="我的答案" :bordered="false" class="detail-card">
        <a-textarea
          v-model:value="answerText"
          :rows="8"
          placeholder="输入你的解答过程..."
          show-count
          :maxlength="5000"
          :disabled="submitted"
        />

        <div style="margin-top: 16px; text-align: center">
          <a-button
            v-if="!submitted"
            type="primary"
            :loading="submitting"
            :disabled="!answerText.trim()"
            @click="handleSubmit"
          >
            提交批改
          </a-button>

          <a-button v-else type="default" @click="$router.push('/my-similar-questions')">
            返回列表
          </a-button>
        </div>
      </a-card>

      <!-- 批改结果 -->
      <a-card v-if="result" title="批改结果" :bordered="false" class="detail-card">
        <a-descriptions :column="2" bordered size="small">
          <a-descriptions-item label="得分">
            <span :class="result.score >= result.max_score * 0.8 ? 'score-good' : 'score-bad'">
              {{ result.score }} / {{ result.max_score }}
            </span>
          </a-descriptions-item>
          <a-descriptions-item label="掌握状态">
            <a-tag :color="result.mastery_status === 'passed' ? 'success' : 'error'">
              {{ result.mastery_status === 'passed' ? '已掌握' : '未通过' }}
            </a-tag>
          </a-descriptions-item>
        </a-descriptions>

        <div v-if="result.comment" style="margin-top: 12px">
          <a-divider orientation="left">评语</a-divider>
          <div class="answer-text">{{ result.comment }}</div>
        </div>

        <a-collapse v-if="result.grading && Object.keys(result.grading).length" ghost style="margin-top: 12px">
          <a-collapse-panel key="detail" header="批改步骤详情">
            <pre class="json-pre">{{ JSON.stringify(result.grading, null, 2) }}</pre>
          </a-collapse-panel>
        </a-collapse>
      </a-card>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { message } from 'ant-design-vue'
import { getSimilarQuestionDetail, submitSimilarAnswer } from '@/api/similarQuestions'

const route = useRoute()
const loading = ref(false)
const submitting = ref(false)
const submitted = ref(false)
const detail = ref({})
const answerText = ref('')
const result = ref(null)

async function loadDetail() {
  const similarId = route.params.id
  if (!similarId) return
  loading.value = true
  try {
    const res = await getSimilarQuestionDetail(similarId)
    detail.value = res.data
    // 如果已经练习过，回显答案
    if (res.data.student_answer) {
      answerText.value = res.data.student_answer
      submitted.value = true
    }
  } catch (e) {
    message.error('加载题目失败')
  } finally {
    loading.value = false
  }
}

async function handleSubmit() {
  const similarId = route.params.id
  if (!similarId || !answerText.value.trim()) return
  submitting.value = true
  try {
    const res = await submitSimilarAnswer(similarId, answerText.value)
    result.value = res.data
    submitted.value = true
    if (res.data.mastery_status === 'passed') {
      message.success('恭喜！已掌握该知识点')
    } else {
      message.warning('未通过，建议重新复习后再试')
    }
  } catch (e) {
    message.error('提交失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    submitting.value = false
  }
}

function variantColor(type) {
  const map = { '根源变式': 'purple', '同类变式': 'blue', '基础铺垫': 'green', '简化原题': 'cyan', '进阶题': 'orange' }
  return map[type] || 'default'
}

onMounted(() => {
  loadDetail()
})
</script>

<style scoped>
.detail-card { border-radius: 12px; margin-bottom: 16px; }
.question-text { white-space: pre-wrap; line-height: 1.8; font-size: 16px; color: #333; }
.answer-text { white-space: pre-wrap; line-height: 1.8; color: #333; }
.json-pre { background: #f5f5f5; padding: 12px; border-radius: 8px; font-size: 12px; max-height: 300px; overflow: auto; }
.score-good { color: #52c41a; font-weight: 600; }
.score-bad { color: #ff4d4f; font-weight: 600; }
</style>
