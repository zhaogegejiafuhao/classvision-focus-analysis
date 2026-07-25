<template>
  <StepComposeAI v-if="store.method === 'ai'" />
  <StepComposeManual v-else-if="store.method === 'manual'" />
  <div v-else class="no-method">
    <a-result status="warning" title="请先选择组卷方式" sub-title="请返回上一步选择 AI 组卷或人工组卷">
      <template #extra>
        <a-button type="primary" @click="goBack">返回选择方式</a-button>
      </template>
    </a-result>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useExamComposeStore } from '@/stores/examCompose'
import StepComposeAI from './StepComposeAI.vue'
import StepComposeManual from './StepComposeManual.vue'

const router = useRouter()
const store = useExamComposeStore()

function goBack() {
  store.setStep(0)
  router.push('/exam-compose')
}
</script>

<style scoped>
.no-method {
  text-align: center;
  padding: 24px;
}
</style>
