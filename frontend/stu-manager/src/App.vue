<template>
  <div id="app" :style="{'background-image': 'url('+bgImg+')'}">
    <el-row id="top-tools-bar">
      <el-col :span="6" :offset="1">
        <h1>Juln-学生管理系统</h1>
      </el-col>
      <el-col :span="10" :offset="5">
        <el-menu id="top-nav"
          :default-active="activeIndex" mode="horizontal" router
          background-color="rgb(36,35,40)"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item index="1" :route="{name:'Index'}">首页</el-menu-item>
          <el-menu-item index="2" :route="{name:'Core'}">学生管理</el-menu-item>
          <el-menu-item index="3" :route="{name:'About'}">关于我们</el-menu-item>
          <el-menu-item
            index="4" :route="{name:'User'}"
            v-if="!isLogin"
          >登录/注册</el-menu-item>
          <el-menu-item index="" v-else>用户: {{$store.state.name}}</el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
    <el-scrollbar style="height:100%">
      <transition name="index-nav" mode="out-in">
        <keep-alive>
          <router-view />
        </keep-alive>
      </transition>
    </el-scrollbar>
  </div>
</template>

<script>
// 创建时间: 2020/11/27
import bgImg from '@/assets/bg.jpg'

export default {
    name: "App",
    
    data () {
      return {
          activeIndex: '1',
          bgImg,
          // isLogin: true,
      }
    },

    created() {
      window.vue = this
    },

    computed: {
      isLogin() {
        return this.$store.state.isLogin || false
      },
      routeName() {
        return this.$route.name
      }
    },

    watch: {
      routeName(newRouteName,oldRouteName) {
        if(newRouteName === oldRouteName) return
        if(newRouteName === 'Index')
          this.activeIndex = "1"
        else if(newRouteName === 'About')
          this.activeIndex = "3"
        else if(newRouteName === 'Login' || routeName === 'Register')
          this.activeIndex = "4"

      }
    },
    
    methods: {
        
    },
    
    components: {
        
    },
}
</script>

<style lang="less">
[v-cloak] {
  display: none;
}
*{
  margin: 0;
  padding: 0;
  color: white;
  user-select: none;
}
a{
  text-decoration: none;
}
li{
  list-style-type: none;
}

.index-nav-enter{
  opacity: 0;
}
.index-nav-leave-to{
  opacity: 0;
}
.index-nav-enter-active,.index-nav-leave-active{
  transition: .5s ease-in-out;
}

#app{
  padding-top: 60px;
  min-width: 870px;
  height: calc(100vh - 60px);
  background-size: cover;
  #top-tools-bar{
    position: fixed;
    z-index: 1000;
    top: 0;
    width: 100%;
    display: flex;
    align-items: center;
    background: rgb(36,35,40);
    box-sizing: border-box;
    box-shadow: 1px 1px 10px black;
    h1{
      font-size: 20px;
    }
    #top-nav.el-menu{
      border: none;
      .el-menu-item{
        &:hover{
          background: none !important;
          opacity: .8 !important;
        }
      }
    }
  }
  .el-scrollbar{
    .el-scrollbar__wrap{
      overflow-x: hidden !important;
      overflow-y: scroll !important;
    }
  }
}

.el-message-box{
  width: 300px !important;
  background-color: rgba(0,0,0,.5) !important;
  .new-table{
    tbody{
      height: 220px;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      span{
        display: inline-block;
        font-size: 16px;
        text-align: center;
        width: 60px;
      }
      input[type=text]{
        padding: 0 5px;
        height: 25px;
        font-size: 16px;
        outline: none;
        border-radius: 2px;
        background-color: rgba(0,0,0,.5) !important;
        user-select: text;
      }
    }
  }
  .el-button{
    background-color: rgba(0,0,0,.5) !important;
  }
}

.el-select-dropdown{
  margin-top: 10px !important;
  margin-left: 10px !important;
  min-width: 80px !important;
  background-color: rgba(0,0,0,.7) !important;
  .el-select-dropdown__item{
    color: white !important;
    height: 25px;
    line-height: 25px;
    background-color: rgba(255,255,255,.1) !important;
  }
}
</style>
