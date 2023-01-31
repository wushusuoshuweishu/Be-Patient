<template>
  <div>
    <el-container>
        <el-container class="aside">
          <el-aside>
            <h2 class="me-articles-title">检查单管理</h2>
            <el-tabs v-model="activeName">
              <el-tab-pane class="lists" label="查看检查单" name="first">
                <ChecklistItem v-for="checklist in checklists" v-bind='checklist' :key="checklist"></ChecklistItem>
              </el-tab-pane>
              <el-tab-pane label="上传检查单" name="second">
                <el-form ref="form" :model="form" style="margin:1vw">
                  <el-form-item label="检查单名">
                    <el-input v-model="form.remark"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-upload
                        class="upload-demo"
                        drag
                        multiple
                        action="#"
                        :on-change="onChange"
                        :auto-upload="false"
                      >
                      <i class="el-icon-upload"></i>
                      <div class="el-upload__text" style="margin:2vw">将图片拖到此处，或<em>点击上传</em></div>
                    </el-upload>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                  </el-form-item>
                </el-form>
              </el-tab-pane>
              <el-tab-pane label="隐私条款" name="third">
              </el-tab-pane>
            </el-tabs>
          </el-aside>
          <el-main class="me-articles">
            <h2 class="me-articles-title">健康日志</h2>
            <el-form class="journal" ref="form2" :model="form2" label-width="80px">
            <el-form-item label="标题">
              <el-input v-model="form2.title"></el-input>
            </el-form-item>
            <el-form-item label="概要">
              <el-input v-model="form2.summary"></el-input>
            </el-form-item>
            <el-form-item label="指标">
              <list>
                <el-form-item label="血压(高压)">
                  <el-input v-model="form2.xueyahigh" class="tags_input" placeholder="单位：(mmHg)"></el-input></el-form-item>
                <el-form-item label="血压(低压)">
                  <el-input v-model="form2.xueyalow" class="tags_input" placeholder="单位：(mmHg)"></el-input></el-form-item>
                <el-form-item label="血糖">
                  <el-input v-model="form2.xuetang" class="tags_input" placeholder="单位：(mmol/L)"></el-input></el-form-item>
                <el-form-item label="血脂">
                  <el-input v-model="form2.xuezhi" class="tags_input" placeholder="单位：(mmol/L)"></el-input></el-form-item>
              </list>
            </el-form-item>
            <el-form-item label="正文">
              <el-input type="textarea" v-model="form2.content"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit2">提交</el-button>
            </el-form-item>
          </el-form>
          </el-main>
        </el-container>
    </el-container>
  </div>
</template>

<script>
import ChecklistItem from "@/components/ChecklistItem.vue"
import axios from "axios"

export default {
  created() {
    var jwt = sessionStorage.getItem("accessToken")
    axios.get('/api/checklist/getChecklist/', {
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
      this.checklists = res.data['checklist']
    })
    .catch((err) => {
      console.error(err);
    });
  },
  components:{
      ChecklistItem
    },
    methods:{
      onChange(file, fileList){
      var This = this;
      //this.imageUrl = URL.createObjectURL(file.raw);
      var reader = new FileReader();
      reader.readAsDataURL(file.raw);
      reader.onload = function(e){
          This.form['checklist'] = this.result;
          console.log('----------upload-photo------------');
          console.log(This.form['checklist']);
      }
    },
      onSubmit2(){
        var jwt = sessionStorage.getItem("accessToken")
      axios.post('/api/healthAid/uploadHealthAid/',{
          title:this.form2['title'],
          abstract:this.form2['summary'],
          diya:this.form2['xueyalow'],
          gaoya:this.form2['xueyahigh'],
          xuetang:this.form2['xuetang'],
          xuezhi:this.form2['xuezhi'],
          content:this.form2['content']
      },
          {
            headers:{'Authorization': jwt}
          }
    )
    .then((res)=>{//接口
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
      this.$router.push({ path: '/PersonalHomePage' })
    })
    .catch((err)=>{
      console.error(err);
      this.showReminder = true;
    });
      },
      onSubmit(){//上传健康日志
        var jwt = sessionStorage.getItem("accessToken")
      axios.post('/api/checklist/uploadChecklist/',{
          checklist:this.form['checklist'],
          remark:this.form['remark']
      },
          {
            headers:{'Authorization': jwt}
          }
    )
    .then((res)=>{//接口
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
          this.$router.go(0);
        }
    })
    .catch((err)=>{
      console.error(err);
      this.showReminder = true;
    });
      },
    },
    data(){
      return {
        activeIndex: '3',
        activeName: "second",
      form: {
          remark:'',
          checklist:''
      },
        checklists:[
          {remark:"加载中..."},
        ],
        form2:
      {
          title:'',
          summary:'',
          xueyahigh:'',
          xueyalow:'',
          xuetang:'',
          xuezhi:'',
          content:''
      }
    }
  }
}

</script>

<style scoped>
::-webkit-scrollbar {
  width: 0 !important;
  height: 0 !important;
}
.el-container {
  height: 80vh;
  overflow: scroll;
}

.el-main {
  padding: 0px;
  line-height: 2vw;
  margin-top: 5vh;
  margin-right: 2vw;
}

.person_info{
  height: max-content;
}

.el-card{
  borde-radius: 0;
  margin-top: 5vh;
}

.el-tabs
{
  text-align: center;
  background-color: white;
  margin: 0;
  padding: 0;
  height: 65vh;
}

.el-aside {
  margin-left: 2vw;
  margin-top: 5vh;
  width: 30vw !important;
}

.detailed_info{
  text-align: center;
  line-height: 2vh;
}

.open_health_aid{
  text-align: center;
  margin-top: 2vh;
}

/deep/ .el-upload {
  margin: 0;
  padding: 0;
}

/deep/ .el-upload-dragger {
  margin: 0;
  padding: 0;
  width: 100%;
}

>>> .el-tabs__nav {
  margin: 1vw;
  padding: 0;
}
</style>