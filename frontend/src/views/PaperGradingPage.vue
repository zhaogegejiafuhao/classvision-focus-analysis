<template>
  <a-layout style="min-height: 100vh">
    <a-layout-header style="display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
      <span style="color: #fff; font-size: 18px; font-weight: bold; cursor: pointer" @click="$router.push('/')">
        ClassVision 试卷批改
      </span>
      <a-button type="link" style="color: #fff" @click="$router.push('/')">返回首页</a-button>
    </a-layout-header>
    <a-layout-content style="padding: 24px">

      <!-- 步骤指示器 -->
      <a-steps :current="currentStep - 1" style="margin-bottom: 24px">
        <a-step title="选择课堂与模板" />
        <a-step title="摄像头扫描" />
        <a-step title="评阅结果" />
        <a-step title="成绩统计" />
      </a-steps>

      <!-- 第一步：选择课堂与模板 -->
      <a-card title="第一步：选择课堂与模板" v-if="currentStep === 1">
        <a-space style="margin-bottom: 16px">
          <a-select v-model:value="selectedClassroomId" placeholder="选择课堂"
                    :options="classroomOptions" style="width: 200px" allow-clear show-search
                    @change="loadTemplates" />
          <a-select v-model:value="selectedTemplateId" placeholder="选择模板"
                    :options="templateOptions" style="width: 200px" />
          <a-button type="primary" @click="showTemplateModal = true">创建新模板</a-button>
          <a-popconfirm v-if="selectedTemplateId" title="确认删除此模板？" ok-text="删除" cancel-text="取消"
                        @confirm="deleteTemplate">
            <a-button danger>删除模板</a-button>
          </a-popconfirm>
          <a-button :disabled="!selectedTemplateId" @click="currentStep = 2">下一步：扫描</a-button>
        </a-space>

        <!-- 模板创建弹窗 -->
        <a-modal v-model:open="showTemplateModal" title="创建试卷模板" width="1200px" @ok="createTemplate"
                 :ok-button-props="{ loading: templateCreating }" @cancel="resetTemplateModal">
          <a-form layout="vertical">
            <a-form-item label="模板名称">
              <a-input v-model:value="newTemplate.name" placeholder="如：期中考试答题卡" />
            </a-form-item>

            <!-- 步骤1：上传答题卡图片 -->
            <a-form-item label="答题卡参考图片">
              <a-space v-if="!templateImageData">
                <a-upload :before-upload="handleTemplateImageUpload" accept="image/*" :show-upload-list="false">
                  <a-button type="primary">上传答题卡图片</a-button>
                </a-upload>
                <span style="color: #999">上传一张空白答题卡照片，用于框选各题区域</span>
              </a-space>
              <a-space v-else>
                <a-button @click="doPerspectivePreview" :loading="perspectiveLoading">透视矫正</a-button>
                <a-button @click="doAutoDetect" :loading="autoDetectLoading">自动检测区域</a-button>
                <a-button @click="clearTemplateImage">更换图片</a-button>
              </a-space>
            </a-form-item>

            <!-- 步骤2：画布框选 + 题目列表 -->
            <div v-if="templateImageData" style="display: flex; gap: 16px">
              <!-- 左侧画布 -->
              <div style="flex: 1">
                <div style="margin-bottom: 8px">
                  <a-typography-text type="secondary">
                    {{ drawingQuestionIndex !== null
                      ? `正在框选第${drawingQuestionIndex}题区域，请在图片上拖动鼠标`
                      : '点击右侧题目的"框选"按钮，或直接点击已有框选区域进行微调' }}
                  </a-typography-text>
                </div>
                <canvas ref="templateCanvas" width="800" height="600"
                        style="border: 1px solid #d9d9d9; border-radius: 4px; cursor: crosshair; max-width: 100%; max-height: 65vh"
                        @mousedown="onCanvasMouseDown"
                        @mousemove="onCanvasMouseMove"
                        @mouseup="onCanvasMouseUp"
                        @mouseleave="onCanvasMouseUp" />
              </div>

              <!-- 右侧题目列表 -->
              <div style="width: 340px; max-height: 450px; overflow-y: auto">
                <a-space style="margin-bottom: 8px">
                  <a-button type="dashed" size="small" @click="addQuestion">+ 添加题目</a-button>
                  <a-button size="small" @click="clearAllRegions">清空框选</a-button>
                </a-space>
                <div v-for="(q, i) in newTemplate.questions" :key="i"
                     :style="{
                       padding: '8px', marginBottom: '8px', borderRadius: '4px',
                       border: drawingQuestionIndex === q.question_index ? '2px solid #1890ff' : '1px solid #d9d9d9',
                       background: drawingQuestionIndex === q.question_index ? '#e6f7ff' : '#fff'
                     }">
                  <div style="display: flex; align-items: center; gap: 4px; margin-bottom: 4px; flex-wrap: wrap">
                    <a-input-number v-model:value="q.question_index" :min="1" :max="100" size="small" style="width: 55px" />
                    <a-select v-model:value="q.question_type" size="small" style="width: 90px">
                      <a-select-option value="objective">客观题</a-select-option>
                      <a-select-option value="subjective">主观题</a-select-option>
                    </a-select>
                    <a-input-number v-model:value="q.max_score" :min="0" :step="1" size="small" style="width: 80px"
                                    addon-before="满分" />
                    <a-button size="small" :type="drawingQuestionIndex === q.question_index ? 'primary' : 'default'"
                              @click="toggleDrawing(q)">框选</a-button>
                    <a-button danger size="small" @click="removeQuestion(i)">删</a-button>
                  </div>
                  <a-input v-model:value="q.standard_answer" size="small" placeholder="标准答案（如A、BCD、关键词）" />
                  <div v-if="q.w > 0" style="font-size: 11px; color: #999; margin-top: 2px">
                    区域: x={{ q.x.toFixed(2) }} y={{ q.y.toFixed(2) }} w={{ q.w.toFixed(2) }} h={{ q.h.toFixed(2) }}
                  </div>
                </div>
              </div>
            </div>
          </a-form>
        </a-modal>
      </a-card>

      <!-- 第二步：摄像头扫描 -->
      <a-card title="第二步：摄像头扫描" v-if="currentStep === 2">
        <div style="display: flex; gap: 24px; flex-wrap: wrap">
          <div>
            <video ref="videoEl" width="640" height="480" autoplay
                   style="border: 1px solid #d9d9d9; border-radius: 4px" v-if="cameraActive" />
            <img v-if="capturedImage" :src="capturedImage"
                 style="max-width: 640px; border-radius: 4px; border: 1px solid #d9d9d9" />
            <div v-if="!cameraActive && !capturedImage"
                 style="width: 640px; height: 480px; border: 1px dashed #d9d9d9; border-radius: 4px;
                        display: flex; align-items: center; justify-content: center; color: #999">
              点击下方按钮开启摄像头
            </div>
            <a-space style="margin-top: 12px">
              <a-button type="primary" @click="startCamera" v-if="!cameraActive">开启摄像头</a-button>
              <a-button @click="stopCamera" v-if="cameraActive">关闭摄像头</a-button>
              <a-button type="primary" @click="captureAndScan" :loading="scanning"
                        :disabled="!cameraActive && !capturedImage">拍照并扫描</a-button>
              <a-button @click="capturedImage = null" v-if="capturedImage">重拍</a-button>
              <a-button @click="currentStep = 1">返回</a-button>
            </a-space>
          </div>

          <div style="width: 280px">
            <a-form layout="vertical">
              <a-form-item label="关联学生（可选）">
                <a-select v-model:value="scanForm.person_id"
                          :options="studentOptions" allow-clear show-search
                          placeholder="选择已注册学生" />
              </a-form-item>
              <a-form-item label="或输入姓名">
                <a-input v-model:value="scanForm.student_name" placeholder="未注册学生姓名" />
              </a-form-item>
              <a-form-item>
                <a-checkbox v-model:checked="scanForm.grade_subjective">
                  同时评分主观题（调用AI，较慢）
                </a-checkbox>
              </a-form-item>
              <a-alert message="提示：将试卷平放在摄像头前，确保四角可见" type="info" show-icon />
            </a-form>
          </div>
        </div>
      </a-card>

      <!-- 第三步：评阅结果 -->
      <a-card title="第三步：评阅结果" v-if="currentStep === 3 && scanResult">
        <a-space style="margin-bottom: 16px">
          <a-button @click="currentStep = 2">继续扫描下一张</a-button>
          <a-button type="primary" @click="saveFinalScore">保存最终成绩</a-button>
          <a-button @click="loadStatistics">查看统计</a-button>
        </a-space>

        <a-row :gutter="16">
          <a-col :span="8">
            <a-image v-if="scanResult.corrected_image"
                     :src="'data:image/jpeg;base64,' + scanResult.corrected_image"
                     :width="400" style="border-radius: 4px" />
            <a-statistic title="自动总分" :value="scanResult.total_auto_score" suffix="分"
                         style="margin-top: 16px" :value-style="{ color: '#1890ff' }" />
          </a-col>
          <a-col :span="16">
            <a-table :columns="answerColumns" :data-source="scanResult.answers" row-key="id"
                     size="small" :pagination="{ pageSize: 10 }">
              <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'question_type'">
                  <a-tag :color="record.question_type === 'objective' ? 'blue' : 'orange'">
                    {{ record.question_type === 'objective' ? '客观' : '主观' }}
                  </a-tag>
                </template>
                <template v-if="column.key === 'correct'">
                  <a-tag v-if="record.correct === true" color="green">正确</a-tag>
                  <a-tag v-else-if="record.correct === false" color="red">错误</a-tag>
                  <span v-else>-</span>
                </template>
                <template v-if="column.key === 'final_score'">
                  <a-input-number v-model:value="record.final_score" :min="0"
                                  :max="record.max_score" :step="0.5" size="small"
                                  @change="markCorrected(record)" style="width: 80px" />
                </template>
                <template v-if="column.key === 'ai_suggestion'">
                  <a-tooltip :title="record.ai_suggestion" v-if="record.ai_suggestion">
                    <a-button size="small" @click="showSuggestion(record)">查看建议</a-button>
                  </a-tooltip>
                  <a-button v-if="record.question_type === 'subjective'" size="small"
                            @click="regradeSubjective(record)" :loading="record._regrading">
                    {{ record.ai_suggestion ? 'AI重评' : 'AI评分' }}
                  </a-button>
                </template>
              </template>
            </a-table>
          </a-col>
        </a-row>
      </a-card>

      <!-- 第四步：成绩统计 -->
      <a-card title="成绩统计" v-if="currentStep === 4 && statistics">
        <a-space style="margin-bottom: 16px">
          <a-button @click="currentStep = 2">继续扫描</a-button>
          <a-button @click="currentStep = 1">返回模板选择</a-button>
        </a-space>
        <a-row :gutter="16" style="margin-bottom: 24px">
          <a-col :span="6"><a-statistic title="试卷总数" :value="statistics.total_papers" /></a-col>
          <a-col :span="6"><a-statistic title="平均分" :value="statistics.avg_score" :value-style="{ color: '#1890ff' }" /></a-col>
          <a-col :span="6"><a-statistic title="最高分" :value="statistics.max_score" :value-style="{ color: '#52c41a' }" /></a-col>
          <a-col :span="6"><a-statistic title="最低分" :value="statistics.min_score" :value-style="{ color: '#ff4d4f' }" /></a-col>
        </a-row>
        <a-row :gutter="16">
          <a-col :span="12">
            <div ref="distributionChartEl" style="width: 100%; height: 350px" />
          </a-col>
          <a-col :span="12">
            <div ref="accuracyChartEl" style="width: 100%; height: 350px" />
          </a-col>
        </a-row>
      </a-card>

    </a-layout-content>
  </a-layout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import axios from 'axios'
import * as echarts from 'echarts'
import { message, Modal } from 'ant-design-vue'
import { waitForBackend } from '../utils/api'

const currentStep = ref(1)

// 课堂与模板
const classrooms = ref([])
const templates = ref([])
const selectedClassroomId = ref(null)
const selectedTemplateId = ref(null)

// 模板创建
const showTemplateModal = ref(false)
const templateCreating = ref(false)
const newTemplate = ref({ name: '', questions: [] })

// 模板画布框选
const templateCanvas = ref(null)
const templateImageData = ref(null)      // base64 图片数据（不含 data: 前缀）
const templateImageObj = ref(null)       // Image 对象
const drawingQuestionIndex = ref(null)   // 当前正在框选的题号
const isDrawing = ref(false)
const drawStart = ref({ x: 0, y: 0 })
const drawCurrent = ref({ x: 0, y: 0 })
const perspectiveLoading = ref(false)
const autoDetectLoading = ref(false)

// 区域颜色（循环使用）
const regionColors = ['#1890ff', '#52c41a', '#faad14', '#f5222d', '#722ed1', '#13c2c2', '#eb2f96', '#fa8c16']

// 摄像头
const videoEl = ref(null)
const cameraActive = ref(false)
const capturedImage = ref(null)
const scanning = ref(false)
let mediaStream = null

// 扫描表单
const scanForm = ref({ person_id: null, student_name: '', grade_subjective: true })

// 扫描结果
const scanResult = ref(null)

// 统计
const statistics = ref(null)
const distributionChartEl = ref(null)
const accuracyChartEl = ref(null)

// 学生列表
const students = ref([])

const classroomOptions = computed(() => classrooms.value.map(c => ({ value: c.id, label: c.name })))
const templateOptions = computed(() => templates.value.map(t => ({ value: t.id, label: t.name })))
const studentOptions = computed(() => students.value.map(s => ({ value: s.id, label: s.name })))

const answerColumns = [
  { title: '题号', dataIndex: 'question_index', key: 'question_index', width: 60 },
  { title: '类型', key: 'question_type', width: 70 },
  { title: 'OCR识别', dataIndex: 'ocr_text', key: 'ocr_text', ellipsis: true },
  { title: '标准答案', dataIndex: 'standard_answer', key: 'standard_answer', width: 100 },
  { title: '满分', dataIndex: 'max_score', key: 'max_score', width: 60 },
  { title: '自动评分', dataIndex: 'auto_score', key: 'auto_score', width: 80 },
  { title: '对错', key: 'correct', width: 60 },
  { title: '最终评分', key: 'final_score', width: 100 },
  { title: 'AI建议', key: 'ai_suggestion', width: 120 },
]

function addQuestion() {
  const idx = newTemplate.value.questions.length + 1
  newTemplate.value.questions.push({
    question_index: idx, question_type: 'objective',
    x: 0, y: 0, w: 0, h: 0,
    max_score: 5, standard_answer: '',
  })
}

function removeQuestion(index) {
  newTemplate.value.questions.splice(index, 1)
  redrawCanvas()
}

function clearAllRegions() {
  newTemplate.value.questions.forEach(q => { q.x = 0; q.y = 0; q.w = 0; q.h = 0 })
  drawingQuestionIndex.value = null
  redrawCanvas()
}

function toggleDrawing(q) {
  if (drawingQuestionIndex.value === q.question_index) {
    drawingQuestionIndex.value = null
  } else {
    drawingQuestionIndex.value = q.question_index
  }
}

function resetTemplateModal() {
  templateImageData.value = null
  templateImageObj.value = null
  drawingQuestionIndex.value = null
  isDrawing.value = false
  newTemplate.value = { name: '', questions: [] }
}

function clearTemplateImage() {
  templateImageData.value = null
  templateImageObj.value = null
  newTemplate.value.questions.forEach(q => { q.x = 0; q.y = 0; q.w = 0; q.h = 0 })
  drawingQuestionIndex.value = null
}

// 图片上传
function handleTemplateImageUpload(file) {
  const reader = new FileReader()
  reader.onload = (e) => {
    const dataUrl = e.target.result
    templateImageData.value = dataUrl.split(',')[1]
    const img = new Image()
    img.onload = () => {
      templateImageObj.value = img
      nextTick(() => drawCanvasImage())
    }
    img.src = dataUrl
  }
  reader.readAsDataURL(file)
  return false
}

// 画布绘制
function drawCanvasImage() {
  const canvas = templateCanvas.value
  if (!canvas || !templateImageObj.value) return
  const ctx = canvas.getContext('2d')
  const img = templateImageObj.value

  // 计算缩放比例，适配画布
  const maxW = 1000, maxH = 700
  const scale = Math.min(maxW / img.width, maxH / img.height)
  canvas.width = img.width * scale
  canvas.height = img.height * scale

  ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
  drawAllRegions()
}

function drawAllRegions() {
  const canvas = templateCanvas.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')

  newTemplate.value.questions.forEach((q, i) => {
    if (q.w <= 0 || q.h <= 0) return
    const x = q.x * canvas.width
    const y = q.y * canvas.height
    const w = q.w * canvas.width
    const h = q.h * canvas.height
    const color = regionColors[i % regionColors.length]

    ctx.strokeStyle = color
    ctx.lineWidth = 2
    ctx.strokeRect(x, y, w, h)

    // 半透明填充
    ctx.fillStyle = color + '20'
    ctx.fillRect(x, y, w, h)

    // 题号标签
    ctx.fillStyle = color
    ctx.fillRect(x, y - 20, 30, 20)
    ctx.fillStyle = '#fff'
    ctx.font = '12px sans-serif'
    ctx.fillText(`Q${q.question_index}`, x + 4, y - 6)
  })
}

function redrawCanvas() {
  const canvas = templateCanvas.value
  if (!canvas || !templateImageObj.value) return
  const ctx = canvas.getContext('2d')
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  ctx.drawImage(templateImageObj.value, 0, 0, canvas.width, canvas.height)
  drawAllRegions()
}

// 鼠标事件
function getCanvasPos(e) {
  const canvas = templateCanvas.value
  const rect = canvas.getBoundingClientRect()
  const scaleX = canvas.width / rect.width
  const scaleY = canvas.height / rect.height
  return {
    x: (e.clientX - rect.left) * scaleX,
    y: (e.clientY - rect.top) * scaleY,
  }
}

function onCanvasMouseDown(e) {
  if (drawingQuestionIndex.value === null) {
    // 检查是否点击了已有框选区域，如果是则选中该题用于重新框选
    const pos = getCanvasPos(e)
    const clicked = newTemplate.value.questions.find(q => {
      if (q.w <= 0 || q.h <= 0) return false
      const canvas = templateCanvas.value
      const x = q.x * canvas.width
      const y = q.y * canvas.height
      const w = q.w * canvas.width
      const h = q.h * canvas.height
      return pos.x >= x && pos.x <= x + w && pos.y >= y && pos.y <= y + h
    })
    if (clicked) {
      drawingQuestionIndex.value = clicked.question_index
      message.info(`已选中第${clicked.question_index}题，可拖动鼠标重新框选区域`)
    } else {
      message.warning('请先点击右侧题目的"框选"按钮，或点击已有框选区域进行微调')
    }
    return
  }
  isDrawing.value = true
  drawStart.value = getCanvasPos(e)
  drawCurrent.value = { ...drawStart.value }
}

function onCanvasMouseMove(e) {
  if (!isDrawing.value) return
  drawCurrent.value = getCanvasPos(e)

  // 实时重绘 + 绘制当前框选中的矩形
  redrawCanvas()
  const canvas = templateCanvas.value
  const ctx = canvas.getContext('2d')
  const x = Math.min(drawStart.value.x, drawCurrent.value.x)
  const y = Math.min(drawStart.value.y, drawCurrent.value.y)
  const w = Math.abs(drawCurrent.value.x - drawStart.value.x)
  const h = Math.abs(drawCurrent.value.y - drawStart.value.y)
  ctx.strokeStyle = '#1890ff'
  ctx.lineWidth = 2
  ctx.setLineDash([5, 5])
  ctx.strokeRect(x, y, w, h)
  ctx.setLineDash([])
}

function onCanvasMouseUp(e) {
  if (!isDrawing.value) return
  isDrawing.value = false

  const canvas = templateCanvas.value
  const x = Math.min(drawStart.value.x, drawCurrent.value.x) / canvas.width
  const y = Math.min(drawStart.value.y, drawCurrent.value.y) / canvas.height
  const w = Math.abs(drawCurrent.value.x - drawStart.value.x) / canvas.width
  const h = Math.abs(drawCurrent.value.y - drawStart.value.y) / canvas.height

  // 过滤太小的区域
  if (w < 0.01 || h < 0.005) {
    redrawCanvas()
    return
  }

  // 更新对应题目的区域
  const q = newTemplate.value.questions.find(q => q.question_index === drawingQuestionIndex.value)
  if (q) {
    q.x = parseFloat(x.toFixed(4))
    q.y = parseFloat(y.toFixed(4))
    q.w = parseFloat(w.toFixed(4))
    q.h = parseFloat(h.toFixed(4))
  }

  drawingQuestionIndex.value = null
  redrawCanvas()
}

// 透视矫正预览
async function doPerspectivePreview() {
  if (!templateImageData.value) return
  perspectiveLoading.value = true
  try {
    const res = await axios.post('/api/papers/templates/perspective-preview', {
      image_data: templateImageData.value,
    })
    if (res.data.corrected_image) {
      templateImageData.value = res.data.corrected_image
      const img = new Image()
      img.onload = () => {
        templateImageObj.value = img
        drawCanvasImage()
        message.success('透视矫正完成')
      }
      img.src = 'data:image/jpeg;base64,' + res.data.corrected_image
    } else {
      message.warning('未能检测到试卷边界，使用原图')
    }
  } catch (e) {
    message.error('透视矫正失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    perspectiveLoading.value = false
  }
}

// 自动检测区域
async function doAutoDetect() {
  if (!templateImageData.value) return
  autoDetectLoading.value = true
  try {
    const res = await axios.post('/api/papers/templates/auto-detect-regions', {
      image_data: templateImageData.value,
    })
    const regions = res.data.regions || []
    if (regions.length === 0) {
      message.warning('未检测到文本区域，请手动框选')
      return
    }

    // 将检测到的区域分配给题目
    // 如果题目数 < 区域数，自动创建题目；如果题目数 > 区域数，多出的题目不分配
    const questions = newTemplate.value.questions
    for (let i = 0; i < regions.length; i++) {
      if (i < questions.length) {
        questions[i].x = regions[i].x
        questions[i].y = regions[i].y
        questions[i].w = regions[i].w
        questions[i].h = regions[i].h
      } else {
        questions.push({
          question_index: i + 1,
          question_type: 'objective',
          x: regions[i].x, y: regions[i].y, w: regions[i].w, h: regions[i].h,
          max_score: 5, standard_answer: '',
        })
      }
    }
    redrawCanvas()
    message.success(`检测到 ${regions.length} 个区域，已自动分配`)
  } catch (e) {
    message.error('自动检测失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    autoDetectLoading.value = false
  }
}

async function createTemplate() {
  if (!newTemplate.value.name) {
    message.warning('请输入模板名称')
    return
  }
  const validQuestions = newTemplate.value.questions.filter(q => q.w > 0 && q.h > 0)
  if (validQuestions.length === 0) {
    message.warning('请至少框选一道题目的答题区域')
    return
  }
  templateCreating.value = true
  try {
    const res = await axios.post('/api/papers/templates', {
      name: newTemplate.value.name,
      classroom_id: selectedClassroomId.value,
      questions: validQuestions,
    })
    message.success('模板创建成功')
    showTemplateModal.value = false
    selectedTemplateId.value = res.data.id
    await loadTemplates()
    resetTemplateModal()
  } catch (e) {
    message.error('创建失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    templateCreating.value = false
  }
}

// 摄像头
async function startCamera() {
  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({ video: { width: 1280, height: 720 } })
    cameraActive.value = true
    await nextTick()
    if (videoEl.value) videoEl.value.srcObject = mediaStream
  } catch (e) {
    message.error('无法访问摄像头: ' + e.message)
  }
}

function stopCamera() {
  if (mediaStream) mediaStream.getTracks().forEach(t => t.stop())
  mediaStream = null
  cameraActive.value = false
}

async function captureAndScan() {
  if (!selectedTemplateId.value) {
    message.warning('请先选择模板')
    return
  }
  scanning.value = true
  try {
    let base64Data
    if (cameraActive.value && videoEl.value) {
      const canvas = document.createElement('canvas')
      canvas.width = 1280
      canvas.height = 720
      canvas.getContext('2d').drawImage(videoEl.value, 0, 0, 1280, 720)
      capturedImage.value = canvas.toDataURL('image/jpeg')
      base64Data = capturedImage.value.split(',')[1]
      stopCamera()
    } else if (capturedImage.value) {
      base64Data = capturedImage.value.split(',')[1]
    } else {
      message.warning('请先拍照')
      return
    }

    const res = await axios.post('/api/papers/scan', {
      image_data: base64Data,
      template_id: selectedTemplateId.value,
      person_id: scanForm.value.person_id,
      student_name: scanForm.value.student_name,
      classroom_id: selectedClassroomId.value,
      grade_subjective: scanForm.value.grade_subjective,
    })

    scanResult.value = res.data
    scanResult.value.answers.forEach(a => { a.final_score = a.final_score ?? a.auto_score })
    currentStep.value = 3
    message.success(`扫描完成，自动得分: ${res.data.total_auto_score} 分`)
  } catch (e) {
    message.error('扫描失败: ' + (e.response?.data?.detail || e.message))
  } finally {
    scanning.value = false
  }
}

async function markCorrected(record) {
  try {
    await axios.put(`/api/papers/${scanResult.value.paper_id}/answers/${record.id}`, {
      final_score: record.final_score,
    })
  } catch (e) {
    console.error('保存失败', e)
  }
}

async function saveFinalScore() {
  const total = scanResult.value.answers.reduce((sum, a) => sum + (a.final_score ?? a.auto_score), 0)
  try {
    await axios.put(`/api/papers/${scanResult.value.paper_id}/final-score`, { final_score: total })
    message.success(`最终成绩已保存: ${total} 分`)
  } catch (e) {
    message.error('保存失败: ' + (e.response?.data?.detail || e.message))
  }
}

function showSuggestion(record) {
  Modal.info({
    title: `第${record.question_index}题 AI评分建议`,
    content: record.ai_suggestion || '无建议',
    width: 600,
  })
}

async function regradeSubjective(record) {
  record._regrading = true
  try {
    const resp = await fetch(`/api/papers/${scanResult.value.paper_id}/answers/${record.id}/grade-subjective`, {
      method: 'POST',
    })
    if (!resp.ok) throw new Error('HTTP ' + resp.status)
    const reader = resp.body.getReader()
    const decoder = new TextDecoder()
    let buffer = ''
    let fullText = ''
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
        if (data.delta) fullText += data.delta
        if (data.done) {
          record.ai_suggestion = data.suggestion || fullText
          record.auto_score = data.score ?? record.auto_score
          record.final_score = data.score ?? record.final_score
          message.success(`AI评分完成: ${data.score} 分`)
        }
        if (data.error) message.error('AI重评失败: ' + data.error)
      }
    }
  } catch (e) {
    message.error('AI重评失败: ' + e.message)
  } finally {
    record._regrading = false
  }
}

async function loadStatistics() {
  currentStep.value = 4
  try {
    const res = await axios.get(`/api/papers/templates/${selectedTemplateId.value}/statistics`)
    statistics.value = res.data
    await nextTick()
    // 分数分布饼图
    const distChart = echarts.init(distributionChartEl.value)
    distChart.setOption({
      title: { text: '分数分布', left: 'center' },
      tooltip: { trigger: 'item', formatter: '{b}: {c}人 ({d}%)' },
      series: [{
        type: 'pie', radius: ['40%', '70%'],
        data: Object.entries(res.data.score_distribution)
          .filter(([k, v]) => v > 0)
          .map(([k, v]) => ({ name: k, value: v })),
        label: { formatter: '{b}\n{c}人' },
      }],
    })
    // 正确率柱状图
    const accChart = echarts.init(accuracyChartEl.value)
    accChart.setOption({
      title: { text: '客观题正确率', left: 'center' },
      tooltip: { trigger: 'axis', formatter: p => `${p[0].name}<br/>正确率: ${(p[0].value * 100).toFixed(1)}%` },
      xAxis: { type: 'category', data: res.data.per_question_accuracy.map(q => `第${q.question_index}题`) },
      yAxis: { type: 'value', max: 1, axisLabel: { formatter: v => (v * 100) + '%' } },
      series: [{
        type: 'bar',
        data: res.data.per_question_accuracy.map(q => q.accuracy),
        itemStyle: { color: '#1890ff' },
        label: { show: true, position: 'top', formatter: d => (d.value * 100).toFixed(0) + '%' },
      }],
    })
  } catch (e) {
    message.error('加载统计失败: ' + (e.response?.data?.detail || e.message))
  }
}

async function loadClassrooms() {
  try {
    const res = await axios.get('/api/classrooms')
    classrooms.value = res.data || []
  } catch { classrooms.value = [] }
}

async function loadTemplates() {
  try {
    const res = await axios.get('/api/papers/templates', {
      params: selectedClassroomId.value ? { classroom_id: selectedClassroomId.value } : {},
    })
    templates.value = res.data || []
  } catch { templates.value = [] }
}

async function deleteTemplate() {
  if (!selectedTemplateId.value) return
  try {
    await axios.delete(`/api/papers/templates/${selectedTemplateId.value}`)
    message.success('模板已删除')
    selectedTemplateId.value = null
    await loadTemplates()
  } catch (e) {
    message.error('删除失败: ' + (e.response?.data?.detail || e.message))
  }
}

async function loadStudents() {
  try {
    const res = await axios.get('/api/persons', { params: { role: 'student' } })
    students.value = res.data || []
  } catch { students.value = [] }
}

onMounted(async () => {
  await waitForBackend()
  await Promise.all([loadClassrooms(), loadTemplates(), loadStudents()])
})

onUnmounted(() => {
  stopCamera()
})
</script>
