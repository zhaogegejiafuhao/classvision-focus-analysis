<template>
  <div class="oj-page">
    <div class="oj-header-wrap">
      <a-page-header title="OJ 判题" sub-title="在线代码编辑与即时运行" style="padding: 0 0 16px 0" />
      <a-tag :color="judgerStatus === 'online' ? 'success' : 'error'">
        <span class="status-dot" :class="judgerStatus"></span>
        {{ judgerStatusText }}
      </a-tag>
    </div>

    <a-row :gutter="16">
      <a-col :span="16">
        <a-card size="small">
          <template #title>
            <a-space>
              <a-select v-model:value="language" style="width: 160px" @change="onLangChange">
                <a-select-option value="cpp">C++ (g++ 17)</a-select-option>
                <a-select-option value="c">C (gcc 11)</a-select-option>
                <a-select-option value="py3">Python 3</a-select-option>
                <a-select-option value="java">Java (JDK 17)</a-select-option>
              </a-select>
              <a-button size="small" @click="clearCode">清空</a-button>
            </a-space>
          </template>
          <template #extra>
            <a-button type="primary" @click="runCode" :loading="running">
              <template #icon><CaretRightOutlined /></template>
              运行代码
            </a-button>
          </template>
          <a-textarea
            v-model:value="code"
            :rows="20"
            class="code-editor"
            spellcheck="false"
            :placeholder="`在这里编写 ${languageLabel} 代码...`"
            @keydown.tab.prevent="handleTab"
          />
        </a-card>
      </a-col>

      <a-col :span="8">
        <a-space direction="vertical" style="width: 100%" :size="16">
          <a-card title="标准输入" size="small">
            <template #extra>
              <a-button type="text" size="small" @click="stdin = ''">清空</a-button>
            </template>
            <a-textarea
              v-model:value="stdin"
              :rows="6"
              spellcheck="false"
              placeholder="输入数据（可选）..."
            />
          </a-card>

          <a-card size="small">
            <template #title>
              <a-space>
                运行结果
                <a-tag v-if="runResult" :color="resultColor">{{ runResult.status }}</a-tag>
              </a-space>
            </template>
            <template #extra>
              <span v-if="runResult" class="result-meta-text">
                {{ runResult.cpu_time }}ms · {{ formatMemory(runResult.memory) }}
              </span>
            </template>
            <div v-if="!runResult && !running" class="output-placeholder">
              <a-empty description="点击运行代码查看结果" :image="simpleImage" />
            </div>
            <div v-else-if="running" class="output-loading">
              <a-spin tip="正在运行..." />
            </div>
            <div v-else>
              <div v-if="runResult.output" class="output-block">
                <span class="output-label">stdout</span>
                <pre class="output-text">{{ runResult.output }}</pre>
              </div>
              <div v-if="runResult.error" class="output-block error-block">
                <span class="output-label">stderr</span>
                <pre class="output-text error-text">{{ runResult.error }}</pre>
              </div>
              <div v-if="!runResult.output && !runResult.error" class="output-empty">
                无输出
              </div>
            </div>
          </a-card>
        </a-space>
      </a-col>
    </a-row>

    <a-card title="代码模板" size="small" style="margin-top: 16px">
      <a-space wrap>
        <a-button v-for="tpl in templates" :key="tpl.name" size="small" @click="loadTemplate(tpl)">
          <template #icon><CodeOutlined /></template>
          {{ tpl.name }}
        </a-button>
      </a-space>
    </a-card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { getOjHealth, runCode as ojRunCode } from '@/api/oj'
import { message, Empty } from 'ant-design-vue'
import { CaretRightOutlined, CodeOutlined } from '@ant-design/icons-vue'

const simpleImage = Empty.PRESENTED_IMAGE_SIMPLE

const language = ref('cpp')
const code = ref('')
const stdin = ref('')
const running = ref(false)
const runResult = ref(null)
const judgerStatus = ref('checking')

const languageLabel = computed(() => {
  const labels = { cpp: 'C++', c: 'C', py3: 'Python 3', java: 'Java' }
  return labels[language.value] || ''
})

const judgerStatusText = computed(() => {
  if (judgerStatus.value === 'online') return '判题机在线'
  if (judgerStatus.value === 'offline') return '判题机离线'
  return '检测中...'
})

const resultColor = computed(() => {
  if (!runResult.value) return 'default'
  const status = runResult.value.status
  if (status === 'Accepted') return 'success'
  if (status.includes('Error') || status.includes('Failed')) return 'error'
  return 'warning'
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

const templates = [
  { name: 'A+B (C++)', lang: 'cpp', code: codeTemplates.cpp },
  { name: 'A+B (C)', lang: 'c', code: codeTemplates.c },
  { name: 'A+B (Python)', lang: 'py3', code: codeTemplates.py3 },
  { name: 'A+B (Java)', lang: 'java', code: codeTemplates.java },
  { name: '快速排序', lang: 'cpp', code: `#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}` },
  { name: '斐波那契', lang: 'py3', code: `n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)` },
]

function onLangChange() {
  code.value = ''
}

function clearCode() {
  code.value = ''
}

function loadTemplate(tpl) {
  language.value = tpl.lang
  code.value = tpl.code
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

function formatMemory(kb) {
  if (!kb) return '0 KB'
  if (kb < 1024) return `${kb} KB`
  return `${(kb / 1024).toFixed(1)} MB`
}

async function checkJudger() {
  try {
    const res = await getOjHealth()
    judgerStatus.value = res.data?.status === 'ok' ? 'online' : 'offline'
  } catch {
    judgerStatus.value = 'offline'
  }
}

async function runCode() {
  if (!code.value.trim()) {
    message.warning('请输入代码')
    return
  }
  running.value = true
  runResult.value = null
  try {
    const res = await ojRunCode({
      language: language.value,
      source: code.value,
      input: stdin.value,
    })
    runResult.value = res.data
  } catch (e) {
    const detail = e.response?.data?.detail || '运行失败'
    message.error(detail)
    runResult.value = { status: 'Failed', error: detail, output: '', cpu_time: 0, memory: 0 }
  } finally {
    running.value = false
  }
}

onMounted(() => {
  checkJudger()
})
</script>

<style scoped>
.oj-page {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  max-width: 1400px;
  margin: 0 auto;
}

.oj-header-wrap {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.status-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  margin-right: 4px;
  vertical-align: middle;
}

.status-dot.online { background: #52c41a; }
.status-dot.offline { background: #ff4d4f; }
.status-dot.checking { background: #faad14; }

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

.result-meta-text {
  font-size: 12px;
  color: #8c8c8c;
}

.output-placeholder {
  padding: 20px 0;
  text-align: center;
}

.output-loading {
  padding: 30px 0;
  text-align: center;
}

.output-block {
  margin-bottom: 8px;
}

.output-label {
  display: inline-block;
  font-size: 11px;
  font-weight: 600;
  color: #8c8c8c;
  background: #f5f5f5;
  padding: 1px 6px;
  border-radius: 3px;
  margin-bottom: 4px;
}

.output-text {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 12px;
  line-height: 1.5;
  color: #333;
  background: #f9f9f9;
  padding: 8px 12px;
  border-radius: 4px;
  white-space: pre-wrap;
  word-break: break-all;
  margin: 0;
  max-height: 200px;
  overflow-y: auto;
}

.error-block .output-label {
  color: #ff4d4f;
  background: #fff2f0;
}

.error-text {
  color: #ff4d4f;
  background: #fff2f0;
}

.output-empty {
  text-align: center;
  color: #8c8c8c;
  padding: 16px 0;
}
</style>
