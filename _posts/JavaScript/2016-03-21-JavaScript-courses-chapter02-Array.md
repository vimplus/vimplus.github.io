---
title: JS课堂第二节 - JavaScript 的数组
date: 2016-03-21 16:50:36
description: "JS课堂第二节 - JavaScript 的数组"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
**前言**：
在本章我们首先学习什么是数组，接着通过几个例子，介绍如何创建数组、给数组赋值及增加新元素等，最后学习多维数组概念。希望大家重点理解**数组的索引**，以及数组的长度即 **length** 属性。

## 什么是数组
### 1. 数组的定义
一句话理解：【可以存放多个数据的变量】。
**数组（Array）是按次序排列的一组值**，单个值称为元素，它们的位置都有编号（从 0 开始也就是说第一个元素的下标为0，第二个为1，以此类推）。整个数组用方括号表示。

```javascript
//表达形式一：
var arr = [];
var arr[0] = 'a';
var arr[1] = 'b';
var arr[2] = 'c';
//表达形式二：
var arr = ['a', 'b', 'c'];
```
### 2. 可以装什么？
任意一种类型的数据，都可以放进数组里。

```javascript
var arr = ['x', {a:1}, [1, 2, 3], function(){ return true; }];
arr[0];    // String
arr[1];    // Object
arr[2];    // Array
arr[3];    // function
```

由此可见，数组中的元素也可以是一个数组，我们把这种形式称为多维数组。

```javascript
var arr = [[1, 2], [3, 4]];
arr[0][1];    // 2
arr[1][1];    // 4
```

### 3. length 属性
3.1 数组的 length 属性，可以返回数组的成员数量。

数组的 length 属性与对象的 length 属性有所区别，只要是数组就一定有 length 属性，而对象不一定有。

而且，数组的 length 属性是一个动态的值，等于键名中最大值加 1。

```javascript
var arr = ['a', 'b'];
arr.length;    // 2

arr[2] = 'c';
arr.length;    // 3

arr[9] = 'd';
arr.length;    // 10

arr[10000] = 'e';
arr.length;    // 10001
```

可以发现，数组的数字键值不需要连续，length 属性的值总是等于最大的那个键值大 1。

3.2 length 属性是可写的。如果人为设置一个小于当前成员个数的值，该数组的成员会自动减少到 length 设置的长度。

```javascript
var arr = ['a', 'b', 'c'];
arr.length;    // 3

arr.length = 2;
arr;    // ["a", "b"]
```

当数组的 length 属性设置为 2 时，即最大的整数键值只能是 1，所以键值 2 对应的元素（'c'）就自动被 删除 了。

因此，将数组清空的一个有效办法，就是将数组的 length 属性设为 0。

3.2 数组的长度
需要注意，因为数组的索引总是由 0 开始，所以一个数组的上下限分别是： 0 和 length - 1 。如数组的长度是 5 ，数组的上下限分别是 0 和 4 。

```javascript
var myarr = ["小吉", "小雷", "小可", "小新", "月影"];
console.log("我们班有：" + myarr.length  + "人");
```

### 4. 创建数组

```javascript
var myarray = new Array(6);
console.log(myarray);
```
### 5. 数组赋值

```javascript
var myarr = new Array(3);
myarr[0] = "小五";
myarr[1] = "大H";
myarr[2] = "月影";
console.log("班里学号为 0 的是：" + myarr[0]);
console.log("班里学号为 1 的是：" + myarr[1]);
console.log("班里学号为 2 的是：" + myarr[2]);
var arr = [1, "abc", myarr];
console.log(arr[1]);
```

### 6. 增加新元素

```javascript
var myarr = new Array(3);
myarr[0] = "小五";
myarr[1] = "大H";
myarr[2] = "月影";
console.log("班里学号为 0 的是：" + myarr[0]);
console.log("班里学号为 1 的是：" + myarr[1]);
console.log("班里学号为 2 的是：" + myarr[2]);
myarr[3] = "小新";
console.log(myarr[3]);
```
### 7. 使用数组字面量
要得到一个数组元素的值，只需引用数组变量并提供一个索引。

```javascript
var myarr = ["小吉", "小雷", "小可", "小新", "月影"];
var mynum = 4;
console.log("学号为 4 的是：" +   myarr[mynum]  );
```

### 8. 数组的嵌套（多维数组）

```javascript
var myarr = [[0, 1, 2], [1, 2, 3]];
myarr[0][1] = 5; //将 5 的值传入到数组中，覆盖原有值。
console.log(  myarr[0][1] 	);
```

## 编程练习
1. 把前端群里任意10位同学的群昵称用数组储存，并分别输出。
2. 把1到10写入数组中，求出所有元素相加的总和。
