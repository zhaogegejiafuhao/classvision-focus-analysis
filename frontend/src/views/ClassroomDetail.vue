<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 18px; font-weight: bold; cursor: pointer" @click="$router.push('/')">
        ClassVision 课眼智析
      </span>
      <a-button type="link" style="color: #fff" @click="$router.push('/classrooms')">返回列表</a-button>
    </a-layout-header>
    <a-layout-content style="padding: 24px">
      <a-spin :spinning="loading">
        <template v-if="classroom">
          <a-page-header :title="classroom.name" :sub-title="`${classroom.teacher} · ${classroom.duration}分钟`" />

          <a-row :gutter="16" style="margin-bottom: 16px">
            <a-col :span="6">
              <a-card><a-statistic title="总人数" :value="classroom.total_students" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="平均注意力" :value="classroom.avg_attention" suffix="/100" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="低头人次" :value="classroom.stats?.head_down_count || 0" :value-style="{ color: '#cf1322' }" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="疲劳人次" :value="classroom.stats?.fatigue_count || 0" :value-style="{ color: '#722ed1' }" /></a-card>
            </a-col>
          </a-row>

          <a-card title="注意力趋势" style="margin-bottom: 16px">
            <div ref="timelineEl" style="width: 100%; height: 300px" />
          </a-card>

          <a-row :gutter="16">
            <a-col :span="12">
              <a-card title="学生列表">
                <a-table :columns="studentCols" :data-source="students" row-key="id" size="small" />
              </a-card>
            </a-col>
            <a-col :span="12">
              <a-card title="AI 课堂分析报告">
                <div v-if="report">
                  <div v-html="renderMarkdown(report.content)" />
                  <a-typography-text type="secondary">
                    生成时间：{{ new Date(report.created_at).toLocaleString('zh-CN') }}
                  </a-typography-text>
                </div>
                <a-empty v-else description="尚未生成报告">
                  <a-button type="primary" @click="genReport" :loading="genLoading">生成报告</a-button>
                </a-empty>
              </a-card>
            </a-col>
          </a-row>
        </template>
      </a-spin>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import * as echarts from 'echarts'
import axios from 'axios'

const route = useRoute()
const classroomId = route.params.id

const classroom = ref(null)
const students = ref([])
const report = ref(null)
const loading = ref(true)
const genLoading = ref(false)
const timelineEl = ref(null)

const studentCols = [
  { title: '姓名', dataIndex: 'name', key: 'name' },
  { title: '平均注意力', dataIndex: 'avg_attention', key: 'avg_attention' },
  { title: '低头次数', dataIndex: 'head_down_count', key: 'head_down_count' },
  { title: '眨眼次数', dataIndex: 'blink_count', key: 'blink_count' },
]

function renderMarkdown(text) {
  return text.replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>')
}

async function genReport() {
  genLoading.value = true
  try {
    const res = await axios.post(`/api/classrooms/${classroomId}/report`)
    report.value = res.data
  } finally {
    genLoading.value = false
  }
}

onMounted(async () => {
  try {
    const [classRes, studentRes, timelineRes] = await Promise.all([
      axios.get(`/api/classrooms/${classroomId}`),
      axios.get(`/api/classrooms/${classroomId}/students`),
      axios.get(`/api/classrooms/${classroomId}/timeline`),
    ])
    classroom.value = classRes.data
    students.value = studentRes.data

    await nextTick()
    const chart = echarts.init(timelineEl.value)
    chart.setOption({
      grid: { top: 20, bottom: 30, left: 50, right: 20 },
      xAxis: { type: 'category', data: timelineRes.data.map(d => d.timestamp) },
      yAxis: { type: 'value', max: 100, min: 0, name: '注意力' },
      series: [{
        type: 'line', data: timelineRes.data.map(d => d.avg_attention),
        smooth: true, areaStyle: { opacity: 0.2 }, itemStyle: { color: '#1890ff' },
      }],
    })

    try {
      const reportRes = await axios.get(`/api/classrooms/${classroomId}/report`)
      report.value = reportRes.data
    } catch { /* 报告未生成 */ }
  } finally {
    loading.value = false
  }
})
</script>
