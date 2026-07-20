<template>
  <a-table
    :columns="columns"
    :data-source="tableData"
    row-key="step_id"
    size="small"
    :pagination="false"
    :row-class-name="getRowClass"
  >
    <template #bodyCell="{ column, record }">
      <template v-if="column.key === 'status'">
        <a-tag v-if="record.status === 'correct'" color="green">✓ 完成</a-tag>
        <a-tag v-else-if="record.status === 'partial'" color="gold">◐ 部分</a-tag>
        <a-tag v-else color="red">✗ 缺失</a-tag>
      </template>
      <template v-else-if="column.key === 'score'">
        <span :class="getScoreClass(record)">{{ record.studentScore }}</span>
        <span class="score-max"> / {{ record.maxScore }}</span>
      </template>
    </template>
  </a-table>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  rubricSteps: { type: Array, default: () => [] },
  gradingSteps: { type: Array, default: () => [] },
})

const columns = [
  { title: '步骤', dataIndex: 'description', key: 'description', ellipsis: true },
  { title: '分值', dataIndex: 'maxScore', key: 'maxScore', width: 70, align: 'center' },
  { title: '得分', key: 'score', width: 100, align: 'center' },
  { title: '状态', key: 'status', width: 90, align: 'center' },
]

const tableData = computed(() => {
  return props.rubricSteps.map((rubric) => {
    const grading = props.gradingSteps.find((g) => g.rubric_ref === rubric.step_id || g.step_id === rubric.step_id)
    const studentScore = grading?.score ?? 0
    const isCorrect = grading?.correct === true
    const isPartial = grading?.correct === false && studentScore > 0

    return {
      step_id: rubric.step_id,
      description: rubric.description,
      maxScore: rubric.score,
      studentScore,
      status: isCorrect ? 'correct' : isPartial ? 'partial' : 'missing',
      required: rubric.required,
    }
  })
})

function getRowClass(record, index) {
  return `cv-line-appear rubric-row`
}

function getScoreClass(record) {
  if (record.status === 'correct') return 'score-correct'
  if (record.status === 'partial') return 'score-partial'
  return 'score-missing'
}
</script>

<style>
/* 非scoped，让cv-line-appear作用到表格行 */
.rubric-row {
  animation: cv-line-appear 0.4s ease both;
}
.rubric-row:nth-child(1) { animation-delay: 0ms; }
.rubric-row:nth-child(2) { animation-delay: 80ms; }
.rubric-row:nth-child(3) { animation-delay: 160ms; }
.rubric-row:nth-child(4) { animation-delay: 240ms; }
.rubric-row:nth-child(5) { animation-delay: 320ms; }
.rubric-row:nth-child(6) { animation-delay: 400ms; }
</style>

<style scoped>
.score-correct { color: #52c41a; font-weight: 700; }
.score-partial { color: #faad14; font-weight: 600; }
.score-missing { color: #ff4d4f; font-weight: 600; }
.score-max { color: #999; font-size: 12px; }
</style>
