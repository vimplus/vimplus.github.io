---
title: 1分钟学会搭建github-Pages
date: 2017-01-18 15:12:23
description: "github搭建博客站点"
layout: post
categories: github
tags: [github, blog]
comments: true
---
github-Pages提供一个用来搭建静态网站的服务，一般可用于自己的博客。

## 一、起步
> 创建一个git仓库：[Create a new repository][1]

仓库名为：`username.github.io`，`username` : 为你的github用户名。

如图：

![github-pages-demo][2]

> **一定记得把`username`改成你的github用户名!**

比如我的用户名是`vimplus`，同理仓库名就是`vimplus.github.io`。
然后点击`Create repository`完成仓库创建。

## 二、上手
将刚刚创建的仓库`git clone`到你的本地，例如我的：

```shell
$ git clone https://github.com/vimplus/vimplus.github.io.git
```

使用编辑器添加一个`index.html`，内容为：

```html
<!DOCTYPE html>
<html lang="zh-cmn-Hans">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
    <div>Hello, World！</div>
</body>
</html>
```

保存完了之后推送到你的git仓库，在地址栏输入：`https://vimplus.github.io`，搞定！

## 拓展阅读
[github-Pages官网][3]


  [1]: https://github.com/new
  [2]: https://thinktxt.static.lxyour.com/images/article/github_pages_create_20170120.png
  [3]: https://pages.github.com/
