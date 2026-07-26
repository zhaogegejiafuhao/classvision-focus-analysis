import pluginVue from 'eslint-plugin-vue'

// 浏览器 + Node 全局变量
const browserGlobals = [
  'window', 'document', 'navigator', 'location', 'history', 'console',
  'fetch', 'URL', 'URLSearchParams', 'Blob', 'File', 'FormData',
  'localStorage', 'sessionStorage', 'setTimeout', 'setInterval',
  'clearTimeout', 'clearInterval', 'requestAnimationFrame', 'cancelAnimationFrame',
  'WebSocket', 'Event', 'EventSource', 'Image', 'HTMLCanvasElement',
  'mediaDevices', 'alert', 'confirm', 'prompt', 'open',
]
const nodeGlobals = ['process', 'require', 'module', '__dirname', '__filename', 'Buffer', 'global']

const globals = {}
;[...browserGlobals, ...nodeGlobals].forEach((name) => {
  globals[name] = 'readonly'
})

export default [
  // Vue 推荐规则集
  ...pluginVue.configs['flat/recommended'],

  // 全局忽略
  {
    ignores: ['dist/**', 'node_modules/**', '*.config.js', 'eslint.config.js'],
  },

  // 项目配置
  {
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals,
    },
    rules: {
      // ─── 严重等级调整 ───────────────────────────────
      // 从 error 降为 warn，避免一次性阻塞整个项目
      'no-unused-vars': ['warn', { argsIgnorePattern: '^_', varsIgnorePattern: '^_' }],
      'no-console': 'off',
      'no-debugger': 'warn',
      'no-undef': 'warn',

      // ─── Vue 规则调整 ────────────────────────────────
      'vue/multi-word-component-names': 'off',
      'vue/max-attributes-per-line': 'off',
      'vue/singleline-html-element-content-newline': 'off',
      'vue/html-self-closing': 'off',
      'vue/attributes-order': 'warn',
      'vue/v-bind-style': 'error',
      'vue/v-on-style': 'error',
      // 降级为 warn：项目历史代码存在 inbox-outlined 等小写组件名，逐步迁移
      'vue/component-name-in-template-casing': ['warn', 'PascalCase'],
      'vue/no-v-html': 'off',
      'vue/no-unused-vars': 'warn',
      // 降级为 warn：7 处 prop mutation 是真实反模式，需重构组件交互，列为技术债
      'vue/no-mutating-props': 'warn',
    },
  },
]
