<template>
    <div>
        <el-container>
            <el-time-picker v-model="value" placeholder="请选择新增用药提醒的时间点" style="width:30vmin;margin-left:0; margin-right:auto;" value-format="HH:mm:ss"/>
        </el-container>
        <el-container>
            <el-input v-model="input" placeholder="请输入药物名称" clearable id="searchInput" />
            <el-button type="primary" icon="el-icon-edit" @click.native="addReminder">添加</el-button>
        </el-container>
        <el-container>
            <el-button type="primary" icon="el-icon-edit" @click.native="deleteReminder">删除当前提醒</el-button>
        </el-container>
    </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios';
const input = ref('')
const value = ref()

export default {
    name: 'Reminder',
    data() { 
        return {
            input,
            value
        }
    },
    methods: {
        deleteReminder() {
            var jwt = sessionStorage.getItem("accessToken")
            axios.post('/api/timer/deleteTimer/', {}, {
                headers: { 'Authorization': jwt }
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
                console.log(res);
                this.$alert('您已成功删除当前帐号的用药提醒。', '提示', {
                    confirmButtonText: '确定',
                    callback: OK => {
                    this.$message({
                    type: 'info',
                        message: `${ OK }`
                        });
                    }
                });
            })
            .catch((error) => {
                console.log(error);
            });
        },
        addReminder() {
            var jwt = sessionStorage.getItem("accessToken")
            axios.post('/api/timer/addTimer/', {
                    schedule_time: this.value,
                    schedule_message: this.input
                },{
              headers: { 'Authorization': jwt }
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
                console.log(res);
                this.$alert('您已成功添加用药提醒，请注意接收用药提醒邮件，按时吃药。', '提示', {
                    confirmButtonText: '确定',
                    callback: OK => {
                    this.$message({
                    type: 'info',
                        message: `${ OK }`
                        });
                    }
                });
            })
            .catch((error) => {
                console.log(error);
            });
        }
    }
}
</script>

<style scoped>
.el-input {
    margin: auto;
    margin-left: 0;
    margin-right: 2vmin;
    width: 40vw;
}

.el-button {
    margin: auto;
    text-align: center;
    width: 10vw;
    margin-left:0;
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
