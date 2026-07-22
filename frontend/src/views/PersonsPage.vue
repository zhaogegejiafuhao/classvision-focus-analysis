<template>
  <div class="cv-page" style="max-width: 1400px">
      <a-page-header :title="pageTitle" :sub-title="pageSubtitle" style="padding: 0 0 16px 0" />

      <a-alert
        v-if="currentRole === 'student'"
        message="无访问权限"
        description="学生账号无法访问人员管理功能，请联系教师或管理员。"
        type="warning"
        show-icon
        style="margin-bottom: 16px"
      />

      <a-row v-else :gutter="16">
        <a-col :span="8">
          <a-card :title="canRegisterTeacher ? '注册新人员' : '注册新学生'">
            <a-form layout="vertical">
              <a-form-item label="姓名">
                <a-input v-model:value="form.name" placeholder="请输入姓名" />
              </a-form-item>
              <a-form-item label="角色">
                <a-radio-group v-model:value="form.role">
                  <a-radio value="student">学生</a-radio>
                  <a-radio v-if="canRegisterTeacher" value="teacher">老师</a-radio>
                </a-radio-group>
              </a-form-item>
              <a-form-item label="人脸照片">
                <a-space direction="vertical" style="width: 100%">
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

        <a-col :span="16">
          <a-card :title="canRegisterTeacher ? '已注册人员' : '学生列表'">
            <a-tabs v-model:activeKey="activeTab">
              <a-tab-pane v-if="canRegisterTeacher" key="all" tab="全部">
                <a-table :columns="columns" :data-source="persons" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'role'">
                      <a-tag :color="record.role === 'teacher' ? 'blue' : record.role === 'admin' ? 'purple' : 'green'">
                        {{ record.role === 'teacher' ? '老师' : record.role === 'admin' ? '管理员' : '学生' }}
                      </a-tag>
                    </template>
                    <template v-if="column.key === 'action'">
                      <a-space>
                        <a-button v-if="canEdit" type="link" size="small" @click="openEditPerson(record)">编辑</a-button>
                        <a-popconfirm v-if="canDelete" title="确定删除该人员？" @confirm="deletePerson(record.id)">
                          <a-button type="link" danger size="small">删除</a-button>
                        </a-popconfirm>
                      </a-space>
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
                      <a-space>
                        <a-button v-if="canEdit" type="link" size="small" @click="openEditPerson(record)">编辑</a-button>
                        <a-popconfirm v-if="canDelete" title="确定删除该人员？" @confirm="deletePerson(record.id)">
                          <a-button type="link" danger size="small">删除</a-button>
                        </a-popconfirm>
                      </a-space>
                    </template>
                  </template>
                </a-table>
              </a-tab-pane>
              <a-tab-pane v-if="canRegisterTeacher" key="teacher" tab="老师">
                <a-table :columns="columns" :data-source="teachers" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'role'">
                      <a-tag color="blue">老师</a-tag>
                    </template>
                    <template v-if="column.key === 'action'">
                      <a-space>
                        <a-button v-if="canEdit" type="link" size="small" @click="openEditPerson(record)">编辑</a-button>
                        <a-popconfirm v-if="canDelete" title="确定删除该人员？" @confirm="deletePerson(record.id)">
                          <a-button type="link" danger size="small">删除</a-button>
                        </a-popconfirm>
                      </a-space>
                    </template>
                  </template>
                </a-table>
              </a-tab-pane>
            </a-tabs>
          </a-card>
        </a-col>
      </a-row>

      <!-- 编辑人员弹窗 -->
      <a-modal
        v-model:open="editModalOpen"
        title="编辑人员"
        @ok="handleEditSave"
        :confirm-loading="editSaving"
        ok-text="保存"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="姓名">
            <a-input v-model:value="editForm.name" />
          </a-form-item>
          <a-form-item label="用户名">
            <a-input v-model:value="editForm.username" placeholder="设置用户名后可用密码登录" />
          </a-form-item>
          <a-form-item label="重置密码">
            <a-input-password v-model:value="editForm.password" placeholder="留空则不修改" />
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { message } from 'ant-design-vue'
import { CameraOutlined, UploadOutlined } from '@ant-design/icons-vue'
import api from '@/api'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const currentRole = computed(() => userStore.role)

const canRegisterTeacher = computed(() => currentRole.value === 'admin')
const canEdit = computed(() => currentRole.value === 'admin' || currentRole.value === 'teacher')
const canDelete = computed(() => currentRole.value === 'admin' || currentRole.value === 'teacher')

const pageTitle = computed(() => {
  if (currentRole.value === 'admin') return '用户管理'
  if (currentRole.value === 'teacher') return '学生管理'
  return '人员管理'
})

const pageSubtitle = computed(() => {
  if (currentRole.value === 'admin') return '人脸注册与身份绑定 · 管理所有用户'
  if (currentRole.value === 'teacher') return '注册学生 · 查看学生列表'
  return ''
})

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

const columns = computed(() => {
  const cols = [
    { title: '姓名', dataIndex: 'name', key: 'name' },
    { title: '角色', dataIndex: 'role', key: 'role' },
    { title: '用户名', dataIndex: 'username', key: 'username' },
    { title: '注册时间', dataIndex: 'created_at', key: 'created_at' },
  ]
  if (canEdit.value || canDelete.value) {
    cols.push({ title: '操作', key: 'action' })
  }
  return cols
})

const students = computed(() => persons.value.filter(p => p.role === 'student'))
const teachers = computed(() => persons.value.filter(p => p.role === 'teacher'))

async function loadPersons() {
  try {
    const params = {}
    if (currentRole.value === 'teacher') {
      params.role = 'student'
    }
    const res = await api.get('/persons', { params })
    persons.value = res.data || []
    if (currentRole.value === 'teacher') {
      activeTab.value = 'student'
    }
  } catch (e) {
    message.error('加载人员列表失败')
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
    message.error('无法访问摄像头，请检查权限设置')
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
  if (form.value.role === 'teacher' && !canRegisterTeacher.value) {
    message.error('无权注册教师账号')
    return
  }
  registering.value = true
  try {
    const base64Data = capturedImage.value.split(',')[1]
    const formData = new FormData()
    formData.append('name', form.value.name)
    formData.append('role', form.value.role)
    formData.append('image_data', base64Data)
    await api.post('/persons/register', formData)
    form.value.name = ''
    capturedImage.value = null
    await loadPersons()
    message.success('注册成功')
  } catch (e) {
    const msg = e.response?.data?.detail || '注册失败'
    message.error(msg)
  } finally {
    registering.value = false
  }
}

async function deletePerson(personId) {
  try {
    await api.delete(`/persons/${personId}`)
    message.success('删除成功')
    await loadPersons()
  } catch (e) {
    const msg = e.response?.data?.detail || '删除失败'
    message.error(msg)
  }
}

// --- 编辑人员 ---
const editModalOpen = ref(false)
const editSaving = ref(false)
const editForm = ref({ id: null, name: '', username: '', password: '' })

function openEditPerson(record) {
  editForm.value = { id: record.id, name: record.name, username: record.username || '', password: '' }
  editModalOpen.value = true
}

async function handleEditSave() {
  editSaving.value = true
  try {
    const payload = { name: editForm.value.name, username: editForm.value.username }
    if (editForm.value.password) {
      payload.password = editForm.value.password
    }
    await api.put(`/persons/${editForm.value.id}`, payload)
    message.success('更新成功')
    editModalOpen.value = false
    await loadPersons()
  } catch (e) {
    const msg = e.response?.data?.detail || '更新失败'
    message.error(msg)
  } finally {
    editSaving.value = false
  }
}

onMounted(async () => {
  if (currentRole.value !== 'student') {
    await loadPersons()
  }
})

onUnmounted(() => {
  stopCamera()
})
</script>
