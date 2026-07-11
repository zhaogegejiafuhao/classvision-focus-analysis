
import { createRouter, createWebHistory , type RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [{path: "/Frame30248", name: "Frame30248", component: () => import("@/views/Frame30248.vue"), meta: { guid: "30:248" }},{path: "/Frame30612", name: "Frame30612", component: () => import("@/views/Frame30612.vue"), meta: { guid: "30:612" }},{path: "/Frame43", name: "Frame43", component: () => import("@/views/Frame43.vue"), meta: { guid: "4:3" }},{path: "/", name: "Frame42", component: () => import("@/views/Frame42.vue"), meta: { guid: "4:2" }},];

const routePathMap = new Map<string, string>();

export const getRoutePathByGuid = (guid: string) => {
  if (!guid) return;
  if (routePathMap.has(guid)) return routePathMap.get(guid);

  const route = routes.find((item) => item.meta?.guid === guid);
  if (!route) return;
  routePathMap.set(guid, route.path);

  return route.path;
}

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
