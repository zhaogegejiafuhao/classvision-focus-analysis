<template>
  <div class="cv-page">
    <a-page-header title="课程资料" sub-title="查看教师分享的课件和资料" />

    <a-spin :spinning="loading">
      <a-empty v-if="materials.length === 0 && !loading" description="暂无课程资料" />
      <a-list v-else :data-source="materials" :pagination="{ pageSize: 10 }">
        <template #renderItem="{ item }">
          <a-list-item>
            <a-list-item-meta>
              <template #avatar>
                <a-avatar :style="{ backgroundColor: getFileColor(item.file_type) }">
                  {{ item.file_type.toUpperCase() }}
                </a-avatar>
              </template>
              <template #title>{{ item.title }}</template>
              <template #description>
                <div>{{ item.description || '无描述' }}</div>
                <div style="margin-top: 4px; font-size: 12px; color: #999">
                  {{ item.file_name }} · {{ formatSize(item.file_size) }} · {{ formatTime(item.created_at) }}
                </div>
              </template>
            </a-list-item-meta>
            <template #actions>
              <a-button type="link" @click="downloadFile(item)">下载</a-button>
            </template>
          </a-list-item>
        </template>
      </a-list>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '../api'

const materials = ref([])
const loading = ref(false)

async function fetchMaterials() {
  loading.value = true
  try {
    // 获取学生所在课堂，然后获取该课堂的课件
    const studentRes = await api.get('/me').catch(() => null)
    // 简单方式：获取所有课件，后端会根据角色过滤
    const res = await api.get('/materials')
    materials.value = res.data
  } catch { /* ignore */ } finally { loading.value = false }
}

function downloadFile(record) {
  window.open(`/api/materials/${record.id}/download`, '_blank')
}

function formatSize(bytes) {
  if (!bytes) return '0B'
  if (bytes < 1024) return bytes + 'B'
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + 'KB'
  return (bytes / 1048576).toFixed(1) + 'MB'
}

function formatTime(time) {
  if (!time) return ''
  return new Date(time).toLocaleString('zh-CN')
}

function getFileColor(type) {
  return { pdf: '#ff4d4f', pptx: '#fa8c16', ppt: '#fa8c16', docx: '#1890ff', mp4: '#722ed1' }[type] || '#666'
}

onMounted(fetchMaterials)
</script>
