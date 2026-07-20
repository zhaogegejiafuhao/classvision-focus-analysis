<template>
  <a-tag :color="badgeColor" class="cv-pulse confidence-badge">
    置信度: {{ percentage }}% · {{ label }}
  </a-tag>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  confidence: { type: Number, default: 0.85 },
})

const percentage = computed(() => Math.round(props.confidence * 100))

const badgeColor = computed(() => {
  if (props.confidence >= 0.8) return 'green'
  if (props.confidence >= 0.6) return 'gold'
  return 'red'
})

const label = computed(() => {
  if (props.confidence >= 0.8) return '高'
  if (props.confidence >= 0.6) return '中'
  return '低'
})
</script>

<style scoped>
.confidence-badge {
  font-size: 13px;
  padding: 4px 12px;
  border-radius: 12px;
  font-weight: 600;
}
</style>
