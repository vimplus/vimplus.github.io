---
title: 自定义sublime或Brackets中Emmet插件模板-Brackets使用心得
date: 2015-11-25 10:55:21
image: https://thinktxt.static.lxyour.com/images/article/thinktxt_emmet_20151125.jpg
description: "自定义sublime或Brackets中Emmet插件模板-Brackets使用心得"
layout: post
categories: Brackets
tags: [Emmet,Brackets]
comments: true
---
Emmet在开发效率上给我们带来了很多方便，Emmet中默认的H5的文档是这样的：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

</body>
</html>
```

如果我想把它根据自己的习惯定制的更加完美，那怎么办呢？
比如说head中加上：`<link rel="stylesheet" href="css/master.css">`
在body中加上：`<script src="js/main.js"></script>`
（上面两个文件一般情况下是经常性需要的）

## 起步
下面我们来一起DIY吧：
首先我们找到Emmet提供了可自定义的配置文件: `snippets.json`
以Brackets为例，该文件位置在`/user/brackets-emmet/node_modules/emmet/lib/snippets.json`。

## 准备
在这个文件中我们找到：

```
"doc": "html>(head>meta[charset=UTF-8]+title{${1:Document}})+body)"
```

默认代码显示后的效果就是上面那样。但是我们要加上上面两个文件引用，效果应该是：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="css/master.css">
</head>
<body>
    <script src="js/main.js"></script>
</body>
</html>
```

## 修改

那么语句应该改为（修改之前记得先拷贝一份，免得改错了回不来了）：

```
"doc": "html>(head>meta[charset=UTF-8]+title{${1:Document}}+link[rel=stylesheet][href=css/master.css])+(body>script[src=js/main.js])"
```

## 完成
修改完了代码重启一下你的Brackets软件试试，如你所期待的样子了吧。

## 其他
同理，我们还以改改别的，这里总结一下修改的要点：

* 添加标签直接写标签名就好了，比如`div`。
* 标签中的属性/属性值直接跟在标签后面`div[name=vimplus]`,有多个属性就放多个[],比如`div[name=vimplus][age=25]`。
* 标签中的内容用`{}`表示。

试试下面的代码：

```
"doc": "html>(head>meta[charset=UTF-8]+title{${1:Document}}+link[rel=stylesheet][href=css/master.css])+(body>div[name=vimplus][age=25]{Content Text}+script[src=js/main.js])",
```

好了，照葫芦画瓢，大家打开自己的脑洞，自己研究研究，自定义出更多方便的模板吧，快乐学习，潇洒游四方！
