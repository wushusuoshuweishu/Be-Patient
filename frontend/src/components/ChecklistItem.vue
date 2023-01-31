<template>
  <el-card class="fl" shadow="always">
    <div class="me-article-header">
      <div class="me-article-title">{{remark}}</div>
      <div>
        <el-image :src="checklist"></el-image>
      </div>
      <div>
        <el-button @click.stop="deleteChecklist" id="btn">删除</el-button>
        <el-button @click.stop="downloadImg" id="dld">下载</el-button>
      </div>
    </div>
  </el-card>
</template>

<script>
  import axios from "axios";

  export default {
    name: 'ChecklistItem',
    props: {
      remark: String,
      checklist: String,
      id: String
    },
    data() {
      return {
      }
    },
    methods: {
      deleteChecklist(){
        var jwt = sessionStorage.getItem("accessToken")
          axios.post('/api/checklist/deleteChecklist/',{
              checklist_id: parseInt(this.id)
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
              this.$router.go(0);
        })
        .catch((err)=>{
          console.error(err);
          this.showReminder = true;
        });
      },
      downloadImg(){
        const a = document.createElement('a')
        a.href = this.checklist
        a.setAttribute('download', 'checklist-download')
        a.click()
      }
    }
  }
</script>

<style scoped>

</style>