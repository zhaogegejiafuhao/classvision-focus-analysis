<template>
  <div class="difficulty-bar">
    <span class="diff-label">难度分布：</span>
    <span v-for="d in distribution" :key="d.level" class="diff-bar-seg" :style="{ width: d.percent + '%', background: d.color }">
      {{ d.label }} {{ d.count }}题
    </span>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  questions: { type: Array, default: () => [] },
})

const distribution = computed(() => {
  const dist = {}
  for (const q of props.questions) {
    const d = q.difficulty || 2
    dist[d] = (dist[d] || 0) + 1
  }
  const total = props.questions.length || 1
  const colors = { 1: '#52c41a', 2: '#73d13d', 3: '#faad14', 4: '#ff7a45', 5: '#ff4d4f' }
  const labels = { 1: '简单', 2: '较易', 3: '中等', 4: '较难', 5: '困难' }
  return Object.entries(dist).sort((a, b) => a[0] - b[0]).map(([level, count]) => ({
    level: Number(level),
    count,
    percent: Math.round(count / total * 100),
    color: colors[level] || '#ccc',
    label: labels[level] || `${level}星`,
  }))
})
</script>

<style scoped>
.difficulty-bar {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-bottom: 12px;
  background: #f8f9fc;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
}
.diff-label {
  color: #666;
  font-weight: 500;
  flex-shrink: 0;
}
.diff-bar-seg {
  text-align: center;
  font-size: 11px;
  color: #fff;
  padding: 2px 4px;
  border-radius: 3px;
  min-width: 40px;
}
</style>
