const webpack = require("webpack");

module.exports = {
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
    }
}
;
