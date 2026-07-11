<template>
  <div class="oj-subs-page">
    <div class="subs-header">
      <a-typography-title :level="3" style="margin: 0">提交记录</a-typography-title>
      <a-button type="text" @click="$router.push('/oj')">
        <template #icon><ArrowLeftOutlined /></template>
        返回题目列表
      </a-button>
    </div>

    <a-card style="margin-top: 16px">
      <a-skeleton v-if="loading && submissions.length === 0" active :paragraph="{ rows: 6 }" />
      <a-table
        v-else
        :columns="columns"
        :data-source="submissions"
        :loading="loading"
        row-key="id"
        :pagination="{ pageSize: 20, hideOnSinglePage: true }"
      >
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'problem_title'">
            <a href="javascript:void(0)" @click.prevent="$router.push(`/oj/${record.problem_id}`)">{{ record.problem_title }}</a>
          </template>
          <template v-if="column.key === 'status'">
            <a-tag :color="statusColor(record.status)">{{ record.status }}</a-tag>
          </template>
          <template v-if="column.key === 'language'">
            {{ langLabel(record.language) }}
          </template>
          <template v-if="column.key === 'cpu_time'">
            <span v-if="record.cpu_time > 0">{{ record.cpu_time }}ms</span>
            <span v-else style="color: #999">-</span>
          </template>
          <template v-if="column.key === 'memory'">
            <span v-if="record.memory > 0">{{ formatMemory(record.memory) }}</span>
            <span v-else style="color: #999">-</span>
          </template>
          <template v-if="column.key === 'submitted_at'">
            {{ formatTime(record.submitted_at) }}
          </template>
        </template>
        <template #expandedRowRender="{ record }">
          <div class="code-expand">
            <div v-if="record.error_message" class="error-info">
              <a-tag color="error">错误信息</a-tag>
              <pre class="error-pre">{{ record.error_message }}</pre>
            </div>
            <a-tag color="blue">源代码 ({{ langLabel(record.language) }})</a-tag>
            <pre class="code-pre">{{ record.source_code }}</pre>
          </div>
        </template>
      </a-table>
    </a-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { ArrowLeftOutlined } from '@ant-design/icons-vue'
import api from '@/api'

const submissions = ref([])
const loading = ref(true)

const columns = [
  { title: '#', dataIndex: 'id', key: 'id', width: 60 },
  { title: '题目', key: 'problem_title' },
  { title: '语言', key: 'language', width: 100 },
  { title: '结果', key: 'status', width: 100 },
  { title: '耗时', key: 'cpu_time', width: 100 },
  { title: '内存', key: 'memory', width: 100 },
  { title: '提交时间', key: 'submitted_at', width: 180 },
]

function statusColor(s) {
  if (s === 'AC') return 'success'
  if (s === 'WA') return 'warning'
  if (s === 'CE') return 'default'
  if (s === 'TLE' || s === 'MLE') return 'orange'
  if (s === 'RE' || s === 'SE') return 'error'
  return 'default'
}

function langLabel(lang) {
  const labels = { cpp: 'C++', c: 'C', py3: 'Python 3', java: 'Java' }
  return labels[lang] || lang
}

function formatMemory(bytes) {
  if (!bytes) return '0 KB'
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(0)} KB`
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`
}

function formatTime(timeStr) {
  return new Date(timeStr).toLocaleString('zh-CN')
}

async function loadSubmissions() {
  loading.value = true
  try {
    const res = await api.get('/oj/submissions')
    submissions.value = res.data || []
  } catch (e) {
    message.error('加载提交记录失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadSubmissions()
})
</script>

<style scoped>
.oj-subs-page {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  max-width: 1200px;
  margin: 0 auto;
}

.subs-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.code-expand {
  padding: 8px 0;
}

.error-info {
  margin-bottom: 12px;
}

.error-pre {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 12px;
  line-height: 1.5;
  color: #ff4d4f;
  background: #fff2f0;
  padding: 8px 12px;
  border-radius: 4px;
  white-space: pre-wrap;
  word-break: break-all;
  margin: 4px 0 0 0;
}

.code-pre {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 12px;
  line-height: 1.5;
  color: #cdd6f4;
  background: #1e1e2e;
  padding: 12px;
  border-radius: 6px;
  white-space: pre-wrap;
  word-break: break-all;
  margin: 4px 0 0 0;
  max-height: 400px;
  overflow-y: auto;
}
</style>
