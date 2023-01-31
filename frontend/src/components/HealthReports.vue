<template>
  <div>
    <el-header>
      <el-button @click="goBack">←返回</el-button>
    </el-header>
    <el-container>
      <DailyHealth v-for="rp in reports" v-bind='rp' :key="rp"></DailyHealth>
    </el-container>
  </div>
</template>

<script>
  import DailyHealth from "@/components/DailyHealth.vue"
  import axios from "axios";
  export default{
    methods:{
      goBack(){
        this.$router.push('/PersonalHomePage');
      }
    },
    components:{
      DailyHealth
    },
    created() {
      var jwt = sessionStorage.getItem("accessToken")
      axios.get('/api/healthAid/getHealthAid/',{
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
          this.reports = res.data['health_aid']
      })
      .catch((err)=>{
          console.error(err);
      });
    },
    data(){
      return{
        reports: [],
      }
    }
  }
</script>

<style>

</style>