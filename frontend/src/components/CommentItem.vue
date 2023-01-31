<template>

  <el-card class="fl" shadow="always">

    <div class="comment_content">
      {{content}}
    </div>
    <div class="me-footer">
	  	<span class="me-article-username">
	    	<i class="el-icon-user-solid"></i>&nbsp;{{username}}
	    </span>

      <span class="me-pull-right me-article-count">
	    	<i class="el-icon-time"></i>&nbsp;{{time}}
	    </span>

      <el-button class="deleter" size="mini" @click="deleteComment">删除评论</el-button>
    </div>
    <el-dialog
    title="提示"
    :visible.sync="dialogVisible"
    width="30%">
    <span>删除失败！你没有权限！</span>
    <span slot="footer" class="dialog-footer">
      <el-button type="primary" @click="dialogVisible = false">确定</el-button>
    </span>
  </el-dialog>
  </el-card>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'CommentItem',
    props: {
      id: String,
      username: String,
      content: String,
      time: String
    },
    data() {
      return {
        dialogVisible: false
      }
    },
    methods:{
      deleteComment(){
        var jwt = sessionStorage.getItem("accessToken")
        axios.post('/api/blog/deleteComment/',{
              comment_id: parseInt(this.id)
            },
            {
              headers:{'Authorization': jwt}
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
              this.$router.go(0);
            }
            else if(res.status === 500){
              this.dialogVisible = true
            }
        })
        .catch((err)=>{
            console.error(err);
        });
      }
    }
  }
</script>

<style scoped>
  .el-card{
    width: 960px;
  }
  .comment_content{
    font-size: 16px;
  }
  .me-footer{
    font-size: 12px;
  }
  .deleter{
    position: relative;
    right: 0px;
    border: hidden;
  }
</style>