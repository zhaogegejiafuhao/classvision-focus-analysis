<template>
  <div class="invite-page">
    <a-alert
      v-if="currentRole === 'student'"
      message="无访问权限"
      description="邀请成员功能仅限教师和管理员使用"
      type="warning"
      show-icon
      style="margin: 40px 0"
    />

    <template v-else>
      <a-page-header title="邀请成员" sub-title="快速注册学生人脸信息，加入课堂考勤系统" style="padding: 0 0 20px 0" />

      <a-row :gutter="24">
        <a-col :span="14">
          <a-card title="快速注册" size="small">
            <a-form layout="vertical">
              <a-form-item label="姓名" required>
                <a-input v-model:value="form.name" placeholder="请输入真实姓名" />
              </a-form-item>

              <a-form-item v-if="currentRole === 'admin'" label="注册角色">
                <a-radio-group v-model:value="form.role">
                  <a-radio value="student">学生</a-radio>
                  <a-radio value="teacher">教师</a-radio>
                </a-radio-group>
              </a-form-item>

              <a-form-item label="人脸照片" required>
                <div class="capture-area">
                  <div v-if="!cameraActive && !capturedImage" class="capture-placeholder">
                    <CameraOutlined style="font-size: 48px; color: #bfbfbf" />
                    <p style="margin-top: 8px; color: #8c8c8c">点击下方按钮开启摄像头拍照</p>
                  </div>

                  <video v-if="cameraActive" ref="videoEl" class="capture-preview" autoplay playsinline></video>

                  <div v-if="capturedImage" class="captured-wrap">
                    <img :src="capturedImage" class="capture-preview-img" alt="captured" />
                  </div>

                  <a-space style="margin-top: 12px">
                    <a-button v-if="!cameraActive && !capturedImage" type="primary" @click="startCamera">
                      <template #icon><CameraOutlined /></template>
                      开启摄像头
                    </a-button>
                    <a-button v-if="cameraActive" type="primary" @click="capture">拍照</a-button>
                    <a-button v-if="capturedImage" @click="retake">重新拍照</a-button>
                    <a-button v-if="cameraActive" @click="stopCamera">取消</a-button>
                  </a-space>
                </div>
              </a-form-item>

              <a-form-item>
                <a-button type="primary" block @click="handleRegister" :loading="registering" :disabled="!form.name || !capturedImage">
                  确认注册
                </a-button>
              </a-form-item>
            </a-form>
          </a-card>

          <a-card title="注册须知" size="small" style="margin-top: 16px">
            <ul class="tips-list">
              <li>请确保照片中人脸清晰、正面、光线充足</li>
              <li>避免佩戴口罩、墨镜等遮挡物</li>
              <li>每人仅需注册一次，系统会自动检测重复</li>
              <li>注册成功后，学生即可在课堂中被自动识别</li>
              <li v-if="currentRole === 'admin'">管理员可注册教师和学生，教师仅能注册学生</li>
            </ul>
          </a-card>
        </a-col>

        <a-col :span="10">
          <a-card size="small">
            <template #title>最近注册成员</template>
            <template #extra>
              <a-button type="text" size="small" @click="loadMembers" :loading="membersLoading">刷新</a-button>
            </template>

            <a-spin :spinning="membersLoading && members.length === 0">
              <a-empty v-if="members.length === 0" description="暂无注册成员" />

              <a-list v-else :data-source="members" size="small">
                <template #renderItem="{ item: m }">
                  <a-list-item>
                    <a-list-item-meta>
                      <template #avatar>
                        <a-avatar :style="{ background: avatarColor(m.role) }">
                          {{ (m.name || '?').charAt(0) }}
                        </a-avatar>
                      </template>
                      <template #title>
                        <span>{{ m.name }}</span>
                        <a-tag :color="m.role === 'teacher' ? 'blue' : 'green'" size="small" style="margin-left: 8px">
                          {{ roleLabel(m.role) }}
                        </a-tag>
                      </template>
                      <template #description>
                        <span v-if="m.username">@{{ m.username }} · </span>
                        {{ formatTime(m.created_at) }}
                      </template>
                    </a-list-item-meta>
                  </a-list-item>
                </template>
              </a-list>

              <div v-if="members.length > 0" style="text-align: center; margin-top: 12px">
                <a-button type="link" @click="goToPersons">查看全部成员 →</a-button>
              </div>
            </a-spin>
          </a-card>
        </a-col>
      </a-row>
    </template>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import api from '@/api'
import { message } from 'ant-design-vue'
import { CameraOutlined } from '@ant-design/icons-vue'

const router = useRouter()
const userStore = useUserStore()
const currentRole = computed(() => userStore.role || 'teacher')

const form = ref({
  name: '',
  role: 'student',
})

const videoEl = ref(null)
let stream = null
const cameraActive = ref(false)
const capturedImage = ref('')
const registering = ref(false)

const members = ref([])
const membersLoading = ref(false)

async function loadMembers() {
  membersLoading.value = true
  try {
    const filterRole = currentRole.value === 'teacher' ? '?role=student' : ''
    const res = await api.get(`/persons${filterRole}`)
    members.value = (res.data || []).slice(0, 20)
  } catch {
    message.error('加载成员列表失败')
  } finally {
    membersLoading.value = false
  }
}

async function startCamera() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: { width: 640, height: 480 } })
    cameraActive.value = true
    setTimeout(() => {
      if (videoEl.value && stream) {
        videoEl.value.srcObject = stream
      }
    }, 100)
  } catch (e) {
    message.error('无法访问摄像头：' + (e.message || '请检查权限设置'))
  }
}

function stopCamera() {
  if (stream) {
    stream.getTracks().forEach(t => t.stop())
    stream = null
  }
  cameraActive.value = false
}

function capture() {
  if (!videoEl.value) return
  const canvas = document.createElement('canvas')
  canvas.width = videoEl.value.videoWidth || 640
  canvas.height = videoEl.value.videoHeight || 480
  const ctx = canvas.getContext('2d')
  ctx.drawImage(videoEl.value, 0, 0)
  capturedImage.value = canvas.toDataURL('image/jpeg', 0.9)
  stopCamera()
}

function retake() {
  capturedImage.value = ''
  startCamera()
}

async function handleRegister() {
  if (!form.value.name.trim()) {
    message.warning('请输入姓名')
    return
  }
  if (!capturedImage.value) {
    message.warning('请先拍照采集人脸')
    return
  }

  registering.value = true
  try {
    const base64Data = capturedImage.value.split(',')[1]
    const formData = new FormData()
    formData.append('name', form.value.name.trim())
    formData.append('role', form.value.role)
    formData.append('image_data', base64Data)

    await api.post('/persons/register', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })

    message.success(`${form.value.name} 注册成功`)
    form.value.name = ''
    capturedImage.value = ''
    await loadMembers()
  } catch (e) {
    const detail = e.response?.data?.detail || '注册失败'
    message.error(detail)
  } finally {
    registering.value = false
  }
}

function roleLabel(role) {
  if (role === 'teacher') return '教师'
  if (role === 'admin') return '管理员'
  return '学生'
}

function avatarColor(role) {
  if (role === 'teacher') return '#3751FE'
  if (role === 'admin') return '#a855f7'
  return '#52c41a'
}

function formatTime(timeStr) {
  if (!timeStr) return ''
  const d = new Date(timeStr)
  const now = new Date()
  const diff = now - d
  if (diff < 60000) return '刚刚'
  if (diff < 3600000) return Math.floor(diff / 60000) + '分钟前'
  if (diff < 86400000) return Math.floor(diff / 3600000) + '小时前'
  return `${d.getMonth() + 1}/${d.getDate()}`
}

function goToPersons() {
  router.push('/persons')
}

onMounted(() => {
  if (currentRole.value !== 'student') {
    loadMembers()
  }
})

onUnmounted(() => {
  stopCamera()
})
</script>

<style scoped>
.invite-page {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  max-width: 1200px;
  margin: 0 auto;
}

.capture-area {
  text-align: center;
}

.capture-placeholder {
  padding: 40px 0;
  text-align: center;
}

.capture-preview {
  width: 100%;
  max-width: 320px;
  height: auto;
  border: 1px solid #d9d9d9;
  border-radius: 8px;
}

.capture-preview-img {
  width: 100%;
  max-width: 320px;
  height: auto;
  border: 1px solid #d9d9d9;
  border-radius: 8px;
}

.captured-wrap {
  margin-bottom: 8px;
}

.tips-list {
  padding-left: 20px;
  margin: 0;
  color: #595959;
  font-size: 13px;
  line-height: 1.8;
}
</style>
