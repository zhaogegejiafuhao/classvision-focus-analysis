<template>
  <div class="dual-input-panel">
    <a-radio-group v-model:value="mode" size="small" style="margin-bottom: 12px">
      <a-radio-button value="image">📷 图片上传</a-radio-button>
      <a-radio-button value="text">📝 文本粘贴</a-radio-button>
    </a-radio-group>

    <div :key="mode" class="cv-tag-pop">
      <!-- 图片上传模式 -->
      <div v-if="mode === 'image'">
        <a-upload-dragger
          :before-upload="handleImageUpload"
          :show-upload-list="false"
          accept="image/*"
          :multiple="false"
        >
          <div class="upload-hint">
            <p class="ant-upload-drag-icon">
              <inbox-outlined />
            </p>
            <p class="ant-upload-text">点击或拖拽上传学生手写答案图片</p>
            <p class="ant-upload-hint">支持 JPG / PNG / BMP 格式</p>
          </div>
        </a-upload-dragger>
        <div v-if="imagePreview" class="image-preview">
          <img :src="imagePreview" alt="预览" />
          <a-button type="link" danger size="small" @click="clearImage">移除图片</a-button>
        </div>
      </div>

      <!-- 文本粘贴模式 -->
      <div v-else>
        <a-textarea
          v-model:value="textContent"
          placeholder="粘贴学生答案文本..."
          :rows="6"
          show-count
          :maxlength="5000"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { InboxOutlined } from '@ant-design/icons-vue'

const props = defineProps({
  modelValue: {
    type: Object,
    default: () => ({ imageBase64: '', textContent: '' }),
  },
})

const emit = defineEmits(['update:modelValue'])

const mode = ref('text')
const imageBase64 = ref(props.modelValue.imageBase64 || '')
const textContent = ref(props.modelValue.textContent || '')
const imagePreview = ref('')

function handleImageUpload(file) {
  const reader = new FileReader()
  reader.onload = (e) => {
    const base64 = e.target.result.split(',')[1]
    imageBase64.value = base64
    imagePreview.value = e.target.result
    emitUpdate()
  }
  reader.readAsDataURL(file)
  return false // 阻止自动上传
}

function clearImage() {
  imageBase64.value = ''
  imagePreview.value = ''
  emitUpdate()
}

function emitUpdate() {
  emit('update:modelValue', {
    imageBase64: imageBase64.value,
    textContent: textContent.value,
  })
}

watch(textContent, () => emitUpdate())
watch(imageBase64, () => emitUpdate())

watch(
  () => props.modelValue,
  (val) => {
    if (val.imageBase64 !== undefined) imageBase64.value = val.imageBase64
    if (val.textContent !== undefined) textContent.value = val.textContent
  }
)
</script>

<style scoped>
.dual-input-panel {
  margin-top: 8px;
}

.upload-hint {
  padding: 16px 0;
  text-align: center;
}

.image-preview {
  margin-top: 8px;
  text-align: center;
}

.image-preview img {
  max-width: 100%;
  max-height: 200px;
  border-radius: 8px;
  border: 1px solid #e8e8e8;
}
</style>