/**
 * 课堂详情页业务逻辑 Composable
 *
 * 从 ClassroomDetail.vue 抽取，包含：
 * - 课堂操作（结束、删除、编辑）
 * - 学生管理（增删改）
 * - 报告生成与删除
 * - 数据加载（时间线、热力图、出席、考试风险）
 * - 流式聊天对话
 */
import { ref, computed, onMounted, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import * as echarts from 'echarts'
import { message } from 'ant-design-vue'
import MarkdownIt from 'markdown-it'
import { listPersons } from '@/api/person'
import { listHomework } from '@/api/homework'
import { listExams } from '@/api/exam'
import { listCheckinSessions } from '@/api/checkin'
import { listMaterials } from '@/api/material'
import {
  endClassroom, deleteClassroom, updateClassroom,
  getClassroom, getChatHistory, exportChat,
} from '@/api/classroom'
import {
  getClassroomTimeline, getClassroomHeatmap, getClassroomAttendance,
  listClassroomStudents, addClassroomStudent, updateClassroomStudent,
  removeClassroomStudent, generateClassroomReport, getClassroomReport,
  deleteClassroomReport, getClassroomExamRisks,
} from '@/api/stats'

export function useClassroomDetail() {
  const md = new MarkdownIt({ html: false, breaks: true, linkify: true })

  const route = useRoute()
  const router = useRouter()
  const userStore = useUserStore()
  const classroomId = route.params.id

  const canManage = computed(() => ['teacher', 'admin'].includes(userStore.role))
  const canEditOrDelete = computed(() => {
    if (!classroom.value) return false
    if (userStore.role === 'admin') return true
    return classroom.value.teacher_person_id === userStore.user?.id
  })

  // ── 核心数据 ──
  const classroom = ref(null)
  const students = ref([])
  const report = ref(null)
  const loading = ref(true)
  const genLoading = ref(false)
  const endLoading = ref(false)

  // ── DOM 引用（图表挂载点）──
  const timelineEl = ref(null)
  const riskChartEl = ref(null)
  const riskTimelineEl = ref(null)
  const heatmapEl = ref(null)

  // ── 考试风险记录 ──
  const examRisks = ref([])
  const riskLoading = ref(false)
  const riskFilter = ref(undefined)
  const riskColumns = [
    { title: '学生', dataIndex: 'student_name', key: 'student_name', width: 100 },
    { title: '风险等级', key: 'risk_level', width: 100 },
    { title: '视线偏移时长', key: 'gaze_deviation_duration', width: 120 },
    { title: '低头时长', key: 'head_down_duration', width: 100 },
    { title: '转头次数', dataIndex: 'head_turn_events', key: 'head_turn_events', width: 100 },
    { title: '作弊物品', key: 'cheating_object_nearby', width: 100 },
    { title: '注意力', dataIndex: 'attention_score', key: 'attention_score', width: 80 },
    { title: '时间', key: 'timestamp', width: 180 },
  ]

  // ── 教学模块 Tab ──
  const teachingTab = ref('homework')
  const classHomeworks = ref([])
  const classExams = ref([])
  const classCheckins = ref([])
  const hwLoading = ref(false)
  const examLoading = ref(false)
  const checkinLoading = ref(false)
  const classMaterials = ref([])
  const materialLoading = ref(false)

  const hwColumns = [
    { key: 'title', title: '标题', dataIndex: 'title' },
    { key: 'status', title: '状态' },
    { key: 'submission_count', title: '提交数', dataIndex: 'submission_count' },
    { key: 'action', title: '操作' },
  ]
  const examColumns = [
    { key: 'title', title: '标题', dataIndex: 'title' },
    { key: 'status', title: '状态' },
    { key: 'question_count', title: '题目数', dataIndex: 'question_count' },
    { key: 'action', title: '操作' },
  ]
  const checkinColumns = [
    { key: 'type', title: '类型', dataIndex: 'type' },
    { key: 'status', title: '状态' },
    { key: 'checked_count', title: '已签到', dataIndex: 'checked_count' },
    { key: 'action', title: '操作' },
  ]

  async function loadTeachingData() {
    if (!canManage.value) return
    hwLoading.value = true
    examLoading.value = true
    checkinLoading.value = true
    materialLoading.value = true
    try {
      const [hwRes, examRes, checkinRes, matRes] = await Promise.all([
        listHomework({ classroom_id: classroomId }, { _skipGlobalError: true }).catch(() => ({ data: [] })),
        listExams({ classroom_id: classroomId }, { _skipGlobalError: true }).catch(() => ({ data: [] })),
        listCheckinSessions({ classroom_id: classroomId }, { _skipGlobalError: true }).catch(() => ({ data: [] })),
        listMaterials({ classroom_id: classroomId }, { _skipGlobalError: true }).catch(() => ({ data: [] })),
      ])
      classHomeworks.value = hwRes.data
      classExams.value = examRes.data
      classCheckins.value = checkinRes.data
      classMaterials.value = matRes.data
    } catch {
      // ignore
    } finally {
      hwLoading.value = false
      examLoading.value = false
      checkinLoading.value = false
      materialLoading.value = false
    }
  }

  const highRiskSummary = computed(() => {
    if (!examRisks.value.length) return []
    const map = {}
    for (const r of examRisks.value) {
      if (!map[r.student_id]) {
        map[r.student_id] = {
          student_id: r.student_id,
          student_name: r.student_name,
          total_events: 0,
          total_gaze: 0,
          total_head_down: 0,
          total_head_turn: 0,
          has_cheating_object: false,
          risk_level: 'low',
        }
      }
      const item = map[r.student_id]
      item.total_events += 1
      item.total_gaze += r.gaze_deviation_duration || 0
      item.total_head_down += r.head_down_duration || 0
      item.total_head_turn += r.head_turn_events || 0
      if (r.cheating_object_nearby) item.has_cheating_object = true
      if (r.risk_level === 'high' || (r.risk_level === 'medium' && item.risk_level !== 'high')) {
        item.risk_level = r.risk_level
      }
    }
    return Object.values(map)
      .filter(m => m.total_events > 0 && (m.risk_level === 'high' || m.risk_level === 'medium' || m.has_cheating_object))
      .sort((a, b) => b.total_events - a.total_events)
  })

  // ── 出席情况 ──
  const attendance = ref({
    identified_count: 0,
    unidentified_count: 0,
    absent_count: 0,
    identified: [],
    unidentified: [],
    absent: [],
  })
  const showAttendanceModal = ref(false)

  // ── 对话相关 ──
  const chatMessages = ref([])
  const chatInput = ref('')
  const chatLoading = ref(false)
  const chatContainerRef = ref(null)
  const chatMode = ref('fast')

  function scrollChatToBottom() {
    nextTick(() => {
      const el = chatContainerRef.value
      if (el) el.scrollTop = el.scrollHeight
    })
  }

  const studentCols = computed(() => {
    const base = [
      { title: '姓名', dataIndex: 'name', key: 'name' },
      { title: '平均注意力', dataIndex: 'avg_attention', key: 'avg_attention' },
      { title: '低头人次', dataIndex: 'head_down_count', key: 'head_down_count' },
      { title: '眨眼次数', dataIndex: 'blink_count', key: 'blink_count' },
    ]
    if (canManage.value) {
      base.push({ title: '操作', key: 'action' })
    }
    return base
  })

  function renderMarkdown(text) {
    if (!text || typeof text !== 'string') return ''
    return md.render(text)
  }

  function formatFileSize(bytes) {
    if (!bytes) return '0B'
    if (bytes < 1024) return bytes + 'B'
    if (bytes < 1048576) return (bytes / 1024).toFixed(1) + 'KB'
    return (bytes / 1048576).toFixed(1) + 'MB'
  }

  function downloadMaterial(record) {
    window.open(`/api/materials/${record.id}/download`, '_blank')
  }

  // ===== 课堂操作 =====
  async function handleEndClassroom() {
    endLoading.value = true
    try {
      await endClassroom(classroomId)
      message.success('课堂已结束')
      await loadClassroom()
    } catch (e) {
      message.error(e.response?.data?.detail || '结束课堂失败')
    } finally {
      endLoading.value = false
    }
  }

  async function handleDeleteClassroom() {
    try {
      await deleteClassroom(classroomId)
      message.success('课堂已删除')
      router.push('/classrooms')
    } catch (e) {
      message.error(e.response?.data?.detail || '删除课堂失败')
    }
  }

  const editClassroomOpen = ref(false)
  const editClassroomSaving = ref(false)
  const editClassroomForm = ref({ name: '', teacher: '', course_code: '', is_public: true })

  function openEditClassroom() {
    editClassroomForm.value = {
      name: classroom.value.name || '',
      teacher: classroom.value.teacher || '',
      course_code: classroom.value.course_code || '',
      is_public: classroom.value.is_public !== false,
    }
    editClassroomOpen.value = true
  }

  async function handleEditClassroom() {
    editClassroomSaving.value = true
    try {
      await updateClassroom(classroomId, editClassroomForm.value)
      message.success('课堂信息已更新')
      editClassroomOpen.value = false
      await loadClassroom()
    } catch (e) {
      message.error(e.response?.data?.detail || '更新失败')
    } finally {
      editClassroomSaving.value = false
    }
  }

  // ===== 学生管理 =====
  const addStudentOpen = ref(false)
  const addStudentSaving = ref(false)
  const addStudentForm = ref({ track_id: 1, name: '', person_id: null })
  const availablePersons = ref([])

  function filterPerson(input, option) {
    const label = option.children?.[0]?.children?.[0] || ''
    return label.toLowerCase().includes(input.toLowerCase())
  }

  function openAddStudent() {
    const maxTrackId = students.value.length > 0
      ? Math.max(...students.value.map(s => s.track_id || 0)) + 1
      : 1
    addStudentForm.value = { track_id: maxTrackId, name: '', person_id: null }
    addStudentOpen.value = true
    loadAvailablePersons()
  }

  async function loadAvailablePersons() {
    try {
      const res = await listPersons({ role: 'student' })
      const existingPersonIds = new Set(students.value.map(s => s.person_id).filter(Boolean))
      availablePersons.value = (res.data || []).filter(p => !existingPersonIds.has(p.id))
    } catch {
      availablePersons.value = []
    }
  }

  async function handleAddStudent() {
    addStudentSaving.value = true
    try {
      const payload = {
        classroom_id: Number(classroomId),
        track_id: addStudentForm.value.track_id,
        name: addStudentForm.value.name || null,
      }
      if (addStudentForm.value.person_id) {
        payload.person_id = addStudentForm.value.person_id
        const person = availablePersons.value.find(p => p.id === addStudentForm.value.person_id)
        if (person && !payload.name) payload.name = person.name
      }
      await addClassroomStudent(classroomId, payload)
      message.success('学生已添加')
      addStudentOpen.value = false
      await loadStudents()
    } catch (e) {
      message.error(e.response?.data?.detail || '添加学生失败')
    } finally {
      addStudentSaving.value = false
    }
  }

  const editStudentOpen = ref(false)
  const editStudentSaving = ref(false)
  const editStudentForm = ref({ id: null, name: '' })

  function openEditStudent(record) {
    editStudentForm.value = { id: record.id, name: record.name || '' }
    editStudentOpen.value = true
  }

  async function handleEditStudent() {
    editStudentSaving.value = true
    try {
      await updateClassroomStudent(classroomId, editStudentForm.value.id, {
        name: editStudentForm.value.name,
      })
      message.success('学生信息已更新')
      editStudentOpen.value = false
      await loadStudents()
    } catch (e) {
      message.error(e.response?.data?.detail || '更新学生失败')
    } finally {
      editStudentSaving.value = false
    }
  }

  async function deleteStudent(studentId) {
    try {
      await removeClassroomStudent(classroomId, studentId)
      message.success('学生已删除')
      await loadStudents()
    } catch (e) {
      message.error(e.response?.data?.detail || '删除学生失败')
    }
  }

  // ===== 报告操作 =====
  async function genReport(force = false) {
    genLoading.value = true
    try {
      const res = await generateClassroomReport(classroomId, { force })
      report.value = res.data
      message.success(force ? '报告已重新生成' : '报告生成成功')
    } catch (e) {
      message.error(e.response?.data?.detail || '报告生成失败')
    } finally {
      genLoading.value = false
    }
  }

  async function deleteReport() {
    try {
      await deleteClassroomReport(classroomId)
      report.value = null
      message.success('报告已删除')
    } catch (e) {
      message.error(e.response?.data?.detail || '删除报告失败')
    }
  }

  // ===== 数据加载 =====
  async function loadClassroom() {
    try {
      const res = await getClassroom(classroomId)
      classroom.value = res.data
    } catch (e) {
      message.error('加载课堂信息失败')
    }
  }

  async function loadStudents() {
    try {
      const res = await listClassroomStudents(classroomId)
      students.value = res.data
    } catch (e) {
      message.error('加载学生列表失败')
    }
  }

  async function loadChatHistory() {
    try {
      const res = await getChatHistory(classroomId)
      chatMessages.value = res.data || []
      scrollChatToBottom()
    } catch {
      chatMessages.value = []
    }
  }

  async function loadAttendance() {
    try {
      const res = await getClassroomAttendance(classroomId)
      attendance.value = res.data
    } catch {
      // 忽略
    }
  }

  async function loadExamRisks() {
    if (!classroom.value?.exam_mode) return
    riskLoading.value = true
    try {
      const params = {}
      if (riskFilter.value) params.risk_level = riskFilter.value
      const res = await getClassroomExamRisks(classroomId, params)
      examRisks.value = res.data || []
    } catch {
      examRisks.value = []
    } finally {
      riskLoading.value = false
    }
  }

  async function loadHeatmap() {
    try {
      const res = await getClassroomHeatmap(classroomId)
      if (res.data.time_labels.length === 0) return

      const chart = echarts.init(heatmapEl.value)
      const heatmapSeriesData = []
      res.data.heatmap_data.forEach((row, yIndex) => {
        row.data.forEach((value, xIndex) => {
          heatmapSeriesData.push([xIndex, yIndex, value])
        })
      })

      chart.setOption({
        tooltip: {
          position: 'top',
          formatter: (params) => {
            const student = res.data.heatmap_data[params.data[1]]
            const time = res.data.time_labels[params.data[0]]
            return `${student.student_name}<br/>时间: ${time}<br/>注意力: ${params.data[2]}`
          },
        },
        grid: { top: 50, bottom: 30, left: 100, right: 20 },
        xAxis: {
          type: 'category',
          data: res.data.time_labels,
          splitArea: { show: true },
        },
        yAxis: {
          type: 'category',
          data: res.data.heatmap_data.map(d => d.student_name),
          splitArea: { show: true },
        },
        visualMap: {
          min: 0, max: 100, calculable: true,
          orient: 'horizontal', left: 'center', bottom: 0,
          inRange: { color: ['#cf1322', '#faad14', '#52c41a'] },
        },
        series: [{
          type: 'heatmap',
          data: heatmapSeriesData,
          label: { show: false },
          emphasis: { itemStyle: { shadowBlur: 10, shadowColor: 'rgba(0, 0, 0, 0.5)' } },
        }],
      })
    } catch {
      // 忽略
    }
  }

  async function sendChat(retryText) {
    const userText = retryText || chatInput.value.trim()
    if (!userText) return
    if (!retryText) chatInput.value = ''

    chatMessages.value.push({
      id: 'tmp-user-' + Date.now(),
      role: 'user',
      content: userText,
      timestamp: new Date().toISOString(),
    })
    chatMessages.value.push({
      id: 'tmp-ai-' + Date.now(),
      role: 'assistant',
      content: '',
      timestamp: new Date().toISOString(),
      streaming: true,
      loadingStage: chatMode.value === 'deep' ? '正在检索知识库...' : 'AI 正在思考...',
    })
    const aiIdx = chatMessages.value.length - 1
    chatLoading.value = true
    scrollChatToBottom()
    const t0 = Date.now()
    let receivedDone = false

    const stageTimer = setInterval(() => {
      const elapsed = (Date.now() - t0) / 1000
      const msg = chatMessages.value[aiIdx]
      if (!msg.streaming) return
      if (msg.content) {
        msg.loadingStage = ''
      } else if (chatMode.value === 'deep') {
        if (elapsed > 30) msg.loadingStage = '正在生成回答...'
        else if (elapsed > 15) msg.loadingStage = '正在深度检索知识库...'
      } else {
        if (elapsed > 20) msg.loadingStage = '正在生成回答...'
      }
    }, 5000)

    try {
      const token = userStore.token || localStorage.getItem('token') || ''
      const resp = await fetch(`/api/classrooms/${classroomId}/chat/stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ content: userText, mode: chatMode.value }),
      })
      if (!resp.ok) throw new Error('HTTP ' + resp.status)
      const reader = resp.body.getReader()
      const decoder = new TextDecoder()
      let buffer = ''
      while (true) {
        const { done, value } = await reader.read()
        if (done) break
        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split('\n')
        buffer = lines.pop()
        for (const line of lines) {
          if (!line.startsWith('data: ')) continue
          let data
          try { data = JSON.parse(line.slice(6)) } catch { continue }
          if (data.delta) {
            chatMessages.value[aiIdx].content += data.delta
            chatMessages.value[aiIdx].loadingStage = ''
            scrollChatToBottom()
          }
          if (data.done) {
            receivedDone = true
            const elapsed = ((Date.now() - t0) / 1000).toFixed(1)
            chatMessages.value[aiIdx].id = data.id
            chatMessages.value[aiIdx].streaming = false
            chatMessages.value[aiIdx].elapsed = `耗时 ${elapsed}s`
            scrollChatToBottom()
          }
          if (data.error) {
            receivedDone = true
            chatMessages.value[aiIdx].content = '[生成失败: ' + data.error + ']'
            chatMessages.value[aiIdx].streaming = false
            chatMessages.value[aiIdx].error = true
          }
        }
      }
      if (!receivedDone) {
        chatMessages.value[aiIdx].content = chatMessages.value[aiIdx].content || '[连接中断，请点击重试]'
        chatMessages.value[aiIdx].streaming = false
        chatMessages.value[aiIdx].error = true
        message.warning('连接中断，可点击重试')
      }
    } catch (e) {
      chatMessages.value[aiIdx].content = '[请求失败: ' + e.message + ']'
      chatMessages.value[aiIdx].streaming = false
      chatMessages.value[aiIdx].error = true
      message.error('对话请求失败，可点击重试')
    } finally {
      clearInterval(stageTimer)
      chatLoading.value = false
    }
  }

  function retryChat(msg) {
    const userMsgs = chatMessages.value.filter(m => m.role === 'user')
    const lastUserMsg = userMsgs[userMsgs.length - 1]
    if (!lastUserMsg) return
    const idx = chatMessages.value.indexOf(msg)
    if (idx >= 0) chatMessages.value.splice(idx, 1)
    sendChat(lastUserMsg.content)
  }

  async function downloadMarkdown() {
    try {
      const res = await exportChat(classroomId)
      const blob = new Blob([res.data], { type: 'text/markdown' })
      const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `${classroom.value?.name || '课堂'}_完整分析报告.md`
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
    } catch (e) {
      message.error('下载报告失败')
    }
  }

  // ===== 初始化 =====
  onMounted(async () => {
    try {
      const [classRes, studentRes, timelineRes] = await Promise.all([
        getClassroom(classroomId),
        listClassroomStudents(classroomId),
        getClassroomTimeline(classroomId),
      ])
      classroom.value = classRes.data
      students.value = studentRes.data

      await nextTick()

      const chart = echarts.init(timelineEl.value)
      chart.setOption({
        grid: { top: 20, bottom: 30, left: 50, right: 20 },
        xAxis: { type: 'category', data: timelineRes.data.map(d => d.timestamp) },
        yAxis: { type: 'value', max: 100, min: 0, name: '注意力' },
        series: [{
          type: 'line', data: timelineRes.data.map(d => d.avg_attention),
          smooth: true, areaStyle: { opacity: 0.2 }, itemStyle: { color: '#1890ff' },
        }],
      })

      await loadHeatmap()
      await loadAttendance()
      await loadTeachingData()

      try {
        const reportRes = await getClassroomReport(classroomId)
        report.value = reportRes.data
      } catch { /* 报告未生成，静默忽略 */ }

      await loadChatHistory()
    } catch (e) {
      message.error('加载课堂数据失败')
    } finally {
      loading.value = false
    }
  })

  return {
    // 核心数据
    classroomId, classroom, students, report, loading,
    canManage, canEditOrDelete,
    // DOM 引用
    timelineEl, riskChartEl, riskTimelineEl, heatmapEl, chatContainerRef,
    // 考试风险
    examRisks, riskLoading, riskFilter, riskColumns, highRiskSummary, loadExamRisks,
    // 教学模块
    teachingTab, classHomeworks, classExams, classCheckins,
    hwLoading, examLoading, checkinLoading,
    classMaterials, materialLoading,
    hwColumns, examColumns, checkinColumns, loadTeachingData,
    // 出席情况
    attendance, showAttendanceModal,
    // 对话
    chatMessages, chatInput, chatLoading, chatMode,
    scrollChatToBottom, sendChat, retryChat, downloadMarkdown,
    // 学生表格
    studentCols,
    // 工具函数
    renderMarkdown, formatFileSize, downloadMaterial,
    // 课堂操作
    endLoading, handleEndClassroom, handleDeleteClassroom,
    editClassroomOpen, editClassroomSaving, editClassroomForm,
    openEditClassroom, handleEditClassroom,
    // 学生管理
    addStudentOpen, addStudentSaving, addStudentForm, availablePersons,
    filterPerson, openAddStudent, handleAddStudent,
    editStudentOpen, editStudentSaving, editStudentForm,
    openEditStudent, handleEditStudent, deleteStudent,
    // 报告
    genLoading, genReport, deleteReport,
    // 数据加载
    loadClassroom, loadStudents, loadChatHistory, loadAttendance, loadHeatmap,
  }
}
