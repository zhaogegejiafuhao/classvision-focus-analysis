<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 20px; font-weight: bold; cursor: pointer" @click="$router.push('/')">
        ClassVision 课眼智析
      </span>
      <a-button type="link" style="color: #fff" @click="$router.push('/classrooms')">历史课堂</a-button>
    </a-layout-header>
    <a-layout-content style="padding: 40px; max-width: 900px; margin: 0 auto">
      <a-typography-title :level="2">开始课堂注意力分析</a-typography-title>
      <a-form :model="form" layout="vertical" @finish="startClass">
        <a-form-item label="课程名称" name="name" :rules="[{ required: true, message: '请输入课程名称' }]">
          <a-input v-model:value="form.name" placeholder="如：高等数学A" size="large" />
        </a-form-item>
        <a-form-item label="教师姓名" name="teacher" :rules="[{ required: true, message: '请输入教师姓名' }]">
          <a-input v-model:value="form.teacher" placeholder="如：张老师" size="large" />
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const form = ref({ name: '', teacher: '' })
const loading = ref(false)

async function startClass() {
  loading.value = true
  try {
    const res = await axios.post('/api/classrooms', form.value)
    router.push(`/live/${res.data.id}`)
  } finally {
    loading.value = false
  }
}
</script>
