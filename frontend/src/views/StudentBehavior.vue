<template>
  <div class="cv-page">
    <a-page-header title="学习行为分析" sub-title="学生学习行为画像" />

    <a-card style="margin-bottom: 16px">
      <a-space>
        <a-input-search
          v-model:value="searchStudent"
          placeholder="搜索学生姓名"
          style="width: 300px"
          enter-button
          @search="searchStudents"
        />
        <a-select v-if="classrooms.length" v-model:value="selectedClassroomId" placeholder="按课堂筛选" allow-clear style="width: 200px" @change="filterStudentsByClassroom">
          <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
        </a-select>
        <a-select v-if="studentOptions.length" v-model:value="selectedStudentId" style="width: 200px" placeholder="选择学生" @change="fetchBehavior">
          <a-select-option v-for="s in studentOptions" :key="s.id" :value="s.id">{{ s.name }}</a-select-option>
        </a-select>
      </a-space>
    </a-card>

    <a-spin :spinning="loading">
      <template v-if="behavior">
        <a-row :gutter="16" style="margin-bottom: 16px">
          <a-col :span="6">
            <a-card>
              <a-statistic title="活跃度评分" :value="behavior.activity_score" suffix="/100" :value-style="{ color: behavior.activity_score >= 60 ? '#3f8600' : '#cf1322' }" />
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card>
              <a-statistic title="出勤率" :value="behavior.attendance.rate" suffix="%" />
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card>
              <a-statistic title="作业平均分" :value="behavior.homework.avg_score" />
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card>
              <a-statistic title="考试平均分" :value="behavior.exams.avg_score" />
            </a-card>
          </a-col>
        </a-row>

        <a-row :gutter="16">
          <a-col :span="8">
            <a-card title="作业行为" size="small">
              <a-descriptions :column="1" size="small">
                <a-descriptions-item label="总提交数">{{ behavior.homework.total }}</a-descriptions-item>
                <a-descriptions-item label="已批改">{{ behavior.homework.graded }}</a-descriptions-item>
                <a-descriptions-item label="平均分">{{ behavior.homework.avg_score }}</a-descriptions-item>
              </a-descriptions>
            </a-card>
          </a-col>
          <a-col :span="8">
            <a-card title="考试行为" size="small">
              <a-descriptions :column="1" size="small">
                <a-descriptions-item label="参加次数">{{ behavior.exams.total }}</a-descriptions-item>
                <a-descriptions-item label="平均分">{{ behavior.exams.avg_score }}</a-descriptions-item>
              </a-descriptions>
            </a-card>
          </a-col>
          <a-col :span="8">
            <a-card title="考勤行为" size="small">
              <a-descriptions :column="1" size="small">
                <a-descriptions-item label="出勤">{{ behavior.attendance.present }}</a-descriptions-item>
                <a-descriptions-item label="迟到">{{ behavior.attendance.late }}</a-descriptions-item>
                <a-descriptions-item label="缺勤">{{ behavior.attendance.absent }}</a-descriptions-item>
                <a-descriptions-item label="请假">{{ behavior.attendance.leave }}</a-descriptions-item>
              </a-descriptions>
            </a-card>
          </a-col>
        </a-row>

        <a-card title="注意力分析" size="small" style="margin-top: 16px">
          <a-descriptions :column="2" size="small">
            <a-descriptions-item label="平均注意力">{{ behavior.attention.avg_score }}</a-descriptions-item>
            <a-descriptions-item label="记录次数">{{ behavior.attention.records }}</a-descriptions-item>
          </a-descriptions>
        </a-card>
      </template>
      <a-empty v-else-if="!loading" description="请选择学生查看行为分析" />
    </a-spin>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '@/api'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const searchStudent = ref('')
const studentOptions = ref([])
const allStudentOptions = ref([])  // 缓存全部搜索结果
const selectedStudentId = ref(null)
const selectedClassroomId = ref(undefined)
const classrooms = ref([])
const behavior = ref(null)
const loading = ref(false)

async function searchStudents() {
  if (!searchStudent.value) return
  try {
    const res = await api.get('/persons', { params: { keyword: searchStudent.value, role: 'student' } })
    allStudentOptions.value = res.data || []
    studentOptions.value = allStudentOptions.value
  } catch (e) {
    message.error('搜索失败')
  }
}

async function fetchBehavior(studentId) {
  loading.value = true
  try {
    const res = await api.get(`/students/${studentId}/behavior`, { _skipGlobalError: true })
    behavior.value = res.data
  } catch (e) {
    message.error('获取行为分析失败')
  } finally {
    loading.value = false
  }
}

// 按课堂筛选学生
async function filterStudentsByClassroom() {
  if (!selectedClassroomId.value) {
    studentOptions.value = allStudentOptions.value
    return
  }
  try {
    const res = await api.get(`/classrooms/${selectedClassroomId.value}/students`, { _skipGlobalError: true })
    const classStudentIds = new Set((res.data || []).map(s => s.person_id).filter(Boolean))
    studentOptions.value = allStudentOptions.value.filter(s => classStudentIds.has(s.id))
    // 如果过滤后只有一个学生，自动选中
    if (studentOptions.value.length === 1) {
      selectedStudentId.value = studentOptions.value[0].id
      fetchBehavior(studentOptions.value[0].id)
    }
  } catch {
    studentOptions.value = allStudentOptions.value
  }
}

onMounted(async () => {
  // 教师端加载课堂列表
  if (userStore.role === 'teacher' || userStore.role === 'admin') {
    try {
      const res = await api.get('/classrooms')
      classrooms.value = res.data || []
    } catch { /* ignore */ }
  }
  // 学生端直接加载自己的行为数据
  if (userStore.role === 'student') {
    const user = JSON.parse(localStorage.getItem('user') || '{}')
    if (user.id) fetchBehavior(user.id)
  }
})
</script>
