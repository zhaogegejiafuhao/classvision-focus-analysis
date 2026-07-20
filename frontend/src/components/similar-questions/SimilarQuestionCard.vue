<template>
  <a-card hoverable size="small" class="cv-bounce-in similar-question-card">
    <div class="sq-header">
      <span class="sq-title">{{ question.title }}</span>
      <a-tag v-if="question.difficulty" :color="difficultyColor" size="small">
        {{ question.difficulty }}
      </a-tag>
    </div>
    <div v-if="question.options?.length" class="sq-options">
      <div v-for="(opt, i) in question.options" :key="i" class="sq-option">
        {{ String.fromCharCode(65 + i) }}. {{ opt }}
      </div>
    </div>
    <a-collapse v-if="question.answer" ghost size="small">
      <a-collapse-panel header="查看答案">
        <div class="sq-answer">{{ question.answer }}</div>
      </a-collapse-panel>
    </a-collapse>
  </a-card>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  question: {
    type: Object,
    default: () => ({ title: '', options: [], answer: '', difficulty: '' }),
  },
})

const difficultyColor = computed(() => {
  const map = {
    '简单': 'green',
    '中等': 'blue',
    '困难': 'red',
    '基础': 'green',
    '提高': 'blue',
    '挑战': 'red',
  }
  return map[props.question.difficulty] || 'default'
})
</script>

<style scoped>
.similar-question-card {
  height: 100%;
}

.sq-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 8px;
  margin-bottom: 8px;
}

.sq-title {
  font-size: 14px;
  font-weight: 600;
  color: #1a1a2e;
  line-height: 1.5;
  flex: 1;
}

.sq-options {
  margin: 8px 0;
  padding-left: 12px;
}

.sq-option {
  font-size: 13px;
  color: #555;
  line-height: 1.8;
}

.sq-answer {
  font-size: 13px;
  color: #3751FE;
  padding: 4px 8px;
  background: rgba(55, 81, 254, 0.05);
  border-radius: 4px;
}
</style>
