<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 18px; font-weight: bold; cursor: pointer" @click="$router.push('/')">
        ClassVision 课眼智析
      </span>
      <a-space>
        <a-button type="link" style="color: #fff" @click="$router.push('/classrooms')">课堂列表</a-button>
        <a-button type="link" style="color: #fff" @click="$router.push('/persons')">人员管理</a-button>
      </a-space>
    </a-layout-header>
    <a-layout-content style="padding: 24px">
      <a-page-header title="人员管理" sub-title="人脸注册与身份绑定" />

      <a-row :gutter="16">
        <!-- 注册区域 -->
        <a-col :span="8">
          <a-card title="注册新人员">
            <a-form layout="vertical">
              <a-form-item label="姓名">
                <a-input v-model:value="form.name" placeholder="请输入姓名" />
              </a-form-item>
              <a-form-item label="角色">
                <a-radio-group v-model:value="form.role">
                  <a-radio value="student">学生</a-radio>
                  <a-radio value="teacher">老师</a-radio>
                </a-radio-group>
              </a-form-item>
              <a-form-item label="人脸照片">
                <a-space direction="vertical" style="width: 100%">
                  <!-- 摄像头捕获 -->
                  <div v-if="cameraActive" style="text-align: center">
                    <video ref="videoEl" width="320" height="240" autoplay style="border: 1px solid #d9d9d9; border-radius: 4px" />
                    <a-space style="margin-top: 8px">
                      <a-button type="primary" @click="capturePhoto" :loading="capturing">拍照</a-button>
                      <a-button @click="stopCamera">关闭摄像头</a-button>
                    </a-space>
                  </div>
                  <div v-else style="text-align: center">
                    <div v-if="capturedImage" style="margin-bottom: 8px">
                      <img :src="capturedImage" width="320" height="240" style="border: 1px solid #d9d9d9; border-radius: 4px" />
                    </div>
                    <a-space>
                      <a-button @click="startCamera" :disabled="registering">
                        <template #icon><CameraOutlined /></template>
                        打开摄像头
                      </a-button>
                      <a-upload :show-upload-list="false" :before-upload="handleUpload">
                        <a-button :disabled="registering">
                          <template #icon><UploadOutlined /></template>
                          上传照片
                        </a-button>
                      </a-upload>
                    </a-space>
                  </div>
                  <a-alert v-if="!capturedImage" message="请拍摄或上传包含清晰人脸的照片" type="info" show-icon />
                </a-space>
              </a-form-item>
              <a-form-item>
                <a-button type="primary" block @click="registerPerson" :loading="registering" :disabled="!form.name || !capturedImage">
                  注册
                </a-button>
              </a-form-item>
            </a-form>
          </a-card>
        </a-col>

        <!-- 已注册人员列表 -->
        <a-col :span="16">
          <a-card title="已注册人员">
            <a-tabs v-model:activeKey="activeTab">
              <a-tab-pane key="all" tab="全部">
                <a-table :columns="columns" :data-source="persons" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'role'">
                      <a-tag :color="record.role === 'teacher' ? 'blue' : 'green'">
                        {{ record.role === 'teacher' ? '老师' : '学生' }}
                      </a-tag>
                    </template>
                    <template v-if="column.key === 'action'">
                      <a-popconfirm title="确定删除该人员？" @confirm="deletePerson(record.id)">
                        <a-button type="link" danger size="small">删除</a-button>
                      </a-popconfirm>
                    </template>
                  </template>
                </a-table>
              </a-tab-pane>
              <a-tab-pane key="student" tab="学生">
                <a-table :columns="columns" :data-source="students" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'role'">
                      <a-tag color="green">学生</a-tag>
                    </template>
                    <template v-if="column.key === 'action'">
                      <a-popconfirm title="确定删除该人员？" @confirm="deletePerson(record.id)">
                        <a-button type="link" danger size="small">删除</a-button>
                      </a-popconfirm>
                    </template>
                  </template>
                </a-table>
              </a-tab-pane>
              <a-tab-pane key="teacher" tab="老师">
                <a-table :columns="columns" :data-source="teachers" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'role'">
                      <a-tag color="blue">老师</a-tag>
                    </template>
                    <template v-if="column.key === 'action'">
                      <a-popconfirm title="确定删除该人员？" @confirm="deletePerson(record.id)">
                        <a-button type="link" danger size="small">删除</a-button>
                      </a-popconfirm>
                    </template>
                  </template>
                </a-table>
              </a-tab-pane>
            </a-tabs>
          </a-card>
        </a-col>
      </a-row>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import { CameraOutlined, UploadOutlined } from '@ant-design/icons-vue'
import { waitForBackend } from '../utils/api'

const form = ref({
  name: '',
  role: 'student',
})

const persons = ref([])
const activeTab = ref('all')
const registering = ref(false)
const capturing = ref(false)
const cameraActive = ref(false)
const capturedImage = ref(null)
const videoEl = ref(null)
let mediaStream = null

const columns = [
  { title: '姓名', dataIndex: 'name', key: 'name' },
  { title: '角色', dataIndex: 'role', key: 'role' },
  { title: '注册时间', dataIndex: 'created_at', key: 'created_at' },
  { title: '操作', key: 'action' },
]

const students = computed(() => persons.value.filter(p => p.role === 'student'))
const teachers = computed(() => persons.value.filter(p => p.role === 'teacher'))

async function loadPersons() {
  try {
    const res = await axios.get('/api/persons')
    persons.value = res.data || []
  } catch (e) {
    console.error('加载人员列表失败', e)
  }
}

async function startCamera() {
  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({ video: { width: 320, height: 240 } })
    cameraActive.value = true
    await new Promise(resolve => setTimeout(resolve, 100))
    if (videoEl.value) {
      videoEl.value.srcObject = mediaStream
    }
  } catch (e) {
    console.error('无法访问摄像头', e)
    alert('无法访问摄像头，请检查权限设置')
  }
}

function stopCamera() {
  if (mediaStream) {
    mediaStream.getTracks().forEach(track => track.stop())
    mediaStream = null
  }
  cameraActive.value = false
}

async function capturePhoto() {
  if (!videoEl.value) return
  capturing.value = true
  try {
    const canvas = document.createElement('canvas')
    canvas.width = 320
    canvas.height = 240
    const ctx = canvas.getContext('2d')
    ctx.drawImage(videoEl.value, 0, 0, 320, 240)
    capturedImage.value = canvas.toDataURL('image/jpeg')
    stopCamera()
  } finally {
    capturing.value = false
  }
}

function handleUpload(file) {
  const reader = new FileReader()
  reader.onload = (e) => {
    capturedImage.value = e.target.result
  }
  reader.readAsDataURL(file)
  return false
}

async function registerPerson() {
  if (!form.value.name || !capturedImage.value) return
  registering.value = true
  try {
    // 提取 base64 数据
    const base64Data = capturedImage.value.split(',')[1]
    const formData = new FormData()
    formData.append('name', form.value.name)
    formData.append('role', form.value.role)
    formData.append('image_data', base64Data)
    await axios.post('/api/persons/register', formData)
    // 重置表单
    form.value.name = ''
    capturedImage.value = null
    // 刷新列表
    await loadPersons()
    alert('注册成功')
  } catch (e) {
    const msg = e.response?.data?.detail || '注册失败'
    alert(msg)
  } finally {
    registering.value = false
  }
}

async function deletePerson(personId) {
  try {
    await axios.delete(`/api/persons/${personId}`)
    await loadPersons()
  } catch (e) {
    const msg = e.response?.data?.detail || '删除失败'
    alert(msg)
  }
}

onMounted(async () => {
  await waitForBackend()
  await loadPersons()
})

onUnmounted(() => {
  stopCamera()
})
</script>