---
title: JS课堂第三节 - 流程控制
date: 2016-03-22 17:50:36
description: "JS课堂第三节 - 流程控制"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
**前言**：
流程控制语句主要包括判断语句、选择语句以及循环语句。
判断语句我们使用 if else 结构，即二分选择，而当选择项比较多的时候，我们会采用 switch 结构。

循环语句主要分两种，一种是 for 结构循环，另一种是 while 结构循环。而在循环体中，也有两个重要的语句，就是退出 break 以及继续 continue。

**三大控制结构**

* 顺序结构
* 选择结构
* 循环结构

## 判断语句 if
if语句是基于条件成立才执行相应代码时使用的语句。

**基本语法：**

```javascript
//判断
if(条件){
    //条件符合后执行的代码
}

//二选一
if(条件){
    //条件符合后执行的代码
}else{
   //不符合条件执行的代码
}

//多种判断
if(条件1){
    //条件1成立时执行的代码
}else if(条件2){
    //条件2成立时执行的代码
}else if(条件n){
    //条件n成立时执行的代码
}else{
    //条件1、2至n不成立时执行的代码
}
```

**多种判断实例：**

```javascript
var eat = "noodles";
if(eat == "rice"){ // 如果满足条件
    console.log("吃米饭");
}
else if(eat == "noodles"){
    console.log("吃面条");
}
else { // 所有都不满足，只能选最后的了
    console.log("只有馒头了啊");
}
```

## 多种选择 switch
当有很多种选项的时候，switch比if else使用更方便，switch适合**选项多**的判断。

**语法结构：**

```javascript
switch(表达式){
case值1:
  执行代码块 1
  break;
case值2:
  执行代码块 2
  break;
...
case值n:
  执行代码块 n
  break;
default:
  与 case值1 、 case值2...case值n 不同时执行的代码
}
```

**注意：**
switch 所依赖的参数必须赋初始值，值与每个 case 值匹配，满足执行该 case 后的所有语句，并用 break 语句来阻止运行下一个 case。一定要记得break！

如果 case 后不写语句，则默认执行接下来 case 的语句。如所有 case 值都不匹配，则执行 default 后的语句。

```javascript
var eat = 3;
// 为方便 switch 做判断，1 表示粥，2 表示米饭，3 表示面条，4 表示馒头
switch(eat){
    case 1: // 然而今天并没有粥，选粥的默认给米饭
    case 2:
        console.log("米饭");
        break; // 拿饭走人

    case 3:
        console.log("面条");
        break; // 拿面走人
    // 所有都不满足，只能选最后的了
    default:
        console.log("馒头");
}
```

## 重复重复 循环语句 for
循环语句，就是重复执行一段代码。

**语法结构：**

```javascript
for(初始化变量; 循环条件; 循环迭代){
    执行语句
}
```

**实例练习：**

```javascript
var eat_arr = [2, 2, 3, 4, 2, 2]; // 吃饭选项数组
// 循环条件设置
for(var i = 0; i < eat_arr.length; i++){ // 循环开始大括号
// 以下为循环内容
    switch(eat_arr[i]){
        case 1:
        case 2:
            console.log("米饭");
            break;
        case 3:
            console.log("面条");
            break;
        default:
            console.log("馒头");
    }
} // 循环结束大括号
```

## 反反复复 循环语句 while
和for循环有相同功能的还有while循环, while循环重复执行一段代码，直到某个条件不再满足。

**语法结构：**

```javascript
var i = 0;// 循环起点设置，初始化变量
while(循环条件){
    执行语句
    i++;// 使 i 自增
}
```

**实例练习：**

```javascript
var eat_arr = [2, 2, 3, 4, 2, 2]; // 吃饭选项数组
var i = 0;// 循环起点设置
while(i < eat_arr.length)// 循环次数
{ // 循环开始大括号
// 以下为循环内容
    switch(eat_arr[i]){
        case 1:
        case 2:
            console.log("米饭");
            break;
        case 3:
            console.log("面条");
            break;
            default:
            console.log("馒头");
    }
    i++;// 使 i 自增
} // 循环结束大括号
```

## 来来回回 循环语句 do while
do while结构的基本原理和while结构是基本相同的，但是它保证循环体至少被执行一次。因为它是先执行代码，后判断条件，如果条件为真，继续循环。

**语法结构：**

```javascript
do{
    循环语句
}
while(判断条件)
```

**实例练习：**

```javascript
num= 1;
do{
    document.write("数值为:" +  num+"<br />");
    num++; //更新条件
}
while (num<=5)
```

## 退出循环 break
在while、for、do...while、while循环中使用break语句退出当前循环，直接执行后面的代码。

```javascript
var eat_arr = [2, 2, 3, 4, 2, 2]; // 吃饭选项数组
var i = 0; // 设置起点
var eat_max = 4; // 库存饭量
while(i < eat_arr.length) // 循环次数
{ // 循环开始大括号
// 以下为循环内容
    if(i == eat_max) break;// 如果饭菜没了，队伍还在排，则告诉他们解散了
    switch(eat_arr[i]){
        case 1:
        case 2:
            console.log("米饭");
            break;
        case 3:
            console.log("面条");
            break;
        default:
            console.log("馒头");
    }
    i++; // 使 i 自增
} // 循环结束大括号
```

## 继续循环 continue
continue的作用是仅仅跳过本次循环，而整个循环仍然继续执行。

```javascript
var eat_arr = [2, 2, 3, 4, 2, 2]; // 吃饭选项数组
var i = 0; // 设置起点
var eat_null = 3; // 没钱童鞋的编号
while(i < eat_arr.length) // 循环次数
{ // 循环开始大括号
// 以下为循环内容
// 如果饭卡没钱了，就自己默默离开
    if(i == eat_null){
        i++;
        continue;
    }
    switch(eat_arr[i]){
        case 1:
        case 2:
            console.log("米饭");
            break;
        case 3:
            console.log("面条");
            break;
        default:
            console.log("馒头");
    }
    i++; // 使 i 自增
} // 循环结束大括号
```

## 编程练习


写一个流程判断，变量 num 与输出值的关系如下：
1、如果 num 能同时被 3 和 5 整除，输出字符串 fizzbuzz
2、如果 num 能被 3 整除，输出字符串 fizz
3、如果 num 能被 5 整除，输出字符串 buzz
4、如果变量为空或者不是 Number 类型，输出 false
5、其余情况，输出 num
