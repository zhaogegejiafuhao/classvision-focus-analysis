<template>
  <div class="cv-page">
    <a-page-header :title="session?.classroom_name || '签到详情'" @back="() => $router.push('/checkin')">
      <template #subTitle>
        <a-tag v-if="session" :color="session.status === 'active' ? 'green' : 'default'">
          {{ session.status === 'active' ? '进行中' : '已结束' }}
        </a-tag>
      </template>
      <template #extra>
        <a-button @click="exportCSV">导出CSV</a-button>
        <template v-if="session?.status === 'active'">
          <a-button v-if="session.type === 'encrypted'" type="primary" @click="showCode = !showCode">
            {{ showCode ? '隐藏验证码' : '显示验证码' }}
          </a-button>
          <a-popconfirm title="确定结束签到？" @confirm="closeSession">
            <a-button type="primary" danger>结束签到</a-button>
          </a-popconfirm>
        </template>
      </template>
    </a-page-header>

    <a-spin :spinning="loading">
      <a-row :gutter="16">
        <!-- 左侧：签到信息 -->
        <a-col :span="8">
          <a-card title="签到信息" size="small">
            <p><strong>签到类型：</strong>
              <a-tag :color="session?.type === 'encrypted' ? 'orange' : 'blue'">
                {{ session?.type === 'encrypted' ? '加密签到' : '普通签到' }}
              </a-tag>
            </p>
            <p><strong>开始时间：</strong>{{ session?.start_time }}</p>
            <p v-if="session?.end_time"><strong>结束时间：</strong>{{ session?.end_time }}</p>
            
            <div v-if="showCode && session?.code" style="margin-top: 16px; padding: 16px; background: #fff7e6; border-radius: 8px; text-align: center">
              <div style="font-size: 12px; color: #999">验证码</div>
              <div style="font-size: 32px; font-weight: bold; color: #fa8c16; letter-spacing: 8px">{{ session.code }}</div>
              <div style="font-size: 12px; color: #999; margin-top: 8px">请将验证码告知学生</div>
            </div>

            <a-progress 
              style="margin-top: 16px" 
              :percent="session?.total_count > 0 ? Math.round(session.checked_count / session.total_count * 100) : 0" 
              :format="(p) => `${session?.checked_count || 0}/${session?.total_count || 0}人`"
            />
          </a-card>

          <a-card title="签到统计" size="small" style="margin-top: 16px">
            <a-row>
              <a-col :span="8" style="text-align: center">
                <div style="font-size: 24px; color: #52c41a">{{ stats.present }}</div>
                <div style="color: #999">已签到</div>
              </a-col>
              <a-col :span="8" style="text-align: center">
                <div style="font-size: 24px; color: #ff4d4f">{{ stats.absent }}</div>
                <div style="color: #999">未签到</div>
              </a-col>
              <a-col :span="8" style="text-align: center">
                <div style="font-size: 24px; color: #1890ff">{{ stats.rate }}%</div>
                <div style="color: #999">出勤率</div>
              </a-col>
            </a-row>
          </a-card>
        </a-col>

        <!-- 右侧：学生列表 -->
        <a-col :span="16">
          <a-card title="学生签到状态" size="small">
            <a-table :columns="attendanceColumns" :data-source="attendances" row-key="id" size="small">
              <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'status'">
                  <a-tag :color="record.status === 'present' ? 'green' : 'red'">
                    {{ record.status === 'present' ? '已签到' : '未签到' }}
                  </a-tag>
                </template>
                <template v-else-if="column.key === 'checkin_time'">
                  {{ record.checkin_time ? new Date(record.checkin_time).toLocaleString('zh-CN') : '-' }}
                </template>
              </template>
            </a-table>
          </a-card>
        </a-col>
      </a-row>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../api'

const route = useRoute()
const router = useRouter()
const sessionId = route.params.id

const session = ref(null)
const attendances = ref([])
const loading = ref(false)
const showCode = ref(false)

const attendanceColumns = [
  { key: 'student_name', title: '学生', dataIndex: 'student_name' },
  { key: 'status', title: '状态', dataIndex: 'status' },
  { key: 'checkin_time', title: '签到时间', dataIndex: 'checkin_time' },
]

const stats = computed(() => {
  if (!attendances.value.length) return { present: 0, absent: 0, rate: 0 }
  const present = attendances.value.filter(a => a.status === 'present').length
  const absent = attendances.value.filter(a => a.status !== 'present').length
  const rate = Math.round(present / attendances.value.length * 100)
  return { present, absent, rate }
})

async function fetchSession() {
  loading.value = true
  try {
    const res = await api.get(`/checkin/sessions/${sessionId}`)
    session.value = {
      ...res.data,
      start_time: new Date(res.data.start_time).toLocaleString('zh-CN'),
      end_time: res.data.end_time ? new Date(res.data.end_time).toLocaleString('zh-CN') : null,
    }
  } catch (e) {
    message.error('获取签到详情失败')
  } finally {
    loading.value = false
  }
}

async function fetchAttendances() {
  try {
    const res = await api.get(`/checkin/sessions/${sessionId}/attendances`)
    attendances.value = res.data
  } catch (e) {
    // 忽略
  }
}

async function closeSession() {
  try {
    await api.post(`/checkin/sessions/${sessionId}/close`)
    message.success('签到已结束')
    fetchSession()
    fetchAttendances()
  } catch (e) {
    message.error('操作失败')
  }
}

async function exportCSV() {
  try {
    const res = await api.get(`/checkin/sessions/${sessionId}/export`, { responseType: 'blob' })
    const url = window.URL.createObjectURL(new Blob([res.data], { type: 'text/csv' }))
    const link = document.createElement('a')
    link.href = url
    link.download = `考勤记录_${sessionId}.csv`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  } catch (e) {
    message.error('导出失败')
  }
}

onMounted(() => {
  fetchSession()
  fetchAttendances()
})
</script>