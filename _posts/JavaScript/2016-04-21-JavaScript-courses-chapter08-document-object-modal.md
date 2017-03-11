---
title: JS课堂第八节 - JavaScript DOM对象
date: 2016-04-21 20:15:21
description: "JS课堂第八节 - JavaScript DOM对象"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
DOM（Document Object Model）即文档对象模型，在此模型中定义了访问和处理 HTML 文档的标准方法。我们可以将整个 document 页面看作树型结构，每一个元素都视为一个节点，每个节点都有自身属性，可以通过这些属性改变节点的内容和样式。同时，每个节点都有一系列树型结构的属性与方法，如父子、同辈节点的遍历、节点的创建、添加、删除、替换等。
本章将学习JavaScript操作DOM的相关知识。

## 认识DOM

DOM（Document Object Model）即文档对象模型，定义访问和处理 HTML 文档的标准方法。DOM 将 HTML 文档呈现为带有元素、属性和文本的树结构（节点树）。

我们可以将 HTML 代码分解为 DOM 节点层次图：
![此处输入图片的描述][1]

## DOM节点
HTML 文档可以说由节点构成的集合，三种常见的 DOM 节点:

1. 元素节点：上图中 `<html>` `<body>` `<p>` 等都是元素节点，即标签。
2. 文本节点：向用户展示的内容，如 `<li>...</li>` 中的 JavaScript、DOM、CSS 等文本。
3. 属性节点：元素属性，如 `<a>` 标签的链接属性href="http://www.lxyweb.com"。

示例：

```html
<a href="http://www.lxyweb.com">JavaScript DOM</a>
```

### 1. 节点属性

+ **nodeName** 节点名称，相当于tagName属性节点返回属性名，文本节点返回 #text。nodeName，是只读的。
+ **nodeValue** 节点的值，返回一个字符串，指示这个节点的值。元素节点返回 null，属性节点返回属性值，文本节点返回文本。nodeValue 可读可写，这是对元素节点不能写。一般只用于设置文本节点的值。
+ **nodeType** 属性：节点的类型，返回值一个整数，是只读的。以下常用的几种结点类型:

| 元素类型 | 节点类型 |
| --- |  --- |
| 元素 |  1 |
| 属性 |  2 |
| 文本 |  3 |
| 注释 |  8 |
| 文档 |  9 |

```html
<p id="ip" title="hello">JavaScript</p>
<script type="text/javascript">
    var op = document.getElementById("ip");
    document.write(op.nodeName + "<br>" + op.nodeValue + "<br>" + op.nodeType);
</script>
```

### 2. 节点方法

| 方法  |  说明 |
| ----  |  ---- |
| write() | 写入内容到文档  |
| getElementById()  |  返回带有指定 ID 的元素  |
| getElementsByTagName() | 返回带有指定标签名的所有元素  |
| getElementsByClassName() | 返回包含指定类名的所有元素的一个列表 |

一些其它的 DOM 操作控制的方法：

| 方法  |  说明 |
| ----  |  ---- |
| createElement('tagName')  | 创建节点。 |
| createTextNode('text'); | 创建文本节点。 |
| appendChild(o) | 在父节点末尾附加子节点 ，其中 o 为节点对象。 |
| createDocumentFragment()  |  创建文档片断。 |
| removeChild(oP) | 删除节点。 |
| replaceChid(newOp, targetOp)  |  替换节点。 |
| insertBefore(newOp, targetOp)  |  已有的子节点前插入一个新的子节点。 |
| insertAfter(newOp, targetOp)  |  已有的子节点之后插入一个新的子节点。 |
| get/setAttribute('key', 'value')  |  设置或得到属性节点。 |
| cloneNode(true/false)  |  复制节点。 |

这些方法的使用主体不只是 document，更多的是各个节点元素。

## 元素内容
我们有两种方法替换元素的内容，一个是 innerHTML，另一个是 innerText。

* innerHTML 属性用于获取或替换元素的内容，比如`<div>` 标签内的所有元素。`<div><a>文本内容</a></div>`
* innerText 属性用于获取或替换元素的文本内容，只有文本内容，没有其它 HTML 标签。`<div><a>文本内容</a></div>`

innerHTML 和 innerText 都是既可读又可写的

**读取使用语法**：

```javascript
Object.innerHTML
Object.innerText
```

**写入使用语法**：

```javascript
Object.innerHTML = str;
Object.innerText = str;
```

**参数说明**： Object 是获取的元素对象，如通过document.getElementById("ID")获取的元素。

```html
<p>JavaScript</p>
<p>JavaScript</p>
<input type="button" id="inp" value="click">
<script type="text/javascript">
    var inp = document.getElementById("inp");
    inp.onclick = function () {
        var ip = document.getElementsByTagName("p");
        alert(ip[0].innerHTML);
        ip[0].innerHTML = "<i>51RGB</i>";
        ip[1].innerText = "<i>LXYWEB</i>";
    }
</script>
```

## 元素样式

* style 属性
* className 属性。

style 可以直接改变元素的样式，比如宽高，颜色，背景等，而 className 只会改变元素的类（即 class），具体的样式写在了类之中。

style 的使用语法：

```javascript
Object.style.property = new style;
```

参数说明：
1. Object 是获取的元素对象，如通过`document.getElementById("id")`获取的元素。
2. property 为 css 样式属性，比如 color，width 等等，不做过多说明。

实例练习：

```html
<h2 id="textbox">JavaScript</h2>
<input type="button" id="inp" value="click">
<script type="text/javascript">
    var inp = document.getElementById("inp");
    inp.onclick = function () {
        var oh = document.getElementById("textbox");
        oh.style.color = "#f00";
        oh.style.width = "300px";
        oh.style.backgroundColor = "#08c";
    }
</script>
```

## 控制类名
className 属性可以设置或返回元素的 class 属性。
使用语法：`Object.className = classname;`
参数说明：
1. Object 是获取的元素对象，如通过`document.getElementById("id")`获取的元素。
2. className 为 元素的 class 属性。

## 操作节点

### 1. 遍历节点树

+ childNodes 返回一个数组，这个数组由给定元素节点的子节点构成
+ firstChild 返回第一个子节点
+ lastChild 返回最后一个子节点
+ parentNode 返回一个给定节点的父节点
+ nextSibling 返回给定节点的下一个子节点
+ previousSibling 返回给定节点的上一个子节点

### 2. 子节点

```html
<ul id="father">
    <li>大娃</li>
    <li>二娃</li>
    <li>三娃</li>
    <li>四娃</li>
    <li>五娃</li>
    <li>六娃</li>
    <li>七娃</li>
</ul>
<script type="text/javascript">
    var li_num = 0;
    var childNodes = document.getElementById("father").childNodes;
    for(var i = 0; i < childNodes.length; i++){
        document.write("节点名：" + childNodes[i].nodeName + " ");
        document.write("节点类型：" + childNodes[i].nodeType + " ");
        if(childNodes[i].nodeType == 1){
            document.write("我是" + childNodes[i].innerHTML + "<br>");
            li_num++;
        }
        else{
            document.write("<br>");
            console.log("这是一个空节点，不用理他");
        }
    }
    document.write("子节点数目：" + childNodes.length + "<br>");
    document.write("li 子节点数目：" + li_num + "<br>");
    document.write("文本子节点数目：" + (childNodes.length - li_num));
</script>
```

### 3. 父级节点

```html
<div id="grandfather" title="孩子救我！">
    <ul id="father">
        <li>大娃</li>
        <li id="second_children">二娃</li>
        <li>三娃</li>
        <li>四娃</li>
        <li>五娃</li>
        <li>六娃</li>
        <li>七娃</li>
    </ul>
</div>
<script type="text/javascript">
    var grandfather = document.getElementById("second_children").parentNode.parentNode;
    document.write(grandfather.id + "说：" + grandfather.title);
</script>
```

### 4. 兄弟节点
在 DOM 树形结构中，除了父子关系属性外，还有同辈关系属性。
同辈关系中，也分为两种，一种是向前的同辈关系 previousSibling，另一种是向后的同辈关系 nextSibling。

* nextSibling 属性可返回某个节点之后紧跟的节点（处于同一树层级中）。如果无此节点，则该属性返回 null。

  使用语法：`nodeObject.nextSibling`
  
* previousSibling 属性可返回某个节点之前紧跟的节点（处于同一树层级中）。如果无此节点，则该属性返回 null。

  使用语法：`nodeObject.previousSibling`
  
```html
<ul id="father">
    <li title="force_max">大娃</li>
    <li id="second_children">二娃</li>
    <li title="fire">三娃</li>
    <li>四娃</li>
    <li>五娃</li>
    <li>六娃</li>
    <li>七娃</li>
</ul>
<script type="text/javascript">
    function getprenode(node) {
        var prenode = node.previousSibling;
        while( prenode && prenode.nodeType != 1){
            prenode = prenode.previousSibling;
        }
        return prenode;
    }
    function getnextnode(node) {
        var nextnode = node.nextSibling;
        while(nextnode && nextnode.nodeType != 1){
            nextnode = nextnode.nextSibling;
        }
        return nextnode;
    }
    var second_children = document.getElementById("second_children");
    var first_children = getprenode(second_children);
    var third_children = getnextnode(second_children);
    alert(first_children.innerHTML + first_children.title);
    alert(third_children.innerHTML + third_children.title);
</script>
```

## DOM操作

常用的DOM操作方法：
| 方法  |  说明 |
| ----  |  ---- |
| createElement('tagName')  | 创建一个新的元素。 |
| createTextNode('text'); | 创建文本节点。 |
| appendChild(o) | 在父节点末尾附加子节点 ，其中 o 为节点对象。 |
| removeChild(oP) | 从一个指定元素中删除一个子节点。 |


* insertBefore 将一个节点插入到一个指定元素节点所属的子节点前面（将你手里的鸡蛋放到一个装有鸡蛋的盒子里，确定那个盒子并且放在已有鸡蛋的最前面）
* replaceChild 把一个指定父元素的一个子节点替换为另外一个节点

### 1. 创建元素
1.1 创建元素节点方法。
createElement()方法可创建元素节点。此方法可返回一个 Element 对象。

使用语法：`document.createElement(tagName);`
参数说明：tagName：字符串值，这个字符串用来指明创建元素的类型。

需要注意的是：createElement() 方法只是创建元素，并不会自动出现在文档中，如果想显示在浏览器中，还需要与appendChild() 或 insertBefore() 方法联合使用哦~

1.2 创建文本节点方法。
createTextNode() 方法创建新的文本节点，返回新创建的 Text 节点。

使用语法：`document.createTextNode(str);`
参数说明：str，字符串值，可规定此节点的文本。

实例练习：

```html
<script type="text/javascript">
    var newinp = document.createElement("input");
    alert(newinp);
    var newtext = document.createTextNode("text");
    alert(newtext);
</script>
```

1.3 添加或删除子节点

```html
<ul id="father">
    <li>大娃</li>
    <li>二娃</li>
    <li>三娃</li>
    <li>四娃</li>
    <li>五娃</li>
    <li>六娃</li>
    <li>七娃</li>
</ul>
<input type="button" id="createbtn" value="祭出紫金葫芦">
<script type="text/javascript">
    function createnode() {
        var btn = document.createElement("input");
        btn.setAttribute("type", "button");
        btn.setAttribute("name", "紫金葫芦");
        btn.setAttribute("value", "吸进去");
        btn.setAttribute("onclick", "removenode()");
        document.body.appendChild(btn);
    }
    function removenode() {
        var fnode = document.getElementById("father");
        var nodes = fnode.childNodes;
        for(var i = 0; i < nodes.length; i++){
            if(nodes[i] && nodes[i].nodeType == 1){
                var rm = fnode.removeChild(nodes[i]);
                rm = null;
                break;
            }
        }
    }
    var createbtn = document.getElementById("createbtn");
    createbtn.onclick = createnode;
</script>
```

### 2. 插入指定位置子节点

```html
<ul id="father">
    <li>二娃</li>
    <li>三娃</li>
    <li>四娃</li>
    <li>五娃</li>
    <li>六娃</li>
    <li>七娃</li>
</ul>
<input type="button" id="add-btn" value="add">
<script type="text/javascript">
    function addnode() {
        var fnode = document.getElementById("father");
        var newnode = document.createElement("li");
        newnode.innerHTML = "大娃";
        fnode.insertBefore(newnode, fnode.childNodes[0]);
    }
    var add = document.getElementById("add-btn");
    add.onclick = addnode;
</script>
```

### 3. 替换子节点的方法

替换子节点的方法 `replaceChild`
这个方法可以用一个**新节点** 去 **替换本来的旧节点**，至于这个新节点，可以是创建出来的，也可以是已存在的其他节点，这样就是一个克隆替换的行为。

replaceChild 实现子节点(对象)的替换。返回被替换对象的引用。

**使用语法**：`fathernode.replaceChild(newnode, oldnode);`
**参数说明**：
1. fathernode : 父级节点
2. newnode：用于替换 oldnode 的对象。
3. oldnode：被 newnode 替换的对象。

**返回值**：被替换的节点。

**需要注意的是**：newnode 必须先被建立，当 oldnode 被替换时，所有与之相关的属性内容都会被移除。

```html
<ul id="father">
    <li id="first">大娃</li>
    <li>二娃</li>
    <li>三娃</li>
    <li>四娃</li>
    <li>五娃</li>
    <li>六娃</li>
    <li>七娃</li>
</ul>
<input type="button" id="replace-btn" value="replace">
<script type="text/javascript">
    function replacenode() {
        var oldnode = document.getElementById("first");
        var newnode = document.createElement("li");
        newnode.innerHTML = "金刚葫芦娃";
        oldnode.parentNode.replaceChild(newnode, oldnode);
    }
    var replace = document.getElementById("replace-btn");
    replace.onclick = replacenode;
</script>
```


## 页面尺寸

常用的页面尺寸属性：

| 属性  |  说明 |
| ----  |  ---- |
| clientWidth / clientHeight | 窗口的当前宽度 / 高度 |
| scrollWidth / scrollHeight | 文档内容的宽度 / 高度（不带滚动条） |
| offsetWidth / offsetHeight | 文档内容的宽度 / 高度 |
在坐标位置里，分为滚轴距离和偏移距离，顺带着我们也说一下事件触发时鼠标指针相对于窗口的。
| 属性  |  说明 |
| ----  |  ---- |
| scrollLeft / scrollTop | 滚轴的水平偏移距离 / 垂直偏移距离 |
| offsetLeft / offsetTop | 对象与页面左边距 / 对象与页面上边距 |
| event.clientX / event.clientY  | 事件触发时鼠标指针对于窗口的水平坐标（左边距） / 垂直坐标（上边距）|


### 1. clientHeight 浏览器可视大小（宽度和高度）

```javascript
//获得不同浏览器可视大小（宽度和高度）兼容的方法
var cw = document.documentElement.clientWidth || document.body.clientWidth;
var ch = document.documentElement.clientHeight || document.body.clientHeight;
```

### 2. scrollHeight 网页尺寸

scrollHeight和scrollWidth，获取网页内容高度和宽度。

```javascript
//兼容方案
var sw = document.documentElement.scrollWidth || document.body.scrollWidth;
var sh = document.documentElement.scrollHeight || document.body.scrollHeight;
```

### 3. offsetHeight 网页尺寸
offsetHeight和offsetWidth，获取网页内容高度和宽度(包括滚动条等边线，会随窗口的显示大小改变)。
offsetWidth = clientHeight + 滚动条 + 边框。

```javascript
//兼容方案
var ow = document.documentElement.offsetWidth || document.body.offsetWidth;
var oh = document.documentElement.offsetHeight || document.body.offsetHeight;
```

## 编程练习


  [1]: https://ww1.sinaimg.cn/large/006tNc79gy1fdja4rfrgpj30gq07wt91.jpg


