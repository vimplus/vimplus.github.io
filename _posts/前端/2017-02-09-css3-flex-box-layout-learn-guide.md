---
title: CSS弹性盒子之Flex布局学习指南
date: 2017-02-09 23:23:21
description: "CSS弹性盒子之Flex布局学习指南"
layout: post
categories: WEB-Front
tags: [CSS,CSS3,Flex,弹性盒子,弹性布局]
comments: true
---
弹性盒子(Flexible Box 或 Flexbox)，是CSS3中一种新的布局方式，当页面需要适应不同的屏幕大小以及设备类型时，它依然能确保元素拥有更恰当的页面布局形式。

## 什么是Flex？
Flex是Flexible Box的简称，意为"弹性盒子"，用来为盒状模型提供布局上最大的灵活性。

注意：Flex布局比较适合Web应用程序的一些小组件和小规模的布局，而Grid布局更适合用于一些大规模的布局。

## 简单使用
任何一个盒子模型都可以设定为Flex布局方式，为要使用弹性布局的元素CSS样式设置`display`属性，例如：

```css
.flex-box {
  display: flex;
}
```

或者，行内元素的也可以设置Flex布局：

```css
.flex-box {
  display: inline-flex;
}
```

Webkit内核的浏览器，必须加上`-webkit`前缀：

```css
.flex-box {
  display: -webkit-flex; /* Safari */
  display: flex;
}
```

## 构成

Flex布局方式由 **Flex容器** 和 **Flex项目** 构成：

* Flex容器 - 我们简称为“容器”，类似于`父元素`
* Flex项目 - 我们简称为“项目”，类似于`子元素`

**注意**：当采用Flex布局时，也就是包含项目的父元素`display`属性设为`flex`后：

* CSS的`columns`属性Flex容器上无效；
* Flex项目的`float`、`clear`和`vertical-align`属性将失效。

Flex盒子结构示意图：

![flex-box](https://s2.ax1x.com/2019/08/20/mGucRK.jpg)

容器默认存在两根轴：水平的主轴（main axis）和垂直的交叉轴（cross axis）。主轴的开始位置（与边框的交叉点）叫做`main start`，结束位置叫做`main end`；交叉轴的开始位置叫做`cross start`，结束位置叫做`cross end`。

项目默认沿主轴排列。单个项目占据的主轴空间叫做`main size`，占据的交叉轴空间叫做`cross size`。

## 属性

当我们采用flex布局时，盒子模型之间自然会有容器与项目的结构关系，容器和项目都有属于自己的一些属性。

### 容器的属性

容器可以设置以下6个属性：

> * `flex-flow` - 作为`flex-direction`和`flex-wrap`属性的简写形式，默认`flex-flow: row nowrap;`
> * `flex-direction` - 定义项目的排列方向；
> * `flex-wrap` - 定义项目的换行方式，如强制换行，默认不换行；
> * `justify-content` -  定义子元素的对齐方式；
> * `align-items` - 定义项目在主轴上的对齐方式；
> * `align-content` - 定义多根轴线的对齐方式，在只有一根主轴的情况下不起作用；

```css
.flex-box {
  flex-flow: <‘flex-direction’> || <‘flex-wrap’>
  flex-direction: row | row-reverse | column | column-reverse;
  flex-wrap: nowrap | wrap | wrap-reverse;
  justify-content: flex-start | flex-end | center | space-between | space-around;
  align-items: flex-start | flex-end | center | baseline | stretch;
  align-content: flex-start | flex-end | center | space-between | space-around | stretch;
}
```



####  flex-direction

`flex-direction`属性用来定义主轴的方向（即项目的排列方向）。

Flex是一种单方向的布局概念，认为Flex项目主要排列方式要么是水平排列，要么是垂直列排列。

```css
.flex-box {
  flex-direction: row | row-reverse | column | column-reverse;
}
```

![flex-direction](https://s2.ax1x.com/2019/08/20/mGJ1Z8.jpg)

包含以下4个值：

- `row`（默认值）：主轴为水平方向，起点在左端。
- `row-reverse`：主轴为水平方向，起点在右端。
- `column`：主轴为垂直方向，起点在上沿。
- `column-reverse`：主轴为垂直方向，起点在下沿。

#### flex-wrap

默认情况下，项目都是尽可能的单行显示，排列在一条“轴线”上，由`flex-wrap`属性控制如何换行。

![flow-wrap_20170209](https://s2.ax1x.com/2019/08/20/mGJnxI.jpg)

该属性包含3个值：

* `nowrap`（默认）：不换行。如图：

  ![flow-wrap_ nowrap](https://s2.ax1x.com/2019/08/20/mGJKMt.jpg)


* `wrap`：换行，第一行在上方。如图：

  ![flow-wrap_wrap](https://s2.ax1x.com/2019/08/20/mGJMsP.jpg)

* `wrap-reverse`：换行，第一行在下方。如图：

  ![flow-wrap_wrap-reverse](https://s2.ax1x.com/2019/08/20/mGJQqf.jpg)

#### justify-content

`justify-content`属性定义了项目在主轴上的对齐方式，

该属性包含5个值，具体的对齐方式与轴的方向有关，下面假设主轴为从左到右：

- `flex-start`（默认值）：左对齐
- `flex-end`：右对齐
- `center`： 居中对齐
- `space-between`：两端对齐，项目之间的间隔都相等。
- `space-around`：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。

图形示例：

![flex-justify-content](https://s2.ax1x.com/2019/08/20/mGJ3dS.jpg)

#### align-items

`align-items`属性定义项目在交叉轴上如何对齐。

该属性包含5个值，具体的对齐方式与交叉轴的方向有关。下面假设交叉轴从上到下：

- `flex-start`：交叉轴的起点对齐。
- `flex-end`：交叉轴的终点对齐。
- `center`：交叉轴的中点对齐。
- `baseline`: 项目的第一行文字的基线对齐。
- `stretch`（默认值）：如果项目未设置高度或设为auto，将占满整个容器的高度。

图形示例：

![flex-align-items](https://s2.ax1x.com/2019/08/20/mGJ8Ig.jpg)

#### align-content

`align-content`属性定义了多根轴线的对齐方式，该属性在只有一行的容器上不起作用。

与`justify-content`属性类似，可以理解为`align-content`是针对轴线之间的对齐方式。

该属性包含6个值：

- `flex-start`：与交叉轴的起点对齐。
- `flex-end`：与交叉轴的终点对齐。
- `center`：与交叉轴的中点对齐。
- `space-between`：与交叉轴两端对齐，轴线之间的间隔平均分布。
- `space-around`：每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍。
- `stretch`（默认值）：轴线占满整个交叉轴。

图形示例：

![flex-align-content](https://s2.ax1x.com/2019/08/20/mGJJiQ.jpg)

### 项目的属性

项目包含以下6个属性：

> - `flex` - 对`flex-grow`，`flex-shrink`和`flex-basis`三个属性的缩写，默认`flex:0 1 auto;`
> - `order` - 定义项目的排列顺序（项目的优先级），数值越小，越靠前，默认0;
> - `flex-grow` - 定义项目的放大比例（默认0，始终不放大）;
> - `flex-shrink` - 定义项目的缩小比例，（默认为1，空间不足将缩小）;
> - `flex-basis` - 定义项目在分配容器剩余空间之前的默认尺寸，默认`auto;`
> - `align-self` - 单独项目上的对齐方式，默认与其父级容器的align-items属性相同；

```css
.flex-item {
  flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ];
  order: <integer>;
  flex-grow: <number>; /* default 0 */
  flex-shrink: <number>; /* default 1 */
  flex-basis: <length> | auto; /* default auto */
  align-self: auto | flex-start | flex-end | center | baseline | stretch;
}
```

#### order

默认情况下，Flex项目是按照文档流的顺序排列，`order`属性可以改变项目的排列顺序，数值越小，排列越靠前，默认为0，可以为负数，相同的数值按照文档流排序。

示例（代码只留出了关键属性，后同）：

```css
.flex-box {
  display: flex;
}
.flex-item {
  flex-shrink: 0;
}
.flex-item:nth-child(2) {
  order: 2;
}
.flex-item:nth-child(3) {
  order: 3;
}
```

```html
<div class="flex-box">
  <div class="flex-item"><span>1</span></div>
  <div class="flex-item"><span>2</span></div>
  <div class="flex-item"><span>3</span></div>
  <div class="flex-item"><span>1</span></div>
  <div class="flex-item"><span>1</span></div>
</div>
```

效果如图所示：

![flex-order](https://s2.ax1x.com/2019/08/20/mGJYGj.jpg)

#### flex-grow

`flex-grow`可以定义一个Flex项目的放大比例（默认为`0`，即使父级有剩余空间也不放大），值为非负数。

如果所有Flex项目的`flex-grow`设置为`1`时，表示Flex容器中的Flex项目具有相等的尺寸，如：

```css
.flex-item {
  flex-grow: 1;
}
```

```html
<div class="flex-box">
  <div class="flex-item"><span>1</span></div>
  <div class="flex-item"><span>1</span></div>
  <div class="flex-item"><span>1</span></div>
</div>
```

效果：

![flex-grow](https://s2.ax1x.com/2019/08/20/mGJtRs.jpg)

如果给其中一个Flex项目设置`flex-grow`的值为`2`，其他都为`1`，那么这个Flex项目 **占据的剩余空间** 将是其他Flex项目2倍，如下：

```css
.flex-item {
  flex-grow: 1;
}

.flex-item:nth-child(2) {
  flex-grow: 2;
}
```

![flex-grow_02](https://s2.ax1x.com/2019/08/20/mGJNzn.jpg)

#### flex-shrink

`flex-shrink`可以定义Flex项目的缩小比例（默认为`1`，即如果空间不足，该项目将缩小），值为非负数。



默认情况下，所有项目的`flex-shrink`属性都为1，当空间不足时，都将等比例缩小，如图：

![flex-shrink_01](https://s2.ax1x.com/2019/08/20/mGJaMq.jpg)

如果一个项目的`flex-shrink`属性为0，其他项目都为1，则空间不足时，值为0的项目不缩小，如：

```css
.flex-box {
  display: flex;
  width: 600px;
}

.flex-item {
  width: 100px;
}

.flex-item:nth-child(3) {
  flex-shrink: 0;
}
```

效果图：

![flex-shrink_02](https://s2.ax1x.com/2019/08/20/mGJds0.jpg)

#### flex-basis

`flex-basis`属性定义了Flex项目在分配Flex容器剩余空间之前的一个默认尺寸（设定项目的初始尺寸），可以像`width`和`height`属性一样设定固定的尺寸，如`200px`，该属性会覆盖自身的`width`属性。

如果设置为`0`，则不会分配给该项目剩余空间。如果设置为`auto`，额外空间会基于`flex-grow`值做分布。

示例一：

```css
.flex-item:nth-child(3) {
  flex-basis: 0;
}
```

效果图：

![flex-basis_01](https://s2.ax1x.com/2019/08/20/mGJwLV.jpg)

示例二：

```css
.flex-item {
  width: 100px;
}

.flex-item:nth-child(3) {
  flex-basis: 300px;
}
```

效果图：

![flex-basis_02](https://s2.ax1x.com/2019/08/20/mGJBZT.jpg)

#### align-self

我们可以利用`align-self`对某个单独的Flex项目上定义独有的对齐方式。（对于其他未定义`align-self`属性的Flex项目，`align-self`的值永远与其关联的Flex容器的`align-items`的值相同，）

该属性包含6个值，除了`auto`，其他都与Flex容器的`align-items`属性完全一致。

默认值为`auto`，表示继承父元素的`align-items`属性，如果没有父元素，则等同于`stretch`。

示例：

![flex-align-self](https://s2.ax1x.com/2019/08/20/mGJDdU.jpg)

## 浏览器兼容前缀

```css
.flex-box {
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
}
```

## 拓展阅读

[一个完整的Flexbox指南](https://www.w3cplus.com/css3/a-guide-to-flexbox-new.html)
