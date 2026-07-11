<template>
  <div class="cv-page" style="max-width: 900px">
      <a-typography-title :level="3">帮助中心</a-typography-title>

      <a-collapse v-model:activeKey="activeKey" accordion>
        <a-collapse-panel key="1" header="如何开始一堂新课？">
          <p>1. 在侧边栏点击"新建课堂"按钮（仅教师和管理员可见）</p>
          <p>2. 填写课程名称、授课教师姓名，选择课堂模式（普通/考试）</p>
          <p>3. 点击"创建课堂"按钮即可创建</p>
          <p>4. 创建后可在课堂列表中查看详情和开始上课</p>
        </a-collapse-panel>

        <a-collapse-panel key="2" header="如何注册学生人脸？">
          <p>1. 在侧边栏点击"学生管理"（教师）或"用户管理"（管理员）</p>
          <p>2. 在左侧注册区域填写姓名和角色</p>
          <p>3. 点击"打开摄像头"拍照或"上传照片"选择图片</p>
          <p>4. 确保照片中包含清晰的人脸，点击"注册"按钮</p>
          <p>注意：教师只能注册学生，管理员可注册学生和教师</p>
        </a-collapse-panel>

        <a-collapse-panel key="3" header="看板的三列代表什么？">
          <p><strong>教师视角：</strong>专注（注意力≥60）/ 一般（30≤注意力&lt;60）/ 分心（注意力&lt;30 或已结束）</p>
          <p><strong>学生视角：</strong>进行中 / 即将开始 / 已结束</p>
          <p><strong>管理员视角：</strong>活跃课堂 / 需关注 / 已结束</p>
        </a-collapse-panel>

        <a-collapse-panel key="4" header="如何使用搜索功能？">
          <p>在主页顶部的搜索框中输入关键词，可按课堂名称或教师姓名过滤看板。</p>
          <p>搜索结果会实时显示匹配数量，匹配的文本会高亮显示。</p>
          <p>点击搜索框右侧的 × 按钮可清除搜索条件。</p>
        </a-collapse-panel>

        <a-collapse-panel key="5" header="如何修改密码？">
          <p>1. 在侧边栏点击"设置"</p>
          <p>2. 在"修改密码"区域输入当前密码和新密码</p>
          <p>3. 新密码至少6位，需输入两次确认</p>
          <p>4. 点击"修改密码"按钮完成修改</p>
        </a-collapse-panel>

        <a-collapse-panel key="6" header="各角色的权限区别？">
          <p><strong>教师：</strong>创建课堂、管理学生、查看课堂详情、实时监控</p>
          <p><strong>学生：</strong>查看我的课堂、注意力报告、OJ训练</p>
          <p><strong>管理员：</strong>管理所有用户、创建课堂、数据分析、全局总览</p>
        </a-collapse-panel>

        <a-collapse-panel key="7" header="遇到问题怎么办？">
          <p>如果遇到技术问题或功能异常，请尝试：</p>
          <p>1. 清除浏览器缓存后重新登录</p>
          <p>2. 检查网络连接是否正常</p>
          <p>3. 确认使用的是正确的账号和密码</p>
          <p>4. 联系系统管理员获取帮助</p>
        </a-collapse-panel>
      </a-collapse>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const activeKey = ref('1')
</script>
