(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-55ed4f04"],{"0806":function(e,r,s){},1348:function(e,r,s){"use strict";s.r(r);var o=function(){var e=this,r=e.$createElement,s=e._self._c||r;return s("div",{attrs:{id:"login-box"}},[s("el-form",{attrs:{model:e.form,rules:e.rules,"label-position":"right","label-width":"90px","label-suffix":":"}},[s("el-form-item",{attrs:{label:"用户名",prop:"name"}},[s("el-input",{attrs:{placeholder:"请输入用户名"},model:{value:e.form.name,callback:function(r){e.$set(e.form,"name",r)},expression:"form.name"}})],1),s("el-form-item",{attrs:{label:"密码",prop:"password"}},[s("el-input",{attrs:{placeholder:"请输入密码","show-password":""},model:{value:e.form.password,callback:function(r){e.$set(e.form,"password",r)},expression:"form.password"}})],1),s("el-form-item",{attrs:{label:"确认密码",prop:"rePassword"}},[s("el-input",{attrs:{placeholder:"请再次输入密码","show-password":""},model:{value:e.form.rePassword,callback:function(r){e.$set(e.form,"rePassword",r)},expression:"form.rePassword"}})],1),s("el-button",{on:{click:e.onsubmit}},[e._v("注册")])],1)],1)},t=[],a=(s("b0c0"),{name:"Login",data:function(){var e=this,r=function(r,s,o){""===s?o(new Error("请再次输入密码")):s!==e.form.password?o(new Error("两次输入密码不一致!")):o()};return{form:{name:"",password:"",rePassword:""},rules:{name:[{required:!0,message:"请输入用户名",trigger:"blur"},{min:10,max:10,message:"用户名即学号,为10位的数字",trigger:"blur"}],password:[{required:!0,message:"请输入密码",trigger:"blur"},{min:3,message:"密码长度不低于3个字符",trigger:"blur"}],rePassword:[{required:!0,validator:r,trigger:"blur"}]}}},methods:{onsubmit:function(){var e=this;this.$http.post("/register",this.form).then((function(r){console.log(r),"success"===r.data.data.msg?(e.$store.commit("login",e.form.name),e.$router.push({name:"Core"}),e.$message({type:"success",showClose:!0,message:"注册成功"})):e.$message({type:"error",showClose:!0,message:"该账号已存在, 请直接登录"})}))}},components:{}}),n=a,l=(s("cfc3"),s("2877")),i=Object(l["a"])(n,o,t,!1,null,"0bb15b8f",null);r["default"]=i.exports},cfc3:function(e,r,s){"use strict";s("0806")}}]);
//# sourceMappingURL=chunk-55ed4f04.e6e1e42e.js.map