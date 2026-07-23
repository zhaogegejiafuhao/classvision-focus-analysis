<template>
  <div class="cv-page">
    <a-page-header title="考勤管理" sub-title="创建和管理签到">
      <template #extra>
        <a-button type="primary" @click="showCreateModal = true">发起签到</a-button>
      </template>
    </a-page-header>

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="sessions" row-key="id">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'classroom_name'">
            {{ record.classroom_name }}
          </template>
          <template v-else-if="column.key === 'type'">
            <a-tag :color="record.type === 'encrypted' ? 'orange' : 'blue'">
              {{ record.type === 'encrypted' ? '加密签到' : '普通签到' }}
            </a-tag>
          </template>
          <template v-else-if="column.key === 'status'">
            <a-tag :color="record.status === 'active' ? 'green' : 'default'">
              {{ record.status === 'active' ? '进行中' : '已结束' }}
            </a-tag>
          </template>
          <template v-else-if="column.key === 'progress'">
            <a-progress :percent="record.total_count > 0 ? Math.round(record.checked_count / record.total_count * 100) : 0" size="small" />
            <span style="margin-left: 8px">{{ record.checked_count }}/{{ record.total_count }}</span>
          </template>
          <template v-else-if="column.key === 'action'">
            <a-space>
              <a-button type="link" size="small" @click="goDetail(record.id)">详情</a-button>
              <a-popconfirm v-if="record.status === 'active'" title="确定结束签到？" @confirm="closeSession(record.id)">
                <a-button type="link" danger size="small">结束</a-button>
              </a-popconfirm>
            </a-space>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 创建签到弹窗 -->
    <a-modal v-model:open="showCreateModal" title="发起签到" @ok="createSession" :confirm-loading="submitting">
      <a-form :label-col="{ span: 6 }">
        <a-form-item label="选择课堂" required>
          <a-select v-model:value="form.classroom_id" placeholder="选择课堂" style="width: 100%">
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="签到类型">
          <a-radio-group v-model:value="form.type">
            <a-radio value="normal">普通签到</a-radio>
            <a-radio value="encrypted">加密签到</a-radio>
          </a-radio-group>
          <div v-if="form.type === 'encrypted'" style="color: #999; font-size: 12px">
            加密签到会生成6位数字验证码，学生需要输入正确的验证码才能签到
          </div>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import { listCheckinSessions, createCheckinSession, closeCheckinSession } from '@/api/checkin'
import { listClassrooms } from '@/api/classroom'

const router = useRouter()
const sessions = ref([])
const classrooms = ref([])
const loading = ref(false)
const submitting = ref(false)
const showCreateModal = ref(false)

const form = ref({
  classroom_id: null,
  type: 'normal',
})

const columns = [
  { key: 'classroom_name', title: '课堂', dataIndex: 'classroom_name' },
  { key: 'type', title: '类型', dataIndex: 'type' },
  { key: 'start_time', title: '开始时间', dataIndex: 'start_time' },
  { key: 'progress', title: '签到进度' },
  { key: 'status', title: '状态', dataIndex: 'status' },
  { key: 'action', title: '操作' },
]

async function fetchSessions() {
  loading.value = true
  try {
    const res = await listCheckinSessions()
    sessions.value = res.data.map(s => ({
      ...s,
      start_time: new Date(s.start_time).toLocaleString('zh-CN'),
    }))
  } catch (e) {
    message.error('获取签到列表失败')
  } finally {
    loading.value = false
  }
}

async function fetchClassrooms() {
  try {
    const res = await listClassrooms()
    classrooms.value = res.data
  } catch (e) {
    // 忽略
  }
}

async function createSession() {
  if (!form.value.classroom_id) {
    message.error('请选择课堂')
    return
  }
  submitting.value = true
  try {
    const res = await createCheckinSession({
      classroom_id: form.value.classroom_id,
      type: form.value.type,
    })
    message.success('签到已发起')
    showCreateModal.value = false
    form.value = { classroom_id: null, type: 'normal' }
    
    // 如果是加密签到，显示验证码
    if (res.data.type === 'encrypted' && res.data.code) {
      message.info(`验证码: ${res.data.code}`, 10)
    }
    
    fetchSessions()
  } catch (e) {
    message.error(e.response?.data?.detail || '发起失败')
  } finally {
    submitting.value = false
  }
}

async function closeSession(id) {
  try {
    await closeCheckinSession(id)
    message.success('签到已结束')
    fetchSessions()
  } catch (e) {
    message.error('操作失败')
  }
}

function goDetail(id) {
  router.push(`/checkin/${id}`)
}

onMounted(() => {
  fetchSessions()
  fetchClassrooms()
})
</script>