
import { createRouter, createWebHistory , type RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [{path: "/Frame6570126202", name: "Frame6570126202", component: () => import("@/views/Frame6570126202.vue"), meta: { guid: "6570:126202" }},{path: "/Frame6570126203", name: "Frame6570126203", component: () => import("@/views/Frame6570126203.vue"), meta: { guid: "6570:126203" }},{path: "/Frame6573126863", name: "Frame6573126863", component: () => import("@/views/Frame6573126863.vue"), meta: { guid: "6573:126863" }},{path: "/Frame6577129204", name: "Frame6577129204", component: () => import("@/views/Frame6577129204.vue"), meta: { guid: "6577:129204" }},{path: "/", name: "Frame6565125001", component: () => import("@/views/Frame6565125001.vue"), meta: { guid: "6565:125001" }},];

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
