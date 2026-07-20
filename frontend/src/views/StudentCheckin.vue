<template>
  <div class="cv-page">
    <a-page-header title="我的考勤" sub-title="签到和考勤记录" />

    <a-row :gutter="16">
      <!-- 左侧：当前签到 -->
      <a-col :span="8">
        <a-card title="当前签到" :loading="checkLoading">
          <div v-if="activeCheckin.active">
            <a-tag :color="activeCheckin.type === 'encrypted' ? 'orange' : 'blue'" style="margin-bottom: 12px">
              {{ activeCheckin.type === 'encrypted' ? '加密签到' : '普通签到' }}
            </a-tag>
            
            <div v-if="activeCheckin.checked" style="text-align: center; padding: 20px">
              <a-result status="success" title="已签到" sub-title="签到成功" />
            </div>
            
            <div v-else>
              <a-input 
                v-if="activeCheckin.type === 'encrypted'" 
                v-model:value="checkinCode" 
                placeholder="请输入6位验证码" 
                :maxlength="6"
                style="margin-bottom: 12px" 
              />
              <a-button type="primary" block @click="doCheckin" :loading="submitting">
                {{ activeCheckin.type === 'encrypted' ? '验证签到' : '立即签到' }}
              </a-button>
            </div>
          </div>
          <a-empty v-else description="当前无进行中的签到" />
        </a-card>

        <a-card title="选择课堂" size="small" style="margin-top: 16px">
          <a-select v-model:value="selectedClassroom" placeholder="选择课堂" style="width: 100%" @change="fetchActiveCheckin">
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-card>
      </a-col>

      <!-- 右侧：签到历史 -->
      <a-col :span="16">
        <a-card title="签到历史" :loading="historyLoading">
          <a-table :columns="historyColumns" :data-source="history" row-key="id" size="small">
            <template #bodyCell="{ column, record }">
              <template v-if="column.key === 'status'">
                <a-tag :color="record.status === 'present' ? 'green' : record.status === 'late' ? 'orange' : 'red'">
                  {{ { present: '已签到', absent: '缺勤', late: '迟到', leave: '请假' }[record.status] || record.status }}
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '../api'

const classrooms = ref([])
const selectedClassroom = ref(null)
const activeCheckin = ref({ active: false })
const history = ref([])
const checkLoading = ref(false)
const historyLoading = ref(false)
const submitting = ref(false)
const checkinCode = ref('')

const historyColumns = [
  { key: 'classroom_name', title: '课堂', dataIndex: 'classroom_name' },
  { key: 'status', title: '状态' },
  { key: 'checkin_time', title: '签到时间' },
]

async function fetchClassrooms() {
  try {
    const res = await api.get('/classrooms')
    classrooms.value = res.data
    if (res.data.length > 0) {
      selectedClassroom.value = res.data[0].id
      fetchActiveCheckin()
    }
  } catch (e) {
    // 忽略
  }
}

async function fetchActiveCheckin() {
  if (!selectedClassroom.value) return
  checkLoading.value = true
  try {
    const res = await api.get(`/checkin/active?classroom_id=${selectedClassroom.value}`)
    activeCheckin.value = res.data
  } catch (e) {
    activeCheckin.value = { active: false }
  } finally {
    checkLoading.value = false
  }
}

async function doCheckin() {
  if (activeCheckin.value.type === 'encrypted' && checkinCode.value.length !== 6) {
    message.error('请输入6位验证码')
    return
  }
  submitting.value = true
  try {
    await api.post('/checkin/submit', {
      session_id: activeCheckin.value.session_id,
      code: checkinCode.value || undefined,
    })
    message.success('签到成功')
    activeCheckin.value.checked = true
    fetchHistory()
  } catch (e) {
    message.error(e.response?.data?.detail || '签到失败')
  } finally {
    submitting.value = false
  }
}

async function fetchHistory() {
  historyLoading.value = true
  try {
    const res = await api.get('/checkin/history')
    history.value = res.data
  } catch (e) {
    // 忽略
  } finally {
    historyLoading.value = false
  }
}

onMounted(() => {
  fetchClassrooms()
  fetchHistory()
})
</script>