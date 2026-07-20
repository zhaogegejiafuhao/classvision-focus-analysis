import axios from 'axios'
import { message } from 'ant-design-vue'

const api = axios.create({
  baseURL: '/api',
  timeout: 30000,
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

const errorMessages = {
  400: '请求参数错误',
  403: '没有权限执行此操作',
  404: '请求的资源不存在',
  408: '请求超时，请重试',
  429: '操作过于频繁，请稍后再试',
  500: '服务器内部错误',
  502: '服务暂时不可用',
  503: '服务维护中，请稍后再试',
}

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const status = error.response?.status
    const detail = error.response?.data?.detail

    if (status === 401) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      if (window.location.pathname !== '/' && window.location.pathname !== '/login') {
        window.location.href = '/'
      }
    } else if (status && status >= 400) {
      // 只对非页面主动处理的错误显示全局提示
      if (!error.config?._skipGlobalError) {
        const msg = detail || errorMessages[status] || `请求失败(${status})`
        message.error(msg)
      }
    } else if (!error.response) {
      message.error('网络连接失败，请检查网络')
    }
    return Promise.reject(error)
  }
)

export default api
