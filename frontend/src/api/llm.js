import api from './index'

/** 获取 LLM 配置（静默预取，失败不弹错误） */
export function getLlmConfig(opts = {}) {
  return api.get('/llm/config', { _skipGlobalError: true, ...opts })
}

/** 更新 LLM 配置 */
export function updateLlmConfig(payload) {
  return api.put('/llm/config', payload)
}

/** 测试 LLM 连接 */
export function testLlm() {
  return api.post('/llm/test')
}
