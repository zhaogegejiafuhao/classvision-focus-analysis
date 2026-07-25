<template>
  <span class="latex-text" ref="container" />
</template>

<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import katex from 'katex'
import 'katex/dist/katex.min.css'

const props = defineProps({
  content: { type: String, default: '' },
  /** 是否为行内模式（true=行内公式，false=块级公式） */
  inline: { type: Boolean, default: true },
})

const container = ref(null)

/**
 * 预处理 LaTeX 文本，修复数据源（TAL-SCQ5K）中的格式问题：
 *
 * 1. $$短公式$$（<=30字符）→ $短公式$（行内渲染）
 * 2. \left { → \left\{ （大括号需要转义）
 * 3. \right } → \right\}
 * 4. {{...}} → {...}（双花括号是数据源格式错误，KaTeX只认单花括号）
 * 5. \left( → \left(（无需改动，本身就合法）
 * 6. \textasciitilde → \sim（波浪线）
 * 7. ~ → 空格（LaTeX中~是不换行空格）
 */
function preprocessLatexText(text) {
  if (!text) return text

  let result = text

  // 步骤1: 修复 \left { → \left\{  和  \right } → \right\}
  // 数据源中 \left { 的大括号前有空格，需要去掉空格并转义
  result = result.replace(/\\left\s*\{/g, '\\left\\{')
  result = result.replace(/\\right\s*\}/g, '\\right\\}')

  // 步骤2: 修复双花括号 {{...}} → {...}
  // 数据源中如 {{a}_{1}} 应该是 {a_{1}}，{{2}^{2}} 应该是 {2^{2}}
  // 只在 LaTeX 公式内部替换（因为 {{ 也可能是 Vue 模板语法或普通文本）
  // 这里我们全局替换，因为普通文本中不太可能出现 LaTeX 风格的 {{...}}
  result = result.replace(/\{\{/g, '{')
  result = result.replace(/\}\}/g, '}')

  // 步骤3: 修复 \textasciitilde → \sim（波浪线符号）
  result = result.replace(/\\textasciitilde/g, '\\sim')

  // 步骤4: 将 $$短公式$$ → $短公式$（行内渲染）
  // 数据源把行内数字也用 $$ 包裹，导致渲染为独立一行
  result = result.replace(/\$\$([\s\S]*?)\$\$/g, (match, inner) => {
    const trimmed = inner.trim()
    // 短公式（≤30字符）→ 降级为行内 $...$
    if (trimmed.length <= 30) {
      return `$${trimmed}$`
    }
    // 长公式保持 $$...$$ 块级
    return match
  })

  return result
}

/**
 * 进一步预处理单个公式字符串（提取后、渲染前）
 * 处理公式内部的格式问题
 */
function preprocessFormula(latex) {
  if (!latex) return latex
  let result = latex

  // 去掉多余的 ~ 符号（LaTeX 中 ~ 是不换行空格，但数据源中常作为填充符）
  // 保留有意义的 ~ 用法，只去掉行首行尾和连续多个的
  result = result.replace(/~{2,}/g, ' ')

  return result
}

function renderLatex(text) {
  if (!container.value || !text) {
    if (container.value) container.value.innerHTML = text || ''
    return
  }

  // 预处理：修复数据源的格式问题
  const processed = preprocessLatexText(text)

  // 将文本按 $$...$$ 和 $...$ 分割，分别处理
  const parts = []
  const regex = /(\$\$[\s\S]*?\$\$|\$[^$\n]+?\$)/g
  let lastIndex = 0
  let match

  while ((match = regex.exec(processed)) !== null) {
    // 添加公式前的普通文本
    if (match.index > lastIndex) {
      parts.push({ type: 'text', value: processed.slice(lastIndex, match.index) })
    }

    const formula = match[0]
    if (formula.startsWith('$$')) {
      // 块级公式 $$...$$
      const latex = preprocessFormula(formula.slice(2, -2).trim())
      parts.push({ type: 'block', value: latex })
    } else {
      // 行内公式 $...$
      const latex = preprocessFormula(formula.slice(1, -1).trim())
      parts.push({ type: 'inline', value: latex })
    }
    lastIndex = match.index + match[0].length
  }

  // 添加最后的普通文本
  if (lastIndex < processed.length) {
    parts.push({ type: 'text', value: processed.slice(lastIndex) })
  }

  // 渲染
  const htmlParts = parts.map(part => {
    if (part.type === 'text') {
      return escapeHtml(part.value)
    }
    try {
      return katex.renderToString(part.value, {
        displayMode: part.type === 'block',
        throwOnError: false,
        trust: true,
        strict: false,
      })
    } catch (e) {
      // 渲染失败时显示原始公式
      return escapeHtml(part.type === 'block' ? `$$${part.value}$$` : `$${part.value}$`)
    }
  })

  container.value.innerHTML = htmlParts.join('')
}

function escapeHtml(text) {
  const div = document.createElement('div')
  div.textContent = text
  return div.innerHTML.replace(/\n/g, '<br>')
}

onMounted(() => {
  renderLatex(props.content)
})

watch(() => props.content, (val) => {
  nextTick(() => renderLatex(val))
})
</script>

<style scoped>
.latex-text :deep(.katex-display) {
  margin: 4px 0;
  overflow-x: auto;
  overflow-y: hidden;
}

.latex-text :deep(.katex) {
  font-size: 1.05em;
}

/* 行内公式与文字自然混排 */
.latex-text :deep(.katex-html) {
  white-space: nowrap;
}
</style>
