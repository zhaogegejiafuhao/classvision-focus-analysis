<template>
    <div class="board-page">
        <div class="board-header">
            <div class="board-header-left">
                <h2 class="board-title">{{ pageTitle }}</h2>
                <span class="board-subtitle">Focus Mind 实时专注度量化与教学智能评估平台 / 看板视图</span>
            </div>
            <div class="board-header-right">
                <div class="search-box">
                    <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                    </svg>
                    <input
                        v-model="searchQuery"
                        type="text"
                        class="search-input"
                        :placeholder="searchPlaceholder"
                    />
                    <button v-if="isSearching" class="search-clear" @click="clearSearch">&times;</button>
                </div>
                <span v-if="isSearching" class="results-count">找到 {{ totalResults }} 个结果</span>
            </div>
        </div>

        <div v-if="loading" class="loading-state">
            <a-spin size="large" tip="加载课堂..." />
        </div>

        <!-- 统计看板 -->
        <div v-if="dashboard" class="dashboard-cards">
          <template v-if="dashboard.role === 'teacher'">
            <div class="dash-card">
              <span class="dash-value">{{ dashboard.total_classrooms }}</span>
              <span class="dash-label">总课堂</span>
            </div>
            <div class="dash-card">
              <span class="dash-value">{{ dashboard.total_students }}</span>
              <span class="dash-label">总学生</span>
            </div>
            <div class="dash-card">
              <span class="dash-value">{{ dashboard.today_classrooms }}</span>
              <span class="dash-label">今日课堂</span>
            </div>
            <div class="dash-card dash-warn" v-if="dashboard.pending_homework > 0">
              <span class="dash-value">{{ dashboard.pending_homework }}</span>
              <span class="dash-label">待批改作业</span>
            </div>
            <div class="dash-card dash-warn" v-if="dashboard.pending_exam > 0">
              <span class="dash-value">{{ dashboard.pending_exam }}</span>
              <span class="dash-label">待批改考试</span>
            </div>
            <div class="dash-card">
              <span class="dash-value">{{ dashboard.avg_attention }}</span>
              <span class="dash-label">平均注意力</span>
            </div>
          </template>
          <template v-else>
            <div class="dash-card">
              <span class="dash-value">{{ dashboard.my_classrooms }}</span>
              <span class="dash-label">我的课堂</span>
            </div>
            <div class="dash-card dash-warn" v-if="dashboard.pending_homework > 0">
              <span class="dash-value">{{ dashboard.pending_homework }}</span>
              <span class="dash-label">待提交作业</span>
            </div>
            <div class="dash-card">
              <span class="dash-value">{{ dashboard.my_exams }}</span>
              <span class="dash-label">已参加考试</span>
            </div>
            <div class="dash-card">
              <span class="dash-value">{{ dashboard.avg_attention }}</span>
              <span class="dash-label">平均注意力</span>
            </div>
          </template>
        </div>

        <div v-else-if="classrooms.length > 0" class="board-columns">
            <div
                v-for="(col, idx) in boardData"
                :key="idx"
                class="board-column"
            >
                <div class="column-header">
                    <span class="column-title">{{ boardColumns[idx] }}</span>
                    <span class="column-count">{{ col.length }}</span>
                </div>
                <div class="column-body">
                    <div
                        v-for="c in col"
                        :key="c.id"
                        class="board-card"
                        @click="navigate(`/classrooms/${c.id}`)"
                    >
                        <div class="card-main">
                            <div class="card-icon">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <rect x="3" y="3" width="18" height="18" rx="2"/>
                                </svg>
                            </div>
                            <span class="card-name" v-html="highlightedName(c.name)"></span>
                        </div>
                        <span class="card-tag">{{ cardSubLabel(c) }}</span>
                    </div>
                    <div
                        v-if="canCreate"
                        class="add-card-btn"
                        @click="openCreateModal"
                    >
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
                        </svg>
                        <span>新建课堂</span>
                    </div>
                </div>
            </div>
        </div>

        <a-empty v-else description="暂无课堂数据" style="margin: 80px 0">
          <a-button v-if="canCreate" type="primary" @click="openCreateModal">创建新课堂</a-button>
        </a-empty>

        <a-modal
            v-model:open="modalVisible"
            title="开始新课堂"
            :ok-text="creating ? '创建中...' : '创建课堂'"
            :confirm-loading="creating"
            cancel-text="取消"
            @ok="handleCreate"
        >
            <div class="create-form">
                <div class="form-group">
                    <label>课程名称 <span class="required">*</span></label>
                    <input v-model="createForm.name" type="text" class="form-input" placeholder="例如：高一(3)班 数学" />
                </div>
                <div class="form-group">
                    <label>授课教师</label>
                    <input v-model="createForm.teacher" type="text" class="form-input" placeholder="教师姓名" />
                </div>
                <div class="form-group">
                    <label>课序号</label>
                    <input v-model="createForm.course_code" type="text" class="form-input" placeholder="例如：CS101" />
                </div>
                <div class="form-group">
                    <label>公开</label>
                    <div class="mode-toggle">
                        <button
                            :class="['mode-btn', { active: createForm.is_public }]"
                            @click="createForm.is_public = true"
                        >公开</button>
                        <button
                            :class="['mode-btn', { active: !createForm.is_public }]"
                            @click="createForm.is_public = false"
                        >私有</button>
                    </div>
                </div>
            </div>
        </a-modal>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, inject, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { message } from 'ant-design-vue'
import api from '@/api'

const router = useRouter()
const userStore = useUserStore()
const classrooms = ref([])
const dashboard = ref(null)
const loading = ref(true)
const searchQuery = ref('')
const creating = ref(false)
const createForm = ref({ name: '', teacher: '', course_code: '', is_public: true })

const externalShowCreate = inject('showCreateModal', ref(false))
const modalVisible = computed({
  get: () => externalShowCreate.value,
  set: (v) => { externalShowCreate.value = v }
})

watch(externalShowCreate, (val) => {
  if (val) {
    createForm.value = { name: '', teacher: userStore.displayName || '', course_code: '', is_public: true }
  }
})

const currentRole = computed(() => userStore.role)

const searchPlaceholder = computed(() => {
  if (currentRole.value === 'student') return '搜索课堂 / 教师'
  if (currentRole.value === 'admin') return '搜索课堂 / 教师 / 学生'
  return '搜索课堂 / 学生'
})

const isSearching = computed(() => searchQuery.value.trim().length > 0)

function clearSearch() {
  searchQuery.value = ''
}

const boardData = computed(() => {
  const col0 = []
  const col1 = []
  const col2 = []

  const q = searchQuery.value.trim().toLowerCase()
  const filtered = q
    ? classrooms.value.filter(c =>
        (c.name || '').toLowerCase().includes(q) ||
        (c.teacher || '').toLowerCase().includes(q)
      )
    : classrooms.value

  for (const c of filtered) {
    if (currentRole.value === 'teacher') {
      const score = c.avg_attention || 0
      if (c.ended_at) {
        col2.push(c)
      } else if (score >= 60) {
        col0.push(c)
      } else if (score >= 30) {
        col1.push(c)
      } else {
        col2.push(c)
      }
    } else if (currentRole.value === 'student') {
      if (c.ended_at) {
        col2.push(c)
      } else if (c.started_at) {
        col0.push(c)
      } else {
        col1.push(c)
      }
    } else if (currentRole.value === 'admin') {
      if (c.ended_at) {
        col2.push(c)
      } else if ((c.total_students || 0) > 0 && (c.avg_attention || 0) >= 30) {
        col0.push(c)
      } else {
        col1.push(c)
      }
    }
  }
  return [col0, col1, col2]
})

const totalResults = computed(() =>
  boardData.value[0].length + boardData.value[1].length + boardData.value[2].length
)

const boardColumns = computed(() => {
  const config = {
    teacher: ['专注', '一般', '分心'],
    student: ['进行中', '即将开始', '已结束'],
    admin: ['活跃课堂', '需关注', '已结束'],
  }
  return config[currentRole.value] || config.teacher
})

const cardSubLabel = (c) => {
  if (currentRole.value === 'teacher') {
    if (c.ended_at) return '已结束'
    return `注意力 ${Math.round(c.avg_attention || 0)}`
  } else if (currentRole.value === 'student') {
    return c.teacher || '未知教师'
  } else {
    return `${c.total_students || 0} 人 · ${c.teacher || '未知'}`
  }
}

const pageTitle = computed(() => {
  const titles = {
    teacher: '教学看板',
    student: '学习看板',
    admin: '管理看板',
  }
  return titles[currentRole.value] || '教学看板'
})

const canCreate = computed(() => currentRole.value === 'teacher' || currentRole.value === 'admin')

function highlightText(text, query) {
  if (!query || !text) return text
  const q = query.trim()
  if (!q) return text
  const reg = new RegExp(`(${q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi')
  return text.replace(reg, '<mark class="search-highlight">$1</mark>')
}

function highlightedName(name) {
  return highlightText(name, searchQuery.value)
}

const navigate = (path) => {
  router.push(path)
}

function openCreateModal() {
  if (!canCreate.value) {
    router.push('/classrooms')
    return
  }
  createForm.value = { name: '', teacher: userStore.displayName || '', exam_mode: false, course_code: '', is_public: true }
  externalShowCreate.value = true
}

async function handleCreate() {
  if (!createForm.value.name) {
    message.warning('请输入课程名称')
    return
  }
  creating.value = true
  try {
    await api.post('/classrooms', {
      name: createForm.value.name,
      teacher: createForm.value.teacher,
      course_code: createForm.value.course_code,
      is_public: createForm.value.is_public,
    })
    message.success('课堂创建成功')
    externalShowCreate.value = false
    const res = await api.get('/classrooms')
    classrooms.value = res.data || []
  } catch (e) {
    const msg = e.response?.data?.detail || '创建失败'
    message.error(msg)
  } finally {
    creating.value = false
  }
}

onMounted(async () => {
  try {
    const [classRes, dashRes] = await Promise.all([
      api.get('/classrooms'),
      api.get('/dashboard').catch(() => ({ data: null })),
    ])
    classrooms.value = classRes.data || []
    dashboard.value = dashRes.data
  } catch (e) {
    message.error('加载课堂数据失败')
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.board-page {
    min-height: 100%;
    padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
    background: var(--cv-bg-page);
}

.dashboard-cards {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.dash-card {
  flex: 1;
  min-width: 120px;
  background: #fff;
  border-radius: 12px;
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}

.dash-card.dash-warn {
  background: #fff7e6;
  border: 1px solid #ffd591;
}

.dash-value {
  font-size: 28px;
  font-weight: 700;
  color: #1a1a2e;
  line-height: 1.2;
}

.dash-warn .dash-value {
  color: #fa8c16;
}

.dash-label {
  font-size: 13px;
  color: #64748b;
  margin-top: 4px;
}

.board-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    flex-wrap: wrap;
    gap: 12px;
}

.board-header-left {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.board-title {
    margin: 0;
    font-size: 22px;
    font-weight: 700;
    color: #1a1a2e;
}

.board-subtitle {
    font-size: 13px;
    color: #94a3b8;
}

.board-header-right {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
}

.search-box {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    min-width: 260px;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.search-box:focus-within {
    border-color: var(--cv-color-primary);
    box-shadow: 0 0 0 3px rgba(52, 97, 253, 0.1);
}

.search-icon {
    color: #94a3b8;
    flex-shrink: 0;
}

.search-input {
    border: none;
    outline: none;
    background: transparent;
    font-size: 13px;
    color: #374151;
    width: 100%;
    padding: 2px 0;
}

.search-input::placeholder {
    color: #94a3b8;
}

.search-clear {
    border: none;
    background: #cbd5e1;
    color: #64748b;
    font-size: 14px;
    cursor: pointer;
    border-radius: 50%;
    width: 18px;
    height: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    line-height: 1;
    padding: 0;
    flex-shrink: 0;
}

.search-clear:hover {
    background: #94a3b8;
    color: #fff;
}

.results-count {
    font-size: 12px;
    color: var(--cv-color-primary);
    font-weight: 600;
    white-space: nowrap;
}

.loading-state {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px;
}

.board-columns {
    display: flex;
    gap: 16px;
    align-items: flex-start;
}

.board-column {
    flex: 1;
    min-width: 260px;
    background: #eff1f5;
    border-radius: 12px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.column-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 4px 8px 8px;
    border-bottom: 1px solid #dfe3ea;
}

.column-title {
    font-size: 14px;
    font-weight: 600;
    color: #475569;
}

.column-count {
    font-size: 12px;
    font-weight: 600;
    color: #64748b;
    background: #fff;
    padding: 2px 8px;
    border-radius: 10px;
}

.column-body {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding-top: 4px;
}

.board-card {
    display: flex;
    flex-direction: column;
    gap: 6px;
    padding: 12px;
    background: #ffffff;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    cursor: pointer;
    transition: all 0.15s ease;
}

.board-card:hover {
    border-color: rgba(52, 97, 253, 0.4);
    box-shadow: 0 2px 8px rgba(52, 97, 253, 0.1);
    transform: translateY(-1px);
}

.card-main {
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    border-radius: 6px;
    background: rgba(52, 97, 253, 0.08);
    color: var(--cv-color-primary);
    flex-shrink: 0;
}

.card-name {
    font-size: 13px;
    font-weight: 600;
    color: #1e293b;
    line-height: 1.3;
    word-break: break-all;
}

.card-tag {
    display: inline-block;
    font-size: 11px;
    color: #64748b;
    background: #f1f5f9;
    padding: 2px 8px;
    border-radius: 4px;
    width: fit-content;
}

.add-card-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 10px;
    border: 1px dashed #cbd5e1;
    border-radius: 8px;
    background: transparent;
    color: #64748b;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.15s ease;
}

.add-card-btn:hover {
    border-color: var(--cv-color-primary);
    color: var(--cv-color-primary);
    background: rgba(52, 97, 253, 0.04);
}

.search-highlight {
    background: rgba(250, 204, 21, 0.3);
    color: inherit;
    padding: 0 2px;
    border-radius: 2px;
}

.create-form {
    padding-top: 8px;
}

.form-group {
    margin-bottom: 16px;
}

.form-group label {
    display: block;
    font-size: 13px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 6px;
}

.required {
    color: #ef4444;
}

.form-input {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 14px;
    color: #1e293b;
    outline: none;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
    box-sizing: border-box;
}

.form-input:focus {
    border-color: var(--cv-color-primary);
    box-shadow: 0 0 0 3px rgba(52, 97, 253, 0.1);
}

.mode-toggle {
    display: flex;
    gap: 8px;
}

.mode-btn {
    flex: 1;
    padding: 8px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    background: #ffffff;
    font-size: 13px;
    color: #475569;
    cursor: pointer;
    transition: all 0.15s ease;
}

.mode-btn.active {
    border-color: var(--cv-color-primary);
    background: rgba(52, 97, 253, 0.08);
    color: var(--cv-color-primary);
    font-weight: 600;
}

@media (max-width: 1024px) {
    .board-columns {
        flex-direction: column;
    }

    .board-column {
        width: 100%;
    }
}

@media (max-width: 640px) {
    .board-page {
        padding: 16px;
    }

    .search-box {
        min-width: 100%;
    }

    .board-header {
        flex-direction: column;
        align-items: stretch;
    }
}
</style>
