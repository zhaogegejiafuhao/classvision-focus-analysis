<template>
  <div class="login-page" :class="`role-${currentRole}`">
    <!-- 整体蓝色渐变背景，消除割裂感 -->
    <div class="bg-gradient"></div>
    <div class="bg-pattern"></div>

    <!-- 返回落地页 -->
    <div class="back-home" @click="goHome">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      <span>返回首页</span>
    </div>

    <!-- 左侧装饰区 -->
    <div class="login-decor">
      <div class="decor-content">
        <!-- 角色图标 -->
        <div class="role-badge">
          <span class="role-emoji">{{ roleConfig.emoji }}</span>
          <span class="role-label">{{ roleConfig.label }}</span>
        </div>
        <!-- 装饰图案 SVG -->
        <div class="decor-pattern" v-html="roleConfig.pattern"></div>
        <!-- 角色标语 -->
        <h2 class="decor-title">{{ roleConfig.title }}</h2>
        <p class="decor-subtitle">{{ roleConfig.subtitle }}</p>
      </div>
    </div>

    <!-- 右侧表单区 -->
    <div class="login-form-area">
      <div class="form-card">
        <!-- 角色切换 -->
        <div class="role-switcher">
          <button
            v-for="r in roles"
            :key="r.key"
            class="role-tab"
            :class="{ active: currentRole === r.key }"
            @click="switchRole(r.key)"
          >
            <span>{{ r.emoji }}</span>
            <span>{{ r.label }}</span>
          </button>
        </div>

        <h1 class="form-title">{{ isRegister ? '注册账号' : '欢迎登录' }}</h1>
        <p class="form-subtitle">{{ isRegister ? `创建您的${roleConfig.label}账号` : `${roleConfig.label}登录 Focus Mind 平台` }}</p>

        <form class="login-form" @submit.prevent="handleSubmit">
          <div v-if="isRegister" class="form-field">
            <label class="form-label">姓名</label>
            <input v-model="form.name" type="text" class="form-input" placeholder="请输入真实姓名" />
          </div>
          <div class="form-field">
            <label class="form-label">用户名</label>
            <input v-model="form.username" type="text" class="form-input" placeholder="请输入用户名" :disabled="loading" />
          </div>
          <div class="form-field">
            <label class="form-label">密码</label>
            <input v-model="form.password" type="password" class="form-input" placeholder="请输入密码" :disabled="loading" />
          </div>
          <div v-if="isRegister" class="form-field">
            <label class="form-label">确认密码</label>
            <input v-model="form.confirmPassword" type="password" class="form-input" placeholder="请再次输入密码" />
          </div>

          <div v-if="!isRegister" class="form-options">
            <label class="remember-me">
              <input type="checkbox" v-model="form.remember" />
              <span>记住我</span>
            </label>
            <span class="forgot-link" @click="showHint('请联系管理员重置密码')">忘记密码？</span>
          </div>

          <div v-if="errorMsg" class="form-error">{{ errorMsg }}</div>

          <button type="submit" class="btn-submit" :disabled="loading">
            {{ loading ? '处理中...' : (isRegister ? '注 册' : '登 录') }}
          </button>

          <div class="form-switch">
            <span>{{ isRegister ? '已有账号？' : '还没有账号？' }}</span>
            <span class="switch-link" @click="toggleMode">{{ isRegister ? '去登录' : '去注册' }}</span>
          </div>
        </form>

        <!-- 测试账号提示（仅登录模式） -->
        <div v-if="!isRegister" class="login-hint">
          <p class="hint-title">测试账号（点击填充）：</p>
          <div class="hint-list">
            <span class="hint-item" :class="{ active: currentRole === 'admin' }" @click="fillAccount('admin', 'admin123')">管理员</span>
            <span class="hint-item" :class="{ active: currentRole === 'teacher' }" @click="fillAccount('teacher', 'teacher123')">教师</span>
            <span class="hint-item" :class="{ active: currentRole === 'student' }" @click="fillAccount('student', 'student123')">学生</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const roles = [
  { key: 'student', label: '我是学生', emoji: '📚' },
  { key: 'teacher', label: '我是教师', emoji: '📋' },
  { key: 'admin', label: '我是管理员', emoji: '⚙️' },
]

const roleConfigs = {
  student: {
    label: '学生',
    emoji: '📚',
    title: '开启学习之旅',
    subtitle: '课堂互动 · OJ训练 · AI助教伴你成长',
    pattern: `<svg viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="40" y="50" width="120" height="90" rx="4" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="60" y1="75" x2="140" y2="75" stroke="rgba(255,255,255,0.25)" stroke-width="1.5"/>
      <line x1="60" y1="90" x2="120" y2="90" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="60" y1="105" x2="130" y2="105" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="60" y1="120" x2="100" y2="120" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <circle cx="100" cy="160" r="6" fill="rgba(255,255,255,0.15)"/>
    </svg>`,
  },
  teacher: {
    label: '教师',
    emoji: '📋',
    title: '高效管理课堂',
    subtitle: '学情分析 · 实时监控 · 智能辅助教学',
    pattern: `<svg viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="30" y="40" width="140" height="100" rx="6" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <rect x="30" y="40" width="140" height="12" fill="rgba(255,255,255,0.1)"/>
      <line x1="50" y1="70" x2="150" y2="70" stroke="rgba(255,255,255,0.3)" stroke-width="2"/>
      <line x1="50" y1="85" x2="130" y2="85" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="50" y1="100" x2="140" y2="100" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="50" y1="115" x2="110" y2="115" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <rect x="85" y="145" width="30" height="6" fill="rgba(255,255,255,0.1)"/>
      <rect x="70" y="155" width="60" height="4" rx="2" fill="rgba(255,255,255,0.08)"/>
    </svg>`,
  },
  admin: {
    label: '管理员',
    emoji: '⚙️',
    title: '全局运营管控',
    subtitle: '人员管理 · 系统配置 · 数据全局掌控',
    pattern: `<svg viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="35" y="45" width="55" height="45" rx="4" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <rect x="110" y="45" width="55" height="45" rx="4" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <rect x="35" y="110" width="55" height="45" rx="4" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <rect x="110" y="110" width="55" height="45" rx="4" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <circle cx="62" cy="67" r="8" fill="rgba(55,81,254,0.3)"/>
      <circle cx="137" cy="67" r="8" fill="rgba(255,255,255,0.15)"/>
      <line x1="48" y1="130" x2="78" y2="130" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="48" y1="140" x2="70" y2="140" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="123" y1="130" x2="153" y2="130" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
      <line x1="123" y1="140" x2="145" y2="140" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
    </svg>`,
  },
}

const currentRole = ref(route.query.role || 'teacher')
const isRegister = ref(route.query.mode === 'register')

const roleConfig = computed(() => roleConfigs[currentRole.value] || roleConfigs.teacher)

const form = reactive({
  name: '',
  username: '',
  password: '',
  confirmPassword: '',
  remember: false,
})
const loading = ref(false)
const errorMsg = ref('')

watch(() => route.query, (q) => {
  if (q.role) currentRole.value = q.role
  if (q.mode) isRegister.value = q.mode === 'register'
}, { immediate: true })

function switchRole(role) {
  currentRole.value = role
  errorMsg.value = ''
  router.replace({ path: '/login', query: { role, mode: isRegister.value ? 'register' : 'login' } })
}

function toggleMode() {
  isRegister.value = !isRegister.value
  errorMsg.value = ''
  router.replace({ path: '/login', query: { role: currentRole.value, mode: isRegister.value ? 'register' : 'login' } })
}

function goHome() {
  router.push('/')
}

function fillAccount(username, password) {
  form.username = username
  form.password = password
  errorMsg.value = ''
}

function showHint(msg) {
  errorMsg.value = msg
}

async function handleSubmit() {
  if (isRegister.value) {
    if (!form.name || !form.username || !form.password) {
      errorMsg.value = '请填写完整信息'
      return
    }
    if (form.password !== form.confirmPassword) {
      errorMsg.value = '两次密码不一致'
      return
    }
    if (form.password.length < 6) {
      errorMsg.value = '密码至少6位'
      return
    }
    loading.value = true
    errorMsg.value = ''
    try {
      const res = await api.post('/auth/register', {
        name: form.name,
        username: form.username,
        password: form.password,
        role: 'student',
      })
      // 注册成功，自动登录
      localStorage.setItem('token', res.data.access_token)
      localStorage.setItem('user', JSON.stringify(res.data.user))
      router.push('/app')
    } catch (err) {
      errorMsg.value = err.response?.data?.detail || '注册失败'
    } finally {
      loading.value = false
    }
    return
  }
  if (!form.username || !form.password) {
    errorMsg.value = '请输入用户名和密码'
    return
  }
  loading.value = true
  errorMsg.value = ''
  try {
    await userStore.login(form.username, form.password)
    router.push('/app')
  } catch (err) {
    errorMsg.value = err.response?.data?.detail || '登录失败，请重试'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  position: relative;
  overflow: hidden;
  font-family: "Roboto-Regular", "PingFang SC", "Microsoft YaHei", sans-serif;
}

/* 统一蓝色渐变背景 - 消除割裂感 */
.bg-gradient {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #4a63ff 0%, #3751FE 40%, #2d42d4 100%);
  z-index: 0;
}

/* 角色色调微调（统一蓝色，轻微差异） */
.role-student .bg-gradient {
  background: linear-gradient(135deg, #5a73ff 0%, #3751FE 40%, #2d42d4 100%);
}
.role-teacher .bg-gradient {
  background: linear-gradient(135deg, #4a63ff 0%, #3751FE 40%, #1e30b8 100%);
}
.role-admin .bg-gradient {
  background: linear-gradient(135deg, #3d56e8 0%, #2d42d4 40%, #1a23a8 100%);
}

.bg-pattern {
  position: absolute;
  inset: 0;
  background-image:
    radial-gradient(circle at 20% 80%, rgba(255,255,255,0.06) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.05) 0%, transparent 50%);
  z-index: 0;
}

/* 返回首页 */
.back-home {
  position: fixed;
  top: 24px;
  left: 24px;
  display: flex;
  align-items: center;
  gap: 6px;
  color: rgba(255,255,255,0.8);
  font-size: 14px;
  cursor: pointer;
  z-index: 10;
  padding: 8px 16px;
  border-radius: 100px;
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(8px);
  transition: all 0.2s;
}

.back-home:hover {
  background: rgba(255,255,255,0.2);
  color: #fff;
}

/* 左侧装饰区 */
.login-decor {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
  padding: 40px;
}

.decor-content {
  text-align: center;
  max-width: 400px;
  color: #fff;
}

.role-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 20px;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 100px;
  margin-bottom: 40px;
  backdrop-filter: blur(8px);
}

.role-emoji {
  font-size: 20px;
}

.role-label {
  font-size: 15px;
  font-weight: 600;
  color: #fff;
}

.decor-pattern {
  width: 200px;
  height: 200px;
  margin: 0 auto 32px;
}

.decor-pattern svg {
  width: 100%;
  height: 100%;
}

.decor-title {
  font-size: 36px;
  font-weight: 800;
  margin: 0 0 12px 0;
  line-height: 1.3;
  letter-spacing: -0.5px;
}

.decor-subtitle {
  font-size: 16px;
  color: rgba(255,255,255,0.8);
  margin: 0;
  line-height: 1.6;
}

/* 右侧表单区 */
.login-form-area {
  flex: 0 0 480px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
  padding: 40px;
}

.form-card {
  width: 100%;
  max-width: 400px;
  background: rgba(255,255,255,0.98);
  border-radius: 20px;
  padding: 40px 36px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.2);
  backdrop-filter: blur(20px);
}

/* 角色切换 */
.role-switcher {
  display: flex;
  gap: 8px;
  margin-bottom: 28px;
  background: #f5f6fa;
  padding: 4px;
  border-radius: 12px;
}

.role-tab {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 10px 8px;
  font-size: 13px;
  color: #666;
  background: transparent;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.role-tab.active {
  background: #3751FE;
  color: #fff;
  box-shadow: 0 2px 8px rgba(55,81,254,0.3);
}

.form-title {
  font-size: 26px;
  font-weight: 700;
  color: #1a1a2e;
  margin: 0 0 8px 0;
}

.form-subtitle {
  font-size: 14px;
  color: #888;
  margin: 0 0 28px 0;
}

/* 表单 */
.login-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label {
  font-size: 13px;
  font-weight: 600;
  color: #374151;
}

.form-input {
  width: 100%;
  padding: 12px 14px;
  border: 1.5px solid #e0e0e0;
  border-radius: 8px;
  font-size: 14px;
  background: #fafbfc;
  outline: none;
  box-sizing: border-box;
  transition: all 0.2s;
}

.form-input:focus {
  border-color: #3751FE;
  background: #fff;
  box-shadow: 0 0 0 3px rgba(55,81,254,0.1);
}

.form-input:disabled {
  cursor: not-allowed;
  opacity: 0.7;
}

.form-options {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #666;
  cursor: pointer;
}

.remember-me input {
  width: 14px;
  height: 14px;
  accent-color: #3751FE;
}

.forgot-link {
  font-size: 13px;
  color: #3751FE;
  cursor: pointer;
}

.forgot-link:hover {
  text-decoration: underline;
}

.form-error {
  color: #ef4444;
  font-size: 13px;
  text-align: center;
  padding: 8px 12px;
  background: rgba(239,68,68,0.08);
  border-radius: 8px;
}

.btn-submit {
  padding: 14px;
  background: #3751FE;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 4px;
}

.btn-submit:hover:not(:disabled) {
  background: #2d42d4;
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(55,81,254,0.3);
}

.btn-submit:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}

.form-switch {
  text-align: center;
  font-size: 14px;
  color: #888;
  margin-top: 4px;
}

.switch-link {
  color: #3751FE;
  cursor: pointer;
  font-weight: 600;
}

.switch-link:hover {
  text-decoration: underline;
}

/* 测试账号 */
.login-hint {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #f0f0f0;
}

.hint-title {
  font-size: 12px;
  color: #999;
  margin: 0 0 10px 0;
}

.hint-list {
  display: flex;
  gap: 8px;
}

.hint-item {
  flex: 1;
  text-align: center;
  font-size: 13px;
  color: #666;
  cursor: pointer;
  padding: 8px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  transition: all 0.2s;
}

.hint-item:hover {
  border-color: #3751FE;
  color: #3751FE;
}

.hint-item.active {
  background: #eef1ff;
  border-color: #3751FE;
  color: #3751FE;
  font-weight: 600;
}

/* 响应式 */
@media (max-width: 1024px) {
  .login-decor {
    display: none;
  }
  .login-form-area {
    flex: 1;
  }
}

@media (max-width: 768px) {
  .login-page {
    flex-direction: column;
  }
  .login-form-area {
    padding: 20px;
    flex: 1;
  }
  .form-card {
    padding: 28px 20px;
  }
  .form-title {
    font-size: 22px;
  }
  .role-tab {
    font-size: 12px;
    padding: 8px 4px;
  }
  .role-tab span:last-child {
    display: none;
  }
}
</style>
