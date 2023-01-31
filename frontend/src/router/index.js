import Vue from "vue";
import VueRouter from "vue-router";
import Forum from "../components/Forum.vue";
import Register from "../components/Register.vue";
import HomePage from "../components/HomePage.vue";
import Article from "../components/Article.vue";
import NoLogIn from "../components/NoLogIn.vue";
import Writer from "../components/Writer.vue";
import Chat   from "../components/Chat.vue";
import PersonalHomePage from "@/components/PersonalHomePage";
import EditInfo from "@/components/EditInfo";
import HealthAid from "@/components/HealthAid";
import Layout from "@/components/Layout/Layout.vue";
import Search from "@/components/Search.vue";
import About from "@/components/About.vue";
import Checklist from "@/components/Checklist.vue";
import HealthReports from "@/components/HealthReports";
import Reminder from "@/components/Reminder";
import axios from "axios";
import Message from "element-ui/packages/message/src/main";

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/Forum",
    name: "Forum",
    component: Forum,
  },
  {
    path: "/Register",
    name: "Register",
    component: Register,
  },
  {
    path: "/view",
    name: "Article",
    component: Article,
  },
  {
    path: "/NoLogIn",
    name: "NoLogIn",
    component: NoLogIn,
  },
  {
    path: "/Writer",
    name: "Writer",
    component: Writer,
  },
  {
    path: "/Chat",
    name: "Chat",
    component: Chat,
  },
  {
    path: "/PersonalHomePage",
    name: "PersonalHomePage",
    component: PersonalHomePage,
  },
  {
    path: "/EditInfo",
    name: "EditInfo",
    component: EditInfo,
  },
  {
    path: "/HealthAid",
    name: "HealthAid",
    component: HealthAid,
  },
  {
    path: "/Layout",
    name: "Layout",
    component: Layout,
  },
  {
    path: "/SearchInfo",
    name: "Search",
    component: Search,
  },
  {
    path: "/About",
    name: "About",
    component: About,
  },
    {
    path: "/Checklist",
    name: "Checklist",
    component: Checklist,
  },
  {
    path: "/HealthReports",
    name: "HealthReports",
    component: HealthReports,
  },
  {
    path: "/Reminder",
    name: "Reminder",
    component: Reminder,
  },
  // {
  //   path: "/about",
  //   name: "about",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;