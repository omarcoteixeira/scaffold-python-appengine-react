var path = require("path");
var webpack = require("webpack");
var autoprefixer = require('autoprefixer');
var precss = require('precss');
var glob = require("glob");

module.exports = {
  entry: glob.sync("./src/app/**/*.js"), //'./src/app/main.js',
  output: {
    path: 'dist/',
    filename: '/js/bundle.js',
    publicPath: '/'
  },
  devServer: {
    inline: true,
    contentBase: './src/app',
    port: 3333
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel',
        query: {
          presets: ['es2015', 'react']
        }
      }, {
        test: /\.scss$/,
        loaders: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  },
  postcss: function () {
    return [autoprefixer, precss];
  },
  sassLoader: {
    includePaths: "./assets/stylesheets"
  }
}
