<template>
  <div class="cv-page">
    <a-page-header title="课堂加入" sub-title="搜索并加入公开课堂，或使用邀请码加入" />

    <div class="join-content">
      <!-- 搜索公开课堂 -->
      <a-card title="公开课堂" style="margin-bottom: 20px">
        <a-input-search
          v-model:value="searchText"
          placeholder="输入课序号或课程名搜索"
          enter-button="搜索"
          style="max-width: 480px; margin-bottom: 16px"
          @search="fetchPublicClassrooms"
          @pressEnter="fetchPublicClassrooms"
        />
        <a-table
          :columns="publicColumns"
          :data-source="publicClassrooms"
          :loading="publicLoading"
          row-key="id"
          :pagination="{ pageSize: 8 }"
          size="middle"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'course_code'">
              {{ record.course_code || '-' }}
            </template>
            <template v-else-if="column.key === 'teacher_person_name'">
              {{ record.teacher_person_name || record.teacher }}
            </template>
            <template v-else-if="column.key === 'total_students'">
              <span>{{ record.total_students }} 人</span>
            </template>
            <template v-else-if="column.key === 'action'">
              <a-button type="primary" size="small" :loading="record._joining" @click="joinClassroom(record)">
                加入
              </a-button>
            </template>
          </template>
        </a-table>
      </a-card>

      <!-- 邀请码加入 -->
      <a-card title="邀请码加入" style="margin-bottom: 20px">
        <a-space>
          <a-input
            v-model:value="inviteCode"
            placeholder="请输入邀请码"
            style="width: 280px"
            @pressEnter="joinByCode"
          />
          <a-button type="primary" :loading="codeJoining" @click="joinByCode">
            通过邀请码加入
          </a-button>
        </a-space>
      </a-card>

      <!-- 已加入的课堂 -->
      <a-card title="已加入的课堂">
        <a-table
          :columns="myColumns"
          :data-source="myClassrooms"
          :loading="myLoading"
          row-key="id"
          :pagination="false"
          size="middle"
        >
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'course_code'">
              {{ record.course_code || '-' }}
            </template>
            <template v-else-if="column.key === 'teacher_person_name'">
              {{ record.teacher_person_name || record.teacher }}
            </template>
            <template v-else-if="column.key === 'action'">
              <a-button type="link" size="small" @click="goToClassroom(record)">进入课堂</a-button>
            </template>
          </template>
        </a-table>
        <a-empty v-if="!myLoading && myClassrooms.length === 0" description="暂未加入任何课堂" style="margin-top: 16px" />
      </a-card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import api from '../api'

const router = useRouter()

const searchText = ref('')
const publicClassrooms = ref([])
const publicLoading = ref(false)

const inviteCode = ref('')
const codeJoining = ref(false)

const myClassrooms = ref([])
const myLoading = ref(false)

const publicColumns = [
  { key: 'name', title: '课堂名', dataIndex: 'name' },
  { key: 'course_code', title: '课序号', width: 120 },
  { key: 'teacher_person_name', title: '教师', width: 120 },
  { key: 'total_students', title: '已加入人数', width: 110 },
  { key: 'action', title: '操作', width: 80 },
]

const myColumns = [
  { key: 'name', title: '课堂名', dataIndex: 'name' },
  { key: 'course_code', title: '课序号', width: 120 },
  { key: 'teacher_person_name', title: '教师', width: 120 },
  { key: 'action', title: '操作', width: 100 },
]

async function fetchPublicClassrooms() {
  publicLoading.value = true
  try {
    const res = await api.get('/classrooms/public', { params: { search: searchText.value } })
    publicClassrooms.value = res.data.map(c => ({ ...c, _joining: false }))
  } catch { /* ignore */ } finally {
    publicLoading.value = false
  }
}

async function fetchMyClassrooms() {
  myLoading.value = true
  try {
    const res = await api.get('/classrooms/my')
    myClassrooms.value = res.data
  } catch { /* ignore */ } finally {
    myLoading.value = false
  }
}

async function joinClassroom(record) {
  record._joining = true
  try {
    await api.post(`/classrooms/join/${record.id}`)
    message.success(`已成功加入「${record.name}」`)
    fetchMyClassrooms()
  } catch (e) {
    const detail = e.response?.data?.detail
    if (detail) message.warning(detail)
  } finally {
    record._joining = false
  }
}

async function joinByCode() {
  if (!inviteCode.value.trim()) {
    message.warning('请输入邀请码')
    return
  }
  codeJoining.value = true
  try {
    const res = await api.post('/classrooms/join', { invite_code: inviteCode.value.trim() })
    message.success(`已成功加入「${res.data.name}」`)
    inviteCode.value = ''
    fetchMyClassrooms()
  } catch (e) {
    const detail = e.response?.data?.detail
    if (detail) message.warning(detail)
  } finally {
    codeJoining.value = false
  }
}

function goToClassroom(record) {
  router.push(`/classrooms/${record.id}`)
}

onMounted(() => {
  fetchPublicClassrooms()
  fetchMyClassrooms()
})
</script>

<style scoped>
.cv-page {
  padding: 24px;
}

.join-content {
  max-width: 960px;
}
</style>
