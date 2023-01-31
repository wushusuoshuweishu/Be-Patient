<template>
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        >
    <el-menu-item index="1" @click="GoPersenalHomepage">
        <el-avatar class="small_avatar" :src="photo" v-loading="avatar_loading"></el-avatar>
    </el-menu-item>
    <el-menu-item index="2" @click="GoForum">论坛</el-menu-item>
    <el-menu-item index="3" @click="Gochat">聊天</el-menu-item>
    <el-menu-item index="4" @click="GoHealthAid">健康日志</el-menu-item>
    <el-menu-item index="5" @click="GoPersenalHomepage">个人中心</el-menu-item>
    <el-menu-item index="6" @click="GoSearch">搜索</el-menu-item>
    <el-menu-item index="7" @click="GoReminder">服药提醒</el-menu-item>
    <el-menu-item index="8" @click="GoAboutUs">关于我们</el-menu-item>
    </el-menu>
</template>

<script>
import { ref } from 'vue'
import axios from "axios";
const activeIndex = ref('2')

export default {
    name: "PageHeader",
    methods: {
        Gochat() {
            this.$router.push("/Chat");
            activeIndex.value = '3'
        },
        GoForum() {
            this.$router.push("/Forum");
            activeIndex.value = '2'
        },
        GoPersenalHomepage() {
            this.$router.push("/PersonalHomePage");
            activeIndex.value = '5'
        },
        GoHealthAid() {
            this.$router.push("/HealthAid");
            activeIndex.value = '4'
        },
        GoSearch() {
            this.$router.push("/SearchInfo");
            activeIndex.value = '6'
        },
        GoReminder() {
            this.$router.push("/Reminder");
            activeIndex.value = '7'
        },
        GoAboutUs() {
            this.$router.push("/About");
            activeIndex.value = '8'
        }
    },
    data() { 
        return {
            activeIndex,
            photo: '',
            avatar_loading: true
        }
    },
    created() {
        if (this.photo === '') {
            var jwt = sessionStorage.getItem("accessToken")
            axios.get('/api/account/getAccountInfo/', {
            headers: { 'Authorization': jwt }
            }
            ).then((res) => {//接口
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
                this.photo = res.data['photo'];
                this.avatar_loading = false;
            })
            .catch((err) => {
            console.error(err);
            });
    }
  },
}
</script>

<style scoped>
.el-menu {
    padding: 0vw;
    margin: 0vh;
}
</style>