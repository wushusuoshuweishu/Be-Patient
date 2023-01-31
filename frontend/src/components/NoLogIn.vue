<template>
  <div id="whole_body">
    <el-container>
        <el-col>
          <el-result icon="error" title="你还没登录！" subTitle="返回登陆页面">
            <template slot="extra">
              <el-button type="primary" size="medium" @click="goBack">返回</el-button>
            </template>
          </el-result>
        </el-col>
    </el-container>
  </div>
</template>

<script>
  export default{
    methods:{
      goBack() {
        this.$router.push({path: `/`});
      }
    },
    data() {
      return {}
    }
  }
</script>

<style scoped>
*{
  text-align: center;
}
</style>
