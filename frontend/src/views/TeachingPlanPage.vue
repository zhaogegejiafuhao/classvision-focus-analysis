<template>
  <div class="cv-page">
    <a-page-header title="教学计划" sub-title="备课与教学安排">
      <template #extra>
        <a-button type="primary" @click="showCreateModal = true">新建计划</a-button>
      </template>
    </a-page-header>

    <a-spin :spinning="loading">
      <a-empty v-if="plans.length === 0 && !loading" description="暂无教学计划" />
      <a-list v-else :data-source="plans" :pagination="{ pageSize: 10 }">
        <template #renderItem="{ item }">
          <a-list-item>
            <a-list-item-meta>
              <template #title>
                {{ item.title }}
                <a-tag :color="item.status === 'published' ? 'green' : 'default'" style="margin-left: 8px">
                  {{ item.status === 'published' ? '已发布' : '草稿' }}
                </a-tag>
              </template>
              <template #description>
                <div v-if="item.objectives"><strong>教学目标：</strong>{{ item.objectives }}</div>
                <div v-if="item.chapters && item.chapters.length > 0" style="margin-top: 4px">
                  <strong>章节安排：</strong>
                  <a-tag v-for="(ch, i) in item.chapters" :key="i" style="margin: 2px">{{ ch }}</a-tag>
                </div>
                <div style="margin-top: 4px; font-size: 12px; color: #999">
                  更新于 {{ item.updated_at ? new Date(item.updated_at).toLocaleString('zh-CN') : '-' }}
                </div>
              </template>
            </a-list-item-meta>
            <template #actions>
              <a-button type="link" size="small" @click="editPlan(item)">编辑</a-button>
              <a-popconfirm title="确定删除？" @confirm="deletePlan(item.id)">
                <a-button type="link" danger size="small">删除</a-button>
              </a-popconfirm>
            </template>
          </a-list-item>
        </template>
      </a-list>
    </a-spin>

    <!-- 新建/编辑弹窗 -->
    <a-modal v-model:open="showCreateModal" :title="editingId ? '编辑计划' : '新建计划'" @ok="savePlan" :confirm-loading="submitting" width="600px">
      <a-form :label-col="{ span: 4 }">
        <a-form-item label="标题" required><a-input v-model:value="form.title" /></a-form-item>
        <a-form-item label="教学目标"><a-textarea v-model:value="form.objectives" :rows="3" /></a-form-item>
        <a-form-item label="章节安排">
          <div v-for="(ch, i) in form.chapters" :key="i" style="margin-bottom: 8px">
            <a-input v-model:value="form.chapters[i]" style="width: 85%" />
            <a-button type="link" danger size="small" @click="form.chapters.splice(i, 1)">删除</a-button>
          </div>
          <a-button type="dashed" size="small" @click="form.chapters.push('')">添加章节</a-button>
        </a-form-item>
        <a-form-item label="备注"><a-textarea v-model:value="form.notes" :rows="2" /></a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '../api'

const plans = ref([])
const loading = ref(false)
const submitting = ref(false)
const showCreateModal = ref(false)
const editingId = ref(null)
const form = ref({ title: '', objectives: '', chapters: [], notes: '' })

async function fetchPlans() {
  loading.value = true
  try { const res = await api.get('/teaching-plans'); plans.value = res.data } catch { /* ignore */ } finally { loading.value = false }
}

function editPlan(item) {
  editingId.value = item.id
  form.value = { title: item.title, objectives: item.objectives || '', chapters: item.chapters || [], notes: item.notes || '' }
  showCreateModal.value = true
}

async function savePlan() {
  if (!form.value.title.trim()) { message.error('请输入标题'); return }
  submitting.value = true
  try {
    if (editingId.value) {
      await api.put(`/teaching-plans/${editingId.value}`, form.value)
      message.success('更新成功')
    } else {
      await api.post('/teaching-plans', form.value)
      message.success('创建成功')
    }
    showCreateModal.value = false
    editingId.value = null
    form.value = { title: '', objectives: '', chapters: [], notes: '' }
    fetchPlans()
  } catch { /* ignore */ } finally { submitting.value = false }
}

async function deletePlan(id) {
  try { await api.delete(`/teaching-plans/${id}`); message.success('删除成功'); fetchPlans() } catch { /* ignore */ }
}

onMounted(fetchPlans)
</script>
