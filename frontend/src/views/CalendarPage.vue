<template>
  <div class="cv-page" style="max-width: 1000px">
      <a-typography-title :level="3">课程日历</a-typography-title>

      <a-row :gutter="16">
        <a-col :span="8">
          <a-card>
            <a-statistic title="总课堂数" :value="classrooms.length" />
          </a-card>
        </a-col>
        <a-col :span="8">
          <a-card>
            <a-statistic title="进行中" :value="ongoingCount" :value-style="{ color: '#52c41a' }" />
          </a-card>
        </a-col>
        <a-col :span="8">
          <a-card>
            <a-statistic title="已结束" :value="endedCount" :value-style="{ color: '#8c8c8c' }" />
          </a-card>
        </a-col>
      </a-row>

      <a-skeleton v-if="loading && classrooms.length === 0" active :paragraph="{ rows: 4 }" style="margin-top: 16px" />

      <a-card title="即将进行" style="margin-top: 16px" v-if="upcomingClassrooms.length > 0">
        <a-list :data-source="upcomingClassrooms" :loading="loading">
          <template #renderItem="{ item }">
            <a-list-item>
              <a-list-item-meta>
                <template #title>
                  <a href="javascript:void(0)" @click.prevent="$router.push(`/classrooms/${item.id}`)">{{ item.name }}</a>
                </template>
                <template #description>
                  教师：{{ item.teacher || '未指定' }} · 状态：未开始
                </template>
                <template #avatar>
                  <a-avatar style="background-color: var(--cv-color-primary)">{{ (item.name || '')[0] }}</a-avatar>
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>
      </a-card>

      <a-card title="历史课堂" style="margin-top: 16px" v-if="!loading || pastClassrooms.length > 0">
        <a-table
          :columns="columns"
          :data-source="pastClassrooms"
          :loading="loading"
          row-key="id"
          :pagination="{ pageSize: 10 }"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'name'">
              <a href="javascript:void(0)" @click.prevent="$router.push(`/classrooms/${record.id}`)">{{ record.name }}</a>
            </template>
            <template v-if="column.key === 'status'">
              <a-tag :color="record.ended_at ? 'default' : record.started_at ? 'green' : 'blue'">
                {{ record.ended_at ? '已结束' : record.started_at ? '进行中' : '未开始' }}
              </a-tag>
            </template>
            <template v-if="column.key === 'started_at'">
              {{ record.started_at ? formatDate(record.started_at) : '-' }}
            </template>
            <template v-if="column.key === 'ended_at'">
              {{ record.ended_at ? formatDate(record.ended_at) : '-' }}
            </template>
            <template v-if="column.key === 'avg_attention'">
              <a-tag :color="(record.avg_attention || 0) >= 60 ? 'green' : (record.avg_attention || 0) >= 30 ? 'orange' : 'red'">
                {{ record.avg_attention != null ? record.avg_attention.toFixed(1) : '-' }}
              </a-tag>
            </template>
          </template>
        </a-table>
      </a-card>

      <!-- 近期事项 -->
      <a-card title="近期事项" style="margin-top: 16px" v-if="upcomingEvents.length > 0">
        <a-list :data-source="upcomingEvents" size="small">
          <template #renderItem="{ item }">
            <a-list-item>
              <a-list-item-meta>
                <template #title>{{ item.title }}<span v-if="item.classroom_name" style="color: #8c8c8c; font-weight: normal; margin-left: 6px; font-size: 12px">（{{ item.classroom_name }}）</span></template>
                <template #description>
                  <a-tag :color="item.type === 'homework' ? 'green' : item.type === 'exam' ? 'orange' : 'blue'" style="margin-right: 4px">
                    {{ { homework: '作业截止', exam: '考试', checkin: '签到' }[item.type] }}
                  </a-tag>
                  {{ item.time ? formatDate(item.time) : '待定' }}
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>
      </a-card>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { listClassrooms } from '@/api/classroom'
import { listAssignedHomework, listHomework } from '@/api/homework'
import { listAssignedExams, listExams } from '@/api/exam'
import { getCheckinHistory, listCheckinSessions } from '@/api/checkin'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const isStudent = computed(() => userStore.role === 'student')

const classrooms = ref([])
const loading = ref(true)

const columns = [
  { title: '课程', key: 'name' },
  { title: '教师', dataIndex: 'teacher', key: 'teacher' },
  { title: '状态', key: 'status' },
  { title: '开始时间', key: 'started_at' },
  { title: '结束时间', key: 'ended_at' },
  { title: '时长(分)', dataIndex: 'duration', key: 'duration' },
  { title: '注意力', key: 'avg_attention' },
  { title: '人数', dataIndex: 'total_students', key: 'total_students' },
]

const ongoingCount = computed(() => classrooms.value.filter(c => c.started_at && !c.ended_at).length)
const endedCount = computed(() => classrooms.value.filter(c => c.ended_at).length)
const upcomingClassrooms = computed(() => classrooms.value.filter(c => !c.started_at && !c.ended_at).slice(0, 5))
const pastClassrooms = computed(() => classrooms.value.filter(c => c.started_at))

const upcomingEvents = computed(() => {
  const events = []
  // 收集作业截止日
  for (const hw of homeworks.value) {
    if (hw.deadline && hw.status === 'open') {
      events.push({ title: hw.title, type: 'homework', time: hw.deadline, sort: new Date(hw.deadline).getTime(), classroom_name: hw.classroom_name || '' })
    }
  }
  // 收集考试
  for (const exam of exams.value) {
    if (exam.status === 'published') {
      events.push({ title: exam.title, type: 'exam', time: exam.start_time, sort: exam.start_time ? new Date(exam.start_time).getTime() : Date.now() + 86400000 })
    }
  }
  // 收集活跃签到
  for (const ci of checkins.value) {
    if (ci.status === 'active') {
      events.push({ title: `签到 - ${ci.classroom_name}`, type: 'checkin', time: ci.start_time, sort: new Date(ci.start_time).getTime() })
    }
  }
  return events.sort((a, b) => a.sort - b.sort).slice(0, 10)
})

const homeworks = ref([])
const exams = ref([])
const checkins = ref([])

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleString('zh-CN')
}

async function loadClassrooms() {
  loading.value = true
  try {
    if (isStudent.value) {
      // 学生端：使用学生专属API
      const [classRes, hwRes, examRes, checkinRes] = await Promise.all([
        listClassrooms({}, { _skipGlobalError: true }).catch(() => ({ data: [] })),
        listAssignedHomework().catch(() => ({ data: [] })),
        listAssignedExams().catch(() => ({ data: [] })),
        getCheckinHistory({ _skipGlobalError: true }).catch(() => ({ data: [] })),
      ])
      classrooms.value = classRes.data || []
      homeworks.value = hwRes.data || []
      exams.value = examRes.data || []
      // 学生端签到历史格式不同，转换一下
      checkins.value = (checkinRes.data || []).map(c => ({
        classroom_name: c.classroom_name || '',
        status: c.status === 'present' ? 'active' : 'closed',
        start_time: c.checkin_time || c.created_at,
      }))
    } else {
      // 教师端：使用教师专属API
      const [classRes, hwRes, examRes, checkinRes] = await Promise.all([
        listClassrooms(),
        listHomework({}, { _skipGlobalError: true }).catch(() => ({ data: [] })),
        listExams({}, { _skipGlobalError: true }).catch(() => ({ data: [] })),
        listCheckinSessions({ _skipGlobalError: true }).catch(() => ({ data: [] })),
      ])
      classrooms.value = classRes.data || []
      homeworks.value = hwRes.data || []
      exams.value = examRes.data || []
      checkins.value = checkinRes.data || []
    }
  } catch (e) {
    message.error('加载课堂数据失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadClassrooms()
})
</script>
