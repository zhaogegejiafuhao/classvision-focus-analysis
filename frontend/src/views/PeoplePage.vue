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

    <a-tabs v-else v-model:activeKey="activeMainTab">
      <!-- Tab 1：人员注册与列表（teacher / admin） -->
      <a-tab-pane key="register" tab="人员注册与列表">
        <a-row :gutter="16">
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
                  <a-button type="primary" block @click="handleRegisterPerson" :loading="registering" :disabled="!form.name || !capturedImage">
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
                          <a-popconfirm v-if="canDelete" title="确定删除该人员？" @confirm="handleDeletePerson(record.id)">
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
                          <a-popconfirm v-if="canDelete" title="确定删除该人员？" @confirm="handleDeletePerson(record.id)">
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
                          <a-popconfirm v-if="canDelete" title="确定删除该人员？" @confirm="handleDeletePerson(record.id)">
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
      </a-tab-pane>

      <!-- Tab 2：批量导入与部门管理（仅 admin） -->
      <a-tab-pane v-if="currentRole === 'admin'" key="import" tab="批量导入">
        <!-- 部门管理 -->
        <a-card title="部门/班级" size="small" style="margin-bottom: 16px">
          <template #extra>
            <a-button type="primary" size="small" @click="addDeptOpen = true">
              新增部门
            </a-button>
          </template>
          <a-table :columns="deptColumns" :data-source="departments" row-key="id" size="small" :pagination="{ pageSize: 5 }">
            <template #bodyCell="{ column, record }">
              <template v-if="column.key === 'type'">
                <a-tag :color="record.type === 'class' ? 'blue' : 'green'">
                  {{ record.type === 'class' ? '班级' : '部门' }}
                </a-tag>
              </template>
              <template v-if="column.key === 'action'">
                <a-popconfirm title="确定删除？" @confirm="deleteDept(record.id)">
                  <a-button type="link" danger size="small" :disabled="record.member_count > 0">删除</a-button>
                </a-popconfirm>
              </template>
            </template>
          </a-table>
        </a-card>

        <!-- 角色筛选 -->
        <a-tabs v-model:activeKey="activeRole" @change="loadRosterPersons">
          <a-tab-pane key="student" tab="学生" />
          <a-tab-pane key="teacher" tab="教师" />
          <a-tab-pane key="admin" tab="管理员" />
        </a-tabs>

        <!-- 操作栏 -->
        <a-space style="margin-bottom: 16px">
          <a-button type="primary" @click="downloadTemplate">
            <template #icon><DownloadOutlined /></template>
            下载模板
          </a-button>
          <a-upload
            :before-upload="handleExcelUpload"
            accept=".xlsx,.xls"
            :show-upload-list="false"
          >
            <a-button type="primary" :loading="importLoading">
              <template #icon><UploadOutlined /></template>
              批量导入 Excel
            </a-button>
          </a-upload>
          <a-button @click="csvOpen = true">
            <template #icon><CopyOutlined /></template>
            复制粘贴导入
          </a-button>
          <a-button @click="loadRosterPersons" :loading="rosterPersonsLoading">刷新</a-button>
        </a-space>

        <!-- 人员表格 -->
        <a-table
          :columns="rosterPersonColumns"
          :data-source="rosterPersons"
          row-key="id"
          size="small"
          :loading="rosterPersonsLoading"
          :pagination="{ pageSize: 20, showSizeChanger: true }"
          :scroll="{ x: 1000 }"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'role'">
              <a-tag :color="record.role === 'teacher' ? 'blue' : record.role === 'admin' ? 'red' : 'green'">
                {{ record.role === 'teacher' ? '教师' : record.role === 'admin' ? '管理员' : '学生' }}
              </a-tag>
            </template>
          </template>
        </a-table>

        <!-- 新增部门弹窗 -->
        <a-modal v-model:open="addDeptOpen" title="新增部门/班级" @ok="handleAddDept" ok-text="创建" cancel-text="取消">
          <a-form layout="vertical">
            <a-form-item label="名称" required>
              <a-input v-model:value="newDeptName" placeholder="如：计算机1班、数学系" />
            </a-form-item>
            <a-form-item label="类型">
              <a-radio-group v-model:value="newDeptType">
                <a-radio value="class">班级</a-radio>
                <a-radio value="department">部门</a-radio>
              </a-radio-group>
            </a-form-item>
          </a-form>
        </a-modal>

        <!-- 复制粘贴弹窗 -->
        <a-modal v-model:open="csvOpen" title="复制粘贴批量导入" @ok="handleCsvImport" :confirm-loading="csvLoading" ok-text="导入" cancel-text="取消" width="700px">
          <a-alert message="每行一条记录，字段用逗号或制表符分隔。格式：学号,姓名,手机号,班级,专业,邮箱,身份证" type="info" show-icon style="margin-bottom: 12px" />
          <a-textarea v-model:value="csvData" :rows="10" placeholder="2024001,张三,13800138000,计算机1班,软件工程,zhangsan@edu.cn&#10;2024002,李四,13900139000,计算机1班,数据科学" />
        </a-modal>

        <!-- 导入结果弹窗 -->
        <a-modal v-model:open="resultOpen" title="导入结果" :footer="null" width="600px">
          <a-result v-if="importResult" :status="importResult.failed === 0 ? 'success' : 'warning'">
            <template #title>
              导入完成
            </template>
            <template #subTitle>
              共 {{ importResult.total }} 条，成功 {{ importResult.success }} 条，失败 {{ importResult.failed }} 条
              <br />
              <span style="font-size: 13px; color: #999">默认密码：{{ defaultPwd }}（用户名 = 学号/工号）</span>
            </template>
            <template #extra>
              <a-button v-if="importResult.errors.length > 0" type="primary" @click="exportErrors">
                下载错误明细
              </a-button>
            </template>
          </a-result>
          <a-table v-if="importResult && importResult.errors.length > 0" :columns="errorColumns" :data-source="importResult.errors" row-key="row" size="small" :pagination="{ pageSize: 10 }" style="margin-top: 16px" />
        </a-modal>
      </a-tab-pane>
    </a-tabs>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { message } from 'ant-design-vue'
import { CameraOutlined, UploadOutlined, DownloadOutlined, CopyOutlined } from '@ant-design/icons-vue'
import { listPersons, registerPerson, deletePerson as _deletePerson, updatePerson } from '@/api/person'
import { listDepartments, createDepartment, deleteDepartment, importExcel, importCsv } from '@/api/import'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const userStore = useUserStore()
const currentRole = computed(() => userStore.role)

const canRegisterTeacher = computed(() => currentRole.value === 'admin')
const canEdit = computed(() => currentRole.value === 'admin' || currentRole.value === 'teacher')
const canDelete = computed(() => currentRole.value === 'admin' || currentRole.value === 'teacher')

const pageTitle = computed(() => {
  if (currentRole.value === 'admin') return '人员管理'
  if (currentRole.value === 'teacher') return '学生管理'
  return '人员管理'
})

const pageSubtitle = computed(() => {
  if (currentRole.value === 'admin') return '人脸注册与身份绑定 · 批量导入 · 管理所有用户'
  if (currentRole.value === 'teacher') return '注册学生 · 查看学生列表'
  return ''
})

// 顶层 Tab：admin 默认根据 query.tab 决定，teacher 只能 register
const activeMainTab = ref('register')

// ===== Tab 1：人员注册与列表（原 PersonsPage） =====
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
    const res = await listPersons(params)
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

async function handleRegisterPerson() {
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
    await registerPerson(formData)
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

async function handleDeletePerson(personId) {
  try {
    await _deletePerson(personId)
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
    await updatePerson(editForm.value.id, payload)
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

// ===== Tab 2：批量导入与部门管理（原 RosterPage） =====
const activeRole = ref('student')
const rosterPersons = ref([])
const rosterPersonsLoading = ref(false)
const departments = ref([])
const importLoading = ref(false)
const importResult = ref(null)
const resultOpen = ref(false)
const defaultPwd = '123456'

// 部门
const addDeptOpen = ref(false)
const newDeptName = ref('')
const newDeptType = ref('class')
const deptColumns = [
  { title: '名称', dataIndex: 'name', key: 'name' },
  { title: '类型', dataIndex: 'type', key: 'type', width: 80 },
  { title: '成员数', dataIndex: 'member_count', key: 'member_count', width: 80 },
  { title: '操作', key: 'action', width: 80 },
]

// 复制粘贴
const csvOpen = ref(false)
const csvData = ref('')
const csvLoading = ref(false)

const rosterPersonColumns = [
  { title: '学号/工号', dataIndex: 'employee_id', key: 'employee_id', width: 120 },
  { title: '姓名', dataIndex: 'name', key: 'name', width: 80 },
  { title: '角色', dataIndex: 'role', key: 'role', width: 80 },
  { title: '用户名', dataIndex: 'username', key: 'username', width: 100 },
  { title: '手机号', dataIndex: 'phone', key: 'phone', width: 120 },
  { title: '部门/班级', dataIndex: 'department_name', key: 'department_name', width: 120 },
  { title: '专业', dataIndex: 'major', key: 'major', width: 100 },
  { title: '邮箱', dataIndex: 'email', key: 'email', width: 150, ellipsis: true },
]

const errorColumns = [
  { title: '行号', dataIndex: 'row', key: 'row', width: 60 },
  { title: '学号/工号', dataIndex: 'employee_id', key: 'employee_id', width: 100 },
  { title: '姓名', dataIndex: 'name', key: 'name', width: 80 },
  { title: '错误原因', dataIndex: 'error', key: 'error' },
]

async function loadDepartments() {
  try {
    const res = await listDepartments()
    departments.value = res.data || []
  } catch {
    departments.value = []
  }
}

async function loadRosterPersons() {
  rosterPersonsLoading.value = true
  try {
    const res = await listPersons({ role: activeRole.value })
    rosterPersons.value = res.data || []
  } catch {
    rosterPersons.value = []
  } finally {
    rosterPersonsLoading.value = false
  }
}

async function handleAddDept() {
  if (!newDeptName.value.trim()) {
    message.error('请输入部门名称')
    return
  }
  try {
    await createDepartment({ name: newDeptName.value, type: newDeptType.value })
    message.success('部门已创建')
    addDeptOpen.value = false
    newDeptName.value = ''
    await loadDepartments()
  } catch (e) {
    message.error(e.response?.data?.detail || '创建失败')
  }
}

async function deleteDept(id) {
  try {
    await deleteDepartment(id)
    message.success('部门已删除')
    await loadDepartments()
  } catch (e) {
    message.error(e.response?.data?.detail || '删除失败')
  }
}

function downloadTemplate() {
  window.open(`/api/import/template?role=${activeRole.value}`, '_blank')
}

async function handleExcelUpload(file) {
  importLoading.value = true
  const formData = new FormData()
  formData.append('file', file)
  try {
    const res = await importExcel(activeRole.value, formData)
    importResult.value = res.data
    resultOpen.value = true
    await loadRosterPersons()
    await loadDepartments()
  } catch (e) {
    message.error('导入失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    importLoading.value = false
  }
  return false
}

async function handleCsvImport() {
  if (!csvData.value.trim()) {
    message.error('请输入数据')
    return
  }
  csvLoading.value = true
  try {
    const res = await importCsv(activeRole.value, csvData.value)
    importResult.value = res.data
    resultOpen.value = true
    csvOpen.value = false
    csvData.value = ''
    await loadRosterPersons()
    await loadDepartments()
  } catch (e) {
    message.error(e.response?.data?.detail || '导入失败')
  } finally {
    csvLoading.value = false
  }
}

function exportErrors() {
  if (!importResult.value?.errors?.length) return
  const header = '行号,学号/工号,姓名,错误原因\n'
  const rows = importResult.value.errors.map(e => `${e.row},${e.employee_id},${e.name},"${e.error}"`).join('\n')
  const blob = new Blob([header + rows], { type: 'text/csv;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'import_errors.csv'
  a.click()
  URL.revokeObjectURL(url)
}

onMounted(async () => {
  if (currentRole.value !== 'student') {
    await loadPersons()
    // admin 进入批量导入 Tab 时加载相关数据
    if (currentRole.value === 'admin') {
      loadDepartments()
      loadRosterPersons()
      // 支持 /roster 路径或 /persons?tab=import 直接定位到批量导入
      if (route.path === '/roster' || route.query.tab === 'import') {
        activeMainTab.value = 'import'
      }
    }
  }
})

onUnmounted(() => {
  stopCamera()
})
</script>
