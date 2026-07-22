<template>
  <div class="cv-page">
    <a-page-header title="作业管理" sub-title="创建和管理作业">
      <template #extra>
        <a-button type="primary" @click="showCreateModal = true">
          创建作业
        </a-button>
      </template>
    </a-page-header>

    <!-- 课堂筛选 -->
    <div style="margin-bottom: 16px">
      <a-select
        v-model:value="selectedClassroomId"
        placeholder="按课堂筛选"
        allow-clear
        style="width: 240px"
        @change="fetchHomeworks"
      >
        <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
      </a-select>
    </div>

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="homeworks" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'title'">
            <a @click="goDetail(record.id)">{{ record.title }}</a>
          </template>
          <template v-else-if="column.key === 'deadline'">
            <span :class="{ 'deadline-passed': isDeadlinePassed(record.deadline) }">
              {{ record.deadline ? formatTime(record.deadline) : '无截止时间' }}
            </span>
          </template>
          <template v-else-if="column.key === 'status'">
            <a-tag :color="getStatusColor(record.status)">{{ getStatusText(record.status) }}</a-tag>
          </template>
          <template v-else-if="column.key === 'action'">
            <a-space>
              <a-button type="link" size="small" @click="goDetail(record.id)">查看</a-button>
              <a-popconfirm title="确定删除？" @confirm="deleteHomework(record.id)">
                <a-button type="link" danger size="small">删除</a-button>
              </a-popconfirm>
            </a-space>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 创建作业弹窗 -->
    <a-modal v-model:open="showCreateModal" title="创建作业" @ok="createHomework" :confirm-loading="submitting" width="600px">
      <a-form :label-col="{ span: 4 }" :wrapper-col="{ span: 18 }">
        <a-form-item label="标题" required>
          <a-input v-model:value="form.title" placeholder="作业标题" />
        </a-form-item>
        <a-form-item label="描述">
          <a-textarea v-model:value="form.description" placeholder="作业描述" :rows="4" />
        </a-form-item>
        <a-form-item label="关联课堂">
          <a-select v-model:value="form.classroom_id" placeholder="选择课堂（可选）" allow-clear>
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="截止时间">
          <a-date-picker v-model:value="form.deadline" show-time placeholder="选择截止时间" style="width: 100%" />
        </a-form-item>
        <a-form-item label="总分">
          <a-input-number v-model:value="form.total_score" :min="0" :max="1000" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import api from '../api'
import dayjs from 'dayjs'

const router = useRouter()
const homeworks = ref([])
const classrooms = ref([])
const selectedClassroomId = ref(undefined)
const loading = ref(false)
const submitting = ref(false)
const showCreateModal = ref(false)

const form = ref({
  title: '',
  description: '',
  classroom_id: null,
  deadline: null,
  total_score: 100,
})

const columns = [
  { key: 'title', title: '标题', dataIndex: 'title' },
  { key: 'classroom', title: '课堂', dataIndex: 'classroom_name' },
  { key: 'deadline', title: '截止时间', dataIndex: 'deadline' },
  { key: 'submissions', title: '提交数', dataIndex: 'submission_count' },
  { key: 'status', title: '状态', dataIndex: 'status' },
  { key: 'action', title: '操作' },
]

async function fetchHomeworks() {
  loading.value = true
  try {
    const params = {}
    if (selectedClassroomId.value) params.classroom_id = selectedClassroomId.value
    const res = await api.get('/homework', { params })
    homeworks.value = res.data
  } catch (e) {
    message.error('获取作业失败')
  } finally {
    loading.value = false
  }
}

async function fetchClassrooms() {
  try {
    const res = await api.get('/classrooms')
    classrooms.value = res.data
  } catch (e) {
    // 忽略
  }
}

async function createHomework() {
  if (!form.value.title.trim()) {
    message.error('请输入标题')
    return
  }
  submitting.value = true
  try {
    const payload = {
      title: form.value.title,
      description: form.value.description,
      classroom_id: form.value.classroom_id,
      deadline: form.value.deadline ? form.value.deadline.toISOString() : null,
      total_score: form.value.total_score,
    }
    await api.post('/homework', payload)
    message.success('创建成功')
    showCreateModal.value = false
    resetForm()
    fetchHomeworks()
  } catch (e) {
    message.error('创建失败')
  } finally {
    submitting.value = false
  }
}

async function deleteHomework(id) {
  try {
    await api.delete(`/homework/${id}`)
    message.success('删除成功')
    fetchHomeworks()
  } catch (e) {
    message.error('删除失败')
  }
}

function resetForm() {
  form.value = {
    title: '',
    description: '',
    classroom_id: null,
    deadline: null,
    total_score: 100,
  }
}

function goDetail(id) {
  router.push(`/homework/${id}`)
}

function formatTime(time) {
  return dayjs(time).format('YYYY-MM-DD HH:mm')
}

function isDeadlinePassed(deadline) {
  return deadline && dayjs(deadline).isBefore(dayjs())
}

function getStatusColor(status) {
  return { open: 'blue', closed: 'gray', archived: 'default' }[status] || 'default'
}

function getStatusText(status) {
  return { open: '进行中', closed: '已截止', archived: '已归档' }[status] || status
}

onMounted(() => {
  fetchHomeworks()
  fetchClassrooms()
})
</script>

<style scoped>
.deadline-passed {
  color: #ff4d4f;
}
</style>