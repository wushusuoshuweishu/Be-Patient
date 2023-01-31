<template>
  <el-tabs value="first">
    <el-tab-pane label="关于我们" name="first">小组成员：杜家锟 何沐 王麒杰 吴俊坚</el-tab-pane>
    <el-tab-pane label="联系方式" name="second">email邮箱：plgydamumu@foxmail.com</el-tab-pane>
    <el-tab-pane label="coding仓库" name="third">仓库地址：https://be-patient.coding.net/p/be-patient</el-tab-pane>
    <el-tab-pane label="github仓库" name="fourth">仓库地址：https://github.com/MuXiaoYun/Be-Patient</el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  name: "PageFooter",
}
</script>

<style scoped>
.el-tabs{
    text-align: left;
    background-color: white;
    padding:1.5vh;
  }
</style>