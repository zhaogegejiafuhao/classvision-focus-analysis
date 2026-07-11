<template>
  <div class="cv-page" style="max-width: 1200px">
    <a-page-header title="我的注意力报告" sub-title="查看你在各课堂的注意力表现" style="padding: 0 0 16px 0" />

    <a-spin :spinning="loading">
      <a-skeleton v-if="loading && !data" active :paragraph="{ rows: 4 }" />
      <template v-else-if="data">
        <a-row :gutter="16" style="margin-bottom: 24px">
          <a-col :xs="12" :sm="6">
            <a-card>
              <a-statistic title="参与课堂" :value="data.total_classrooms" />
            </a-card>
          </a-col>
          <a-col :xs="12" :sm="6">
            <a-card>
              <a-statistic
                title="平均注意力"
                :value="data.overall_avg_attention"
                suffix="%"
                :value-style="{ color: data.overall_avg_attention >= 60 ? '#3f8600' : '#cf1322' }"
              />
            </a-card>
          </a-col>
          <a-col :xs="12" :sm="6">
            <a-card>
              <a-statistic title="最佳课堂" :value="data.best_classroom || '-'" :value-style="{ fontSize: '16px', color: '#3f8600' }" />
            </a-card>
          </a-col>
          <a-col :xs="12" :sm="6">
            <a-card>
              <a-statistic title="需改进课堂" :value="data.worst_classroom || '-'" :value-style="{ fontSize: '16px', color: '#cf1322' }" />
            </a-card>
          </a-col>
        </a-row>

        <a-empty v-if="data.classrooms.length === 0" description="暂无课堂数据，请等待教师添加你到课堂" style="margin: 60px 0" />

        <a-list v-else item-layout="vertical" :data-source="data.classrooms" :split="true">
          <template #renderItem="{ item: c }">
            <a-list-item>
              <a-card hoverable size="small" @click="toggleExpand(c.classroom_id)" style="cursor: pointer">
                <div class="card-header-row">
                  <div class="card-header-left">
                    <a-badge :status="c.started_at ? 'processing' : 'default'" />
                    <div>
                      <span class="card-title">{{ c.classroom_name }}</span>
                      <span class="card-meta">{{ c.teacher }} · {{ c.duration }}分钟</span>
                    </div>
                  </div>
                  <div class="card-header-right">
                    <a-tag :color="attentionColor(c.avg_attention)">
                      {{ Math.round(c.avg_attention) }}% · {{ attentionLabel(c.avg_attention) }}
                    </a-tag>
                    <a-button type="text" size="small">
                      <template #icon>
                        <DownOutlined :class="{ 'expand-rotated': expandedId === c.classroom_id }" />
                      </template>
                    </a-button>
                  </div>
                </div>
              </a-card>

              <div v-if="expandedId === c.classroom_id" class="card-detail-area">
                <a-row :gutter="16" style="margin-bottom: 16px">
                  <a-col :span="8">
                    <a-statistic title="平均注意力" :value="c.avg_attention" suffix="%" />
                  </a-col>
                  <a-col :span="8">
                    <a-statistic title="低头次数" :value="c.head_down_count" :value-style="{ color: '#cf1322' }" />
                  </a-col>
                  <a-col :span="8">
                    <a-statistic title="眨眼次数" :value="c.blink_count" :value-style="{ color: '#722ed1' }" />
                  </a-col>
                </a-row>

                <a-card v-if="c.timeline.length > 0" title="注意力趋势" size="small">
                  <div :ref="el => setChartEl(c.classroom_id, el)" style="width: 100%; height: 250px" />
                </a-card>
                <a-empty v-else description="暂无时间线数据" />
              </div>
            </a-list-item>
          </template>
        </a-list>
      </template>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick, onBeforeUnmount } from 'vue'
import api from '@/api'
import { message } from 'ant-design-vue'
import { DownOutlined } from '@ant-design/icons-vue'
import * as echarts from 'echarts'

const loading = ref(true)
const data = ref(null)
const expandedId = ref(null)
const chartEls = {}
const chartInstances = {}

function setChartEl(classroomId, el) {
  if (el) chartEls[classroomId] = el
}

function attentionColor(val) {
  if (val >= 75) return 'success'
  if (val >= 50) return 'warning'
  return 'error'
}

function attentionLabel(val) {
  if (val >= 75) return '良好'
  if (val >= 50) return '一般'
  return '偏低'
}

async function toggleExpand(classroomId) {
  if (expandedId.value === classroomId) {
    expandedId.value = null
    if (chartInstances[classroomId]) {
      chartInstances[classroomId].dispose()
      delete chartInstances[classroomId]
    }
    return
  }
  // 清理旧图表
  if (expandedId.value && chartInstances[expandedId.value]) {
    chartInstances[expandedId.value].dispose()
    delete chartInstances[expandedId.value]
  }
  expandedId.value = classroomId
  await nextTick()
  renderChart(classroomId)
}

function renderChart(classroomId) {
  const c = data.value?.classrooms.find(x => x.classroom_id === classroomId)
  if (!c || c.timeline.length === 0) return
  const el = chartEls[classroomId]
  if (!el) return
  if (chartInstances[classroomId]) {
    chartInstances[classroomId].dispose()
  }
  const chart = echarts.init(el)
  chartInstances[classroomId] = chart
  chart.setOption({
    grid: { top: 20, bottom: 30, left: 50, right: 20 },
    xAxis: { type: 'category', data: c.timeline.map(t => t.timestamp) },
    yAxis: { type: 'value', max: 100, min: 0, name: '注意力' },
    series: [{
      type: 'line',
      data: c.timeline.map(t => t.avg_attention),
      smooth: true,
      areaStyle: { opacity: 0.2 },
      itemStyle: { color: '#1890ff' },
    }],
  })
}

async function loadData() {
  loading.value = true
  try {
    const res = await api.get('/me/attention-history')
    data.value = res.data
  } catch (e) {
    message.error(e.response?.data?.detail || '加载个人报告失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => { loadData() })

onBeforeUnmount(() => {
  Object.values(chartInstances).forEach(c => c.dispose())
})
</script>

<style scoped>
.card-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.card-title {
  font-size: 15px;
  font-weight: 600;
  color: #1a1a2e;
  display: block;
}

.card-meta {
  font-size: 12px;
  color: #8c8c8c;
}

.card-header-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

.expand-rotated {
  transform: rotate(180deg);
  transition: transform 0.2s;
}

.card-detail-area {
  padding: 16px 0 8px 0;
}
</style>
