<template>
  <a-card title="批改设置" :bordered="false" class="settings-card">
    <a-form layout="vertical">
      <a-form-item :label="questionLabel" required>
        <a-textarea
          v-model:value="form.question"
          :rows="3"
          :placeholder="questionPlaceholder"
          show-count
          :maxlength="2000"
        />
      </a-form-item>

      <a-form-item :label="standardAnswerLabel">
        <a-textarea
          v-model:value="form.standardAnswer"
          :rows="2"
          :placeholder="standardAnswerPlaceholder"
          show-count
          :maxlength="1000"
        />
      </a-form-item>

      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-item label="满分值">
            <a-input-number
              v-if="totalScoreEditable"
              v-model:value="form.totalScore"
              :min="1"
              :max="100"
              style="width: 100%"
            />
            <a-input-number
              v-else
              :value="100"
              disabled
              style="width: 100%"
            />
          </a-form-item>
        </a-col>
        <a-col :span="12">
          <a-form-item label="提交ID">
            <a-input-number
              v-model:value="form.submissionId"
              :min="1"
              style="width: 100%"
              placeholder="学生提交ID"
            />
          </a-form-item>
        </a-col>
      </a-row>

      <a-form-item label="学生作答">
        <DualInputPanel :model-value="inputData" @update:model-value="onInputUpdate" />
      </a-form-item>

      <a-form-item>
        <a-button
          type="primary"
          block
          size="large"
          :loading="loading"
          @click="$emit('grade')"
        >
          <template #icon><ThunderboltOutlined /></template>
          开始批改
        </a-button>
      </a-form-item>
    </a-form>
  </a-card>
</template>

<script setup>
import { ThunderboltOutlined } from '@ant-design/icons-vue'
import DualInputPanel from '@/components/ai-grading/DualInputPanel.vue'

/**
 * AI 批改公共设置面板
 * 抽取自 AIGradingPage / AIEssayGradingPage 的左列设置表单。
 * form 与 inputData 通过对象引用共享（父组件传入 reactive 对象），
 * 子组件直接编辑其字段即可双向同步，无需 emit 整体更新。
 */
const props = defineProps({
  // 表单对象：{ question, standardAnswer, totalScore, submissionId }
  form: {
    type: Object,
    required: true,
  },
  // 输入数据对象：{ imageBase64, textContent }
  inputData: {
    type: Object,
    required: true,
  },
  questionLabel: {
    type: String,
    default: '题目',
  },
  questionPlaceholder: {
    type: String,
    default: '输入题目...',
  },
  standardAnswerLabel: {
    type: String,
    default: '标准答案',
  },
  standardAnswerPlaceholder: {
    type: String,
    default: '输入标准答案（可选）...',
  },
  // 满分值是否可编辑；false 时固定 100 且禁用（作文场景）
  totalScoreEditable: {
    type: Boolean,
    default: true,
  },
  // 开始批改按钮 loading 状态
  loading: {
    type: Boolean,
    default: false,
  },
})

defineEmits(['grade'])

// DualInputPanel 以整体对象 emit 更新，这里把新值属性写回共享的 inputData 引用，
// 保证父组件 reactive 对象同步（属性赋值而非整体替换，保留同一引用）
function onInputUpdate(val) {
  if (!val) return
  props.inputData.imageBase64 = val.imageBase64 ?? ''
  props.inputData.textContent = val.textContent ?? ''
}
</script>

<style scoped>
.settings-card {
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
}
</style>
