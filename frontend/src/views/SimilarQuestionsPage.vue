<template>
  <div class="cv-page" style="padding: 24px">
    <a-page-header
      title="相似题推荐"
      sub-title="分层变式·错因针对·练习闭环"
      style="padding: 0 0 16px 0"
    />

    <a-row :gutter="24">
      <!-- 左列：参数表单 -->
      <a-col :xs="24" :lg="10">
        <a-card title="出题参数" :bordered="false" class="settings-card">
          <a-form layout="vertical">
            <!-- 学生ID + 拉取薄弱点 -->
            <a-form-item label="学生ID（可选，用于拉取薄弱知识点）">
              <a-input-group compact>
                <a-input-number
                  v-model:value="form.studentId"
                  :min="1"
                  style="width: calc(100% - 140px)"
                  placeholder="输入学生ID"
                />
                <a-button
                  type="primary"
                  ghost
                  :loading="loadingWeakPoints"
                  :disabled="!form.studentId"
                  style="width: 140px"
                  @click="fetchWeakPoints"
                >
                  <template #icon><DownloadOutlined /></template>
                  拉取薄弱点
                </a-button>
              </a-input-group>
            </a-form-item>

            <!-- 原题 -->
            <a-form-item label="原题" required>
              <a-textarea
                v-model:value="form.question"
                :rows="4"
                placeholder="粘贴原题文本..."
                show-count
                :maxlength="2000"
              />
            </a-form-item>

            <!-- 标准答案 -->
            <a-form-item label="标准答案（可选）">
              <a-textarea
                v-model:value="form.standardAnswer"
                :rows="2"
                placeholder="参考答案，有助于生成更精准的变式题"
                :maxlength="1000"
              />
            </a-form-item>

            <!-- 错因 -->
            <a-form-item label="错因">
              <a-select
                v-model:value="form.errorType"
                placeholder="选择错因类型"
                allow-clear
              >
                <a-select-option value="计算粗心">计算粗心</a-select-option>
                <a-select-option value="概念混淆">概念混淆</a-select-option>
                <a-select-option value="审题不清">审题不清</a-select-option>
                <a-select-option value="辅助线缺失">辅助线缺失</a-select-option>
                <a-select-option value="逻辑跳步">逻辑跳步</a-select-option>
                <a-select-option value="知识缺失">知识缺失</a-select-option>
              </a-select>
            </a-form-item>

            <!-- 知识点 -->
            <a-form-item label="知识点">
              <a-select
                v-model:value="knowledgePoints"
                mode="tags"
                placeholder="输入知识点回车添加，或点上方「拉取薄弱点」自动填入"
                :token-separators="[',', '，']"
              />
            </a-form-item>

            <!-- 学生分层 -->
            <a-form-item label="学生分层（决定变式策略）">
              <a-radio-group v-model:value="form.tier" button-style="solid">
                <a-radio-button value="优等生">
                  <ThunderboltOutlined /> 优等生
                  <a-tooltip title="根源变式：改变题设条件，考察深层概念">
                    <InfoCircleOutlined style="margin-left: 4px; color: #999" />
                  </a-tooltip>
                </a-radio-button>
                <a-radio-button value="中等生">
                  <CheckCircleOutlined /> 中等生
                  <a-tooltip title="同类变式：保持结构，仅改数值和情境">
                    <InfoCircleOutlined style="margin-left: 4px; color: #999" />
                  </a-tooltip>
                </a-radio-button>
                <a-radio-button value="学困生">
                  <RiseOutlined /> 学困生
                  <a-tooltip title="分层铺垫：基础题→简化原题→进阶题">
                    <InfoCircleOutlined style="margin-left: 4px; color: #999" />
                  </a-tooltip>
                </a-radio-button>
              </a-radio-group>
            </a-form-item>

            <!-- 生成数量 -->
            <a-form-item label="生成数量">
              <a-input-number v-model:value="form.count" :min="1" :max="5" style="width: 100%" />
            </a-form-item>

            <!-- 生成按钮 -->
            <a-form-item>
              <a-button
                type="primary"
                block
                size="large"
                :loading="generating"
                :disabled="!form.question"
                @click="handleGenerate"
              >
                <template #icon><ThunderboltOutlined /></template>
                生成相似题（{{ form.tier }}策略）
              </a-button>
            </a-form-item>
          </a-form>
        </a-card>
      </a-col>

      <!-- 右列：相似题列表 -->
      <a-col :xs="24" :lg="14">
        <!-- 空状态 -->
        <a-card v-if="!questions.length && !generating" :bordered="false" class="result-empty">
          <a-empty description="填写原题后点击「生成相似题」" />
        </a-card>

        <!-- 加载中 -->
        <a-card v-if="generating" :bordered="false">
          <a-skeleton active :paragraph="{ rows: 10 }" />
          <div style="text-align: center; margin-top: 16px; color: #999">
            <a-spin /> 正在调用LLM生成变式题，预计 8-15 秒...
          </div>
        </a-card>

        <!-- 结果展示 -->
        <div v-if="questions.length && !generating">
          <a-alert
            type="success"
            show-icon
            :message="`已生成 ${questions.length} 道相似题`"
            :description="`分层策略：${form.tier} · 变式类型：${[...new Set(questions.map(q => q.variant_type))].join(' / ')}`"
            style="margin-bottom: 16px"
          />

          <a-card
            v-for="(q, idx) in questions"
            :key="idx"
            :bordered="false"
            class="question-card"
          >
            <template #title>
              <span class="q-title">
                <a-tag color="blue">第 {{ idx + 1 }} 题</a-tag>
                <a-tag v-if="q.difficulty" :color="difficultyColor(q.difficulty)">
                  {{ q.difficulty }}
                </a-tag>
                <a-tag v-if="q.variant_type" color="purple">
                  {{ q.variant_type }}
                </a-tag>
              </span>
            </template>
            <template #extra>
              <a-button type="link" size="small" @click="copyQuestion(q)">
                <CopyOutlined /> 复制
              </a-button>
            </template>

            <div class="q-content">{{ q.question_text }}</div>

            <a-collapse :bordered="false" ghost style="margin-top: 8px">
              <a-collapse-panel key="answer" header="📖 参考答案">
                <div class="q-answer">{{ q.standard_answer }}</div>
              </a-collapse-panel>
              <a-collapse-panel
                v-if="q.rubric_suggestion && q.rubric_suggestion.steps"
                key="rubric"
                header="📝 评分量规"
              >
                <a-steps :current="q.rubric_suggestion.steps.length" size="small" direction="vertical">
                  <a-step
                    v-for="(step, sIdx) in q.rubric_suggestion.steps"
                    :key="sIdx"
                    :title="`${step.step_id || 's' + (sIdx + 1)} · ${step.score}分`"
                    :description="step.description"
                  />
                </a-steps>
              </a-collapse-panel>
            </a-collapse>
          </a-card>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script setup>
import { ref, reactive, nextTick } from 'vue'
import { message } from 'ant-design-vue'
import {
  ThunderboltOutlined,
  CheckCircleOutlined,
  RiseOutlined,
  DownloadOutlined,
  InfoCircleOutlined,
  CopyOutlined,
} from '@ant-design/icons-vue'
import { generateSimilarQuestions } from '@/api/similarQuestions'
import { analyzeKnowledge } from '@/api/attribution'

const form = reactive({
  studentId: null,
  question: '',
  standardAnswer: '',
  errorType: undefined,
  tier: '中等生',
  count: 3,
})
// 知识点独立用 ref，避免 a-select mode="tags" 对 reactive 内数组的响应性问题
const knowledgePoints = ref([])
const generating = ref(false)
const loadingWeakPoints = ref(false)
const questions = ref([])

// ===== 拉取薄弱点 =====
async function fetchWeakPoints() {
  if (!form.studentId) {
    message.warning('请先输入学生ID')
    return
  }
  loadingWeakPoints.value = true
  try {
    const res = await analyzeKnowledge({
      student_id: form.studentId,
      analysis_type: 'math',
    })
    const wps = res.data?.weak_points || []
    if (wps.length === 0) {
      message.info('该学生暂无薄弱点记录')
      return
    }
    // 取薄弱度最高的前3个知识点
    const topWps = [...wps]
      .sort((a, b) => (b.weakness_score || 0) - (a.weakness_score || 0))
      .slice(0, 3)
    const kpNames = topWps.map(wp => wp.knowledge_name).filter(Boolean)
    // 直接赋值新数组引用，强制 a-select mode="tags" 视图刷新
    knowledgePoints.value = [...kpNames]

    // 同时填充最常见的错因
    const causeCounter = {}
    wps.forEach(wp => {
      const dist = wp.error_cause_distribution || {}
      Object.entries(dist).forEach(([cause, count]) => {
        causeCounter[cause] = (causeCounter[cause] || 0) + count
      })
    })
    const topCause = Object.entries(causeCounter).sort((a, b) => b[1] - a[1])[0]
    if (topCause) {
      form.errorType = topCause[0]
    }

    // 根据订正率自动推荐分层
    const cs = res.data?.correction_status || {}
    const rate = cs.correction_rate || 0
    let recommendedTier = '中等生'
    if (rate >= 0.8) {
      recommendedTier = '优等生'
    } else if (rate >= 0.4) {
      recommendedTier = '中等生'
    } else {
      recommendedTier = '学困生'
    }
    form.tier = recommendedTier

    // 等待 DOM 更新后再次确认分层 radio 视图同步
    await nextTick()
    form.tier = recommendedTier

    message.success(
      `已拉取 ${kpNames.length} 个薄弱知识点（${kpNames.join('、')}），推荐分层：${recommendedTier}（订正率 ${(rate * 100).toFixed(0)}%）`
    )
  } catch (e) {
    message.error('拉取薄弱点失败：' + (e.response?.data?.detail || e.message))
    console.error(e)
  } finally {
    loadingWeakPoints.value = false
  }
}

// ===== 生成相似题 =====
async function handleGenerate() {
  if (!form.question) {
    message.warning('请输入原题')
    return
  }
  generating.value = true
  questions.value = []
  try {
    const res = await generateSimilarQuestions({
      question: form.question,
      standard_answer: form.standardAnswer,
      error_type: form.errorType || '',
      knowledge_points: knowledgePoints.value,
      tier: form.tier,
      count: form.count,
    })
    const list = res.data?.questions || []
    if (list.length === 0) {
      message.warning('LLM 未返回有效题目，请稍后重试或调整参数')
      return
    }
    questions.value = list
    // 友好处理 LLM 生成题数可能少于请求数的情况
    if (list.length < form.count) {
      message.info(`已生成 ${list.length} 道相似题（计划 ${form.count} 道），LLM 返回数量略少于预期`)
    } else {
      message.success(`成功生成 ${list.length} 道相似题`)
    }
  } catch (e) {
    message.error('生成失败：' + (e.response?.data?.detail || e.message))
    console.error(e)
  } finally {
    generating.value = false
  }
}

// ===== 工具函数 =====
function difficultyColor(diff) {
  if (!diff) return 'default'
  if (diff.includes('基') || diff.includes('简')) return 'green'
  if (diff.includes('难') || diff.includes('进')) return 'red'
  return 'orange'
}

async function copyQuestion(q) {
  const text = `【${q.variant_type || '相似题'}】${q.difficulty || ''}
题目：${q.question_text}

参考答案：
${q.standard_answer || ''}`
  try {
    await navigator.clipboard.writeText(text)
    message.success('已复制到剪贴板')
  } catch (e) {
    message.error('复制失败，请手动选择文本复制')
  }
}
</script>

<style scoped>
.settings-card {
  margin-bottom: 16px;
}

.result-empty {
  text-align: center;
  padding: 60px 0;
}

.question-card {
  margin-bottom: 12px;
  border-left: 3px solid #3751FE !important;
}

.q-title {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.q-content {
  font-size: 15px;
  line-height: 1.7;
  color: #1a1a2e;
  white-space: pre-wrap;
  padding: 8px 0;
}

.q-answer {
  font-size: 14px;
  line-height: 1.7;
  color: #444;
  white-space: pre-wrap;
  background: rgba(55, 81, 254, 0.04);
  padding: 12px;
  border-radius: 6px;
}

.q-answer :deep(.ant-collapse-content) {
  padding: 0;
}
</style>
