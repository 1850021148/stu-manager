<template>
  <div id="index">
    <!-- <el-carousel height="400px" trigger="click">
      <el-carousel-item v-for="item in banner" :key="item.id">
        <img :src="item.src" alt="" />
      </el-carousel-item>
    </el-carousel> -->
    <swiper ref="mySwiper" :options="swiperOptions">
      <swiper-slide v-for="item in banner" :key="item.id">
        <img :src="item.src" alt="" />
      </swiper-slide>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>

    <div class="content">
      欢迎来到Juln的学生管理系统
    </div>
    <footer>
      <p>该网站由Juln开发</p>
      <p>qq: 1850021148</p>
    </footer>
  </div>
</template>

<script>
// 创建时间: 2020/11/27

import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

import img1 from '@/assets/images/1.jpg'
import img2 from '@/assets/images/2.jpg'
import img3 from '@/assets/images/3.jpg'

export default {
  name: "Index",
    
  data () {
    return {
      swiperOptions: {
        loop: true,
        autoplay: true,
        effect:'cube',
        cubeEffect: {
          slideShadows: true,
          shadow: true,
          shadowOffset: 100,
          shadowScale: 0.6
        },
        // effect : 'fade',
        // fadeEffect: {
        //   crossFade: true,
        // },
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
      },
      banner: [
        {id: 0, src: img1},
        {id: 1, src: img2},
        {id: 2, src: img3},
      ]
    }
  },
    
  methods: {
      
  },

  mounted() {
    
  },

  computed: {
    swiper() {
      return this.$refs.mySwiper.$swiper
    }
  },
  
  components: {
    Swiper,
    SwiperSlide
  },
}
</script>

<style scoped lang="less">
[v-cloak] {
  display: none;
}
#index{
  padding-top: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  .el-carousel{
    width: 750px;
    height: 400px;
    border: 1px solid white;
    border-radius: 5px;
    /deep/ .el-carousel__arrow{
      background-color: gray;
      opacity: .5;
      &:hover{
        opacity: 1;
      }
    }
    img{
      width: 750px;
      height: 400px;
    }
  }
  .swiper-container{
    width: 750px;
    height: 400px;
    img{
      width: 750px;
      height: 400px;
    }
  }
  .content{
    margin: 100px 0 60px 0;
  }
  footer{
    padding: 20px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    border-top: 1px solid gray;
    background: rgb(36,35,40);
    p{
      color: gray;
    }
  }
}

</style>