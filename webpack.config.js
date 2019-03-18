const path = require("path");
var webpack = require("webpack");
var MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = () => {
  "use strict";
  var project_path = path.resolve(__dirname, "project");
  var resources_path = path.join(project_path, "resources");
  var output_path = path.join(project_path, "static");
  var in_production = process.env.NODE_ENV === "production";

  var baseConfig = {
    entry: {
      app: [resources_path + "/js/index.js", resources_path + "/sass/app.scss"]
    },
    output: {
      path: output_path,
      filename: "app.js"
    },
    module: {
      rules: [
        {
          test: /\.s[ac]ss$/,
          use: [
            {
              loader: MiniCssExtractPlugin.loader
            },
            "css-loader",
            "sass-loader"
          ]
        },
        {
          test: /\.(png|je?pg|gif|svg)$/,
          loader: "file-loader",
          options: {
            name: "[name].[ext]",
            outputPath: "images"
          }
        },
        {
          test: /\.js?$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
            options: {
              presets: ["@babel/preset-env"]
            }
          }
        }
      ]
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: "[name].css"
      }),
      new webpack.LoaderOptionsPlugin({
        minimize: in_production
      })
    ]
  };

  if (process.env.CLEAN) {
    var CleanWebpackPlugin = require("clean-webpack-plugin");
    baseConfig.plugins = baseConfig.plugins.concat([
      new CleanWebpackPlugin({
        path: output_path
      })
    ]);
  }

  return baseConfig;
};
