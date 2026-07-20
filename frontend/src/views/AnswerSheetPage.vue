<template>
  <div class="cv-page answer-sheet-page" style="padding: 24px">
    <a-page-header
      title="答题卡扫描批改"
      sub-title="试卷模板标注 · 整卷扫描 · AI 自动批改"
      style="padding: 0 0 16px 0"
    />

    <a-tabs v-model:activeKey="activeTab" type="card">
      <!-- ============ Tab 1: 试卷模板管理 ============ -->
      <a-tab-pane key="template" tab="试卷模板管理">
        <a-card :bordered="false" class="section-card">
          <a-form layout="vertical">
            <a-form-item label="选择考试">
              <a-select
                v-model:value="selectedExamId"
                placeholder="请选择要配置模板的考试"
                style="width: 100%; max-width: 600px"
                :loading="loadingExams"
                @change="onExamChange"
              >
                <a-select-option
                  v-for="e in exams"
                  :key="e.id"
                  :value="e.id"
                  :disabled="e.question_count === 0"
                >
                  {{ e.title }}
                  <a-tag
                    :color="e.has_template ? 'green' : 'default'"
                    size="small"
                    style="margin-left: 8px"
                  >
                    {{ e.has_template ? '已配置' : '未配置' }}
                  </a-tag>
                  <span style="color: #999; margin-left: 8px">
                    ({{ e.question_count }}题, {{ e.total_score }}分)
                  </span>
                </a-select-option>
              </a-select>
            </a-form-item>

            <a-alert
              v-if="selectedExamId && !questions.length"
              type="info"
              show-icon
              message="该考试暂无题目，请先在「考试管理」中添加题目"
              style="margin-bottom: 12px"
            />

            <div v-if="templateInfo" class="template-status">
              <a-alert type="success" show-icon style="margin-bottom: 12px">
                <template #message>
                  已有模板配置：{{ templateInfo.regions.length }} 个区域标注
                  <a-button
                    type="link"
                    size="small"
                    danger
                    @click="handleDeleteTemplate"
                    :loading="deletingTemplate"
                  >
                    删除模板
                  </a-button>
                </template>
              </a-alert>
            </div>
          </a-form>
        </a-card>

        <!-- 快捷操作：一键生成模板（按预设布局自动生成区域） -->
        <div v-if="selectedExamId && questions.length" class="quick-actions">
          <a-button
            type="primary"
            ghost
            @click="showBatchTemplateModal = true"
          >
            <template #icon><ThunderboltOutlined /></template>
            一键生成模板（自动布局）
          </a-button>
          <span class="hint-text">
            免去手工拖框，按预设布局自动生成区域；生成后仍可在编辑器中微调
          </span>
        </div>

        <!-- 模板编辑器（选择考试且有题目后展示） -->
        <PaperTemplateEditor
          v-if="selectedExamId && questions.length"
          :examId="selectedExamId"
          :questions="questions"
          :existingRegions="existingRegions"
          :blankImageUrl="blankImageUrl"
          :blankImageSize="blankImageSize"
          @save="handleSaveTemplate"
          @blank-uploaded="onBlankUploaded"
        />
      </a-tab-pane>

      <!-- ============ Tab 2: 扫描批改 ============ -->
      <a-tab-pane key="scan" tab="扫描批改">
        <a-card :bordered="false" class="section-card" title="扫描参数">
          <a-form layout="vertical">
            <a-row :gutter="16">
              <a-col :xs="24" :md="12">
                <a-form-item label="选择考试（仅显示已配置模板的考试）">
                  <a-select
                    v-model:value="scanForm.examId"
                    placeholder="请选择考试"
                    style="width: 100%"
                    :loading="loadingExams"
                    @change="onScanExamChange"
                  >
                    <a-select-option
                      v-for="e in scannableExams"
                      :key="e.id"
                      :value="e.id"
                    >
                      {{ e.title }} ({{ e.question_count }}题)
                    </a-select-option>
                  </a-select>
                  <div v-if="!scannableExams.length" class="hint-text">
                    暂无已配置模板的考试，请先在「试卷模板管理」Tab 配置模板
                  </div>
                </a-form-item>
              </a-col>

              <a-col :xs="24" :md="12">
                <a-form-item label="学生 ID">
                  <a-input-number
                    v-model:value="scanForm.studentId"
                    :min="1"
                    placeholder="输入学生用户ID"
                    style="width: 100%"
                  />
                  <div class="hint-text">输入学生的注册ID（RegisteredPerson.id）</div>
                </a-form-item>
              </a-col>
            </a-row>

            <a-form-item label="上传整卷扫描件">
              <a-upload-dragger
                :before-upload="handleScanUpload"
                :show-upload-list="false"
                accept="image/png,image/jpeg,image/jpg,image/bmp,image/webp"
                :multiple="false"
              >
                <div class="upload-hint">
                  <p class="ant-upload-drag-icon">
                    <InboxOutlined />
                  </p>
                  <p class="upload-text">点击或拖拽上传整卷扫描件</p>
                  <p class="upload-sub">JPG / PNG / BMP / WebP</p>
                </div>
              </a-upload-dragger>
              <div v-if="scanFile" class="scan-file-info">
                <PaperClipOutlined />
                {{ scanFile.name }} ({{ (scanFile.size / 1024).toFixed(1) }} KB)
                <a-button type="link" danger size="small" @click="scanFile = null">
                  移除
                </a-button>
              </div>
            </a-form-item>

            <a-form-item>
              <a-button
                type="primary"
                size="large"
                :loading="scanning"
                :disabled="!canScan"
                @click="doScan"
              >
                <template #icon><ScanOutlined /></template>
                开始扫描批改
              </a-button>
              <span v-if="!canScan" class="hint-text" style="margin-left: 12px">
                请选择考试 + 输入学生ID + 上传扫描件
              </span>
            </a-form-item>
          </a-form>
        </a-card>

        <!-- 扫描进度 -->
        <ScanProgressSteps
          v-if="scanning || scanResult || scanError"
          :current="scanStep"
          :status="scanStatus"
        />

        <!-- 扫描结果 -->
        <ScanReportPanel v-if="scanResult" :result="scanResult" />

        <!-- 错误提示 -->
        <a-alert
          v-if="scanError"
          type="error"
          show-icon
          :message="scanError"
          style="margin-top: 12px"
        />
      </a-tab-pane>

      <!-- ============ Tab 3: 调试工具 ============ -->
      <a-tab-pane key="debug" tab="气泡检测调试">
        <a-card :bordered="false" class="section-card" title="独立气泡检测">
          <a-alert
            type="info"
            show-icon
            message="本工具用于单独测试答题卡气泡检测，不上传数据库。可直接上传一张答题卡图片查看检测结果。"
            style="margin-bottom: 12px"
          />
          <a-form layout="vertical">
            <a-form-item label="模板类型">
              <a-radio-group v-model:value="debugForm.templateType">
                <a-radio value="standard_5x10x4">标准 5×10×4（5列×10题×4选项）</a-radio>
                <a-radio value="generic">通用检测（Phase 4 预留）</a-radio>
              </a-radio-group>
            </a-form-item>

            <a-form-item label="上传答题卡图片">
              <a-upload-dragger
                :before-upload="handleDebugUpload"
                :show-upload-list="false"
                accept="image/*"
              >
                <div class="upload-hint">
                  <p class="ant-upload-drag-icon"><InboxOutlined /></p>
                  <p class="upload-text">点击或拖拽上传答题卡图片</p>
                </div>
              </a-upload-dragger>
            </a-form-item>

            <a-form-item>
              <a-button
                type="primary"
                :loading="detecting"
                :disabled="!debugFile"
                @click="doDetect"
              >
                <template #icon><SearchOutlined /></template>
                开始检测
              </a-button>
            </a-form-item>
          </a-form>

          <!-- 检测结果 -->
          <div v-if="detectResult" class="debug-result">
            <a-row :gutter="16">
              <a-col :xs="24" :md="12">
                <a-card size="small" title="检测结果" :bordered="false">
                  <a-descriptions size="small" :column="1" bordered>
                    <a-descriptions-item label="模板类型">
                      {{ detectResult.template_type }}
                    </a-descriptions-item>
                    <a-descriptions-item label="倾斜角度">
                      {{ (detectResult.skew_angle || 0).toFixed(2) }}°
                    </a-descriptions-item>
                    <a-descriptions-item label="检测气泡数">
                      {{ detectResult.bubbles_count }}
                    </a-descriptions-item>
                    <a-descriptions-item label="已填涂气泡">
                      {{ detectResult.filled_count }}
                    </a-descriptions-item>
                  </a-descriptions>

                  <div class="answers-list">
                    <div class="section-title">识别到的答案</div>
                    <a-tag
                      v-for="(opts, qIdx) in detectResult.answers"
                      :key="qIdx"
                      color="blue"
                      style="margin: 2px"
                    >
                      Q{{ parseInt(qIdx) + 1 }}: {{ opts.map(o => String.fromCharCode(65 + o)).join(',') }}
                    </a-tag>
                    <a-empty
                      v-if="!Object.keys(detectResult.answers || {}).length"
                      description="未识别到填涂"
                      :image="simpleImage"
                    />
                  </div>
                </a-card>
              </a-col>

              <a-col :xs="24" :md="12">
                <a-card size="small" title="检测可视化" :bordered="false">
                  <div v-if="detectResult.debug_image_b64" class="debug-image-wrap">
                    <img
                      :src="`data:image/png;base64,${detectResult.debug_image_b64}`"
                      alt="检测可视化"
                    />
                  </div>
                  <a-empty v-else description="无可视化图" :image="simpleImage" />
                </a-card>
              </a-col>
            </a-row>
          </div>
        </a-card>
      </a-tab-pane>

      <!-- ============ Tab 4: 批量扫描批改 ============ -->
      <a-tab-pane key="batch" tab="批量扫描批改">
        <a-alert
          type="info"
          show-icon
          message="批量扫描批改：一次上传多份答卷 + 对应学生 ID，顺序批改，单个失败不阻塞其他。批改完成后可一键批量导出 Excel 报告（ZIP 包）。"
          style="margin-bottom: 12px"
        />
        <BatchScanPanel />
      </a-tab-pane>
    </a-tabs>

    <!-- 一键生成模板 Modal（B 方案） -->
    <BatchTemplateGenerate
      v-model:open="showBatchTemplateModal"
      :examId="selectedExamId"
      @success="handleBatchTemplateSuccess"
    />
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { message, Empty } from 'ant-design-vue'
import {
  InboxOutlined,
  ScanOutlined,
  SearchOutlined,
  PaperClipOutlined,
  ThunderboltOutlined,
} from '@ant-design/icons-vue'
import PaperTemplateEditor from '@/components/answer-sheet/PaperTemplateEditor.vue'
import ScanProgressSteps from '@/components/answer-sheet/ScanProgressSteps.vue'
import ScanReportPanel from '@/components/answer-sheet/ScanReportPanel.vue'
import BatchTemplateGenerate from '@/components/answer-sheet/BatchTemplateGenerate.vue'
import BatchScanPanel from '@/components/answer-sheet/BatchScanPanel.vue'
import {
  listScannableExams,
  listExamQuestions,
  getPaperTemplate,
  savePaperTemplate,
  deletePaperTemplate,
  scanAndGrade,
  detectBubbles,
} from '@/api/answerSheet'

const simpleImage = Empty.PRESENTED_IMAGE_SIMPLE

const activeTab = ref('template')

// ===== Tab 1: 模板管理 =====
const exams = ref([])
const loadingExams = ref(false)
const selectedExamId = ref(null)
const questions = ref([])
const templateInfo = ref(null)
const existingRegions = ref([])
const blankImageUrl = ref('')
const blankImageSize = ref([0, 0])
const deletingTemplate = ref(false)

// 当前上传的空白卷文件（PaperTemplateEditor emit blank-uploaded 时记录）
const currentBlankFile = ref(null)

// 一键生成模板 Modal 开关（B 方案）
const showBatchTemplateModal = ref(false)

// ===== Tab 2: 扫描批改 =====
const scanForm = reactive({ examId: null, studentId: null })
const scanFile = ref(null)
const scanning = ref(false)
const scanResult = ref(null)
const scanError = ref('')
const scanStep = ref(0)

const scannableExams = computed(() => exams.value.filter(e => e.has_template))

const canScan = computed(
  () => scanForm.examId && scanForm.studentId && scanFile.value && !scanning.value
)

const scanStatus = computed(() => {
  if (scanError.value) return 'error'
  if (scanResult.value) return 'finish'
  return 'process'
})

// ===== Tab 3: 调试 =====
const debugForm = reactive({ templateType: 'standard_5x10x4' })
const debugFile = ref(null)
const detecting = ref(false)
const detectResult = ref(null)

// ============ 加载考试列表 ============
async function loadExams() {
  loadingExams.value = true
  try {
    const res = await listScannableExams()
    exams.value = res.data || []
  } catch (e) {
    message.error('加载考试列表失败：' + (e.response?.data?.detail || e.message))
  } finally {
    loadingExams.value = false
  }
}

// ============ 选择考试 ============
async function onExamChange(examId) {
  if (!examId) return
  templateInfo.value = null
  existingRegions.value = []
  blankImageUrl.value = ''
  blankImageSize.value = [0, 0]
  questions.value = []
  currentBlankFile.value = null

  try {
    // 并行加载题目和模板
    const [qRes, tRes] = await Promise.all([
      listExamQuestions(examId),
      getPaperTemplate(examId).catch(() => null),
    ])
    questions.value = qRes.data || []

    if (tRes && tRes.data) {
      templateInfo.value = tRes.data
      existingRegions.value = tRes.data.regions || []
      // blank_image_url 是后端相对路径 /uploads/...，前端走 axios 代理直接拼接
      blankImageUrl.value = tRes.data.blank_image_url || ''
      blankImageSize.value = tRes.data.blank_image_size || [0, 0]
    }
  } catch (e) {
    message.error('加载考试数据失败：' + (e.response?.data?.detail || e.message))
  }
}

// ============ PaperTemplateEditor 事件 ============
function onBlankUploaded(file, dataUrl, naturalSize) {
  currentBlankFile.value = file
  // 编辑器内部已自行加载图片，这里只保存文件对象供后续上传
}

async function handleSaveTemplate(regions) {
  if (!selectedExamId.value) {
    message.warning('请先选择考试')
    return
  }
  if (!currentBlankFile.value && !blankImageUrl.value) {
    message.warning('请先上传空白卷图片')
    return
  }
  try {
    // 若编辑器中用户没上传新文件，复用已有 blankImageUrl（编辑模式无新上传时）
    const blankFile = currentBlankFile.value || await urlToFile(blankImageUrl.value)
    if (!blankFile) {
      message.error('空白卷文件获取失败')
      return
    }
    const res = await savePaperTemplate({
      examId: selectedExamId.value,
      blankFile,
      regions,
    })
    message.success(`模板保存成功：${regions.length} 个区域，模板ID=${res.data.template_id}`)
    // 重新加载模板信息
    await onExamChange(selectedExamId.value)
    // 刷新考试列表的 has_template 状态
    await loadExams()
  } catch (e) {
    message.error('保存模板失败：' + (e.response?.data?.detail || e.message))
  }
}

async function handleDeleteTemplate() {
  if (!selectedExamId.value) return
  deletingTemplate.value = true
  try {
    await deletePaperTemplate(selectedExamId.value)
    message.success('模板已删除')
    await onExamChange(selectedExamId.value)
    await loadExams()
  } catch (e) {
    message.error('删除模板失败：' + (e.response?.data?.detail || e.message))
  } finally {
    deletingTemplate.value = false
  }
}

// ============ 一键生成模板（B 方案）成功回调 ============
async function handleBatchTemplateSuccess(result) {
  // result: { template_id, exam_id, regions_count, layout, grid, image_size, regions }
  message.success(`模板自动生成成功：${result.regions_count} 个区域，模板ID=${result.template_id}`)
  // 刷新模板状态 + 考试列表的 has_template
  await onExamChange(selectedExamId.value)
  await loadExams()
}

// 把后端返回的 URL 转为 File 对象（编辑模式无新上传时复用）
async function urlToFile(url) {
  if (!url) return null
  try {
    const resp = await fetch(url)
    const blob = await resp.blob()
    const filename = url.split('/').pop() || 'blank.png'
    return new File([blob], filename, { type: blob.type || 'image/png' })
  } catch (e) {
    return null
  }
}

// ============ 扫描批改 ============
function onScanExamChange() {
  scanResult.value = null
  scanError.value = ''
}

function handleScanUpload(file) {
  scanFile.value = file
  scanResult.value = null
  scanError.value = ''
  return false
}

async function doScan() {
  if (!canScan.value) return
  scanning.value = true
  scanResult.value = null
  scanError.value = ''
  scanStep.value = 0

  // 模拟步骤推进（实际后端是一次性返回，这里做 UI 进度感）
  const stepTimer = setInterval(() => {
    if (scanStep.value < 3) scanStep.value++
  }, 800)

  try {
    const res = await scanAndGrade({
      examId: scanForm.examId,
      file: scanFile.value,
      studentId: scanForm.studentId,
    })
    scanStep.value = 4
    scanResult.value = res.data
    message.success('扫描批改完成')
  } catch (e) {
    scanError.value = e.response?.data?.detail || e.message || '扫描失败'
    message.error('扫描批改失败：' + scanError.value)
  } finally {
    clearInterval(stepTimer)
    scanning.value = false
  }
}

// ============ 调试 Tab ============
function handleDebugUpload(file) {
  debugFile.value = file
  detectResult.value = null
  return false
}

async function doDetect() {
  if (!debugFile.value) return
  detecting.value = true
  detectResult.value = null
  try {
    const res = await detectBubbles({
      file: debugFile.value,
      templateType: debugForm.templateType,
    })
    detectResult.value = res.data
    message.success('检测完成')
  } catch (e) {
    message.error('检测失败：' + (e.response?.data?.detail || e.message))
  } finally {
    detecting.value = false
  }
}

// ============ 生命周期 ============
onMounted(() => {
  loadExams()
})
</script>

<style scoped>
.answer-sheet-page {
  background: #f5f6fa;
  min-height: 100vh;
}

.section-card {
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
  margin-bottom: 16px;
}

.template-status {
  margin-top: 8px;
}

.quick-actions {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #f0f5ff;
  border: 1px dashed #adc6ff;
  border-radius: 8px;
  padding: 10px 14px;
  margin: 12px 0 16px;
}

.quick-actions .hint-text {
  margin-top: 0;
  font-size: 12px;
  color: #666;
  flex: 1;
}

.upload-hint {
  padding: 16px 0;
  text-align: center;
}

.upload-hint .ant-upload-drag-icon {
  color: #3751FE;
  font-size: 32px;
  margin-bottom: 4px;
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

.scan-file-info {
  margin-top: 8px;
  font-size: 13px;
  color: #555;
  background: #f6f8ff;
  padding: 6px 10px;
  border-radius: 6px;
}

.hint-text {
  font-size: 12px;
  color: #999;
  margin-top: 4px;
}

.debug-result {
  margin-top: 16px;
}

.debug-image-wrap {
  text-align: center;
  background: #fafafa;
  padding: 8px;
  border-radius: 6px;
}

.debug-image-wrap img {
  max-width: 100%;
  border-radius: 4px;
}

.answers-list {
  margin-top: 12px;
}

.section-title {
  font-size: 13px;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 6px;
}
</style>
