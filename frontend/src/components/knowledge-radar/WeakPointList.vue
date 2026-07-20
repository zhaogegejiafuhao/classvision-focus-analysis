<template>
  <a-list :data-source="weakPoints" size="small" :split="true">
    <template #renderItem="{ item, index }">
      <a-list-item class="cv-tag-pop weak-point-item" :style="{ animationDelay: index * 80 + 'ms' }">
        <a-list-item-meta>
          <template #title>
            <span class="wp-name">{{ item.name }}</span>
            <a-tag v-if="item.weight" color="blue" size="small" style="margin-left: 8px; font-size: 11px">
              权重 {{ (item.weight * 100).toFixed(0) }}%
            </a-tag>
          </template>
          <template #description>
            <a-progress
              :percent="Math.round(item.score || 0)"
              :stroke-color="getProgressColor(item.score)"
              :show-info="true"
              size="small"
              :format="(p) => p + '%'"
            />
          </template>
        </a-list-item-meta>
      </a-list-item>
    </template>
  </a-list>
</template>

<script setup>
const props = defineProps({
  weakPoints: {
    type: Array,
    default: () => [],
  },
})

function getProgressColor(score) {
  if (score >= 70) return '#52c41a'
  if (score >= 40) return '#faad14'
  return '#ff4d4f'
}
</script>

<style scoped>
.weak-point-item {
  transition: all 0.3s ease;
}

.wp-name {
  font-weight: 600;
  color: #1a1a2e;
  font-size: 14px;
}
</style>
