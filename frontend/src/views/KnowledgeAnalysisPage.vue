<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      :title="pageTitle"
      sub-title="能力雷达·薄弱归因·订正进度·知识图谱"
      style="padding: 0 0 16px 0"
    />

    <!-- 学生选择 -->
    <a-card :bordered="false" class="settings-card" style="margin-bottom: 16px">
      <a-row :gutter="16" align="middle">
        <!-- 学生身份：自动加载自己的 student_id -->
        <a-col :xs="24" :md="6">
          <div v-if="isStudent && myStudents.length > 0" class="student-tag-area">
            <a-tag color="green" style="font-size: 14px; padding: 4px 12px">
              学生 #{{ selectedStudentId }}
            </a-tag>
            <a-select
              v-if="myStudents.length > 1"
              v-model:value="selectedStudentId"
              size="small"
              style="width: 160px; margin-left: 8px"
              @change="onStudentChange"
            >
              <a-select-option v-for="s in myStudents" :key="s.student_id" :value="s.student_id">
                {{ s.classroom_name }}
              </a-select-option>
            </a-select>
            <span v-else style="margin-left: 8px; color: #666">
              {{ myStudents[0]?.classroom_name }}
            </span>
          </div>
          <a-form-item v-else-if="!isStudent" label="学生ID" :colon="false" style="margin-bottom: 0">
            <a-input-number
              v-model:value="selectedStudentId"
              :min="1"
              style="width: 100%"
              placeholder="输入学生ID"
            />
          </a-form-item>
          <a-empty v-else description="未关联学生身份" :image="simpleImage" />
        </a-col>

        <!-- 教师身份：课堂筛选 + 学生列表 -->
        <a-col v-if="!isStudent" :xs="24" :md="5">
          <a-form-item label="课堂ID（可选）" :colon="false" style="margin-bottom: 0">
            <a-input-number
              v-model:value="classroomFilter"
              :min="1"
              style="width: 100%"
              placeholder="输入后回车加载"
              @pressEnter="loadClassroomStudents"
            />
          </a-form-item>
        </a-col>

        <a-col v-if="!isStudent && classroomStudents.length > 0" :xs="24" :md="6">
          <a-form-item label="选择学生" :colon="false" style="margin-bottom: 0">
            <a-select
              v-model:value="selectedStudentId"
              placeholder="选择学生"
              show-search
              optionFilterProp="label"
              @change="onStudentChange"
            >
              <a-select-option
                v-for="s in classroomStudents"
                :key="s.student_id"
                :value="s.student_id"
                :label="s.name + ' #' + s.student_id"
              >
                {{ s.name }} (#{{ s.student_id }})
              </a-select-option>
            </a-select>
          </a-form-item>
        </a-col>

        <a-col :xs="24" :md="isStudent ? 6 : 7" style="text-align: right">
          <a-space>
            <a-button
              v-if="!isStudent && classroomFilter"
              size="small"
              @click="loadClassroomStudents"
            >
              加载学生列表
            </a-button>
            <a-button
              type="primary"
              :loading="loading"
              :disabled="!selectedStudentId"
              @click="loadAnalysis"
            >
              <template #icon><ReloadOutlined /></template>
              开始分析
            </a-button>
          </a-space>
        </a-col>
      </a-row>
    </a-card>

    <!-- 分析类型 Tab -->
    <a-tabs v-model:activeKey="analysisType" @change="onTabChange" style="margin-bottom: 16px">
      <a-tab-pane key="math" tab="📐 数学" />
      <a-tab-pane key="writing" tab="✍️ 写作" />
    </a-tabs>

    <!-- 空状态 -->
    <a-card v-if="!analysisData && !loading" :bordered="false" class="result-empty">
      <a-empty description="选择学生后点击「开始分析」生成归因报告" />
    </a-card>

    <!-- 加载中 -->
    <a-card v-if="loading" :bordered="false">
      <a-skeleton active :paragraph="{ rows: 8 }" />
    </a-card>

    <!-- 主体：2x2 网格 -->
    <div v-if="analysisData && !loading" class="analysis-grid">
      <!-- 左上：能力雷达图 -->
      <a-card title="能力雷达图" :bordered="false" class="module-card">
        <template #extra>
          <a-tooltip title="数值为各维度掌握度（0-100，越高越好）">
            <InfoCircleOutlined style="color: #999" />
          </a-tooltip>
        </template>
        <div v-if="radarIndicators.length > 0" class="radar-wrap">
          <KnowledgeRadarChart :radar-data="radarChartData" />
          <div class="radar-legend">
            <a-tag v-for="(ind, i) in radarIndicators" :key="ind.name" color="blue">
              {{ ind.name }}: {{ radarValues[i] }}
            </a-tag>
          </div>
        </div>
        <a-empty v-else description="暂无雷达数据（学生可能还没有批改记录）" />
      </a-card>

      <!-- 右上：薄弱知识点 -->
      <a-card title="薄弱知识点" :bordered="false" class="module-card">
        <template #extra>
          <a-tag color="orange">{{ weakPoints.length }} 个</a-tag>
        </template>
        <a-list
          v-if="weakPoints.length > 0"
          :data-source="weakPoints"
          :pagination="{ pageSize: 5, size: 'small' }"
          item-layout="vertical"
        >
          <template #renderItem="{ item }">
            <a-list-item>
              <a-list-item-meta>
                <template #title>
                  <span style="font-weight: 600">{{ item.knowledge_name }}</span>
                  <a-tag color="red" style="margin-left: 8px">
                    薄弱度 {{ Math.round((item.weakness_score || 0) * 100) }}%
                  </a-tag>
                  <a-tag v-if="item.error_count" color="volcano">
                    {{ item.error_count }} 次错误
                  </a-tag>
                </template>
                <template #description>
                  <div v-if="item.error_cause_distribution && Object.keys(item.error_cause_distribution).length > 0" class="cause-dist">
                    <span class="cause-label">错因分布：</span>
                    <a-tag v-for="(count, cause) in item.error_cause_distribution" :key="cause" color="orange">
                      {{ cause }} ×{{ count }}
                    </a-tag>
                  </div>
                  <div v-if="item.root_cause" class="root-cause">
                    <span class="cause-label">根因路径：</span>
                    <span>{{ formatRootCause(item.root_cause) }}</span>
                  </div>
                  <div v-if="item.suggestion" class="suggestion">
                    <BulbOutlined style="color: #faad14; margin-right: 4px" />
                    <span>{{ item.suggestion }}</span>
                  </div>
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>
        <a-empty v-else description="暂无薄弱知识点（继续保持！）" />
      </a-card>

      <!-- 左下：订正状态面板 -->
      <a-card title="订正状态" :bordered="false" class="module-card">
        <template #extra>
          <a-tag :color="correctionRate >= 0.7 ? 'green' : correctionRate >= 0.4 ? 'orange' : 'red'">
            订正率 {{ Math.round(correctionRate * 100) }}%
          </a-tag>
        </template>
        <a-row :gutter="16" style="margin-bottom: 16px">
          <a-col :span="6">
            <a-statistic title="总错题" :value="correctionStatus.total_errors || 0">
              <template #prefix><FileTextOutlined /></template>
            </a-statistic>
          </a-col>
          <a-col :span="6">
            <a-statistic
              title="已订正"
              :value="correctionStatus.corrected || 0"
              :value-style="{ color: '#16a34a' }"
            >
              <template #prefix><CheckCircleOutlined /></template>
            </a-statistic>
          </a-col>
          <a-col :span="6">
            <a-statistic
              title="待订正"
              :value="correctionStatus.uncorrected || 0"
              :value-style="{ color: '#ef4444' }"
            >
              <template #prefix><ExclamationCircleOutlined /></template>
            </a-statistic>
          </a-col>
          <a-col :span="6">
            <a-statistic
              title="订正率"
              :value="Math.round(correctionRate * 100)"
              suffix="%"
              :value-style="{ color: correctionRate >= 0.7 ? '#16a34a' : '#faad14' }"
            >
              <template #prefix><TrophyOutlined /></template>
            </a-statistic>
          </a-col>
        </a-row>
        <a-progress
          :percent="Math.round(correctionRate * 100)"
          :stroke-color="correctionRate >= 0.7 ? '#16a34a' : '#faad14'"
          status="active"
        />
        <a-alert
          v-if="(correctionStatus.uncorrected || 0) > 0"
          style="margin-top: 12px"
          type="warning"
          show-icon
          :message="`还有 ${correctionStatus.uncorrected} 题待订正，前往「订正闭环」页面完成订正`"
        />
        <a-alert
          v-else-if="(correctionStatus.total_errors || 0) > 0"
          style="margin-top: 12px"
          type="success"
          show-icon
          message="所有错题已订正完成，继续保持！"
        />
      </a-card>

      <!-- 右下：知识图谱可视化 -->
      <a-card title="知识图谱" :bordered="false" class="module-card">
        <template #extra>
          <a-radio-group v-model:value="graphLayout" size="small" @change="renderGraph">
            <a-radio-button value="force">力导图</a-radio-button>
            <a-radio-button value="tree">层级树</a-radio-button>
          </a-radio-group>
        </template>
        <div ref="graphChartRef" class="graph-chart" />
        <div v-if="graphData.nodes.length > 0" class="graph-legend">
          <a-tag v-for="(color, level) in levelColors" :key="level" :color="color">
            L{{ level }}
          </a-tag>
          <span style="margin-left: 8px; color: #999; font-size: 12px">
            实线=父子层级，虚线=前置依赖
          </span>
        </div>
      </a-card>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, nextTick, watch } from 'vue'
import { message } from 'ant-design-vue'
import { Empty } from 'ant-design-vue'
import * as echarts from 'echarts'
import {
  ReloadOutlined,
  InfoCircleOutlined,
  BulbOutlined,
  CheckCircleOutlined,
  ExclamationCircleOutlined,
  FileTextOutlined,
  TrophyOutlined,
} from '@ant-design/icons-vue'
import { useUserStore } from '@/stores/user'
import KnowledgeRadarChart from '@/components/knowledge-radar/KnowledgeRadarChart.vue'
import {
  analyzeKnowledge,
  getMyStudentInfo,
  listStudentsForAnalysis,
  getKnowledgeGraph,
} from '@/api/attribution'

const userStore = useUserStore()
const simpleImage = Empty.PRESENTED_IMAGE_SIMPLE

const isStudent = computed(() => userStore.role === 'student')
const pageTitle = computed(() => (isStudent.value ? '我的知识画像' : '知识归因分析'))

// ===== 学生选择 =====
const selectedStudentId = ref(null)
const myStudents = ref([])
const classroomFilter = ref(null)
const classroomStudents = ref([])

// ===== 分析状态 =====
const loading = ref(false)
const analysisType = ref('math')
const analysisData = ref(null)

// ===== 知识图谱 =====
const graphChartRef = ref(null)
let graphChartInstance = null
let graphResizeObserver = null
const graphData = ref({ nodes: [], edges: [] })
const graphLayout = ref('force')
const levelColors = ['#3751FE', '#16a34a', '#faad14', '#ef4444', '#a855f7']

// ===== 雷达图数据转换 =====
// 后端返回 {dim_name: float(0-1)}，前端组件需要 {indicators, values}
const radarIndicators = computed(() => {
  const radar = analysisData.value?.radar || {}
  return Object.keys(radar).map((name) => ({ name, max: 100 }))
})
const radarValues = computed(() => {
  const radar = analysisData.value?.radar || {}
  return Object.values(radar).map((v) => Math.round((v || 0) * 100))
})
const radarChartData = computed(() => ({
  indicators: radarIndicators.value,
  values: radarValues.value,
}))

// ===== 薄弱点列表 =====
const weakPoints = computed(() => analysisData.value?.weak_points || [])

// ===== 订正状态 =====
const correctionStatus = computed(() => analysisData.value?.correction_status || {})
const correctionRate = computed(() => correctionStatus.value?.correction_rate || 0)

// ===== 工具函数 =====
function formatRootCause(rootCause) {
  if (!rootCause || typeof rootCause !== 'object') return ''
  const root = rootCause.root_node_name || rootCause.root_node || ''
  const path = Array.isArray(rootCause.path) ? rootCause.path.join(' → ') : ''
  const ratio = rootCause.contribution_ratio
  const ratioStr = ratio ? ` (贡献度 ${Math.round(ratio * 100)}%)` : ''
  if (path) return `${path}${ratioStr}`
  return root ? `根因：${root}${ratioStr}` : ''
}

// ===== 学生选择处理 =====
async function loadMyStudentInfo() {
  if (!isStudent.value) return
  try {
    const res = await getMyStudentInfo()
    myStudents.value = res.data?.students || []
    if (myStudents.value.length > 0) {
      selectedStudentId.value = myStudents.value[0].student_id
      // 学生身份自动加载首次分析
      await loadAnalysis()
    }
  } catch (e) {
    console.warn('[KnowledgeAnalysis] 加载学生身份失败:', e)
  }
}

async function loadClassroomStudents() {
  if (!classroomFilter.value) {
    message.warning('请先输入课堂ID')
    return
  }
  try {
    const res = await listStudentsForAnalysis(classroomFilter.value)
    classroomStudents.value = res.data?.students || []
    if (classroomStudents.value.length === 0) {
      message.info('该课堂暂无学生记录')
    } else {
      message.success(`已加载 ${classroomStudents.value.length} 名学生`)
    }
  } catch (e) {
    message.error('加载学生列表失败')
    console.error(e)
  }
}

function onStudentChange() {
  // 切换学生后清空当前分析，等待用户点开始分析
  analysisData.value = null
}

// ===== Tab 切换 =====
function onTabChange() {
  if (selectedStudentId.value) {
    loadAnalysis()
  }
}

// ===== 加载分析 =====
async function loadAnalysis() {
  if (!selectedStudentId.value) {
    message.warning('请先选择学生')
    return
  }
  // 销毁旧的知识图谱实例，避免切换 Tab 时引用已失效的 DOM 导致 echarts 内部错误
  if (graphChartInstance) {
    try { graphChartInstance.dispose() } catch (e) { /* ignore */ }
    graphChartInstance = null
  }
  loading.value = true
  analysisData.value = null
  try {
    const res = await analyzeKnowledge({
      student_id: selectedStudentId.value,
      analysis_type: analysisType.value,
    })
    analysisData.value = res.data
    if (
      !res.data.radar ||
      Object.keys(res.data.radar).length === 0
    ) {
      message.info('该学生暂无批改数据，无法生成雷达图')
    }
    // 加载知识图谱
    await loadGraph()
  } catch (e) {
    message.error('归因分析失败：' + (e.response?.data?.detail || e.message))
    console.error(e)
  } finally {
    loading.value = false
  }
}

// ===== 知识图谱加载与渲染 =====
async function loadGraph() {
  try {
    const res = await getKnowledgeGraph(analysisType.value)
    const graph = res.data?.graph || {}
    graphData.value = {
      nodes: graph.nodes || [],
      edges: graph.edges || [],
    }
    await nextTick()
    renderGraph()
  } catch (e) {
    console.warn('[KnowledgeAnalysis] 加载知识图谱失败:', e)
  }
}

function renderGraph() {
  if (!graphChartRef.value) return
  try {
    if (!graphChartInstance) {
      graphChartInstance = echarts.init(graphChartRef.value)
      graphResizeObserver = new ResizeObserver(() => graphChartInstance?.resize())
      graphResizeObserver.observe(graphChartRef.value)
    }

    const { nodes, edges } = graphData.value
    if (!nodes || nodes.length === 0) {
      graphChartInstance.clear()
      graphChartInstance.setOption({
        title: { text: '暂无图谱数据', left: 'center', top: 'center', textStyle: { color: '#999', fontSize: 14 } },
      })
      return
    }

    // 节点分类（按 level）
    const categories = []
    for (let i = 0; i < 5; i++) {
      categories.push({ name: `L${i}` })
    }

    const seriesNodes = nodes.map((n) => ({
      id: n.id,
      name: n.name,
      category: n.category ?? n.level ?? 0,
      symbolSize: n.symbolSize || 30,
      value: n.level,
      label: { show: (n.level || 0) <= 1 },
    }))

    const seriesLinks = edges.map((e) => ({
      source: e.source,
      target: e.target,
      lineStyle: e.type === 'prerequisite'
        ? { type: 'dashed', color: '#faad14', width: 1, curveness: 0.2 }
        : { color: '#bfbfbf', width: 1, curveness: 0.1 },
      value: e.type,
    }))

    const isForce = graphLayout.value === 'force'

    graphChartInstance.clear()
    graphChartInstance.setOption({
      tooltip: {
        formatter: (p) => {
          if (p.dataType === 'node') return `${p.data.name} (L${p.data.value})`
          if (p.dataType === 'edge') return `${p.data.source} → ${p.data.target} (${p.data.value})`
          return p.name
        },
      },
      legend: {
        data: categories.map((c) => c.name),
        top: 8,
        textStyle: { fontSize: 11 },
      },
      series: [
        {
          type: 'graph',
          layout: isForce ? 'force' : 'none',
          roam: true,
          draggable: true,
          categories,
          data: seriesNodes,
          links: seriesLinks,
          force: {
            repulsion: 200,
            edgeLength: [60, 160],
            gravity: 0.05,
          },
          label: {
            show: true,
            position: 'right',
            fontSize: 11,
            color: '#333',
          },
          lineStyle: { color: 'source', curveness: 0.1 },
          emphasis: {
            focus: 'adjacency',
            lineStyle: { width: 3 },
            label: { show: true, fontWeight: 'bold' },
          },
          progressiveThreshold: 700,
        },
      ],
    })
  } catch (e) {
    console.warn('[KnowledgeAnalysis] 知识图谱渲染异常:', e)
    // 渲染失败时尝试清理实例，下次重新初始化
    if (graphChartInstance) {
      try { graphChartInstance.dispose() } catch (_) { /* ignore */ }
      graphChartInstance = null
    }
  }
}

watch(graphLayout, () => renderGraph())

// ===== 生命周期 =====
onMounted(async () => {
  await loadMyStudentInfo()
})

onBeforeUnmount(() => {
  if (graphResizeObserver) graphResizeObserver.disconnect()
  if (graphChartInstance) {
    graphChartInstance.dispose()
    graphChartInstance = null
  }
})
</script>

<style scoped>
.analysis-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.module-card {
  margin-bottom: 0;
  min-height: 420px;
}

.student-tag-area {
  display: flex;
  align-items: center;
  height: 32px;
}

.radar-wrap {
  text-align: center;
}

.radar-legend {
  margin-top: 8px;
  text-align: left;
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.graph-chart {
  width: 100%;
  height: 380px;
}

.graph-legend {
  margin-top: 8px;
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  align-items: center;
}

.cause-dist,
.root-cause,
.suggestion {
  margin-top: 4px;
  font-size: 13px;
  line-height: 1.6;
}

.cause-label {
  color: #666;
  margin-right: 4px;
}

.suggestion {
  color: #555;
  background: rgba(250, 173, 20, 0.06);
  padding: 6px 8px;
  border-radius: 4px;
  margin-top: 6px;
}

.result-empty {
  text-align: center;
  padding: 60px 0;
}

@media (max-width: 992px) {
  .analysis-grid {
    grid-template-columns: 1fr;
  }
}
</style>
