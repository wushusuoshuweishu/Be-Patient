<template>
  <div>
    <el-container>
      <el-header>
        <el-button @click="goBack">←返回</el-button>
        <el-button @click="deleteBlog">删除帖子</el-button>
        <el-button @click="addStar">帖子加精</el-button>
      </el-header>
      <el-container class="article-area">
        <el-main class="me-articles">
          <div style="background-color: white; -moz-border-radius: 1vmin;-webkit-border-radius: 1vmin; border-radius:1vmin; padding: 0.5vmin; margin: 1vmin;">
            <div class="me-article-header">
              <div class="me-article-title"><h3>{{article.blog_title}}</h3></div>
            </div>
            <div class="me-article-description">
              <h5 class="hisummray">{{article.summary}}</h5>
            </div>
            <div class="me-article-footer">
              <span class="me-article-username">
                <i class="el-icon-user-solid"></i>&nbsp;{{article.username}}
              </span>
              <span class="me-pull-right me-article-count">
                <i class="el-icon-time"></i>&nbsp;{{article.time}}
              </span>
            </div>
              <div class="me-article-tags"><el-tag v-for="t in article.labels" :key="t" size="mini" type="success">{{t}}</el-tag></div>
            <div class="me-article-content"><pre>{{article.blog_content}}</pre>
              </div>
          </div>
          <div class="comment_area" v-if="this.commentList.length > 0">
            <h2 class="pinglun">评论</h2>
            <CommentItem class="comments" v-for="one_comment in commentList" v-bind="one_comment" :key="one_comment.id">???</CommentItem>
          </div>
        </el-main>
      </el-container>
      <el-footer class="footer">
        <el-form>
        <el-form-item>
            <el-input v-model="form.comment" placeholder="发表你的评论..."></el-input>
        </el-form-item>
          <el-form-item>
            <el-button type="primary" @click=onSubmit size="mini">发表评论</el-button>
          </el-form-item>
        </el-form>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
  import ArticleItem from "@/components/ArticleItem.vue";
  import CommentItem from "@/components/CommentItem.vue";
  import axios from 'axios';
  export default{
    created() {
      var jwt = sessionStorage.getItem("accessToken")
      var needed_id = this.$route.query.id[0]
      axios.get(`/api/blog/getBlogByID/${needed_id}/`,{
            headers:{'Authorization': jwt},
            blog_id: parseInt(needed_id),
          }
      )
      .then((res)=>{//接口
          this.article = res.data;
          this.article["blog_content"] = this.article["blog_content"].replaceAll("<br>","\n");
      })
      .catch((err)=>{
          console.error(err);
      });
      axios.get(`/api/blog/getComments/${needed_id}/`,{
          headers:{'Authorization': jwt},
          blog_id: parseInt(needed_id),
        }
      )
      .then((res)=>{//接口
            this.commentList = res.data['commentList'];
      })
      .catch((err)=>{
          console.error(err);
      });

      }
    ,
    methods:{
      goBack() {
        this.$router.push({path: `/Forum`,
                    query: {
                    }});
      },
      deleteBlog(){
        this.$confirm('此操作将永久删除该文章, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          var jwt = sessionStorage.getItem("accessToken")
          axios.post('/api/blog/deleteBlog/',{
            blog_id: parseInt(this.article.id),
          },{headers:{'Authorization': jwt}}
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
          this.$router.push({path: `/PersonalHomePage`,
                    query: {
                    }});
        })
        .catch((err)=>{
            console.error(err);
        });
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      onSubmit(){
        var jwt = sessionStorage.getItem("accessToken")
        axios.post('/api/blog/publishComment/',{
            blog_id: parseInt(this.article.id),
            content: this.form['comment']
          },{headers:{'Authorization': jwt}}
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
          this.$router.go(0);
        })
        .catch((err)=>{
            console.error(err);
        });
      },
      addStar(){
        var jwt = sessionStorage.getItem("accessToken")
        axios.post('/api/blog/setStarBlog/',{
            blog_id: parseInt(this.article.id),
          },{headers:{'Authorization': jwt}}
        )
        .then((res)=>{//接口
            this.$router.go(0);
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
        })
        .catch((err)=>{
            console.error(err);
            this.$router.go(0);
        });
      }
    },
    components:{
      ArticleItem,CommentItem
    },
    data(){
      return {
        star_id: 0,
        form:{
          comment:''
        },
        article:
          {
            id:"0",
            blog_title:"错误！",
            summary:"您想要的文章加载失败！请检查网络设置或联系网站管理员。",
            labels:["ERROR"],
            time:"00/00",
            username:"ERROR",
            blog_content:""
          },
        commentList:[

            ]
      }
      }
  }
</script>

<style scoped>
  ::-webkit-scrollbar {
    width: 0 !important;
    height: 0 !important;
  }

  .el-container {
    height: 100%;
    margin-top: 0 !important;
  }

  .el-main {
    padding: 0px;
    margin-top: 0;
    line-height: 2vw;
  }

  .el-card {
    width: 60vw;
    margin-left: 2vw;
    margin-right: 2vw;
    margin-top: 2vh;
  }

  .el-tabs
  {
    text-align: left;
    background-color: white;
  }

  .ads {
    height: max-content;
  }

  .article-area{
    margin-left: 2vw;
    margin-top: 5vh;
    width: 65vw;
  }

  .el-main{
    border-radius: 4px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    height: 100%;
    text-align: left;
    line-height: 1.5vw;
  }

  .el-main div {
    text-align: center;
  }

  .me-articles{
    height: 70vh;
    width: 70vw;
    margin: auto;
  }

  h5, el-main, .me-article-content {
    text-align: left !important;
    margin: 2vw;
  }

  .me-article-content {
    text-indent: 2em;
  }

  .el-form /deep/{
    margin-left: 8vw;
    margin-bottom: 1vh;
    margin-top: 3vh;
    width: 50vw;
  }

  .el-button{
    top: 1vh;
  }

  .pinglun{
    margin-left: 0px;
  }

  .comment_area{
    margin-left: 0;
    overflow-x: auto;
  }

  .hisummray {
    text-align: center !important;
  }

  .el-header {
    text-align: left;
    margin-top: 3vw;
    margin-bottom: 0;
    margin-left: 1vw;
  }

  pre {
    white-space: pre-wrap; /* CSS-3 /
    white-space: -moz-pre-wrap; / Mozilla, since 1999 /
    white-space: -pre-wrap; / Opera 4-6 /
    white-space: -o-pre-wrap; / Opera 7 /
    Word-wrap: break-word; / Internet Explorer 5.5+ */
  }

</style>
