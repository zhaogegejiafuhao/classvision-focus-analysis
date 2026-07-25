import { ref } from 'vue'
import { message } from 'ant-design-vue'
import api from '@/api/index'

/**
 * 答案图片上传 composable
 * 调用 POST /exams/answers/upload-image API
 */
export function useImageUpload() {
  const uploading = ref(false)

  async function uploadImage(file) {
    // 前端预校验
    const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp']
    if (!ALLOWED_TYPES.includes(file.type)) {
      message.error('仅支持 JPG/PNG/WebP 格式图片')
      return null
    }
    if (file.size > 10 * 1024 * 1024) {
      message.error('图片不能超过 10MB')
      return null
    }

    uploading.value = true
    try {
      const formData = new FormData()
      formData.append('file', file)
      const res = await api.post('/exams/answers/upload-image', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      return res.data.url  // 返回图片 URL
    } catch (e) {
      message.error('图片上传失败')
      return null
    } finally {
      uploading.value = false
    }
  }

  return { uploading, uploadImage }
}
