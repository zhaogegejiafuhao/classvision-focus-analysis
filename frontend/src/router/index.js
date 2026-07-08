import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('../views/HomePage.vue') },
  { path: '/live/:id', name: 'live', component: () => import('../views/LivePage.vue') },
  { path: '/classrooms', name: 'classrooms', component: () => import('../views/ClassroomList.vue') },
  { path: '/classrooms/:id', name: 'classroom-detail', component: () => import('../views/ClassroomDetail.vue') },
  { path: '/persons', name: 'persons', component: () => import('../views/PersonsPage.vue') },
  { path: '/rag', name: 'rag', component: () => import('../views/RagPage.vue') },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
