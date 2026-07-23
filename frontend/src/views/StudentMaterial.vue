<template>
  <div class="cv-page">
    <a-page-header title="课程资料" sub-title="查看教师分享的课件和资料" />

    <!-- 课堂筛选 -->
    <div v-if="classrooms.length > 1" style="margin-bottom: 16px">
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

    <a-spin :spinning="loading">
      <a-empty v-if="materials.length === 0 && !loading" description="暂无课程资料" />
      <a-list v-else :data-source="materials" :pagination="{ pageSize: 10 }">
        <template #renderItem="{ item }">
          <a-list-item>
            <a-list-item-meta>
              <template #avatar>
                <a-avatar :style="{ backgroundColor: getFileColor(item.file_type) }">
                  {{ item.file_type?.toUpperCase() || '?' }}
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
import { listMaterials } from '@/api/material'

const materials = ref([])
const classrooms = ref([])
const selectedClassroomId = ref(undefined)
const loading = ref(false)

async function fetchMaterials() {
  loading.value = true
  try {
    // 获取学生所在课堂的课件
    const params = {}
    if (selectedClassroomId.value) {
      params.classroom_id = selectedClassroomId.value
    }
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
    // 如果只有一个课堂，自动选中
    if (classrooms.value.length === 1) {
      selectedClassroomId.value = classrooms.value[0].id
    }
  } catch { /* ignore */ }
}

function downloadFile(record) {
  window.open(`/api/materials/${record.id}/download`, '_blank')
}

function formatSize(bytes) {
  if (!bytes || bytes < 1024) return (bytes || 0) + 'B'
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

onMounted(async () => {
  await fetchClassrooms()
  await fetchMaterials()
})
</script>
