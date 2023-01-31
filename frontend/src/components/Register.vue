<template>
  <el-container>
    <el-header class="title">协心力 慢性病患者社交平台</el-header>
    <el-form ref="form" :model="form"  class="login-wrapper">
      <div class='login-title'>用户注册</div>
      <el-form-item label="邮箱" required  class="user-name">
        <el-col :md="{span:10, offset:0}" :sm="12">
          <el-form-item label-width="0px">
            <el-input v-model="form.email" class="user-input"></el-input>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="用户名" required  class="user-name">
        <el-col :md="{span:10, offset:0}" :sm="12">
          <el-form-item label-width="0px">
            <el-input v-model="form.username" class="user-input"></el-input>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="密码" required  class="pass-word">
        <el-col :md="{span:10, offset:0}" :sm="12">
          <el-form-item label-width="0px">
            <el-input v-model="form.password" class="user-input" show-password></el-input>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item label="验证码" required  class="user-name">
        <el-col :md="{span:10, offset:0}" :sm="12">
          <el-form-item label-width="0px">
            <el-input v-model="form.identity" class="user-input"></el-input>
          </el-form-item>
        </el-col>
      </el-form-item>
      <div class="reminder" v-show="showReminder">注册失败！请检查你的信息是否正确填写！</div>
      <div class="reminder" v-show="showEmail">邮箱不能为空</div>
      <div class="reminder" v-show="showUser">用户名不能为空</div>
      <div class="reminder" v-show="showPass">密码不能为空</div>
      <div class="reminder" v-show="showIden">验证码不能为空</div>
      <div class="login-btn">
        <el-button type="primary" @click="send_identity" id="send_button">发送验证码</el-button>
        <el-button type="primary" @click="register">注册</el-button>
      </div>
    </el-form>
  </el-container>
</template>

<style scoped>
.el-container {
  height:100vh;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
.reminder {
  color: red;
}
.title {
  color:#096391;
  padding-top: 10vw;
  padding-bottom: 10vh;
  font-size: 3vmin;
}
.el-form-item {
  padding-top: 1vh;
  margin-bottom: 1vh;
}
.login-btn {
  padding: 1vh;
}
::v-deep .el-form-item__label {
  font-size: 1.5vmin;
  width: 8vmin;
}
::v-deep .el-button {
  font-size:1.5vmin;
}
.login-wrapper {
  background-color: #fff;
  width: 30vmin;
  height: 55vmax;
  border-radius: 2vw;
  padding: 0 4vw;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -80%);
}
.login-title {
  margin-top: 4vh;
  margin-bottom: 4vh;
  font-size: 2.5vmin;
  color:#333399;
}
.user-input {
  width: 20vmin;
  font-size: 1.5vmin;
}
</style>

<script>
import axios from 'axios';
import {SM2, SM4} from "gm-crypto";
let button_text = "发送验证码";
export default {
  name: "Register",
  data() {
    return {
        showReminder:false,
        showUser:false,
        showPass:false,
        showIden:false,
        showEmail:false,
        form: {
          email:'',//邮箱
          username:'',//用户名
          password:'',//用户密码
          identity:'',//验证码
        }
    };
  },
  methods:{
    send_identity(){
      this.showReminder = false;
      this.showUser = false;
      this.showPass = false;
      this.showEmail = false;
      this.showIden = false;
      if(this.form.email == "")
      {
        this.showEmail = true;
        return;
      }
      axios.post('/api/email/sendVerifyEmail/',{
          email:this.form['email']//邮箱
        }
      )
      .then((res)=>{
          if(res.status === 200){//注册成功则跳转到登陆页面
            var p = document.getElementById("send_button");
            p.innerText = "验证码已发送";
            console.log("identity sent");
          }
      })
      .catch((err)=>{
          console.error(err);
      });
    },
    register(){
      this.showReminder = false;
      this.showUser = false;
      this.showPass = false;
      this.showEmail = false;
      this.showIden = false;
      if(this.form.username == "")
      {
        this.showUser = true;
        return;
      }
      else if(this.form.password == "")
      {
        this.showPass = true;
        return;
      }
      else if(this.form.identity == "")
      {
        this.showIden = true;
        return;
      }
      else if(this.form.email == "")
      {
        this.showEmail = true;
        return;
      }
      const key = "0123456789abcdeffedcba9876543210"
      axios.post('/api/account/register/',{
          username:this.form['username'],//用户名
          password:SM4.encrypt(this.form['password'], key, {
         key,
         mode: SM2.constants.CBC,
         inputEncoding: 'utf8',
         outputEncoding: 'hex'
        }),//密码
          email:this.form['email'],//邮箱
          verify_code:this.form['identity'],//验证码
        }
      )
      .then((res)=>{
          if(res.status === 201){//注册成功则跳转到登陆页面
            this.$router.push(
                {
                    path: '/',
                    query: {
                        username: this.form.username
                    }
                }
            );
          }
      })
      .catch((err)=>{
          this.showReminder=true;
          console.error(err);
      });
    },
  },
};
</script>