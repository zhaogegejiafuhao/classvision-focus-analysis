import axios from 'axios'

/**
 * 等待后端服务就绪（轮询 /api/health）。
 * 在项目重启后，后端模型预热需要时间，前端需要等待后端就绪再加载数据。
 *
 * @param {number} maxRetries - 最大重试次数（默认30次）
 * @param {number} interval - 轮询间隔毫秒（默认2000ms）
 * @returns {Promise<boolean>} 后端是否就绪
 */
export async function waitForBackend(maxRetries = 30, interval = 2000) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      await axios.get('/api/health', { timeout: 3000 })
      return true
    } catch {
      await new Promise(resolve => setTimeout(resolve, interval))
    }
  }
  return false
}

/**
 * 带重试的 API 调用。连接失败时自动重试。
 *
 * @param {Function} apiFn - 返回 Promise 的 API 调用函数
 * @param {number} maxRetries - 最大重试次数
 * @param {number} interval - 重试间隔毫秒
 * @returns {Promise} API 调用结果
 */
export async function retryApiCall(apiFn, maxRetries = 3, interval = 1000) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await apiFn()
    } catch (err) {
      if (i === maxRetries - 1) throw err
      await new Promise(resolve => setTimeout(resolve, interval))
    }
  }
}
