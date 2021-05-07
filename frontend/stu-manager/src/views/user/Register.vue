<template>
  <div id="login-box">
    <el-form 
      :model="form"
      :rules="rules"
      label-position="right" 
      label-width="90px"
      label-suffix=":"
    >
      <el-form-item label="用户名" prop="name">
        <el-input v-model="form.name" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="form.password" placeholder="请输入密码" show-password></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="rePassword">
        <el-input v-model="form.rePassword" placeholder="请再次输入密码" show-password></el-input>
      </el-form-item>
      <el-button @click="onsubmit">注册</el-button>
    </el-form>
  </div>
</template>

<script>
// 创建时间: 2020/11/27

export default {
  name: "Login",
  
  data () {
    let validateRePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.form.password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    }
    return {
      form: {
        name: '',
        password: '',
        rePassword: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 10, max: 10, message: '用户名即学号,为10位的数字', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 3, message: '密码长度不低于3个字符', trigger: 'blur' }
        ],
        rePassword: [
          { required: true, validator: validateRePassword, trigger: 'blur' }
        ],
      }
    }
  },
  
  methods: {
    onsubmit() {
      this.$http.post('/register',this.form)
      .then(result => {
        console.log(result)
        if(result.data.data.msg === 'success') {
          this.$store.commit('login',this.form.name)
          this.$router.push({name: 'Core'})
          this.$message({
            type: 'success',
            showClose: true,
            message: '注册成功'
          })
        }
        else{
          this.$message({
            type: 'error',
            showClose: true,
            message: '该账号已存在, 请直接登录'
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
  padding: @padding;
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