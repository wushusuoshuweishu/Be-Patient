<template>
    <el-aside class="affix-container">
            <el-carousel class="ads">
                <el-carousel-item v-for="item in 3" :key="item">
                  <h3><br/>{{ item }}</h3>
                </el-carousel-item>
            </el-carousel>
            <el-container class="hot_topic_container">
              <h3 id="choosed">版主精选</h3>
              <ArticleItem class="hot_topic" v-for="Rarticle in Rarticles" v-bind='Rarticle' :key="Rarticle.id"></ArticleItem>
            </el-container>
    </el-aside>
</template>

<script>
import ArticleItem from "@/components/ArticleItem.vue"
import axios from "axios";
export default {
    created() {
      var jwt = sessionStorage.getItem("accessToken")
      axios.get(`/api/blog/getStarBlog/`,{
          headers:{'Authorization': jwt},
        }
      )
      .then((res)=>{//接口
          this.star_id = res.data['id'];
          console.log("star:")
          console.log(this.star_id)
          var temp_star_id = this.star_id.toString()
          axios.get(`/api/blog/getBlogByID/${temp_star_id}/`,{
                headers:{'Authorization': jwt},
                blog_id: this.star_id,
              }
          )
          .then((res)=>{//接口
              this.Rarticles = [res.data]
          })
          .catch((err)=>{
              console.error(err);
          });
      })
      .catch((err)=>{
          console.error(err);
      });
    },
  name: "Sidebar",
    components:{
        ArticleItem
    },
    data() {
        return {
            Rarticles:[
              {
                id:"0",
                blog_title:"错误！",
                summary:"您想要的文章加载失败！请检查网络设置或联系网站管理员。",
                labels:["ERROR"],
                time:"00/00",
                username:"ERROR",
              }
        ]}
    }
}
</script>

<style scoped>
::-webkit-scrollbar {
  width: 0 !important;
  height: 0 !important;
}

.el-carousel__item h3 {
    color: #475669;
    font-size: 1vw;
    opacity: 0.75;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
    -moz-border-radius: 1vmin;
    -webkit-border-radius: 1wmin; border-radius:1vmin;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
    -moz-border-radius: 1vmin;
    -webkit-border-radius: 1wmin; border-radius:1vmin;
}

.el-aside {
    margin-top: 8vh;
    padding-right: 1vw;
    height: 1.5vh;
}

#choosed {
    width: 1.5vw;
    font-size:1vw;
}

.hot_topic{
    flex: fit-content;
    height: 20vh;
    width: 2vw;
    margin-top: 1vw;
    overflow: scroll;
}

.hot_topic_container{
    width: 100%;
    height: 30vh;
    -moz-border-radius: 1vmin;
    -webkit-border-radius: 1wmin; border-radius:1vmin;
}


</style>
  