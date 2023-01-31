<template>
    <div>
        <el-container>
            <el-input v-model="input" placeholder="Please input" clearable id="searchInput" />
            <el-button type="primary" icon="el-icon-search" @click.native="searchKnowledge">搜索</el-button>
        </el-container>
        <el-container>
            <el-card class="box-card">
                <template #header>
                <div class="card-header">
                    <span>{{ CardName }}</span>
                </div>
                </template>
                <div class="text item" id="textitem" v-html="message"></div>
            </el-card>
        </el-container>
    </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios';
import urlencode from 'urlencode'
const input = ref('')
export default {
    name: 'Search',
    data() { 
        return {
            input,
            message: '',
            CardName: '搜索结果'
        }
    },
    methods: {
        searchKnowledge() {
            var searchword = document.getElementById('searchInput').value
            var temp_url = 'https://www.dayi.org.cn/search?keyword=' + urlencode(searchword)
            window.open(temp_url)
          /*
            var jwt = sessionStorage.getItem("accessToken")
            axios.get('/api/search/searchByWord/', {
                headers: { 'Authorization': jwt },
                params: {
                    search_word: searchword
                }
            }).then((res) => {
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
                this.CardName = "\"" + searchword + "\"" + '的搜索结果'
                var tempMessage = res.data['message']
                this.message=(tempMessage + '').replace(/\n/g,"<br/>&nbsp&nbsp&nbsp&nbsp")
            }).catch((err) => {
                if (err.response.status === 500) {
                    console.log("yes")
                    this.$alert('输入信息过于模糊，请清晰地输入您想搜索的药品或病症名称', '检索失败', {
                        confirmButtonText: '确定',
                        callback: action => {
                            this.$message({
                            type: 'info',
                            message: `已知晓`
                            });
                        }
                    });
                }
                console.error(err);
            });*/
        },
    }
}
</script>

<style scoped>
.el-input {
    margin: auto;
    width: 80vw;
}

.el-button {
    margin: auto;
    text-align: center;
    width: 10vw;
    margin-left: 0.5vw;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 1.75vh;
}

.item {
  margin-bottom: 1.75vh;
}

.box-card {
  width: 80vw;
  height: 50vh;
  margin: auto;
}

#textitem {
    padding:1vh;
    text-align: left;
}

.el-container {
    margin: 5vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
