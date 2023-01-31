<template>
  <el-container>
    <el-header class="title">协心力 慢性病患者社交平台</el-header>
    <el-form ref="form" :model="form" class="login-wrapper">
      <div class='login-title'>用户登录</div>
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
      <div class="reminder" v-show="showReminder">您输入的密码错误,请重新输入</div>
      <div class="reminder" v-show="showUser">用户名不能为空</div>
      <div class="reminder" v-show="showPass">密码不能为空</div>
      <div class="login-btn">
        <el-button type="primary" @click="login">登录</el-button>
      </div>
      <div class="register-link">
        <a href="/register">没有账号？点我注册！</a>
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
.user-name {
  padding-top: 1vh;
  margin-bottom: 3vh;
}
.login-btn {
  padding: 1vh;
}
::v-deep .el-form-item__label {
  width: 8vmin;
  font-size: 1.5vmin;
}
::v-deep .el-button {
  font-size:1.5vmin;
}
.login-wrapper {
  background-color: #fff;
  width: 30vmin;
  height: 50vmin;
  border-radius: 2vw;
  padding: 0 4vw;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -80%);
}
.login-title {
  margin-top:4vh;
  margin-bottom:4vh;
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
import { SM2, SM4 } from 'gm-crypto'
export default {
  name: "HomePage",
  data() {
    return {
        showReminder:false,
        showUser:false,
        showPass:false,
        form: {
          username:'',//用户名
          password:'',//用户密码
        }
    };
  },
  methods:{
    login(){
      this.showReminder = false;
      this.showUser = false;
      this.showPass = false;
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
      const key = "0123456789abcdeffedcba9876543210"
      axios.post('/api/account/login/',{
          username: this.form['username'],//用户名
          password: SM4.encrypt(this.form['password'], key, {
         key,
         mode: SM2.constants.CBC,
         inputEncoding: 'utf8',
         outputEncoding: 'hex'
        }),//密码
        }
      )
      .then((res)=>{//接口
          if(res.status === 200){//登陆成功则跳转
            sessionStorage.setItem('accessToken', res.data['jwt'])
            this.$router.push(
                {
                    path: '/Forum',
                    query: {
                        username: this.form.username
                    }
                }
            );
          }
      })
      .catch((err)=>{
          console.error(err);
          this.showReminder = true;
      });
    },
  },
};
</script>