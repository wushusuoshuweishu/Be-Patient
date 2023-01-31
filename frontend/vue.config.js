const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false,
  configureWebpack: {
    resolve: {
      alias: {
        'domain':false,
      },
      fallback: {
        //其他的如果不启用可以用 keyname :false，例如：crypto:false, 
        'domain':false,
      },
    },
  },
  devServer: {
    port: 8080,
    proxy:{
      '/api':{
        target:"/api",
        changeOrigin:true,
        pathRewrite:{
          '^/api':''
        },
      }
    }
  }
});
