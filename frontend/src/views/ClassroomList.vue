<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 18px; font-weight: bold; cursor: pointer" @click="$router.push('/')">
        ClassVision 课眼智析
      </span>
      <a-button type="primary" @click="$router.push('/')">开始新课堂</a-button>
    </a-layout-header>
    <a-layout-content style="padding: 24px">
      <a-typography-title :level="3">历史课堂</a-typography-title>
      <a-alert v-if="backendError" message="后端服务未就绪，请确认后端已启动" type="error" show-icon
               style="margin-bottom: 16px">
        <template #action>
          <a-button size="small" @click="loadClassrooms">重试</a-button>
        </template>
      </a-alert>
      <a-table :columns="columns" :data-source="classrooms" :loading="loading" row-key="id">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'action'">
            <a-button type="link" @click="$router.push(`/classrooms/${record.id}`)">查看详情</a-button>
            <a-popconfirm title="确认删除此课堂及其所有数据？" ok-text="删除" cancel-text="取消"
                          @confirm="deleteClassroom(record.id)">
              <a-button type="link" danger>删除</a-button>
            </a-popconfirm>
          </template>
          <template v-if="column.key === 'avg_attention'">
            <a-tag :color="record.avg_attention >= 60 ? 'green' : record.avg_attention >= 30 ? 'orange' : 'red'">
              {{ record.avg_attention?.toFixed(1) }}
            </a-tag>
          </template>
          <template v-if="column.key === 'ended_at'">
            {{ record.ended_at ? new Date(record.ended_at).toLocaleString('zh-CN') : '进行中' }}
          </template>
        </template>
      </a-table>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { message } from 'ant-design-vue'
import { waitForBackend } from '../utils/api'

const classrooms = ref([])
const loading = ref(true)
const backendError = ref(false)

const columns = [
  { title: '课程', dataIndex: 'name', key: 'name' },
  { title: '教师', dataIndex: 'teacher', key: 'teacher' },
  { title: '开始时间', dataIndex: 'started_at', key: 'started_at' },
  { title: '结束时间', key: 'ended_at' },
  { title: '时长(分)', dataIndex: 'duration', key: 'duration' },
  { title: '平均注意力', key: 'avg_attention' },
  { title: '人数', dataIndex: 'total_students', key: 'total_students' },
  { title: '操作', key: 'action' },
]

async function loadClassrooms() {
  loading.value = true
  backendError.value = false
  const ready = await waitForBackend()
  if (!ready) {
    backendError.value = true
    loading.value = false
    return
  }
  try {
    const res = await axios.get('/api/classrooms')
    classrooms.value = res.data
  } catch {
    backendError.value = true
  } finally {
    loading.value = false
  }
}

async function deleteClassroom(id) {
  try {
    await axios.delete(`/api/classrooms/${id}`)
    message.success('课堂已删除')
    classrooms.value = classrooms.value.filter(c => c.id !== id)
  } catch (e) {
    message.error('删除失败: ' + (e.response?.data?.detail || e.message))
  }
}

onMounted(() => {
  loadClassrooms()
})
</script>
