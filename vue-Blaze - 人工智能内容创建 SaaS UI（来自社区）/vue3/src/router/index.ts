
import { createRouter, createWebHistory , type RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [{path: "/Frame17448", name: "Frame17448", component: () => import("@/views/Frame17448.vue"), meta: { guid: "17:448" }},{path: "/Frame293744", name: "Frame293744", component: () => import("@/views/Frame293744.vue"), meta: { guid: "29:3744" }},{path: "/Frame293293", name: "Frame293293", component: () => import("@/views/Frame293293.vue"), meta: { guid: "29:3293" }},{path: "/Frame282357", name: "Frame282357", component: () => import("@/views/Frame282357.vue"), meta: { guid: "28:2357" }},{path: "/Frame281780", name: "Frame281780", component: () => import("@/views/Frame281780.vue"), meta: { guid: "28:1780" }},{path: "/Frame281518", name: "Frame281518", component: () => import("@/views/Frame281518.vue"), meta: { guid: "28:1518" }},{path: "/Frame28841", name: "Frame28841", component: () => import("@/views/Frame28841.vue"), meta: { guid: "28:841" }},{path: "/Frame27219", name: "Frame27219", component: () => import("@/views/Frame27219.vue"), meta: { guid: "27:219" }},{path: "/", name: "Frame04", component: () => import("@/views/Frame04.vue"), meta: { guid: "0:4" }},];

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
