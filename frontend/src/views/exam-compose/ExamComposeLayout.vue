<template>
  <div class="cv-page exam-compose-wizard">
    <a-page-header title="智能组卷" sub-title="AI 智能组卷 / 人工选题组卷" style="padding-bottom: 12px" />

    <div class="wizard-container">
      <!-- 步骤进度条 -->
      <a-steps :current="store.currentStep" class="wizard-steps" @change="handleStepChange">
        <a-step title="选择方式" />
        <a-step title="组卷操作" />
        <a-step title="审核发布" />
      </a-steps>

      <!-- 步骤内容 -->
      <div class="wizard-content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
import { watch, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useExamComposeStore } from '@/stores/examCompose'

const router = useRouter()
const route = useRoute()
const store = useExamComposeStore()

// 路由路径到步骤索引的映射
const stepRoutes = ['', '/compose', '/review']

// 监听路由变化同步步骤索引
watch(() => route.path, (path) => {
  const basePath = '/exam-compose'
  const relativePath = path.replace(basePath, '') || ''
  const stepIndex = stepRoutes.indexOf(relativePath)
  if (stepIndex >= 0 && stepIndex !== store.currentStep) {
    store.setStep(stepIndex)
  }
}, { immediate: true })

// 点击步骤条切换
function handleStepChange(step) {
  if (step <= store.currentStep || step === store.currentStep + 1) {
    if (step > store.currentStep && !store.canNextStep) return
    store.setStep(step)
    router.push(`/exam-compose${stepRoutes[step]}`)
  }
}

// 进入组卷页时重置状态
onMounted(() => {
  if (route.path === '/exam-compose') {
    store.reset()
  }
})
</script>

<style scoped>
.exam-compose-wizard {
  padding: 0 24px 24px;
}
.wizard-container {
  background: #fff;
  border-radius: 10px;
  padding: 24px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
}
.wizard-steps {
  margin-bottom: 24px;
}
.wizard-content {
  min-height: 400px;
}
</style>
