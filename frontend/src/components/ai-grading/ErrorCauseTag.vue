<template>
  <div class="error-cause-tag" v-if="errorCause && errorCause !== 'none'">
    <div class="cause-section">
      <span class="section-label">错因判定：</span>
      <a-tag :color="causeColorMap[errorCause] || 'default'" class="cv-tag-pop cause-tag">
        {{ errorCause }}
      </a-tag>
      <a-tag v-if="errorType && errorType !== 'none'" color="default" class="cv-tag-pop" style="animation-delay: 60ms">
        {{ errorTypeLabel }}
      </a-tag>
    </div>
    <div v-if="knowledgePoints.length" class="kp-section">
      <span class="section-label">涉及知识点：</span>
      <a-tag
        v-for="(kp, i) in knowledgePoints"
        :key="i"
        color="blue"
        class="cv-tag-pop kp-tag"
        :style="{ animationDelay: (120 + i * 80) + 'ms' }"
      >
        {{ kp }}
      </a-tag>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  errorType: { type: String, default: '' },
  errorCause: { type: String, default: '' },
  knowledgePoints: { type: Array, default: () => [] },
})

const causeColorMap = {
  '计算粗心': 'blue',
  '概念混淆': 'purple',
  '审题不清': 'orange',
  '辅助线缺失': 'cyan',
  '逻辑跳步': 'magenta',
  '知识缺失': 'red',
  '素材匮乏': 'volcano',
  '逻辑断层': 'geekblue',
  '修辞单一': 'lime',
  '偏题跑题': 'orange',
  '书写潦草': 'gold',
}

const errorTypeLabel = computed(() => {
  const map = {
    calculation_error: '计算错误',
    concept_error: '概念错误',
    process_error: '过程错误',
    none: '',
  }
  return map[props.errorType] || props.errorType
})
</script>

<style scoped>
.error-cause-tag {
  padding: 8px 0;
}

.cause-section,
.kp-section {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 6px;
}

.section-label {
  font-size: 13px;
  color: #666;
  font-weight: 500;
}

.cause-tag {
  font-weight: 600;
  font-size: 13px;
}

.kp-tag {
  font-size: 12px;
}
</style>