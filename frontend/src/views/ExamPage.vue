<template>
  <div class="cv-page">
    <a-page-header title="考试管理" sub-title="创建和管理在线考试">
      <template #extra>
        <a-button type="primary" @click="showCreateModal = true">创建考试</a-button>
      </template>
    </a-page-header>

    <!-- 课堂筛选 -->
    <div style="margin-bottom: 16px">
      <a-select
        v-model:value="selectedClassroomId"
        placeholder="按课堂筛选"
        allow-clear
        style="width: 240px"
        @change="fetchExams"
      >
        <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
      </a-select>
    </div>

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="exams" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'title'">
	            <a @click="goDetail(record.id)">{{ record.title }}</a>
	          </template>
	          <template v-else-if="column.key === 'exam_type'">
	            <a-tag :color="record.exam_type === 'paper' ? '#722ed1' : '#1890ff'">
	              {{ record.exam_type === 'paper' ? '📝 笔试' : '💻 机试' }}
	            </a-tag>
	          </template>
          <template v-else-if="column.key === 'status'">
            <a-tag :color="getStatusColor(record.status)">{{ getStatusText(record.status) }}</a-tag>
          </template>
          <template v-else-if="column.key === 'action'">
            <a-space>
              <a-button type="link" size="small" @click="goDetail(record.id)">详情</a-button>
              <a-popconfirm v-if="record.status === 'draft'" title="确定发布考试？" @confirm="handlePublishExam(record.id)">
                <a-button type="link" size="small">发布</a-button>
              </a-popconfirm>
              <a-popconfirm title="确定删除？" @confirm="handleDeleteExam(record.id)">
                <a-button type="link" danger size="small">删除</a-button>
              </a-popconfirm>
            </a-space>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 创建考试弹窗 -->
    <a-modal v-model:open="showCreateModal" title="创建考试" @ok="handleCreateExam" :confirm-loading="submitting" width="700px">
      <a-form :label-col="{ span: 4 }" :wrapper-col="{ span: 18 }">
        <a-form-item label="考试标题" required>
          <a-input v-model:value="form.title" placeholder="考试标题" />
        </a-form-item>
        <a-form-item label="考试说明">
          <a-textarea v-model:value="form.description" placeholder="考试说明" :rows="3" />
        </a-form-item>
        <a-form-item label="关联课堂">
          <a-select v-model:value="form.classroom_id" placeholder="选择课堂" allow-clear style="width: 100%">
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="考试时长">
          <a-input-number v-model:value="form.duration" :min="10" :max="180" addon-after="分钟" />
        </a-form-item>
        <a-form-item label="总分">
	          <a-input-number v-model:value="form.total_score" :min="10" :max="500" />
	        </a-form-item>
	        <a-form-item label="考试类型">
	          <a-radio-group v-model:value="form.exam_type">
	            <a-radio-button value="computer">💻 机试</a-radio-button>
	            <a-radio-button value="paper">📝 笔试</a-radio-button>
	          </a-radio-group>
	        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import { listExams, createExam, deleteExam } from '@/api/exam'
import { publishExam as publishExamWithPayload } from '@/api/examTemplate'
import { listClassrooms } from '@/api/classroom'

const router = useRouter()
const exams = ref([])
const classrooms = ref([])
const selectedClassroomId = ref(undefined)
const loading = ref(false)
const submitting = ref(false)
const showCreateModal = ref(false)

const form = ref({
  title: '',
  description: '',
  classroom_id: null,
  duration: 60,
  total_score: 100,
  exam_type: 'computer',
})

const columns = [
  { key: 'title', title: '标题', dataIndex: 'title' },
  { key: 'classroom', title: '课堂', dataIndex: 'classroom_name' },
  { key: 'exam_type', title: '类型' },
  { key: 'duration', title: '时长', dataIndex: 'duration', suffix: '分钟' },
  { key: 'questions', title: '题目数', dataIndex: 'question_count' },
  { key: 'status', title: '状态', dataIndex: 'status' },
  { key: 'action', title: '操作' },
]

async function fetchExams() {
  loading.value = true
  try {
    const params = {}
    if (selectedClassroomId.value) params.classroom_id = selectedClassroomId.value
    const res = await listExams(params)
    exams.value = res.data
  } catch (e) {
    message.error('获取考试列表失败')
  } finally {
    loading.value = false
  }
}

async function fetchClassrooms() {
  try {
    const res = await listClassrooms()
    classrooms.value = res.data
  } catch (e) {
    // 忽略
  }
}

async function handleCreateExam() {
  if (!form.value.title.trim()) {
    message.error('请输入考试标题')
    return
  }
  submitting.value = true
  try {
    await createExam({
      title: form.value.title,
      description: form.value.description,
      classroom_id: form.value.classroom_id,
      duration: form.value.duration,
      total_score: form.value.total_score,
      exam_type: form.value.exam_type,
      questions: [],
    })
    message.success('考试创建成功，请在详情页添加题目')
    showCreateModal.value = false
    resetForm()
    fetchExams()
  } catch (e) {
    message.error('创建失败')
  } finally {
    submitting.value = false
  }
}

async function handlePublishExam(id) {
  try {
    const res = await publishExamWithPayload(id, {})
    message.success(`考试发布成功！${res.data.question_count} 题 / ${res.data.total_score} 分`)
    fetchExams()
  } catch (e) {
    const msg = e?.response?.data?.detail || '发布失败'
    message.error(msg)
  }
}

async function handleDeleteExam(id) {
  try {
    await deleteExam(id)
    message.success('删除成功')
    fetchExams()
  } catch (e) {
    message.error('删除失败')
  }
}

function resetForm() {
  form.value = {
    title: '',
    description: '',
    classroom_id: null,
    duration: 60,
    total_score: 100,
    exam_type: 'computer',
  }
}

function goDetail(id) {
  router.push(`/exams/${id}`)
}

function getStatusColor(status) {
  return { draft: 'default', published: 'blue', closed: 'gray' }[status] || 'default'
}

function getStatusText(status) {
  return { draft: '草稿', published: '已发布', closed: '已关闭' }[status] || status
}

onMounted(() => {
  fetchExams()
  fetchClassrooms()
})
</script>
