import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // 落地页（登录前的平台信息展示页，设为首页）
  { path: '/', name: 'landing', component: () => import('@/views/Landing.vue'), meta: { public: true } },
  // 登录页
  { path: '/login', name: 'login', component: () => import('@/views/Login.vue'), meta: { public: true } },
  // 主应用（共享布局：侧边栏 + 顶栏 + 内容区）
  {
    path: '/app',
    component: () => import('@/views/MainLayout.vue'),
    children: [
      { path: '', name: 'home-app', component: () => import('@/views/Frame04.vue') },
      { path: '/classrooms', name: 'classrooms', component: () => import('@/views/ClassroomList.vue') },
      { path: '/classrooms/:id', name: 'classroom-detail', component: () => import('@/views/ClassroomDetail.vue') },
      { path: '/persons', name: 'persons', component: () => import('@/views/PersonsPage.vue') },
      { path: '/rag', name: 'rag', component: () => import('@/views/RagPage.vue') },
      { path: '/calendar', name: 'calendar', component: () => import('@/views/Frame27219.vue') },
      { path: '/settings', name: 'settings', component: () => import('@/views/Frame282357.vue') },
      { path: '/help', name: 'help', component: () => import('@/views/Frame17448.vue') },
      { path: '/analytics', name: 'analytics', component: () => import('@/views/Frame293293.vue') },
      { path: '/report', name: 'report', component: () => import('@/views/Frame293744.vue') },
      { path: '/oj', name: 'oj-list', component: () => import('@/views/OjProblemList.vue') },
      { path: '/oj/run', name: 'oj-run', component: () => import('@/views/Frame281780.vue') },
      { path: '/oj/submissions', name: 'oj-submissions', component: () => import('@/views/OjSubmissions.vue') },
      { path: '/oj/:id', name: 'oj-detail', component: () => import('@/views/OjProblemDetail.vue') },
      { path: '/invite', name: 'invite', component: () => import('@/views/Frame281518.vue') },
    ]
  },
  // 独立页面（不需要侧边栏）
  { path: '/home', redirect: '/app' },
  { path: '/live/:id', name: 'live', component: () => import('@/views/LivePage.vue') },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  // 未登录访问受保护页面 -> 跳转登录页
  if (!to.meta.public && !token) {
    next('/login')
  // 已登录访问落地页或登录页 -> 跳转主页
  } else if (token && (to.path === '/' || to.path === '/login')) {
    next('/app')
  } else {
    next()
  }
})

export default router
