# Be-Patient

2022年清华软件工程课程作业

## 项目启动（本地部署）

本地部署版本仓库位置

前端：./frontend/
后端：./backend/

### 前端启动

在frontend目录下windows的powershell或cmd中使用命令：

```
npm install
npm run serve
```

### 后端启动

在backend目录下windows的powershell或cmd中使用命令：

```
python manage.py runserver
```

## 项目仓库（远程部署）

拉取本仓库的deploy分支到服务器

依次配置好docker及docker-compose

再切换目录到项目目录下，使用命令`docker-compose up -d`即可将项目在服务器上部署起来。