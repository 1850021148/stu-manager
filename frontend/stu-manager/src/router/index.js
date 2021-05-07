import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/', redirect: '/index',
  },
  {
    path: '/index', name: 'Index',
    component: () => import('@/views/Index.vue')
  },
  {
    path: '/user', name: 'User', redirect: {name: 'Login'},
    component: () => import('@/views/User.vue'),
    children: [
      {
        path: 'login', name: 'Login',
        components: {
          default: () => import('@/views/User.vue'),
          user: () => import('@/views/user/Login.vue')
        }
      },
      {
        path: 'register', name: 'Register',
        components: {
          default: () => import('@/views/User.vue'),
          user: () => import('@/views/user/Register.vue')
        }
      },
    ]
  },
  {
    path: '/core', name: 'Core',
    component: () => import('@/views/Core.vue'),
    meta: {
      requireLogin: true,
    }
  },
  {
    path: '/about', name: 'About',
    component: () => import('@/views/About.vue')
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  // 登录检验
  if(to.meta.requireLogin) {
    if(store.state.isLogin) {
      next()
      window.vue.activeIndex = "2"
      return
    }
    window.vue.$message({
      type: 'warning',
      showClose: true,
      message: '请先登录'
    })
    window.vue.activeIndex = '4' // 解决index-nav的样式问题
    next("/user")
    return
  }
  next()
})

export default router
