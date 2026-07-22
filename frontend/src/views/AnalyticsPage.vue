<template>
  <div class="cv-page">
      <a-typography-title :level="3">数据分析</a-typography-title>

      <a-row :gutter="16">
        <a-col :span="6">
          <a-card>
            <a-statistic title="总课堂数" :value="stats.totalClassrooms" :loading="loading" />
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card>
            <a-statistic title="总学生数" :value="stats.totalStudents" :loading="loading" />
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card>
            <a-statistic title="总教师数" :value="stats.totalTeachers" :loading="loading" />
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card>
            <a-statistic
              title="平均注意力"
              :value="stats.avgAttention"
              :loading="loading"
              :precision="1"
              :value-style="{ color: attentionColor }"
            />
          </a-card>
        </a-col>
      </a-row>

      <a-row :gutter="16" style="margin-top: 16px">
        <a-col :span="6">
          <a-card>
            <a-statistic title="作业总数" :value="homeworks.length" :loading="loading" />
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card>
            <a-statistic title="待批改作业" :value="pendingHwCount" :loading="loading" :value-style="{ color: '#fa8c16' }" />
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card>
            <a-statistic title="考试总数" :value="exams.length" :loading="loading" />
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card>
            <a-statistic title="考试平均分" :value="avgExamScore" :loading="loading" :precision="1" />
          </a-card>
        </a-col>
      </a-row>

      <a-row :gutter="16">
        <a-col :span="12">
          <a-card title="注意力分布" :loading="loading">
            <div class="dist-bar" v-for="item in attentionDist" :key="item.label">
              <span class="dist-label">{{ item.label }}</span>
              <div class="dist-track">
                <div class="dist-fill" :style="{ width: item.percent + '%', background: item.color }"></div>
              </div>
              <span class="dist-count">{{ item.count }}</span>
            </div>
          </a-card>
        </a-col>
        <a-col :span="12">
          <a-card title="课堂状态分布" :loading="loading">
            <div class="dist-bar" v-for="item in statusDist" :key="item.label">
              <span class="dist-label">{{ item.label }}</span>
              <div class="dist-track">
                <div class="dist-fill" :style="{ width: item.percent + '%', background: item.color }"></div>
              </div>
              <span class="dist-count">{{ item.count }}</span>
            </div>
          </a-card>
        </a-col>
      </a-row>

      <!-- 趋势分析 -->
      <a-row :gutter="16" style="margin-top: 16px">
        <a-col :span="12">
          <a-card title="注意力趋势（近10次课堂）" :loading="loading">
            <div class="trend-chart">
              <div v-for="(val, i) in attentionTrend" :key="i" class="trend-bar-wrap">
                <div class="trend-bar" :style="{ height: val + '%', background: val >= 60 ? '#52c41a' : val >= 30 ? '#fa8c16' : '#ff4d4f' }"></div>
                <span class="trend-label">{{ i + 1 }}</span>
              </div>
            </div>
          </a-card>
        </a-col>
        <a-col :span="12">
          <a-card title="课堂规模分布" :loading="loading">
            <div class="dist-bar" v-for="item in sizeDist" :key="item.label">
              <span class="dist-label">{{ item.label }}</span>
              <div class="dist-track">
                <div class="dist-fill" :style="{ width: item.percent + '%', background: item.color }"></div>
              </div>
              <span class="dist-count">{{ item.count }}</span>
            </div>
          </a-card>
        </a-col>
      </a-row>

      <a-card title="最近课堂" style="margin-top: 16px" :loading="loading">
        <a-table
          :columns="columns"
          :data-source="recentClassrooms"
          row-key="id"
          :pagination="{ pageSize: 8 }"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'status'">
              <a-tag :color="record.ended_at ? 'default' : record.started_at ? 'green' : 'blue'">
                {{ record.ended_at ? '已结束' : record.started_at ? '进行中' : '未开始' }}
              </a-tag>
            </template>
            <template v-if="column.key === 'avg_attention'">
              <a-tag :color="(record.avg_attention || 0) >= 60 ? 'green' : (record.avg_attention || 0) >= 30 ? 'orange' : 'red'">
                {{ record.avg_attention != null ? record.avg_attention.toFixed(1) : '-' }}
              </a-tag>
            </template>
          </template>
        </a-table>
      </a-card>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '@/api'

const classrooms = ref([])
const persons = ref([])
const loading = ref(true)

const columns = [
  { title: '课程', dataIndex: 'name', key: 'name' },
  { title: '教师', dataIndex: 'teacher', key: 'teacher' },
  { title: '状态', key: 'status' },
  { title: '人数', dataIndex: 'total_students', key: 'total_students' },
  { title: '平均注意力', key: 'avg_attention' },
  { title: '时长(分)', dataIndex: 'duration', key: 'duration' },
]

const stats = computed(() => {
  const totalClassrooms = classrooms.value.length
  const totalStudents = persons.value.filter(p => p.role === 'student').length
  const totalTeachers = persons.value.filter(p => p.role === 'teacher').length
  const attentionScores = classrooms.value.filter(c => c.avg_attention != null).map(c => c.avg_attention)
  const avgAttention = attentionScores.length > 0
    ? attentionScores.reduce((a, b) => a + b, 0) / attentionScores.length
    : 0
  return { totalClassrooms, totalStudents, totalTeachers, avgAttention }
})

const attentionColor = computed(() => {
  const s = stats.value.avgAttention
  if (s >= 60) return '#52c41a'
  if (s >= 30) return '#faad14'
  return '#ff4d4f'
})

const attentionDist = computed(() => {
  const high = classrooms.value.filter(c => (c.avg_attention || 0) >= 60).length
  const medium = classrooms.value.filter(c => (c.avg_attention || 0) >= 30 && (c.avg_attention || 0) < 60).length
  const low = classrooms.value.filter(c => (c.avg_attention || 0) < 30).length
  const total = classrooms.value.length || 1
  return [
    { label: '高（≥60）', count: high, percent: (high / total * 100).toFixed(0), color: '#52c41a' },
    { label: '中（30-59）', count: medium, percent: (medium / total * 100).toFixed(0), color: '#faad14' },
    { label: '低（<30）', count: low, percent: (low / total * 100).toFixed(0), color: '#ff4d4f' },
  ]
})

const statusDist = computed(() => {
  const ongoing = classrooms.value.filter(c => c.started_at && !c.ended_at).length
  const ended = classrooms.value.filter(c => c.ended_at).length
  const notStarted = classrooms.value.filter(c => !c.started_at).length
  const total = classrooms.value.length || 1
  return [
    { label: '进行中', count: ongoing, percent: (ongoing / total * 100).toFixed(0), color: '#52c41a' },
    { label: '已结束', count: ended, percent: (ended / total * 100).toFixed(0), color: '#8c8c8c' },
    { label: '未开始', count: notStarted, percent: (notStarted / total * 100).toFixed(0), color: '#1890ff' },
  ]
})

const recentClassrooms = computed(() => classrooms.value.slice(0, 20))

const attentionTrend = computed(() => {
  return classrooms.value
    .filter(c => c.avg_attention != null)
    .slice(0, 10)
    .reverse()
    .map(c => Math.round(c.avg_attention || 0))
})

const sizeDist = computed(() => {
  const small = classrooms.value.filter(c => (c.student_count || 0) < 20).length
  const medium = classrooms.value.filter(c => (c.student_count || 0) >= 20 && (c.student_count || 0) < 50).length
  const large = classrooms.value.filter(c => (c.student_count || 0) >= 50).length
  const total = small + medium + large || 1
  return [
    { label: '<20人', count: small, percent: (small / total * 100).toFixed(0), color: '#1890ff' },
    { label: '20-50人', count: medium, percent: (medium / total * 100).toFixed(0), color: '#52c41a' },
    { label: '>50人', count: large, percent: (large / total * 100).toFixed(0), color: '#fa8c16' },
  ]
})

const homeworks = ref([])
const exams = ref([])
const pendingHwCount = computed(() => homeworks.value.filter(h => h.status === 'open').length)
const avgExamScore = computed(() => {
  const graded = exams.value.filter(e => e.status === 'closed')
  if (graded.length === 0) return 0
  return graded.reduce((sum, e) => sum + (e.avg_score || 0), 0) / graded.length
})

async function loadData() {
  loading.value = true
  try {
    const [classroomRes, personRes, hwRes, examRes] = await Promise.all([
      api.get('/classrooms'),
      api.get('/persons'),
      api.get('/homework', { _skipGlobalError: true }).catch(() => ({ data: [] })),
      api.get('/exams', { _skipGlobalError: true }).catch(() => ({ data: [] })),
    ])
    classrooms.value = classroomRes.data || []
    persons.value = personRes.data || []
    homeworks.value = hwRes.data || []
    exams.value = examRes.data || []
  } catch (e) {
    message.error('加载数据失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadData()
})
</script>

<style scoped>
.dist-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}
.dist-label {
  width: 100px;
  font-size: 13px;
  color: #666;
  flex-shrink: 0;
}
.dist-track {
  flex: 1;
  height: 20px;
  background: #f0f0f0;
  border-radius: 10px;
  overflow: hidden;
}
.dist-fill {
  height: 100%;
  border-radius: 10px;
  transition: width 0.3s ease;
  min-width: 2px;
}
.dist-count {
  width: 40px;
  text-align: right;
  font-size: 13px;
  font-weight: 600;
  color: #333;
}
.trend-chart {
  display: flex;
  align-items: flex-end;
  height: 120px;
  gap: 8px;
  padding: 0 10px;
}
.trend-bar-wrap {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  justify-content: flex-end;
}
.trend-bar {
  width: 100%;
  max-width: 30px;
  border-radius: 3px 3px 0 0;
  min-height: 2px;
  transition: height 0.3s;
}
.trend-label {
  font-size: 10px;
  color: #999;
  margin-top: 4px;
}
</style>
