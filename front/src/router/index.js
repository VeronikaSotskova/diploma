import { createRouter, createWebHistory } from 'vue-router'
import CirclePacking from "../views/CirclePacking";
import TableTreeSearch from "../views/TableTreeSearch";

const routes = [
  {
    path: '/',
    name: 'Main',
    component: CirclePacking
  },
  {
    path: '/search/:searchText',
    name: 'Search',
    component: TableTreeSearch
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
