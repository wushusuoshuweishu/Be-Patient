<template>
    <el-container>
        <div id="fri">
            <h2 class="frititle">好友列表</h2>
            <div id="buttons">
                <el-button class="add_button" @click="visible2" type="primary" icon="el-icon-user" >添加好友</el-button>
            <el-button class="add_group" @click="addgroup" type="primary" icon="el-icon-folder-add" >新建分组</el-button>
            </div>
                
            <el-container direction="vertical">
                <el-dialog :visible.sync="visible">
                    <div style="height: 40vh; overflow-y: auto">
                        <el-input 
                            placeholder="请输入您所要添加的用户名"
                            v-model="input3"       
                            class="input-with-select"
                            :autofocus="true"
                            ref="serachBox">
                                <el-button
                                :loading="loading"
                                slot="append"
                                type="primary"
                                @click="search_user"
                                    >搜索
                                </el-button>
                        </el-input>
                        <div v-show="visible4" class="result">
                            <el-avatar :size="size" src=""></el-avatar>
                            <h3 class="fri_name" v-text="this.searchuser.username"></h3>
                            <el-button @click="add_searchuser" type="primary" icon="el-icon-circle-plus-outline" circle></el-button>
                        </div>

                        <div v-for="(a,i) in addme" class="addme">
                            <el-avatar :size="size" :src="a.src"></el-avatar>
                            <h3 v-text="a.friend_name"></h3>
                            <h3 v-text="a.remark"></h3>
                            <el-button @click="handlerequest(2,a.friend_name)" type="primary" icon="el-icon-success" circle></el-button>
                            <el-button @click="handlerequest(1,a.friend_name)" type="primary" icon="el-icon-error" circle></el-button>
                        </div>
                        
                    </div>
                </el-dialog>
            <Group v-for="group in groups" v-bind='group' :key="group.id" :group_type="grouptype"></Group> 
            </el-container>
        </div>
    </el-container>
</template>

<style scoped>
::-webkit-scrollbar {
  width: 0 !important;
  height: 0 !important;
}

#fri{
    margin: auto;
    margin-top: 10vh;
    width: 90vw;
    height: 60vh;
    -moz-border-radius: 1vmin;
    -webkit-border-radius: 1wmin;
    border-radius: 1vmin;
}

.add_button, .add_group{
    right:5vw;
}

#buttons {
    text-align: right !important;
    margin:1vw;
}

.frititle{
    font-size: 2vw;
} 
</style>

<script>
    import Group from "@/components/Group.vue"
import axios from "axios";
    export default{
        components:{
            Group
        },
        created(){

            var jwt = sessionStorage.getItem("accessToken")
            axios.get('/api/account/getFriends/',{
                    headers:{'Authorization': jwt}
                })
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
                                if(res.status === 200){
                                    this.grouptype.length = 0;
                                    this.groups.length =0 ;
                                    let count=0;
                                    for(let e in res.data.friendList){
                                        
                                        this.groups[count] = {
                                            groupname : e,
                                            list : res.data.friendList[e]
                                        };
                                        count++;
                                        this.grouptype.push(e);
                                    }

                                }
                            }).catch((err)=>{
                                console.log("更新好友列表失败");
                            });

            this.visible2();
            this.visible = false ;
        },
        mounted(){
            var jwt = sessionStorage.getItem("accessToken")
            this.timer = setInterval(()=>{   //更新好友列表
                axios.get('/api/account/getFriends/',{
                    headers:{'Authorization': jwt}
                })
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
                                if(res.status === 200){
                                   
                                    this.grouptype.length = 0;
                                    this.groups.length =0 ;
                                    let count=0;
                                    for(let e in res.data.friendList){
                                        
                                        this.groups[count] = {
                                            groupname : e,
                                            list : res.data.friendList[e]
                                        };
                                        count++;
                                        this.grouptype.push(e);
                                    }

                                }
                            }).catch((err)=>{
                                console.log("更新好友列表失败");
                            });
            },1000);
            
        },
        beforeDestroy() {
            if(this.timer){
                clearInterval(this.timer);
            }
        },
        data(){
            return{
                grouptype:['default'],
                timer:null,
                groups:[
                

                ],
                visible:false,
                visible4:false,
                input3:"",
                loading:false,
                addme:[],                
                searchuser:{},
                myremark:""                
            }
        },
        methods:{
            GoForum(){
                this.$router.push('/Forum')
            },
            visible2(){
                this.visible = true;
                /*this.$nextTick(() => {
                this.$refs.serachBox.focus();
            }); */
                
                this.addme.length = 0;
                var jwt = sessionStorage.getItem("accessToken")
                axios.get('/api/account/getFriendRequests/',{
                    headers:{'Authorization': jwt}
                })
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
                    if(res.status === 200 ){
                        this.addme = res.data.friendRequestList ;
                        console.log("获取申请列表成功");
                    }
                }).catch((err)=>{
                    console.log(err);
                });
            },
            addgroup(){
                this.$prompt('请输入新建组名', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消'
                    
                    }).then(({ value }) => {
                        this.$message({
                            type: 'success',
                            message: '新建分组是: ' + value
                        });
                        var jwt = sessionStorage.getItem("accessToken")
                        axios.post('/api/account/addGroup/',{
                            group_name: value
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
                                console.log("新建分组成功");
                            }
                        }).catch((err)=>{
                            console.log(err);
                        });

                    }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消输入'
                    });       
                    });
            },
            search_user(){
                console.log(this.input3, "搜索信息");
            if (this.input3 !== "") {
                this.loading = true;
                var jwt = sessionStorage.getItem("accessToken")
                axios.get(`/api/account/searchUser/${this.input3}/`,{
                    headers:{'Authorization': jwt},
                    params:{ username: this.input3 }
                }).then((res)=>{
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
                    if(res.status === 200){
                        this.searchuser = {};
                        this.searchuser = res.data ;
                        this.visible4 = true
                    }
                }).catch((err)=>{
                    console.log(err);
                });
                this.input3 = "";
                this.loading = false;
                }
            },
            add_searchuser(){
                this.$prompt('请输入备注', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消'
                    
                    }).then(({ value }) => {
                        this.$message({
                            type: 'success',
                            message: value + '备注已发送'
                        });
                        var jwt = sessionStorage.getItem("accessToken")
                        axios.post('/api/account/sendAddFriendRequest/',{
                            friend_name: this.searchuser['username'],
                            remark: value
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
                                console.log("发送请求成功");
                                this.visible4 = false;
                            }
                        }).catch((err)=>{
                            console.log(err);
                        });

                    }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消输入'
                    });       
                    });
                    this.visible2();
                        /*
                        axios.post('/api/account/sendAddFriendRequest/',{
                                friend_name: this.searchuser[username],
                                remark: value   
                        },{headers:{'Authorization': jwt}})
                        .then((res)=>{
                            if(res.status === 201){
                                console.log("发送请求成功");
                                this.$message({
                                    type: 'success',
                                    message: '已发送请求 '
                                });
                                
                            }
                        }).catch((err)=>{
                            console.log(err);
                        });*/
                        
                    
                    
            },
            handlerequest(t,name){
                
                var jwt = sessionStorage.getItem("accessToken")
                axios.post('/api/account/handleFriendRequest/',{
                        friend_name: name,
                        type:t
                    
                },{headers:{'Authorization': jwt}}).then((res)=>{
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
                  if(res.status === 200){
                        console.log("拒绝成功");
                        this.$message({
                        type: 'success',
                        message: '拒绝成功'
                    });     

                    }else if(res.status === 201){
                        console.log("加好友成功");
                        this.$message({
                        type: 'success',
                        message: '加好友成功'
                    }); 
                    }
                }).catch((err)=>{
                    console.log("err");
                });
            }
            
        }
    }
</script>
