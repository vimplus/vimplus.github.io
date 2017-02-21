---
title: JS课堂第一节 - JavaScript 基础入门
date: 2016-03-20 15:50:21
description: "JS课堂第一节 - JavaScript 基础入门"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
JavaScript诞生于1995年，为表单验证而生。
JavaScript 作为一种脚本语言，被广泛的应用于浏览器端和服务端。在这一部分，我们将对 JavaScript 有一个简单的介绍，并在之后对 JavaScript 中的基本输出方式、变量相关定义和使用进行学习。

![javascript-history](https://ww1.sinaimg.cn/large/006tNbRwgy1fcx2jhitjij30pt07o0tn.jpg)

## JavaScript 简介

### 1. 为什么要学？

* 提高用户体验
* 增加动效
* 开发强大的WEB应用

### 2. 能做什么？

* 增强页面动态效果（如：下拉菜单、图片轮播、信息滚动等）
* 实时、动态交互（如：表单验证等）
* Ajax网络请求数据

### 3. 组成部分？
Javascript是一种专为网页交互而设计的脚本语言，由下列三个不同的部门组成：
1.ECMAScirpt， 由ECMA-262定义，提供核心语言功能，js核心语言标准；
2.文档对象模型（DOM），提供访问和操作网页内容的方法和接口；
3.浏览器对象模型（BOM），提供与浏览器交互的方法和接口。

![javascript-env](https://ww4.sinaimg.cn/large/006tNbRwgy1fcx2kxi8zqj30m609gjsa.jpg)

### 4. 使用方式？
* 4.1 JavaScript的引入方法一：内嵌代码
* 4.2 JavaScript的引入方法二：外部引入
  - 优点：可维护性、可缓存、适应未来
* 4.3 JavaScript的引入方法三：延迟脚本

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
	<script defer="defer" src="js/main.js"></script>
</head>
<body>
    <!-- 网页内容 -->
</body>
</html>
```

## 第一个程序：Hello World

```javascript
console.log('Hello World');
```

## 变量

### 1. 啥叫变量？
变量是一个储存数值的容器；
### 2. 游戏规则

【变量命名】变量可以用字母、 数字以及下划线（`_`）或者美元符（`$`） 组成。
1. 必须以字母、下划线或美元符号开头，后面可以跟字母、下划线、美元符号和数字。
2. 变量名区分大小写，如：myvar 与 myVar 是两个不同的变量。
3. 不允许使用 JavaScript 关键字和保留字作为变量名，比如说break， Boolean

```javascript
//正确的写法：
myvar;
_myvar;
$myvar;
//错误的写法：
2myvar;
%myvar;
```

### 3. 变量声明与赋值

```javascript
var myvar = 123;
```
### 4. 数据类型

* String
* Number
* Boolean
* Array
* Object
* undefined和null

```javascript
var mychar1 = "双引号包起来的字符串"; // 这是字符串
var mychar2 = '单引号包起来的字符串'; // 这也是字符串
var mychar3 = '小蒜："我喜欢我们班的小可。"'; // 字符串中有双引号，用单引号包含
var mychar4 = "Uncle Wang：\"小蒜啊，'学习好'才能吸引女孩哦~\""; // 或者在特定符号（引号）前使用 \ 符号，使其转义输出
var mynum1 = 6; // 这是数字6
var mynum2 = 6.00; // 这也是数字6
var mynum3 = 123e5; // 这是使用科学（指数）计数法来书写的12300000
var mynum4 = 123e-5; // 这是0.00123
var mybool = true; // 这是布尔值
var myarr = [1, 2, 3]; // 这是数组
var myobject = {"p": "Hello"}; // 这是对象
```

## 基本的表达式与运算符

### 1. 基本的表达式
在 JavaScript 中，使用`+`来连接字符串时，其他变量也都会转变成为字符串进行连接哦~

```javascript
var y = "you";
var mysay = "I" + "love" + y; // = 后面是串表达式，mysay 值是字符串
var mynum = 12 + 6 * 2; // = 后面是数值表达式，mynum 值是数值
var mybool = mynum > 12; // = 后面是布尔表达式，mysay 值是布尔值
```

### 2. 运算符

#### 2.1 算数运算符

比如： + - * /

```javascript
var num = 24;
var myresult1 = ++num % 4 + 6 * 2; // myresult 是多少呢？
var myresult2 = num++ % 4 + 6 * 2; // myresult 是多少呢？
```

#### 2.2 赋值运算符
将算数运算符放在`=`前就可以简化，比如 `num %= 4` 等价于 `num = num % 4`。

#### 2.3 比较运算符
比如： >  <  >=  <=
== 等于
=== 全等于
!= 不等于

#### 2.4 逻辑运算符
&& （串联）
|| （并联）
![open-and](https://ww2.sinaimg.cn/large/006tNbRwgy1fcx2jgmfdzj30d306tjrm.jpg)
![open-or](https://ww2.sinaimg.cn/large/006tNbRwgy1fcx2jgza9ej30a606hjrm.jpg)

#### 2.5 运算符优先级
各运算符之间的优先级（高到低）：
`+` `-` `*` `/` 等算术操作符
`&gt;` `=` `&lt;` 等比较操作符
`&amp;` `&amp;` `||` `!` 等逻辑操作符
`=` 赋值符号。
如果同级的运算是按从左到右次序进行，多层括号由里向外。
在这里提醒一下，在分不清优先级的时候，通过加括号来记住运算顺序就可以了。

## 编程练习
连接数字和字符串，指出下面非字符串的结果

```javascript
var a = "6" + "6"; console.log(a);
var b = 6 + "6"; console.log(b);
var c = 60 + 6; console.log(c);
var d = 6 + 6 + ""; console.log(d);
var x = 10 + "20" - 10; console.log(x)
var v = 10 + + '10'; console.log(v)
```
