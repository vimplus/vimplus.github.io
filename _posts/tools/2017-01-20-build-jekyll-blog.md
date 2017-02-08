---
title: 基于jekyll轻松搭建Github-Pages博客
date: 2017-01-20 15:12:21
image: https://thinktxt.static.lxyour.com/images/article/github-pages-jekyll-img.png
description: "基于jekyll轻松搭建Github-Pages博客"
layout: post
categories: jekyll
tags: [jekyll,blog]
comments: true
---
## 前言
有时候看到一些大牛的博客简洁，版式美观，一看就是markdown的风格，所以一直很想自己弄一个版式简洁，支持markdown的独立博客。

刚接触前端的时候只知道有那些WordPress这种博客系统，自己也曾经搭建过，但是觉得太复杂，要自己买服务器、备案之类的，重点是自己写的本地markdown笔记文件还不能直接任意搬迁上去，恕我井底蛙，隔了好久后来终于发现原来有一种叫做 **jekyll** 的博客系统（还有[hexo][1]、[Octopres][2]、[Ruhoh][3]，喜欢hexo的朋友也可以玩一下），于是如同发现新大陆，立马实践一把。

## 特点
* 无需数据库
* 无缝对接markdown
* 页面静态化（将markdown生成HTML）
* 支持博客相关的所有功能，如归档、标签，评论等等。

## 准备
首先看看你的系统有没有`Ruby环境`，没有的自行安装(这里主要介绍的是Mac OS X下的教程)，比如Windows用户（自从自己用了Mac编程之后再也不想用自己那台Windows笔记本了）。

身为共产主义接班人有必要先把gem源设置修改一下，我们来使用淘宝的ruby镜像源：

```
gem sources --remove https://rubygems.org/
gem sources -a https://ruby.taobao.org/
gem sources -l
```

## 安装jekyll
设置好之后执行以下命令：

```
$ gem install jekyll
```

一般情况下可能会报错(没有权限)：

```
While executing gem ... (Gem::FilePermissionError)
You don't have write permissions for the /Library/Ruby/Gems/2.0.0 directory.
```

那就使用：

```
$ sudo gem install jekyll
```

接下来执行`bundler install`，这样jekyll已经安装好了。

## 新建jekyll项目
使用以下命令快速创建一个jekyll站点的经典目录结构：

```
$ jekyll new myBlog
```

然后访问到该目录，执行：

```
$ cd myBlog
$ jekyll server
```

打开浏览器，输入：http://localhost:4000/
这样一个基本的jekyll站点就建立好了。

## 创建Github-Pages
> 首先创建一个git仓库：[Create a new repository][4]

仓库名为：`username.github.io`，`username` : 为你的github用户名。

> **一定记得把`username`改成你的github用户名!**

比如我的用户名是`vimplus`，同理仓库名就是`vimplus.github.io`。
然后点击`Create repository`完成仓库创建。

## 推送到Github
将你刚刚创建的jekyll站点代码推送到你新创建的`username.github.io`仓库。
然后访问你的github-Pages页面地址，比如我的：https://vimplus.github.io

到这里你的Github-Pages博客站点就大功告成啦！

## 博客主题
作为强迫症的我怎能容忍丑陋的博客页面，当然是找[jekyll主题][5]或者自己设计，找到喜欢的主题后下载主题代码自行替换你站点目录的代码（你可以全部替换，因为一个主题就是有基本功能的jekyll站点）。

## 最后
如果你根据我这篇并不那么详细的教程搭建出属于你自己的博客，那么恭喜你，欢迎入坑！
更多坑自行Google搜索吧。

## 拓展阅读
[1分钟学会搭建github-Pages][6]


  [1]: http://hexo.io/
  [2]: http://octopress.org/
  [3]: http://ruhoh.com/
  [4]: https://github.com/new
  [5]: http://jekyllthemes.org/
  [6]: https://vimplus.github.io/github/2017/01/18/1minutes-build-github-pages.html
