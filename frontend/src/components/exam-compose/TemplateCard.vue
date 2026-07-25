<template>
  <a-card size="small" class="template-card">
    <template #title>
      <span>📋 试卷模板</span>
    </template>
    <template #extra>
      <a-button type="link" size="small" @click="$emit('createTemplate')">
        <template #icon><PlusOutlined /></template>
        新建
      </a-button>
    </template>
    <a-select
      :value="modelValue"
      allow-clear
      placeholder="选择模板（可选，软约束）"
      style="width: 100%"
      @change="$emit('update:modelValue', $event)"
    >
      <a-select-option v-for="t in templates" :key="t.id" :value="t.id">
        <span>{{ t.name }}</span>
        <a-tag v-if="t.is_builtin" color="blue" style="margin-left: 6px; font-size: 10px">内置</a-tag>
      </a-select-option>
    </a-select>

    <template v-if="currentTemplate">
      <div class="template-info">
        <div class="template-row">
          <span class="label">总分</span>
          <span class="value">{{ currentTemplate.total_score }} 分</span>
        </div>
        <div class="template-row">
          <span class="label">时长</span>
          <span class="value">{{ currentTemplate.duration }} 分钟</span>
        </div>
        <div v-if="currentTemplate.description" class="template-desc">{{ currentTemplate.description }}</div>
      </div>
      <div class="template-structure">
        <div v-for="sec in currentTemplate.structure" :key="sec.type + sec.count" class="structure-row">
          <a-tag size="small">{{ getTypeText(sec.type) }}</a-tag>
          <span class="structure-count">{{ sec.count }}题 × {{ sec.score_per }}分</span>
          <span v-if="sec.knowledge && sec.knowledge.length" class="structure-knowledge">
            {{ sec.knowledge.join('、') }}
          </span>
        </div>
      </div>
      <div class="template-actions">
        <a-button
          v-if="!currentTemplate.is_builtin"
          type="link"
          danger
          size="small"
          @click="$emit('deleteTemplate', currentTemplate.id)"
        >
          删除此模板
        </a-button>
      </div>
    </template>
  </a-card>
</template>

<script setup>
import { computed } from 'vue'
import { PlusOutlined } from '@ant-design/icons-vue'

const props = defineProps({
  modelValue: { type: [Number, null], default: null },
  templates: { type: Array, default: () => [] },
})

const emit = defineEmits(['update:modelValue', 'createTemplate', 'deleteTemplate'])

const currentTemplate = computed(() => {
  if (!props.modelValue) return null
  return props.templates.find(t => t.id === props.modelValue) || null
})

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}
</script>

<style scoped>
.template-card :deep(.ant-card-body) {
  padding: 12px 14px;
}
.template-card :deep(.ant-card-head) {
  min-height: 36px;
  padding: 0 14px;
}
.template-card :deep(.ant-card-head-title) {
  padding: 8px 0;
  font-size: 13px;
}
.template-info {
  margin-top: 10px;
}
.template-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
  font-size: 13px;
}
.template-row .label {
  color: #999;
  width: 36px;
  flex-shrink: 0;
}
.template-row .value {
  color: #333;
  font-weight: 500;
}
.template-desc {
  font-size: 12px;
  color: #888;
  margin-top: 4px;
  line-height: 1.4;
}
.template-structure {
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px dashed #e8e8e8;
}
.structure-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
  font-size: 12px;
}
.structure-count {
  color: #555;
  font-weight: 500;
}
.structure-knowledge {
  color: #aaa;
  font-size: 11px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 120px;
}
.template-actions {
  margin-top: 6px;
}
</style>
