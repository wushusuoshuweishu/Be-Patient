<template>
    <div>
        <div type="success"  class="grouptype"  @click="open=!open">
            <span :class="open?'rotate':' '"></span>
            <span >{{groupname}}</span>
            <span>{{onlines}}/{{list.length}}</span>
            
            <el-button v-show="isdefault" class="delete_group" @click="removegroup" type="danger" icon="el-icon-delete" size="mini" radius></el-button>
        </div>
        
        <el-collapse-transition class="myfriend"  name="fade">
                <dev v-show="open">
                <el-card v-for="f in newList" class="zai">
                    <el-avatar  :size="size" :src="f.src"></el-avatar>
                    <h3 class="fri_name" v-text="f.username"></h3>
                    <!--<el-tag class="frisign">{{f.sign}}</el-tag>-->
                    <el-container direction="vertical" style="margin-left:70vw">
                        <el-container>
                            <el-button @click="removefriend(f.username)" class="remove_button" type="danger" icon="el-icon-remove-outline" >删除好友</el-button>
                        </el-container>
                        <el-container>

                            <el-popover
                            placement="right"
                            width="200"
                            trigger="click">
                            <el-tag v-for="(s_group, i) in group_type" :key="i" @click="change_group(f.username,s_group)">{{ s_group }}</el-tag>
                            <el-button slot="reference">移动分组</el-button>
                            </el-popover>


                                
                            
                        </el-container>
                    </el-container>
                    <Contact class="contact_button" :fri_name="f.username"></Contact>
                </el-card>
            </dev>
        </el-collapse-transition> 
    </div>
</template>



<script>
import Contact from "@/components/Contact.vue"
import axios from "axios"
export default {
    name: 'Group',
    components: { 
        Contact
    },
    props: {
        groupname: String,
        list: Array,
        group_type:Array         
    },
    data() {
      return {
        isdefault:true,
        open: false
      }
    },
    created(){
        if(this.groupname == 'default'){
            this.isdefault = false;
        }
    },
    computed:{
            onlines(){
                let count = 0
                this.list.forEach(element=>{
                    if (element.status) {
                        count++
                    }
                })
                return count
            },
            newList(){
                let arr = []
                this.list.forEach(e=>{
                    if (e.status) {
                        arr.unshift(e)
                    }else{
                        arr.push(e)
                    }
                })
                return arr
            }
        },
    methods: {   
            removefriend(f){

                //直接删除数据库里的groups【】；；
                var jwt = sessionStorage.getItem("accessToken")
                axios.post('/api/account/deleteFriend/',{
                    friend_name : f
                },{ headers:{'Authorization': jwt}})
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
                       console.log("删除好友成功");
                    }
                }).catch((err)=>{
                    console.log(err);
                });
            },
            removegroup(){
                var jwt = sessionStorage.getItem("accessToken")
                axios.post('/api/account/deleteGroup/',{
                    group_name : this.groupname
                },{ headers:{'Authorization': jwt}})
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
                        console.log("removegroup succeed");
                    }
                    else if(res.status === 500){
                        this.$message({
                            type : 'error',
                            message : '删除分组失败'
                        });
                    }
                }).catch((err)=>{
                    console.log(err);
                });
            },
            change_group(friname,groupname){
                //移动元素this
                /*
                this.groups.foreach()
                */
               console.log(friname+"修改分组get");
               console.log(groupname);

               
                var jwt = sessionStorage.getItem("accessToken")
                axios.post('/api/account/changeGroupOfFriend/',{

                        friend_name: friname,
                        group_name: groupname
                    
                },{headers:{'Authorization': jwt}})
                .then((res)=>{

                    if(res.status === 201){
                        console.log("修改分组成功");
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
                }).catch((err)=>{
                        console.log(err);
                    });
                
            }
    }
  }

</script>

<style>
.delete_group{
    position: relative;
    left: 75vw;
    -moz-border-radius: 1vmin;
    -webkit-border-radius: 1wmin;
    border-radius: 1vmin;
}
.grouptype{
    text-align: left;
    margin: 1vmin;
    padding: 1vmin;
    list-style-type :none;
    background-color: #f5f5f5;
    -moz-border-radius: 1vmin;
    -webkit-border-radius: 1wmin;
    border-radius: 1vmin;
} 

.grouptype span{
    font-size: 24px;
}

.zai{
    padding: 0;
    margin: auto;
    list-style :none;
    background-color: #f5f5f5;
    -moz-border-radius: 1vmin;
    -webkit-border-radius: 1wmin;
    border-radius: 1vmin;
}

.fri_name{
    position: relative;
    top: -1vh;
}
.frisign{
    position: relative;
    top: -3vh;
    left: 5vw;
}

.ul {
    list-style: none;
    margin: 0 !important;
    padding: 0 !important;
}

.remove_button{
    position: relative;
    width: 12vw;
    text-align: center;
}
</style>