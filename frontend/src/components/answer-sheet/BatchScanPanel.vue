<template>
  <div class="batch-scan-panel">
    <a-card :bordered="false" class="section-card" title="批量扫描批改">
      <a-alert
        type="info"
        show-icon
        message="一次上传多份学生答卷，系统顺序批改，单个失败不阻塞其他学生。单批最多 50 份。"
        style="margin-bottom: 16px"
      />

      <a-form layout="vertical">
        <a-form-item label="选择考试（仅显示已配置模板的考试）" required>
          <a-select
            v-model:value="batchForm.examId"
            placeholder="请选择考试"
            style="width: 100%; max-width: 600px"
            :loading="loadingExams"
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

        <a-form-item label="上传多份答卷" required>
          <a-upload-dragger
            :before-upload="handleBatchUpload"
            :show-upload-list="false"
            accept="image/png,image/jpeg,image/jpg,image/bmp,image/webp"
            :multiple="true"
          >
            <div>
              <p class="ant-upload-drag-icon"><InboxOutlined /></p>
              <p class="upload-text">点击或拖拽上传多份答卷（可多选）</p>
              <p class="upload-sub">JPG / PNG / BMP / WebP，最多 50 份</p>
            </div>
          </a-upload-dragger>
        </a-form-item>

        <!-- 文件列表 + 学生 ID 配对 -->
        <div v-if="pairs.length" class="pairs-section">
          <div class="pairs-header">
            <span>共 {{ pairs.length }} 份答卷，请为每份指定学生 ID</span>
            <a-button type="link" size="small" @click="autoFillStudentIds">
              <SnippetsOutlined />
              从文件名提取数字自动填充
            </a-button>
            <a-button type="link" danger size="small" @click="pairs = []">
              <DeleteOutlined />
              清空
            </a-button>
          </div>
          <a-table
            :data-source="pairs"
            :columns="pairColumns"
            :pagination="false"
            size="small"
            row-key="rowKey"
            bordered
          >
            <template #bodyCell="{ column, record, index }">
              <template v-if="column.dataIndex === 'index'">{{ index + 1 }}</template>
              <template v-else-if="column.dataIndex === 'fileName'">
                <span class="file-name">{{ record.fileName }}</span>
                <span class="file-size">({{ (record.file.size / 1024).toFixed(1) }} KB)</span>
              </template>
              <template v-else-if="column.dataIndex === 'studentId'">
                <a-input-number
                  v-model:value="record.studentId"
                  :min="1"
                  placeholder="学生 ID"
                  style="width: 100%"
                />
              </template>
              <template v-else-if="column.dataIndex === 'action'">
                <a-button type="link" danger size="small" @click="removePair(index)">
                  移除
                </a-button>
              </template>
            </template>
          </a-table>
        </div>

        <a-form-item style="margin-top: 16px">
          <a-button
            type="primary"
            size="large"
            :loading="batchScanning"
            :disabled="!canBatchScan"
            @click="doBatchScan"
          >
            <template #icon><ScanOutlined /></template>
            开始批量批改（{{ pairs.length }} 份）
          </a-button>
          <span v-if="!canBatchScan && pairs.length" class="hint-text" style="margin-left: 12px">
            请确保所有学生 ID 已填写
          </span>
        </a-form-item>
      </a-form>
    </a-card>

    <!-- 批量结果汇总 -->
    <a-card
      v-if="batchResult"
      :bordered="false"
      class="section-card"
      style="margin-top: 16px"
      title="批量批改结果"
    >
      <a-row :gutter="16" style="margin-bottom: 16px">
        <a-col :span="6">
          <a-statistic title="总数" :value="batchResult.total" />
        </a-col>
        <a-col :span="6">
          <a-statistic title="成功" :value="batchResult.success" :value-style="{ color: '#3f8600' }" />
        </a-col>
        <a-col :span="6">
          <a-statistic title="失败" :value="batchResult.failed" :value-style="{ color: '#cf1322' }" />
        </a-col>
        <a-col :span="6" style="text-align: right">
          <a-button
            type="primary"
            :loading="downloadingZip"
            :disabled="!successfulSubmissionIds.length"
            @click="downloadBatchReports"
          >
            <template #icon><DownloadOutlined /></template>
            批量下载报告（ZIP，{{ successfulSubmissionIds.length }} 份）
          </a-button>
        </a-col>
      </a-row>

      <a-table
        :data-source="batchResult.results"
        :columns="resultColumns"
        :pagination="{ pageSize: 20 }"
        size="small"
        row-key="student_id"
        bordered
      >
        <template #bodyCell="{ column, record }">
          <template v-if="column.dataIndex === 'student'">
            {{ record.student_name }}
            <span style="color: #999">（ID: {{ record.student_id }}）</span>
          </template>
          <template v-else-if="column.dataIndex === 'score'">
            <span v-if="record.success" style="color: #3f8600; font-weight: bold">
              {{ record.total_score }} / {{ record.max_score }}
            </span>
            <span v-else style="color: #cf1322">—</span>
          </template>
          <template v-else-if="column.dataIndex === 'status'">
            <a-tag :color="record.success ? 'green' : 'red'">
              {{ record.success ? '成功' : '失败' }}
            </a-tag>
          </template>
          <template v-else-if="column.dataIndex === 'error'">
            <a-tooltip v-if="record.error" :title="record.error">
              <span style="color: #cf1322">{{ truncateError(record.error) }}</span>
            </a-tooltip>
            <span v-else style="color: #999">—</span>
          </template>
          <template v-else-if="column.dataIndex === 'action'">
            <a-button
              v-if="record.success"
              type="link"
              size="small"
              @click="downloadSingleReport(record.submission_id, record.student_name)"
            >
              下载 Excel
            </a-button>
          </template>
        </template>
      </a-table>
    </a-card>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import {
  InboxOutlined,
  ScanOutlined,
  DownloadOutlined,
  SnippetsOutlined,
  DeleteOutlined,
} from '@ant-design/icons-vue'
import {
  listScannableExams,
  scanBatch,
  exportExcelBatch,
  exportExcelReport,
} from '@/api/answerSheet'

const exams = ref([])
const loadingExams = ref(false)
const batchForm = reactive({ examId: null })
const pairs = ref([])  // [{rowKey, file, fileName, studentId}]
const batchScanning = ref(false)
const batchResult = ref(null)
const downloadingZip = ref(false)

const scannableExams = computed(() => exams.value.filter(e => e.has_template))

const canBatchScan = computed(() => {
  return (
    batchForm.examId &&
    pairs.value.length > 0 &&
    pairs.value.every(p => p.studentId) &&
    !batchScanning.value
  )
})

const pairColumns = [
  { title: '#', dataIndex: 'index', width: 50 },
  { title: '文件名', dataIndex: 'fileName' },
  { title: '学生 ID', dataIndex: 'studentId', width: 160 },
  { title: '操作', dataIndex: 'action', width: 80 },
]

const resultColumns = [
  { title: '学生', dataIndex: 'student' },
  { title: '文件名', dataIndex: 'file_name', width: 200 },
  { title: '得分', dataIndex: 'score', width: 120 },
  { title: '状态', dataIndex: 'status', width: 90 },
  { title: '错误信息', dataIndex: 'error', width: 250 },
  { title: '操作', dataIndex: 'action', width: 110 },
]

const successfulSubmissionIds = computed(() => {
  if (!batchResult.value) return []
  return batchResult.value.results
    .filter(r => r.success && r.submission_id)
    .map(r => r.submission_id)
})

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

function handleBatchUpload(file) {
  // 限制 50 份
  if (pairs.value.length >= 50) {
    message.warning('单批最多 50 份答卷')
    return false
  }
  pairs.value.push({
    rowKey: Date.now() + '_' + Math.random(),
    file,
    fileName: file.name,
    studentId: null,
  })
  return false  // 阻止自动上传
}

function removePair(index) {
  pairs.value.splice(index, 1)
}

function autoFillStudentIds() {
  let filled = 0
  pairs.value.forEach((p) => {
    // 从文件名提取数字（如 "2024001_张三.jpg" → 2024001，但需为合理的 ID）
    const match = p.fileName.match(/(\d+)/)
    if (match) {
      // 文件名中的数字可能是学号，不是 RegisteredPerson.id
      // 这里仅作为参考填充，用户需手动确认
      p.studentId = parseInt(match[1], 10)
      filled += 1
    }
  })
  if (filled > 0) {
    message.info(`已从文件名提取 ${filled} 个数字作为学生 ID，请核对（文件名中的数字可能是学号而非用户 ID）`)
  } else {
    message.warning('未从文件名中识别到数字，请手动填写')
  }
}

async function doBatchScan() {
  if (!canBatchScan.value) return
  batchScanning.value = true
  batchResult.value = null
  try {
    const res = await scanBatch({
      examId: batchForm.examId,
      files: pairs.value.map(p => p.file),
      studentIds: pairs.value.map(p => p.studentId),
    })
    batchResult.value = res.data
    const r = res.data
    if (r.failed > 0) {
      message.warning(`批量批改完成：${r.success} 成功 / ${r.failed} 失败`)
    } else {
      message.success(`批量批改完成：${r.success} 份全部成功`)
    }
  } catch (e) {
    message.error('批量批改失败：' + (e.response?.data?.detail || e.message))
  } finally {
    batchScanning.value = false
  }
}

async function downloadBatchReports() {
  const ids = successfulSubmissionIds.value
  if (!ids.length) {
    message.warning('没有可下载的报告')
    return
  }
  downloadingZip.value = true
  try {
    const res = await exportExcelBatch(ids)
    // 从响应 header 提取批量统计
    const total = res.headers['x-batch-total'] || ids.length
    const success = res.headers['x-batch-success'] || ids.length
    const failed = res.headers['x-batch-failed'] || 0
    const failedDetail = res.headers['x-batch-failed-detail']

    // 触发下载
    const blob = new Blob([res.data], { type: 'application/zip' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `答题卡报告_batch_${new Date().toISOString().slice(0, 19).replace(/[:-]/g, '')}.zip`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)

    if (failed > 0) {
      message.warning(`ZIP 已下载：${success}/${total} 份成功${failedDetail ? '，失败: ' + failedDetail : ''}`)
    } else {
      message.success(`ZIP 已下载：${success} 份报告`)
    }
  } catch (e) {
    message.error('批量下载失败：' + (e.response?.data?.detail || e.message))
  } finally {
    downloadingZip.value = false
  }
}

async function downloadSingleReport(submissionId, studentName) {
  try {
    const res = await exportExcelReport(submissionId)
    const blob = new Blob([res.data], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    const safeName = (studentName || '').replace(/[\\/:*?"<>|]/g, '_')
    a.download = `答题卡报告_${safeName}_${submissionId}.xlsx`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
    message.success('Excel 已下载')
  } catch (e) {
    message.error('下载失败：' + (e.response?.data?.detail || e.message))
  }
}

function truncateError(err) {
  if (!err) return ''
  return err.length > 50 ? err.slice(0, 50) + '…' : err
}

onMounted(() => {
  loadExams()
})
</script>

<style scoped>
.batch-scan-panel .section-card {
  margin-bottom: 0;
}
.hint-text {
  font-size: 12px;
  color: #999;
  margin-top: 4px;
}
.pairs-section {
  margin-top: 12px;
  padding: 12px;
  background: #fafafa;
  border-radius: 4px;
}
.pairs-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
  font-size: 13px;
  color: #666;
}
.file-name {
  font-weight: 500;
}
.file-size {
  color: #999;
  margin-left: 6px;
  font-size: 12px;
}
.upload-text {
  font-size: 14px;
  color: #333;
}
.upload-sub {
  font-size: 12px;
  color: #999;
}
</style>
