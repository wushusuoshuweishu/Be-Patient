<template>
  <el-card class="fl" @click.native=view(id) shadow="always">
    <div class="me-article-header">
      <div class="me-article-title">{{blog_title}}</div>
    </div>

    <div class="me-article-description">
      {{summary}}
    </div>
    <div class="me-article-footer">
	  	<span class="me-article-username">
	    	<i class="el-icon-user-solid"></i>&nbsp;{{username}}
	    </span>

      <el-tag v-for="t in labels" :key="t" size="mini" type="success">{{t}}</el-tag>

      <span class="me-pull-right me-article-count">
	    	<i class="el-icon-time"></i>&nbsp;{{time}}
	    </span>
    </div>
  </el-card>
</template>

<script>
  export default {
    name: 'ArticleItem',
    props: {
      username: String,
      blog_title: String,
      summary: String,
      id: String,
      labels: Array,
      time: String
    },
    data() {
      return {}
    },
    methods: {
      view(id) {
        this.$router.push({path: `/view`,
          query: {id:id}
        })
      }
    }
  }
</script>

<style scoped>
.me-article-title /deep/{
  font-size: 20px;
  font-family: "黑体";
}

</style>
