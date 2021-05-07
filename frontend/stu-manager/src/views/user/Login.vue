<template>
  <div id="login-box">
    <el-form 
      :model="form"
      :rules="rules"
      label-position="right" 
      label-width="80px"
      label-suffix=":"
    >
      <el-form-item label="用户名" prop="name">
        <el-input v-model="form.name" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="form.password" placeholder="请输入密码" show-password></el-input>
      </el-form-item>
      <el-button @click="onsubmit">登录</el-button>
    </el-form>
  </div>
</template>

<script>
// 创建时间: 2020/11/27

export default {
  name: "Login",
  
  data () {
    return {
      form: {
        name: '',
        password: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 10, max: 10, message: '用户名即学号,为10位的数字', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 3, message: '密码长度不低于3个字符', trigger: 'blur' }
        ]
      }
    }
  },
  
  methods: {
    onsubmit() {
      console.log(this.form)
      this.$http.post('/login',this.form)
      .then(result => {
        console.log(result)
        if(result.data.data.msg === 'success') {
          this.$store.commit('login',this.form.name)
          this.$router.push({name: 'Core'})
          this.$message({
            type: 'success',
            showClose: true,
            message: '登录成功'
          })
        }
        else{
          this.$message({
            type: 'error',
            showClose: true,
            message: '用户名或密码错误'
          })
        }
      })
    }
  },
  
  components: {
      
  },
}
</script>

<style scoped lang="less">
[v-cloak] {
  display: none;
}
#login-box{
  @padding: 30px;
  padding: 60px @padding;
  width: 100%;
  height: 300px;
  .el-form{
    width: calc(100% - 2 * @padding);
    /deep/ .el-form-item__label{
      color: white !important;
    }
    .el-input{
      /deep/ .el-input__inner{
        background: rgb(40,40,41) !important;
        color: gray;
      }
    }
    .el-button{
      margin-left: 50%;
      transform: translateX(-50%);
      background: rgb(40,40,41);
      /deep/ span{
        color: white !important;
      }
    }
  }
}
</style>