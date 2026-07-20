<template>
  <div class="score-counter" :class="{ 'cv-score-bounce': bounced }">
    <span class="score-value">{{ displayScore }}</span>
    <span class="score-divider">/</span>
    <span class="score-max">{{ maxScore }}</span>
  </div>
</template>

<script setup>
import { ref, watch, onBeforeUnmount } from 'vue'

const props = defineProps({
  targetScore: { type: Number, default: 0 },
  maxScore: { type: Number, default: 100 },
  duration: { type: Number, default: 1500 },
})

const emit = defineEmits(['done'])

const displayScore = ref(0)
const bounced = ref(false)
let animFrameId = null

function easeOutExpo(t) {
  return t === 1 ? 1 : 1 - Math.pow(2, -10 * t)
}

function animateCount(target) {
  if (animFrameId) cancelAnimationFrame(animFrameId)

  const start = displayScore.value
  const delta = target - start
  if (delta === 0) return

  const startTime = performance.now()

  function step(currentTime) {
    const elapsed = currentTime - startTime
    const progress = Math.min(elapsed / props.duration, 1)
    const easedProgress = easeOutExpo(progress)
    displayScore.value = Math.round(start + delta * easedProgress)

    if (progress < 1) {
      animFrameId = requestAnimationFrame(step)
    } else {
      displayScore.value = target
      bounced.value = true
      setTimeout(() => { bounced.value = false }, 300)
      emit('done')
    }
  }

  animFrameId = requestAnimationFrame(step)
}

watch(() => props.targetScore, (newVal) => {
  if (newVal !== undefined && newVal !== null) {
    animateCount(newVal)
  }
}, { immediate: true })

onBeforeUnmount(() => {
  if (animFrameId) cancelAnimationFrame(animFrameId)
})
</script>

<style scoped>
.score-counter {
  display: inline-flex;
  align-items: baseline;
  gap: 2px;
}

.score-value {
  font-size: 48px;
  font-weight: 800;
  color: #1a1a2e;
  line-height: 1;
}

.score-divider {
  font-size: 24px;
  color: #bbb;
  margin: 0 2px;
}

.score-max {
  font-size: 20px;
  font-weight: 500;
  color: #999;
}
</style>
