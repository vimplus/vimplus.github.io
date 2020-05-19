---
title: 关于对CSS中BFC的理解
date: 2017-02-18 16:10:21
description: "关于对CSS中BFC的理解"
layout: post
categories: WEB-Front
tags: [CSS,BFC,margin重叠,两栏自适应布局]
comments: true
---

也许你已经掌握了HTML、CSS的基本布局技能，但是有可能还有一些难以琢磨透的专业名词还不是很清楚，比如BFC。今天我们就来聊聊对BFC的理解，以便我们在布局的过程中能够更加得心应手。

## 概念

BFC(Block Formatting Context)，**块级格式化上下文**，一个创建了新的BFC的盒子是独立布局的，盒子里面的子元素的样式不会影响到外面的元素。

BFC是Web页面中**盒模型**布局的一种CSS渲染模式。它的定位体系属于 **常规文档流**。

W3C规范定义：

> 浮动元素和绝对定位元素，非块级盒子的块级容器（例如 inline-blocks, table-cells, 和 table-captions），以及overflow值不为“visiable”的块级盒子，都会为他们的内容创建新的BFC（块级格式上下文）。
>
> 在BFC中，盒子从顶端开始垂直地一个接一个地排列，两个盒子之间的垂直的间隙是由他们的margin 值所决定的。在一个BFC中，两个相邻的块级盒子的垂直外边距会产生折叠。
>
> 在BFC中，每一个盒子的左外边缘（margin-left）会触碰到容器的左边缘(border-left)（对于从右到左的格式来说，则触碰到右边缘）。

## 行成要素

[W3C](https://www.w3.org/TR/CSS2/visuren.html#block-formatting)中提到：

> 一些元素，如`float`，绝对定位元素，`inline-block`, `table-cell`, `table-caption`,和`overflow`的值不为visible的元素，（除了这个值已经被传到了视口的时候）将创建一个新的块级格式化上下文。

**归纳形成BFC的几个要点：**

* `float`的值不为`none`;
* `position`的值不为`static`或者`relative`;
* `display`的值为 `table-cell`, `table-caption`, `inline-block`, `flex`, 或者 `inline-flex`中的其中一个;
* `overflow`的值不为`visible`。

详细可参考：[MDN-块格式化上下文](https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Block_formatting_context)

## 创建一个BFC

创建一个新的BFC模式，只要满足上面所述要素中的任何一个条件即可，添加相关的CSS属性。

示例：

```html
<div class="container"> Some Content here </div>
```

给容器`.container` 添加诸如：`overflow: scroll`, `overflow: hidden`, `display: flex`, `float: left`,或者 `display: table`等任何一个属性，就可以形成一个新的BFC。尽管这些条件都能形成一个BFC，但是它们各自却有着不一样的表现：

- `display: table;` —— 在响应式布局中会有问题
- `overflow: scroll;` —— 可能会出现你不想要的滚动条
- `float: left;` —— 使元素左浮动，并且其他元素对其环绕
- `overflow: hidden;` —— 隐藏溢出部分

总的说来，建立BFC最好的方式也许就是`overflow:hidden`了，如下：

```css
.container {
  overflow: hidden;
}
```

## 特点

* 在同一个 BFC 中的两个毗邻的块级盒在垂直方向（和布局方向有关系）的 margin 会发生折叠。
* 所有属于BFC中的Box都`默认左对齐`，并且它们的左边距可以触及到容器`container的左边`。最后一个Box，尽管它是浮动的，但它依然遵循这个原则。

## 用途

说了这么多规则与概念，那么我们运用BFC能做些什么呢？

### 消除外边距合并

根据BFC布局规则第二条：

> Box垂直方向之间的距离由margin决定，属于同一个BFC的两个相邻Box的margin会发生重叠。

由此规则体现为：相邻的两个盒子（可能是兄弟关系也可能是祖先关系）的外边距可以结合成一个单独的外边距。这种合并外边距的方式被称为**重叠**，并且因而所结合成的外边距称为**重叠外边距**。

**产生折叠的必备条件：margin必须是邻接的!**

#### 折叠的结果

* 两个相邻的外边距都是正数时，折叠结果是它们两者之间较大的值。
* 两个相邻的外边距都是负数时，折叠结果是两者绝对值的较大值。
* 两个外边距一正一负时，折叠结果是两者的相加的和。

示例：

```html
<style>
  .wrap {
    width:330px;
    background: #08c;
    overflow: hidden;
  }
  .item {
    width: 300px;
    height: 50px;
    margin: 15px;
    line-height: 50px;
    text-align: center;
    color: #fff;
    background: #6c0;
  }
</style>
<div class="wrap">
  <div class="item">aaa</div>
  <div class="item">bbb</div>
  <div class="item">ccc</div>
</div>
```

如图所示：

![margin-collapse-01](https://thinktxt.static.lxyour.com/article/margin-collapse-01.jpg)

item元素垂直方向之间的margin值合并了，原本应该是30px，目前只有15px。

#### 解决方案

建立新的BFC元素包裹起来：

```html
<div class="wrap">
  <div class="item">aaa</div>
  <div class="item">bbb</div>
  <div class="new-BFC">
    <div class="item">ccc</div>
  </div>
</div>
```

添加CSS属性：

```css
.new-BFC {
  overflow: hidden;
}
```

这样被新BFC元素隔离出来的item就不受外部影响了，离第二个盒子之间的垂直margin距离达到30px，如图：

![margin-collapse-02](https://thinktxt.static.lxyour.com/article/margin-collapse-02.jpg)

但是个人觉得没必要这么做，其实一般情况下设置单方向的margin值就好了，比如给item都设置`margin-top:30px;`, 如果觉得第一个元素顶部边距太多可以单独添加`.item:first-child {margin-top:15px;}`，如果大家还有更好的见解也可以提出来讨论。

### 容纳内部浮动元素

根据BFC布局规则第六条：

> 计算BFC的高度时，浮动元素也参与计算

由BFC的独立区域特性体现，BFC内部的元素不会影响到外部元素。

示例：

```html
<style>
  .content {
    width:360px;
    padding: 10px;
    background: #08c;
  }
  .child {
    float: left;
    width: 150px;
    height: 50px;
    margin: 0 15px;
    line-height: 50px;
    text-align: center;
    color: #fff;
    background: #6c0;
  }
</style>
<div class="content">
  <div class="child">child 01</div>
  <div class="child">child 02</div>
</div>
```

由于子元素浮动导致的父元素高度塌陷，如图：

![float-01](https://thinktxt.static.lxyour.com/article/float-01.jpg)

#### 解决方案

清除浮动的方法有很多，更多方法可参考：[你必须懂得的CSS清除浮动方法，4种清除浮动方法](https://www.thinktxt.com/web-front/2017/02/08/css-clear-float.html)

这里我们可以根据W3C的规则触发父元素`content`形成BFC，让内部的浮动元素也参与计算，给父元素添加：

```css
.content {
    overflow: hidden;
}
```

如图，父级高度由子元素撑开了：

![float-02](https://thinktxt.static.lxyour.com/article/float-02.jpg)

### 自适应两栏布局

BFC布局规则第三条与第四条：

> * 每个元素的margin box的左边， 与包含块border box的左边相接触(对于从左往右的格式化，否则相反)，即使存在浮动也是如此。
> * BFC的区域不会与float box重叠。

了解以上规则后，我们可以利用BFC来实现自适应两栏布局。

示例代码：

```html
<style>
  .wrap {
    width:300px;
    background: #08c;
  }
  .side {
    float: left;
    width: 120px;
    height: 200px;
    background: #6c0;
  }
  .main {
    height: 300px;
    background: #66c;
  }
</style>
<div class="wrap">
  <div class="side"></div>
  <div class="main"></div>
</div>
```

根据BFC规则第三条体现为：紫色的`main`元素以及绿色的 **浮动** 元素`side`都会紧贴 **wrap的左边** border（由于浮动元素脱离文档流会盖在紫色盒子上面），如图：

![column-layout-01](https://thinktxt.static.lxyour.com/article/column-layout-01.jpg)

根据BFC布局规则第四条，我们可以采用给main添加`overflow: hidden;`来触发新的BFC，这样新的BFC元素不会与浮动的side重叠。

```css
.main {
    overflow: hidden;
}
```

因此会根据父级元素的宽度以及side的宽度，自动变窄，形成侧栏固定，主体自适应宽度布局。如图所示：

![column-layout-02](https://thinktxt.static.lxyour.com/article/column-layout-02.jpg)

#### 利用BFC阻止文本环绕

我们经常见到的“左图+右文本”的布局方式，根据以上原理我们也可以利用BFC来解决文字环绕的问题，让文字隔离图片并自适应排版。

如下结构：

```html
<style>
  .content {
    width:300px;
    background: #08c;
  }
  .img {
    float: left;
    width: 100px;
    height: 80px;
    background: #fd0;
  }
  .info {
    background: #f66;
  }
</style>
<div class="content">
  <div class="img"></div>
  <p class="info">一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息一些信息</p>
</div>
```

如图所示：

![image-text-01](https://thinktxt.static.lxyour.com/article/image-text-01.jpg)

有时候我们不想要上面的展示，而是下面的效果：

![image-text-02](https://thinktxt.static.lxyour.com/article/image-text-02.jpg)

那么根据上面所了解的知识，我们可以触发p元素的BFC来形成新的BFC独有区域，不与浮动的图片元素重叠，因此给`.info`添加能触发BFC模式的CSS属性属性即可，这里采用`overflow:hidden;`，你也可以试试别的能够触发BFC的属性：

```css
.info {
  overflow: hidden;
  background: #f66;
}
```

## 总结

根据上面几个例子印证了BFC布局规则第五条：

> BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素。反之也如此。

因此我们可以利用这些特性来优化我们的margin、float元素、自适应布局等布局，希望今后在布局的过程中我们能够写出更加优雅的代码，深入地理解每一块布局结构原理。

## 拓展阅读

* [前端精选文摘：BFC 神奇背后的原理【推荐】](https://www.w3ctech.com/topic/865)
* [理解CSS中的BFC](https://www.w3cplus.com/css/understanding-block-formatting-contexts-in-css.html)
* [深入理解BFC和Margin Collapse](https://www.w3cplus.com/css/understanding-bfc-and-margin-collapse.html)
* [理解CSS中的BFC(块级可视化上下文)](http://www.jianshu.com/p/fc1d61dace7b)
* [CSS深入理解流体特性和BFC特性下多栏自适应布局](http://www.zhangxinxu.com/wordpress/2015/02/css-deep-understand-flow-bfc-column-two-auto-layout/)
