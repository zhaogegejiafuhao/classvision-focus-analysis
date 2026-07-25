<template>
  <a-card size="small" class="selected-card">
    <template #title>
      <span>📝 试题篮</span>
    </template>
    <template #extra>
      <span class="selected-stats">{{ questions.length }} 题 · {{ totalScore }} 分</span>
    </template>

    <div v-if="questions.length === 0" class="empty-selected">
      <div class="empty-icon">📋</div>
      <div class="empty-text">暂无题目</div>
      <div class="empty-hint">请从题库中勾选并加入</div>
    </div>
    <div v-else>
      <div v-for="group in questionGroups" :key="group.type" class="selected-group">
        <div class="selected-group-header">
          <a-tag :color="getTypeColor(group.type)" size="small">{{ getTypeText(group.type) }}</a-tag>
          <span class="selected-group-count">{{ group.items.length }}题 · {{ group.totalScore }}分</span>
        </div>
        <div v-for="(item, idx) in group.items" :key="item.id || idx" class="selected-item">
          <div class="selected-item-left">
            <span class="selected-order">{{ item.globalIndex }}</span>
            <LatexText :content="item.content" class="selected-content" />
          </div>
          <div class="selected-item-right">
            <a-input-number
              v-model:value="item.scoreOverride"
              :min="1"
              :max="100"
              size="small"
              style="width: 60px"
            />
            <span class="score-unit">分</span>
            <a-button type="text" size="small" @click="$emit('moveUp', item.globalIndex)" :disabled="item.globalIndex <= 1">
              <template #icon><UpOutlined /></template>
            </a-button>
            <a-button type="text" size="small" @click="$emit('moveDown', item.globalIndex)" :disabled="item.globalIndex >= questions.length">
              <template #icon><DownOutlined /></template>
            </a-button>
            <a-button type="text" danger size="small" @click="$emit('remove', item.globalIndex - 1)" class="remove-btn">
              <template #icon><CloseOutlined /></template>
            </a-button>
          </div>
        </div>
      </div>

      <div v-if="totalScore !== (templateScore || 0) && templateScore" class="score-warning-bar">
        <a-alert type="warning" show-icon :message="`当前总分 ${totalScore} 分与模板设定 ${templateScore} 分不一致`" style="margin-top: 8px" />
      </div>
    </div>

    <div v-if="questions.length > 0" class="selected-footer">
      <a-button type="link" danger size="small" @click="$emit('clear')">清空已选</a-button>
    </div>
  </a-card>
</template>

<script setup>
import { computed } from 'vue'
import { UpOutlined, DownOutlined, CloseOutlined } from '@ant-design/icons-vue'
import LatexText from '@/components/LatexText.vue'

const props = defineProps({
  questions: { type: Array, default: () => [] },
  templateScore: { type: Number, default: 0 },
})

defineEmits(['remove', 'moveUp', 'moveDown', 'clear'])

const totalScore = computed(() =>
  props.questions.reduce((sum, q) => sum + (q.scoreOverride || q.score), 0)
)

const questionGroups = computed(() => {
  const typeOrder = ['single', 'multi', 'judge', 'fill', 'essay']
  const groups = {}
  let globalIdx = 1
  for (const q of props.questions) {
    q.globalIndex = globalIdx++
    if (!groups[q.type]) {
      groups[q.type] = { type: q.type, items: [], totalScore: 0 }
    }
    groups[q.type].items.push(q)
    groups[q.type].totalScore += (q.scoreOverride || q.score)
  }
  return typeOrder.filter(t => groups[t]).map(t => groups[t])
})

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

function getTypeColor(type) {
  return { single: 'blue', multi: 'purple', judge: 'green', fill: 'orange', essay: 'red' }[type] || 'default'
}
</script>

<style scoped>
.selected-card :deep(.ant-card-body) {
  padding: 10px 14px;
  max-height: 380px;
  overflow-y: auto;
}
.selected-card :deep(.ant-card-head) {
  min-height: 36px;
  padding: 0 14px;
}
.selected-card :deep(.ant-card-head-title) {
  padding: 8px 0;
  font-size: 13px;
}
.selected-stats {
  font-size: 12px;
  color: #3751FE;
  font-weight: 600;
}
.empty-selected {
  text-align: center;
  padding: 16px 0;
}
.empty-icon { font-size: 28px; margin-bottom: 6px; }
.empty-text { font-size: 13px; color: #999; font-weight: 500; }
.empty-hint { font-size: 11px; color: #ccc; margin-top: 2px; }
.selected-group { margin-bottom: 8px; }
.selected-group-header {
  display: flex; align-items: center; gap: 6px;
  margin-bottom: 4px; padding-bottom: 4px;
  border-bottom: 1px dashed #e8e8e8;
}
.selected-group-count { color: #555; font-size: 12px; font-weight: 500; }
.selected-item {
  display: flex; justify-content: space-between; align-items: center;
  padding: 4px 8px; background: #f8f9fc; border-radius: 6px;
  border: 1px solid #eef0f5; transition: background 0.15s; margin-bottom: 3px;
}
.selected-item:hover { background: #f0f2fa; }
.selected-item-left { display: flex; align-items: center; gap: 6px; min-width: 0; flex: 1; }
.selected-order {
  width: 18px; height: 18px; border-radius: 50%;
  background: #3751FE; color: #fff; font-size: 10px; font-weight: 600;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.selected-content {
  font-size: 12px; color: #333;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 130px;
}
.selected-item-right { display: flex; align-items: center; gap: 2px; flex-shrink: 0; }
.score-unit { font-size: 11px; color: #aaa; }
.remove-btn { padding: 0 4px !important; }
.score-warning-bar { margin-top: 6px; }
.selected-footer {
  margin-top: 6px; padding-top: 6px;
  border-top: 1px solid #f0f0f0; text-align: right;
}
</style>
