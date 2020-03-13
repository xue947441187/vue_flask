const webpack = require("webpack");

module.exports = {
     publicPath: '/',
     devServer: {
        open: true,
        host: 'localhost',
        port: 8080,
        https: false,
        //以上的ip和端口是我们本机的;下面为需要跨域的
        proxy: {//配置跨域
            '/api': {
                target: 'http://127.0.0.1:5000',//这里后台的地址模拟的;
                ws: true,
                changOrigin: true,//允许跨域
                pathRewrite: {
                    '^/api': ''  //请求的时候使用这个api就可以
                }
            }

        }
    },
    configureWebpack: {
        plugins: [
// new webpack.optimize.CommonsChunkPlugin('common.js'),
            new webpack.ProvidePlugin({
                $: 'jquery',
                jQuery: 'jquery',
                'window.jQuery': 'jquery',
                Popper: ['popper.js', 'default']
            })
        ],
        optimization: {
            splitChunks: {
                name: "common"
            }
        }
    },
    devServer: {
        proxy: "http://127.0.0.1:5000",
        https:
            false
    },
};
