<template>
  <div>
    <el-container class="article-area">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="标题">
          <el-input v-model="form.blog_title"></el-input>
        </el-form-item>
        <el-form-item label="概要">
          <el-input v-model="form.summary"></el-input>
        </el-form-item>
        <el-form-item label="标签">
          <el-input v-model="form.labels" class="tags_input" placeholder="可以输入多个标签，用空格隔开"></el-input>
        </el-form-item>
        <el-form-item label="正文">
          <el-input type="textarea" v-model="form.blog_content" id="cert"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">提交</el-button>
          <el-button type="primary" @click="goBack">返回</el-button>
        </el-form-item>
      </el-form>
      <el-aside>
        <el-carousel class="ads">
            <el-carousel-item v-for="item in 3" :key="item">
              <h3><br/>{{ item }}</h3>
            </el-carousel-item>
        </el-carousel>
        <el-container id="tool_bar">
          <el-upload
            class="upload-demo"
            drag
            action="https://jsonplaceholder.typicode.com/posts/"
            multiple
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          </el-upload>
        </el-container>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
  import axios from 'axios';
  export default{
    methods:{
      goBack() {
        this.$router.push({path: `/PersonalHomePage`,
                    query: {
                    }});
      },
      onSubmit() { //提交文章
        var jwt = sessionStorage.getItem("accessToken")
        axios.post('/api/blog/publishBlog/',{
          blog_title:this.form['blog_title'],
          blog_content:this.form['blog_content'].replace(/\n|\r\n/g,"<br>"),
          summary:this.form['summary'],
          labels:this.form['labels'],
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
                    path: '/Forum',
                    query: {
                    }
                });
      }
    },
    data(){
      return {
        form: {
          title:'',
          summary:'',
          labels:'',
          content:''
        }
      }
    }
  }
</script>

<style scoped>
  .el-container {
    height: 100%;
  }

  .el-tabs
  {
    text-align: left;
    background-color: white;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 2vw;
    opacity: 0.75;
    line-height: 10vw;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }

  .el-aside {
    margin-left: 5vw;
    margin-top: 5vh;
    height: 80vh;
    width: 30vw !important;
    overflow-y: hidden;
  }

  .article-area{
    margin-left: 2vw;
    margin-right: 2vw;
    margin-top: 5vh;
    width: 100%;
  }

  .el-input{
    width: 30vw;
  }

  .submit_button {
    text-align: right;
  }

  /deep/ textarea{
    width: 60vw;
    height: 60vh;
    resize: none;
  }

  .article-area{
    text-align: left;
  }

  .el-aside{
    text-align: center !important;
  }

  /deep/ .el-carousel {
    width: 20vw;
    height: 40vh;
  }
  /deep/ .el-carousel__container {
    height: 100% !important;
  }

  /deep/ .el-upload{
    width: 20vw;
    height: 30vh;
  }
  /deep/ .el-upload .el-upload-dragger{
    width: 20vw;
    height: 20vh;
  }

</style>
