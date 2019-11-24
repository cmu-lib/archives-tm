import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Box from '../views/Box.vue'
import Document from '../views/Document.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: Home
  },
  {
    path: '/boxes/:box_id',
    name: 'BoxView',
    component: Box,
    props: (route) => ({ box_id: route.params.box_id }),
    children: [
      {
        path: 'documents/:document_id',
        name: 'DocumentDetailView',
        component: Document,
        props: (route) => ({ document_id: route.params.document_id })
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
