---
title: 解决iOS Safari中按钮默认属性样式问题
date: 2015-07-02 18:14:21
description: "解决ios safari中按钮默认属性样式问题"
layout: post
categories: WEB-Front
tags: [button,safari]
comments: true
---
## 问题描述

使用HTML5编写网页在移动APP中嵌套，总会涉及到按钮`<input type="button">`的使用，在android手机浏览器中显示正常，但在ios safari浏览器中会看到按钮显示为圆角等一些默认样式，设置`border-radius:0`也不好使，其实给css属性添加`-webkit-appearance`就能解决问题。

## 问题截图

![img01][1]

## 解决方案

```
<input type="button" class="code-btn"/>
.code-btn {
    display: inline-block;
    width: 75px;
    height: 30px;
    font-size: 14px;
    color: #fff;
    background: #ff7900;
    border: 0;
    border-radius: 3px;
    -webkit-appearance : none ;  /*解决iphone safari上的默认样式问题*/
}
```

## 总结
使用CSS属性`-webkit-appearance: none; `轻松解决iPhone手机中safari上的默认样式问题。


  [1]: https://thinktxt.static.lxyour.com/images/article/ios_button_hack_20170208.png
