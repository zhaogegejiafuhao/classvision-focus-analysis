<template>
  <div class="correction-form">
    <a-form layout="vertical">
      <a-form-item label="订正内容" required>
        <a-textarea
          v-model:value="correctionText"
          placeholder="输入订正后的解答过程..."
          :rows="4"
          show-count
          :maxlength="3000"
        />
      </a-form-item>
      <a-form-item label="订正图片（可选）">
        <a-upload
          :before-upload="handleImageUpload"
          :show-upload-list="false"
          accept="image/*"
        >
          <a-button size="small">
            📷 上传订正图片
          </a-button>
        </a-upload>
        <div v-if="imagePreview" class="correction-preview">
          <img :src="imagePreview" alt="订正图片" />
          <a-button type="link" danger size="small" @click="clearImage">移除</a-button>
        </div>
      </a-form-item>
      <a-button type="primary" @click="handleSubmit" :loading="submitting" :disabled="!correctionText.trim()">
        提交订正
      </a-button>
    </a-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { submitCorrection } from '@/api/correction'
import { message } from 'ant-design-vue'

const props = defineProps({
  submissionId: { type: Number, required: true },
})

const emit = defineEmits(['submitted'])

const correctionText = ref('')
const imageBase64 = ref('')
const imagePreview = ref('')
const submitting = ref(false)

function handleImageUpload(file) {
  const reader = new FileReader()
  reader.onload = (e) => {
    imageBase64.value = e.target.result.split(',')[1]
    imagePreview.value = e.target.result
  }
  reader.readAsDataURL(file)
  return false
}

function clearImage() {
  imageBase64.value = ''
  imagePreview.value = ''
}

async function handleSubmit() {
  if (!correctionText.value.trim()) {
    message.warning('请输入订正内容')
    return
  }
  submitting.value = true
  try {
    const corrections = [{
      question_id: `sub_${props.submissionId}`,
      content: correctionText.value,
    }]
    if (imageBase64.value) {
      corrections[0].image_base64 = imageBase64.value
    }
    await submitCorrection({
      submission_id: props.submissionId,
      corrections,
    })
    message.success('订正已提交')
    emit('submitted')
  } catch (e) {
    message.error(e.response?.data?.detail || '提交订正失败')
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.correction-form {
  margin-top: 8px;
}

.correction-preview {
  margin-top: 8px;
  text-align: center;
}

.correction-preview img {
  max-width: 100%;
  max-height: 150px;
  border-radius: 6px;
  border: 1px solid #e8e8e8;
}
</style>
