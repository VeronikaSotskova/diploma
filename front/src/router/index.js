import { createRouter, createWebHistory } from 'vue-router'
import CirclePacking from "../views/CirclePacking";
import SearchPage from "../views/SearchPage";
import ModelPage from "../views/ModelPage";

const routes = [
  {
    path: '/',
    name: 'Main',
    component: CirclePacking
  },
  {
    path: '/search',
    name: 'SearchPage',
    component: SearchPage
  },
  {
    path: '/model',
    name: 'ModelPage',
    component: ModelPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
