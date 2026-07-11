import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/api'

export const useUserStore = defineStore('user', () => {
  const token = ref(localStorage.getItem('token') || '')
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))

  const isLoggedIn = computed(() => !!token.value)
  const role = computed(() => user.value?.role || 'teacher')
  const username = computed(() => user.value?.username || '')
  const displayName = computed(() => user.value?.name || '')

  async function login(loginUsername, password) {
    const res = await api.post('/auth/login', { username: loginUsername, password })
    token.value = res.data.access_token
    user.value = res.data.user
    localStorage.setItem('token', token.value)
    localStorage.setItem('user', JSON.stringify(user.value))
    return res.data
  }

  function logout() {
    token.value = ''
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }

  async function fetchMe() {
    if (!token.value) return null
    try {
      const res = await api.get('/auth/me')
      user.value = res.data
      localStorage.setItem('user', JSON.stringify(user.value))
      return res.data
    } catch {
      logout()
      return null
    }
  }

  return { token, user, isLoggedIn, role, username, displayName, login, logout, fetchMe }
})
