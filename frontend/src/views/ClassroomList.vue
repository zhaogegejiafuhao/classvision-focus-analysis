<template>
  <div class="cv-page">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px">
        <a-typography-title :level="3" style="margin: 0">{{ pageTitle }}</a-typography-title>
        <a-button v-if="canCreate" type="primary" @click="openCreate">开始新课堂</a-button>
      </div>

      <a-skeleton v-if="loading && classrooms.length === 0" active :paragraph="{ rows: 6 }" />
      <a-table v-else :columns="columns" :data-source="classrooms" :loading="loading" row-key="id">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'action'">
            <a-space>
              <a-button type="link" size="small" @click="$router.push(`/classrooms/${record.id}`)">查看详情</a-button>
              <template v-if="canEditOrDelete(record)">
                <a-button type="link" size="small" @click="openEdit(record)">
                  <template #icon><EditOutlined /></template>
                  编辑
                </a-button>
                <a-popconfirm title="确定删除该课堂？所有关联数据（学生、记录、报告等）将一并删除。" @confirm="deleteClassroom(record)">
                  <a-button type="link" danger size="small">
                    <template #icon><DeleteOutlined /></template>
                    删除
                  </a-button>
                </a-popconfirm>
              </template>
            </a-space>
          </template>
          <template v-if="column.key === 'avg_attention'">
            <a-tag :color="(record.avg_attention || 0) >= 60 ? 'green' : (record.avg_attention || 0) >= 30 ? 'orange' : 'red'">
              {{ record.avg_attention != null ? record.avg_attention.toFixed(1) : '-' }}
            </a-tag>
          </template>
          <template v-if="column.key === 'ended_at'">
            {{ record.ended_at ? new Date(record.ended_at).toLocaleString('zh-CN') : '进行中' }}
          </template>
          <template v-if="column.key === 'started_at'">
            {{ record.started_at ? new Date(record.started_at).toLocaleString('zh-CN') : '-' }}
          </template>
          <template v-if="column.key === 'status'">
            <a-tag :color="record.ended_at ? 'default' : record.started_at ? 'green' : 'blue'">
              {{ record.ended_at ? '已结束' : record.started_at ? '进行中' : '未开始' }}
            </a-tag>
          </template>
        </template>
      </a-table>

      <!-- 创建/编辑课堂弹窗 -->
      <a-modal
        v-model:open="showModal"
        :title="editingId ? '编辑课堂' : '开始新课堂'"
        @ok="handleSave"
        :confirm-loading="saving"
        ok-text="保存"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="课程名称" required>
            <a-input v-model:value="form.name" placeholder="例如：高一(3)班 数学" />
          </a-form-item>
          <a-form-item label="授课教师">
            <a-input v-model:value="form.teacher" placeholder="教师姓名" />
          </a-form-item>
          <a-form-item label="考试模式">
            <a-switch v-model:checked="form.exam_mode" checked-children="考试" un-checked-children="普通" />
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { EditOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import api from '@/api'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const classrooms = ref([])
const loading = ref(true)
const showModal = ref(false)
const saving = ref(false)
const editingId = ref(null)

const form = ref({
  name: '',
  teacher: '',
  exam_mode: false,
})

const currentRole = computed(() => userStore.role)
const currentUserId = computed(() => userStore.user?.id)

const canCreate = computed(() => currentRole.value === 'teacher' || currentRole.value === 'admin')

const pageTitle = computed(() => {
  const titles = { teacher: '课堂管理', student: '我的课堂', admin: '课堂总览' }
  return titles[currentRole.value] || '历史课堂'
})

function canEditOrDelete(record) {
  if (!canCreate.value) return false
  if (currentRole.value === 'admin') return true
  return record.teacher_person_id === currentUserId.value
}

const columns = computed(() => {
  const base = [
    { title: '课程', dataIndex: 'name', key: 'name' },
    { title: '状态', key: 'status' },
  ]
  if (currentRole.value !== 'student') {
    base.push({ title: '教师', dataIndex: 'teacher', key: 'teacher' })
  }
  base.push(
    { title: '开始时间', key: 'started_at' },
    { title: '结束时间', key: 'ended_at' },
    { title: '时长(分)', dataIndex: 'duration', key: 'duration' },
  )
  if (currentRole.value !== 'student') {
    base.push({ title: '平均注意力', key: 'avg_attention' })
    base.push({ title: '人数', dataIndex: 'total_students', key: 'total_students' })
  }
  base.push({ title: '操作', key: 'action' })
  return base
})

async function loadClassrooms() {
  loading.value = true
  try {
    const res = await api.get('/classrooms')
    classrooms.value = res.data || []
  } catch (e) {
    message.error('加载课堂列表失败')
  } finally {
    loading.value = false
  }
}

function openCreate() {
  editingId.value = null
  form.value = { name: '', teacher: '', exam_mode: false }
  showModal.value = true
}

function openEdit(record) {
  editingId.value = record.id
  form.value = {
    name: record.name,
    teacher: record.teacher,
    exam_mode: record.exam_mode,
  }
  showModal.value = true
}

async function handleSave() {
  if (!form.value.name) {
    message.warning('请输入课程名称')
    return
  }
  saving.value = true
  try {
    if (editingId.value) {
      await api.put(`/classrooms/${editingId.value}`, {
        name: form.value.name,
        teacher: form.value.teacher,
        exam_mode: form.value.exam_mode,
      })
      message.success('课堂已更新')
    } else {
      await api.post('/classrooms', {
        name: form.value.name,
        teacher: form.value.teacher || userStore.displayName,
        exam_mode: form.value.exam_mode,
      })
      message.success('课堂创建成功')
    }
    showModal.value = false
    await loadClassrooms()
  } catch (e) {
    const msg = e.response?.data?.detail || '保存失败'
    message.error(msg)
  } finally {
    saving.value = false
  }
}

async function deleteClassroom(record) {
  try {
    await api.delete(`/classrooms/${record.id}`)
    message.success('课堂已删除')
    await loadClassrooms()
  } catch (e) {
    const msg = e.response?.data?.detail || '删除失败'
    message.error(msg)
  }
}

onMounted(() => {
  loadClassrooms()
})
</script>
