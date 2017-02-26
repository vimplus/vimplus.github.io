---
title: JS课堂第四节 - JavaScript函数
date: 2016-03-24 19:50:36
description: "JS课堂第四节 - JavaScript函数"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
**前言**：
在这一章我们将学习函数的声明与函数的用法，接下来用几个例子来演示函数的调用方法以及函数参数、返回值的用法。

## 什么是函数

### 1. 函数的概念

函数是由事件驱动的或者当它被调用时执行的可重复使用的代码块。

### 2. 函数的作用
函数的作用：可以写一次代码，然后反复地重用这个代码。

## 函数声明
声明函数时，前面需要使用关键字 function，然后紧跟函数名()，函数体(即执行的语句)要被包在 {} 中：

语法结构：

```javascript
function  函数名( ) {
     函数体;
}
```

实例练习：

```javascript
function add() {
    sum = 3 + 2;
    alert(sum);
}
add();
```

## 函数调用
函数定义好后，是不能自动执行的，需要调用它,直接在需要的位置写函数名。

* 在script代码中调用
* 在HTML代码中调用

## 带参数的函数

语法结构：

```javascript
function 函数名(参数1,参数2) {
     函数代码
}
```

注意:参数可以多个，根据需要增减参数个数。参数之间用(逗号，）隔开。

```javascript
function add(x,y)
{
   sum = x + y;
   console.log(sum);
}
```

x和y则是函数的两个参数，调用函数的时候，我们可通过这两个参数把两个实际的加数传递给函数了。

## 函数的返回值

语法结构：

```javascript
function add(x,y){
   sum = x + y;
   return sum; //返回函数值,return后面的值叫做返回值。
}
```

还可以通过变量存储调用函数的返回值，代码如下:

```javascript
result = add(3,4);//语句执行后,result变量中的值为7。
```

注意:函数中参数和返回值不只是数字，还可以是字符串等其它类型。

```javascript
function  app(x,y)
  { var sum,x,y;
    sum = x * y;
    return sum;
  }
 var req1 = app(5,6);
 var req2 = app(2,3);
 var sumq = req1 + req2;
document.write("req1的值:"+req1+"<br/>");
document.write("req2的值:"+req2+"<br/>");
document.write(req1+"与"+req2+"和:"+sumq);
```

## 闭包

### 前言

要学习闭包首先要了解JavaScript的**变量作用域**。
**变量的作用域** 无非就是两种：`全局变量`和`局部变量`。

在函数外部自然无法读取函数内的局部变量。

```javascript
function fn(){
    var n=999;
}
console.log(n); // error: n is not defined
```

如何从外部读取局部变量?
那就是在函数的内部，再定义一个函数。这就形成了我们要说的闭包。

### 闭包的概念

「官方」的解释：「闭包」，是指拥有多个变量和绑定了这些变量的环境的
表达式（通常是一个函数），因而这些变量也是该表达式的一部分。

但不要咬文嚼字，我们简单的可以理解为: **能够读取其他函数内部变量的函数**。
> 闭包是个函数，而它「记住了周围发生了什么」。表现为由「一个函数」体中定义了「另个函数」

### 闭包的作用

* 1.可以读取函数内部的变量；

```javascript
function outer () {
    var a = 2;
    function inner () {
        console.log(a);
    }
    return inner();
}
outer();
```

* 2.让这些变量的值始终保持在内存中。

```javascript
//示例1：
var add = null;
function outer () {
    var a = 999;

    add = function (){
        a++;
    }
    function inner () {
        console.log(a);
    }
    return inner;
}
var res = outer();
res(); //999
add();
res(); //1000

//示例2：
function makeAdder(x) {
  return function(y) {
    return x + y;
  };
}

var add5 = makeAdder(5);
var add10 = makeAdder(10);

console.log(add5(2));  // 7
console.log(add10(2)); // 12
```

## 编程练习

1、使用javascript代码写出一个函数：实现传入两个整数后弹出较大的整数。

```javascript
//定义函数
function maxNum(x,y){
    if(x>y){
        return x;
    }else if(y>x){
        return y;
    }else{
        return "我们是相等的！";
    }
}
```

2、写一个函数第一次运行时输出1，第二次运行输出2，第三次输出1……以此类推(不允许全局变量);
