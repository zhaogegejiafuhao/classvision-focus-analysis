<template>
  <div class="cv-page">
    <a-page-header title="课件管理" sub-title="上传和管理教学资源">
      <template #extra>
        <a-upload :before-upload="handleUpload" :show-upload-list="false" accept=".pdf,.pptx,.ppt,.docx,.doc,.mp4,.txt,.md">
          <a-button type="primary" :loading="uploading">上传课件</a-button>
        </a-upload>
      </template>
    </a-page-header>

    <!-- 课堂筛选 -->
    <div style="margin-bottom: 16px">
      <a-select
        v-model:value="selectedClassroomId"
        placeholder="按课堂筛选"
        allow-clear
        style="width: 240px"
        @change="fetchMaterials"
      >
        <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
      </a-select>
    </div>

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="materials" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'file_type'">
            <a-tag :color="getFileColor(record.file_type)">{{ record.file_type }}</a-tag>
          </template>
          <template v-else-if="column.key === 'file_size'">
            {{ formatSize(record.file_size) }}
          </template>
          <template v-else-if="column.key === 'classroom_name'">
            {{ record.classroom_name || '未关联课堂' }}
          </template>
          <template v-else-if="column.key === 'action'">
            <a-space>
              <a-button type="link" size="small" @click="downloadFile(record)">下载</a-button>
              <a-popconfirm title="确定删除？" @confirm="handleDeleteMaterial(record.id)">
                <a-button type="link" danger size="small">删除</a-button>
              </a-popconfirm>
            </a-space>
          </template>
        </template>
      </a-table>
    </a-card>

    <!-- 上传弹窗 -->
    <a-modal
      v-model:open="uploadModalOpen"
      title="上传课件"
      @ok="confirmUpload"
      :confirm-loading="uploading"
      ok-text="上传"
      cancel-text="取消"
    >
      <a-form layout="vertical">
        <a-form-item label="课件标题" required>
          <a-input v-model:value="uploadForm.title" placeholder="输入课件标题" />
        </a-form-item>
        <a-form-item label="关联课堂">
          <a-select v-model:value="uploadForm.classroom_id" placeholder="选择关联课堂" allow-clear style="width: 100%">
            <a-select-option v-for="c in classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="课件描述">
          <a-input v-model:value="uploadForm.description" placeholder="可选，输入课件描述" />
        </a-form-item>
        <a-form-item label="选择文件" required>
          <a-input :value="uploadForm.file_name" disabled placeholder="请先选择文件" />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { listMaterials, uploadMaterial, deleteMaterial } from '@/api/material'
import { listClassrooms } from '@/api/classroom'

const materials = ref([])
const classrooms = ref([])
const selectedClassroomId = ref(undefined)
const loading = ref(false)
const uploading = ref(false)
const uploadModalOpen = ref(false)
const uploadForm = ref({ title: '', classroom_id: undefined, description: '', file: null, file_name: '' })

const columns = [
  { key: 'title', title: '标题', dataIndex: 'title' },
  { key: 'classroom_name', title: '关联课堂', width: 150 },
  { key: 'file_name', title: '文件名', dataIndex: 'file_name' },
  { key: 'file_type', title: '类型', width: 80 },
  { key: 'file_size', title: '大小', width: 100 },
  { key: 'created_at', title: '上传时间', dataIndex: 'created_at' },
  { key: 'action', title: '操作', width: 120 },
]

async function fetchMaterials() {
  loading.value = true
  try {
    const params = {}
    if (selectedClassroomId.value) params.classroom_id = selectedClassroomId.value
    const res = await listMaterials(params)
    // 附加课堂名称
    const classMap = {}
    for (const c of classrooms.value) classMap[c.id] = c.name
    materials.value = (res.data || []).map(m => ({
      ...m,
      classroom_name: classMap[m.classroom_id] || '',
    }))
  } catch { /* ignore */ } finally { loading.value = false }
}

async function fetchClassrooms() {
  try {
    const res = await listClassrooms()
    classrooms.value = res.data || []
  } catch { /* ignore */ }
}

function handleUpload(file) {
  uploadForm.value = {
    title: file.name.replace(/\.[^.]+$/, ''),
    classroom_id: selectedClassroomId.value || undefined,
    description: '',
    file: file,
    file_name: file.name,
  }
  uploadModalOpen.value = true
  return false  // 阻止自动上传
}

async function confirmUpload() {
  if (!uploadForm.value.title) {
    message.warning('请输入课件标题')
    return
  }
  if (!uploadForm.value.file) {
    message.warning('请选择文件')
    return
  }
  uploading.value = true
  try {
    const formData = new FormData()
    formData.append('file', uploadForm.value.file)
    formData.append('title', uploadForm.value.title)
    if (uploadForm.value.classroom_id) formData.append('classroom_id', uploadForm.value.classroom_id)
    if (uploadForm.value.description) formData.append('description', uploadForm.value.description)
 const res = await uploadMaterial(formData)
    message.success('上传成功')
    uploadModalOpen.value = false
    fetchMaterials()
  } catch { message.error('上传失败') } finally { uploading.value = false }
}

function downloadFile(record) {
  window.open(`/api/materials/${record.id}/download`, '_blank')
}

async function handleDeleteMaterial(id) {
  try { await deleteMaterial(id); message.success('删除成功'); fetchMaterials() } catch { /* ignore */ }
}

function formatSize(bytes) {
  if (!bytes || bytes < 1024) return (bytes || 0) + 'B'
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + 'KB'
  return (bytes / 1048576).toFixed(1) + 'MB'
}

function getFileColor(type) {
  return { pdf: 'red', pptx: 'orange', ppt: 'orange', docx: 'blue', mp4: 'purple' }[type] || 'default'
}

onMounted(async () => {
  await fetchClassrooms()
  await fetchMaterials()
})
</script>
