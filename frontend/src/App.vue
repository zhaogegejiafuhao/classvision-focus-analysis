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
    Layout: {
      headerBg: '#fff',
      headerHeight: 56,
      siderBg: '#fff',
      bodyBg: '#f5f6fa',
    },
    Menu: {
      itemSelectedBg: 'rgba(55, 81, 254, 0.08)',
      itemSelectedColor: '#3751FE',
    },
  },
}
</script>

<style>
.page-fade-enter-active,
.page-fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.page-fade-enter-from {
  opacity: 0;
  transform: translateY(8px);
}
.page-fade-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
