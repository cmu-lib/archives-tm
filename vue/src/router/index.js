import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Box from '../views/Box.vue'
import Document from '../views/Document.vue'
import TopicModelList from "../views/TopicModelList.vue"
import TopicModel from "../views/TopicModel.vue"

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
  {
    path: '/topic_models',
    name: 'TopicModelList',
    component: TopicModelList,
  },
  {
    path: '/topic/models/:topic_model_id',
    name: 'TopicModel',
    component: TopicModel,
    props: (route) => ({ topic_model_id: route.params.topic_model_id })
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
