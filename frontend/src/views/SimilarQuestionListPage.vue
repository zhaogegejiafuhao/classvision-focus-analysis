<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="我的相似题"
      sub-title="变式练习·掌握追踪·进步可见"
      style="padding: 0 0 16px 0"
    />

    <!-- 状态筛选 -->
    <a-card :bordered="false" class="settings-card" style="margin-bottom: 16px">
      <a-radio-group v-model:value="filterStatus" button-style="solid" @change="loadData">
        <a-radio-button value="">全部</a-radio-button>
        <a-radio-button value="pending">待练习</a-radio-button>
        <a-radio-button value="passed">已掌握</a-radio-button>
        <a-radio-button value="failed">未通过</a-radio-button>
      </a-radio-group>
    </a-card>

    <!-- 列表 -->
    <a-card :bordered="false" class="settings-card">
      <a-table
        :columns="columns"
        :data-source="items"
        :loading="loading"
        :pagination="pagination"
        row-key="similar_id"
        @change="handleTableChange"
      >
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'question_text'">
            <span class="question-text">{{ record.question_text.slice(0, 80) }}{{ record.question_text.length > 80 ? '...' : '' }}</span>
          </template>
          <template v-else-if="column.key === 'variant_type'">
            <a-tag :color="variantColor(record.variant_type)">{{ record.variant_type }}</a-tag>
          </template>
          <template v-else-if="column.key === 'difficulty'">
            <a-tag>{{ record.difficulty }}</a-tag>
          </template>
          <template v-else-if="column.key === 'mastery_status'">
            <a-tag :color="statusColor(record.mastery_status)">{{ statusLabel(record.mastery_status) }}</a-tag>
          </template>
          <template v-else-if="column.key === 'created_at'">
            {{ formatDate(record.created_at) }}
          </template>
          <template v-else-if="column.key === 'action'">
            <a-button type="link" size="small" @click="viewDetail(record.similar_id)">
              查看
            </a-button>
          </template>
        </template>
      </a-table>

      <a-empty v-if="!loading && items.length === 0" description="暂无相似题，可从错题本一键生成" />
    </a-card>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { listSimilarQuestions } from '@/api/similarQuestions'

const router = useRouter()
const loading = ref(false)
const items = ref([])
const filterStatus = ref('')

const pagination = reactive({
  current: 1,
  pageSize: 20,
  total: 0,
  showSizeChanger: true,
  showTotal: (total) => `共 ${total} 道相似题`,
})

const columns = [
  { title: '题目', dataIndex: 'question_text', key: 'question_text', ellipsis: true },
  { title: '变式类型', key: 'variant_type', width: 120 },
  { title: '难度', key: 'difficulty', width: 80 },
  { title: '掌握状态', key: 'mastery_status', width: 100 },
  { title: '生成时间', key: 'created_at', width: 160 },
  { title: '操作', key: 'action', width: 80, fixed: 'right' },
]

async function loadData() {
  loading.value = true
  try {
    const res = await listSimilarQuestions({
      status: filterStatus.value || undefined,
      page: pagination.current,
      pageSize: pagination.pageSize,
    })
    items.value = res.data.items || []
    pagination.total = res.data.total || 0
  } catch (e) {
    message.error('加载相似题列表失败')
  } finally {
    loading.value = false
  }
}

function handleTableChange(pag) {
  pagination.current = pag.current
  pagination.pageSize = pag.pageSize
  loadData()
}

function viewDetail(similarId) {
  // 阶段3将跳转到练习页面
  router.push(`/my-similar-questions/${similarId}`)
}

function variantColor(type) {
  const map = { '根源变式': 'purple', '同类变式': 'blue', '基础铺垫': 'green', '简化原题': 'cyan', '进阶题': 'orange' }
  return map[type] || 'default'
}

function statusColor(status) {
  const map = { pending: 'default', passed: 'success', failed: 'error' }
  return map[status] || 'default'
}

function statusLabel(status) {
  const map = { pending: '待练习', passed: '已掌握', failed: '未通过' }
  return map[status] || status
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
.settings-card { border-radius: 12px; }
.question-text { line-height: 1.6; }
</style>
