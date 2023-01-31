<template>
  <div>
    <el-container class="aside" >
      <el-aside id="person_card">
        <el-card class="person_info" id="person_info" v-loading="loading">
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
            <div class="open_health_aid">
              <el-button @click="Gowriter">去发帖</el-button>
              <br>
              <el-button @click="Goedit" style="margin-top:2vh">修改个人信息</el-button>
              <br>
              <el-button @click="Goreport" style="margin-top:2vh">查看健康日志</el-button>
              <br>
              <el-button @click="Goout" style="margin-top:2vh">登出</el-button>
            </div>
          </div>
        </el-card>
      </el-aside>
      <el-main class="me-articles" v-loading="article_loading">
        <h2 class="me-articles-title">我的帖子</h2>
        <ArticleItem v-for="article in articles" v-bind='article' :key="article.id" id="items"></ArticleItem>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import ArticleItem from "@/components/ArticleItem.vue"
  import axios from 'axios'
  import { ref } from 'vue'
  const loading = ref(true)

export default {
  components: {
    ArticleItem
  },
  data() {
    return {
      activeIndex: '4',
      username:'',
      email:"",
      mobile:"",
      job:"",
      home:"",
      edit:"",
      photo:"",
      articles: [],
      loading: true,
      article_loading: true
    }
  },
  created() {
    var jwt = sessionStorage.getItem("accessToken")
    axios.get('/api/blog/getMyBlogs/', {
        headers: { 'Authorization': jwt }
      }
    )
      .then((res) => {//接口
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
        this.articles = res.data['blogList']
        this.article_loading = false;
      })
      .catch((err) => {
        console.error(err);
      });
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
      this.loading = false;
    })
    .catch((err) => {
      console.error(err);
    });
  },
  methods: {
    Gowriter() {
      this.$router.push({ path: '/Writer' })
    },
    Goedit() {
      this.$router.push({ path: '/EditInfo' })
    },
    Goreport() {
      this.$router.push({ path: '/HealthReports' })
    },
    Goout() {
      var jwt = sessionStorage.getItem("accessToken")
      axios.get('/api/account/logout/',{
            headers:{'Authorization': jwt}
          }
      )
      .then((res)=>{//接口
        if(res.status === 401){
          sessionStorage.clear()
          this.$router.push(
              {
                path: '/NoLogIn',
                query: {
                }
              }
          );
          return;
        }
          this.$router.push({ path: '/' })
      })
      .catch((err)=>{
          console.error(err);
      });
    },
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

</style>