import { ref, onUnmounted } from 'vue'

/**
 * 考试摄像头作弊检测 composable
 * 从 LivePage.vue 提取核心逻辑，针对考试场景优化
 * - 5FPS 低帧率（节省带宽）
 * - 640x480 低分辨率
 * - 专注违规事件检测
 */
export function useExamCamera(classroomId, examId) {
  const cameraActive = ref(false)
  const violationCount = ref(0)
  const violations = ref([])

  let ws = null
  let stream = null
  let videoEl = null
  let sendCanvas = null
  let sendCtx = null
  let lastSendTime = 0
  let animFrameId = null
  const SEND_INTERVAL = 200  // 5 FPS

  function startCamera(videoElement) {
    videoEl = videoElement
    navigator.mediaDevices.getUserMedia({ video: { width: 640, height: 480 } })
      .then(s => {
        stream = s
        cameraActive.value = true
        if (videoEl) {
          videoEl.srcObject = s
          videoEl.play()
        }
        connectWS()
        animFrameId = requestAnimationFrame(sendFrame)
      })
      .catch(err => {
        console.error('摄像头启动失败', err)
      })
  }

  function stopCamera() {
    if (animFrameId) {
      cancelAnimationFrame(animFrameId)
      animFrameId = null
    }
    if (stream) {
      stream.getTracks().forEach(t => t.stop())
      stream = null
    }
    cameraActive.value = false
    if (ws) {
      ws.close()
      ws = null
    }
  }

  function connectWS() {
    const proto = location.protocol === 'https:' ? 'wss' : 'ws'
    let url = `${proto}://${location.host}/ws/video?classroom_id=${classroomId || 1}`
    if (examId) url += `&exam_id=${examId}`

    ws = new WebSocket(url)
    ws.onopen = () => {
      console.log('[ExamCamera] WebSocket 已连接')
    }
    ws.onmessage = (e) => {
      try {
        const data = JSON.parse(e.data)
        if (data.cheating_events?.length) {
          violations.value.push(...data.cheating_events)
          violationCount.value += data.cheating_events.length
        }
      } catch { /* ignore */ }
    }
    ws.onclose = () => {
      console.log('[ExamCamera] WebSocket 已断开')
      // 自动重连
      if (cameraActive.value) {
        setTimeout(() => {
          if (cameraActive.value) connectWS()
        }, 3000)
      }
    }
    ws.onerror = () => { /* ws.onclose will handle */ }
  }

  function sendFrame() {
    if (!cameraActive.value || !videoEl?.videoWidth) {
      if (cameraActive.value) animFrameId = requestAnimationFrame(sendFrame)
      return
    }
    const now = performance.now()
    if (ws?.readyState === WebSocket.OPEN && now - lastSendTime >= SEND_INTERVAL) {
      if (ws.bufferedAmount > 30000) {
        animFrameId = requestAnimationFrame(sendFrame)
        return
      }
      lastSendTime = now
      if (!sendCanvas || sendCanvas.width !== videoEl.videoWidth) {
        sendCanvas = document.createElement('canvas')
        sendCanvas.width = videoEl.videoWidth
        sendCanvas.height = videoEl.videoHeight
        sendCtx = sendCanvas.getContext('2d')
      }
      sendCtx.drawImage(videoEl, 0, 0)
      ws.send(JSON.stringify({ frame: sendCanvas.toDataURL('image/jpeg', 0.5).split(',')[1] }))
    }
    animFrameId = requestAnimationFrame(sendFrame)
  }

  onUnmounted(() => {
    stopCamera()
  })

  return { cameraActive, violationCount, violations, startCamera, stopCamera }
}
