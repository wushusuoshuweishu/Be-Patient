<template>
    <div class="common-layout">
      <div id="background"></div>
      <el-container :key="new Date().getTime()">
        <el-header v-if="showHeader" id="mainContainer">
          <PageHeader></PageHeader>
        </el-header>
        <el-container :key="new Date().getTime()">
          <el-main class="affix-container" id="mainContainer">
            <router-view></router-view>
            <el-backtop :bottom="100">
              <div
                style="
                  height: 100%;
                  width: 100%;
                  background-color: var(--el-bg-color-overlay);
                  box-shadow: var(--el-box-shadow-lighter);
                  text-align: center;
                  line-height: 200%;
                  color: #1989fa;
                "
              >
                UP
              </div>
            </el-backtop>
          </el-main>
          <el-aside v-if="showAside" id="mainContainer">
            <Sidebar></Sidebar>
          </el-aside>
        </el-container>
        <el-footer v-if="showFooter" id="mainContainer">
          <PageFooter></PageFooter>
        </el-footer>
      </el-container>
    </div>
</template>

<script>
import PageHeader from "@/components/smallComps/PageHeader.vue";
import PageFooter from "@/components/smallComps/PageFooter.vue";
import Sidebar from "@/components/smallComps/Sidebar.vue";

var title = document.title;

export default {
  name: "Layout",
  components: {
    PageHeader,
    PageFooter,
    Sidebar
  },
  data() {
    return {
      showHeader: (window.location.pathname === "/Forum" || window.location.pathname === "/view" || window.location.pathname === "/Writer" || window.location.pathname === "/Chat" || window.location.pathname === "/PersonalHomePage" || window.location.pathname === "/EditInfo" || window.location.pathname === "/HealthAid" || window.location.pathname === "/SearchInfo" || window.location.pathname === "/About" || window.location.pathname === "/Reminder"),

      showAside: window.location.pathname === "/Forum" || window.location.pathname === "/view",
      
      showFooter: window.location.pathname === "/Forum" || window.location.pathname === "/Writer" || window.location.pathname === "/Chat" || window.location.pathname === "/SearchInfo" || window.location.pathname === "/About" || window.location.pathname === "/HealthAid" || window.location.pathname === "/Reminder"
    };
  },
  watch: {
    $route: function () {
      this.showComponents();
    }
  },
  created() { 
    document.addEventListener("visibilitychange", function () {
      console.log('document.visibilityState=' + document.visibilityState);
      console.log('document.hidden=' + document.hidden, document.hidden ? '页面隐藏' : '页面显示');
      if (document.visibilityState === 'hidden') {
        document.title = '离开'
      } else {
        document.title = title
      }
    });
  },
  methods: {
    showComponents: function () {
      var tempHeader = window.location.pathname === "/Forum" || window.location.pathname === "/view" || window.location.pathname === "/Writer" || window.location.pathname === "/Chat" || window.location.pathname === "/PersonalHomePage" || window.location.pathname === "/EditInfo" || window.location.pathname === "/HealthAid" || window.location.pathname === "/SearchInfo" || window.location.pathname === "/About" || window.location.pathname === "/Reminder";
      this.showHeader = tempHeader;

      var tempAside = window.location.pathname === "/Forum" || window.location.pathname === "/view";
      this.showAside = tempAside;

      var tempFooter = window.location.pathname === "/Forum" || window.location.pathname === "/Writer" || window.location.pathname === "/Chat" || window.location.pathname === "/SearchInfo" || window.location.pathname === "/About" || window.location.pathname === "/HealthAid" || window.location.pathname === "/Reminder";
      this.showFooter = tempFooter;
      
      return {
        showHeader: tempHeader,
        showAside: tempAside,
        showFooter: tempFooter
      }
    },
  },
}
</script>

<style scoped>
.el-header{
  margin: 0;
  padding: 0;
  font-size: 1vh;
  height: 10vh;
  width: 100vw;
}
.el-footer{
  margin: 0;
  padding: 0;
  font-size: 0.8vw;
  height: 10vh;
  width: 100vw;
}
.el-aside{
  height: 100%;
}
.el-main{
  height: 190vh;
  width: 75vw !important;
}

::-webkit-scrollbar {
  width: 0 !important;
  height: 0 !important;
}

.el-main {
  padding:0 !important;
}

.common-layout{
    position: relative;
    background-color: #f5f5f5;
    overflow: auto;
    /* opacity: 0.75; */
}

#background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("../../assets/backgrounds/background.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.4;
    z-index: 1;
}

#mainContainer {
  z-index: 2;
}
</style>