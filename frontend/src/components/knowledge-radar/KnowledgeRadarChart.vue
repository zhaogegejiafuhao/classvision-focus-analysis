<template>
  <div ref="chartRef" class="knowledge-radar-chart cv-radar-spin-in" />
</template>

<script setup>
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  radarData: {
    type: Object,
    default: () => ({ indicators: [], values: [] }),
  },
})

const chartRef = ref(null)
let chartInstance = null
let resizeObserver = null

function initChart() {
  if (!chartRef.value) return
  if (chartInstance) {
    chartInstance.dispose()
  }
  chartInstance = echarts.init(chartRef.value)
  updateChart()

  resizeObserver = new ResizeObserver(() => {
    chartInstance?.resize()
  })
  resizeObserver.observe(chartRef.value)
}

function updateChart() {
  if (!chartInstance || !props.radarData) return

  const { indicators, values } = props.radarData
  if (!indicators || indicators.length === 0) return

  chartInstance.setOption({
    animationDuration: 1200,
    animationEasing: 'elasticOut',
    radar: {
      indicator: indicators.map((ind) => ({
        name: ind.name,
        max: ind.max || 100,
      })),
      shape: 'circle',
      splitNumber: 4,
      axisName: {
        color: '#666',
        fontSize: 12,
      },
      splitArea: {
        areaStyle: {
          color: ['rgba(55, 81, 254, 0.02)', 'rgba(55, 81, 254, 0.04)', 'rgba(55, 81, 254, 0.06)', 'rgba(55, 81, 254, 0.08)'],
        },
      },
    },
    series: [
      {
        type: 'radar',
        data: [
          {
            value: values || [],
            animationDelay: (idx) => idx * 100,
            areaStyle: {
              opacity: 0.2,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(55, 81, 254, 0.4)' },
                { offset: 1, color: 'rgba(55, 81, 254, 0.05)' },
              ]),
            },
            lineStyle: {
              color: '#3751FE',
              width: 2,
            },
            itemStyle: {
              color: '#3751FE',
            },
            symbol: 'circle',
            symbolSize: 6,
          },
        ],
      },
    ],
  })
}

watch(
  () => props.radarData,
  () => {
    if (chartInstance) {
      updateChart()
    }
  },
  { deep: true }
)

onMounted(async () => {
  await nextTick()
  initChart()
})

onBeforeUnmount(() => {
  if (resizeObserver) {
    resizeObserver.disconnect()
  }
  if (chartInstance) {
    chartInstance.dispose()
    chartInstance = null
  }
})
</script>

<style scoped>
.knowledge-radar-chart {
  width: 100%;
  height: 300px;
}
</style>
