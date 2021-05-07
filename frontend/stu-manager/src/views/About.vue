<template>
    <div id="about">
        <div class="inner-about">
            <p>Juln</p>
            <p>庄哥出品</p>
            <p>qq: 1850021148</p>
        </div>
    </div>
</template>

<script>
// 创建时间: 2020/11/27

export default {
    name: "About",
    
    data () {
      return {
          
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
#about{
    height: calc(100vh - 60px);
    display: flex;
    justify-content: space-around;
    align-items: center;
    div.inner-about{
        width: 100%;
        height: 100px;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }
}
</style>