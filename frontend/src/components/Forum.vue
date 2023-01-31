<template>
  <div>
    <el-main class="me-articles" v-loading="main_loading">
      <ArticleItem v-for="article in articles" v-bind='article' :key="article.id"></ArticleItem>
      <el-button type="primary" icon="el-icon-edit" @click="commitBlog" id="commitBlog" >发帖</el-button>
    </el-main>
  </div>
</template>

<script>
  import ArticleItem from "@/components/ArticleItem.vue"
  import axios from 'axios';
  import {SM2, SM4} from "gm-crypto";
  export default{
    components:{
      ArticleItem
    },
    created(){
      var jwt = sessionStorage.getItem("accessToken")
      axios.get('/api/blog/getBlogs/',{
            headers:{'Authorization': jwt}
          }
      )
      .then((res)=>{//接口
        this.articles = res.data['blogList']
        this.main_loading = false;
      })
      .catch((err)=>{
          console.error(err);
      });
    },
    data(){
      return {
        activeIndex: '1',
        articles:[

        ],
        main_loading: true
      }
    },
    methods: {
      commitBlog(){
        this.$router.push('/Writer')
      }
    },  
  }
</script>

<style scoped>

  .el-card {
    margin: auto;
    width: 60vw;
    margin-top: 5vw;
  }

  .el-tabs
  {
    text-align: left;
    background-color: white;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }

  .ads {
    height: max-content;
  }

  #commitBlog {
    margin-top: 3vw;
  }

  .ArticleItem{
    margin: auto;
  }
</style>
