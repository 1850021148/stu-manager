import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    name: null,
  },
  mutations: {
    login(state,name) {
      state.isLogin = true
      state.name = name
    }
  },
  actions: {
  },
  modules: {
  }
})
