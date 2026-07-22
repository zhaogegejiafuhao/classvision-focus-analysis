<template>
  <a-layout class="main-layout">
    <a-layout-sider
      v-model:collapsed="collapsed"
      :trigger="null"
      collapsible
      :width="240"
      :collapsedWidth="64"
      class="app-sider"
    >
      <div class="logo-area" @click="navigate('/app')">
        <span class="logo-icon">FM</span>
        <span v-if="!collapsed" class="logo-text">Focus Mind</span>
      </div>

      <div v-if="!collapsed && canCreate" class="create-btn-wrap">
        <button class="create-btn" @click="openCreateModal">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          <span>新建课堂</span>
        </button>
      </div>

      <a-menu
        v-model:selectedKeys="selectedKeys"
        mode="inline"
        theme="light"
        class="app-menu"
        @click="onMenuClick"
      >
        <a-menu-item key="/app">
          <template #icon><HomeOutlined /></template>
          <span>首页</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="start-class">
          <template #icon><VideoCameraOutlined /></template>
          <span>开始课堂</span>
        </a-menu-item>

        <a-menu-item key="/classrooms">
          <template #icon><BookOutlined /></template>
          <span>{{ currentRole === 'student' ? '我的课堂' : '课堂管理' }}</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'student' || currentRole === 'admin'" key="/join-class">
          <template #icon><UserAddOutlined /></template>
          <span>课堂加入</span>
        </a-menu-item>

        <a-menu-item key="/calendar">
          <template #icon><CalendarOutlined /></template>
          <span>课程日历</span>
        </a-menu-item>

        <a-menu-item key="/report">
          <template #icon><BarChartOutlined /></template>
          <span>{{ currentRole === 'student' ? '我的报告' : '注意力报告' }}</span>
        </a-menu-item>

        <a-divider style="margin: 8px 0" />

        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/question-bank">
          <template #icon><DatabaseOutlined /></template>
          <span>题库管理</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/materials">
          <template #icon><FolderOutlined /></template>
          <span>课件管理</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/grades">
          <template #icon><FundOutlined /></template>
          <span>综合成绩</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/teaching-plans">
          <template #icon><EditOutlined /></template>
          <span>教学计划</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/alerts">
          <template #icon><AlertOutlined /></template>
          <span>教学预警</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/ai-grading">
          <template #icon><RobotOutlined /></template>
          <span>AI数学批改</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/ai-essay-grading">
          <template #icon><FormOutlined /></template>
          <span>AI作文批改</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/knowledge-analysis">
          <template #icon><RadarChartOutlined /></template>
          <span>知识归因分析</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/my-similar-questions">
          <template #icon><ThunderboltOutlined /></template>
          <span>相似题管理</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/mistake-book">
          <template #icon><ReadOutlined /></template>
          <span>错题本</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/answer-sheet">
          <template #icon><ScanOutlined /></template>
          <span>答题卡扫描</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/experiments">
          <template #icon><DatabaseOutlined /></template>
          <span>实验报告</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/leaves">
          <template #icon><FileTextOutlined /></template>
          <span>请假管理</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/behavior">
          <template #icon><BarChartOutlined /></template>
          <span>行为分析</span>
        </a-menu-item>

        <a-divider style="margin: 8px 0" />

        <a-menu-item key="/settings">
          <template #icon><SettingOutlined /></template>
          <span>设置</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/persons">
          <template #icon><TeamOutlined /></template>
          <span>{{ personsLabel }}</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'admin'" key="/roster">
          <template #icon><SolutionOutlined /></template>
          <span>花名册</span>
        </a-menu-item>

        <a-menu-item key="/rag">
          <template #icon><FileTextOutlined /></template>
          <span>RAG 文档库</span>
        </a-menu-item>

        <a-menu-item key="/oj">
          <template #icon><CodeOutlined /></template>
          <span>OJ 判题</span>
        </a-menu-item>

        <a-divider v-if="currentRole === 'student'" style="margin: 8px 0" />

        <a-menu-item v-if="currentRole === 'student'" key="/student/homework">
          <template #icon><FileTextOutlined /></template>
          <span>我的作业</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'student'" key="/student/checkin">
          <template #icon><CalendarOutlined /></template>
          <span>签到考勤</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'student'" key="/student/exams">
          <template #icon><SolutionOutlined /></template>
          <span>我的考试</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'student'" key="/student/materials">
          <template #icon><FolderOutlined /></template>
          <span>课程资料</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'student'" key="/student/grades">
          <template #icon><FundOutlined /></template>
          <span>我的成绩</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'student'" key="/student/grading">
          <template #icon><FileSearchOutlined /></template>
          <span>我的批改</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'student'" key="/knowledge-analysis">
          <template #icon><RadarChartOutlined /></template>
          <span>我的知识画像</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'student'" key="/mistake-book">
          <template #icon><ReadOutlined /></template>
          <span>错题本</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'student'" key="/my-similar-questions">
          <template #icon><ThunderboltOutlined /></template>
          <span>错题强化</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'student'" key="/experiments">
          <template #icon><DatabaseOutlined /></template>
          <span>实验报告</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'student'" key="/leaves">
          <template #icon><FileTextOutlined /></template>
          <span>请假管理</span>
        </a-menu-item>
        <a-menu-item v-if="currentRole === 'student'" key="/behavior">
          <template #icon><BarChartOutlined /></template>
          <span>行为分析</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'student'" key="/notifications">
          <template #icon><BellOutlined /></template>
          <span>消息通知</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/homework">
          <template #icon><FileTextOutlined /></template>
          <span>作业管理</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/checkin">
          <template #icon><CalendarOutlined /></template>
          <span>考勤管理</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'teacher' || currentRole === 'admin'" key="/exams">
          <template #icon><SolutionOutlined /></template>
          <span>考试管理</span>
        </a-menu-item>

        <a-menu-item v-if="currentRole === 'admin'" key="/analytics">
          <template #icon><DashboardOutlined /></template>
          <span>数据分析</span>
        </a-menu-item>

        <a-menu-item key="/help">
          <template #icon><QuestionCircleOutlined /></template>
          <span>帮助</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>

    <a-layout class="app-body">
      <a-layout-header class="app-header">
        <div class="header-left">
          <button class="collapse-btn" @click="collapsed = !collapsed">
            <MenuFoldOutlined v-if="!collapsed" />
            <MenuUnfoldOutlined v-else />
          </button>
          <span class="header-title">{{ currentPageTitle }}</span>
        </div>
        <div class="header-right">
          <a-badge :count="unreadCount" :overflow-count="99" style="margin-right: 16px">
            <a-button type="text" @click="$router.push('/notifications')">
              <BellOutlined />
            </a-button>
          </a-badge>
          <span class="role-badge" :class="'role-' + currentRole">{{ roleLabel }}</span>
          <span class="user-name">{{ userStore.displayName }}</span>
          <button class="logout-btn" @click="handleLogout">退出</button>
        </div>
      </a-layout-header>

      <a-layout-content class="app-content">
        <router-view v-slot="{ Component }">
          <transition name="page-fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </a-layout-content>
    </a-layout>

    <!-- 开始课堂模态框 -->
    <a-modal
      v-model:open="showStartClassModal"
      title="开始新课堂"
      @ok="handleStartClass"
      :confirm-loading="startClassLoading"
      ok-text="开始检测"
      cancel-text="取消"
    >
      <a-form layout="vertical">
        <a-form-item label="课程名称" required>
          <a-input v-model:value="startClassForm.name" placeholder="例如：高一(3)班 数学" />
        </a-form-item>
        <a-form-item label="课序号">
          <a-input v-model:value="startClassForm.course_code" placeholder="例如：CS101" />
        </a-form-item>
      </a-form>
    </a-modal>
  </a-layout>
</template>

<script setup>
import { ref, computed, watch, provide, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import api from '@/api'

import {
  HomeOutlined,
  BookOutlined,
  CalendarOutlined,
  BarChartOutlined,
  SettingOutlined,
  TeamOutlined,
  SolutionOutlined,
  FileTextOutlined,
  CodeOutlined,
  DashboardOutlined,
  UserAddOutlined,
  QuestionCircleOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  BellOutlined,
  DatabaseOutlined,
  FolderOutlined,
  FundOutlined,
  EditOutlined,
  AlertOutlined,
  RobotOutlined,
  FormOutlined,
  FileSearchOutlined,
  RadarChartOutlined,
  ThunderboltOutlined,
  VideoCameraOutlined,
  ScanOutlined,
  ReadOutlined,
} from '@ant-design/icons-vue'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const collapsed = ref(false)
const selectedKeys = ref([route.path])
let notificationTimer = null

// 开始课堂模态框
const showStartClassModal = ref(false)
const startClassLoading = ref(false)
const startClassForm = ref({
  name: '',
  course_code: '',
})

function openStartClassModal() {
  startClassForm.value = { name: '', course_code: '' }
  showStartClassModal.value = true
}

async function handleStartClass() {
  if (!startClassForm.value.name) {
    return
  }
  startClassLoading.value = true
  try {
    const res = await api.post('/classrooms', {
      name: startClassForm.value.name,
      teacher: userStore.displayName,
      course_code: startClassForm.value.course_code,
      is_public: true,
    })
    if (res.data.id) {
      showStartClassModal.value = false
      router.push(`/live/${res.data.id}`)
    }
  } catch (e) {
    console.error('创建课堂失败', e)
  } finally {
    startClassLoading.value = false
  }
}

function checkScreenWidth() {
  if (window.innerWidth <= 1024 && window.innerWidth > 768) {
    collapsed.value = true
  }
}
onMounted(() => {
  checkScreenWidth()
  window.addEventListener('resize', checkScreenWidth)
  fetchUnreadCount()
  // 每30秒自动刷新通知未读数
  notificationTimer = setInterval(fetchUnreadCount, 30000)
})
onUnmounted(() => {
  window.removeEventListener('resize', checkScreenWidth)
  if (notificationTimer) clearInterval(notificationTimer)
})

const unreadCount = ref(0)

async function fetchUnreadCount() {
  try {
    const token = userStore.token || localStorage.getItem('token')
    if (!token) return
    const { data } = await api.get('/notifications/unread-count', { _skipGlobalError: true })
    unreadCount.value = data.unread_count
  } catch (e) {
    // 忽略错误
  }
}

const currentRole = computed(() => userStore.role || 'teacher')

const canCreate = computed(() => currentRole.value === 'teacher' || currentRole.value === 'admin')

const roleLabel = computed(() => {
  const labels = { teacher: '教师', student: '学生', admin: '管理员' }
  return labels[currentRole.value] || '教师'
})

const personsLabel = computed(() => {
  return currentRole.value === 'admin' ? '用户管理' : '学生管理'
})

const currentPageTitle = computed(() => {
  const titles = {
    '/app': '首页看板',
    '/classrooms': currentRole.value === 'student' ? '我的课堂' : '课堂管理',
    '/join-class': '课堂加入',
    '/calendar': '课程日历',
    '/report': currentRole.value === 'student' ? '我的报告' : '注意力报告',
    '/my-report': '我的报告',
    '/settings': '设置',
    '/persons': personsLabel.value,
    '/roster': '花名册',
    '/rag': 'RAG 文档库',
    '/oj': '题目列表',
    '/oj/run': '代码运行',
    '/oj/submissions': '提交记录',
    '/analytics': '数据分析',
    '/help': '帮助',
    '/homework': '作业管理',
    '/checkin': '考勤管理',
    '/exams': '考试管理',
    '/notifications': '消息通知',
    '/student/homework': '我的作业',
    '/student/checkin': '签到考勤',
    '/student/exams': '我的考试',
    '/student/materials': '课程资料',
    '/student/grades': '我的成绩',
    '/question-bank': '题库管理',
    '/materials': '课件管理',
    '/grades': '综合成绩',
    '/teaching-plans': '教学计划',
    '/alerts': '教学预警',
    '/experiments': '实验报告',
    '/leaves': '请假管理',
    '/behavior': '行为分析',
    '/ai-grading': 'AI数学批改',
    '/ai-essay-grading': 'AI作文批改',
    '/student/grading': '我的批改',
    '/knowledge-analysis': currentRole.value === 'student' ? '我的知识画像' : '知识归因分析',
    '/similar-questions': currentRole.value === 'student' ? '错题强化' : '相似题推荐',
    '/answer-sheet': '答题卡扫描批改',
    '/mistake-book': '错题本',
    '/my-similar-questions': '我的相似题',
  }
  if (titles[route.path]) return titles[route.path]
  if (route.path.startsWith('/oj/') && !route.path.startsWith('/oj/run') && !route.path.startsWith('/oj/submissions')) {
    return '题目详情'
  }
  if (route.path.match(/^\/homework\/\d+$/)) return '作业详情'
  if (route.path.match(/^\/checkin\/\d+$/)) return '签到详情'
  if (route.path.match(/^\/exams\/\d+$/)) return '考试详情'
  return 'Focus Mind'
})

watch(() => route.path, (newPath) => {
  selectedKeys.value = [newPath]
})

function navigate(path) {
  router.push(path)
}

function onMenuClick({ key }) {
  if (key === 'start-class') {
    openStartClassModal()
    return
  }
  if (key === '/report' && currentRole.value === 'student') {
    router.push('/my-report')
  } else {
    router.push(key)
  }
}

function handleLogout() {
  userStore.logout()
  router.push('/')
}

const showCreateModal = ref(false)
provide('showCreateModal', showCreateModal)

function openCreateModal() {
  showCreateModal.value = true
}
</script>

<style scoped>
.main-layout {
  height: 100vh;
  overflow: hidden;
}

.app-sider {
  background: var(--cv-bg-container) !important;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.06);
  z-index: 10;
  display: flex;
  flex-direction: column;
}

.app-sider :deep(.ant-layout-sider-children) {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  height: 100vh;
}

.app-sider :deep(.ant-menu) {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  border-right: none;
}

.logo-area {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  cursor: pointer;
  border-bottom: 1px solid var(--cv-border-light);
}

.logo-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: linear-gradient(135deg, #3751FE, #5566ff);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.logo-text {
  font-size: 18px;
  font-weight: 700;
  color: var(--cv-color-primary);
  white-space: nowrap;
}

.create-btn-wrap {
  padding: 12px 16px 8px;
}

.create-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 8px 12px;
  background: linear-gradient(135deg, #3751FE, #5566ff);
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.create-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(55, 81, 254, 0.3);
}

.app-menu {
  border-right: none !important;
  padding: 0 8px;
}

.app-menu :deep(.ant-menu-item) {
  border-radius: 8px;
  margin: 2px 0;
  width: 100%;
}

.app-menu :deep(.ant-menu-item-selected) {
  background: var(--cv-color-primary-bg);
  color: var(--cv-color-primary);
  font-weight: 600;
}

.app-body {
  background: #f5f6fa;
  overflow: hidden;
}

.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  background: #fff;
  height: 56px;
  line-height: 56px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
  z-index: 9;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.collapse-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: none;
  background: var(--cv-bg-page);
  border-radius: 6px;
  cursor: pointer;
  color: var(--cv-text-tertiary);
  font-size: 16px;
  transition: all 0.2s;
}

.collapse-btn:hover {
  background: var(--cv-border-light);
  color: var(--cv-color-primary);
}

.header-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a2e;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.role-badge {
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.role-teacher { background: rgba(55, 81, 254, 0.1); color: #3751FE; }
.role-student { background: rgba(34, 197, 94, 0.1); color: #16a34a; }
.role-admin { background: rgba(168, 85, 247, 0.1); color: #a855f7; }

.user-name {
  font-size: 14px;
  color: var(--cv-text-secondary);
  font-weight: 500;
}

.logout-btn {
  padding: 4px 12px;
  background: rgba(239, 68, 68, 0.08);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s;
}

.logout-btn:hover {
  background: rgba(239, 68, 68, 0.12);
}

.app-content {
  overflow-y: auto;
  overflow-x: hidden;
  padding: 0;
}

@media (max-width: 768px) {
  .app-sider {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    z-index: 100;
    box-shadow: 4px 0 16px rgba(0, 0, 0, 0.12);
  }

  .app-sider.ant-layout-sider-collapsed {
    transform: translateX(-100%);
    transition: transform 0.2s ease;
  }

  .app-body {
    width: 100%;
  }

  .header-title {
    display: none;
  }

  .header-right {
    gap: 8px;
  }

  .user-name {
    display: none;
  }
}
</style>
