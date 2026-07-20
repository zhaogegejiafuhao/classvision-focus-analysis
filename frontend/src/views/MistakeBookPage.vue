<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="错题本"
      sub-title="错题归集·知识定位·订正追踪"
      style="padding: 0 0 16px 0"
    />

    <!-- 筛选栏 -->
    <a-card :bordered="false" class="settings-card" style="margin-bottom: 16px">
      <a-row :gutter="16" align="middle">
        <a-col :xs="24" :sm="8" :md="6">
          <a-input
            v-model:value="filterKp"
            placeholder="知识点关键词"
            allow-clear
            @press-enter="loadData"
          />
        </a-col>
        <a-col>
          <a-button type="primary" @click="loadData">
            <template #icon><SearchOutlined /></template>
            查询
          </a-button>
          <a-button style="margin-left: 8px" @click="resetFilter">重置</a-button>
        </a-col>
      </a-row>
    </a-card>

    <!-- 错题列表 -->
    <a-card :bordered="false" class="settings-card">
      <a-table
        :columns="columns"
        :data-source="items"
        :loading="loading"
        :pagination="pagination"
        row-key="grading_id"
        @change="handleTableChange"
      >
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'score'">
            <span :class="scoreClass(record.score, record.max_score)">
              {{ record.score }}/{{ record.max_score }}
            </span>
          </template>
          <template v-else-if="column.key === 'error_type'">
            <a-tag v-if="record.error_type" :color="errorTagColor(record.error_type)">
              {{ record.error_type }}
            </a-tag>
            <span v-else class="text-muted">-</span>
          </template>
          <template v-else-if="column.key === 'knowledge_points'">
            <a-tag v-for="kp in (record.knowledge_points || []).slice(0, 3)" :key="kp" color="blue">
              {{ kp }}
            </a-tag>
            <span v-if="(record.knowledge_points || []).length > 3" class="text-muted">
              +{{ record.knowledge_points.length - 3 }}
            </span>
          </template>
          <template v-else-if="column.key === 'homework_title'">
            {{ record.homework_title || '-' }}
          </template>
          <template v-else-if="column.key === 'created_at'">
            {{ formatDate(record.created_at) }}
          </template>
          <template v-else-if="column.key === 'action'">
            <a-button type="link" size="small" @click="goDetail(record.grading_id)">
              查看详情
            </a-button>
          </template>
        </template>
      </a-table>

      <a-empty v-if="!loading && items.length === 0" description="暂无错题记录" />
    </a-card>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { SearchOutlined } from '@ant-design/icons-vue'
import { listMistakes } from '@/api/correction'

const router = useRouter()

const loading = ref(false)
const items = ref([])
const filterKp = ref('')

const pagination = reactive({
  current: 1,
  pageSize: 20,
  total: 0,
  showSizeChanger: true,
  showTotal: (total) => `共 ${total} 条错题`,
})

const columns = [
  { title: '题目来源', dataIndex: 'homework_title', key: 'homework_title', ellipsis: true },
  { title: '得分', key: 'score', width: 100 },
  { title: '错因', key: 'error_type', width: 120 },
  { title: '知识点', key: 'knowledge_points', width: 240 },
  { title: '时间', key: 'created_at', width: 160 },
  { title: '操作', key: 'action', width: 100, fixed: 'right' },
]

async function loadData() {
  loading.value = true
  try {
    const res = await listMistakes({
      kp: filterKp.value || undefined,
      page: pagination.current,
      pageSize: pagination.pageSize,
    })
    items.value = res.data.items || []
    pagination.total = res.data.total || 0
  } catch (e) {
    message.error('加载错题列表失败')
  } finally {
    loading.value = false
  }
}

function resetFilter() {
  filterKp.value = ''
  pagination.current = 1
  loadData()
}

function handleTableChange(pag) {
  pagination.current = pag.current
  pagination.pageSize = pag.pageSize
  loadData()
}

function goDetail(gradingId) {
  router.push(`/mistake-book/${gradingId}`)
}

function scoreClass(score, maxScore) {
  if (maxScore <= 0) return 'text-muted'
  const ratio = score / maxScore
  if (ratio >= 0.8) return 'score-good'
  if (ratio >= 0.5) return 'score-mid'
  return 'score-bad'
}

function errorTagColor(errorType) {
  const map = {
    '计算粗心': 'orange',
    '概念混淆': 'red',
    '审题不清': 'purple',
    '辅助线缺失': 'cyan',
    '逻辑跳步': 'geekblue',
    '知识缺失': 'volcano',
  }
  return map[errorType] || 'default'
}

function formatDate(dt) {
  if (!dt) return '-'
  try {
    const d = new Date(dt)
    return d.toLocaleDateString('zh-CN', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' })
  } catch {
    return dt
  }
}

onMounted(() => {
  loadData()
})
</script>

<style scoped>
.settings-card {
  border-radius: 12px;
}
.score-good { color: #52c41a; font-weight: 600; }
.score-mid { color: #faad14; font-weight: 600; }
.score-bad { color: #ff4d4f; font-weight: 600; }
.text-muted { color: #999; }
</style>
