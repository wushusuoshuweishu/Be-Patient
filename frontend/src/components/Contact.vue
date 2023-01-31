<template>
    <div>
                    <el-button class="contactbutton" @click="visible11" type="primary" icon="el-icon-chat-line-round">Contact</el-button>
                    
                    <!--对话框-->

                    <el-dialog :visible.sync="visible" :title="fri_name">
                        <div style="height: 500px; overflow-y: auto" id="bigBox">
                        
                        <div
                            v-for="(item, index) in msglist"
                            class="msgCss"
                            :style="{textAlign: item['align']}"
                        >
                            
                            <span v-if="item && item['align'] == 'left'">
                            <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                            <span>{{item['text']}}</span>
                            
                            </span>
                            
                            <span v-if="item && item['align'] == 'right'">
                            {{item.text}}
                            <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                            </span>
                        </div>
                        </div>
                        <div style="margin-top: 15px">
                        <el-input
                            placeholder="请输入内容"
                            v-model="input3"
                            class="input-with-select"
                            :autofocus="true"
                            ref="serachBox"
                        >
                            <el-button
                            :loading="loading"
                            @keydown.enter.native="handleMsg"
                            slot="append"
                            type="primary"
                            @click="handleMsg"
                            >发送</el-button
                            >
                        </el-input>
                        </div>
                    </el-dialog>
    </div>
</template>


<script>
import axios from 'axios';

export default{
    name : 'Contact',
    props:{
      fri_name:String
    },
    created(){
      var jwt = sessionStorage.getItem("accessToken")
      axios.get('/api/account/isLoggedIn/',{
        headers:{'Authorization': jwt}
      })
        .then((res)=>{
          if(res.status === 200){
            console.log("获取用户名");
            this.myname = res.data ;  //获取用户名
          }
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
        })
    },
    mounted(){     //每隔1s脉冲检测
      this.timer = setInterval(() =>{
        
        this.getMsg();
        this.scrollTop11();
      },1000);
    },
    beforeDestroy(){
      if(this.timer){
                clearInterval(this.timer);
            }
    },
    data(){
        return{
            myname:"",
            timer:null,//计时器
            visible: false,
            input3: "",
            msglist: [],
            loading: false,
            show3: false,
            show4: false ,
            the_fri_msg:[],
            my_msg:[]
        } 
    },
    methods: {
        visible11() {
          this.visible = true;
          this.$nextTick(() => {
            this.$refs.serachBox.focus();
          });
        },
        timestampToTime(times) {
            let time = times[1]
            let mdy = times[0]
            mdy = mdy.split('/')
            let month = parseInt(mdy[0]);
            let day = parseInt(mdy[1]);
            let year = parseInt(mdy[2])
            return year + '-' + month + '-' + day + ' ' + time
        },
        handleMsg() {
          
          console.log(this.input3, "发送信息");
          if (this.input3 !== "") {
            this.loading = true;
            console.log("发送信息");

            var jwt = sessionStorage.getItem("accessToken")
            axios.post('/api/chat/sendMessage/',{
                friend_name: this.fri_name,
                content: this.input3
              
            },{headers:{'Authorization': jwt}})
            .then((res)=>{
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
              if(res.status === 201){
                this.input3 = "";
                this.loading = false;
                console.log("发送信息成功");
              }
            }).catch((err)=>{
              console.log(err);
            });

           
            
          }
          


            /*
           * 模拟信息返回
           
          setTimeout(async () => {
            let listMsg = {
              align: "left",
              text: "模拟信息",
              link: "",
            };
            await this.msglist.push(listMsg);
            await this.scrollTop11();
            this.loading = false;
          }, 1000);*/

        },
        getMsg() {
          // 处理自己的接口请求 返回需要的数据
          var jwt = sessionStorage.getItem("accessToken");
          axios
            .get('/api/chat/getMessage/',{
                headers:{'Authorization': jwt}
            })
            .then((res)=>{
              if(res.status === 200){
                
                
                let msg_all = res.data['message_list'];
                this.the_fri_msg.length = 0;
                this.my_msg.length = 0;
                for(let e in msg_all){
                  if(msg_all[e]['sender'] == this.fri_name){
                    this.the_fri_msg.push(msg_all[e]);
                  }
                  if(msg_all[e]['sender'] == this.myname && msg_all[e]['receiver'] == this.fri_name){
                    this.my_msg.push(msg_all[e]);
                  }
                }
                
              }
              
              
            })
            .catch((err)=>{
              console.log(err);
            });
            this.computemsglist();
         
          
        },
        computemsglist(){
          this.msglist.length = 0;
          let msgall = [];
          msgall = this.my_msg.concat(this.the_fri_msg);
          const compare = function (obj1, obj2) {
              const val1 = obj1['time'];
              const val2 = obj2['time'];
              if (val1 < val2) {
                  return -1;
              } else if (val1 > val2) {
                  return 1;
              } else {
                  return 0;
              }
          }
          msgall = msgall.sort(compare);
          for(let e in msgall){
            
            let text = msgall[e]['content'];
        
            if(msgall[e]['sender'] == this.fri_name){

              this.msglist.push({'align':"left",'text':text});
            }else{
              this.msglist.push({'align':"right",'text':text});
            }
            
          }

        },
        // 处理滚动条一直保持最上方
        scrollTop11() {
          let div = document.getElementById("bigBox");
          div.scrollTop = div.scrollHeight;
        },
    }
}
</script>