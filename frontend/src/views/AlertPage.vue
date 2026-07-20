<template>
  <div class="cv-page">
    <a-page-header title="教学预警" sub-title="自动检测需要关注的学生">
      <template #extra>
        <a-tag color="red">高风险: {{ report.high || 0 }}</a-tag>
        <a-tag color="orange">总计: {{ report.total || 0 }}</a-tag>
      </template>
    </a-page-header>

    <a-spin :spinning="loading">
      <a-empty v-if="alerts.length === 0 && !loading" description="暂无预警，一切正常" />
      <a-list v-else :data-source="alerts" :pagination="{ pageSize: 10 }">
        <template #renderItem="{ item }">
          <a-list-item>
            <a-list-item-meta>
              <template #avatar>
                <a-avatar :style="{ backgroundColor: item.level === 'high' ? '#ff4d4f' : '#fa8c16' }">
                  {{ item.level === 'high' ? '!' : '?' }}
                </a-avatar>
              </template>
              <template #title>
                <a-tag :color="item.level === 'high' ? 'red' : 'orange'">{{ item.level === 'high' ? '高风险' : '中风险' }}</a-tag>
                <a-tag :color="typeColor(item.type)">{{ typeText(item.type) }}</a-tag>
                {{ item.student_name }} — {{ item.classroom_name }}
              </template>
              <template #description>{{ item.message }}</template>
            </a-list-item-meta>
          </a-list-item>
        </template>
      </a-list>
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../api'

const report = ref({})
const loading = ref(false)
const alerts = computed(() => report.value.alerts || [])

async function fetchData() {
  loading.value = true
  try { const res = await api.get('/alerts'); report.value = res.data } catch { /* ignore */ } finally { loading.value = false }
}

function typeColor(type) {
  return { attendance: 'purple', homework: 'green', exam: 'orange' }[type] || 'blue'
}
function typeText(type) {
  return { attendance: '出勤', homework: '作业', exam: '考试' }[type] || type
}

onMounted(fetchData)
</script>
