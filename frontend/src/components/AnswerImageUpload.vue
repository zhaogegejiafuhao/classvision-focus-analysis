<template>
  <div class="answer-image-upload">
    <div class="upload-area">
      <a-upload
        :before-upload="handleBeforeUpload"
        accept="image/jpeg,image/png,image/webp"
        :show-upload-list="false"
        :multiple="true"
      >
        <a-button size="small" :loading="uploading">
          <template #icon><CameraOutlined /></template>
          {{ required ? '拍照/上传答案图片' : '补充图片答案' }}
        </a-button>
      </a-upload>
      <span v-if="required && imageUrls.length === 0" class="upload-required-hint">
        请上传答案照片
      </span>
    </div>
    <div v-if="imageUrls.length" class="image-preview-list">
      <div v-for="(url, idx) in imageUrls" :key="idx" class="image-preview-item">
        <a-image :src="url" :width="120" :height="90" style="border-radius: 4px; object-fit: cover" />
        <a-button type="text" danger size="small" @click="removeImage(idx)" class="remove-btn">
          <template #icon><DeleteOutlined /></template>
        </a-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { CameraOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import { useImageUpload } from '@/composables/useImageUpload'

const props = defineProps({
  imageUrls: { type: Array, default: () => [] },
  required: { type: Boolean, default: false },
})

const emit = defineEmits(['update:imageUrls'])

const { uploading, uploadImage } = useImageUpload()

async function handleBeforeUpload(file) {
  const url = await uploadImage(file)
  if (url) {
    const newList = [...props.imageUrls, url]
    emit('update:imageUrls', newList)
  }
  return false  // 阻止默认上传行为
}

function removeImage(idx) {
  const newList = [...props.imageUrls]
  newList.splice(idx, 1)
  emit('update:imageUrls', newList)
}
</script>

<style scoped>
.answer-image-upload { margin-top: 4px; }
.upload-area { display: flex; align-items: center; gap: 8px; }
.upload-required-hint { color: #ff4d4f; font-size: 12px; }
.image-preview-list {
  display: flex; gap: 8px; flex-wrap: wrap;
  margin-top: 8px;
}
.image-preview-item {
  position: relative; display: inline-block;
}
.image-preview-item .remove-btn {
  position: absolute; top: -4px; right: -4px;
  background: rgba(255, 255, 255, 0.9); border-radius: 50%;
  min-width: 20px; width: 20px; height: 20px; padding: 0;
  display: flex; align-items: center; justify-content: center;
}
</style>
