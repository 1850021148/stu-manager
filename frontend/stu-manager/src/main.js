import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(VueAxios,axios)

axios.defaults.baseURL = 'http://127.0.0.1:8080'
// 'http://mengxuegu.com:7300/mock/5fc12195a528522f7959e270/stuManager'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
