import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGradingStore = defineStore('grading', () => {
  const isGrading = ref(false)
  const currentStepIndex = ref(-1) // -1=未开始, 0=观察, 1=判断, 2=量规, 3=评分
  const gradingResult = ref(null)
  const stepTimers = ref([])

  function startGrading() {
    isGrading.value = true
    currentStepIndex.value = -1
    gradingResult.value = null
  }

  function setResult(result) {
    gradingResult.value = result
    isGrading.value = false
    revealSteps()
  }

  function revealSteps() {
    clearStepTimers()
    const delays = [0, 800, 1600, 2400]
    delays.forEach((delay, idx) => {
      const timer = setTimeout(() => {
        currentStepIndex.value = idx
      }, delay)
      stepTimers.value.push(timer)
    })
  }

  function clearStepTimers() {
    stepTimers.value.forEach(t => clearTimeout(t))
    stepTimers.value = []
  }

  function reset() {
    clearStepTimers()
    isGrading.value = false
    currentStepIndex.value = -1
    gradingResult.value = null
  }

  return { isGrading, currentStepIndex, gradingResult, startGrading, setResult, reset }
})
