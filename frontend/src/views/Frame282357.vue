<template>
  <div class="cv-page" style="max-width: 800px">
    <a-typography-title :level="3">设置</a-typography-title>

    <a-row :gutter="16">
      <a-col :span="14">
        <a-card title="个人信息" style="margin-bottom: 16px">
          <a-descriptions :column="1" size="small">
            <a-descriptions-item label="用户名">{{ username }}</a-descriptions-item>
            <a-descriptions-item label="姓名">{{ displayName || '未设置' }}</a-descriptions-item>
            <a-descriptions-item label="角色">
              <a-tag :color="roleColor">{{ roleLabel }}</a-tag>
            </a-descriptions-item>
          </a-descriptions>
        </a-card>

        <a-card title="修改密码">
          <a-form layout="vertical" @finish="handleChangePassword">
            <a-form-item label="当前密码" name="oldPassword" :rules="[{ required: true, message: '请输入当前密码' }]">
              <a-input-password v-model:value="passwordForm.oldPassword" placeholder="输入当前密码" />
            </a-form-item>
            <a-form-item label="新密码" name="newPassword" :rules="[
              { required: true, message: '请输入新密码' },
              { min: 6, message: '密码至少6位' },
            ]">
              <a-input-password v-model:value="passwordForm.newPassword" placeholder="输入新密码（至少6位）" />
            </a-form-item>
            <a-form-item label="确认新密码" name="confirmPassword" :rules="[
              { required: true, message: '请确认新密码' },
              { validator: validateConfirmPassword },
            ]">
              <a-input-password v-model:value="passwordForm.confirmPassword" placeholder="再次输入新密码" />
            </a-form-item>
            <a-button type="primary" html-type="submit" :loading="changingPassword">修改密码</a-button>
          </a-form>
        </a-card>
      </a-col>

      <a-col :span="10">
        <a-card title="关于系统" style="margin-bottom: 16px">
          <a-descriptions :column="1" size="small">
            <a-descriptions-item label="系统名称">ClassVision</a-descriptions-item>
            <a-descriptions-item label="版本">1.0.0</a-descriptions-item>
            <a-descriptions-item label="描述">课堂学情智能实训平台</a-descriptions-item>
          </a-descriptions>
        </a-card>

        <a-card title="快捷操作">
          <a-space direction="vertical" style="width: 100%">
            <a-button block @click="goHelp">查看帮助中心</a-button>
            <a-popconfirm title="确定退出登录？" @confirm="handleLogout">
              <a-button block danger>退出登录</a-button>
            </a-popconfirm>
          </a-space>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import api from '@/api'
import { message } from 'ant-design-vue'

const router = useRouter()
const userStore = useUserStore()

const username = computed(() => userStore.username)
const displayName = computed(() => userStore.displayName)
const role = computed(() => userStore.role)

const roleLabel = computed(() => {
  const map = { teacher: '教师', student: '学生', admin: '管理员' }
  return map[role.value] || role.value
})

const roleColor = computed(() => {
  const map = { teacher: 'blue', student: 'green', admin: 'purple' }
  return map[role.value] || 'default'
})

const passwordForm = reactive({
  oldPassword: '',
  newPassword: '',
  confirmPassword: '',
})

const changingPassword = ref(false)

function validateConfirmPassword(_, value) {
  if (value !== passwordForm.newPassword) {
    return Promise.reject('两次输入的密码不一致')
  }
  return Promise.resolve()
}

async function handleChangePassword() {
  changingPassword.value = true
  try {
    await api.post('/auth/change-password', {
      old_password: passwordForm.oldPassword,
      new_password: passwordForm.newPassword,
    })
    message.success('密码修改成功')
    passwordForm.oldPassword = ''
    passwordForm.newPassword = ''
    passwordForm.confirmPassword = ''
  } catch (e) {
    message.error(e.response?.data?.detail || '密码修改失败')
  } finally {
    changingPassword.value = false
  }
}

function goHelp() {
  router.push('/help')
}

function handleLogout() {
  userStore.logout()
  router.push('/login')
}
</script>

<style scoped>
</style>
