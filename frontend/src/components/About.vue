<template>
    <el-container id="aboutInformation" direction="vertical" style="background-color: #fff">
        <div id="background">
        </div>
        <el-avatar id="aboutAvatar" :src="wqj"
        />
        <el-descriptions class="margin-top" :column="3" border>
            <template slot="extra">
            <!-- 
            <el-button type="primary" size="small">操作</el-button>
            -->
            </template>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-user"></i>
                邮箱
            </template>
            wangqj20@mails.tsinghua.edu.cn
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-mobile-phone"></i>
                手机号
            </template>
            18970048533
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-location-outline"></i>
                所在地
            </template>
            江西省南昌市
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-tickets"></i>
                工作
            </template>
            学生
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-office-building"></i>
                联系地址
            </template>
            江西省南昌市东湖区
            </el-descriptions-item>
        </el-descriptions>

        <el-avatar id="aboutAvatar"
            :src="hm"
        />
        <el-descriptions class="margin-top" :column="3" border>
            <template slot="extra">
            <!-- 
            <el-button type="primary" size="small">操作</el-button>
            -->
            </template>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-user"></i>
                邮箱
            </template>
            plgydamumu@foxmail.com
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-mobile-phone"></i>
                手机号
            </template>
            13685569120
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-location-outline"></i>
                所在地
            </template>
            安徽省安庆市
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-tickets"></i>
                工作
            </template>
            学生
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-office-building"></i>
                联系地址
            </template>
            安徽省安庆市潜山县源潭中学
            </el-descriptions-item>
        </el-descriptions>

        <el-avatar id="aboutAvatar"
            :src="djk"
        />
        <el-descriptions class="margin-top" :column="3" border>
            <template slot="extra">
            <!-- 
            <el-button type="primary" size="small">操作</el-button>
            -->
            </template>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-user"></i>
                邮箱
            </template>
            djk1160708111@gmail.com
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-mobile-phone"></i>
                手机号
            </template>
            13767548041
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-location-outline"></i>
                所在地
            </template>
            江西省宜春市
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-tickets"></i>
                工作
            </template>
            学生
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-office-building"></i>
                联系地址
            </template>
            江西省宜春市袁州区
            </el-descriptions-item>
        </el-descriptions>

        <el-avatar id="aboutAvatar"
            :src="wjj"
        />
        <el-descriptions class="margin-top" :column="3" border>
            <template slot="extra">
            <!-- 
            <el-button type="primary" size="small">操作</el-button>
            -->
            </template>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-user"></i>
                邮箱
            </template>
            wu-jj20@mails.tsinghua.edu.cn
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-mobile-phone"></i>
                手机号
            </template>
            18513727255
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-location-outline"></i>
                所在地
            </template>
            福建省漳州市
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-tickets"></i>
                工作
            </template>
            学生
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-office-building"></i>
                联系地址
            </template>
            福建省漳州市南靖县
            </el-descriptions-item>
        </el-descriptions>
        <el-timeline id="timeline">
            <el-timeline-item center timestamp="2022/9/23" placement="top">
            <el-card>
                <h4>Innitial Commit</h4>
                <p>项目创建</p>
            </el-card>
            </el-timeline-item>
            <el-timeline-item timestamp="2022/12/21" placement="top">
            <el-card>
                <h4>Finish</h4>
                <p>项目迭代完成</p>
            </el-card>
            </el-timeline-item>
            <el-timeline-item center>
            </el-timeline-item>
        </el-timeline>
    </el-container>
</template>

<script>
import wqj from "../assets/aboutAvatars/wqj.jpg"
import hm  from "../assets/aboutAvatars/hm.jpg"
import djk from "../assets/aboutAvatars/djk.jpg"
import wjj from "../assets/aboutAvatars/wjj.jpg"


export default {
    name: "About",
    data() {
        return {
            wqj: wqj,
            hm: hm,
            djk: djk,
            wjj: wjj
        }
    }
}
</script>

<style>
.el-descriptions {
    margin-bottom: 2vw;
    margin-top: 2vh;
    margin-left: 10vw;
    margin-right: 10vw;
    z-index: 2;
}

#aboutInformation {
    height: 100%;
    width: 100%;
    position: relative;
    /* opacity: 0.75; */
}

#background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("../assets/backgrounds/AboutBackground.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.75;
    z-index: 1;
}

#aboutAvatar {
    border-radius: 50%;
    margin: 0;
    margin-left: 10vw;
    margin-top: 5vh;
    z-index: 2;
}

#timeline {
    margin-left: 10vw;
    margin-right: 10vw;
    margin-top: 10vh;
    height:30vh;
    z-index: 2;
}

.el-timeline-item__timestamp {
    color: #fff !important;
    font-size: 1.5vw !important;
}

.el-timeline-item__node{
    background-color: #128811 !important;
}

.el-timeline-item__tail{
    background-color: #ccff11 !important;
}
</style>