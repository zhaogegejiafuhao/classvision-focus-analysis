<template>
  <a-modal
    :open="open"
    title="一键生成试卷模板"
    width="640px"
    :confirm-loading="loading"
    :ok-text="loading ? '生成中…' : '生成模板'"
    cancel-text="取消"
    @ok="handleGenerate"
    @cancel="handleCancel"
  >
    <a-alert
      type="info"
      show-icon
      message="上传空白卷 + 选择布局，系统自动按布局为该考试的所有题目生成区域标注，免去手工逐题拖框。"
      style="margin-bottom: 16px"
    />

    <a-form layout="vertical">
      <a-form-item label="选择布局" required>
        <a-radio-group v-model:value="form.layout">
          <a-radio
            v-for="opt in layoutOptions"
            :key="opt.value"
            :value="opt.value"
            style="display: block; margin-bottom: 6px"
          >
            {{ opt.label }}
            <span style="color: #999; margin-left: 6px">{{ opt.desc }}</span>
          </a-radio>
        </a-radio-group>
      </a-form-item>

      <a-form-item label="上传空白卷" required>
        <a-upload-dragger
          :before-upload="handleFileSelected"
          :show-upload-list="false"
          accept="image/png,image/jpeg,image/jpg,image/bmp,image/webp"
          :multiple="false"
        >
          <div>
            <p class="ant-upload-drag-icon"><InboxOutlined /></p>
            <p class="upload-text">点击或拖拽上传空白卷扫描件</p>
            <p class="upload-sub">JPG / PNG / BMP / WebP</p>
          </div>
        </a-upload-dragger>
        <div v-if="blankFile" class="blank-file-info">
          <PaperClipOutlined />
          {{ blankFile.name }} ({{ (blankFile.size / 1024).toFixed(1) }} KB)
          <a-button type="link" danger size="small" @click="blankFile = null">
            移除
          </a-button>
        </div>
      </a-form-item>

      <a-collapse :bordered="false" ghost expand-icon-position="end">
        <a-collapse-panel key="advanced" header="高级选项（留白比例调整）">
          <a-row :gutter="12">
            <a-col :span="8">
              <a-form-item label="顶部留白">
                <a-input-number
                  v-model:value="form.topMarginRatio"
                  :min="0"
                  :max="0.3"
                  :step="0.01"
                  style="width: 100%"
                />
              </a-form-item>
            </a-col>
            <a-col :span="8">
              <a-form-item label="底部留白">
                <a-input-number
                  v-model:value="form.bottomMarginRatio"
                  :min="0"
                  :max="0.3"
                  :step="0.01"
                  style="width: 100%"
                />
              </a-form-item>
            </a-col>
            <a-col :span="8">
              <a-form-item label="左右留白">
                <a-input-number
                  v-model:value="form.sideMarginRatio"
                  :min="0"
                  :max="0.2"
                  :step="0.01"
                  style="width: 100%"
                />
              </a-form-item>
            </a-col>
          </a-row>
          <div style="color: #999; font-size: 12px">
            留白比例用于避开试卷边距和题号区，默认顶部 5% / 底部 3% / 左右 3%
          </div>
        </a-collapse-panel>
      </a-collapse>
    </a-form>

    <div v-if="result" class="generate-result">
      <a-alert type="success" show-icon style="margin-top: 12px">
        <template #message>
          生成成功：{{ result.regions_count }} 个区域，模板 ID = {{ result.template_id }}
        </template>
        <template #description>
          <div>布局：{{ result.layout }}（{{ result.grid.rows }} 行 × {{ result.grid.cols }} 列）</div>
          <div>空白卷尺寸：{{ result.image_size.width }} × {{ result.image_size.height }} px</div>
        </template>
      </a-alert>
    </div>
  </a-modal>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'
import { message } from 'ant-design-vue'
import { InboxOutlined, PaperClipOutlined } from '@ant-design/icons-vue'
import { autoGenerateTemplate } from '@/api/answerSheet'

const props = defineProps({
  open: { type: Boolean, default: false },
  examId: { type: Number, default: null },
})
const emit = defineEmits(['update:open', 'success'])

const loading = ref(false)
const blankFile = ref(null)
const result = ref(null)

const form = reactive({
  layout: 'standard_5col',
  topMarginRatio: 0.05,
  bottomMarginRatio: 0.03,
  sideMarginRatio: 0.03,
})

const layoutOptions = [
  { value: 'standard_5col', label: '5 列布局', desc: '默认，每列 10 题，最多 50 题' },
  { value: 'standard_4col', label: '4 列布局', desc: '每列 10 题，最多 40 题' },
  { value: 'standard_3col', label: '3 列布局', desc: '每列 10 题，最多 30 题' },
  { value: 'standard_2col', label: '2 列布局', desc: '适合大题，最多 20 题' },
  { value: 'single_col', label: '单列布局', desc: '适合纯大题卷，最多 20 题' },
]

// Modal 打开时重置状态
watch(() => props.open, (val) => {
  if (val) {
    blankFile.value = null
    result.value = null
    form.layout = 'standard_5col'
    form.topMarginRatio = 0.05
    form.bottomMarginRatio = 0.03
    form.sideMarginRatio = 0.03
  }
})

function handleFileSelected(file) {
  blankFile.value = file
  return false  // 阻止自动上传
}

async function handleGenerate() {
  if (!props.examId) {
    message.warning('请先选择考试')
    return
  }
  if (!blankFile.value) {
    message.warning('请上传空白卷图片')
    return
  }
  loading.value = true
  result.value = null
  try {
    const res = await autoGenerateTemplate({
      examId: props.examId,
      blankFile: blankFile.value,
      layout: form.layout,
      topMarginRatio: form.topMarginRatio,
      bottomMarginRatio: form.bottomMarginRatio,
      sideMarginRatio: form.sideMarginRatio,
    })
    result.value = res.data
    message.success(`模板生成成功：${res.data.regions_count} 个区域`)
    emit('success', res.data)
    // 不立即关闭，让用户看到结果，点击取消关闭
  } catch (e) {
    message.error('生成模板失败：' + (e.response?.data?.detail || e.message))
  } finally {
    loading.value = false
  }
}

function handleCancel() {
  emit('update:open', false)
}
</script>

<style scoped>
.blank-file-info {
  margin-top: 8px;
  padding: 6px 10px;
  background: #f5f5f5;
  border-radius: 4px;
  font-size: 13px;
}
.generate-result {
  margin-top: 12px;
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
