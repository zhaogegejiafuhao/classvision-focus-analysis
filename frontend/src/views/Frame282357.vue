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

        <a-card title="修改密码" style="margin-bottom: 16px">
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

        <a-card title="AI 模型配置" style="margin-bottom: 16px">
          <a-form layout="vertical">
            <a-form-item label="LLM 服务商">
              <a-select v-model:value="llmConfig.provider" @change="onProviderChange" style="width: 100%">
                <a-select-option v-for="p in availableProviders" :key="p.value" :value="p.value">
                  {{ p.label }}
                </a-select-option>
              </a-select>
            </a-form-item>

            <template v-if="llmConfig.provider === 'ollama'">
              <a-form-item label="Ollama 地址">
                <a-input v-model:value="llmConfig.ollama_host" placeholder="http://localhost:11434" />
              </a-form-item>
              <a-form-item label="深度模型">
                <a-input v-model:value="llmConfig.ollama_model" placeholder="qwen3:4b" />
              </a-form-item>
              <a-form-item label="快速模型">
                <a-input v-model:value="llmConfig.ollama_model_fast" placeholder="qwen2.5:3b" />
              </a-form-item>
            </template>

            <template v-else>
              <a-form-item label="API Key">
                <a-input-password v-model:value="llmConfig.api_key" :placeholder="llmConfig.api_key_set ? '已设置（留空保持不变）' : '输入 API Key'" />
              </a-form-item>
              <a-form-item label="API 地址">
                <a-input v-model:value="llmConfig.base_url" :placeholder="providerHint" />
              </a-form-item>
              <a-form-item label="深度模型名">
                <a-input v-model:value="llmConfig.model" placeholder="如 tencent/hunyuan-3、qwen-plus" />
              </a-form-item>
              <a-form-item label="快速模型名">
                <a-input v-model:value="llmConfig.model_fast" placeholder="如 qwen-turbo（留空则使用深度模型）" />
              </a-form-item>
            </template>

            <a-space>
              <a-button type="primary" :loading="savingLLM" @click="saveLLMConfig">保存配置</a-button>
              <a-button :loading="testingLLM" @click="testLLMConnection">测试连接</a-button>
            </a-space>
            <div v-if="llmTestResult" style="margin-top: 8px">
              <a-alert :type="llmTestResult.success ? 'success' : 'error'" :message="llmTestResult.message" show-icon />
            </div>
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

        <a-card title="通知偏好" style="margin-bottom: 16px">
          <a-form layout="vertical">
            <a-form-item label="作业通知">
              <a-switch v-model:checked="notifPrefs.homework" @change="saveNotifPrefs" />
            </a-form-item>
            <a-form-item label="考试通知">
              <a-switch v-model:checked="notifPrefs.exam" @change="saveNotifPrefs" />
            </a-form-item>
            <a-form-item label="签到通知">
              <a-switch v-model:checked="notifPrefs.attendance" @change="saveNotifPrefs" />
            </a-form-item>
          </a-form>
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
import { ref, computed, reactive, onMounted } from 'vue'
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

const notifPrefs = reactive({
  homework: true,
  exam: true,
  attendance: true,
})

// ── LLM 配置 ──
const llmConfig = reactive({
  provider: 'ollama',
  api_key: '',
  api_key_set: false,
  base_url: '',
  model: '',
  model_fast: '',
  ollama_host: 'http://localhost:11434',
  ollama_model: 'qwen3:4b',
  ollama_model_fast: 'qwen2.5:3b',
})
const availableProviders = ref([])
const savingLLM = ref(false)
const testingLLM = ref(false)
const llmTestResult = ref(null)

const providerHint = computed(() => {
  const p = availableProviders.value.find(x => x.value === llmConfig.provider)
  return p?.base_url || '输入 API Base URL'
})

async function loadLLMConfig() {
  try {
    const { data } = await api.get('/llm/config')
    llmConfig.provider = data.provider
    llmConfig.api_key_set = data.api_key_set
    llmConfig.base_url = data.base_url
    llmConfig.model = data.model
    llmConfig.model_fast = data.model_fast
    llmConfig.ollama_host = data.ollama_host
    llmConfig.ollama_model = data.ollama_model
    llmConfig.ollama_model_fast = data.ollama_model_fast
    availableProviders.value = data.available_providers || []
  } catch { /* ignore */ }
}

function onProviderChange(val) {
  const p = availableProviders.value.find(x => x.value === val)
  if (p?.base_url && p.base_url !== '本地') {
    llmConfig.base_url = p.base_url
  }
  llmTestResult.value = null
}

async function saveLLMConfig() {
  savingLLM.value = true
  try {
    const payload = { provider: llmConfig.provider }
    if (llmConfig.provider === 'ollama') {
      payload.ollama_host = llmConfig.ollama_host
      payload.ollama_model = llmConfig.ollama_model
      payload.ollama_model_fast = llmConfig.ollama_model_fast
    } else {
      if (llmConfig.api_key) payload.api_key = llmConfig.api_key
      payload.base_url = llmConfig.base_url
      payload.model = llmConfig.model
      payload.model_fast = llmConfig.model_fast
    }
    await api.put('/llm/config', payload)
    message.success('LLM 配置已保存')
    await loadLLMConfig()
  } catch (e) {
    message.error(e.response?.data?.detail || '保存失败')
  } finally {
    savingLLM.value = false
  }
}

async function testLLMConnection() {
  testingLLM.value = true
  llmTestResult.value = null
  try {
    const { data } = await api.post('/llm/test')
    llmTestResult.value = data
  } catch (e) {
    llmTestResult.value = { success: false, message: e.response?.data?.detail || '测试失败' }
  } finally {
    testingLLM.value = false
  }
}

onMounted(() => {
  const saved = localStorage.getItem('notif_prefs')
  if (saved) {
    try { Object.assign(notifPrefs, JSON.parse(saved)) } catch { /* ignore */ }
  }
  loadLLMConfig()
})

function saveNotifPrefs() {
  localStorage.setItem('notif_prefs', JSON.stringify({ ...notifPrefs }))
  message.success('偏好已保存')
}

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
