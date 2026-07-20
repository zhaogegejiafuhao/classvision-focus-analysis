<template>
  <a-card title="试卷模板编辑器" :bordered="false" class="template-editor">
    <!-- 顶部工具栏 -->
    <div class="toolbar">
      <a-upload-dragger
        :before-upload="handleBlankUpload"
        :show-upload-list="false"
        accept="image/*"
        :multiple="false"
        class="blank-uploader"
      >
        <div class="upload-hint">
          <InboxOutlined />
          <p class="upload-text">{{ imageLoaded ? '重新上传空白卷' : '点击或拖拽上传空白卷' }}</p>
          <p class="upload-sub">JPG / PNG / BMP</p>
        </div>
      </a-upload-dragger>

      <div class="actions">
        <a-button
          type="primary"
          :disabled="!regions.length || !imageLoaded"
          :loading="saving"
          @click="emitSave"
        >
          <template #icon><SaveOutlined /></template>
          保存模板（{{ regions.length }} 个区域）
        </a-button>
        <a-button :disabled="!regions.length" @click="clearAll">
          清空所有
        </a-button>
        <a-tag v-if="imageLoaded && naturalSize" color="default">
          原图：{{ naturalSize[0] }} × {{ naturalSize[1] }} px
        </a-tag>
      </div>
    </div>

    <!-- 主体：左 canvas + 右区域列表 -->
    <a-row :gutter="16" class="main-row">
      <a-col :xs="24" :lg="16">
        <div class="canvas-wrap" ref="canvasWrapRef">
          <canvas
            ref="canvasRef"
            @mousedown="onMouseDown"
            @mousemove="onMouseMove"
            @mouseup="onMouseUp"
            @mouseleave="onMouseUp"
          />
          <div v-if="!imageLoaded" class="hint-overlay">
            <EmptyOutlined style="font-size: 48px; color: #bbb" />
            <p>请先上传空白卷图片</p>
          </div>
        </div>
        <div class="canvas-tip">
          <InfoCircleOutlined /> 在图片上按住鼠标左键拖动框选每道题的答题区域，松开后右侧自动新增一条标注
        </div>
      </a-col>

      <a-col :xs="24" :lg="8">
        <a-card size="small" title="已标注区域" :bordered="false" class="regions-card">
          <a-empty v-if="!regions.length" description="尚未标注" :image="emptyImage" />
          <a-list v-else :data-source="regions" size="small">
            <template #renderItem="{ item, index }">
              <a-list-item>
                <div class="region-item">
                  <div class="region-row">
                    <a-tag color="blue">第{{ index + 1 }}区</a-tag>
                    <a-tag :color="regionTypeColor(item.region_type)">
                      {{ regionTypeLabel(item.region_type) }}
                    </a-tag>
                    <a-button
                      type="link"
                      danger
                      size="small"
                      @click="removeRegion(index)"
                    >
                      删除
                    </a-button>
                  </div>
                  <a-select
                    v-model:value="item.question_id"
                    size="small"
                    style="width: 100%; margin-top: 4px"
                    placeholder="选择题号"
                    @change="onQuestionChange(item)"
                  >
                    <a-select-option
                      v-for="q in questions"
                      :key="q.id"
                      :value="q.id"
                      :disabled="isQuestionUsed(q.id, index)"
                    >
                      {{ q.order }}. [{{ typeLabel(q.type) }}] {{ truncate(q.content, 24) }}
                    </a-select-option>
                  </a-select>
                  <div class="bbox-text">
                    bbox: ({{ item.bbox.x }}, {{ item.bbox.y }}) {{ item.bbox.w }}×{{ item.bbox.h }}
                  </div>
                </div>
              </a-list-item>
            </template>
          </a-list>
        </a-card>
      </a-col>
    </a-row>
  </a-card>
</template>

<script setup>
import { ref, reactive, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { message, Empty } from 'ant-design-vue'
import {
  InboxOutlined,
  SaveOutlined,
  InfoCircleOutlined,
  FileImageOutlined,
} from '@ant-design/icons-vue'

const props = defineProps({
  examId: { type: Number, required: true },
  questions: { type: Array, default: () => [] },
  existingRegions: { type: Array, default: () => [] },
  blankImageUrl: { type: String, default: '' },
  blankImageSize: { type: Array, default: () => [0, 0] },
})

const emit = defineEmits(['save', 'cancel', 'blank-uploaded'])

const canvasRef = ref(null)
const canvasWrapRef = ref(null)
const imageLoaded = ref(false)
const naturalSize = ref(null) // [width, height] 原图像素
const saving = ref(false)
const emptyImage = Empty.PRESENTED_IMAGE_SIMPLE

// canvas 尺寸（显示尺寸，可能小于原图）
const canvasWidth = ref(0)
const canvasHeight = ref(0)
// 缩放比例 = 原图 / canvas
const scaleX = ref(1)
const scaleY = ref(1)

// 已标注的区域列表（坐标存原图坐标）
// 每项: { question_id, region_type, bbox: {x, y, w, h}, order }
const regions = ref([])

// 当前正在绘制的矩形（屏幕坐标）
const drawing = reactive({
  isDrawing: false,
  startX: 0,
  startY: 0,
  curX: 0,
  curY: 0,
})

let imageObj = null // 缓存的 Image 对象

// ===== 图片加载 =====
function loadImage(url) {
  if (!url) return
  const img = new Image()
  img.crossOrigin = 'anonymous'
  img.onload = () => {
    imageObj = img
    naturalSize.value = [img.naturalWidth, img.naturalHeight]
    setupCanvas()
    redraw()
  }
  img.onerror = () => {
    message.error('图片加载失败')
  }
  img.src = url
}

function setupCanvas() {
  if (!canvasRef.value || !canvasWrapRef.value || !naturalSize.value) return
  const wrapWidth = canvasWrapRef.value.clientWidth
  // 显示宽度 = min(容器宽度, 800px)
  const displayW = Math.min(wrapWidth, 800)
  const ratio = naturalSize.value[1] / naturalSize.value[0]
  const displayH = Math.round(displayW * ratio)
  canvasWidth.value = displayW
  canvasHeight.value = displayH
  scaleX.value = naturalSize.value[0] / displayW
  scaleY.value = naturalSize.value[1] / displayH
  canvasRef.value.width = displayW
  canvasRef.value.height = displayH
  canvasRef.value.style.width = displayW + 'px'
  canvasRef.value.style.height = displayH + 'px'
  imageLoaded.value = true
}

// ===== 重绘 canvas =====
function redraw() {
  const canvas = canvasRef.value
  if (!canvas || !imageObj) return
  const ctx = canvas.getContext('2d')
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  // 绘制底图
  ctx.drawImage(imageObj, 0, 0, canvas.width, canvas.height)

  // 绘制所有已完成矩形（屏幕坐标）
  regions.value.forEach((r, idx) => {
    const sx = r.bbox.x / scaleX.value
    const sy = r.bbox.y / scaleY.value
    const sw = r.bbox.w / scaleX.value
    const sh = r.bbox.h / scaleY.value
    drawRect(ctx, sx, sy, sw, sh, regionTypeColor(r.region_type), idx + 1)
  })

  // 绘制当前正在绘制的矩形
  if (drawing.isDrawing) {
    const x = Math.min(drawing.startX, drawing.curX)
    const y = Math.min(drawing.startY, drawing.curY)
    const w = Math.abs(drawing.curX - drawing.startX)
    const h = Math.abs(drawing.curY - drawing.startY)
    ctx.strokeStyle = '#3751FE'
    ctx.lineWidth = 2
    ctx.setLineDash([6, 4])
    ctx.strokeRect(x, y, w, h)
    ctx.setLineDash([])
    ctx.fillStyle = 'rgba(55, 81, 254, 0.15)'
    ctx.fillRect(x, y, w, h)
  }
}

function drawRect(ctx, x, y, w, h, color, label) {
  ctx.strokeStyle = color
  ctx.lineWidth = 2
  ctx.strokeRect(x, y, w, h)
  ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'
  ctx.fillRect(x, y, w, h)
  // 题号标签
  ctx.fillStyle = color
  ctx.fillRect(x, y - 18, 32, 18)
  ctx.fillStyle = '#fff'
  ctx.font = '12px sans-serif'
  ctx.textBaseline = 'middle'
  ctx.fillText(`#${label}`, x + 4, y - 9)
}

// ===== 鼠标事件 =====
function getCanvasPos(e) {
  const rect = canvasRef.value.getBoundingClientRect()
  return {
    x: e.clientX - rect.left,
    y: e.clientY - rect.top,
  }
}

function onMouseDown(e) {
  if (!imageLoaded.value) return
  const pos = getCanvasPos(e)
  drawing.isDrawing = true
  drawing.startX = pos.x
  drawing.startY = pos.y
  drawing.curX = pos.x
  drawing.curY = pos.y
}

function onMouseMove(e) {
  if (!drawing.isDrawing) return
  const pos = getCanvasPos(e)
  drawing.curX = pos.x
  drawing.curY = pos.y
  redraw()
}

function onMouseUp(e) {
  if (!drawing.isDrawing) return
  drawing.isDrawing = false
  const x = Math.min(drawing.startX, drawing.curX)
  const y = Math.min(drawing.startY, drawing.curY)
  const w = Math.abs(drawing.curX - drawing.startX)
  const h = Math.abs(drawing.curY - drawing.startY)
  // 过滤太小的矩形（误点击）
  if (w < 10 || h < 10) {
    redraw()
    return
  }
  // 换算为原图坐标
  const realX = Math.round(x * scaleX.value)
  const realY = Math.round(y * scaleY.value)
  const realW = Math.round(w * scaleX.value)
  const realH = Math.round(h * scaleY.value)

  // 自动选下一道未标注的题
  const nextQuestion = pickNextQuestion()
  const region = {
    question_id: nextQuestion ? nextQuestion.id : null,
    region_type: nextQuestion ? inferRegionType(nextQuestion.type) : 'bubble',
    bbox: { x: realX, y: realY, w: realW, h: realH },
    order: regions.value.length + 1,
  }
  regions.value.push(region)
  redraw()
}

function pickNextQuestion() {
  const usedIds = new Set(
    regions.value.map(r => r.question_id).filter(id => id !== null)
  )
  // 按 order 顺序找第一个未标注的
  const sorted = [...props.questions].sort((a, b) => (a.order || 0) - (b.order || 0))
  return sorted.find(q => !usedIds.has(q.id)) || null
}

function isQuestionUsed(qid, currentIndex) {
  return regions.value.some((r, idx) => idx !== currentIndex && r.question_id === qid)
}

function inferRegionType(qType) {
  if (qType === 'fill') return 'fill'
  if (qType === 'essay') return 'essay'
  return 'bubble' // single / multi / judge
}

function onQuestionChange(item) {
  // 切换题号时，根据题型自动调整 region_type（如未手动改过）
  const q = props.questions.find(qq => qq.id === item.question_id)
  if (q) {
    item.region_type = inferRegionType(q.type)
  }
  redraw()
}

function removeRegion(index) {
  regions.value.splice(index, 1)
  // 重排序号
  regions.value.forEach((r, i) => (r.order = i + 1))
  redraw()
}

function clearAll() {
  regions.value = []
  redraw()
}

// ===== 上传空白卷 =====
function handleBlankUpload(file) {
  const reader = new FileReader()
  reader.onload = (e) => {
    const dataUrl = e.target.result
    // 获取原始尺寸
    const img = new Image()
    img.onload = () => {
      naturalSize.value = [img.naturalWidth, img.naturalHeight]
      // 通知父组件文件已上传（父组件用于保存时提交 FormData）
      emit('blank-uploaded', file, dataUrl, [img.naturalWidth, img.naturalHeight])
      // 加载到 canvas
      loadImage(dataUrl)
      // 清空已有标注（新空白卷，旧标注失效）
      regions.value = []
    }
    img.src = dataUrl
  }
  reader.readAsDataURL(file)
  return false // 阻止自动上传
}

// ===== 保存 =====
async function emitSave() {
  if (!regions.value.length) {
    message.warning('请至少标注一个区域')
    return
  }
  // 校验所有区域都选择题号
  const noQ = regions.value.filter(r => !r.question_id)
  if (noQ.length) {
    message.warning(`有 ${noQ.length} 个区域未选择题号，请先选择题号再保存`)
    return
  }
  saving.value = true
  try {
    // 重新排序号
    const payload = regions.value.map((r, i) => ({
      question_id: r.question_id,
      region_type: r.region_type,
      bbox: r.bbox,
      order: i + 1,
    }))
    emit('save', payload)
  } finally {
    saving.value = false
  }
}

// ===== 工具函数 =====
function typeLabel(type) {
  const m = { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '大题' }
  return m[type] || type
}

function regionTypeLabel(type) {
  const m = { bubble: '选择题', fill: '填空', essay: '大题' }
  return m[type] || type
}

function regionTypeColor(type) {
  const m = { bubble: '#3751FE', fill: '#fa8c16', essay: '#722ed1' }
  return m[type] || '#3751FE'
}

function truncate(s, n) {
  if (!s) return ''
  return s.length > n ? s.slice(0, n) + '...' : s
}

// ===== 编辑模式：加载已有模板 =====
function loadExistingRegions() {
  if (!props.existingRegions || !props.existingRegions.length) return
  regions.value = props.existingRegions.map((r, i) => ({
    question_id: r.question_id,
    region_type: r.region_type,
    bbox: r.bbox, // 已是原图坐标
    order: r.order || i + 1,
  }))
  redraw()
}

// ===== 监听 =====
watch(
  () => props.blankImageUrl,
  (url) => {
    if (url) {
      nextTick(() => loadImage(url))
    }
  },
  { immediate: true }
)

watch(
  () => props.existingRegions,
  () => {
    if (imageLoaded.value) {
      loadExistingRegions()
    } else {
      // 等图片加载后再回填
      nextTick(() => {
        setTimeout(loadExistingRegions, 300)
      })
    }
  },
  { immediate: true, deep: true }
)

// 窗口 resize 重新计算 canvas
let resizeTimer = null
function handleResize() {
  if (!imageLoaded.value || !naturalSize.value) return
  clearTimeout(resizeTimer)
  resizeTimer = setTimeout(() => {
    setupCanvas()
    redraw()
  }, 200)
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize)
  if (resizeTimer) clearTimeout(resizeTimer)
})
</script>

<style scoped>
.template-editor {
  margin-top: 16px;
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
}

.toolbar {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.blank-uploader {
  flex: 1;
  min-width: 280px;
}

.blank-uploader :deep(.ant-upload.ant-upload-drag) {
  border-radius: 8px;
}

.upload-hint {
  padding: 12px 0;
  text-align: center;
}

.upload-hint .anticon {
  font-size: 28px;
  color: #3751FE;
  margin-bottom: 6px;
}

.upload-text {
  font-size: 13px;
  color: #1a1a2e;
  margin: 4px 0 2px;
}

.upload-sub {
  font-size: 12px;
  color: #999;
  margin: 0;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: stretch;
  min-width: 200px;
}

.main-row {
  margin-top: 8px;
}

.canvas-wrap {
  position: relative;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  background: #fafafa;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 8px;
  min-height: 300px;
  overflow: auto;
}

.canvas-wrap canvas {
  cursor: crosshair;
  display: block;
  max-width: 100%;
}

.hint-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #999;
  pointer-events: none;
}

.hint-overlay p {
  margin-top: 8px;
  font-size: 13px;
}

.canvas-tip {
  margin-top: 8px;
  font-size: 12px;
  color: #888;
  line-height: 1.5;
}

.regions-card {
  max-height: 600px;
  overflow-y: auto;
}

.region-item {
  width: 100%;
}

.region-row {
  display: flex;
  align-items: center;
  gap: 4px;
  flex-wrap: wrap;
}

.bbox-text {
  font-size: 11px;
  color: #999;
  margin-top: 4px;
  font-family: monospace;
}
</style>
