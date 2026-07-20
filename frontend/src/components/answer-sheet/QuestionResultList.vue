<template>
  <div class="question-result-list">
    <a-list :data-source="results" item-layout="vertical" size="small">
      <template #renderItem="{ item, index }">
        <a-list-item>
          <a-card
            size="small"
            :bordered="false"
            :class="['result-card', resultClass(item)]"
          >
            <!-- 题头：题号 + 题型 + 评分状态 -->
            <div class="result-header">
              <a-space>
                <a-tag color="blue">第 {{ index + 1 }} 题</a-tag>
                <a-tag :color="typeColor(item.question_type)">
                  {{ typeLabel(item.question_type) }}
                </a-tag>
                <a-tag :color="regionTypeColor(item.region_type)">
                  {{ regionTypeLabel(item.region_type) }}
                </a-tag>
              </a-space>
              <a-space>
                <template v-if="item.is_correct === true">
                  <CheckCircleFilled style="color: #16a34a; font-size: 18px" />
                  <span class="score-text correct">
                    {{ item.score }} / {{ item.max_score }}
                  </span>
                </template>
                <template v-else-if="item.is_correct === false">
                  <CloseCircleFilled style="color: #ef4444; font-size: 18px" />
                  <span class="score-text wrong">
                    {{ item.score }} / {{ item.max_score }}
                  </span>
                </template>
                <template v-else>
                  <WarningFilled style="color: #fa8c16; font-size: 18px" />
                  <span class="score-text ungraded">未批改</span>
                </template>
              </a-space>
            </div>

            <!-- 题目内容 -->
            <div class="question-content">{{ item.question_content }}</div>

            <!-- 答案对比 -->
            <a-row :gutter="8" class="answer-row">
              <a-col :span="12">
                <div class="answer-block student">
                  <div class="answer-label">学生答案</div>
                  <div class="answer-text">{{ formatAnswer(item.student_answer) }}</div>
                </div>
              </a-col>
              <a-col :span="12">
                <div class="answer-block standard">
                  <div class="answer-label">标准答案</div>
                  <div class="answer-text">{{ formatAnswer(item.standard_answer) }}</div>
                </div>
              </a-col>
            </a-row>

            <!-- 错误信息 -->
            <a-alert
              v-if="item.error"
              type="error"
              show-icon
              :message="item.error"
              style="margin-top: 8px"
            />

            <!-- 评语 -->
            <div v-if="item.comment" class="comment-text">
              <MessageOutlined /> {{ item.comment }}
            </div>

            <!-- 人工补录按钮（D 方案）-->
            <!-- 显示条件：未批改 或 有 error；且非大题（大题应走 LLM 重批改）-->
            <div
              v-if="canManualInput(item)"
              class="manual-input-section"
            >
              <a-button
                type="primary"
                ghost
                size="small"
                :loading="loadingId === item.question_id"
                @click="openManualInputModal(item)"
              >
                <template #icon><EditOutlined /></template>
                人工补录学生答案
              </a-button>
              <span class="manual-hint">
                OCR 识别失败或置信度过低，可手动输入学生答案后重新判分
              </span>
            </div>

            <!-- 重新 LLM 批改按钮（E 方案，仅大题）-->
            <!-- 显示条件：大题 + 有 submissionId；无论已批改/未批改都可重批改 -->
            <div
              v-if="canRegradeEssay(item)"
              class="regrade-section"
            >
              <a-button
                size="small"
                class="regrade-btn"
                :loading="regradeLoadingId === item.question_id"
                @click="openRegradeModal(item)"
              >
                <template #icon><RobotOutlined /></template>
                重新 LLM 批改
              </a-button>
              <!-- F 方案：重批改历史按钮 -->
              <a-button
                size="small"
                class="history-btn"
                :loading="historyLoadingId === item.question_id"
                @click="openHistoryDrawer(item)"
              >
                <template #icon><HistoryOutlined /></template>
                重批改历史
              </a-button>
              <span class="regrade-hint">
                上次 OCR 误识别或评分不准？可手输答案文字或重新上传图片，重新触发 LLM 批改
              </span>
            </div>

            <!-- 折叠：详细信息 -->
            <a-collapse :bordered="false" ghost style="margin-top: 4px">
              <a-collapse-panel
                v-if="item.ocr_text"
                key="ocr"
                header="OCR 识别文本"
              >
                <pre class="ocr-text">{{ item.ocr_text }}</pre>
              </a-collapse-panel>
              <a-collapse-panel
                v-if="item.grading_detail"
                key="detail"
                header="批改详情"
              >
                <a-descriptions size="small" :column="2" bordered>
                  <a-descriptions-item label="置信度">
                    {{ (item.confidence * 100).toFixed(0) }}%
                  </a-descriptions-item>
                  <a-descriptions-item
                    v-if="item.grading_detail.bubbles_detected !== undefined"
                    label="检测气泡数"
                  >
                    {{ item.grading_detail.bubbles_detected }}（已填涂 {{ item.grading_detail.bubbles_filled }}）
                  </a-descriptions-item>
                  <a-descriptions-item
                    v-if="item.grading_detail.skew_angle !== undefined"
                    label="倾斜角度"
                  >
                    {{ item.grading_detail.skew_angle.toFixed(2) }}°
                  </a-descriptions-item>
                </a-descriptions>
              </a-collapse-panel>
            </a-collapse>
          </a-card>
        </a-list-item>
      </template>
    </a-list>

    <!-- 人工补录 Modal（D 方案）-->
    <a-modal
      v-model:open="modalOpen"
      title="人工补录学生答案"
      :confirm-loading="submitLoading"
      ok-text="提交并重新判分"
      cancel-text="取消"
      @ok="submitManualInput"
      @cancel="modalOpen = false"
    >
      <a-alert type="info" show-icon style="margin-bottom: 12px">
        <template #message>人工补录并重新判分</template>
        <template #description>
          <div>题目类型：{{ modalItem ? typeLabel(modalItem.question_type) : '' }}</div>
          <div>题目内容：{{ modalItem ? modalItem.question_content : '' }}</div>
          <div>标准答案：{{ modalItem ? modalItem.standard_answer || '（无）' : '' }}</div>
        </template>
      </a-alert>
      <a-form layout="vertical">
        <a-form-item label="学生答案" required>
          <a-textarea
            v-model:value="modalAnswer"
            :rows="3"
            placeholder="请输入学生实际答案（填空题多空可用 ; ， 、 等分隔）"
          />
        </a-form-item>
      </a-form>
      <div class="modal-hint">
        提交后将调用 auto_grade 重新判分（填空题会走多空拆分 + 数值/单位容差逻辑），并更新该题分数和提交总分
      </div>
    </a-modal>

    <!-- 重新 LLM 批改 Modal（E 方案，仅大题）-->
    <a-modal
      v-model:open="regradeModalOpen"
      title="重新 LLM 批改（大题/作文）"
      :confirm-loading="regradeSubmitting"
      ok-text="提交并重新批改"
      cancel-text="取消"
      :width="640"
      @ok="submitRegrade"
      @cancel="regradeModalOpen = false"
    >
      <a-alert type="info" show-icon style="margin-bottom: 12px">
        <template #message>大题/作文 LLM 重批改</template>
        <template #description>
          <div>题目类型：{{ regradeItem ? typeLabel(regradeItem.question_type) : '' }}</div>
          <div>题目内容：{{ regradeItem ? regradeItem.question_content : '' }}</div>
          <div>标准答案：{{ regradeItem ? regradeItem.standard_answer || '（无）' : '' }}</div>
        </template>
      </a-alert>

      <a-tabs v-model:activeKey="regradeMode" size="small">
        <a-tab-pane key="text" tab="文字答案（跳过 OCR）">
          <a-form layout="vertical">
            <a-form-item label="学生答案文字" required>
              <a-textarea
                v-model:value="regradeText"
                :rows="5"
                placeholder="请输入学生实际答案文字（OCR 误识别时用此项，跳过 OCR 直接走 LLM）"
              />
            </a-form-item>
          </a-form>
          <div class="modal-hint">
            教师手输的学生答案文字，confidence=1.0，直接调 LLM 批改，不经过 OCR
          </div>
        </a-tab-pane>

        <a-tab-pane key="image" tab="重新上传图片（重新 OCR）">
          <a-upload-dragger
            :file-list="regradeFileList"
            :before-upload="handleRegradeFileSelect"
            :max-count="1"
            accept="image/png,image/jpeg,image/jpg,image/bmp,image/webp"
          >
            <p class="ant-upload-drag-icon">
              <UploadOutlined />
            </p>
            <p class="ant-upload-text">点击或拖拽图片到此处</p>
            <p class="ant-upload-hint">支持 PNG/JPG/BMP/WEBP，重新走 OCR + LLM</p>
          </a-upload-dragger>
          <div v-if="regradeFile" class="modal-hint" style="margin-top: 8px">
            已选择：{{ regradeFile.name }}（{{ (regradeFile.size / 1024).toFixed(1) }} KB）
          </div>
        </a-tab-pane>
      </a-tabs>

      <a-form layout="vertical" style="margin-top: 8px">
        <a-form-item label="路由模式">
          <a-switch
            v-model:checked="regradeForceEssay"
            checked-children="强制作文"
            un-checked-children="自动判定"
          />
          <span class="modal-hint" style="margin-left: 12px">
            默认按 _is_essay_question 自动判定（含"作文/写一篇/不少于"等关键词 → 作文）；
            强制作文模式时调 grade_essay 四维批改
          </span>
        </a-form-item>
      </a-form>

      <div class="modal-hint">
        提交后会重新调用 grading_service（作文四维批改 / 数学过程分批改），并更新该题分数、总分和批改详情。
        LLM 调用耗时较长（约 10-60s），请耐心等待。
      </div>
    </a-modal>

    <!-- F 方案：重批改历史 Drawer -->
    <a-drawer
      v-model:open="historyDrawerOpen"
      title="重批改历史记录"
      placement="right"
      :width="640"
    >
      <div v-if="historyDrawerLoading" class="history-loading">
        <a-spin tip="加载中..." />
      </div>
      <div v-else-if="historyRecords.length === 0" class="history-empty">
        <a-empty description="暂无重批改历史记录" />
      </div>
      <a-timeline v-else>
        <a-timeline-item
          v-for="rec in historyRecords"
          :key="rec.id"
          :color="historyTimelineColor(rec)"
        >
          <div class="history-card">
            <!-- 卡片头：时间 + 操作人 + 方式徽章 -->
            <div class="history-card-header">
              <span class="history-time">{{ formatHistoryTime(rec.created_at) }}</span>
              <a-tag :color="historyMethodColor(rec.regrade_method)">
                {{ historyMethodLabel(rec.regrade_method) }}
              </a-tag>
              <a-tag v-if="rec.input_mode" color="blue">
                {{ rec.input_mode === 'text' ? '文字' : '图片' }}
              </a-tag>
              <a-tag v-if="rec.force_essay" color="purple">强制作文</a-tag>
              <span class="history-operator">
                {{ rec.operator_name }}（{{ rec.operator_role }}）
              </span>
            </div>

            <!-- 题目分数变化 -->
            <div class="history-score-row">
              <span class="history-label">题目分数：</span>
              <span class="history-before">
                {{ rec.before_score === null ? '未批改' : `${rec.before_score}/${rec.max_score}` }}
              </span>
              <ArrowRightOutlined />
              <span class="history-after" :class="historyAfterClass(rec)">
                {{ rec.after_score }}/{{ rec.max_score }}
              </span>
              <a-tag v-if="rec.after_is_correct === true" color="green">对</a-tag>
              <a-tag v-else-if="rec.after_is_correct === false" color="red">错</a-tag>
            </div>

            <!-- 提交总分变化 -->
            <div class="history-score-row">
              <span class="history-label">提交总分：</span>
              <span class="history-before">
                {{ rec.before_total_score === null ? '—' : rec.before_total_score }}
              </span>
              <ArrowRightOutlined />
              <span class="history-after">{{ rec.after_total_score }}</span>
            </div>

            <!-- LLM 元信息（仅 regrade_essay） -->
            <div v-if="rec.regrade_method === 'regrade_essay'" class="history-llm-row">
              <a-tag color="cyan">{{ rec.is_essay ? '作文' : '数学' }}</a-tag>
              <a-tag v-if="rec.model_key" color="geekblue">{{ rec.model_key }}</a-tag>
              <a-tag v-if="rec.grading_method">{{ rec.grading_method }}</a-tag>
              <a-tag v-if="rec.error_cause && rec.error_cause !== 'none'" color="orange">
                错因：{{ rec.error_cause }}
              </a-tag>
            </div>

            <!-- 学生答案预览（列表模式只显示前 100 字） -->
            <div v-if="rec.student_text_head" class="history-student-text">
              <div class="history-label">学生答案（预览）：</div>
              <div class="history-text">
                {{ rec.student_text_head }}{{ rec.student_text_head.length >= 100 ? '...' : '' }}
              </div>
            </div>

            <!-- 知识点 -->
            <div v-if="rec.knowledge_points && rec.knowledge_points.length" class="history-kp">
              <div class="history-label">知识点：</div>
              <a-tag v-for="kp in rec.knowledge_points" :key="kp" color="blue">{{ kp }}</a-tag>
            </div>

            <!-- 评语 comment -->
            <div v-if="rec.comment" class="history-comment">
              <div class="history-label">评语：</div>
              <div class="history-text">{{ rec.comment }}</div>
            </div>

            <!-- 详情模式才显示的字段（点击"查看完整 LLM 详情"按钮触发 detail=true 重新拉取） -->
            <a-collapse
              v-if="rec._detail"
              :bordered="false"
              ghost
              style="margin-top: 8px"
            >
              <a-collapse-panel key="student_full" header="学生答案全文">
                <pre class="history-full-text">{{ rec.student_text }}</pre>
              </a-collapse-panel>
              <a-collapse-panel
                v-if="rec.writing_attribution_json"
                key="wa"
                header="写作归因 writing_attribution"
              >
                <a-descriptions size="small" :column="1" bordered>
                  <a-descriptions-item label="维度">
                    {{ rec.writing_attribution_json.dimension }}
                  </a-descriptions-item>
                  <a-descriptions-item label="细粒度节点">
                    {{ (rec.writing_attribution_json.fine_nodes || []).join('、') }}
                  </a-descriptions-item>
                  <a-descriptions-item label="改进建议">
                    {{ rec.writing_attribution_json.suggestion }}
                  </a-descriptions-item>
                </a-descriptions>
              </a-collapse-panel>
              <a-collapse-panel
                v-if="rec.grading_json"
                key="gj"
                header="批改详情 grading_json"
              >
                <pre class="history-full-text">{{ JSON.stringify(rec.grading_json, null, 2) }}</pre>
              </a-collapse-panel>
            </a-collapse>

            <!-- 展开详情按钮 -->
            <a-button
              v-if="!rec._detail"
              size="small"
              type="link"
              @click="loadHistoryDetail(rec)"
            >
              查看完整 LLM 详情
            </a-button>
          </div>
        </a-timeline-item>
      </a-timeline>
    </a-drawer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { message } from 'ant-design-vue'
import {
  CheckCircleFilled,
  CloseCircleFilled,
  WarningFilled,
  MessageOutlined,
  EditOutlined,
  RobotOutlined,
  UploadOutlined,
  HistoryOutlined,
  ArrowRightOutlined,
} from '@ant-design/icons-vue'
import { manualInputAnswer, regradeEssay, listRegradeHistory } from '@/api/answerSheet'

const props = defineProps({
  results: { type: Array, default: () => [] },
  submissionId: { type: Number, default: null },  // D 方案：人工补录需要
})

const emit = defineEmits(['update:item'])  // D/E 方案：批改成功后通知父组件

// ============ D 方案：人工补录 ============
const loadingId = ref(null)
const modalOpen = ref(false)
const modalItem = ref(null)
const modalAnswer = ref('')
const submitLoading = ref(false)

function canManualInput(item) {
  // 没有 submissionId 不能补录
  if (!props.submissionId) return false
  // 大题不支持人工补录（应走 LLM 重批改）
  if (item.question_type === 'essay') return false
  if (item.question_type === 'unknown') return false
  // 显示条件：未批改 或 有 error
  return item.is_correct === null || !!item.error
}

function openManualInputModal(item) {
  modalItem.value = item
  modalAnswer.value = item.student_answer || ''
  modalOpen.value = true
}

async function submitManualInput() {
  if (!modalItem.value) return
  if (!modalAnswer.value.trim()) {
    message.warning('请输入学生答案')
    return
  }
  if (!props.submissionId) {
    message.error('缺少 submissionId，无法提交')
    return
  }

  submitLoading.value = true
  try {
    const res = await manualInputAnswer(
      props.submissionId,
      modalItem.value.question_id,
      modalAnswer.value.trim(),
    )
    message.success(`已重新判分：${res.data.score}/${res.data.max_score}`)

    // 局部更新该题目结果（让父组件替换原条目）
    const updated = {
      ...modalItem.value,
      student_answer: res.data.student_answer,
      score: res.data.score,
      is_correct: res.data.is_correct,
      error: null,  // 清除原 error
      comment: `教师人工补录：${res.data.is_correct ? '判对' : '判错'}（${res.data.score}/${res.data.max_score}）`,
      confidence: 1.0,  // 人工补录置信度为 1
      total_score: res.data.total_score,  // 后端重新计算的总分，供父组件同步
    }
    emit('update:item', updated)

    modalOpen.value = false
  } catch (e) {
    const detail = e.response?.data?.detail || e.message
    message.error('人工补录失败：' + detail)
  } finally {
    submitLoading.value = false
  }
}

// ============ E 方案：大题/作文 LLM 重批改 ============
const regradeLoadingId = ref(null)
const regradeModalOpen = ref(false)
const regradeItem = ref(null)
const regradeMode = ref('text')  // 'text' | 'image'
const regradeText = ref('')
const regradeFile = ref(null)
const regradeFileList = ref([])
const regradeForceEssay = ref(false)
const regradeSubmitting = ref(false)

function canRegradeEssay(item) {
  // 没有 submissionId 不能重批改
  if (!props.submissionId) return false
  // 仅大题（essay）支持 LLM 重批改
  return item.question_type === 'essay'
}

function openRegradeModal(item) {
  regradeItem.value = item
  // 默认填入当前学生答案（如果是 OCR 误识别，教师可改）
  regradeText.value = item.student_answer || ''
  regradeMode.value = 'text'
  regradeFile.value = null
  regradeFileList.value = []
  regradeForceEssay.value = false
  regradeModalOpen.value = true
}

function handleRegradeFileSelect(file) {
  // before-upload 钩子：返回 false 阻止自动上传，由我们手动控制
  regradeFile.value = file
  regradeFileList.value = [file]
  return false
}

async function submitRegrade() {
  if (!regradeItem.value) return
  if (!props.submissionId) {
    message.error('缺少 submissionId，无法提交')
    return
  }

  // 根据模式校验入参
  let payload = { forceEssay: regradeForceEssay.value }
  if (regradeMode.value === 'text') {
    if (!regradeText.value.trim()) {
      message.warning('请输入学生答案文字')
      return
    }
    payload.studentText = regradeText.value.trim()
  } else {  // image 模式
    if (!regradeFile.value) {
      message.warning('请上传学生答案图片')
      return
    }
    payload.imageFile = regradeFile.value
  }

  regradeLoadingId.value = regradeItem.value.question_id
  regradeSubmitting.value = true
  const hide = message.loading('LLM 批改中，请耐心等待（约 10-60s）...', 0)

  try {
    const res = await regradeEssay(
      props.submissionId,
      regradeItem.value.question_id,
      payload,
    )
    hide()
    message.success(`已重新批改：${res.data.score}/${res.data.max_score}（${res.data.is_essay ? '作文' : '数学'} → ${res.data.model_key}）`)

    // 局部更新该题目结果（让父组件替换原条目）
    const updated = {
      ...regradeItem.value,
      student_answer: res.data.student_answer,
      score: res.data.score,
      is_correct: res.data.is_correct,
      error: null,
      comment: res.data.comment,
      confidence: 1.0,
      // 把后端返回的完整 grading_detail 也带回前端，供折叠面板展示
      grading_detail: {
        is_essay: res.data.is_essay,
        model_key: res.data.model_key,
        grading_method: res.data.grading_method,
        grading: res.data.grading,
        error_cause: res.data.error_cause,
        knowledge_points: res.data.knowledge_points,
        writing_attribution: res.data.writing_attribution,
      },
      total_score: res.data.total_score,  // 后端重新计算的总分，供父组件同步
    }
    emit('update:item', updated)

    regradeModalOpen.value = false
  } catch (e) {
    hide()
    const detail = e.response?.data?.detail || e.message
    message.error('LLM 重批改失败：' + detail)
  } finally {
    regradeLoadingId.value = null
    regradeSubmitting.value = false
  }
}

// ============ F 方案：重批改历史 ============
const historyLoadingId = ref(null)
const historyDrawerOpen = ref(false)
const historyDrawerLoading = ref(false)
const historyRecords = ref([])
const historyItem = ref(null)  // 当前查看历史的题目

async function openHistoryDrawer(item) {
  historyItem.value = item
  historyDrawerOpen.value = true
  historyDrawerLoading.value = true
  historyRecords.value = []
  historyLoadingId.value = item.question_id
  try {
    const res = await listRegradeHistory(
      props.submissionId,
      item.question_id,
      { detail: false, limit: 100, offset: 0 },
    )
    historyRecords.value = (res.data.records || []).map(r => ({ ...r, _detail: false }))
  } catch (e) {
    const detail = e.response?.data?.detail || e.message
    message.error('加载历史记录失败：' + detail)
  } finally {
    historyDrawerLoading.value = false
    historyLoadingId.value = null
  }
}

async function loadHistoryDetail(rec) {
  // 单条记录按需加载 detail=true
  try {
    const res = await listRegradeHistory(
      props.submissionId,
      historyItem.value.question_id,
      { detail: true, limit: 100, offset: 0 },
    )
    // 找到对应的 detail 版本替换
    const detailed = (res.data.records || []).find(r => r.id === rec.id)
    if (detailed) {
      const idx = historyRecords.value.findIndex(r => r.id === rec.id)
      if (idx >= 0) {
        historyRecords.value.splice(idx, 1, { ...detailed, _detail: true })
      }
    }
  } catch (e) {
    const detail = e.response?.data?.detail || e.message
    message.error('加载详情失败：' + detail)
  }
}

function historyTimelineColor(rec) {
  // 错误批改红色，正确批改绿色，null（人工补录判分前的中间态）蓝色
  if (rec.after_is_correct === true) return 'green'
  if (rec.after_is_correct === false) return 'red'
  return 'blue'
}

function historyMethodLabel(method) {
  return method === 'regrade_essay' ? 'LLM 重批改' : '人工补录'
}

function historyMethodColor(method) {
  return method === 'regrade_essay' ? 'purple' : 'orange'
}

function historyAfterClass(rec) {
  if (rec.before_score === null) return 'is-new'
  if (rec.after_score > rec.before_score) return 'is-up'
  if (rec.after_score < rec.before_score) return 'is-down'
  return 'is-same'
}

function formatHistoryTime(iso) {
  if (!iso) return '—'
  const d = new Date(iso)
  if (isNaN(d.getTime())) return iso
  const pad = n => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`
}

// ============ 通用辅助函数 ============

function typeLabel(type) {
  const m = { single: '单选', multi: '多选', judge: '判断', fill: '填空', essay: '大题', unknown: '未知' }
  return m[type] || type
}

function typeColor(type) {
  const m = { single: 'blue', multi: 'cyan', judge: 'geekblue', fill: 'orange', essay: 'purple', unknown: 'default' }
  return m[type] || 'default'
}

function regionTypeLabel(type) {
  const m = { bubble: '选择题', fill: '填空', essay: '大题' }
  return m[type] || type
}

function regionTypeColor(type) {
  const m = { bubble: '#3751FE', fill: '#fa8c16', essay: '#722ed1' }
  return m[type] || 'default'
}

function formatAnswer(ans) {
  if (ans === null || ans === undefined || ans === '') return '（空）'
  // 单选/多选的索引转 A/B/C/D 显示更友好
  if (/^\d+(,\d+)*$/.test(String(ans))) {
    return String(ans)
      .split(',')
      .map(i => String.fromCharCode(65 + parseInt(i, 10)))
      .join(' / ')
  }
  if (ans === 'true') return '正确'
  if (ans === 'false') return '错误'
  return String(ans)
}

function resultClass(item) {
  if (item.is_correct === true) return 'is-correct'
  if (item.is_correct === false) return 'is-wrong'
  return 'is-ungraded'
}
</script>

<style scoped>
.result-card {
  margin-bottom: 8px;
  border-left: 3px solid #e8e8e8 !important;
  transition: all 0.2s;
}

.result-card.is-correct {
  border-left-color: #16a34a !important;
  background: rgba(22, 163, 74, 0.02);
}

.result-card.is-wrong {
  border-left-color: #ef4444 !important;
  background: rgba(239, 68, 68, 0.02);
}

.result-card.is-ungraded {
  border-left-color: #fa8c16 !important;
  background: rgba(250, 140, 22, 0.02);
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
  flex-wrap: wrap;
  gap: 4px;
}

.score-text {
  font-size: 14px;
  font-weight: 600;
}

.score-text.correct { color: #16a34a; }
.score-text.wrong { color: #ef4444; }
.score-text.ungraded { color: #fa8c16; }

.question-content {
  font-size: 13px;
  color: #1a1a2e;
  line-height: 1.6;
  margin: 4px 0 8px;
  white-space: pre-wrap;
}

.answer-row {
  margin-bottom: 4px;
}

.answer-block {
  padding: 6px 8px;
  border-radius: 4px;
  font-size: 13px;
}

.answer-block.student {
  background: rgba(239, 68, 68, 0.06);
  border-left: 2px solid #ef4444;
}

.answer-block.standard {
  background: rgba(22, 163, 74, 0.06);
  border-left: 2px solid #16a34a;
}

.answer-label {
  font-size: 11px;
  color: #888;
  margin-bottom: 2px;
}

.answer-text {
  font-weight: 500;
  color: #1a1a2e;
  word-break: break-all;
}

.comment-text {
  margin-top: 8px;
  font-size: 12px;
  color: #555;
  background: rgba(55, 81, 254, 0.04);
  padding: 6px 8px;
  border-radius: 4px;
  line-height: 1.5;
}

.ocr-text {
  margin: 0;
  font-size: 12px;
  color: #555;
  white-space: pre-wrap;
  background: #fafafa;
  padding: 6px;
  border-radius: 4px;
}

.manual-input-section {
  margin-top: 8px;
  padding: 8px 10px;
  background: rgba(250, 140, 22, 0.06);
  border-left: 2px solid #fa8c16;
  border-radius: 4px;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.manual-hint {
  font-size: 12px;
  color: #888;
  flex: 1;
  min-width: 200px;
}

.modal-hint {
  margin-top: 4px;
  font-size: 12px;
  color: #888;
  line-height: 1.5;
}

/* E 方案：大题 LLM 重批改按钮区（紫色调，与人工补录的橙色调区分）*/
.regrade-section {
  margin-top: 8px;
  padding: 8px 10px;
  background: rgba(114, 46, 209, 0.06);
  border-left: 2px solid #722ed1;
  border-radius: 4px;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.regrade-btn {
  color: #722ed1 !important;
  border-color: #722ed1 !important;
}

.regrade-btn:hover {
  color: #9254de !important;
  border-color: #9254de !important;
  background: rgba(114, 46, 209, 0.06) !important;
}

.regrade-hint {
  font-size: 12px;
  color: #888;
  flex: 1;
  min-width: 200px;
}

/* F 方案：重批改历史按钮区 */
.history-btn {
  color: #13c2c2 !important;
  border-color: #13c2c2 !important;
  margin-left: 8px;
}

.history-btn:hover {
  color: #36cfc9 !important;
  border-color: #36cfc9 !important;
  background: rgba(19, 194, 194, 0.06) !important;
}

/* Drawer 内 Timeline 卡片 */
.history-card {
  padding: 8px 10px;
  background: #fafafa;
  border-radius: 4px;
  margin-bottom: 4px;
}

.history-card-header {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 6px;
  font-size: 12px;
}

.history-time {
  color: #888;
  font-family: 'Courier New', monospace;
}

.history-operator {
  color: #555;
  margin-left: auto;
}

.history-score-row {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  margin: 4px 0;
}

.history-label {
  color: #888;
  font-size: 12px;
  min-width: 70px;
}

.history-before {
  color: #999;
  text-decoration: line-through;
}

.history-after {
  font-weight: 600;
  color: #1a1a2e;
}

.history-after.is-up { color: #16a34a; }
.history-after.is-down { color: #ef4444; }
.history-after.is-new { color: #1890ff; }
.history-after.is-same { color: #1a1a2e; }

.history-llm-row {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
  margin: 4px 0;
}

.history-student-text,
.history-kp,
.history-comment {
  margin: 4px 0;
  font-size: 12px;
}

.history-text {
  color: #333;
  background: #fff;
  padding: 4px 6px;
  border-radius: 3px;
  line-height: 1.5;
  white-space: pre-wrap;
  word-break: break-all;
}

.history-full-text {
  margin: 0;
  font-size: 11px;
  color: #555;
  background: #fff;
  padding: 6px;
  border-radius: 3px;
  white-space: pre-wrap;
  word-break: break-all;
  max-height: 240px;
  overflow-y: auto;
}

.history-loading,
.history-empty {
  padding: 40px 0;
  text-align: center;
}
</style>
