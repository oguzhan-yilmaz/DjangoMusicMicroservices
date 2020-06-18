import Vue from "vue";
import App from "./App.vue";
import Vuex from "vuex";
import VueRouter from "vue-router";
import { store } from "./store/store.js";
import HomePageComponent from './components/HomePageComponent'
import LoginComponent from './components/LoginComponent'



Vue.use(Vuex);
Vue.use(VueRouter);
Vue.config.productionTip = false;

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomePageComponent
  },
  {
    path: '/',
    name: 'signin',
    component: LoginComponent
  },
]

const router = new VueRouter({
  mode:'history',
  base: process.env.BASE_URL,
  routes
})

export default router

new Vue({
  render: (h) => h(App),
  store,
  router
}).$mount("#app");
