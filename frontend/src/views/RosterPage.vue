<template>
  <div class="cv-page" style="max-width: 1400px">
    <a-page-header title="花名册管理" sub-title="批量导入与管理师生管理员" style="padding: 0 0 16px 0" />

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

    <!-- 角色标签页 -->
    <a-tabs v-model:activeKey="activeRole" @change="loadPersons">
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
      <a-button @click="loadPersons" :loading="personsLoading">刷新</a-button>
    </a-space>

    <!-- 人员表格 -->
    <a-table
      :columns="personColumns"
      :data-source="persons"
      row-key="id"
      size="small"
      :loading="personsLoading"
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import { message } from 'ant-design-vue'
import { DownloadOutlined, UploadOutlined, CopyOutlined } from '@ant-design/icons-vue'

const activeRole = ref('student')
const persons = ref([])
const personsLoading = ref(false)
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

const personColumns = [
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
    const res = await api.get('/import/departments')
    departments.value = res.data || []
  } catch {
    departments.value = []
  }
}

async function loadPersons() {
  personsLoading.value = true
  try {
    const res = await api.get('/persons', { params: { role: activeRole.value } })
    persons.value = res.data || []
  } catch {
    persons.value = []
  } finally {
    personsLoading.value = false
  }
}

async function handleAddDept() {
  if (!newDeptName.value.trim()) {
    message.error('请输入部门名称')
    return
  }
  try {
    await api.post('/import/departments', null, { params: { name: newDeptName.value, type: newDeptType.value } })
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
    await api.delete(`/import/departments/${id}`)
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
    const token = localStorage.getItem('token') || ''
    const res = await fetch(`/api/import/excel?role=${activeRole.value}`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
      body: formData,
    })
    importResult.value = await res.json()
    resultOpen.value = true
    await loadPersons()
    await loadDepartments()
  } catch (e) {
    message.error('导入失败: ' + e.message)
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
    const res = await api.post(`/import/csv?role=${activeRole.value}`, csvData.value, {
      headers: { 'Content-Type': 'text/plain' },
    })
    importResult.value = res.data
    resultOpen.value = true
    csvOpen.value = false
    csvData.value = ''
    await loadPersons()
    await loadDepartments()
  } catch (e) {
    message.error(e.response?.data?.detail || '导入失败')
  } finally {
    csvLoading.value = false
  }
}

function exportErrors() {
  if (!importResult.value?.errors?.length) return
  // 生成简单 CSV 下载
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

onMounted(() => {
  loadDepartments()
  loadPersons()
})
</script>
