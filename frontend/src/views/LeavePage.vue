<template>
  <div class="leave-page">
    <a-card title="请假管理">
      <template #extra>
        <a-space>
          <a-select v-model:value="filterStatus" style="width: 120px" placeholder="状态" allowClear @change="fetchLeaves">
            <a-select-option value="pending">待审批</a-select-option>
            <a-select-option value="approved">已通过</a-select-option>
            <a-select-option value="rejected">已拒绝</a-select-option>
          </a-select>
          <a-button v-if="userStore.role === 'student'" type="primary" @click="showModal = true">申请请假</a-button>
        </a-space>
      </template>

      <a-table :columns="columns" :data-source="leaves" row-key="id" :loading="loading" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'status'">
            <a-tag :color="statusColor(record.status)">{{ statusText(record.status) }}</a-tag>
          </template>
          <template v-else-if="column.key === 'leave_type'">
            {{ typeText(record.leave_type) }}
          </template>
          <template v-else-if="column.key === 'action'">
            <a-button v-if="userStore.role !== 'student' && record.status === 'pending'" type="link" size="small" @click="review(record, 'approved')">通过</a-button>
            <a-button v-if="userStore.role !== 'student' && record.status === 'pending'" type="link" size="small" danger @click="review(record, 'rejected')">拒绝</a-button>
          </template>
        </template>
      </a-table>
    </a-card>

    <a-modal v-model:open="showModal" title="申请请假" @ok="submitLeave" :confirm-loading="submitting">
      <a-form layout="vertical">
        <a-form-item label="课堂" required>
          <a-select v-model:value="form.classroom_id" placeholder="选择课堂">
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="请假类型" required>
          <a-select v-model:value="form.leave_type">
            <a-select-option value="sick">病假</a-select-option>
            <a-select-option value="personal">事假</a-select-option>
            <a-select-option value="official">公假</a-select-option>
            <a-select-option value="other">其他</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="开始时间" required>
          <a-date-picker v-model:value="form.start_date" show-time style="width: 100%" />
        </a-form-item>
        <a-form-item label="结束时间" required>
          <a-date-picker v-model:value="form.end_date" show-time style="width: 100%" />
        </a-form-item>
        <a-form-item label="请假原因" required>
          <a-textarea v-model:value="form.reason" :rows="3" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import dayjs from 'dayjs'
import { listLeaves, createLeave, reviewLeave } from '@/api/leave'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const leaves = ref([])
const loading = ref(false)
const filterStatus = ref()
const showModal = ref(false)
const submitting = ref(false)
const classrooms = ref([])
const form = ref({
  classroom_id: null,
  leave_type: 'sick',
  start_date: null,
  end_date: null,
  reason: '',
})

const columns = [
  { title: '学生', dataIndex: 'student_name', key: 'student_name' },
  { title: '课堂', dataIndex: 'classroom_name', key: 'classroom_name' },
  { title: '类型', dataIndex: 'leave_type', key: 'leave_type' },
  { title: '开始时间', dataIndex: 'start_date', key: 'start_date', customRender: ({ text }) => text ? dayjs(text).format('YYYY-MM-DD HH:mm') : '-' },
  { title: '结束时间', dataIndex: 'end_date', key: 'end_date', customRender: ({ text }) => text ? dayjs(text).format('YYYY-MM-DD HH:mm') : '-' },
  { title: '原因', dataIndex: 'reason', key: 'reason', ellipsis: true },
  { title: '状态', key: 'status' },
  { title: '操作', key: 'action' },
]

function statusColor(s) {
  return { pending: 'orange', approved: 'green', rejected: 'red' }[s] || 'default'
}
function statusText(s) {
  return { pending: '待审批', approved: '已通过', rejected: '已拒绝' }[s] || s
}
function typeText(t) {
  return { sick: '病假', personal: '事假', official: '公假', other: '其他' }[t] || t
}

async function fetchLeaves() {
  loading.value = true
  try {
    const params = {}
    if (filterStatus.value) params.status = filterStatus.value
    const res = await listLeaves(params)
    leaves.value = res.data
  } catch (e) {
    message.error('获取请假列表失败')
  } finally {
    loading.value = false
  }
}

async function fetchClassrooms() {
  try {
    const res = await listClassrooms()
    classrooms.value = res.data
  } catch (e) {}
}

async function submitLeave() {
  if (!form.value.classroom_id || !form.value.start_date || !form.value.end_date || !form.value.reason) {
    message.warning('请填写完整')
    return
  }
  submitting.value = true
  try {
    await createLeave({
      classroom_id: form.value.classroom_id,
      leave_type: form.value.leave_type,
      start_date: form.value.start_date.toISOString(),
      end_date: form.value.end_date.toISOString(),
      reason: form.value.reason,
    })
    message.success('请假申请已提交')
    showModal.value = false
    form.value = { classroom_id: null, leave_type: 'sick', start_date: null, end_date: null, reason: '' }
    fetchLeaves()
  } catch (e) {
    message.error('提交失败')
  } finally {
    submitting.value = false
  }
}

async function review(record, status) {
  const feedback = window.prompt(`确认${status === 'approved' ? '通过' : '拒绝'}此请假申请，输入反馈：`, '')
  if (feedback === null) return
  try {
    await reviewLeave(record.id, { status, feedback })
    message.success('已审批')
    fetchLeaves()
  } catch (e) {
    message.error('审批失败')
  }
}

onMounted(() => {
  fetchLeaves()
  if (userStore.role === 'student') fetchClassrooms()
})
</script>
