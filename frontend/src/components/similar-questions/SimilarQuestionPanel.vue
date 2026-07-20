<template>
  <div class="similar-question-panel">
    <a-spin :spinning="loading">
      <template v-if="questions.length">
        <div v-for="(q, i) in questions" :key="i" class="similar-question-item cv-dimension-reveal" :style="{ animationDelay: (i * 100) + 'ms' }">
          <a-card size="small" :title="`练习 ${i + 1}`" class="question-card">
            <template #extra>
              <a-tag v-if="q.difficulty" :color="difficultyColor(q.difficulty)">{{ q.difficulty }}</a-tag>
              <a-tag v-if="q.variant_type" color="blue">{{ q.variant_type }}</a-tag>
            </template>
            <div class="question-text">{{ q.question_text }}</div>
            <a-collapse size="small" :bordered="false" style="margin-top: 8px">
              <a-collapse-panel key="answer" header="查看参考答案">
                <div class="answer-text">{{ q.standard_answer }}</div>
              </a-collapse-panel>
            </a-collapse>
          </a-card>
        </div>
      </template>
      <a-empty v-else-if="!loading" description="暂无相似练习题" />
    </a-spin>

    <a-button
      v-if="!loading && questions.length === 0"
      type="primary"
      size="small"
      @click="generateQuestions"
      style="margin-top: 8px"
    >
      生成相似练习
    </a-button>
    <a-button
      v-if="!loading && questions.length > 0"
      size="small"
      @click="generateQuestions"
      style="margin-top: 8px"
    >
      换一批
    </a-button>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { generateSimilarQuestions } from '@/api/similarQuestions'
import { message } from 'ant-design-vue'

const props = defineProps({
  question: { type: String, default: '' },
  knowledgePoints: { type: Array, default: () => [] },
  errorType: { type: String, default: '' },
  standardAnswer: { type: String, default: '' },
  tier: { type: String, default: '中等生' },
  count: { type: Number, default: 3 },
})

const questions = ref([])
const loading = ref(false)

async function generateQuestions() {
  if (!props.knowledgePoints.length && !props.errorType) {
    message.warning('缺少知识点或错因信息，无法生成相似题')
    return
  }
  loading.value = true
  try {
    const res = await generateSimilarQuestions({
      question: props.question,
      knowledge_points: props.knowledgePoints,
      error_type: props.errorType,
      standard_answer: props.standardAnswer,
      tier: props.tier,
      count: props.count,
    })
    questions.value = res.data?.questions || []
  } catch (e) {
    message.error('生成相似题失败')
  } finally {
    loading.value = false
  }
}

function difficultyColor(difficulty) {
  const map = { '基础': 'green', '简化': 'cyan', '中等': 'blue', '进阶': 'orange', '较难': 'red' }
  return map[difficulty] || 'default'
}

onMounted(() => {
  if (props.knowledgePoints.length || props.errorType) {
    generateQuestions()
  }
})
</script>

<style scoped>
.similar-question-panel {
  padding: 4px 0;
}

.similar-question-item {
  margin-bottom: 12px;
}

.question-card {
  border-left: 3px solid #3751FE;
}

.question-text {
  font-size: 14px;
  line-height: 1.8;
  color: #333;
  white-space: pre-wrap;
}

.answer-text {
  font-size: 13px;
  line-height: 1.7;
  color: #555;
  white-space: pre-wrap;
  padding: 8px;
  background: #f6ffed;
  border-radius: 4px;
}
</style>
