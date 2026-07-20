<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="订正闭环"
      sub-title="提交订正·二次批改·进步追踪"
      style="padding: 0 0 16px 0"
    />

    <a-row :gutter="24">
      <!-- 左列：订正提交 -->
      <a-col :span="10">
        <a-card title="提交订正" :bordered="false" class="settings-card">
          <a-form layout="vertical">
            <a-form-item label="原始提交ID" required>
              <a-input-number
                v-model:value="form.submissionId"
                :min="1"
                style="width: 100%"
                placeholder="学生原始提交ID（可在批改记录中查询）"
              />
            </a-form-item>

            <a-form-item label="原始题目（只读）">
              <a-textarea
                v-model:value="originalInfo.question"
                :rows="3"
                placeholder="填入提交ID后点击「查询原题」"
                readonly
              />
            </a-form-item>

            <a-form-item v-if="originalInfo.score !== null" label="原始批改信息">
              <a-alert type="info" show-icon>
                <template #message>
                  原始得分：<b>{{ originalInfo.score }}/{{ originalInfo.maxScore }}</b>
                  <span v-if="originalInfo.errorCause && originalInfo.errorCause !== 'none'" style="margin-left: 12px">
                    错因：{{ originalInfo.errorCause }}
                  </span>
                </template>
              </a-alert>
            </a-form-item>

            <a-form-item label="订正答案" required>
              <a-radio-group v-model:value="inputMode" size="small" style="margin-bottom: 12px">
                <a-radio-button value="text">📝 文本粘贴</a-radio-button>
                <a-radio-button value="image">📷 图片上传</a-radio-button>
              </a-radio-group>

              <div v-if="inputMode === 'text'">
                <a-textarea
                  v-model:value="form.correctionText"
                  placeholder="输入订正后的解答..."
                  :rows="8"
                  show-count
                  :maxlength="5000"
                />
              </div>

              <div v-else>
                <a-upload-dragger
                  :before-upload="handleImageUpload"
                  :show-upload-list="false"
                  accept="image/*"
                  :multiple="false"
                >
                  <div class="upload-hint">
                    <p class="ant-upload-drag-icon">
                      <inbox-outlined />
                    </p>
                    <p class="ant-upload-text">点击或拖拽上传订正手写图片</p>
                    <p class="ant-upload-hint">支持 JPG / PNG / BMP 格式</p>
                  </div>
                </a-upload-dragger>
                <div v-if="imagePreview" class="image-preview">
                  <img :src="imagePreview" alt="预览" />
                  <a-button type="link" danger size="small" @click="clearImage">移除图片</a-button>
                </div>
              </div>
            </a-form-item>

            <a-form-item>
              <a-space style="width: 100%" direction="vertical">
                <a-button block @click="loadOriginal" :loading="loadingOriginal">
                  <template #icon><SearchOutlined /></template>
                  查询原题
                </a-button>
                <a-button
                  type="primary"
                  block
                  size="large"
                  :loading="submitting"
                  @click="handleSubmit"
                >
                  <template #icon><CheckCircleOutlined /></template>
                  提交订正
                </a-button>
              </a-space>
            </a-form-item>
          </a-form>
        </a-card>
      </a-col>

      <!-- 右列：订正结果 -->
      <a-col :span="14">
        <!-- 无结果占位 -->
        <a-card v-if="!result && !submitting" :bordered="false" class="result-card result-empty">
          <a-empty description="提交订正答案后，将显示二次批改结果与进步对比" />
        </a-card>

        <!-- 提交中 -->
        <a-card v-else-if="submitting && !result" :bordered="false" class="result-card">
          <a-skeleton active :paragraph="{ rows: 8 }" :title="true" />
          <div style="text-align: center; margin-top: 16px; color: #888">
            <a-spin tip="AI正在批改订正答案..." />
          </div>
        </a-card>

        <!-- 订正结果展示 -->
        <div v-else-if="result" class="result-steps">
          <!-- 进步对比卡片 -->
          <a-card :bordered="false" class="result-card cv-comparison-pop">
            <a-row :gutter="16" align="middle">
              <a-col :span="10" style="text-align: center">
                <div class="score-label">原始得分</div>
                <ScoreCounter
                  :target-score="result.original_score"
                  :max-score="originalInfo.maxScore || 10"
                  :duration="800"
                />
              </a-col>
              <a-col :span="4" style="text-align: center">
                <ArrowRightOutlined style="font-size: 32px; color: #3751FE" />
                <div v-if="result.improved" class="improve-tag cv-tag-pop">
                  <RiseOutlined style="color: #52c41a" />
                  <span style="color: #52c41a">进步</span>
                </div>
                <div v-else class="improve-tag cv-tag-pop">
                  <FallOutlined style="color: #faad14" />
                  <span style="color: #faad14">未提升</span>
                </div>
              </a-col>
              <a-col :span="10" style="text-align: center">
                <div class="score-label">订正后得分</div>
                <ScoreCounter
                  :target-score="result.correction_score"
                  :max-score="originalInfo.maxScore || 10"
                  :duration="1200"
                />
              </a-col>
            </a-row>
          </a-card>

          <!-- 进步详情 -->
          <a-card title="订正详情" :bordered="false" size="small" class="result-card">
            <a-descriptions :column="2" size="small">
              <a-descriptions-item label="提交ID">{{ form.submissionId }}</a-descriptions-item>
              <a-descriptions-item label="订正记录ID">{{ result.correction_id }}</a-descriptions-item>
              <a-descriptions-item label="分数变化">
                <a-tag :color="result.improved ? 'green' : 'orange'">
                  {{ result.original_score }} → {{ result.correction_score }}
                </a-tag>
              </a-descriptions-item>
              <a-descriptions-item label="进步状态">
                <a-tag :color="result.improved ? 'success' : 'warning'">
                  {{ result.improved ? '已掌握' : '仍需练习' }}
                </a-tag>
              </a-descriptions-item>
            </a-descriptions>

            <a-divider style="margin: 12px 0" />

            <a-alert
              v-if="result.improved"
              type="success"
              show-icon
              message="恭喜！订正成功"
              description="本次订正答案正确，已掌握该知识点。建议继续挑战相似题巩固。"
            />
            <a-alert
              v-else-if="result.message"
              type="warning"
              show-icon
              message="订正答案为空"
              :description="result.message"
            />
            <a-alert
              v-else
              type="error"
              show-icon
              message="订正仍未通过"
              description="订正答案仍有错误，建议查看错因归因分析，针对薄弱知识点专项练习。"
            />
          </a-card>

          <!-- 操作按钮 -->
          <a-card :bordered="false" size="small" class="result-card">
            <a-space>
              <a-button type="primary" @click="handleViewAttribution">
                <template #icon><RadarChartOutlined /></template>
                查看错因归因
              </a-button>
              <a-button @click="handleGetSimilarQuestions">
                <template #icon><BulbOutlined /></template>
                推荐相似题
              </a-button>
              <a-button @click="handleReset">
                <template #icon><ReloadOutlined /></template>
                重新订正
              </a-button>
            </a-space>
          </a-card>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import {
  SearchOutlined, CheckCircleOutlined, ArrowRightOutlined,
  RiseOutlined, FallOutlined, RadarChartOutlined,
  BulbOutlined, ReloadOutlined, InboxOutlined,
} from '@ant-design/icons-vue'
import { submitCorrection } from '@/api/correction'
import { getGradingResult } from '@/api/grading'
import ScoreCounter from '@/components/ai-grading/ScoreCounter.vue'
import '@/assets/styles/ai-grading-animations.css'

const route = useRoute()
const router = useRouter()

const form = reactive({
  submissionId: null,
  correctionText: '',
})

const originalInfo = reactive({
  question: '',
  score: null,
  maxScore: 10,
  errorCause: '',
})

const inputMode = ref('text')
const imageBase64 = ref('')
const imagePreview = ref('')
const loadingOriginal = ref(false)
const submitting = ref(false)
const result = ref(null)

// 查询原始批改信息
async function loadOriginal() {
  if (!form.submissionId) {
    message.warning('请输入提交ID')
    return
  }
  loadingOriginal.value = true
  try {
    const res = await getGradingResult(form.submissionId)
    const data = res.data || res
    originalInfo.question = data.rubric?.question || `提交#${form.submissionId}（题目详情见批改记录）`
    originalInfo.score = data.score
    originalInfo.maxScore = data.max_score || 10
    originalInfo.errorCause = data.error_cause || ''
    message.success('已加载原始批改信息')
  } catch (e) {
    message.error('查询失败：' + (e?.response?.data?.detail || e?.message || '未找到批改记录'))
  } finally {
    loadingOriginal.value = false
  }
}

// 图片上传处理
function handleImageUpload(file) {
  const reader = new FileReader()
  reader.onload = (e) => {
    imagePreview.value = e.target.result
    imageBase64.value = e.target.result.split(',')[1]
  }
  reader.readAsDataURL(file)
  return false
}

function clearImage() {
  imageBase64.value = ''
  imagePreview.value = ''
}

// 提交订正
async function handleSubmit() {
  if (!form.submissionId) {
    message.warning('请输入提交ID')
    return
  }
  if (inputMode.value === 'text' && !form.correctionText.trim()) {
    message.warning('请输入订正答案')
    return
  }
  if (inputMode.value === 'image' && !imageBase64.value) {
    message.warning('请上传订正图片')
    return
  }

  submitting.value = true
  result.value = null

  try {
    const correction = {
      question_id: 'q1',
      text: inputMode.value === 'text' ? form.correctionText.trim() : undefined,
      image_base64: inputMode.value === 'image' ? imageBase64.value : undefined,
    }
    const res = await submitCorrection({
      submission_id: form.submissionId,
      corrections: [correction],
    })
    result.value = res.data || res
    if (result.value.improved) {
      message.success(`订正成功！${result.value.original_score} → ${result.value.correction_score} 分`)
    } else if (result.value.message) {
      message.warning(result.value.message)
    } else {
      message.info(`订正完成，分数未提升（${result.value.correction_score}分）`)
    }
    // 如果从错题详情跳转来，订正成功后自动跳回
    if (route.query.from_grading_id) {
      setTimeout(() => {
        router.push(`/mistake-book/${route.query.from_grading_id}`)
      }, 2000)
    }
  } catch (e) {
    message.error('订正提交失败：' + (e?.response?.data?.detail || e?.message || '未知错误'))
  } finally {
    submitting.value = false
  }
}

// 查看错因归因（跳转到归因页面，待开发）
function handleViewAttribution() {
  message.info('错因归因页面开发中，敬请期待')
}

// 推荐相似题（跳转到相似题页面，待开发）
function handleGetSimilarQuestions() {
  message.info('相似题推荐页面开发中，敬请期待')
}

// 重置
function handleReset() {
  form.correctionText = ''
  imageBase64.value = ''
  imagePreview.value = ''
  result.value = null
}

// 从错题详情跳转时，自动填充 submission_id 并查询原题
onMounted(() => {
  const sid = route.query.submission_id
  if (sid) {
    form.submissionId = parseInt(sid)
    loadOriginal()
  }
})
</script>

<style scoped>
.settings-card {
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
}

.result-card {
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
  margin-bottom: 16px;
}

.result-empty {
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-steps {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.score-label {
  font-size: 13px;
  color: #888;
  margin-bottom: 8px;
}

.improve-tag {
  margin-top: 8px;
  font-size: 13px;
  font-weight: 600;
}

.upload-hint {
  padding: 16px;
}

.image-preview {
  margin-top: 12px;
  text-align: center;
}

.image-preview img {
  max-width: 100%;
  max-height: 200px;
  border-radius: 8px;
  border: 1px solid #eee;
}
</style>
