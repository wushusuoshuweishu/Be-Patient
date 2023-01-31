<template>
    <div class="me-article-header">
      <div class="me-article-title">{{remark}}</div>
      <div>
        <el-image :src="checklist"></el-image>
      </div>
    </div>
</template>

<script>
  export default {
    created() {
      this.remark=this.$route.query.remark[0];
      this.checklist=this.$route.query.checklist[0];
      this.id=this.$route.query.id[0];
    },
    name: 'ChecklistItem',
    data() {
      return {
        remark: '',
        checklist: '',
        id: 0
      }
    },
    methods: {
      check(title) {
        this.$router.push({path: `/check/${id}`,
                    query: {
                    }})
      }
    }
  }
</script>

<style scoped>
  .el-card{
    width: 40vw;
  }
</style>