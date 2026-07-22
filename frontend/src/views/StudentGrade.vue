<template>
  <div class="cv-page">
    <a-page-header title="我的成绩" sub-title="查看综合成绩和各项得分" />

    <a-spin :spinning="loading">
      <template v-if="report && report.students">
        <a-row :gutter="16" style="margin-bottom: 16px">
          <a-col :span="6">
            <a-card>
              <a-statistic title="作业均分" :value="myGrade?.homework_avg || 0" :precision="1" />
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card>
              <a-statistic title="考试均分" :value="myGrade?.exam_avg || 0" :precision="1" />
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card>
              <a-statistic title="出勤率" :value="myGrade?.attendance_rate || 0" suffix="%" :precision="1" />
            </a-card>
          </a-col>
          <a-col :span="6">
            <a-card>
              <a-statistic
                title="总评成绩"
                :value="myGrade?.total_grade || 0"
                :precision="1"
                :value-style="{ color: (myGrade?.total_grade || 0) >= 60 ? '#3f8600' : '#cf1322', fontWeight: 'bold' }"
              />
            </a-card>
          </a-col>
        </a-row>

        <a-card title="成绩构成" size="small" v-if="report.config">
          <a-descriptions bordered size="small" :column="2">
            <a-descriptions-item label="作业权重">{{ (report.config.homework_weight * 100).toFixed(0) }}%</a-descriptions-item>
            <a-descriptions-item label="考试权重">{{ (report.config.exam_weight * 100).toFixed(0) }}%</a-descriptions-item>
            <a-descriptions-item label="考勤权重">{{ (report.config.attendance_weight * 100).toFixed(0) }}%</a-descriptions-item>
            <a-descriptions-item label="平时分权重">{{ (report.config.usual_weight * 100).toFixed(0) }}%</a-descriptions-item>
          </a-descriptions>
        </a-card>

        <a-card title="班级排名" size="small" style="margin-top: 16px">
          <a-table :columns="rankColumns" :data-source="report.students" row-key="person_id" size="small" :pagination="{ pageSize: 20 }">
            <template #bodyCell="{ column, record }">
              <template v-if="column.key === 'total_grade'">
                <span :style="{ color: record.total_grade >= 60 ? '#52c41a' : '#ff4d4f', fontWeight: record.person_id === myPersonId ? 'bold' : 'normal' }">
                  {{ record.total_grade }}
                </span>
              </template>
              <template v-else-if="column.key === 'name'">
                <span :style="{ fontWeight: record.person_id === myPersonId ? 'bold' : 'normal' }">
                  {{ record.name }}{{ record.person_id === myPersonId ? '（我）' : '' }}
                </span>
              </template>
              <template v-else-if="column.key === 'attendance_rate'">
                {{ record.attendance_rate }}%
              </template>
            </template>
          </a-table>
        </a-card>

        <a-card title="成绩趋势" size="small" style="margin-top: 16px">
          <a-button type="primary" size="small" @click="fetchTrend" :loading="trendLoading">加载趋势</a-button>
          <div v-if="trend" style="margin-top: 16px">
            <a-row :gutter="16" style="margin-bottom: 16px">
              <a-col :span="12"><a-statistic title="作业平均得分率" :value="trend.avg_homework" suffix="%" /></a-col>
              <a-col :span="12"><a-statistic title="考试平均得分率" :value="trend.avg_exam" suffix="%" /></a-col>
            </a-row>
            <div v-if="trend.trend?.length">
              <div style="display: flex; align-items: end; height: 200px; gap: 8px; padding: 0 20px; border-bottom: 1px solid #e8e8e8">
                <div v-for="(item, i) in trend.trend" :key="i" style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: end; height: 100%">
                  <div :style="{
                    width: '100%',
                    maxWidth: '40px',
                    height: (item.percentage) + '%',
                    background: item.type === 'exam' ? '#ff7a45' : '#1890ff',
                    borderRadius: '4px 4px 0 0',
                    minHeight: '2px'
                  }" :title="`${item.title}: ${item.percentage}%`"></div>
                  <div style="font-size: 10px; color: #999; margin-top: 4px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 60px">{{ item.title }}</div>
                </div>
              </div>
              <div style="margin-top: 8px; display: flex; gap: 16px; justify-content: center; font-size: 12px; color: #666">
                <span><span style="display: inline-block; width: 12px; height: 12px; background: #1890ff; border-radius: 2px; margin-right: 4px"></span>作业</span>
                <span><span style="display: inline-block; width: 12px; height: 12px; background: #ff7a45; border-radius: 2px; margin-right: 4px"></span>考试</span>
              </div>
            </div>
            <a-empty v-else description="暂无趋势数据" />
          </div>
        </a-card>

        <!-- 知识归因雷达图 -->
        <a-card title="知识雷达" size="small" style="margin-top: 16px">
          <KnowledgeRadarChart v-if="radarData" :radar-data="radarData" />
          <a-empty v-else description="暂无归因数据" />
        </a-card>

        <!-- 薄弱知识点 -->
        <a-card title="薄弱知识点" size="small" style="margin-top: 16px" v-if="weakPoints.length">
          <WeakPointList :weak-points="weakPoints" />
        </a-card>
      </template>
      <a-empty v-else-if="!loading" description="暂无成绩数据" />
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '../api'
import { getRadarData } from '@/api/attribution'
import KnowledgeRadarChart from '@/components/knowledge-radar/KnowledgeRadarChart.vue'
import WeakPointList from '@/components/knowledge-radar/WeakPointList.vue'

const report = ref(null)
const loading = ref(false)
const myPersonId = ref(null)
const trend = ref(null)
const trendLoading = ref(false)
const radarData = ref(null)
const weakPoints = ref([])

const myGrade = computed(() => {
  if (!report.value?.students || !myPersonId.value) return null
  return report.value.students.find(s => s.person_id === myPersonId.value)
})

const rankColumns = [
  { key: 'name', title: '学生', dataIndex: 'name' },
  { key: 'homework_avg', title: '作业', dataIndex: 'homework_avg' },
  { key: 'exam_avg', title: '考试', dataIndex: 'exam_avg' },
  { key: 'attendance_rate', title: '出勤率' },
  { key: 'total_grade', title: '总评' },
]

async function fetchData() {
  loading.value = true
  try {
    // 获取当前用户信息
    const userStr = localStorage.getItem('user')
    if (userStr) {
      const user = JSON.parse(userStr)
      myPersonId.value = user.id
    }

    // 获取学生所在课堂
    const classRes = await api.get('/classrooms')
    const myClass = classRes.data.find(c => c.students?.some(s => s.person_id === myPersonId.value))
    if (!myClass) { loading.value = false; return }

    const res = await api.get(`/grades/report/${myClass.id}`, { _skipGlobalError: true })
    report.value = res.data

    // 获取知识归因雷达数据
    try {
      const radarRes = await getRadarData(myPersonId.value)
      if (radarRes.data) {
        radarData.value = radarRes.data.radar || null
        weakPoints.value = radarRes.data.weak_points || []
      }
    } catch { /* 归因数据获取失败不影响主流程 */ }
  } catch { /* ignore */ } finally { loading.value = false }
}

onMounted(fetchData)

async function fetchTrend() {
  trendLoading.value = true
  try {
    const res = await api.get(`/grades/trend/${myPersonId.value}`, { _skipGlobalError: true })
    trend.value = res.data
  } catch (e) {
    message.error('获取趋势失败')
  } finally {
    trendLoading.value = false
  }
}
</script>
