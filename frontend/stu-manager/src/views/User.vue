<template>
    <div id="user-box">
        <div class="inner-user-box">
            <el-menu
                :default-active="activeIndex" mode="horizontal" router
                background-color="rgb(36,35,40)"
                text-color="#fff" active-text-color="#ffd04b"
            >
                <el-menu-item index="1" :route="{name: 'Login'}">登录</el-menu-item>
                <el-menu-item index="2" :route="{name: 'Register'}">注册</el-menu-item>
            </el-menu>
            <transition name="user-nav" mode="out-in">
                <keep-alive>
                    <router-view name="user"></router-view>
                </keep-alive>
            </transition>
        </div>
    </div>
</template>

<script>
// 创建时间: 2020/11/27

export default {
    name: "User",
    
    data () {
      return {
          activeIndex: '1',
      }
    },
    
    methods: {
        
    },
    
    components: {
        
    },
}
</script>

<style scoped lang="less">
[v-cloak] {
    display: none;
}

.user-nav-enter, .user-nav-leave-to{
    opacity: 0;
}
.user-nav-enter-active, .user-nav-leave-active{
    transition: .3s;
}

#user-box{
    width: 100vw;
    height: calc(100vh - 60px);
    display: flex;
    justify-content: center;
    align-items: center;
    .inner-user-box{
        width: 400px;
        height: 360px;
        border-radius: 5px;
        overflow: hidden;
        box-shadow: 1px 1px 10px black;
        .el-menu{
            border: none;
            .el-menu-item{
                width: 50%;
                text-align: center;
                &:hover{
                    background: none !important;
                    opacity: .8;
                }
            }
        }
    }
}
</style>