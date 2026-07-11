# UI/UX 整体优化方案

## Context

ClassVision 前端目前存在以下影响用户体验的问题：
- **颜色不统一**：存在 3 种"主色蓝"（`#3751FE` 53处、`#3461fd` 10处、`#1890ff` 8处），ant-design-vue 组件运行在默认 `#1677ff` 主题下
- **无设计令牌**：所有颜色、间距、圆角硬编码在各 .vue 文件的 scoped CSS 中
- **无页面过渡**：App.vue 是裸 `<router-view />`，路由切换无动画
- **响应式不足**：仅 MainLayout 和 Login 有 @media 断点，其余 14 个页面无适配
- **padding 不统一**：有 `24px 32px` 和 `24px` 两种写法，max-width 从 800px 到 1400px 共 5 种取值
- **无骨架屏**：首屏加载白屏 + spinner
- **HomePage.vue 残留旧布局**：未接入 MainLayout，路由 `/home` 孤立

本方案通过 4 个阶段的增量改进解决上述问题，不引入新依赖，不破坏现有功能。

---

## 阶段一：设计基础层（高影响低成本）

### 1.1 global.css — 建立 CSS 变量设计令牌

**文件**：`frontend/src/assets/styles/global.css`

在现有 reset 之后追加 `:root` 变量定义，将散落的硬编码值统一化：

```css
:root {
  --cv-color-primary: #3751FE;
  --cv-color-primary-hover: #5566ff;
  --cv-color-primary-active: #2d42d4;
  --cv-color-primary-bg: rgba(55, 81, 254, 0.08);
  --cv-color-primary-border: rgba(55, 81, 254, 0.3);
  --cv-text-primary: #1a1a2e;
  --cv-text-secondary: #374151;
  --cv-text-tertiary: #666;
  --cv-text-quaternary: #999;
  --cv-bg-page: #f5f6fa;
  --cv-bg-container: #fff;
  --cv-bg-subtle: #fafafa;
  --cv-border-light: #f0f0f0;
  --cv-border-base: #e0e0e0;
  --cv-color-success: #52c41a;
  --cv-color-warning: #faad14;
  --cv-color-error: #ef4444;
  --cv-spacing-page-x: 24px;
  --cv-spacing-page-y: 24px;
  --cv-page-max-width: 1200px;
  --cv-radius-sm: 6px;
  --cv-radius-base: 8px;
  --cv-radius-lg: 12px;
  --cv-shadow-card: 0 1px 2px rgba(0, 0, 0, 0.04);
  --cv-shadow-hover: 0 2px 8px rgba(55, 81, 254, 0.1);
  --cv-transition-base: all 0.2s ease;
  --cv-header-height: 56px;
  --cv-sider-width: 240px;
}
```

同时追加统一页面容器工具类：

```css
.cv-page {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  max-width: var(--cv-page-max-width);
  margin: 0 auto;
  width: 100%;
  min-height: calc(100vh - var(--cv-header-height));
}
.cv-page-full {
  padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x);
  width: 100%;
  min-height: calc(100vh - var(--cv-header-height));
}
```

### 1.2 App.vue — ConfigProvider 主题定制 + 全局路由过渡

**文件**：`frontend/src/App.vue`

从裸 `<router-view />` 升级为 ConfigProvider 包裹 + 页面过渡动画：

```vue
<template>
  <a-config-provider :theme="themeConfig">
    <router-view v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </a-config-provider>
</template>

<script setup>
const themeConfig = {
  token: {
    colorPrimary: '#3751FE',
    colorInfo: '#3751FE',
    colorSuccess: '#52c41a',
    colorWarning: '#faad14',
    colorError: '#ef4444',
    borderRadius: 8,
    fontFamily: '"Roboto-Regular", "PingFang SC", "Microsoft YaHei", sans-serif',
  },
  components: {
    Layout: { headerBg: '#fff', headerHeight: 56, siderBg: '#fff', bodyBg: '#f5f6fa' },
    Menu: { itemSelectedBg: 'rgba(55, 81, 254, 0.08)', itemSelectedColor: '#3751FE' },
  },
}
</script>

<style>
.page-fade-enter-active, .page-fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.page-fade-enter-from { opacity: 0; transform: translateY(8px); }
.page-fade-leave-to { opacity: 0; transform: translateY(-8px); }
</style>
```

---

## 阶段二：布局一致性 + 颜色统一

### 2.1 MainLayout.vue — 变量替换 + 子路由过渡

**文件**：`frontend/src/views/MainLayout.vue`

- 将 `<style scoped>` 中所有硬编码颜色（`#fff`、`#3751FE`、`#f5f6fa`、`#1a1a2e`、`#374151`、`#666`、`#f0f0f0` 等）替换为对应的 CSS 变量
- 在 `<a-layout-content>` 的 `<router-view>` 处添加与 App.vue 相同的 `<transition name="page-fade" mode="out-in">` 过渡

### 2.2 统一各页面 padding 和 max-width

**A 组 — 内联 style 页面（8个），改为 `class="cv-page"`**：

| 文件 | 原 max-width | 处理 |
|------|-------------|------|
| ClassroomList.vue | 1200px | 直接用 `cv-page` |
| Frame293293.vue (数据分析) | 1200px | 直接用 `cv-page` |
| Frame282357.vue (设置) | 800px | `cv-page` + `style="max-width: 800px"` |
| Frame27219.vue (日历) | 1000px | `cv-page` + `style="max-width: 1000px"` |
| ClassroomDetail.vue | 1400px | `cv-page` + `style="max-width: 1400px"` |
| RagPage.vue | 1400px | `cv-page` + `style="max-width: 1400px"` |
| PersonsPage.vue | 1400px | `cv-page` + `style="max-width: 1400px"` |
| Frame17448.vue (帮助) | 900px | `cv-page` + `style="max-width: 900px"` |

**B 组 — scoped class 页面（6个），padding 值替换为变量**：

OjProblemList.vue、OjProblemDetail.vue、OjSubmissions.vue、Frame281780.vue、Frame293744.vue、Frame281518.vue — 将 `padding: 24px 32px` 统一为 `padding: var(--cv-spacing-page-y) var(--cv-spacing-page-x)`（消除 32px 不一致）。

### 2.3 颜色统一

- **Frame04.vue**：8 处 `#3461fd` → `var(--cv-color-primary)`
- **Frame281518.vue**：1 处 `#3461fd`（JS 中）→ `'#3751FE'`
- **Frame293744.vue**：1 处 `#3461fd` → `var(--cv-color-primary)`
- **RagPage.vue**：4 处 `#1890ff`（UI 元素）→ `var(--cv-color-primary)`
- **Frame27219.vue**：1 处 `#1890ff`（a-avatar 背景）→ `var(--cv-color-primary)`
- **保留 `#1890ff`**：ClassroomDetail.vue、Frame293293.vue、LivePage.vue 中 echarts 图表数据色（不涉及品牌一致性）

---

## 阶段三：响应式 + 骨架屏

### 3.1 MainLayout 响应式增强

**文件**：`frontend/src/views/MainLayout.vue`

- 平板端（769px-1024px）：默认收起侧边栏（JS 监听 resize）
- 移动端（≤768px）：侧边栏 overlay + 阴影，header 隐藏用户名，隐藏标题
- script 中添加 `checkScreenWidth` 函数 + resize 监听

### 3.2 关键列表页骨架屏

为 3 个最常访问的列表页添加 `a-skeleton`（仅首次加载 `data.length === 0` 时显示）：

- **OjProblemList.vue**：`<a-skeleton active :paragraph="{ rows: 8 }" />`
- **ClassroomList.vue**：`<a-skeleton active :paragraph="{ rows: 6 }" />`
- **Frame293744.vue**（注意力报告）：`<a-skeleton active :paragraph="{ rows: 4 }" />`

---

## 阶段四：微交互 + 清理

### 4.1 全局微交互类

**文件**：`frontend/src/assets/styles/global.css`

追加 `.cv-card-hover`（hover 抬升）、`.cv-btn-press`（点击缩放）、`.cv-fade-in`（入场动画）工具类。

### 4.2 HomePage 路由重定向

**文件**：`frontend/src/router/index.js`

```js
// 原: { path: '/home', name: 'home', component: () => import('@/views/HomePage.vue') },
// 改为:
{ path: '/home', redirect: '/app' },
```

已确认无其他代码 `router.push('/home')`。HomePage.vue 的"开始课堂"功能已在 Frame04 的"新建课堂"模态框中实现。

---

## 验证方法

1. **颜色一致性**：浏览器 DevTools 检查 `<a-button type="primary">` 计算样式应为 `#3751FE`；Frame04 看板页蓝色元素与其他页面一致
2. **页面过渡**：在侧边栏菜单间切换，内容区应有 0.2s 淡入淡出 + 位移
3. **响应式**：DevTools 切换设备至 iPad（768px-1024px）侧边栏自动收起；iPhone 375px 侧边栏 overlay
4. **骨架屏**：DevTools Network → Slow 3G，首次进入 OjProblemList 应显示骨架屏动画
5. **padding 统一**：各页面左右 padding 均为 24px
6. **HomePage 重定向**：访问 `/home` 自动跳转 `/app`
7. **功能回归**：OJ 判题、课堂创建、RAG 问答等核心功能不受影响

## 实施顺序

阶段一 → 阶段二 → 阶段三 → 阶段四（每阶段完成后独立验证）
