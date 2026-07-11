<template>
  <div class="landing-page">
    <!-- 顶部导航栏（HiFiVE 风格） -->
    <header class="nav-bar">
      <div class="nav-logo" @click="scrollTo('hero')">ClassEyes</div>
      <nav class="nav-links">
        <a class="nav-link" @click="scrollTo('features')">产品功能</a>
        <a class="nav-link" @click="scrollTo('classroom')">课堂管理</a>
        <a class="nav-link" @click="scrollTo('ai')">AI 助教</a>
        <a class="nav-link" @click="scrollTo('analytics')">学情分析</a>
        <a class="nav-link" @click="scrollTo('docs')">帮助文档</a>
      </nav>
      <div class="nav-actions">
        <!-- 登录按钮 - 悬停/点击下拉 -->
        <div class="role-dropdown" :class="{ open: loginOpen }" @mouseleave="loginOpen = false">
          <button class="btn-ghost" @click="toggleLogin">登录</button>
          <div class="dropdown-menu">
            <div class="dropdown-item" @click="goLogin('student')">
              <span class="dropdown-icon">📚</span>
              <span>我是学生</span>
            </div>
            <div class="dropdown-item" @click="goLogin('teacher')">
              <span class="dropdown-icon">📋</span>
              <span>我是教师</span>
            </div>
            <div class="dropdown-item" @click="goLogin('admin')">
              <span class="dropdown-icon">⚙️</span>
              <span>我是管理员</span>
            </div>
          </div>
        </div>
        <!-- 注册按钮 - 悬停/点击下拉 -->
        <div class="role-dropdown" :class="{ open: registerOpen }" @mouseleave="registerOpen = false">
          <button class="btn-filled" @click="toggleRegister">注册</button>
          <div class="dropdown-menu">
            <div class="dropdown-item" @click="goRegister('student')">
              <span class="dropdown-icon">📚</span>
              <span>我是学生</span>
            </div>
            <div class="dropdown-item" @click="goRegister('teacher')">
              <span class="dropdown-icon">📋</span>
              <span>我是教师</span>
            </div>
            <div class="dropdown-item" @click="goRegister('admin')">
              <span class="dropdown-icon">⚙️</span>
              <span>我是管理员</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Hero 区域 -->
    <section id="hero" class="hero-section">
      <div class="hero-bg"></div>
      <div class="hero-content">
        <h1 class="hero-title">课堂学情<br />智能实训平台</h1>
        <p class="hero-subtitle">AI 驱动的一站式课堂教学管理解决方案<br />实时学情监测 · 三端协同 · 数据驱动决策</p>
        <button class="btn-experience" @click="scrollTo('features')">
          立即体验
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>
      <div class="hero-scroll-hint" @click="scrollTo('features')">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
      </div>
    </section>

    <!-- 我们的优势 -->
    <section id="features" class="advantage-section">
      <h2 class="section-title">我们的优势</h2>
      <div class="advantage-cards">
        <div class="advantage-card">
          <div class="card-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#3751FE" stroke-width="1.5"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 4v6l4 2"/></svg>
          </div>
          <h3 class="card-title">AI 智能分析</h3>
          <p class="card-desc">实时采集课堂数据，AI 算法智能分析学情，让教学有据可依</p>
        </div>
        <div class="advantage-card">
          <div class="card-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#3751FE" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3 class="card-title">三端协同</h3>
          <p class="card-desc">教师、学生、管理员三端差异化界面，各司其职，高效协作</p>
        </div>
        <div class="advantage-card">
          <div class="card-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#3751FE" stroke-width="1.5"><path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"/></svg>
          </div>
          <h3 class="card-title">数据驱动</h3>
          <p class="card-desc">人脸识别考勤，学情报告自动生成，教学决策有据可依</p>
        </div>
      </div>
    </section>

    <!-- 满足多场景需要 -->
    <section class="scenario-section">
      <h2 class="section-title">满足多场景需要</h2>
      <p class="section-subtitle">深度理解教学场景，为课堂提供全方位智能管理</p>
      <div class="scenario-tags">
        <div class="scenario-tag active">课堂管理</div>
        <div class="scenario-tag">实时监控</div>
        <div class="scenario-tag">学情分析</div>
        <div class="scenario-tag">OJ 训练</div>
        <div class="scenario-tag">AI 助教</div>
        <div class="scenario-tag">人脸考勤</div>
      </div>
    </section>

    <!-- 核心功能 -->
    <section id="classroom" class="feature-section">
      <div class="feature-block">
        <div class="feature-text">
          <h2 class="feature-title">课堂管理</h2>
          <p class="feature-desc">创建课堂、管理学生、一键开始授课。支持课堂详情查看、学生名单管理，让课堂组织更加高效有序。</p>
          <ul class="feature-list">
            <li>✓ 一键创建课堂，自动生成课堂编号</li>
            <li>✓ 学生名单管理，人脸识别注册</li>
            <li>✓ 课堂状态实时跟踪</li>
          </ul>
        </div>
        <div class="feature-visual classroom-visual">
          <div class="mock-window">
            <div class="mock-titlebar">
              <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
            </div>
            <div class="mock-content">
              <div class="mock-sidebar">
                <div class="mock-nav-item active">首页</div>
                <div class="mock-nav-item">课堂管理</div>
                <div class="mock-nav-item">课程日历</div>
                <div class="mock-nav-item">RAG 文档库</div>
              </div>
              <div class="mock-main">
                <div class="mock-card">课堂 A</div>
                <div class="mock-card">课堂 B</div>
                <div class="mock-card">课堂 C</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="ai" class="feature-section alt-bg">
      <div class="feature-block reverse">
        <div class="feature-text">
          <h2 class="feature-title">AI 助教问答</h2>
          <p class="feature-desc">基于 RAG 文档库的智能问答系统，辅助教师教学。上传教学资料，AI 自动构建知识库，随时解答学生疑问。</p>
          <ul class="feature-list">
            <li>✓ 教学文档自动入库，智能检索</li>
            <li>✓ 自然语言问答，即时响应</li>
            <li>✓ 支持多种文档格式</li>
          </ul>
        </div>
        <div class="feature-visual ai-visual">
          <div class="mock-chat">
            <div class="chat-msg user">什么是快速排序？</div>
            <div class="chat-msg bot">快速排序是一种分治算法...</div>
            <div class="chat-input">
              <span>输入问题...</span>
              <button class="send-btn">发送</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="analytics" class="feature-section">
      <div class="feature-block">
        <div class="feature-text">
          <h2 class="feature-title">学情分析与报告</h2>
          <p class="feature-desc">课堂参与度、学习数据可视化呈现。学情报告自动生成，帮助教师精准掌握学生学习状态。</p>
          <ul class="feature-list">
            <li>✓ 课堂参与度实时统计</li>
            <li>✓ 学习数据可视化看板</li>
            <li>✓ 学情报告自动生成</li>
          </ul>
        </div>
        <div class="feature-visual analytics-visual">
          <div class="mock-dashboard">
            <div class="dash-card">
              <div class="dash-label">出勤率</div>
              <div class="dash-value">96%</div>
            </div>
            <div class="dash-card">
              <div class="dash-label">参与度</div>
              <div class="dash-value">87%</div>
            </div>
            <div class="dash-chart">
              <div class="bar" style="height: 60%"></div>
              <div class="bar" style="height: 80%"></div>
              <div class="bar" style="height: 45%"></div>
              <div class="bar" style="height: 90%"></div>
              <div class="bar" style="height: 70%"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- OJ 编程训练 -->
    <section class="feature-section alt-bg">
      <div class="feature-block reverse">
        <div class="feature-text">
          <h2 class="feature-title">OJ 编程训练</h2>
          <p class="feature-desc">在线编程练习，自动评判。集成 WebIDE 编辑器，支持代码提交、运行测试，助力编程教学。</p>
          <ul class="feature-list">
            <li>✓ Monaco Editor 在线编码</li>
            <li>✓ 代码提交自动评判</li>
            <li>✓ 运行结果实时反馈</li>
          </ul>
        </div>
        <div class="feature-visual oj-visual">
          <div class="mock-editor">
            <div class="editor-tabs">
              <span class="tab active">main.py</span>
            </div>
            <div class="editor-code">
              <div class="code-line">def quicksort(arr):</div>
              <div class="code-line indent">if len(arr) &lt;= 1:</div>
              <div class="code-line indent2">return arr</div>
              <div class="code-line indent">pivot = arr[0]</div>
              <div class="code-line indent">return quicksort(left)</div>
            </div>
            <div class="editor-status">
              <span class="status-pass">✓ 通过</span>
              <span class="status-time">12ms</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA 区域 -->
    <section class="cta-section">
      <div class="cta-content">
        <h2 class="cta-title">开启智能教学新体验</h2>
        <p class="cta-desc">立即选择您的身份，开始使用 ClassEyes 课堂学情智能实训平台</p>
        <div class="cta-buttons">
          <button class="btn-cta" @click="goLogin('teacher')">教师登录</button>
          <button class="btn-cta" @click="goLogin('student')">学生登录</button>
          <button class="btn-cta" @click="goLogin('admin')">管理员登录</button>
        </div>
      </div>
    </section>

    <!-- 页脚 -->
    <footer id="docs" class="footer">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="footer-logo">ClassEyes</div>
          <p class="footer-desc">课堂学情智能实训平台<br />AI 驱动的一站式课堂教学管理解决方案</p>
        </div>
        <div class="footer-links">
          <div class="footer-col">
            <h4 class="footer-title">产品功能</h4>
            <a href="javascript:void(0)" @click.prevent="scrollTo('classroom')">课堂管理</a>
            <a href="javascript:void(0)" @click.prevent="scrollTo('ai')">AI 助教</a>
            <a href="javascript:void(0)" @click.prevent="scrollTo('analytics')">学情分析</a>
          </div>
          <div class="footer-col">
            <h4 class="footer-title">帮助文档</h4>
            <a href="javascript:void(0)" @click.prevent="goLogin('teacher')">用户指南</a>
            <a href="javascript:void(0)" @click.prevent="goLogin('admin')">管理员手册</a>
            <a href="javascript:void(0)" @click.prevent="scrollTo('hero')">关于我们</a>
          </div>
          <div class="footer-col">
            <h4 class="footer-title">快速入口</h4>
            <a href="javascript:void(0)" @click.prevent="goLogin('student')">学生入口</a>
            <a href="javascript:void(0)" @click.prevent="goLogin('teacher')">教师入口</a>
            <a href="javascript:void(0)" @click.prevent="goLogin('admin')">管理员入口</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 ClassEyes 课堂学情智能实训平台</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const loginOpen = ref(false)
const registerOpen = ref(false)

onMounted(() => {
  document.body.style.overflow = 'auto'
  document.body.style.height = 'auto'
})

onUnmounted(() => {
  document.body.style.overflow = ''
  document.body.style.height = ''
})

function toggleLogin() {
  loginOpen.value = !loginOpen.value
  registerOpen.value = false
}

function toggleRegister() {
  registerOpen.value = !registerOpen.value
  loginOpen.value = false
}

function scrollTo(id) {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' })
  }
}

function goLogin(role) {
  loginOpen.value = false
  router.push({ path: '/login', query: { role, mode: 'login' } })
}

function goRegister(role) {
  registerOpen.value = false
  router.push({ path: '/login', query: { role, mode: 'register' } })
}
</script>

<style scoped>
.landing-page {
  font-family: "Roboto-Regular", "PingFang SC", "Microsoft YaHei", sans-serif;
  color: #1a1a2e;
  background: #ffffff;
}

/* 导航栏 */
.nav-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 72px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  align-items: center;
  padding: 0 100px;
  z-index: 1000;
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.04);
}

.nav-logo {
  font-size: 24px;
  font-weight: 700;
  color: #3751FE;
  cursor: pointer;
  letter-spacing: -0.5px;
}

.nav-links {
  display: flex;
  gap: 48px;
  margin-left: 80px;
  flex: 1;
}

.nav-link {
  font-size: 16px;
  color: #333;
  cursor: pointer;
  transition: color 0.2s;
  position: relative;
  text-decoration: none;
}

.nav-link:hover {
  color: #3751FE;
}

.nav-link:hover::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 0;
  right: 0;
  height: 2px;
  background: #3751FE;
  border-radius: 1px;
}

.nav-actions {
  display: flex;
  gap: 12px;
  position: relative;
}

/* 角色下拉 */
.role-dropdown {
  position: relative;
}

.btn-ghost {
  padding: 8px 24px;
  font-size: 15px;
  color: #333;
  background: transparent;
  border: 1px solid #d0d0d0;
  border-radius: 100px;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.btn-ghost:hover {
  border-color: #3751FE;
  color: #3751FE;
}

.btn-filled {
  padding: 8px 24px;
  font-size: 15px;
  color: #fff;
  background: #3751FE;
  border: 1px solid #3751FE;
  border-radius: 100px;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.btn-filled:hover {
  background: #2d42d4;
  border-color: #2d42d4;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  padding: 8px;
  min-width: 180px;
  z-index: 1001;
  opacity: 0;
  visibility: hidden;
  transition: all 0.2s ease;
}

.role-dropdown:hover .dropdown-menu,
.role-dropdown.open .dropdown-menu {
  opacity: 1;
  visibility: visible;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  font-size: 15px;
  color: #333;
  cursor: pointer;
  border-radius: 8px;
  transition: background 0.15s;
  white-space: nowrap;
}

.dropdown-item:hover {
  background: #f5f6ff;
  color: #3751FE;
}

.dropdown-icon {
  font-size: 18px;
}

/* Hero */
.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding-top: 72px;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #f5f7ff 0%, #e8ecff 40%, #f0f2ff 100%);
  z-index: 0;
}

.hero-bg::before {
  content: '';
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(55, 81, 254, 0.12) 0%, transparent 70%);
  top: -200px;
  right: -100px;
  border-radius: 50%;
}

.hero-bg::after {
  content: '';
  position: absolute;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(55, 81, 254, 0.08) 0%, transparent 70%);
  bottom: -150px;
  left: -100px;
  border-radius: 50%;
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  max-width: 800px;
  padding: 0 40px;
}

.hero-title {
  font-size: 56px;
  font-weight: 800;
  color: #1a1a2e;
  margin: 0 0 24px 0;
  line-height: 1.3;
  letter-spacing: -1px;
}

.hero-subtitle {
  font-size: 20px;
  color: #555;
  margin: 0 0 40px 0;
  line-height: 1.6;
}

.btn-experience {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 16px 40px;
  font-size: 17px;
  font-weight: 600;
  color: #fff;
  background: #3751FE;
  border: none;
  border-radius: 100px;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 8px 24px rgba(55, 81, 254, 0.3);
}

.btn-experience:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(55, 81, 254, 0.4);
  background: #2d42d4;
}

.hero-scroll-hint {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  color: #999;
  cursor: pointer;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(8px); }
}

/* 通用 section 标题 */
.section-title {
  font-size: 36px;
  font-weight: 700;
  text-align: center;
  margin: 0 0 16px 0;
  color: #1a1a2e;
}

.section-subtitle {
  font-size: 18px;
  color: #666;
  text-align: center;
  margin: 0 0 48px 0;
}

/* 优势区域 */
.advantage-section {
  padding: 100px 100px;
  background: #fff;
}

.advantage-cards {
  display: flex;
  gap: 32px;
  max-width: 1200px;
  margin: 60px auto 0;
}

.advantage-card {
  flex: 1;
  padding: 40px 32px;
  background: #f9faff;
  border: 1px solid #e8ecff;
  border-radius: 16px;
  text-align: center;
  transition: all 0.3s;
}

.advantage-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(55, 81, 254, 0.1);
  border-color: #3751FE;
}

.card-icon {
  width: 72px;
  height: 72px;
  margin: 0 auto 20px;
  background: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(55, 81, 254, 0.08);
}

.card-title {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a2e;
  margin: 0 0 12px 0;
}

.card-desc {
  font-size: 15px;
  color: #666;
  line-height: 1.6;
  margin: 0;
}

/* 场景区域 */
.scenario-section {
  padding: 80px 100px;
  background: #f5f7ff;
}

.scenario-tags {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
  max-width: 1000px;
  margin: 0 auto;
}

.scenario-tag {
  padding: 14px 32px;
  font-size: 17px;
  color: #555;
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 100px;
  cursor: pointer;
  transition: all 0.2s;
}

.scenario-tag:hover,
.scenario-tag.active {
  color: #fff;
  background: #3751FE;
  border-color: #3751FE;
  box-shadow: 0 4px 12px rgba(55, 81, 254, 0.3);
}

/* 核心功能区 */
.feature-section {
  padding: 100px;
}

.feature-section.alt-bg {
  background: #f9faff;
}

.feature-block {
  display: flex;
  align-items: center;
  gap: 60px;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-block.reverse {
  flex-direction: row-reverse;
}

.feature-text {
  flex: 1;
}

.feature-title {
  font-size: 32px;
  font-weight: 700;
  color: #1a1a2e;
  margin: 0 0 16px 0;
}

.feature-desc {
  font-size: 17px;
  color: #555;
  line-height: 1.7;
  margin: 0 0 24px 0;
}

.feature-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.feature-list li {
  font-size: 15px;
  color: #444;
  padding: 8px 0;
  line-height: 1.6;
}

.feature-visual {
  flex: 1;
  min-height: 360px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Mock 窗口 - 课堂管理 */
.mock-window {
  width: 100%;
  max-width: 480px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
  overflow: hidden;
}

.mock-titlebar {
  height: 36px;
  background: #f5f5f5;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 0 16px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.dot.red { background: #ff5f57; }
.dot.yellow { background: #febc2e; }
.dot.green { background: #28c840; }

.mock-content {
  display: flex;
  height: 320px;
}

.mock-sidebar {
  width: 140px;
  background: #fafafe;
  padding: 16px 0;
  border-right: 1px solid #f0f0f0;
}

.mock-nav-item {
  padding: 10px 20px;
  font-size: 14px;
  color: #666;
  cursor: default;
}

.mock-nav-item.active {
  background: #eef1ff;
  color: #3751FE;
  font-weight: 600;
  border-left: 3px solid #3751FE;
}

.mock-main {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-content: flex-start;
}

.mock-card {
  width: calc(50% - 6px);
  height: 70px;
  background: #f5f7ff;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: #3751FE;
  font-weight: 600;
  border: 1px solid #e8ecff;
}

/* Mock 聊天 - AI 助教 */
.mock-chat {
  width: 100%;
  max-width: 420px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.chat-msg {
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 14px;
  max-width: 80%;
  line-height: 1.5;
}

.chat-msg.user {
  background: #3751FE;
  color: #fff;
  align-self: flex-end;
  border-bottom-right-radius: 4px;
}

.chat-msg.bot {
  background: #f5f7ff;
  color: #333;
  align-self: flex-start;
  border-bottom-left-radius: 4px;
}

.chat-input {
  display: flex;
  gap: 8px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.chat-input span {
  flex: 1;
  padding: 10px 14px;
  background: #f5f5f5;
  border-radius: 8px;
  font-size: 14px;
  color: #999;
}

.send-btn {
  padding: 10px 20px;
  background: #3751FE;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
}

/* Mock 仪表盘 - 学情分析 */
.mock-dashboard {
  width: 100%;
  max-width: 420px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
  padding: 24px;
}

.dash-card {
  display: inline-block;
  width: calc(50% - 8px);
  background: #f5f7ff;
  border-radius: 10px;
  padding: 16px;
  margin-bottom: 12px;
}

.dash-card:nth-child(2) {
  margin-left: 8px;
}

.dash-label {
  font-size: 13px;
  color: #888;
  margin-bottom: 6px;
}

.dash-value {
  font-size: 28px;
  font-weight: 700;
  color: #3751FE;
}

.dash-chart {
  display: flex;
  align-items: flex-end;
  gap: 16px;
  height: 120px;
  padding: 16px 0;
  border-top: 1px solid #f0f0f0;
}

.bar {
  flex: 1;
  background: linear-gradient(180deg, #3751FE 0%, #6b83ff 100%);
  border-radius: 6px 6px 0 0;
  min-height: 20px;
}

/* Mock 编辑器 - OJ */
.mock-editor {
  width: 100%;
  max-width: 480px;
  background: #1e1e2e;
  border-radius: 12px;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.editor-tabs {
  background: #2a2a3e;
  padding: 8px 16px;
}

.tab {
  font-size: 13px;
  color: #888;
  padding: 6px 12px;
  border-radius: 6px 6px 0 0;
}

.tab.active {
  color: #fff;
  background: #1e1e2e;
}

.editor-code {
  padding: 20px;
  font-family: "Fira Code", "Consolas", monospace;
  font-size: 13px;
  line-height: 1.8;
  min-height: 180px;
}

.code-line {
  color: #c5c8d6;
}

.code-line.indent { padding-left: 24px; color: #61afef; }
.code-line.indent2 { padding-left: 48px; color: #98c379; }

.editor-status {
  padding: 10px 16px;
  background: #2a2a3e;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.status-pass {
  color: #28c840;
  font-size: 13px;
  font-weight: 600;
}

.status-time {
  color: #888;
  font-size: 13px;
}

/* CTA 区域 */
.cta-section {
  padding: 100px 40px;
  background: linear-gradient(135deg, #3751FE 0%, #5570ff 100%);
  text-align: center;
}

.cta-title {
  font-size: 36px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 16px 0;
}

.cta-desc {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.85);
  margin: 0 0 40px 0;
}

.cta-buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.btn-cta {
  padding: 14px 36px;
  font-size: 16px;
  font-weight: 600;
  color: #3751FE;
  background: #fff;
  border: none;
  border-radius: 100px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

/* 页脚 */
.footer {
  background: #1a1a2e;
  color: #999;
  padding: 60px 100px 0;
}

.footer-content {
  display: flex;
  gap: 80px;
  max-width: 1200px;
  margin: 0 auto;
  padding-bottom: 40px;
}

.footer-brand {
  flex: 1;
}

.footer-logo {
  font-size: 24px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 12px;
}

.footer-desc {
  font-size: 14px;
  line-height: 1.7;
  color: #888;
}

.footer-links {
  display: flex;
  gap: 60px;
}

.footer-col {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-title {
  font-size: 15px;
  color: #fff;
  margin: 0 0 4px 0;
}

.footer-col a {
  font-size: 14px;
  color: #888;
  cursor: pointer;
  transition: color 0.2s;
  text-decoration: none;
}

.footer-col a:hover {
  color: #3751FE;
}

.footer-bottom {
  border-top: 1px solid #2a2a3e;
  padding: 24px 0;
  text-align: center;
}

.footer-bottom p {
  font-size: 13px;
  color: #666;
  margin: 0;
}

/* 响应式 */
@media (max-width: 1024px) {
  .nav-bar { padding: 0 40px; }
  .nav-links { gap: 32px; margin-left: 40px; }
  .advantage-section, .scenario-section, .feature-section { padding: 60px 40px; }
  .hero-title { font-size: 40px; }
  .advantage-cards { flex-direction: column; }
  .feature-block { flex-direction: column; gap: 40px; }
  .feature-block.reverse { flex-direction: column; }
}

@media (max-width: 768px) {
  .nav-bar { padding: 0 20px; height: 60px; }
  .nav-links { display: none; }
  .nav-actions { gap: 8px; }
  .btn-ghost, .btn-filled { padding: 6px 16px; font-size: 14px; }
  .hero-title { font-size: 28px; }
  .hero-subtitle { font-size: 16px; }
  .section-title { font-size: 26px; }
  .advantage-section, .scenario-section, .feature-section { padding: 40px 20px; }
  .cta-section { padding: 60px 20px; }
  .cta-buttons { flex-direction: column; align-items: center; }
  .footer { padding: 40px 20px 0; }
  .footer-content { flex-direction: column; gap: 32px; }
  .footer-links { flex-wrap: wrap; gap: 32px; }
}
</style>
