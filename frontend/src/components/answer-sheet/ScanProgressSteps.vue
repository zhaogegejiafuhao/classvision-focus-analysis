<template>
  <div class="scan-progress">
    <a-steps :current="current" :status="status" size="small" style="margin: 16px 0">
      <a-step title="上传扫描件" description="接收整卷图片" />
      <a-step title="模板切分" description="按 bbox 切分各题" />
      <a-step title="AI 识别+批改" description="气泡检测/OCR" />
      <a-step title="生成报告" description="汇总批改结果" />
    </a-steps>

    <div v-if="status === 'process'" class="loading-text">
      <a-spin size="small" />
      <span>{{ stepHint }}</span>
    </div>
    <div v-else-if="status === 'error'" class="error-text">
      <CloseCircleOutlined /> 扫描批改失败，请查看错误提示
    </div>
    <div v-else-if="status === 'finish'" class="success-text">
      <CheckCircleOutlined /> 批改完成，请查看下方报告
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { CheckCircleOutlined, CloseCircleOutlined } from '@ant-design/icons-vue'

const props = defineProps({
  current: { type: Number, default: 0 },
  status: { type: String, default: 'process' }, // process | finish | error
})

const stepHints = [
  '正在上传整卷扫描件...',
  '正在按试卷模板切分各题区域...',
  '正在 AI 识别答案并批改（可能耗时较长）...',
  '正在生成批改报告...',
]

const stepHint = computed(() => stepHints[props.current] || '处理中...')
</script>

<style scoped>
.scan-progress {
  background: #fafafa;
  padding: 16px;
  border-radius: 8px;
  margin: 12px 0;
}

.loading-text {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #3751FE;
  font-size: 13px;
  justify-content: center;
}

.error-text {
  color: #ef4444;
  font-size: 13px;
  text-align: center;
}

.success-text {
  color: #16a34a;
  font-size: 13px;
  text-align: center;
}
</style>
