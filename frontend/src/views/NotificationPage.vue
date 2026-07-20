<template>
  <div class="cv-page">
    <a-page-header title="消息通知" sub-title="查看和管理系统通知">
      <template #extra>
        <a-space>
          <a-select v-model:value="filterType" style="width: 120px" allow-clear placeholder="类型筛选">
            <a-select-option value="homework">作业</a-select-option>
            <a-select-option value="exam">考试</a-select-option>
            <a-select-option value="attendance">签到</a-select-option>
            <a-select-option value="system">系统</a-select-option>
          </a-select>
          <a-button v-if="notifications.length > 0" @click="markAllRead" :loading="loading">
            全部标记已读
          </a-button>
        </a-space>
      </template>
    </a-page-header>

    <a-spin :spinning="loading">
      <a-list
        v-if="filteredNotifications.length > 0"
        :data-source="filteredNotifications"
        :pagination="{ pageSize: 10 }"
      >
        <template #renderItem="{ item }">
          <a-list-item :class="{ 'unread-item': !item.is_read }">
            <a-list-item-meta>
              <template #avatar>
                <a-badge :dot="!item.is_read">
                  <a-avatar :style="getAvatarStyle(item.type)">
                    {{ getAvatarIcon(item.type) }}
                  </a-avatar>
                </a-badge>
              </template>
              <template #title>
                <span :style="{ fontWeight: item.is_read ? 'normal' : 'bold' }">
                  {{ item.title }}
                </span>
                <a-tag v-if="!item.is_read" color="blue" style="margin-left: 8px">未读</a-tag>
              </template>
              <template #description>
                <div>{{ item.content }}</div>
                <div style="margin-top: 4px; font-size: 12px; color: #999">
                  <span v-if="item.sender_name">发送人: {{ item.sender_name }}</span>
                  <span style="margin-left: 12px">{{ formatTime(item.created_at) }}</span>
                </div>
              </template>
            </a-list-item-meta>
            <template #actions>
              <a-button v-if="!item.is_read" type="link" size="small" @click="markRead(item.id)">
                标记已读
              </a-button>
              <a-popconfirm title="确定删除此通知？" @confirm="deleteNotification(item.id)">
                <a-button type="link" danger size="small">删除</a-button>
              </a-popconfirm>
            </template>
          </a-list-item>
        </template>
      </a-list>
      <a-empty v-else description="暂无通知" />
    </a-spin>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import api from '../api'

const notifications = ref([])
const loading = ref(false)
const filterType = ref(null)

const filteredNotifications = computed(() => {
  if (!filterType.value) return notifications.value
  return notifications.value.filter(n => n.type === filterType.value)
})

async function fetchNotifications() {
  loading.value = true
  try {
    const res = await api.get('/notifications')
    notifications.value = res.data
  } catch (e) {
    message.error('获取通知失败')
  } finally {
    loading.value = false
  }
}

async function markRead(id) {
  try {
    await api.post(`/notifications/${id}/read`)
    const idx = notifications.value.findIndex(n => n.id === id)
    if (idx >= 0) {
      notifications.value[idx].is_read = true
    }
  } catch (e) {
    message.error('操作失败')
  }
}

async function markAllRead() {
  try {
    await api.post('/notifications/read-all')
    notifications.value.forEach(n => n.is_read = true)
    message.success('已全部标记为已读')
  } catch (e) {
    message.error('操作失败')
  }
}

async function deleteNotification(id) {
  try {
    await api.delete(`/notifications/${id}`)
    notifications.value = notifications.value.filter(n => n.id !== id)
    message.success('删除成功')
  } catch (e) {
    message.error('删除失败')
  }
}

function getAvatarStyle(type) {
  const styles = {
    system: { backgroundColor: '#1890ff' },
    homework: { backgroundColor: '#52c41a' },
    exam: { backgroundColor: '#faad14' },
    attendance: { backgroundColor: '#722ed1' },
  }
  return styles[type] || styles.system
}

function getAvatarIcon(type) {
  const icons = { system: '📢', homework: '📝', exam: '📄', attendance: '✅' }
  return icons[type] || '📢'
}

function formatTime(time) {
  const date = new Date(time)
  return date.toLocaleString('zh-CN')
}

onMounted(fetchNotifications)
</script>

<style scoped>
.unread-item {
  background: #f6ffed;
}
</style>
