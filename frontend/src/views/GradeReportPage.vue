<template>
  <div class="cv-page">
    <a-page-header title="综合成绩" sub-title="加权计算总评成绩">
      <template #extra>
        <a-select v-model:value="classroomId" style="width: 200px" placeholder="选择课堂" @change="fetchReport">
          <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
        </a-select>
      </template>
    </a-page-header>

    <a-row :gutter="16" style="margin-bottom: 16px">
      <a-col :span="6">
        <a-card>
          <a-statistic title="学生数" :value="report.students?.length || 0" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="平均总评" :value="avgTotalGrade" :precision="1" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="最高分" :value="maxGrade" :precision="1" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="及格率" :value="passRate" suffix="%" :precision="1" />
        </a-card>
      </a-col>
    </a-row>

    <a-card title="成绩权重配置" size="small" style="margin-bottom: 16px">
      <a-form layout="inline">
        <a-form-item label="作业"><a-input-number v-model:value="weights.homework_weight" :min="0" :max="1" :step="0.05" style="width: 80px" /></a-form-item>
        <a-form-item label="考试"><a-input-number v-model:value="weights.exam_weight" :min="0" :max="1" :step="0.05" style="width: 80px" /></a-form-item>
        <a-form-item label="考勤"><a-input-number v-model:value="weights.attendance_weight" :min="0" :max="1" :step="0.05" style="width: 80px" /></a-form-item>
        <a-form-item label="平时分"><a-input-number v-model:value="weights.usual_weight" :min="0" :max="1" :step="0.05" style="width: 80px" /></a-form-item>
        <a-form-item>
          <a-button type="primary" size="small" @click="saveConfig" :loading="saving">保存配置</a-button>
        </a-form-item>
      </a-form>
    </a-card>

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="report.students || []" row-key="person_id" :pagination="{ pageSize: 20 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'total_grade'">
            <span :style="{ color: record.total_grade >= 60 ? '#52c41a' : '#ff4d4f', fontWeight: 'bold' }">
              {{ record.total_grade }}
            </span>
          </template>
          <template v-else-if="column.key === 'attendance_rate'">
            {{ record.attendance_rate }}%
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 班级知识归因总览 -->
    <a-card title="班级知识归因总览" size="small" style="margin-top: 16px">
      <KnowledgeRadarChart v-if="classRadarData" :radar-data="classRadarData" />
      <a-empty v-else description="暂无归因数据" />
    </a-card>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '../api'
import { getKnowledgeGraph } from '@/api/attribution'
import KnowledgeRadarChart from '@/components/knowledge-radar/KnowledgeRadarChart.vue'

const report = ref({})
const loading = ref(false)
const saving = ref(false)
const classroomId = ref(null)
const classrooms = ref([])
const classRadarData = ref(null)

const weights = reactive({ homework_weight: 0.3, exam_weight: 0.4, attendance_weight: 0.1, usual_weight: 0.2 })

const columns = [
  { key: 'name', title: '学生', dataIndex: 'name' },
  { key: 'homework_avg', title: '作业均分', dataIndex: 'homework_avg' },
  { key: 'exam_avg', title: '考试均分', dataIndex: 'exam_avg' },
  { key: 'attendance_rate', title: '出勤率' },
  { key: 'usual_score', title: '平时分', dataIndex: 'usual_score' },
  { key: 'total_grade', title: '总评成绩' },
]

const avgTotalGrade = computed(() => {
  const s = report.value.students
  if (!s || s.length === 0) return 0
  return (s.reduce((sum, x) => sum + x.total_grade, 0) / s.length).toFixed(1)
})

const maxGrade = computed(() => {
  const s = report.value.students
  if (!s || s.length === 0) return 0
  return Math.max(...s.map(x => x.total_grade)).toFixed(1)
})

const passRate = computed(() => {
  const s = report.value.students
  if (!s || s.length === 0) return 0
  return ((s.filter(x => x.total_grade >= 60).length / s.length) * 100).toFixed(1)
})

async function fetchData() {
  loading.value = true
  try {
    const classRes = await api.get('/classrooms', { _skipGlobalError: true })
    classrooms.value = classRes.data
    if (classRes.data.length === 0) { loading.value = false; return }
    classroomId.value = classRes.data[0].id
    await fetchReport()
  } catch { /* ignore */ } finally { loading.value = false }
}

async function fetchReport() {
  if (!classroomId.value) return
  loading.value = true
  try {
    const [configRes, reportRes] = await Promise.all([
      api.get(`/grades/config/${classroomId.value}`, { _skipGlobalError: true }).catch(() => ({ data: null })),
      api.get(`/grades/report/${classroomId.value}`, { _skipGlobalError: true }).catch(() => ({ data: {} })),
    ])
    if (configRes.data) {
      weights.homework_weight = configRes.data.homework_weight
      weights.exam_weight = configRes.data.exam_weight
      weights.attendance_weight = configRes.data.attendance_weight
      weights.usual_weight = configRes.data.usual_weight
    }
    report.value = reportRes.data

    // 获取班级知识归因数据
    try {
      const graphRes = await getKnowledgeGraph('math')
      if (graphRes.data) {
        classRadarData.value = graphRes.data.radar || graphRes.data
      }
    } catch { /* 归因数据获取失败不影响主流程 */ }
  } catch { /* ignore */ } finally { loading.value = false }
}

async function saveConfig() {
  if (!classroomId.value) return
  saving.value = true
  try {
    await api.post(`/grades/config/${classroomId.value}`, { ...weights })
    message.success('权重配置已保存')
    fetchData()
  } catch { /* ignore */ } finally { saving.value = false }
}

onMounted(fetchData)
</script>
