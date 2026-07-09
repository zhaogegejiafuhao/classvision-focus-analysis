<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 20px; font-weight: bold; cursor: pointer" @click="$router.push('/')">
        ClassVision 课眼智析
      </span>
      <a-space>
        <a-button type="link" style="color: #fff" @click="$router.push('/persons')">人员管理</a-button>
        <a-button type="link" style="color: #fff" @click="$router.push('/rag')">知识库问答</a-button>
        <a-button type="link" style="color: #fff" @click="$router.push('/papers')">试卷批改</a-button>
        <a-button type="link" style="color: #fff" @click="$router.push('/classrooms')">历史课堂</a-button>
      </a-space>
    </a-layout-header>
    <a-layout-content style="padding: 40px; max-width: 900px; margin: 0 auto">
      <a-typography-title :level="2">开始课堂注意力分析</a-typography-title>
      <a-form :model="form" layout="vertical" @finish="startClass">
        <a-form-item label="课程名称" name="name" :rules="[{ required: true, message: '请输入课程名称' }]">
          <a-input v-model:value="form.name" placeholder="如：高等数学A" size="large" />
        </a-form-item>
        <a-form-item label="教师姓名" name="teacher" :rules="[{ required: true, message: '请输入教师姓名' }]">
          <a-space style="width: 100%">
            <a-input v-model:value="form.teacher" placeholder="如：张老师" size="large" style="flex: 1" />
            <a-select
              v-model:value="form.teacher_person_id"
              placeholder="选择已注册老师"
              style="width: 200px"
              allow-clear
              show-search
              :options="teacherOptions"
            />
          </a-space>
          <a-typography-text type="secondary">可选：关联已注册的老师身份（需先在人员管理中注册）</a-typography-text>
        </a-form-item>
        <a-form-item label="考场模式">
          <a-switch v-model:checked="form.exam_mode" />
          <span style="margin-left: 8px; color: #999">
            {{ form.exam_mode ? '启用异常行为检测与风险预警' : '普通注意力监测模式' }}
          </span>
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" size="large" :loading="loading">
            开始检测
          </a-button>
        </a-form-item>
      </a-form>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const form = ref({ name: '', teacher: '', exam_mode: false, teacher_person_id: null })
const loading = ref(false)
const teachers = ref([])

const teacherOptions = computed(() =>
  teachers.value.map(t => ({ value: t.id, label: t.name }))
)

async function loadTeachers() {
  try {
    const res = await axios.get('/api/persons', { params: { role: 'teacher' } })
    teachers.value = res.data || []
  } catch {
    teachers.value = []
  }
}

async function startClass() {
  loading.value = true
  try {
    const res = await axios.post('/api/classrooms', form.value)
    router.push(`/live/${res.data.id}`)
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await loadTeachers()
})
</script>
