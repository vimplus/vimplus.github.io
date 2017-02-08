---
title: 你必须懂得的CSS清除浮动方法，4种清除浮动方法
date: 2017-02-08 17:23:21
description: "你必须懂得的CSS清除浮动方法，4种清除浮动方法"
layout: post
categories: WEB-Front
tags: [CSS,float,清除浮动]
comments: true
---
做前端开发我们都不得不使用float浮动属性，但是如果使用了浮动，由于浮动本身的特性，难免会遇到父级元素塌陷的情况，不能自适应高度。

假设了有三个盒子对象，一个父级里包含了两个子级，父级元素没有设置固定高度，子级一个使用了float:left（左浮动）属性，另外一个子级使用float:right（右浮动）属性，这种情况的话父级元素的高度就必定不能被子内容而撑开。



## 场景

三个盒子对象：

```html
<div class="content">
    <div class="col-1">布局1</div>
    <div class="col-2">布局2</div>
    内容
</div>
```

设置了浮动之后，父级元素不能被撑开，如图：

![img20150203001-1](https://ww4.sinaimg.cn/large/006y8lVagy1fcj79wqka8j30s406aaaa.jpg)

我们所希望的效果：

![img20150203001-2](https://ww2.sinaimg.cn/large/006y8lVagy1fcj79x6iicj30sa062aaa.jpg)

这种情况在我们的工作中特别常见，我们可以通过四种方法清除浮动。

## 方法一

使用一个空标签

```html
<div class="content">
    <div class="col-1">布局1</div>
    <div class="col-2">布局2</div>
    内容
    <div class="clear"></div>
</div>
```

`clear`的 CSS样式如下：

```css
.clear {
    clear: both;
}
```

## 方法二：

给父元素设置display:inline-block属性：

```css
.content {
  display: inline-block
}
```

## 方法三

给父元素设置overflow:auto或hidden属性：

```css
.content {
    overflow: auto;  /* 设置 hidden 也可以 */
}
```



## 方法四

给父元素添加类名`clearfix`，利用css伪类（比较常用，例如bootstrap框架使用的就是这种方法）

```
.clearfix:after {content:""; display: table; clear: both;}
.clearfix {*zoom:1;}
```

HTML标签如下：

```
<div class="content clearfix"></div>
```

好啦，以上就是清除浮动的几种方法，不知道童鞋你学会了么？
