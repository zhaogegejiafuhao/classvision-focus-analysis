<template>
  <div class="step-compose-ai">
    <div v-if="!store.examId" class="ai-compose-panel">
      <a-form layout="vertical" style="max-width: 640px">
        <a-form-item label="描述你的组卷需求" required>
          <a-textarea
            v-model:value="prompt"
            :rows="4"
            placeholder="例如：高数期中，5道单选3道大题，覆盖极限和积分，难度中等偏上"
          />
        </a-form-item>
        <a-row :gutter="16">
          <a-col :span="8">
            <a-form-item label="出题场景（可选）">
              <a-select v-model:value="scene" allow-clear placeholder="选择场景" style="width: 100%">
                <a-select-option value="sync">同步教学</a-select-option>
                <a-select-option value="quiz">阶段测试</a-select-option>
                <a-select-option value="midterm">期中考试</a-select-option>
                <a-select-option value="final">期末考试</a-select-option>
                <a-select-option value="contest">竞赛模拟</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>
        <a-button type="primary" size="large" block :loading="composing" @click="handleAICompose" style="margin-top: 8px">
          <template #icon><ThunderboltOutlined /></template>
          智能组卷
        </a-button>
        <p v-if="composing" style="text-align: center; color: #999; margin-top: 8px; font-size: 13px">
          🤖 AI 正在为你智能组卷，请耐心等待（约 10-30 秒）...
        </p>
      </a-form>
    </div>

    <div v-else class="ai-compose-done">
      <a-result status="success" title="AI 组卷完成" :sub-title="`共 ${store.reviewQuestionCount} 题，已进入审核确认环节`">
        <template #extra>
          <a-button type="primary" @click="goReview">进入审核确认</a-button>
        </template>
      </a-result>
    </div>

    <div class="step-actions">
      <a-button @click="goBack">
        上一步
      </a-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import { ThunderboltOutlined } from '@ant-design/icons-vue'
import { useExamComposeStore } from '@/stores/examCompose'
import { aiComposeExam } from '@/api/examTemplate'

const router = useRouter()
const store = useExamComposeStore()

const prompt = ref('')
const scene = ref(null)
const composing = ref(false)

async function handleAICompose() {
  if (!prompt.value.trim()) {
    message.error('请输入组卷需求描述')
    return
  }
  composing.value = true
  try {
    let finalPrompt = prompt.value
    if (scene.value) {
      const sceneMap = { sync: '同步教学', quiz: '阶段测试', midterm: '期中考试', final: '期末考试', contest: '竞赛模拟' }
      finalPrompt = `[${sceneMap[scene.value] || scene.value}] ${finalPrompt}`
    }
    const payload = {
      prompt: finalPrompt,
      template_id: store.templateId || null,
      classroom_id: store.classroomId || null,
      title: store.title || '',
      exam_type: store.examType,
    }
    const res = await aiComposeExam(payload)
    store.setAIResult(res.data)
    message.success(`AI 组卷成功！共 ${res.data.question_count} 题，请审核后发布`)
    // 自动跳转到审核页
    goReview()
  } catch (e) {
    const msg = e?.response?.data?.detail || 'AI 组卷失败，请检查 LLM 配置后重试'
    message.error(msg)
  } finally {
    composing.value = false
  }
}

function goReview() {
  store.setStep(2)
  router.push('/exam-compose/review')
}

function goBack() {
  store.setStep(0)
  router.push('/exam-compose')
}
</script>

<style scoped>
.step-compose-ai {
  padding: 0 8px;
}
.ai-compose-panel {
  max-width: 640px;
}
.ai-compose-done {
  text-align: center;
  padding: 24px;
}
.step-actions {
  margin-top: 24px;
}
</style>
