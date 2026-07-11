
import { createRouter, createWebHistory , type RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [{path: "/Frame57864", name: "Frame57864", component: () => import("@/views/Frame57864.vue"), meta: { guid: "57:864" }},{path: "/", name: "Frame334", component: () => import("@/views/Frame334.vue"), meta: { guid: "3:34" }},];

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
