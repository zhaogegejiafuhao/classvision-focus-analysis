<template>
  <div class="cv-page">
    <a-page-header title="课件管理" sub-title="上传和管理教学资源">
      <template #extra>
        <a-upload :before-upload="handleUpload" :show-upload-list="false" accept=".pdf,.pptx,.ppt,.docx,.doc,.mp4,.txt,.md">
          <a-button type="primary" :loading="uploading">上传课件</a-button>
        </a-upload>
      </template>
    </a-page-header>

    <a-card :loading="loading">
      <a-table :columns="columns" :data-source="materials" row-key="id" :pagination="{ pageSize: 10 }">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key === 'file_type'">
            <a-tag :color="getFileColor(record.file_type)">{{ record.file_type }}</a-tag>
          </template>
          <template v-else-if="column.key === 'file_size'">
            {{ formatSize(record.file_size) }}
          </template>
          <template v-else-if="column.key === 'action'">
            <a-space>
              <a-button type="link" size="small" @click="downloadFile(record)">下载</a-button>
              <a-popconfirm title="确定删除？" @confirm="deleteMaterial(record.id)">
                <a-button type="link" danger size="small">删除</a-button>
              </a-popconfirm>
            </a-space>
          </template>
        </template>
      </a-table>
    </a-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '../api'

const materials = ref([])
const loading = ref(false)
const uploading = ref(false)

const columns = [
  { key: 'title', title: '标题', dataIndex: 'title' },
  { key: 'file_name', title: '文件名', dataIndex: 'file_name' },
  { key: 'file_type', title: '类型', width: 80 },
  { key: 'file_size', title: '大小', width: 100 },
  { key: 'created_at', title: '上传时间', dataIndex: 'created_at' },
  { key: 'action', title: '操作', width: 120 },
]

async function fetchMaterials() {
  loading.value = true
  try { const res = await api.get('/materials'); materials.value = res.data } catch { /* ignore */ } finally { loading.value = false }
}

async function handleUpload(file) {
  uploading.value = true
  try {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('title', file.name.replace(/\.[^.]+$/, ''))
    await api.post('/materials/upload', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
    message.success('上传成功')
    fetchMaterials()
  } catch { message.error('上传失败') } finally { uploading.value = false }
  return false
}

function downloadFile(record) {
  window.open(`/api/materials/${record.id}/download`, '_blank')
}

async function deleteMaterial(id) {
  try { await api.delete(`/materials/${id}`); message.success('删除成功'); fetchMaterials() } catch { /* ignore */ }
}

function formatSize(bytes) {
  if (bytes < 1024) return bytes + 'B'
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + 'KB'
  return (bytes / 1048576).toFixed(1) + 'MB'
}

function getFileColor(type) {
  return { pdf: 'red', pptx: 'orange', ppt: 'orange', docx: 'blue', mp4: 'purple' }[type] || 'default'
}

onMounted(fetchMaterials)
</script>
