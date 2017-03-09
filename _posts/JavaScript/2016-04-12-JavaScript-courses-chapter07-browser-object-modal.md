---
title: JS课堂第七节 - JavaScript 浏览器对象（BOM）
date: 2016-04-12 19:36:21
description: "JS课堂第七节 - JavaScript 浏览器对象（BOM）"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
window 对象指当前的浏览器窗口，这个对象有一些常用的方法与属性。在本章，首先学习四种计时器方法，配合使用可以实现时钟计数等效果。接着来学习三个浏览器对象下的子对象，分别是:

* location（链接信息）
* navigator（浏览器信息）
* screen（屏幕窗口信息）

## window对象

window对象是BOM的核心，window对象指当前的浏览器窗口。

### 1. 打开新窗口

```html
<input id="input" type="button" value="点击我，打开新窗口！">
<script type="text/javascript">
    function windowOpen(){
        window.open('http://www.51rgb.com', '_blank', 'width = 600, height = 400, top = 100, left = 0');
    }
    var inp = document.getElementById("input");
    inp.onclick = windowOpen;
</script>
```

## 计时器

在 JavaScript 中，我们可以在设定的时间间隔之后来执行代码，而不是在函数被调用后立即执行。

计时器有两种类型：

* 一次性计时器：仅在指定的延迟时间之后触发一次。
* 间隔性触发计时器：每隔一定的时间间隔就触发一次。

计时器有四种方法：

* setTimeout() ：在指定的毫秒数后调用函数或计算表达式。
* clearTimeout() ：取消由 setTimeout() 方法设置的 timeout。
* setInterval() ：按照指定的周期（以毫秒计）来调用函数或计算表达式。
* clearInterval() ：取消由 setInterval() 设置的 timeout。

### 1. setTimeout

setTimeout() 计时器，在载入后延迟指定时间后，去执行一次表达式，仅执行一次。

**使用语法**：setTimeout(代码, 延迟时间);
**参数说明**：
1. 要调用的函数或要执行的代码串。
2. 延时时间：在执行代码前需等待的时间，以毫秒为单位（1s = 1000ms)。

```html
<input type="text" id="inum">
<input type="button" id="ialt" value="Start">
<script type="text/javascript">
    var inum = document.getElementById("inum");
    var ialt = document.getElementById("ialt");
    ialt.onclick = function () {
        setTimeout("inum.value = 1", 1000);
        setTimeout("inum.value = 2", 2000);
        setTimeout("inum.value = 3", 3000);
        setTimeout("inum.value = 4", 4000);
        setTimeout("alert('666')", 5000);
    }
</script>
```

### 2. clearTimeout

setTimeout() 和 clearTimeout() 一起使用，可实现开始/停止计时器。

**使用方法**：clearTimeout(id_of_setTimeout)
**参数说明**：id_of_setTimeout：由 setTimeout() 返回的 ID 值。该值标识要取消的延迟执行代码块。

```javascript
var seti;
var num = 0;
function startCount(){
    document.getElementById('count').value = num;
    num = num + 1;
    seti = setTimeout("startCount()", 1000);
}
var istart = document.getElementById("istart");
istart.onclick = function () {
    startCount();
}
var istop = document.getElementById("istop");
istop.onclick = function () {
    clearTimeout(seti);
}
```

### 3. setInterval

setInterval() ：按照指定的周期（以毫秒计）来调用函数或计算表达式。

**使用语法**：setInterval(代码, 交互时间)
**参数说明**：  
代码：要调用的函数或要执行的代码串。
交互时间：周期性执行或调用表达式之间的时间间隔，以毫秒计（1s = 1000ms）。

```html
<input type="text" id="clock" size="50">
<script type="text/javascript">
    function clock(){
        var time = new Date();
        var attime = time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds();
        document.getElementById("clock").value = attime;
    }
    setInterval(clock, 1000);
</script>
```

### 4. clearInterval
clearInterval() 方法可取消由 setInterval() 设置的交互时间。

**使用语法**： clearInterval(id_of_setInterval)
**参数说明**：id_of_setInterval：由 setInterval() 返回的 ID 值。

```html
<input type="text" id="clock">
<input type="button" id="istart" value="Start">
<input type="button" id="istop" value="Stop">
<script type="text/javascript">
    var setid;
    var time;
    var attime;
    function clock(){
        time = new Date();
        attime = time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds();
        document.getElementById("clock").value = attime;
    }
    var istart = document.getElementById("istart");
    istart.onclick = function (){
        setid = setInterval(clock, 100);
    }
    var istop = document.getElementById("istop");
    istop.onclick = function (){
        clearInterval(setid);
    }
</script>
```

## location对象

location 用于获取或设置窗体的 URL，并且可以用于解析 URL。
使用语法：`location.[属性|方法]` 或 `window.location.[属性|方法]`

### 1. 对象属性
![host][1]

| 属性  |  描述 |
| ----  |  ---- |
| hash      |  设置或返回从井号 (#) 开始的 URL（锚）。 |
| host      |  设置或返回主机名和当前 URL 的端口号。 |
| hostname  |      设置或返回当前 URL 的主机名。 |
| href      |  设置或返回完整的 URL。 |
| pathname  |      设置或返回当前 URL 的路径部分。 |
| port      |  设置或返回当前 URL 的端口号。 |
| protocol  |      设置或返回当前 URL 的协议。 |
| search    |  设置或返回从问号 (?) 开始的 URL（查询部分）。 |

### 2. 对象方法

| 方法  |  描述 |
| ----  |  ---- |
| assign() |	加载新的文档。 |
| reload() |	重新加载当前文档。 |
| replace() |	用新的文档替换当前文档。 |

实例练习：

```javascript
alert(location);
location = "http://lxyweb.com";
```

## History 对象

history对象记录了用户曾经浏览过的页面(URL)，并可以实现浏览器前进与后退相似导航的功能。

**注意**:从窗口被打开的那一刻开始记录，每个浏览器窗口、每个标签页乃至每个框架，都有自己的history对象与特定的window对象关联。

**使用方法**： `window.history.[属性|方法]`  (window可以省略)

### 1. 对象属性

| 属性  |  描述 |
| ----  |  ---- |
| length |	返回浏览器历史列表中的URL数量 |

### 2. 对象方法

| 方法  |  描述 |
| ----  |  ---- |
| back() |	加载history列表中的前一个URL。 |
| forward() |	加载history列表中的下一个URL。 |
| go() |	加载history列表中的某一个具体的页面。 |


## navigator对象

navigator 对象包含有关浏览器的信息，通常用于检测浏览器与操作系统的版本。
![此处输入图片的描述][2]

```javascript
document.write(navigator.appVersion);
```

实例练习：

```javascript
var u_agent =  navigator.userAgent;     ; 
var B_name="不是想用的主流浏览器!"; 
if(u_agent.indexOf("Firefox")>-1){ 
    B_name="Firefox"; 
}else if(u_agent.indexOf("Chrome")>-1){ 
    B_name="Chrome"; 
}else if(u_agent.indexOf("MSIE")>-1 && u_agent.indexOf("Trident")>-1){ 
    B_name="IE(8-10)";  
}
document.write("浏览器:"+B_name+"<br>");
document.write("u_agent:"+u_agent+"<br>"); 
```

## screen对象

顾名思义，screen 就是你的屏幕，而这个对象里就包含了很多关于你的屏幕的信息，比如高度、宽度、颜色深度等。

* screen.height 可以返回屏幕分辨率的高。
* screen.width 返回屏幕分辨率的宽。(单位都以像素计)
除了正常的高度、宽度，还有可用高度与宽度属性。

* screen.availWidth 属性返回访问者屏幕的宽度，以像素计，减去界面特性，比如任务栏。
* screen.availHeight 属性返回访问者屏幕的高度，以像素计，减去界面特性，比如任务栏。

不同系统的任务栏默认高度不一样，及任务栏的位置可在屏幕上下左右任何位置，所以有可能可用宽度和高度不一样~

```javascript
document.write("屏幕宽度：" + screen.width + "px<br>");
document.write("屏幕高度：" + screen.height + "px<br>");
document.write("可用宽度：" + screen.availWidth + "px<br>");
document.write("可用高度：" + screen.availHeight + "px<br>");
```

## 编程练习
1. 写一个函数，用于检测当前浏览器的名称，返回一个对象，包含浏览器的名称和操作系统。



  [1]: https://ww1.sinaimg.cn/large/006tNc79gy1fdgys0i0mmj30ri060aaq.jpg
  [2]: https://ww2.sinaimg.cn/large/006tNc79gy1fdgys1depzj30gs0ckmzh.jpg


