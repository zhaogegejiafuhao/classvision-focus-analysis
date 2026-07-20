<template>
  <div class="experiment-page">
    <a-card title="实验报告管理">
      <template #extra>
        <a-button v-if="userStore.role === 'teacher'" type="primary" @click="showCreate = true">创建实验</a-button>
      </template>

      <a-table :columns="columns" :data-source="experiments" row-key="id" :loading="loading" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'title'">
            <a @click="goDetail(record.id)">{{ record.title }}</a>
          </template>
          <template v-else-if="column.key === 'deadline'">
            {{ record.deadline ? dayjs(record.deadline).format('YYYY-MM-DD HH:mm') : '无截止' }}
          </template>
          <template v-else-if="column.key === 'status'">
            <a-tag :color="record.status === 'open' ? 'green' : 'default'">{{ record.status === 'open' ? '进行中' : '已关闭' }}</a-tag>
          </template>
          <template v-else-if="column.key === 'action'">
            <a-button type="link" size="small" @click="goDetail(record.id)">详情</a-button>
            <a-button v-if="userStore.role === 'teacher'" type="link" size="small" danger @click="del(record.id)">删除</a-button>
          </template>
        </template>
      </a-table>
    </a-card>

    <a-modal v-model:open="showCreate" title="创建实验" @ok="createExp" :confirm-loading="creating">
      <a-form layout="vertical">
        <a-form-item label="标题" required>
          <a-input v-model:value="form.title" />
        </a-form-item>
        <a-form-item label="描述">
          <a-textarea v-model:value="form.description" :rows="3" />
        </a-form-item>
        <a-form-item label="实验要求">
          <a-textarea v-model:value="form.requirements" :rows="4" />
        </a-form-item>
        <a-form-item label="课堂">
          <a-select v-model:value="form.classroom_id" placeholder="可选" allowClear>
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="截止时间">
          <a-date-picker v-model:value="form.deadline" show-time style="width: 100%" />
        </a-form-item>
        <a-form-item label="总分">
          <a-input-number v-model:value="form.total_score" :min="1" :max="1000" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { message, Modal } from 'ant-design-vue'
import dayjs from 'dayjs'
import api from '@/api'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
const experiments = ref([])
const loading = ref(false)
const showCreate = ref(false)
const creating = ref(false)
const classrooms = ref([])
const form = ref({ title: '', description: '', requirements: '', classroom_id: null, deadline: null, total_score: 100 })

const columns = [
  { title: '标题', key: 'title' },
  { title: '课堂', dataIndex: 'classroom_name', key: 'classroom_name' },
  { title: '报告数', dataIndex: 'report_count', key: 'report_count' },
  { title: '截止时间', key: 'deadline' },
  { title: '状态', key: 'status' },
  { title: '操作', key: 'action' },
]

async function fetchExps() {
  loading.value = true
  try {
    const res = await api.get('/experiments')
    experiments.value = res.data
  } catch (e) {
    message.error('获取实验列表失败')
  } finally {
    loading.value = false
  }
}

async function fetchClassrooms() {
  try {
    const res = await api.get('/classrooms')
    classrooms.value = res.data
  } catch (e) {}
}

function goDetail(id) {
  router.push(`/experiments/${id}`)
}

async function createExp() {
  if (!form.value.title) { message.warning('请输入标题'); return }
  creating.value = true
  try {
    await api.post('/experiments', {
      ...form.value,
      deadline: form.value.deadline ? form.value.deadline.toISOString() : null,
    })
    message.success('创建成功')
    showCreate.value = false
    form.value = { title: '', description: '', requirements: '', classroom_id: null, deadline: null, total_score: 100 }
    fetchExps()
  } catch (e) {
    message.error('创建失败')
  } finally {
    creating.value = false
  }
}

async function del(id) {
  Modal.confirm({
    title: '确认删除此实验？',
    onOk: async () => {
      try {
        await api.delete(`/experiments/${id}`)
        message.success('已删除')
        fetchExps()
      } catch (e) { message.error('删除失败') }
    }
  })
}

onMounted(() => {
  fetchExps()
  if (userStore.role === 'teacher') fetchClassrooms()
})
</script>
