<template>
  <el-card>
    <el-container>
      <el-main>
        <h2>{{title}}</h2>
        <div>高压：{{gaoya}}mmHg</div>
        <div>低压：{{diya}}mmHg</div>
        <div>血糖：{{xuetang}}mmol/L</div>
        <div>血脂：{{xuezhi}}mmol/L</div>
        <h5>{{abstract}}</h5>
        <div>{{content}}</div>
        <h4>健康建议</h4>
        <div>{{suggest}}</div>
      </el-main>
    </el-container>
  </el-card>
</template>

<script>
  import axios from 'axios';
  export default{
    created() {
      this.suggest = ''
    for(var key in this.abnormal){
      var item = ''
      if(key === 'xuetang'){
        item = '血糖'
      }
      if(key === 'diya'){
        item = '血压(低压)'
      }
      if(key === 'xuezhi'){
        item = '血脂'
      }
      if(key === 'gaoya'){
        item = '血压(高压)'
      }
      this.suggest = this.suggest + item
      if(this.abnormal[key] === 'too high'){
        item = '过高'
      }
      if(this.abnormal[key] === 'too low'){
        item = '过低'
      }
      this.suggest = this.suggest + item + ' '
    }
    if(this.suggest === ' '){
      this.suggest = "您的健康状况良好！"
    }
    else{
      this.suggest = this.suggest + '请及时调整生活习惯！'
    }
      },
    methods:{

    },
    props:{
      title: String,
      abstract: String,
      diya: String,
      gaoya: String,
      xuetang: String,
      xuezhi: String,
      content: String,
      suggest: String,
      abnormal: {}
    },
    data(){
      return {
      }}
  }
</script>

<style scoped>
*{
 text-align: center !important;
}
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
</style>
