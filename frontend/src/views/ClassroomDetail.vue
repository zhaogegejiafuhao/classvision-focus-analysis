<template>
  <div class="cv-page" style="max-width: 1400px">
      <a-spin :spinning="loading">
        <a-skeleton v-if="loading && !classroom" active :paragraph="{ rows: 4 }" />
        <template v-if="classroom">
          <div class="page-header-wrap">
            <a-page-header :title="classroom.name" :sub-title="`${classroom.teacher} · ${classroom.duration}分钟`" style="padding: 0 0 16px 0" />
            <a-space v-if="canEditOrDelete || canManage">
              <a-button v-if="canManage && classroom.ended_at && !report" @click="genReport()" :loading="genLoading">
                <template #icon><FileOutlined /></template>
                生成报告
              </a-button>
              <a-button v-if="!classroom.ended_at && canManage" type="primary" @click="$router.push(`/live/${classroomId}`)">
                <template #icon><VideoCameraOutlined /></template>
                {{ classroom.started_at ? '进入课堂检测' : '开始课堂' }}
              </a-button>
              <a-button v-if="!classroom.ended_at && canManage" @click="handleEndClassroom" :loading="endLoading">
                <template #icon><CheckCircleOutlined /></template>
                结束课堂
              </a-button>
              <a-button v-if="canEditOrDelete" @click="openEditClassroom">
                <template #icon><EditOutlined /></template>
                编辑课堂
              </a-button>
              <a-popconfirm v-if="canEditOrDelete" title="确定删除该课堂？将同时删除所有关联数据（学生、记录、报告等）。" @confirm="handleDeleteClassroom">
                <a-button danger>
                  <template #icon><DeleteOutlined /></template>
                  删除课堂
                </a-button>
              </a-popconfirm>
            </a-space>
          </div>

          <a-row :gutter="16" style="margin-bottom: 16px">
            <a-col :span="6">
              <a-card><a-statistic title="总人数" :value="classroom.total_students" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="平均注意力" :value="classroom.avg_attention" suffix="/100" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="低头人次" :value="classroom.stats?.head_down_count || 0" :value-style="{ color: '#cf1322' }" /></a-card>
            </a-col>
            <a-col :span="6">
              <a-card><a-statistic title="疲劳人次" :value="classroom.stats?.fatigue_count || 0" :value-style="{ color: '#722ed1' }" /></a-card>
            </a-col>
          </a-row>

          <!-- 出席情况 -->
          <a-card title="出席情况" style="margin-bottom: 16px">
            <a-row :gutter="16">
              <a-col :span="6">
                <a-statistic title="已识别" :value="attendance.identified_count" :value-style="{ color: '#52c41a' }" />
              </a-col>
              <a-col :span="6">
                <a-statistic title="未识别" :value="attendance.unidentified_count" :value-style="{ color: '#faad14' }" />
              </a-col>
              <a-col :span="6">
                <a-statistic title="缺席（已注册）" :value="attendance.absent_count" :value-style="{ color: '#cf1322' }" />
              </a-col>
              <a-col :span="6">
                <a-button type="link" @click="showAttendanceModal = true">查看详情</a-button>
              </a-col>
            </a-row>
          </a-card>

          <!-- 注意力趋势 -->
          <a-card title="注意力趋势" style="margin-bottom: 16px">
            <div ref="timelineEl" style="width: 100%; height: 300px" />
          </a-card>

          <!-- 热力图 -->
          <a-card title="学生注意力热力图" style="margin-bottom: 16px">
            <a-alert message="热力图显示每个学生在不同时间段的注意力分布，颜色越绿表示注意力越高" type="info" show-icon style="margin-bottom: 12px" />
            <div ref="heatmapEl" style="width: 100%; height: 400px" />
          </a-card>

          <a-row :gutter="16">
            <a-col :span="12">
              <a-card title="学生列表">
                <template #extra>
                  <a-button v-if="canManage" type="primary" size="small" @click="openAddStudent">
                    <template #icon><PlusOutlined /></template>
                    添加学生
                  </a-button>
                </template>
                <a-table :columns="studentCols" :data-source="students" row-key="id" size="small">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'risk_level'">
                      <a-tag :color="record.risk_level === 'high' ? 'red' : record.risk_level === 'medium' ? 'orange' : 'green'">
                        {{ { low: '低风险', medium: '中风险', high: '高风险' }[record.risk_level] || '低风险' }}
                      </a-tag>
                    </template>
                    <template v-if="column.key === 'action'">
                      <a-space>
                        <a-button type="link" size="small" @click="openEditStudent(record)">编辑</a-button>
                        <a-popconfirm title="确定删除该学生？将同时删除其注意力记录。" @confirm="deleteStudent(record.id)">
                          <a-button type="link" danger size="small">删除</a-button>
                        </a-popconfirm>
                      </a-space>
                    </template>
                  </template>
                </a-table>
              </a-card>
            </a-col>
            <a-col :span="12">
              <!-- AI 报告：无报告时不显示 -->
              <a-card v-if="report" title="AI 课堂分析报告">
                <template #extra>
                  <a-space v-if="report && canManage" size="small">
                    <a-popconfirm title="确定重新生成报告？将覆盖当前内容。" @confirm="genReport(true)">
                      <a-button type="link" size="small" :loading="genLoading">
                        <template #icon><ReloadOutlined /></template>
                        重新生成
                      </a-button>
                    </a-popconfirm>
                    <a-popconfirm title="确定删除该报告？" @confirm="deleteReport">
                      <a-button type="link" danger size="small">
                        <template #icon><DeleteOutlined /></template>
                        删除
                      </a-button>
                    </a-popconfirm>
                  </a-space>
                </template>
                <div v-if="report">
                  <div v-html="renderMarkdown(report?.content)" style="max-height: 300px; overflow-y: auto" />
                  <a-typography-text type="secondary">
                    生成时间：{{ new Date(report.created_at).toLocaleString('zh-CN') }}
                  </a-typography-text>
                </div>
              </a-card>

              <!-- 对话区域 -->
              <a-card title="AI 智能对话" style="margin-top: 16px">
                <a-alert
                  message="AI 已接入知识库（RAG），自动检索相关文档辅助回答，您可以追问细节或请求更多建议"
                  type="info"
                  show-icon
                  style="margin-bottom: 12px"
                />
                <!-- 对话历史 -->
                <div ref="chatContainerRef" v-if="chatMessages.length > 0" class="chat-container">
                  <div v-for="msg in chatMessages" :key="msg.id" :class="['chat-msg', msg.role === 'user' ? 'chat-msg-user' : 'chat-msg-ai']">
                    <div v-if="msg.role === 'assistant'" class="chat-avatar">🤖</div>
                    <div class="chat-bubble-wrap">
                      <div :class="['chat-bubble', msg.role === 'user' ? 'bubble-user' : 'bubble-ai']">
                        <div v-if="msg.streaming && !msg.content" class="chat-loading">
                          <span class="dot-pulse"></span>
                          <span class="dot-pulse"></span>
                          <span class="dot-pulse"></span>
                          <span class="loading-text">{{ msg.loadingStage || 'AI 正在思考...' }}</span>
                        </div>
                        <div class="markdown-body" v-html="renderMarkdown(msg.content)" />
                        <span v-if="msg.streaming && msg.content" class="streaming-cursor">▌</span>
                      </div>
                      <div class="chat-meta">
                        <span class="chat-time">{{ new Date(msg.timestamp).toLocaleTimeString('zh-CN') }}</span>
                        <span v-if="msg.elapsed" class="chat-elapsed">{{ msg.elapsed }}</span>
                        <a-button v-if="msg.error" type="link" size="small" @click="retryChat(msg)">重试</a-button>
                      </div>
                    </div>
                    <div v-if="msg.role === 'user'" class="chat-avatar">👤</div>
                  </div>
                </div>
                <a-empty v-else description="暂无对话记录" style="margin-bottom: 16px" />

                <!-- 输入框 -->
                <div style="margin-bottom: 8px">
                  <a-radio-group v-model:value="chatMode" size="small" :disabled="chatLoading">
                    <a-radio-button value="fast">⚡ 快速回答</a-radio-button>
                    <a-radio-button value="deep">🧠 深度思考</a-radio-button>
                  </a-radio-group>
                  <span style="margin-left: 12px; font-size: 12px; color: #999">
                    {{ chatMode === 'fast'
                      ? '约 20-70 秒 | qwen3:4b 思考模式'
                      : '约 35-90 秒 | qwen3:4b 思考模式 + Reranker'
                    }}
                  </span>
                </div>
                <div class="chat-input-area">
                  <a-textarea
                    v-model:value="chatInput"
                    placeholder="输入问题，如：为什么疲劳人次这么高？（Enter 发送，Shift+Enter 换行）"
                    :auto-size="{ minRows: 1, maxRows: 4 }"
                    :disabled="chatLoading"
                    @keydown.enter.exact.prevent="sendChat()"
                  />
                  <a-button type="primary" @click="sendChat()" :loading="chatLoading" :disabled="!chatInput.trim()">
                    发送
                  </a-button>
                </div>

                <!-- 下载按钮 -->
                <a-space style="margin-top: 12px">
                  <a-button @click="downloadMarkdown" :disabled="chatMessages.length === 0 && !report">
                    下载完整报告（含对话记录）
                  </a-button>
                </a-space>
              </a-card>
            </a-col>
          </a-row>

          <!-- 教学模块 Tab -->
          <a-card title="教学活动" style="margin-top: 16px" v-if="canManage">
            <a-tabs v-model:activeKey="teachingTab">
              <a-tab-pane key="homework" tab="作业">
                <a-table :columns="hwColumns" :data-source="classHomeworks" row-key="id" size="small" :loading="hwLoading">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'status'">
                      <a-tag :color="{ open: 'blue', closed: 'gray' }[record.status] || 'default'">{{ { open: '进行中', closed: '已截止' }[record.status] || record.status }}</a-tag>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <a-button type="link" size="small" @click="$router.push(`/homework/${record.id}`)">详情</a-button>
                    </template>
                  </template>
                </a-table>
                <a-button type="primary" size="small" style="margin-top: 8px" @click="$router.push('/homework')">管理作业</a-button>
              </a-tab-pane>
              <a-tab-pane key="exam" tab="考试">
                <a-table :columns="examColumns" :data-source="classExams" row-key="id" size="small" :loading="examLoading">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'status'">
                      <a-tag :color="{ draft: 'default', published: 'blue', closed: 'gray' }[record.status] || 'default'">{{ { draft: '草稿', published: '已发布', closed: '已结束' }[record.status] || record.status }}</a-tag>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <a-button type="link" size="small" @click="$router.push(`/exams/${record.id}`)">详情</a-button>
                    </template>
                  </template>
                </a-table>
                <a-button type="primary" size="small" style="margin-top: 8px" @click="$router.push('/exams')">管理考试</a-button>
              </a-tab-pane>
              <a-tab-pane key="checkin" tab="签到">
                <a-table :columns="checkinColumns" :data-source="classCheckins" row-key="id" size="small" :loading="checkinLoading">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'status'">
                      <a-tag :color="record.status === 'active' ? 'green' : 'gray'">{{ record.status === 'active' ? '进行中' : '已结束' }}</a-tag>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <a-button type="link" size="small" @click="$router.push(`/checkin/${record.id}`)">详情</a-button>
                    </template>
                  </template>
                </a-table>
                <a-button type="primary" size="small" style="margin-top: 8px" @click="$router.push('/checkin')">管理签到</a-button>
              </a-tab-pane>
              <a-tab-pane key="materials" tab="课件">
                <a-list :data-source="classMaterials" :loading="materialLoading" size="small">
                  <template #renderItem="{ item }">
                    <a-list-item>
                      <a-list-item-meta>
                        <template #title>{{ item.title }}</template>
                        <template #description>{{ item.file_name }} · {{ formatFileSize(item.file_size) }}</template>
                      </a-list-item-meta>
                      <template #actions>
                        <a-button type="link" size="small" @click="downloadMaterial(item)">下载</a-button>
                      </template>
                    </a-list-item>
                  </template>
                  <template #footer>
                    <a-button type="primary" size="small" @click="$router.push('/materials')">管理课件</a-button>
                  </template>
                </a-list>
                <a-empty v-if="classMaterials.length === 0 && !materialLoading" description="暂无课件" />
              </a-tab-pane>
            </a-tabs>
          </a-card>
        </template>
        <a-empty v-else-if="!loading" description="课堂不存在" />
      </a-spin>

      <!-- 出席详情弹窗 -->
      <a-modal v-model:open="showAttendanceModal" title="出席详情" width="800px" :footer="null">
        <a-tabs>
          <a-tab-pane key="identified" tab="已识别">
            <a-table :data-source="attendance.identified" :columns="[
              { title: '姓名', dataIndex: 'name' },
              { title: '平均注意力', dataIndex: 'avg_attention' },
            ]" row-key="student_record_id" size="small" />
          </a-tab-pane>
          <a-tab-pane key="unidentified" tab="未识别">
            <a-table :data-source="attendance.unidentified" :columns="[
              { title: '跟踪ID', dataIndex: 'track_id' },
              { title: '平均注意力', dataIndex: 'avg_attention' },
            ]" row-key="student_record_id" size="small" />
          </a-tab-pane>
          <a-tab-pane key="absent" tab="缺席（已注册）">
            <a-table :data-source="attendance.absent" :columns="[
              { title: '姓名', dataIndex: 'name' },
            ]" row-key="id" size="small" />
          </a-tab-pane>
        </a-tabs>
      </a-modal>

      <!-- 编辑课堂弹窗 -->
      <a-modal
        v-model:open="editClassroomOpen"
        title="编辑课堂信息"
        @ok="handleEditClassroom"
        :confirm-loading="editClassroomSaving"
        ok-text="保存"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="课堂名称">
            <a-input v-model:value="editClassroomForm.name" />
          </a-form-item>
          <a-form-item label="教师">
            <a-input v-model:value="editClassroomForm.teacher" />
          </a-form-item>
          <a-form-item label="课序号">
            <a-input v-model:value="editClassroomForm.course_code" placeholder="例如：CS101" />
          </a-form-item>
          <a-form-item label="公开">
            <a-switch v-model:checked="editClassroomForm.is_public" checked-children="公开" un-checked-children="私有" />
          </a-form-item>
        </a-form>
      </a-modal>

      <!-- 添加学生弹窗 -->
      <a-modal
        v-model:open="addStudentOpen"
        title="添加学生到课堂"
        @ok="handleAddStudent"
        :confirm-loading="addStudentSaving"
        ok-text="添加"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="选择已注册人员" v-if="availablePersons.length > 0">
            <a-select
              v-model:value="addStudentForm.person_id"
              placeholder="选择已注册学生加入课堂"
              show-search
              :filter-option="filterPerson"
              allow-clear
              style="width: 100%"
            >
              <a-select-option v-for="p in availablePersons" :key="p.id" :value="p.id">
                {{ p.name }} ({{ p.username || 'ID:' + p.id }})
              </a-select-option>
            </a-select>
          </a-form-item>
          <a-alert v-else message="暂无可添加的已注册学生，请先到人员管理页面注册" type="info" show-icon style="margin-bottom: 12px" />
          <a-divider v-if="addStudentForm.person_id">或手动填写</a-divider>
          <a-form-item label="跟踪ID" :required="!addStudentForm.person_id">
            <a-input-number v-model:value="addStudentForm.track_id" :min="1" style="width: 100%" :disabled="!!addStudentForm.person_id" />
          </a-form-item>
          <a-form-item label="姓名">
            <a-input v-model:value="addStudentForm.name" placeholder="可选，选择已注册人员时自动填充" />
          </a-form-item>
        </a-form>
      </a-modal>

      <!-- 编辑学生弹窗 -->
      <a-modal
        v-model:open="editStudentOpen"
        title="编辑学生"
        @ok="handleEditStudent"
        :confirm-loading="editStudentSaving"
        ok-text="保存"
        cancel-text="取消"
      >
        <a-form layout="vertical">
          <a-form-item label="姓名">
            <a-input v-model:value="editStudentForm.name" />
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
</template>

<script setup>
import {
  CheckCircleOutlined, EditOutlined, DeleteOutlined,
  PlusOutlined, ReloadOutlined, VideoCameraOutlined, FileOutlined,
} from '@ant-design/icons-vue'
import { useClassroomDetail } from '@/composables/useClassroomDetail'

const {
  // 核心数据
  classroomId, classroom, students, report, loading,
  canManage, canEditOrDelete,
  // DOM 引用
  timelineEl, riskChartEl, riskTimelineEl, heatmapEl, chatContainerRef,
  // 考试风险
  examRisks, riskLoading, riskFilter, riskColumns, highRiskSummary, loadExamRisks,
  // 教学模块
  teachingTab, classHomeworks, classExams, classCheckins,
  hwLoading, examLoading, checkinLoading,
  classMaterials, materialLoading,
  hwColumns, examColumns, checkinColumns,
  // 出席情况
  attendance, showAttendanceModal,
  // 对话
  chatMessages, chatInput, chatLoading, chatMode,
  sendChat, retryChat, downloadMarkdown,
  // 学生表格
  studentCols,
  // 工具函数
  renderMarkdown, formatFileSize, downloadMaterial,
  // 课堂操作
  endLoading, handleEndClassroom, handleDeleteClassroom,
  editClassroomOpen, editClassroomSaving, editClassroomForm,
  openEditClassroom, handleEditClassroom,
  // 学生管理
  addStudentOpen, addStudentSaving, addStudentForm, availablePersons,
  filterPerson, openAddStudent, handleAddStudent,
  editStudentOpen, editStudentSaving, editStudentForm,
  openEditStudent, handleEditStudent, deleteStudent,
  // 报告
  genLoading, genReport, deleteReport,
} = useClassroomDetail()
</script>


<style scoped>
.page-header-wrap {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.markdown-body {
  font-size: 14px;
  line-height: 1.7;
  color: var(--cv-text-secondary, #475569);
}

.markdown-body :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 8px 0;
}
.markdown-body :deep(th),
.markdown-body :deep(td) {
  border: 1px solid #d9d9d9;
  padding: 6px 12px;
  text-align: left;
}
.markdown-body :deep(pre) {
  background: #f0f0f0;
  padding: 12px;
  border-radius: 4px;
  overflow-x: auto;
}
.markdown-body :deep(code) {
  background: #f0f0f0;
  padding: 2px 4px;
  border-radius: 3px;
  font-family: Consolas, Monaco, monospace;
  font-size: 0.9em;
}
.markdown-body :deep(pre code) {
  background: none;
  padding: 0;
}
.streaming-cursor {
  display: inline-block;
  animation: blink 1s step-end infinite;
  color: #52c41a;
  font-weight: bold;
}
@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

/* 聊天容器 */
.chat-container {
  max-height: 450px;
  overflow-y: auto;
  margin-bottom: 16px;
  scroll-behavior: smooth;
  padding: 4px;
}

/* 消息行 */
.chat-msg {
  display: flex;
  align-items: flex-start;
  margin-bottom: 16px;
  gap: 8px;
}
.chat-msg-user {
  flex-direction: row-reverse;
}
.chat-msg-ai {
  flex-direction: row;
}

/* 头像 */
.chat-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
  background: #f0f0f0;
}

/* 气泡容器 */
.chat-bubble-wrap {
  max-width: 75%;
  display: flex;
  flex-direction: column;
}
.chat-msg-user .chat-bubble-wrap {
  align-items: flex-end;
}
.chat-msg-ai .chat-bubble-wrap {
  align-items: flex-start;
}

/* 气泡 */
.chat-bubble {
  padding: 10px 14px;
  border-radius: 12px;
  word-break: break-word;
  line-height: 1.6;
}
.bubble-user {
  background: #1890ff;
  color: #fff;
  border-bottom-right-radius: 4px;
}
.bubble-ai {
  background: #f5f5f5;
  color: #333;
  border-bottom-left-radius: 4px;
}
.bubble-user .markdown-body {
  color: #fff;
}

/* 元数据 */
.chat-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 4px;
  font-size: 11px;
}
.chat-time {
  color: #bbb;
}
.chat-elapsed {
  color: #999;
  background: #f5f5f5;
  padding: 1px 6px;
  border-radius: 8px;
}

/* 加载动画 */
.chat-loading {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #999;
}
.dot-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #1890ff;
  animation: dotPulse 1.4s infinite ease-in-out;
}
.dot-pulse:nth-child(2) {
  animation-delay: 0.2s;
}
.dot-pulse:nth-child(3) {
  animation-delay: 0.4s;
}
.loading-text {
  margin-left: 6px;
  font-size: 13px;
}
@keyframes dotPulse {
  0%, 80%, 100% {
    transform: scale(0.6);
    opacity: 0.4;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}

/* 输入框区域 */
.chat-input-area {
  display: flex;
  gap: 8px;
  align-items: flex-end;
}
.chat-input-area .ant-input {
  flex: 1;
}
</style>
