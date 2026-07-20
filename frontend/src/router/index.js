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
      { path: '/join-class', name: 'join-class', component: () => import('@/views/JoinClassPage.vue') },
      { path: '/classrooms/:id', name: 'classroom-detail', component: () => import('@/views/ClassroomDetail.vue') },
      { path: '/persons', name: 'persons', component: () => import('@/views/PersonsPage.vue') },
      { path: '/roster', name: 'roster', component: () => import('@/views/RosterPage.vue') },
      { path: '/rag', name: 'rag', component: () => import('@/views/RagPage.vue') },
      { path: '/calendar', name: 'calendar', component: () => import('@/views/Frame27219.vue') },
      { path: '/settings', name: 'settings', component: () => import('@/views/Frame282357.vue') },
      { path: '/help', name: 'help', component: () => import('@/views/Frame17448.vue') },
      { path: '/analytics', name: 'analytics', component: () => import('@/views/Frame293293.vue') },
      { path: '/report', name: 'report', component: () => import('@/views/Frame293744.vue') },
      { path: '/my-report', name: 'my-report', component: () => import('@/views/StudentReport.vue') },
      { path: '/oj', name: 'oj-list', component: () => import('@/views/OjProblemList.vue') },
      { path: '/oj/run', name: 'oj-run', component: () => import('@/views/Frame281780.vue') },
      { path: '/oj/submissions', name: 'oj-submissions', component: () => import('@/views/OjSubmissions.vue') },
      { path: '/oj/:id', name: 'oj-detail', component: () => import('@/views/OjProblemDetail.vue') },
      { path: '/notifications', name: 'notifications', component: () => import('@/views/NotificationPage.vue') },
      { path: '/homework', name: 'homework', component: () => import('@/views/HomeworkPage.vue') },
      { path: '/homework/:id', name: 'homework-detail', component: () => import('@/views/HomeworkDetail.vue') },
      { path: '/checkin', name: 'checkin', component: () => import('@/views/CheckinPage.vue') },
      { path: '/checkin/:id', name: 'checkin-detail', component: () => import('@/views/CheckinDetail.vue') },
      { path: '/exams', name: 'exams', component: () => import('@/views/ExamPage.vue') },
      { path: '/exams/:id', name: 'exam-detail', component: () => import('@/views/ExamDetail.vue') },
      { path: '/student/homework', name: 'student-homework', component: () => import('@/views/StudentHomework.vue') },
      { path: '/student/checkin', name: 'student-checkin', component: () => import('@/views/StudentCheckin.vue') },
      { path: '/student/exams', name: 'student-exams', component: () => import('@/views/StudentExam.vue') },
      { path: '/student/materials', name: 'student-materials', component: () => import('@/views/StudentMaterial.vue') },
      { path: '/student/grades', name: 'student-grades', component: () => import('@/views/StudentGrade.vue') },
      { path: '/alerts', name: 'alerts', component: () => import('@/views/AlertPage.vue') },
      { path: '/teaching-plans', name: 'teaching-plans', component: () => import('@/views/TeachingPlanPage.vue') },
      { path: '/question-bank', name: 'question-bank', component: () => import('@/views/QuestionBankPage.vue') },
      { path: '/materials', name: 'materials', component: () => import('@/views/MaterialPage.vue') },
      { path: '/grades', name: 'grades', component: () => import('@/views/GradeReportPage.vue') },
      { path: '/leaves', name: 'leaves', component: () => import('@/views/LeavePage.vue') },
      { path: '/experiments', name: 'experiments', component: () => import('@/views/ExperimentList.vue') },
      { path: '/experiments/:id', name: 'experiment-detail', component: () => import('@/views/ExperimentDetail.vue') },
      { path: '/behavior', name: 'behavior', component: () => import('@/views/StudentBehavior.vue') },
      // AI智能批改
      { path: '/ai-grading', name: 'ai-grading', component: () => import('@/views/AIGradingPage.vue') },
      { path: '/ai-essay-grading', name: 'ai-essay-grading', component: () => import('@/views/AIEssayGradingPage.vue') },
      { path: '/student/grading', name: 'student-grading', component: () => import('@/views/StudentGradingPage.vue') },
      { path: '/correction', name: 'correction', component: () => import('@/views/CorrectionPage.vue') },
      { path: '/knowledge-analysis', name: 'knowledge-analysis', component: () => import('@/views/KnowledgeAnalysisPage.vue') },
      { path: '/similar-questions', name: 'similar-questions', component: () => import('@/views/SimilarQuestionsPage.vue') },
      { path: '/answer-sheet', name: 'answer-sheet', component: () => import('@/views/AnswerSheetPage.vue') },
      { path: '/mistake-book', name: 'mistake-book', component: () => import('@/views/MistakeBookPage.vue') },
      { path: '/mistake-book/:id', name: 'mistake-detail', component: () => import('@/views/MistakeDetailPage.vue') },
      { path: '/my-similar-questions', name: 'my-similar-questions', component: () => import('@/views/SimilarQuestionListPage.vue') },
      { path: '/my-similar-questions/:id', name: 'similar-question-practice', component: () => import('@/views/SimilarQuestionPracticePage.vue') },
      { path: '/homework/extensions', name: 'homework-extensions', component: () => import('@/views/HomeworkPage.vue'), meta: { defaultTab: 'extensions' } },
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
