<template>
  <div class="correction-comparison" v-if="comparisonData">
    <a-row :gutter="16" align="middle">
      <!-- 原始 -->
      <a-col :span="10">
        <a-card size="small" title="原始作答" class="compare-card original">
          <div class="compare-score">
            <span class="score-label">得分</span>
            <span class="score-value" :style="{ color: '#ff4d4f' }">{{ comparisonData.original_score }}</span>
            <span class="score-max"> / {{ comparisonData.max_score }}</span>
          </div>
          <div v-if="comparisonData.remaining_errors?.length" class="error-list">
            <div class="error-label">错误点：</div>
            <a-tag v-for="(err, i) in comparisonData.remaining_errors" :key="i" color="red" size="small">
              {{ err }}
            </a-tag>
          </div>
        </a-card>
      </a-col>

      <!-- 箭头 -->
      <a-col :span="4" class="arrow-area cv-arrow-slide">
        <div class="compare-arrow">
          <span class="arrow-icon">→</span>
          <a-tag v-if="comparisonData.improved" color="green" class="improved-tag">进步 ✓</a-tag>
          <a-tag v-else color="default" class="improved-tag">未改善</a-tag>
        </div>
      </a-col>

      <!-- 订正后 -->
      <a-col :span="10">
        <a-card size="small" title="订正作答" class="compare-card corrected">
          <div class="compare-score">
            <span class="score-label">得分</span>
            <span class="score-value" :style="{ color: comparisonData.improved ? '#52c41a' : '#999' }">
              {{ comparisonData.correction_score }}
            </span>
            <span class="score-max"> / {{ comparisonData.max_score }}</span>
          </div>
          <div v-if="comparisonData.new_comment" class="new-comment">
            <div class="comment-label">AI评语：</div>
            <div class="comment-text">{{ comparisonData.new_comment }}</div>
          </div>
        </a-card>
      </a-col>
    </a-row>
  </div>
  <a-spin v-else-if="loading" />
  <a-empty v-else description="暂无对比数据" />
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { getCorrectionComparison } from '@/api/correction'
import { message } from 'ant-design-vue'

const props = defineProps({
  correctionId: { type: Number, required: true },
})

const comparisonData = ref(null)
const loading = ref(false)

async function fetchComparison() {
  if (!props.correctionId) return
  loading.value = true
  try {
    const res = await getCorrectionComparison(props.correctionId)
    comparisonData.value = res.data
  } catch (e) {
    message.error('获取订正对比失败')
  } finally {
    loading.value = false
  }
}

onMounted(fetchComparison)
watch(() => props.correctionId, fetchComparison)
</script>

<style scoped>
.correction-comparison {
  padding: 8px 0;
}

.compare-card {
  text-align: center;
}

.compare-card.original {
  border-color: #ffccc7;
}

.compare-card.corrected {
  border-color: #b7eb8f;
}

.compare-score {
  margin: 12px 0;
}

.score-label {
  display: block;
  font-size: 12px;
  color: #999;
  margin-bottom: 4px;
}

.score-value {
  font-size: 32px;
  font-weight: 800;
}

.score-max {
  font-size: 16px;
  color: #999;
}

.arrow-area {
  text-align: center;
}

.compare-arrow {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.arrow-icon {
  font-size: 24px;
  color: #3751FE;
  font-weight: 700;
}

.improved-tag {
  font-size: 11px;
}

.error-list,
.new-comment {
  margin-top: 8px;
  text-align: left;
}

.error-label,
.comment-label {
  font-size: 12px;
  color: #999;
  margin-bottom: 4px;
}

.comment-text {
  font-size: 13px;
  color: #333;
  line-height: 1.6;
}
</style>
