<template>
  <div class="scan-report-panel">
    <!-- 顶部汇总卡片 -->
    <PaperSummaryCard
      :student-name="result.student_name"
      :submission-id="result.submission_id"
      :total-score="result.total_score"
      :max-score="result.max_score"
      :summary="result.summary || {}"
    />

    <!-- 三 Tab：题目明细 / 调试图 / 错题汇总 -->
    <a-tabs v-model:activeKey="activeTab" type="line">
      <a-tab-pane key="detail" tab="题目明细">
        <QuestionResultList
          :results="result.question_results || []"
          :submission-id="result.submission_id"
          @update:item="handleItemUpdate"
        />
      </a-tab-pane>

      <a-tab-pane key="debug" tab="调试可视化">
        <a-card v-if="result.debug_image_b64" :bordered="false" size="small">
          <div class="debug-image-wrap">
            <img
              :src="`data:image/png;base64,${result.debug_image_b64}`"
              alt="答题卡检测可视化"
            />
          </div>
          <a-alert
            type="info"
            show-icon
            message="绿色圆圈=已填涂气泡，红色圆圈=未填涂气泡"
            style="margin-top: 8px"
          />
        </a-card>
        <a-empty
          v-else
          description="本次扫描无可视化图（可能未涉及气泡检测题型）"
          style="padding: 40px 0"
        />
      </a-tab-pane>

      <a-tab-pane key="wrong" tab="错题汇总">
        <a-card v-if="wrongList.length" :bordered="false" size="small">
          <a-table
            :data-source="wrongList"
            :columns="wrongColumns"
            :pagination="{ pageSize: 10, hideOnSinglePage: true }"
            size="small"
            row-key="question_id"
          >
            <template #bodyCell="{ column, record, index }">
              <template v-if="column.dataIndex === 'index'">{{ index + 1 }}</template>
              <template v-else-if="column.dataIndex === 'question_content'">
                <span class="wrong-content">{{ record.question_content }}</span>
              </template>
              <template v-else-if="column.dataIndex === 'student_answer'">
                <span class="wrong-answer">{{ formatAnswer(record.student_answer) }}</span>
              </template>
              <template v-else-if="column.dataIndex === 'standard_answer'">
                <span class="right-answer">{{ formatAnswer(record.standard_answer) }}</span>
              </template>
              <template v-else-if="column.dataIndex === 'error'">
                <a-tag v-if="record.error" color="red" size="small">{{ record.error }}</a-tag>
                <span v-else style="color: #999">—</span>
              </template>
            </template>
          </a-table>
        </a-card>
        <a-empty
          v-else
          description="本次扫描无错题，太棒了！"
          style="padding: 40px 0"
        />
      </a-tab-pane>
    </a-tabs>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import PaperSummaryCard from './PaperSummaryCard.vue'
import QuestionResultList from './QuestionResultList.vue'

const props = defineProps({
  result: { type: Object, required: true },
})

const activeTab = ref('detail')

const wrongList = computed(() => props.result.summary?.wrong_list || [])

// D 方案：人工补录成功后局部更新该题结果
// updated 是 QuestionResultList emit 出来的完整 item 对象，含 total_score（后端返回）
function handleItemUpdate(updated) {
  const list = props.result.question_results
  if (list && Array.isArray(list)) {
    const idx = list.findIndex(r => r.question_id === updated.question_id)
    if (idx >= 0) {
      // 用 splice 触发响应式更新（避免直接赋值索引不触发更新）
      list.splice(idx, 1, { ...list[idx], ...updated })
    }
  }
  // 同步更新 total_score（后端已重新计算总分）
  if (updated.total_score !== undefined) {
    props.result.total_score = updated.total_score
  }
}

const wrongColumns = [
  { title: '#', dataIndex: 'index', width: 50 },
  { title: '题目内容', dataIndex: 'question_content', ellipsis: true },
  { title: '学生答案', dataIndex: 'student_answer', width: 120 },
  { title: '标准答案', dataIndex: 'standard_answer', width: 120 },
  { title: '错误原因', dataIndex: 'error', width: 180 },
]

function formatAnswer(ans) {
  if (ans === null || ans === undefined || ans === '') return '（空）'
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
</script>

<style scoped>
.scan-report-panel {
  margin-top: 16px;
}

.debug-image-wrap {
  text-align: center;
  background: #fafafa;
  padding: 8px;
  border-radius: 8px;
}

.debug-image-wrap img {
  max-width: 100%;
  border-radius: 4px;
}

.wrong-content {
  font-size: 13px;
  color: #1a1a2e;
}

.wrong-answer {
  color: #ef4444;
  font-weight: 500;
}

.right-answer {
  color: #16a34a;
  font-weight: 500;
}
</style>
