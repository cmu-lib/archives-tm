import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Document from '../views/Document.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: Home
  },
  {
    path: '/documents/:id',
    name: 'DocumentDetailView',
    component: Document,
    props: (route) => ({ document_id: route.params.id })
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
