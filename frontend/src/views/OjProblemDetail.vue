<template>
  <div class="oj-detail-page">
    <div class="detail-header">
      <a-button type="text" @click="$router.push('/oj')">
        <template #icon><ArrowLeftOutlined /></template>
        返回列表
      </a-button>
      <a-space v-if="canEdit" style="margin-left: auto">
        <a-button @click="$router.push(`/oj?edit=${problem.id}`)">
          <template #icon><EditOutlined /></template>
          编辑题目
        </a-button>
      </a-space>
    </div>

    <a-spin :spinning="loading">
      <a-skeleton v-if="loading && !problem" active :paragraph="{ rows: 6 }" />
      <a-row :gutter="16" v-else-if="problem">
        <!-- 左侧：题目描述 -->
        <a-col :span="12">
          <a-card>
            <template #title>
              <a-space>
                <span>#{{ problem.id }} {{ problem.title }}</span>
                <a-tag :color="difficultyColor(problem.difficulty)">{{ problem.difficulty }}</a-tag>
              </a-space>
            </template>

            <div class="problem-section">
              <h4>题目描述</h4>
              <p class="problem-text">{{ problem.description }}</p>
            </div>

            <div class="problem-section">
              <h4>输入格式</h4>
              <pre class="problem-pre">{{ problem.input_format }}</pre>
            </div>

            <div class="problem-section">
              <h4>输出格式</h4>
              <pre class="problem-pre">{{ problem.output_format }}</pre>
            </div>

            <div class="problem-section">
              <h4>样例输入</h4>
              <pre class="problem-pre sample">{{ problem.sample_input }}</pre>
            </div>

            <div class="problem-section">
              <h4>样例输出</h4>
              <pre class="problem-pre sample">{{ problem.sample_output }}</pre>
            </div>

            <div class="problem-section" v-if="problem.hint">
              <h4>提示</h4>
              <p class="problem-text">{{ problem.hint }}</p>
            </div>

            <div class="problem-meta">
              <a-tag>时间限制: {{ problem.time_limit }}ms</a-tag>
              <a-tag>内存限制: {{ (problem.memory_limit / 1024 / 1024).toFixed(0) }}MB</a-tag>
            </div>
          </a-card>
        </a-col>

        <!-- 右侧：代码编辑器 -->
        <a-col :span="12">
          <a-card>
            <template #title>
              <a-space>
                <a-select v-model:value="language" style="width: 160px" @change="onLangChange">
                  <a-select-option value="cpp">C++ (g++ 17)</a-select-option>
                  <a-select-option value="c">C (gcc 11)</a-select-option>
                  <a-select-option value="py3">Python 3</a-select-option>
                  <a-select-option value="java">Java (JDK 17)</a-select-option>
                </a-select>
              </a-space>
            </template>
            <template #extra>
              <a-button type="primary" @click="submitCode" :loading="submitting">
                <template #icon><CaretRightOutlined /></template>
                提交判题
              </a-button>
            </template>

            <a-textarea
              v-model:value="code"
              :rows="22"
              class="code-editor"
              spellcheck="false"
              placeholder="在这里编写代码..."
              @keydown.tab.prevent="handleTab"
            />
          </a-card>

          <!-- 判题结果 -->
          <a-card v-if="result" style="margin-top: 16px" size="small">
            <template #title>
              <a-space>
                <span>判题结果</span>
                <a-tag :color="statusColor(result.status)">{{ result.status }}</a-tag>
              </a-space>
            </template>
            <template #extra>
              <span class="result-meta" v-if="result.status !== 'CE'">
                {{ result.cpu_time }}ms · {{ formatMemory(result.memory) }}
              </span>
            </template>

            <div v-if="result.status === 'AC'" class="result-success">
              <CheckCircleOutlined style="font-size: 20px; color: #52c41a" />
              <span>恭喜！代码通过所有测试用例。</span>
            </div>
            <div v-else-if="result.error_message" class="result-error">
              <pre class="error-pre">{{ result.error_message }}</pre>
            </div>
          </a-card>
        </a-col>
      </a-row>
      <a-empty v-else-if="!loading" description="题目不存在" />
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { ArrowLeftOutlined, CaretRightOutlined, CheckCircleOutlined, EditOutlined } from '@ant-design/icons-vue'
import api from '@/api'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const problem = ref(null)
const loading = ref(true)
const language = ref('cpp')
const code = ref('')
const submitting = ref(false)
const result = ref(null)

const canEdit = computed(() => {
  if (!problem.value) return false
  if (!['teacher', 'admin'].includes(userStore.role)) return false
  if (userStore.role === 'admin') return true
  return problem.value.created_by === userStore.user?.id
})

const codeTemplates = {
  cpp: `#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}`,
  c: `#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\\n", a + b);
    return 0;
}`,
  py3: `a, b = map(int, input().split())
print(a + b)`,
  java: `import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(a + b);
    }
}`,
}

function difficultyColor(d) {
  if (d === '简单') return 'green'
  if (d === '中等') return 'orange'
  return 'red'
}

function statusColor(s) {
  if (s === 'AC') return 'success'
  if (s === 'WA') return 'warning'
  if (s === 'CE') return 'default'
  if (s === 'TLE' || s === 'MLE') return 'orange'
  if (s === 'RE' || s === 'SE') return 'error'
  return 'default'
}

function formatMemory(bytes) {
  if (!bytes) return '0 KB'
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(0)} KB`
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`
}

function onLangChange() {
  code.value = codeTemplates[language.value] || ''
}

function handleTab(e) {
  const target = e.target
  const start = target.selectionStart
  const end = target.selectionEnd
  code.value = code.value.substring(0, start) + '    ' + code.value.substring(end)
  setTimeout(() => {
    target.selectionStart = target.selectionEnd = start + 4
  }, 0)
}

async function loadProblem() {
  loading.value = true
  try {
    const res = await api.get(`/oj/problems/${route.params.id}`)
    problem.value = res.data
    code.value = codeTemplates[language.value] || ''
  } catch (e) {
    message.error('加载题目失败')
    router.push('/oj')
  } finally {
    loading.value = false
  }
}

async function submitCode() {
  if (!code.value.trim()) {
    message.warning('请输入代码')
    return
  }
  submitting.value = true
  result.value = null
  try {
    const res = await api.post('/oj/submit', {
      problem_id: parseInt(route.params.id),
      language: language.value,
      source_code: code.value,
    })
    result.value = res.data
    if (res.data.status === 'AC') {
      message.success('通过！')
    } else {
      message.warning(`判题结果: ${res.data.status}`)
    }
  } catch (e) {
    const detail = e.response?.data?.detail || '提交失败'
    message.error(detail)
  } finally {
    submitting.value = false
  }
}

onMounted(() => {
  loadProblem()
})
</script>

<style scoped>
.oj-detail-page {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  max-width: 1400px;
  margin: 0 auto;
}

.detail-header {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
}

.problem-section {
  margin-bottom: 16px;
}

.problem-section h4 {
  font-size: 14px;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 6px;
}

.problem-text {
  font-size: 14px;
  line-height: 1.7;
  color: #333;
  margin: 0;
  white-space: pre-wrap;
}

.problem-pre {
  background: #f5f6fa;
  border: 1px solid #e8e8e8;
  border-radius: 6px;
  padding: 10px 14px;
  font-size: 13px;
  font-family: 'Consolas', 'Monaco', monospace;
  line-height: 1.5;
  color: #333;
  margin: 0;
  white-space: pre-wrap;
  word-break: break-all;
}

.problem-pre.sample {
  background: #f0f5ff;
  border-color: #adc6ff;
}

.problem-meta {
  display: flex;
  gap: 8px;
  margin-top: 16px;
}

.code-editor :deep(textarea) {
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace !important;
  font-size: 13px !important;
  line-height: 1.6 !important;
  background: #1e1e2e !important;
  color: #cdd6f4 !important;
  border: none !important;
  resize: vertical;
}

.code-editor :deep(textarea)::placeholder {
  color: #6c7086;
}

.result-meta {
  font-size: 12px;
  color: #8c8c8c;
}

.result-success {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #52c41a;
}

.result-error {
  margin: 0;
}

.error-pre {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 12px;
  line-height: 1.5;
  color: #ff4d4f;
  background: #fff2f0;
  padding: 8px 12px;
  border-radius: 4px;
  white-space: pre-wrap;
  word-break: break-all;
  margin: 0;
}
</style>
