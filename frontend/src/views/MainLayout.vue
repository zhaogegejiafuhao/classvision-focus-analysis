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
        <span class="logo-icon">CE</span>
        <span v-if="!collapsed" class="logo-text">ClassEyes</span>
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

        <a-menu-item key="/classrooms">
          <template #icon><BookOutlined /></template>
          <span>{{ currentRole === 'student' ? '我的课堂' : '课堂管理' }}</span>
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
  </a-layout>
</template>

<script setup>
import { ref, computed, watch, provide, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'

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
} from '@ant-design/icons-vue'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const collapsed = ref(false)
const selectedKeys = ref([route.path])

function checkScreenWidth() {
  if (window.innerWidth <= 1024 && window.innerWidth > 768) {
    collapsed.value = true
  }
}
onMounted(() => {
  checkScreenWidth()
  window.addEventListener('resize', checkScreenWidth)
})
onUnmounted(() => {
  window.removeEventListener('resize', checkScreenWidth)
})

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
  }
  if (titles[route.path]) return titles[route.path]
  if (route.path.startsWith('/oj/') && !route.path.startsWith('/oj/run') && !route.path.startsWith('/oj/submissions')) {
    return '题目详情'
  }
  return 'ClassEyes'
})

watch(() => route.path, (newPath) => {
  selectedKeys.value = [newPath]
})

function navigate(path) {
  router.push(path)
}

function onMenuClick({ key }) {
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
