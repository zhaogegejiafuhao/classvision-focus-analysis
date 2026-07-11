<template>
  <div class="oj-list-page">
    <div class="oj-list-header">
      <a-typography-title :level="3" style="margin: 0">题目列表</a-typography-title>
      <a-space>
        <a-button type="primary" v-if="canManage" @click="openCreate">
          <template #icon><PlusOutlined /></template>
          创建题目
        </a-button>
        <a-button @click="$router.push('/oj/submissions')">
          <template #icon><HistoryOutlined /></template>
          提交记录
        </a-button>
        <a-button @click="$router.push('/oj/run')">
          <template #icon><CodeOutlined /></template>
          代码运行
        </a-button>
      </a-space>
    </div>

    <a-card style="margin-top: 16px">
      <a-skeleton v-if="loading && problems.length === 0" active :paragraph="{ rows: 8 }" />
      <a-table
        v-else
        :columns="columns"
        :data-source="problems"
        :loading="loading"
        row-key="id"
        :pagination="{ pageSize: 20, hideOnSinglePage: true }"
      >
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'title'">
            <a href="javascript:void(0)" @click.prevent="$router.push(`/oj/${record.id}`)">{{ record.title }}</a>
          </template>
          <template v-if="column.key === 'difficulty'">
            <a-tag :color="difficultyColor(record.difficulty)">{{ record.difficulty }}</a-tag>
          </template>
          <template v-if="column.key === 'rate'">
            <span v-if="record.submitted_count > 0">
              {{ ((record.accepted_count / record.submitted_count) * 100).toFixed(1) }}%
            </span>
            <span v-else style="color: #999">-</span>
          </template>
          <template v-if="column.key === 'stats'">
            <span style="color: #52c41a">{{ record.accepted_count }}</span> /
            <span style="color: #999">{{ record.submitted_count }}</span>
          </template>
          <template v-if="column.key === 'action'">
            <a-space v-if="canEditOrDelete(record)">
              <a-button type="link" size="small" @click="openEdit(record)">
                <template #icon><EditOutlined /></template>
                编辑
              </a-button>
              <a-popconfirm title="确定删除该题目？所有相关提交记录也将删除。" @confirm="deleteProblem(record)">
                <a-button type="link" danger size="small">
                  <template #icon><DeleteOutlined /></template>
                  删除
                </a-button>
              </a-popconfirm>
            </a-space>
            <span v-else style="color: #ccc">-</span>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 创建/编辑题目弹窗 -->
    <a-modal
      v-model:open="modalOpen"
      :title="editingId ? '编辑题目' : '创建题目'"
      :width="800"
      :confirm-loading="saving"
      ok-text="保存"
      cancel-text="取消"
      @ok="handleSave"
      @cancel="modalOpen = false"
    >
      <a-form layout="vertical" :model="form" style="max-height: 60vh; overflow-y: auto; padding-right: 8px">
        <a-form-item label="题目标题" required>
          <a-input v-model:value="form.title" placeholder="如：A+B Problem" />
        </a-form-item>
        <a-row :gutter="16">
          <a-col :span="8">
            <a-form-item label="难度">
              <a-select v-model:value="form.difficulty">
                <a-select-option value="简单">简单</a-select-option>
                <a-select-option value="中等">中等</a-select-option>
                <a-select-option value="困难">困难</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
          <a-col :span="8">
            <a-form-item label="时间限制 (ms)">
              <a-input-number v-model:value="form.time_limit" :min="100" :step="100" style="width: 100%" />
            </a-form-item>
          </a-col>
          <a-col :span="8">
            <a-form-item label="内存限制 (MB)">
              <a-input-number v-model:value="memoryMB" :min="16" :max="1024" :step="16" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-form-item label="题目描述" required>
          <a-textarea v-model:value="form.description" :rows="4" placeholder="描述题目的背景和要求" />
        </a-form-item>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="输入格式">
              <a-textarea v-model:value="form.input_format" :rows="3" />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="输出格式">
              <a-textarea v-model:value="form.output_format" :rows="3" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="样例输入">
              <a-textarea v-model:value="form.sample_input" :rows="3" />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="样例输出">
              <a-textarea v-model:value="form.sample_output" :rows="3" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-form-item label="提示">
          <a-textarea v-model:value="form.hint" :rows="2" />
        </a-form-item>

        <a-divider>测试用例</a-divider>
        <div v-for="(tc, idx) in form.test_cases" :key="idx" class="test-case-item">
          <a-row :gutter="8" align="middle">
            <a-col :span="10">
              <a-textarea v-model:value="tc.input" :rows="2" placeholder="输入" />
            </a-col>
            <a-col :span="10">
              <a-textarea v-model:value="tc.expected_output" :rows="2" placeholder="期望输出" />
            </a-col>
            <a-col :span="3">
              <a-checkbox v-model:checked="tc.is_sample">样例</a-checkbox>
            </a-col>
            <a-col :span="1">
              <a-button type="link" danger size="small" @click="form.test_cases.splice(idx, 1)">
                <DeleteOutlined />
              </a-button>
            </a-col>
          </a-row>
        </div>
        <a-button type="dashed" block style="margin-top: 8px" @click="addTestCase">
          <PlusOutlined /> 添加测试用例
        </a-button>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import {
  CodeOutlined, HistoryOutlined, PlusOutlined,
  EditOutlined, DeleteOutlined,
} from '@ant-design/icons-vue'
import api from '@/api'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()
const problems = ref([])
const loading = ref(true)

const canManage = computed(() => ['teacher', 'admin'].includes(userStore.role))
const currentUserId = computed(() => userStore.user?.id)

const columns = computed(() => {
  const cols = [
    { title: '#', dataIndex: 'id', key: 'id', width: 60 },
    { title: '题目', key: 'title' },
    { title: '难度', key: 'difficulty', width: 100 },
    { title: '通过率', key: 'rate', width: 100 },
    { title: '通过/提交', key: 'stats', width: 120 },
  ]
  if (canManage.value) {
    cols.push({ title: '操作', key: 'action', width: 160 })
  }
  return cols
})

function canEditOrDelete(record) {
  if (!canManage.value) return false
  if (userStore.role === 'admin') return true
  return record.created_by === currentUserId.value
}

function difficultyColor(d) {
  if (d === '简单') return 'green'
  if (d === '中等') return 'orange'
  return 'red'
}

const modalOpen = ref(false)
const editingId = ref(null)
const saving = ref(false)
const memoryMB = ref(256)
const form = ref(getEmptyForm())

function getEmptyForm() {
  return {
    title: '',
    description: '',
    input_format: '',
    output_format: '',
    sample_input: '',
    sample_output: '',
    hint: '',
    time_limit: 1000,
    memory_limit: 256 * 1024 * 1024,
    difficulty: '简单',
    test_cases: [],
  }
}

function addTestCase() {
  form.value.test_cases.push({ input: '', expected_output: '', is_sample: false })
}

function openCreate() {
  editingId.value = null
  form.value = getEmptyForm()
  memoryMB.value = 256
  modalOpen.value = true
}

async function openEdit(record) {
  editingId.value = record.id
  modalOpen.value = true
  try {
    const res = await api.get(`/oj/problems/${record.id}`)
    const d = res.data
    form.value = {
      title: d.title,
      description: d.description,
      input_format: d.input_format,
      output_format: d.output_format,
      sample_input: d.sample_input,
      sample_output: d.sample_output,
      hint: d.hint,
      time_limit: d.time_limit,
      memory_limit: d.memory_limit,
      difficulty: d.difficulty,
      test_cases: (d.sample_test_cases || []).map(tc => ({
        input: tc.input,
        expected_output: tc.expected_output,
        is_sample: tc.is_sample,
      })),
    }
    memoryMB.value = Math.round(d.memory_limit / 1024 / 1024)
  } catch (e) {
    message.error('加载题目详情失败')
  }
}

async function handleSave() {
  if (!form.value.title.trim() || !form.value.description.trim()) {
    message.warning('请填写标题和描述')
    return
  }
  if (form.value.test_cases.length === 0) {
    message.warning('请至少添加一个测试用例')
    return
  }
  saving.value = true
  const payload = { ...form.value, memory_limit: memoryMB.value * 1024 * 1024 }
  try {
    if (editingId.value) {
      await api.put(`/oj/problems/${editingId.value}`, payload)
      message.success('题目已更新')
    } else {
      await api.post('/oj/problems', payload)
      message.success('题目已创建')
    }
    modalOpen.value = false
    loadProblems()
  } catch (e) {
    const detail = e.response?.data?.detail || '保存失败'
    message.error(detail)
  } finally {
    saving.value = false
  }
}

async function deleteProblem(record) {
  try {
    await api.delete(`/oj/problems/${record.id}`)
    message.success('题目已删除')
    loadProblems()
  } catch (e) {
    const detail = e.response?.data?.detail || '删除失败'
    message.error(detail)
  }
}

async function loadProblems() {
  loading.value = true
  try {
    const res = await api.get('/oj/problems')
    problems.value = res.data || []
    if (route.query.edit) {
      const target = problems.value.find(p => p.id === parseInt(route.query.edit))
      if (target && canEditOrDelete(target)) {
        openEdit(target)
      }
      router.replace({ query: {} })
    }
  } catch (e) {
    message.error('加载题目列表失败')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadProblems()
})
</script>

<style scoped>
.oj-list-page {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  max-width: 1200px;
  margin: 0 auto;
}

.oj-list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.test-case-item {
  margin-bottom: 8px;
  padding: 8px;
  background: #fafafa;
  border-radius: 4px;
}
</style>
