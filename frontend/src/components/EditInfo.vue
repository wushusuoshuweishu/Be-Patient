<template>
  <div>
    <el-container class="aside">
      <el-aside id="person_card">
        <el-card class="person_info" id="person_info">
          <h2>个人信息</h2>
          <el-divider></el-divider>
          <el-avatar class="person_avatar" :size="100" :src="photo"></el-avatar>
          <el-divider></el-divider>
          <h2>{{username}}</h2>
          <div class="detailed_info">
            <div><i class="el-icon-phone"></i>&nbsp手机号 
              <br>{{mobile}}
            </div>
            <div><i class="el-icon-message"></i>&nbsp邮箱
              <br>{{email}}
            </div>
            <div><i class="el-icon-user-solid"></i>&nbsp职业
              <br>{{job}}
            </div>
            <div><i class="el-icon-s-home"></i>&nbsp家庭住址
              <br>{{home}}
            </div>
            <div><i class="el-icon-edit"></i>&nbsp个性签名
              <br>{{edit}}
            </div>
          </div>
        </el-card>
      </el-aside>
      <el-main class="me-articles">
        <el-form ref="form" :model="form" label-width="10vw" label-position="right">
        <el-form-item>
          <h2>修改信息</h2>
        </el-form-item>
        <el-form-item label="电话">
          <el-input v-model="form.mobile"></el-input>
        </el-form-item>
        <el-form-item label="职业">
          <el-input v-model="form.job"></el-input>
        </el-form-item>
          <el-form-item label="所在地">
          <el-input v-model="form.home"></el-input>
        </el-form-item>
          <el-form-item label="个性签名">
          <el-input v-model="form.edit"></el-input>
        </el-form-item>
          <el-form-item>
          <el-upload
            class="upload-demo"
            drag
            multiple
            action="#"
            :on-change="onChange"
            :auto-upload="false"
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text"><em>上传头像</em></div>
          </el-upload>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit" id="commit_bt">提交</el-button>
        </el-form-item>
      </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import ArticleItem from "@/components/ArticleItem.vue"
  import axios from "axios";
  export default{
    components:{
      ArticleItem
  },
  created() {
    var jwt = sessionStorage.getItem("accessToken")
    axios.get('/api/account/getAccountInfo/', {
      headers: { 'Authorization': jwt }
    }
    ).then((res) => {//接口
      if(res.status === 401){
          this.$router.push(
              {
                path: '/NoLogIn',
                query: {
                }
              }
          );
          return;
        }
      this.username = res.data['username']
      this.email = res.data['email']
      this.mobile = res.data['mobile']
      this.job = res.data['job']
      this.home = res.data['home']
      this.edit = res.data['edit']
      this.photo = res.data['photo']
      console.log(res.data['email'])
      console.log('----------show-photo------------')
      console.log(this.photo)
    })
    .catch((err) => {
      console.error(err);
    });
  },
  data(){
    return {
      username: '',
      email: '',
      mobile: '',
      job: '',
      home: '',
      edit: '',
      photo: '',
      form:{
        mobile:'',
        job:'',
        home:'',
        edit:'',
        photo:''
        }
      }
  },
  methods:{
    Gowriter(){
      this.$router.push('/Writer')
    },
    onChange(file, fileList){
      var This = this;
      //this.imageUrl = URL.createObjectURL(file.raw);
      var reader = new FileReader();
      reader.readAsDataURL(file.raw);
      reader.onload = function(e){
          This.photo = this.result;
          console.log('----------upload-photo------------');
          console.log(This.photo);
      }
    },
    onSubmit(){
      var jwt = sessionStorage.getItem("accessToken")
      axios.post('/api/account/changeAccountInfo/',{
        mobile:this.form['mobile'],
        job:this.form['job'],
        home:this.form['home'],
        edit:this.form['edit'],
        photo:this.photo
      },
          {
        headers:{'Authorization': jwt},
      }
    )
    .then((res)=>{//接口
      if(res.status === 401){
          this.$router.push(
              {
                path: '/NoLogIn',
                query: {
                }
              }
          );
          return;
        }
        if(res.status === 200){
          this.$router.push(
              {
                path: '/Forum',
                query: {
                }
              }
          );
        }
    })
    .catch((err)=>{
      console.error(err);
      this.showReminder = true;
    });

    this.$router.push({
          path: '/PersonalHomePage',
          query: {
          }
        });
      }
    }
  }
</script>

<style scoped>
  ::-webkit-scrollbar {
    width: 0 !important;
    height: 0 !important;
  }

  .person_info{
    height: max-content;
  }

  .el-card:not(.person_info) {
    width: 60vw;
    margin: auto;
  }

  .el-tabs
  {
    text-align: left;
    background-color: white;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 1vw;
    opacity: 0.75;
    line-height: 10vh;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }

  .el-aside {
    margin-left: 3vw;
    margin-top: 3vw;
    height: 75vh;
    width: 30vmin;
  }

  .ads {
    height: max-content;
  }

  .detailed_info{
    text-align: left;
    line-height: 3.5vh;
    word-break: break-all;
    word-wrap: break-word
  }

  .open_health_aid{
    text-align: center;
    margin-top: 2vh;
  }

  .el-main {
    margin-top: 2vw;
    height: 100%;
    width: 40vw;
  }

  #items {
    width: 40vw;
  }

  #person_info {
    width: 28vmin;
  }

  #person_card {
    width: 30vmin !important;
    height: 100% !important;
  }
  
  .el-main {
    width: 60vw;
    height: 100%;
    margin: auto;
    margin-top: 5vh;
  }

  .el-form-item {
    width: 100%;
    text-align: left;
  }

  .el-input {
    width: 30vw;
  }
</style>