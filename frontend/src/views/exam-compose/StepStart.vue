<template>
  <div class="step-start">
    <!-- 方式选择 -->
    <h3 style="text-align: center; margin-bottom: 20px; color: #333">选择组卷方式</h3>

    <div class="method-cards">
      <div
        class="method-card"
        :class="{ selected: store.method === 'ai' }"
        @click="store.setMethod('ai')"
      >
        <div class="method-icon">🤖</div>
        <h4>AI 智能组卷</h4>
        <p>输入自然语言需求，AI 自动从题库匹配并生成试卷</p>
      </div>

      <div
        class="method-card"
        :class="{ selected: store.method === 'manual' }"
        @click="store.setMethod('manual')"
      >
        <div class="method-icon">📝</div>
        <h4>人工组卷</h4>
        <p>从题库中手动筛选题目，自由组合成试卷</p>
      </div>
    </div>

    <!-- 基本信息 -->
    <div v-if="store.method" class="basic-info-section">
      <a-divider>{{ store.method === 'ai' ? 'AI 组卷设置' : '人工组卷设置' }}</a-divider>

      <a-form layout="vertical" style="max-width: 600px; margin: 0 auto">
        <a-form-item label="考试标题" required>
          <a-input v-model:value="store.title" placeholder="输入考试标题，如：高一数学期中考试" />
        </a-form-item>

        <a-form-item label="考试类型" required>
          <a-radio-group v-model:value="store.examType" size="large">
            <a-radio-button value="computer">💻 机试 — 学生在电脑上作答</a-radio-button>
            <a-radio-button value="paper">📝 笔试 — 学生拍照上传答案</a-radio-button>
          </a-radio-group>
          <div v-if="store.examType === 'paper'" style="margin-top: 4px; color: #722ed1; font-size: 12px">
            笔试模式下，学生需对每道题拍照上传答案，系统将启动摄像头作弊检测。
          </div>
          <div v-else style="margin-top: 4px; color: #1890ff; font-size: 12px">
            机试模式下，学生可直接在电脑上答题，填空/简答支持上传图片，系统将启动摄像头作弊检测。
          </div>
        </a-form-item>

        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="关联课堂">
              <a-select v-model:value="store.classroomId" allow-clear placeholder="选择课堂" style="width: 100%">
                <a-select-option v-for="c in store.classrooms" :key="c.id" :value="c.id">{{ c.name }}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="考试时长（分钟）">
              <a-input-number v-model:value="store.duration" :min="10" :max="180" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-form-item label="试卷模板（可选）">
          <TemplateCard
            v-model:modelValue="store.templateId"
            :templates="store.templates"
            @create-template="showTemplateModal = true"
            @delete-template="handleDeleteTemplate"
          />
        </a-form-item>
      </a-form>

      <div class="step-actions">
        <a-button type="primary" size="large" :disabled="!store.title.trim()" @click="goNext">
          开始组卷
          <template #icon><RightOutlined /></template>
        </a-button>
      </div>
    </div>

    <!-- 创建模板弹窗 -->
    <a-modal
      v-model:open="showTemplateModal"
      title="创建自定义试卷模板"
      @ok="handleCreateTemplate"
      :confirm-loading="creatingTemplate"
      width="680px"
    >
      <a-form :label-col="{ span: 4 }" :wrapper-col="{ span: 18 }">
        <a-form-item label="模板名称" required>
          <a-input v-model:value="templateForm.name" placeholder="如：期中考试模板" />
        </a-form-item>
        <a-form-item label="说明">
          <a-textarea v-model:value="templateForm.description" :rows="2" placeholder="模板用途描述" />
        </a-form-item>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="总分" :label-col="{ span: 8 }">
              <a-input-number v-model:value="templateForm.total_score" :min="10" :max="500" style="width: 100%" />
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="时长" :label-col="{ span: 8 }">
              <a-input-number v-model:value="templateForm.duration" :min="10" :max="180" addon-after="分钟" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>
        <a-divider>题型结构</a-divider>
        <div v-for="(sec, idx) in templateForm.structure" :key="idx" class="template-section-row">
          <a-row :gutter="8" align="middle">
            <a-col :span="6">
              <a-select v-model:value="sec.type" style="width: 100%">
                <a-select-option value="single">单选题</a-select-option>
                <a-select-option value="multi">多选题</a-select-option>
                <a-select-option value="judge">判断题</a-select-option>
                <a-select-option value="fill">填空题</a-select-option>
                <a-select-option value="essay">简答题</a-select-option>
              </a-select>
            </a-col>
            <a-col :span="4"><a-input-number v-model:value="sec.count" :min="1" :max="50" style="width: 100%" placeholder="数量" /></a-col>
            <a-col :span="4"><a-input-number v-model:value="sec.score_per" :min="1" :max="100" style="width: 100%" placeholder="每题分" /></a-col>
            <a-col :span="7"><a-input v-model:value="sec.knowledgeStr" placeholder="知识点（逗号分隔）" /></a-col>
            <a-col :span="3"><a-rate v-model:value="sec.difficulty" :count="5" style="font-size: 14px" /></a-col>
          </a-row>
          <div class="section-row-actions">
            <a-button type="link" danger size="small" @click="templateForm.structure.splice(idx, 1)">删除此行</a-button>
          </div>
        </div>
        <a-button type="dashed" block @click="addTemplateSection">
          <template #icon><PlusOutlined /></template>
          添加题型
        </a-button>
        <div v-if="templateForm.structure.length" class="estimated-score">
          预计总分：<span :class="{ 'score-warning': templateEstimatedScore !== templateForm.total_score }">{{ templateEstimatedScore }}</span> 分
          <span v-if="templateEstimatedScore !== templateForm.total_score" class="score-hint">（与设定总分 {{ templateForm.total_score }} 不一致）</span>
        </div>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { useRouter } from 'vue-router'
import { RightOutlined, PlusOutlined } from '@ant-design/icons-vue'
import { useExamComposeStore } from '@/stores/examCompose'
import { listExamTemplates, createExamTemplate, deleteExamTemplate } from '@/api/examTemplate'
import { listClassrooms } from '@/api/classroom'
import TemplateCard from '@/components/exam-compose/TemplateCard.vue'

const router = useRouter()
const store = useExamComposeStore()

const showTemplateModal = ref(false)
const creatingTemplate = ref(false)
const templateForm = ref({
  name: '', description: '', total_score: 100, duration: 90,
  structure: [{ type: 'single', count: 10, score_per: 5, knowledgeStr: '', difficulty: 2 }],
})

const templateEstimatedScore = computed(() =>
  templateForm.value.structure.reduce((sum, s) => sum + (s.count || 0) * (s.score_per || 0), 0)
)

function addTemplateSection() {
  templateForm.value.structure.push({ type: 'single', count: 5, score_per: 5, knowledgeStr: '', difficulty: 2 })
}

async function handleCreateTemplate() {
  if (!templateForm.value.name.trim()) { message.error('请输入模板名称'); return }
  creatingTemplate.value = true
  try {
    const structure = templateForm.value.structure.map(s => ({
      type: s.type, count: s.count, score_per: s.score_per,
      knowledge: s.knowledgeStr ? s.knowledgeStr.split(/[,，]/).map(k => k.trim()).filter(Boolean) : [],
      difficulty: s.difficulty,
    }))
    await createExamTemplate({ name: templateForm.value.name, description: templateForm.value.description, total_score: templateForm.value.total_score, duration: templateForm.value.duration, structure })
    message.success('模板创建成功')
    showTemplateModal.value = false
    templateForm.value = { name: '', description: '', total_score: 100, duration: 90, structure: [{ type: 'single', count: 10, score_per: 5, knowledgeStr: '', difficulty: 2 }] }
    fetchTemplates()
  } catch (e) { message.error('创建模板失败') }
  finally { creatingTemplate.value = false }
}

async function handleDeleteTemplate(templateId) {
  try {
    await deleteExamTemplate(templateId)
    message.success('模板已删除')
    if (store.templateId === templateId) store.templateId = null
    fetchTemplates()
  } catch (e) { message.error('删除模板失败') }
}

async function fetchTemplates() {
  try { const res = await listExamTemplates(); store.templates = res.data } catch { /* ignore */ }
}
async function fetchClassrooms() {
  try { const res = await listClassrooms(); store.classrooms = res.data } catch { /* ignore */ }
}

function goNext() {
  store.setStep(1)
  router.push('/exam-compose/compose')
}

onMounted(() => { fetchTemplates(); fetchClassrooms() })
</script>

<style scoped>
.step-start {
  padding: 0 8px;
}
.method-cards {
  display: flex;
  gap: 24px;
  justify-content: center;
  max-width: 600px;
  margin: 0 auto;
}
.method-card {
  flex: 1;
  max-width: 280px;
  padding: 20px;
  border: 2px solid #e8e8e8;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
  background: #fff;
  text-align: center;
}
.method-card:hover { border-color: #3751FE; box-shadow: 0 4px 12px rgba(55, 81, 254, 0.15); }
.method-card.selected { border-color: #3751FE; background: linear-gradient(135deg, #f0f5ff 0%, #e8f4f8 100%); box-shadow: 0 4px 16px rgba(55, 81, 254, 0.2); }
.method-icon { font-size: 36px; margin-bottom: 8px; }
.method-card h4 { font-size: 16px; margin-bottom: 6px; color: #333; }
.method-card p { font-size: 12px; color: #666; margin: 0; }
.basic-info-section {
  margin-top: 24px;
}
.step-actions { margin-top: 20px; text-align: center; }
.template-section-row { margin-bottom: 10px; padding: 10px 12px; background: #fafbfc; border-radius: 6px; border: 1px solid #f0f0f0; }
.section-row-actions { margin-top: 4px; text-align: right; }
.estimated-score { margin-top: 10px; font-size: 13px; color: #666; }
.estimated-score .score-warning { color: #fa8c16; font-weight: 600; }
.score-hint { color: #fa8c16; font-size: 12px; }
</style>
