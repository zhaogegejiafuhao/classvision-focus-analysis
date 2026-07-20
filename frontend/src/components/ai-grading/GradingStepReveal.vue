<template>
  <div class="grading-step-reveal" :class="{ 'cv-step-reveal': isVisible }">
    <!-- 步骤标题 -->
    <div class="step-header">
      <span class="step-badge" :class="{ 'step-active': isVisible, 'step-pending': !isVisible }">
        {{ isVisible ? stepIndex + 1 : '…' }}
      </span>
      <span class="step-title">{{ title }}</span>
    </div>

    <!-- 步骤内容 -->
    <div v-if="isVisible" class="step-content">
      <slot />
    </div>
    <div v-else class="step-skeleton">
      <a-skeleton active :paragraph="{ rows: 2 }" :title="false" />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  stepIndex: { type: Number, required: true },
  currentStepIndex: { type: Number, default: -1 },
  title: { type: String, default: '' },
})

const isVisible = computed(() => props.stepIndex <= props.currentStepIndex)
</script>

<style scoped>
.grading-step-reveal {
  padding: 16px;
  margin-bottom: 12px;
  border: 1px solid #f0f0f0;
  border-radius: 8px;
  background: #fafafa;
  transition: all 0.3s ease;
}

.grading-step-reveal.cv-step-reveal {
  background: #fff;
  border-color: #e6e6e6;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
}

.step-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

.step-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  font-size: 14px;
  font-weight: 700;
  transition: all 0.3s ease;
}

.step-active {
  background: linear-gradient(135deg, #3751fe, #5566ff);
  color: #fff;
  box-shadow: 0 2px 8px rgba(55, 81, 254, 0.3);
}

.step-pending {
  background: #e8e8e8;
  color: #999;
}

.step-title {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a2e;
}

.step-content {
  padding-left: 38px;
}

.step-skeleton {
  padding-left: 38px;
  opacity: 0.5;
}
</style>
