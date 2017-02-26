---
title: JS课堂第五节 - JavaScript 网页交互（事件）
date: 2016-03-27 20:50:36
description: "JS课堂第五节 - JavaScript 网页交互（事件）"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
**前言**：
想要在网页中输出信息，有两种方法，一种是用 write 直接写在页面中，另一种是用 alert 在浏览器中弹出小窗。从页面中获取元素，常见的有三种方法，分别是通过 id 获取、通过标签名获取以及通过名称获取。本章将学习事件绑定的用法，以及一些常见的页面事件，如鼠标单击、输入框选中等等。

## 输出到网页

### 1. document.write
实例练习：

```javascript
var mychar = "JavaScript";
document.write(mychar);
var mynum = "12";
document.write(mynum);
var mynum = "1&nbsp;&nbsp;&nbsp;2";
document.write(mynum);
```

### 2. 警告框 alert
使用语法： alert(字符串或变量)

## 获取HTML元素

### 1. 通过id获取元素
document.getElementById();

```html
<p id="pid">JavaScript</p>
<script type="text/javascript">
    var pid = document.getElementById("pid");
    document.write("内容：" + pid.innerHTML); //输出获取的 P 标签内容。
</script>
```

### 2. 通过标签名获取元素
document.getElementsByTagName()返回的是指定标签名的元素对象的集合。
**使用语法**：document.getElementsByTagName(tagname);
**参数说明**：tagname 是标签的名称，例如：div，p，span
**注意事项**：和数组类似也有 length 属性，可以和访问数组一样的方法来访问，从 0 开始。

实例练习：

```html
<p>Hello</p>
<p>Do you like</p>
<p>JavaScript</p>
<script type="text/javascript">
    var p = document.getElementsByTagName("p");
    for(var i = 0; i < p.length; i++){
        alert(p[i].innerHTML);
    }
</script>
```

### 3. 通过名称获取元素
getElementsByName()返回带有指定名称的元素对象的集合。与 getElementById 方法不同的是，通过元素的 name 属性查询元素，而不是通过 id 属性。id 的值是唯一的，就像身份证号，而名字是可以相同的，所以使用 name 属性查询元素时，会把所有同名的元素都找到。

**使用语法**：document.getElementsByName("name_value")
**注意事项**：
1. 因为文档中的 name 属性可能不唯一，所以 getElementsByName() 方法返回的是元素的数组，而不是一个元素。
2. 和数组类似也有 length 属性，可以使用访问数组元素的方法来访问成员元素，下标从 0 开始。

实例练习：

```html
<input name="iname" type="text" value="1">
<input name="iname" type="text" value="2">
<input name="iname" type="text" value="3">
<input name="iname" type="text" value="4">
<input name="iname" type="text" value="5">
<input name="iname" type="text" value="6">
<script type="text/javascript">
    var inp = document.getElementsByName("iname");
    for(var i = 0; i < inp.length; i++){
        alert(inp[i].value);
    }
</script>
```

## 获取属性

### 1. 获取属性与设置属性

```html
<p id="pid" title="JavaScript">JavaScript</p>
<button id="btn">click</button>
<script type="text/javascript">
    var btn = document.getElementById("btn");
    btn.onclick = attr;
    function attr() {
        var pid = document.getElementById("pid");
        alert(pid.getAttribute("id"));
        alert(pid.getAttribute("title"));
        pid.setAttribute("title", "hello");
        alert(pid.getAttribute("title"));
    }
</script>
```

## JavaScript事件

### 1. 什么是事件
事件是可以被 JavaScript 侦测到的行为。

### 2. 事件的三个阶段
DOM2.0模型将事件处理流程分为三个阶段：

* 一、事件捕获阶段
* 二、事件目标阶段
* 三、事件冒泡阶段。


![event](https://ww2.sinaimg.cn/large/006tNc79gy1fd4802qps9j30f00diaap.jpg)

**事件捕获**：当某个元素触发某个事件（如onclick），顶层对象document就会发出一个事件流，随着DOM树的节点向目标元素节点流去，直到到达事件真正发生的目标元素。在这个过程中，事件相应的监听函数是不会被触发的。

**事件目标**：当到达目标元素之后，执行目标元素该事件相应的处理函数。如果没有绑定监听函数，那就不执行。

**事件起泡**：从目标元素开始，往顶层元素传播。途中如果有节点绑定了相应的事件处理函数，这些函数都会被一次触发。如果想阻止事件起泡，可以使用e.stopPropagation()（Firefox）或者e.cancelBubble=true（IE）来组织事件的冒泡传播。

### 3. 事件绑定的三种方式
方式一：

```html
<a href="#" onclick="fn()";></a>
```

方式二： 元素.事件名 = 函数名;
方式三：

```
obj.addEventListener('事件名（不带ON）', 函数名, true/false); //FF等
attachEvent("事件名"，函数名); //IE下
```

兼容方式：

```javascript
//绑定
if (typeof document.addEventListener != "undefined") {
    document.addEventListener("mousedown",fn,true);
} else {
    document.attachEvent("onmousedown",fn);
}
//移除
if (typeof document.addEventListener != "undefined") {
    document.removeEventListener("mousedown",fn,true);
} else {
    document.detachEvent("onmousedown",fn);
}
```

### 4. 鼠标单击
onclick 是鼠标单击事件，当用户在网页上单击某元素时，就会触发该事件。
用法： 元素.onclick = 函数名;

```html
<p id="pid">JavaScript</p>
<button id="btn">click</button>
<script type="text/javascript">
    var btn = document.getElementById("btn");
    btn.onclick = hello;
    function hello() {
        var pid = document.getElementById("pid");
        pid.innerHTML = "Hello!";
    }
</script>
```

### 5. 鼠标经过与移出
鼠标经过事件，当鼠标移到一个对象上时，该对象就触发 **onmouseover**事件，并执行**onmouseover**事件调用的程序。

鼠标移开事件，当鼠标移开当前对象时，执行**onmouseout**调用的程序。

```javascript
var btn = document.getElementById("btn");
btn.onmouseover = over;
btn.onmouseout = out;
function over() {
    var pid = document.getElementById("pid");
    pid.innerHTML = "over";
}
function out() {
    var pid = document.getElementById("pid");
    pid.innerHTML = "out";
}
```

### 6. 光标焦点与失去焦点
当网页中的对象获得聚焦时，执行**onfocus**调用的程序就会被执行。
**onblur** 事件与 **onfocus** 是相对事件，当光标离开当前获得聚焦对象的时候，触发 **onblur** 事件，同时执行被调用的程序。

```javascript
var inp = document.getElementById("input");
inp.onfocus = focus;
inp.onblur = blur;
function focus() {
    var pid = document.getElementById("pid");
    pid.innerHTML = "focus";
}
function blur() {
    var pid = document.getElementById("pid");
    pid.innerHTML = "blur";
}
```

### 7. 输入框内容选中与改变
选中事件，当文本框或者文本域中的文字被选中时，触发 **onselect** 事件，同时调用的程序就会被执行。
通过改变文本框的内容来触发 **onchange** 事件，同时执行被调用的程序。

```javascript
var inp = document.getElementById("input");
inp.onselect = select;
inp.onchange = change;
function select() {
    var pid = document.getElementById("pid");
    pid.innerHTML = "select";
}
function change() {
    var pid = document.getElementById("pid");
    pid.innerHTML = "change";
}
```

### 8. 确认框
confirm 消息对话框通常用于允许用户做选择的动作，如：“确定提交？”等。弹出对话框(包括一个确定按钮和一个取消按钮)。

**使用语法**：`confirm(str)`
**参数说明**：str 在消息对话框中要显示的文本。

```html
<input id="input" type="button" value="点击我">
<script type="text/javascript">
    function rec(){
        var message = confirm("Do you like me?");
        if (message == true) {
            document.write("么么哒！~");
        }else {
            document.write("泥奏凯！");
        }
    }
var inp = document.getElementById("input");
inp.onclick = rec;
</script>
```

### 9. 提问框
prompt 弹出消息对话框,通常用于询问一些需要与用户交互的信息。弹出消息对话框（包含一个确定按钮、取消按钮与一个文本输入框）。
**使用语法**：`prompt(str1, str2)`
**参数说明**：
str1: 要显示在消息对话框中的文本，不可修改。
str2: 选填，文本框中的内容，可以修改。
**返回值**：
1、点击确定按钮，文本框中的内容将作为函数返回值。
2、点击取消按钮，将返回 null。

```html
<input id="input" type="button" value="点击我">
<script type="text/javascript">
    function rec(){
        var score; // score变量，用来存储用户输入的成绩值。
        score = prompt("Your score");

        if(score >= 90){
            document.write("你很棒！");
        }else if (score >= 75) {
            document.write("不错哦！");
        }else if (score >= 60) {
            document.write("要加油！");
        }else{
            document.write("要努力了哦！");
        }
    }
    var inp = document.getElementById("input");
    inp.onclick = rec;
</script>
```

### 10. 页面加载完
当一个页面加载出来或者刷新的时候，window 对象的 onload 事件就会被触发。
用法： **对象.事件 = 函数名**

```javascript
window.onload = load;
function load() {
    alert("load");
}
```

## 事件冒泡与事件委托（事件代理）

### 冒泡
当一个元素上的事件被触发的时候，比如说鼠标点击了一个按钮，同样的事件将会在那个元素的所有祖先元素中被触发。这一过程被称为事件冒泡；这个事件从原始元素开始一直冒泡到DOM树的最上层。
[JavaScript事件冒泡][1]

#### 冒泡的作用
（1）事件冒泡允许多个操作被集中处理（把事件处理器添加到一个父级元素上，避免把事件处理器添加到多个子级元素上），它还可以让你在对象层的不同级别捕获事件。
（2）让不同的对象同时捕获同一事件，并调用自己的专属处理程序做自己的事情，就像老板一下命令，各自员工做自己岗位上的工作去了。

#### 冒泡的优缺点
> 让需要创建的以及驻留在内存中的事件处理器少了

#### 阻止冒泡

```
e.stopPropagation()（Firefox）或者 e.cancelBubble=true（IE）
//该函数的功能用来阻止事件冒泡．并兼容多浏览器
function stopBubble(e){
	//如果传入了事件对象.那么就是非IE浏览器
	if (e && e.stopPropagation) {
		//因此它支持W3C的stopPropation()方法
		e.stopPropagation();
	} else {
		//否则,我们得使用IE的方式来取消事件冒泡
		window.event.cancelBubble = true;
	}
}
```

### 事件委托
得益于浏览器的事件冒泡机制，当我们需要对很多元素添加事件的时候，我们可以通过将事件添加到它们的父节点而将事件委托给父节点来触发处理函数。
[JavaScript事件代理和委托][2]

```javascript
function getEventTarget(e) {
   e = e || window.event;
   return e.target || e.srcElement;
}
function editCell(e) {
   var target = getEventTarget(e);
   if(target.tagName.toLowerCase() === 'td') {
     // DO SOMETHING WITH THE CELL
   }
}
```

## 编程练习
拖拽元素：

```html
<div id="box"></div>
<script type="text/javascript">
    var oDiv = document.getElementById("box");
    oDiv.onmousedown = function (ev) {
        var oEvent = ev;
        var disX = oEvent.clientX - oDiv.offsetLeft;
        var disY = oEvent.clientY - oDiv.offsetTop;
        document.onmousemove = function (ev) {
            oEvent = ev;
            oDiv.style.left = oEvent.clientX - disX + "px";
            oDiv.style.top = oEvent.clientY - disY + "px";
        }
        document.onmouseup = function () {
            document.onmousemove = null;
            document.onmouseup = null;
        }
    }
</script>
```


[1]: https://my.oschina.net/chape/blog/190198
[2]: https://www.cnblogs.com/owenChen/archive/2013/02/18/2915521.html
