<template>
  <a-modal
    :open="open"
    title="选择替换题目"
    width="700px"
    :footer="null"
    @cancel="$emit('update:open', false)"
  >
    <div v-if="candidates.length === 0" style="text-align: center; padding: 24px; color: #999">
      暂无候选题目，请调整筛选条件
    </div>
    <div v-else class="swap-candidates-list">
      <div v-for="c in candidates" :key="c.id" class="swap-candidate-item" @click="$emit('select', c)">
        <div class="swap-candidate-left">
          <a-tag :color="getTypeColor(c.type)" size="small">{{ getTypeText(c.type) }}</a-tag>
          <span v-for="i in (c.difficulty || 2)" :key="i" style="color: #faad14; font-size: 10px">★</span>
          <LatexText :content="c.content" />
        </div>
        <div class="swap-candidate-right">
          <span style="color: #3751FE; font-weight: 600">{{ c.score }}分</span>
          <a-tag v-if="c.source" :color="c.source === 'AI生成' ? 'orange' : 'green'" size="small">{{ c.source }}</a-tag>
        </div>
      </div>
    </div>
  </a-modal>
</template>

<script setup>
import LatexText from '@/components/LatexText.vue'

defineProps({
  open: { type: Boolean, default: false },
  candidates: { type: Array, default: () => [] },
})

defineEmits(['update:open', 'select'])

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

function getTypeColor(type) {
  return { single: 'blue', multi: 'purple', judge: 'green', fill: 'orange', essay: 'red' }[type] || 'default'
}
</script>

<style scoped>
.swap-candidates-list {
  display: flex; flex-direction: column; gap: 6px;
}
.swap-candidate-item {
  display: flex; justify-content: space-between; align-items: center;
  padding: 8px 12px; background: #f8f9fc; border-radius: 6px;
  cursor: pointer; transition: background 0.2s; border: 1px solid #eef0f5;
}
.swap-candidate-item:hover { background: #e8f4f8; border-color: #3751FE; }
.swap-candidate-left {
  display: flex; align-items: center; gap: 6px; font-size: 13px;
  min-width: 0; overflow: hidden; text-overflow: ellipsis;
}
.swap-candidate-right {
  display: flex; align-items: center; gap: 6px; flex-shrink: 0;
}
</style>
