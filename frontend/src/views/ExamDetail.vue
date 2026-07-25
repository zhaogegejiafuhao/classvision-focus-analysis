<template>
  <div class="cv-page">
    <a-page-header :title="exam?.title || '考试详情'" @back="() => $router.push('/exams')">
      <template #subTitle>
        <a-tag v-if="exam" :color="getStatusColor(exam.status)">{{ getStatusText(exam.status) }}</a-tag>
        <a-tag v-if="exam" :color="exam.exam_type === 'paper' ? '#722ed1' : '#1890ff'">
          {{ exam.exam_type === 'paper' ? '📝 笔试' : '💻 机试' }}
        </a-tag>
      </template>
      <template #extra>
        <a-space>
          <a-button @click="exportPaper">导出试卷</a-button>
          <a-popconfirm v-if="exam?.status === 'draft'" title="确定发布考试？" @confirm="handlePublishExam">
            <a-button type="primary">发布考试</a-button>
          </a-popconfirm>
          <a-popconfirm v-if="exam?.status === 'published'" title="确定关闭考试？学生将无法继续提交。" @confirm="handleCloseExam">
            <a-button danger>关闭考试</a-button>
          </a-popconfirm>
          <a-button v-if="exam?.status !== 'draft' && hasSubjectiveQuestions" type="primary" @click="goToReview" ghost>
            <template #icon><RobotOutlined /></template>
            AI 审核
          </a-button>
          <a-button v-if="exam?.status !== 'draft'" @click="exportCSV">导出成绩</a-button>
        </a-space>
      </template>
    </a-page-header>

    <a-spin :spinning="loading">
      <a-row :gutter="16">
        <!-- 左侧：考试信息 -->
        <a-col :span="8">
          <a-card title="考试信息" size="small">
	            <p><strong>考试类型：</strong>
	              <a-tag :color="exam?.exam_type === 'paper' ? '#722ed1' : '#1890ff'">
	                {{ exam?.exam_type === 'paper' ? '📝 笔试' : '💻 机试' }}
	              </a-tag>
	            </p>
	            <p><strong>考试时长：</strong>{{ exam?.duration }}分钟</p>
	            <p><strong>总分：</strong>{{ exam?.total_score }}分</p>
	            <p><strong>题目数：</strong>{{ exam?.question_count }}题</p>
	            <p><strong>课堂：</strong>{{ exam?.classroom_name || '未指定' }}</p>
	          </a-card>

          <a-card title="添加题目" size="small" style="margin-top: 16px">
            <a-form :label-col="{ span: 6 }" size="small">
              <a-form-item label="题型">
                <a-select v-model:value="questionForm.type" style="width: 100%">
                  <a-select-option value="single">单选题</a-select-option>
                  <a-select-option value="multi">多选题</a-select-option>
                  <a-select-option value="judge">判断题</a-select-option>
                  <a-select-option value="fill">填空题</a-select-option>
                  <a-select-option value="essay">简答题</a-select-option>
                </a-select>
              </a-form-item>
              <a-form-item label="题目内容">
                <a-textarea v-model:value="questionForm.content" :rows="3" />
              </a-form-item>
              <a-form-item v-if="questionForm.type === 'single' || questionForm.type === 'multi'" label="选项">
                <div v-for="(opt, i) in questionForm.options" :key="i" style="margin-bottom: 8px">
                  <a-input v-model:value="questionForm.options[i]" :placeholder="`选项${i + 1}`" style="width: 85%" />
                  <a-button type="link" danger size="small" @click="questionForm.options.splice(i, 1)">删除</a-button>
                </div>
                <a-button type="dashed" size="small" @click="questionForm.options.push('')">添加选项</a-button>
              </a-form-item>
              <a-form-item label="正确答案">
                <a-input v-model:value="questionForm.answer" placeholder="单选填选项序号(0,1..)，判断填true/false" />
              </a-form-item>
              <a-form-item label="分值">
                <a-input-number v-model:value="questionForm.score" :min="1" :max="100" />
              </a-form-item>
              <a-form-item>
                <a-button type="primary" @click="addQuestion" :loading="adding">添加题目</a-button>
              </a-form-item>
            </a-form>
          </a-card>
        </a-col>

        <!-- 右侧：题目列表和提交 -->
        <a-col :span="16">
          <a-card title="题目列表" size="small">
            <a-list :data-source="exam?.questions || []" item-layout="horizontal">
              <template #renderItem="{ item, index }">
                <a-list-item>
                  <a-list-item-meta>
                    <template #title>
                      <span style="font-weight: bold">{{ index + 1 }}. [{{ getTypeText(item.type) }}]</span>
                      <LatexText :content="item.content" style="font-weight: bold" />
                      <span style="margin-left: 8px; color: #999">（{{ item.score }}分）</span>
                    </template>
                    <template #description>
                      <div v-if="item.options" style="display: flex; flex-wrap: wrap; gap: 8px">
                        <span v-for="(opt, i) in item.options" :key="i">
                          <span>{{ String.fromCharCode(65 + i) }}.</span><LatexText :content="opt" />
                        </span>
                      </div>
                    </template>
                  </a-list-item-meta>
                </a-list-item>
              </template>
            </a-list>
          </a-card>

          <a-card v-if="exam?.status !== 'draft'" title="学生提交" size="small" style="margin-top: 16px">
            <a-table :columns="submissionColumns" :data-source="submissions" row-key="id" size="small">
              <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'status'">
                  <a-tag :color="getStatusTagColor(record.status)">{{ getStatusTagText(record.status) }}</a-tag>
                </template>
                <template v-else-if="column.key === 'score'">
                  {{ record.score ?? '-' }} / {{ exam?.total_score }}
                </template>
                <template v-else-if="column.key === 'action'">
                  <a-button type="link" size="small" @click="openGradeDetail(record)">查看/批改</a-button>
                </template>
              </template>
            </a-table>
          </a-card>

          <a-card v-if="exam?.status !== 'draft'" title="统计分析" size="small" style="margin-top: 16px">
            <a-button type="primary" size="small" @click="fetchStats" :loading="statsLoading">获取分析数据</a-button>
            <div v-if="stats" style="margin-top: 16px">
              <a-row :gutter="16" style="margin-bottom: 16px">
                <a-col :span="4"><a-statistic title="提交人数" :value="stats.submitted_count" /></a-col>
                <a-col :span="4"><a-statistic title="平均分" :value="stats.avg_score" /></a-col>
                <a-col :span="4"><a-statistic title="最高分" :value="stats.max_score" /></a-col>
                <a-col :span="4"><a-statistic title="最低分" :value="stats.min_score" /></a-col>
                <a-col :span="4"><a-statistic title="及格率" :value="stats.pass_rate" suffix="%" /></a-col>
              </a-row>
              <div v-if="stats.score_distribution?.length" style="margin-bottom: 16px">
                <h4>分数分布</h4>
                <div v-for="d in stats.score_distribution" :key="d.range" style="display: flex; align-items: center; margin-bottom: 4px">
                  <span style="width: 60px">{{ d.range }}分</span>
                  <div style="flex: 1; background: #f0f0f0; height: 20px; border-radius: 4px; overflow: hidden">
                    <div :style="{ width: (d.count / Math.max(...stats.score_distribution.map(s => s.count), 1) * 100) + '%', background: '#1890ff', height: '100%' }"></div>
                  </div>
                  <span style="margin-left: 8px; width: 30px">{{ d.count }}人</span>
                </div>
              </div>
              <a-table v-if="stats.question_stats?.length" :columns="qStatColumns" :data-source="stats.question_stats" row-key="question_id" size="small" :pagination="false">
                <template #bodyCell="{ column, record }">
                  <template v-if="column.key === 'correct_rate'">{{ (record.correct_rate * 100).toFixed(1) }}%</template>
                  <template v-else-if="column.key === 'difficulty'">
                    <a-tag :color="record.difficulty > 0.7 ? 'red' : record.difficulty > 0.4 ? 'orange' : 'green'">{{ record.difficulty > 0.7 ? '难' : record.difficulty > 0.4 ? '中' : '易' }}</a-tag>
                  </template>
                  <template v-else-if="column.key === 'discrimination'">{{ record.discrimination.toFixed(2) }}</template>
                </template>
              </a-table>
            </div>
          </a-card>
        </a-col>
      </a-row>
    </a-spin>
    <!-- 批改弹窗 -->
    <a-modal v-model:open="gradeDetailVisible" :title="`批改 - ${gradeDetail?.student_name || ''}`" width="800px" :footer="null">
      <a-spin :spinning="gradeDetailLoading">
        <div v-if="gradeDetail">
          <a-descriptions bordered size="small" :column="2" style="margin-bottom: 16px">
            <a-descriptions-item label="状态">
              <a-tag :color="gradeDetail.status === 'graded' ? 'green' : 'blue'">{{ gradeDetail.status === 'graded' ? '已批改' : '待批改' }}</a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="得分">{{ gradeDetail.score ?? '待批改' }} / {{ exam?.total_score }}</a-descriptions-item>
          </a-descriptions>

          <div v-for="ans in gradeDetail.answers" :key="ans.answer_id" style="margin-bottom: 16px; padding: 12px; background: #fafafa; border-radius: 8px">
            <div style="font-weight: bold; margin-bottom: 8px">
              [{{ getTypeText(ans.question_type) }}] <LatexText :content="ans.question_content" />
            </div>
            <div v-if="ans.options" style="margin-bottom: 8px">
              选项：<span v-for="(opt, i) in ans.options" :key="i">{{ String.fromCharCode(65 + i) }}.<LatexText :content="opt" />；</span>
            </div>
            <div style="margin-bottom: 8px">
	              <span style="color: #1890ff">学生答案：</span>{{ formatAnswer(ans.student_answer, ans.question_type) }}
	            </div>
	            <!-- 学生上传的图片答案 -->
	            <div v-if="ans.image_urls && ans.image_urls.length" style="margin-bottom: 8px">
	              <span style="color: #999; font-size: 12px">图片答案：</span>
	              <a-image-preview-group>
	                <a-image v-for="(url, idx) in ans.image_urls" :key="idx" :src="url" :width="100" :height="75" style="border-radius: 4px; object-fit: cover; margin-right: 4px; vertical-align: top" />
	              </a-image-preview-group>
	            </div>
            <div v-if="ans.correct_answer != null" style="margin-bottom: 8px">
              <span style="color: #52c41a">正确答案：</span>{{ formatAnswer(ans.correct_answer, ans.question_type) }}
            </div>

            <div v-if="ans.question_type === 'essay'" style="margin-top: 8px; padding: 8px; background: #fff; border: 1px solid #d9d9d9; border-radius: 4px">
              <a-form layout="inline">
                <a-form-item label="给分">
                  <a-input-number v-model:value="essayScores[ans.answer_id]" :min="0" :max="ans.max_score || 100" size="small" style="width: 80px" />
                </a-form-item>
                <a-form-item>
                  <a-radio-group v-model:value="essayCorrect[ans.answer_id]" size="small">
                    <a-radio-button :value="true">正确</a-radio-button>
                    <a-radio-button :value="false">错误</a-radio-button>
                  </a-radio-group>
                </a-form-item>
              </a-form>
            </div>
            <div v-else style="margin-top: 4px">
              <a-tag :color="ans.is_correct ? 'green' : 'red'">{{ ans.is_correct ? '正确' : '错误' }}</a-tag>
              <span style="margin-left: 8px">{{ ans.score ?? 0 }}分</span>
            </div>
          </div>

          <a-button type="primary" @click="submitEssayGrades" :loading="essayGrading" :disabled="!hasEssayQuestions">
            批改简答题
          </a-button>
        </div>
      </a-spin>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { RobotOutlined } from '@ant-design/icons-vue'
import { useRoute, useRouter } from 'vue-router'
import { getExam, getExamStats, getExamSubmission, listExamSubmissions, addExamQuestion, gradeExamAnswers, closeExam, exportExam, exportExamPaper } from '@/api/exam'
import { publishExam as publishExamWithPayload } from '@/api/examTemplate'
import LatexText from '@/components/LatexText.vue'

const route = useRoute()
const router = useRouter()
const examId = route.params.id

const exam = ref(null)
const submissions = ref([])
const loading = ref(false)
const adding = ref(false)

const questionForm = ref({
  type: 'single',
  content: '',
  options: ['', '', '', ''],
  answer: '',
  score: 10,
})

const submissionColumns = [
  { key: 'student_name', title: '学生', dataIndex: 'student_name' },
  { key: 'status', title: '状态', dataIndex: 'status' },
  { key: 'score', title: '得分' },
  { key: 'submitted_at', title: '提交时间', dataIndex: 'submitted_at' },
  { key: 'action', title: '操作' },
]

// 批改相关
const gradeDetailVisible = ref(false)
const gradeDetailLoading = ref(false)
const gradeDetail = ref(null)
const essayScores = reactive({})
const essayCorrect = reactive({})
const essayGrading = ref(false)

const stats = ref(null)
const statsLoading = ref(false)
const qStatColumns = [
  { title: '题号', dataIndex: 'order', key: 'order', width: 60 },
  { title: '题型', dataIndex: 'type', key: 'type', width: 80, customRender: ({ text }) => ({ single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[text] || text) },
  { title: '内容', dataIndex: 'content', key: 'content', ellipsis: true },
  { title: '正确率', key: 'correct_rate', width: 80 },
  { title: '难度', key: 'difficulty', width: 60 },
  { title: '区分度', key: 'discrimination', width: 80 },
]

async function fetchStats() {
  statsLoading.value = true
  try {
    const res = await getExamStats(examId)
    stats.value = res.data
  } catch (e) {
    message.error('获取统计失败')
  } finally {
    statsLoading.value = false
  }
}

const hasEssayQuestions = computed(() => {
  if (!gradeDetail.value) return false
  return gradeDetail.value.answers.some(a => a.question_type === 'essay')
})

// 是否含主观题（用于显示 AI 审核入口）
const hasSubjectiveQuestions = computed(() => {
  if (!exam.value || !exam.value.questions) return false
  return exam.value.questions.some(q => q.type === 'essay' || q.type === 'fill')
})

function goToReview() {
  router.push(`/exams/${examId}/review`)
}

// 学生提交列表状态显示
function getStatusTagColor(status) {
  return {
    in_progress: 'default',
    submitted: 'blue',
    ai_grading: 'orange',
    ai_graded: 'cyan',
    graded: 'green',
    timeout: 'red',
  }[status] || 'default'
}

function getStatusTagText(status) {
  return {
    in_progress: '考试中',
    submitted: '已提交',
    ai_grading: 'AI 批改中',
    ai_graded: '待审核',
    graded: '已批改',
    timeout: '已超时',
  }[status] || status
}

async function openGradeDetail(record) {
  gradeDetailVisible.value = true
  gradeDetailLoading.value = true
  try {
    const res = await getExamSubmission(record.id)
    gradeDetail.value = res.data
    // 初始化简答题评分
    Object.keys(essayScores).forEach(k => delete essayScores[k])
    Object.keys(essayCorrect).forEach(k => delete essayCorrect[k])
    for (const ans of res.data.answers) {
      if (ans.question_type === 'essay') {
        essayScores[ans.answer_id] = ans.score || 0
        essayCorrect[ans.answer_id] = ans.is_correct ?? false
      }
    }
  } catch (e) {
    message.error('获取提交详情失败')
  } finally {
    gradeDetailLoading.value = false
  }
}

async function submitEssayGrades() {
  if (!gradeDetail.value) return
  essayGrading.value = true
  try {
    const payload = []
    for (const ans of gradeDetail.value.answers) {
      if (ans.question_type === 'essay') {
        payload.push({
          answer_id: ans.answer_id,
          score: essayScores[ans.answer_id] || 0,
          is_correct: essayCorrect[ans.answer_id] ?? false,
        })
      }
    }
    await gradeExamAnswers(gradeDetail.value.id, payload)
    message.success('批改成功')
    gradeDetailVisible.value = false
    fetchSubmissions()
  } catch (e) {
    message.error('批改失败')
  } finally {
    essayGrading.value = false
  }
}

async function fetchExam() {
  loading.value = true
  try {
    const res = await getExam(examId)
    exam.value = res.data
    if (res.data.status !== 'draft') {
      fetchSubmissions()
    }
  } catch (e) {
    message.error('获取考试详情失败')
  } finally {
    loading.value = false
  }
}

async function fetchSubmissions() {
  try {
    const res = await listExamSubmissions(examId)
    submissions.value = res.data.map(s => ({
      ...s,
      submitted_at: s.submitted_at ? new Date(s.submitted_at).toLocaleString('zh-CN') : '-',
    }))
  } catch (e) {
    // 忽略
  }
}

async function addQuestion() {
  if (!questionForm.value.content.trim()) {
    message.error('请输入题目内容')
    return
  }
  if (!questionForm.value.answer.trim()) {
    message.error('请输入正确答案')
    return
  }
  adding.value = true
  try {
    const payload = {
      type: questionForm.value.type,
      content: questionForm.value.content,
      options: (questionForm.value.type === 'single' || questionForm.value.type === 'multi') 
        ? questionForm.value.options.filter(o => o.trim()) : null,
      answer: questionForm.value.answer,
      score: questionForm.value.score,
    }
    
    await addExamQuestion(examId, payload)
    message.success('题目添加成功')
    
    // 重置表单
    questionForm.value = {
      type: 'single',
      content: '',
      options: ['', '', '', ''],
      answer: '',
      score: 10,
    }
    
    // 刷新考试详情
    fetchExam()
  } catch (e) {
    message.error('添加失败')
  } finally {
    adding.value = false
  }
}

async function handlePublishExam() {
  try {
    const res = await publishExamWithPayload(examId, {})
    message.success(`考试发布成功！${res.data.question_count} 题 / ${res.data.total_score} 分`)
    fetchExam()
  } catch (e) {
    const msg = e?.response?.data?.detail || '发布失败'
    message.error(msg)
  }
}

async function exportPaper() {
  try {
    const res = await exportExamPaper(examId)
    const blob = new Blob([res.data], { type: 'text/html' })
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `试卷_${examId}.html`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  } catch (e) {
    message.error('导出试卷失败')
  }
}

async function handleCloseExam() {
  try {
    await closeExam(examId)
    message.success('考试已关闭')
    fetchExam()
  } catch (e) {
    message.error('关闭失败')
  }
}

async function exportCSV() {
  try {
    const res = await exportExam(examId)
    const url = window.URL.createObjectURL(new Blob([res.data], { type: 'text/csv' }))
    const link = document.createElement('a')
    link.href = url
    link.download = `考试成绩_${examId}.csv`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  } catch (e) {
    message.error('导出失败')
  }
}

function getStatusColor(status) {
  return { draft: 'default', published: 'blue', closed: 'gray' }[status] || 'default'
}

function getStatusText(status) {
  return { draft: '草稿', published: '已发布', closed: '已关闭' }[status] || status
}

function getTypeText(type) {
  return { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '简答' }[type] || type
}

/**
 * 格式化答案显示：将索引格式（"0","1"）统一转为字母格式（"A","B"）
 * 兼容后端可能存储的字母格式和索引格式
 */
function formatAnswer(answer, questionType) {
  if (!answer && answer !== 0) return '（未作答）'
  const str = String(answer).trim()
  if (!str) return '（未作答）'

  if (questionType === 'single') {
    // 单选：可能是 "0"/"1"/"2" 或 "A"/"B"/"C"
    if (/^\d+$/.test(str)) {
      return String.fromCharCode(65 + parseInt(str))
    }
    return str
  }

  if (questionType === 'multi') {
    // 多选：可能是 "0,2,3" 或 "A,C,D"
    return str.split(',').map(s => {
      const trimmed = s.trim()
      if (/^\d+$/.test(trimmed)) {
        return String.fromCharCode(65 + parseInt(trimmed))
      }
      return trimmed
    }).join(',')
  }

  if (questionType === 'judge') {
    return str.toLowerCase() === 'true' ? '正确' : '错误'
  }

  return str
}

onMounted(fetchExam)
</script>