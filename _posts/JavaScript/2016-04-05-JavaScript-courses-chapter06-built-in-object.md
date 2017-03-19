---
title: JS课堂第六节 - JavaScript 内置对象
date: 2016-04-05 21:12:36
description: "JS课堂第六节 - JavaScript 内置对象"
layout: post
categories: JavaScript
tags: [JavaScript,JS课程笔记]
comments: true
pay: true
---
**前言**：
在本章我们首先学习什么是对象，对象是**一种无序的数据集合**，由若干个 “键值对”（key-value）构成。接下来我们介绍js内置对象，分别是：字符串对象、数组对象、时间对象、及Math 对象，通过一些例子来详细介绍他们的一些方法。

## 什么是对象

### 1. 对象的定义

对象（Object）是 JavaScript 的核心概念，也是最重要的数据类型。

所谓对象，带有属性和方法的数据类型，一般由若干个 “键值对”（key-value）构成。如：

```javascript
var obj = {
    content: "Hello Lxyour！"
};
```

大括号定义了一个对象，它被赋值给变量 obj ，内部包含一对键值对（属性），content 是“键名”（属性名），字符串 “Hello” 是 “键值” （属性值）。键名与键值之间用冒号分割。如果有多个键值对，每个键值对之间用逗号分隔。

### 2. 键名

键名加不加引号都可以，前面的代码也可以写成这样：

```javascript
var obj = {
    "content": "Hello Lxyour"
};
```

### 3. 书写语法

对象的书写语法，通常有3种：

```javascript
var obj1 = {};
var obj2 = new Object();
var obj3 = Object.create(null);
```

这三句是等价的。一般来说，第一种采用大括号的写法（即对象字面量的写法）比较简洁，第二种采用构造函数的写法清晰表示了意图，第三种写法一般用在需要对象继承的场合。

### 4. 对象的引用

如果不同的变量名指向同一个对象，那么它们都是这个对象的引用，也就是说指向同一个内存地址。修改其中一个变量的属性，会影响到其他所有变量。

```javascript
var obj1 = {};
var obj2 = obj1;

obj1.a = 1;
obj2.a;    // 1

obj2.b = 2;
obj1.b;    // 2
```

上面代码中， obj1 和 obj2 指向同一个对象，因此为其中任何一个变量添加属性，另一个变量都可以读写该属性。

当变量是一个原始类型数据时，其值即数据值。如：var num = 1;。
当变量是一个对象（包括数组等）时，该变量实际上存的是对该对象的一个引用。如：

```javascript
var obj1 = {};
var obj2 = obj1;
```

## JS内置对象

字符串、数字、布尔值、undefined 以及 null 都是原始类型（primitive value）而非对象。而 String, Number, Boolean, Object 都是语言内置的对象(built-in object)，可以通过各自的构造函数得到。

比如在 JavaScript 中，字符串是一个原始类型，它本身没有属性，当你对一个字符串作属性运算的时候（如 "some string".length）, JavaScript 引擎会将该字符串包装成一个对象，该对象是通过 String 构造函数得到的。也就是说 "some string".length 实际上是 (new String("some string")).length。

> 把基本数据类型转换为对应的引用类型的操作称为装箱，比如：new String("some string")，将字符串 "some
> string" 转换为一个 String 对象。

### 1. 对象的属性与方法

对象的特征叫**属性**，在对象上执行来实现一些功能的动作(函数)叫**方法**

#### 1.1 对象的属性

```javascript
var message = "Hello World!";
var mlen = message.length;
console.log(mlen);
```

#### 1.2 对象的方法

```javascript
var message = "Hello World!";
var upmess = message.toUpperCase();
console.log(upmess);
```

### 2. String对象

```javascript
var mystr = "I like JavaScript!";
var mylen = mystr.length;
var myup = mystr.toUpperCase();
var mylow = mystr.toLowerCase();
console.log("字符串长度：" + mylen);
console.log("大写转化后：" + myup);
console.log("小写转化后：" + mylow);
```

#### 2.1 返回字符串首次出现的位置-indexOf()

`indexOf()` 方法可返回某个指定的字符串值在字符串中首次出现的位置。
使用语法：

```javascript
stringObject.indexOf(substring, startpos);
```

参数说明：substring 必填的哦，就是你想搜索的子字符串。
startpos是可选填的整数参数，规定开始检索的位置，取值范围是 0 到 stringObject.length - 1。省略的话就从首字符开始检索。
需要注意的是： indexOf() 方法区分大小写。
如果要检索的字符串值没有出现，则该方法返回 -1。

```javascript
var mystr = "I like JavaScript!";
console.log(mystr.indexOf("I"));
console.log(mystr.indexOf("v"));
console.log(mystr.indexOf("v", 8));
console.log(mystr.indexOf("a", mystr.indexOf("a") + 1));
```

#### 2.2 返回指定位置字符-charAt()

`charAt()` 方法可返回指定位置的字符。返回的字符是长度为 1 的字符串。
使用语法：

```javascript
stringObject.charAt(index);
```

参数说明：index 必填，表示字符串中某个位置的数字，即字符在字符串中的下标。

```javascript
var mystr = "I love JavaScript!";
console.log(mystr.charAt(2)); //l
```
#### 3.3 字符串分割成数组-split()

`split()` 方法将字符串分割为字符串数组，并返回此数组。
使用语法：

```javascript
stringObject.split(separator, limit);
```

参数说明：separator 必填，从该参数指定的地方分割 stringObject。limit 可选参数，分割的次数，如果设置，返回所以的字串
需要注意的是：如果把空字符串 "" 用作 separator，那么 stringObject 中的每个字符之间都会被分割。

```javascript
var mystr = "www.lxyweb.com";
console.log(mystr.split("."));
console.log(mystr.split(".", 2));
```

#### 2.4 提取字符串-substring()

`substring()` 方法用于提取字符串中介于两个指定下标之间的字符。
使用语法：

```javascript
stringObject.substring(starPos, stopPos);
```

参数说明：starPos 必填，一个非负的整数，提取的开始位置； stopPos 可选参数，截取的结束位置，如果不填，那么返回的字串会一直到字符串对象的结尾。

需要注意的是：
返回的内容是从 start 开始(包含 start 位置的字符)到 stop - 1 处的所有字符，其长度为 stop 减 start。
如果参数 start 与 stop 相等，那么该方法返回的就是一个空串（即长度为 0 的字符串）。
如果 start 比 stop 大，那么该方法在提取子串之前会先交换这两个参数。

```javascript
var mystr = "I like JavaScript!";
console.log(mystr.substring(7));
console.log(mystr.substring(2, 6));
```

#### 2.5 提取指定数目的字符串-substr()

`substr()` 方法从字符串中提取从指定位置开始的指定数目的字符串。
使用语法：

```javascript
stringObject.substr(startPos, length);
```

参数说明：startPos 必填的哦，要提取的子串的起始位置，必须是数值；length，可选，指提取字符串的长度，如果省略，则返回从 stringObject 的开始位置 startPos 到 stringObject 的结尾的字符。

需要注意的是：如果参数 startPos 是负数，从字符串的尾部开始算起的位置。也就是说，-1 指字符串中最后一个字符，-2 指倒数第二个字符，以此类推。
如果 startPos 为负数且绝对值大于字符串长度，startPos 为 0。

```javascript
var mystr = "I like JavaScript!";
console.log(mystr.substr(7));
console.log(mystr.substr(2,4));
```

#### 2.6 选区部分字符串-slice()

`slice()` 提取字符串的一部分，并返回这个新的字符串。
使用语法：

```javascript
str.slice(beginSlice[, endSlice])
```

注意：
slice() 提取的新字符串包括beginSlice但**不包括 endSlice**。
例1：`str.slice(1, 4)` 提取新字符串从第二个字符到第四个 (字符索引值为 1, 2, 和 3)。

#### 编程练习
写一个函数，统计字符串中出现次数最多的字符和次数
例如：

```javascript
var str = 'abcdaagjdaa'; 输出：{maxKey: 'a', maxNum: 5}
```

#### 拓展阅读

[MDN - JavaScript 标准库 - String][1]

### 3. 数组对象

定义数组的语法：

定义了一个空数组：`var 数组名 = new Array()` 或者 `var arrName = []`;
定义时指定有 n 个空元素的数组：var 数组名 = new Array(n);
定义数组的时候，直接初始化数据：var 数组名 = [<元素 1>, <元素 2>, <元素 3>...];

我们定义 myArray 数组，并赋值，代码如：`var myArray = [2, 5, 6];`
说明：定义了一个数组 myArray，里边的元素是：

```javascript
myArray[0] = 2;
myArray[1] = 5;
myArray[2] = 6;
```

#### 常用方法

| 方法名 | 作用 | 返回值 | 说明 | 示例 |
| --- | --- | --- | --- |
| `slice()` | 选区子元素，选区部分元素 | 新数组| **返回新数组** | arr.slice(0) //选区所有 |
| `concat()` | 两个数组之间 **连接** 起来 | 新数组 | **返回新数组** | arrA.concat(arrB) |
| `splice()` | **删除/添加/替换**数组中元素 | 返回被**删除/添加/替换**的元素组成的一个新数组 | **改变原数组** | arr.splice(0,1) |
| `push()` | 添加一个或多个元素到数组的 **末尾** (往数组后面追加新元素) | 返回原数组的长度 | **改变原数组** | arr.push(item) |
| `unshift()` | 在数组的 **开头** 添加一个或者多个元素 | 返回原数组的长度 | **改变原数组** | arr.unshift(item) |
| `shift()` | 删除数组的 **第一个** 元素 | 返回被删除的这个元素 | **改变原数组** | arr.slice(0) |
| `pop()` | 删除一个数组中的 **最后一个** 元素 | 返回被删除的这个元素 | **改变原数组** | arr.slice(0) |
| `join()` | 数组转字符串 | 返回组成的字符串 | **返回字符串** | arr.join('-') |
| `reverse()` | 颠倒数组的顺序 | 返回颠倒后的数组 | **改变原数组** | arr.reverse() |
| `sort()` | 数组的排序 | 返回排序后的数组 | 默认按Unicode编码排序 | arr.sort() |

#### 3.1 数组连接-concat()

concat() 方法用于连接两个或多个数组。此方法返回一个新数组，不改变原来的数组。   
使用语法：

```javascript
array1.concat(array2, array3, ...arrayi..., arrayN);
```

参数说明：array1 是要连接的第一个数组，arrayi 是后续连接的第 i 个数组。  

```javascript
var mya1 = new Array("hello!");
var mya2 = new Array("I", "love");
var mya3 = new Array("JavaScript", "!");
console.log(mya1.concat(mya2,mya3));
console.log(mya1);
```

#### 3.2 数组转化成字符串-join()

* `split()`将`字符串`分割并返回`数组`；
* `join()` 方法用于把`数组`中的所有元素放入一个`字符串`，并返回这个字符串。元素是通过指定的分隔符进行分隔的，不影响原数组。

使用语法：

```javascript
arrayObject.join(separator);
```

参数说明：separator 可选，指定要使用的分隔符，如省略，则使用`逗号`作为分隔符

```javascript
var myarr = new Array(3);
myarr[0] = "www";
myarr[1] = "lxyweb";
myarr[2] = "com";
console.log(myarr.join("."));
```

#### 3.3 选取数组子元素-slice()

`slice()` 方法可从已有的数组中返回一个新的数组，包含从 start 到 end （不包括该元素）的 所有元素。
使用语法：`arrayObject.slice(start, end)`
参数说明：star 必填，规定从何处开始选取。如果是负数，就从数组尾部开始算起始位置，比如 -1 指最后一个元素，-2 指倒数第二个元素。
 end 可选，规定从何处结束选取。该参数是子数组结束处的父数组下标。如果不指定，则一直选取到 arrayObject 末尾。如果为负数，则从数组尾部开始算结束位置，同 start。

需要注意的是：

* 1.可使用负值从数组的尾部选取元素。
* 2.如果 end 未被规定，那么 slice() 方法会选取从 start 到数组结尾的所有元素。
* 3.String.slice() 与 Array.slice() 相似。
* 4.该方法并不会修改数组，而是返回一个子数组。

```javascript
var myarr = new Array(3);
myarr[0] = "www";
myarr[1] = "lxyweb";
myarr[2] = "com";
console.log(myarr.slice(0,2));
```

#### 3.4 删除/添加/替换数组中的元素-splice()

`splice()` 方法用新元素替换旧元素，以此修改数组的内容, 返回被删除/添加/替换的元素组成的新元素。
使用语法：`array.splice(start, deleteCount[, item1[, item2[, ...]]])`

**返回值:**
由被删除的元素组成的一个数组。如果只删除了一个元素，则返回只包含一个元素的数组。如果没有删除元素，则返回空数组。
**示例：**

```javascript
var arr = ['a','b','c','x','z'];
arr.splice(4, 0, 'y');
console.log(arr); //['a','b','c','x','y','z']

arr.splice(3, 1);
console.log(arr); //['a','b','c','z']
```

#### 3.5 颠倒数组元素顺序-reverse()

`reverse()` 方法用于颠倒数组中元素的顺序。
使用语法：`arrayObject.reverse()`

```javascript
var myarr = new Array(3);
myarr[0] = "www";
myarr[1] = "lxyweb";
myarr[2] = "com";
console.log(myarr.reverse());
console.log(myarr);
```

#### 3.6 数组排序-sort()

`sort()`方法使数组中的元素按照一定的顺序排列。
使用语法： `arrayObject.sort (fn)`
参数说明：fn 方法函数可选，如果不指定方法函数，则按 unicode 码顺序排列。

```javascript
function sortNum(a,b) {
    return a - b;
    //升序，如降序，把“a - b”该成“b - a”
}
var myarr1 = new Array("Hello", "John", "love", "JavaScript");
var myarr2 = new Array("80", "16", "50", "6", "100", "1");
console.log(myarr1.sort());
console.log(myarr2.sort());
console.log(myarr2.sort(sortNum));
```

#### 编程练习

为下列要求分别写一个函数实现其功能：

> 1. 查找数组元素的位置，没有该元素则返回-1；例如：[1,2,4,6,8]  传入4返回2。
> 2. 将数组所有元素求和；例如：[1,2,3,4,5]  求和得到15。
> 3. 移除数组中指定元素，不改变原数组；例如：[1,2,4,6,8]  传入4返回[1,2,6,8]。
> 4. 移除数组中指定元素，改变原数组；例如：[1,2,2,4,6,2,8]  传入2返回[1,4,6,8]。
> 5. 用三种方法实现在数组后面添加元素，不改变原数组；例如：[1,2,3,5]  传入6返回[1,2,3,5,6] 。
> 6. 删除数组最后一个元素，不改变原数组；例如：[1,2,3,5]  删除后返回[1,2,3] 。
> 7. 在数组数组开头添加一个元素，不改变原数组；例如：[1,2,3]  传入5返回[5,1,2,3] 。
> 8. 删除数组第一个元素，不改变原数组；例如：[1,2,3,5]  删除后返回[2,3,5] 。
> 9. 合并数组 arr1 和数组 arr2。不要直接修改数组 arr，结果返回新的数组。例如：insert([1, 2, 3, 4], 'z', 2) 得到[1, 2, 'z', 3, 4]。
> 10. 统计数组 arr 中值等于 item 的元素出现的次数；例如：count([1, 2, 5, 5, 3, 5, 3], 5) 得到3。


#### 拓展阅读

[MDN - JavaScript 标准库 - Array][2]


### 4. 时间对象（Date）

```javascript
var nowTime = new Date();
console.log(nowTime);
```

#### 编程练习

Data()的相关方法实例：

```javascript
var now = new Date();
now.setTime(now.getTime() + 60 * 60 * 1000);
var myyear = now.getFullYear(); // 四位数年份，如 2015
var mymonth = now.getMonth(); // 月份 [0, 11]，要加 1，如 7 (8 月)
var mydate = now.getDate(); // 月中日期，如 1 (1 号)
var myhours = now.getHours(); // 小时，24 小时制
var myminutes = now.getMinutes(); // 分钟
var myseconds = now.getSeconds(); // 秒钟
console.log("今天是" + myyear + "年"+ mymonth + "月" + mydate + "日");
console.log("时间是" + myhours + "点"+ myminutes + "分" + myseconds + "秒");
```

返回星期的方法：

```javascript
var now = new Date();
var weekday=["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
var mynum = now.getDay();
console.log(mynum);
console.log(weekday[mynum]);
```

### 5. Math对象
Math 对象是一个可以直接使用的对象，他与其他对象的区别在于，String、Date、Number 其实都是函数，都可以当作普通函数、构造函数来用，而 Math 直接就是一个对象。
Math有很多直接可用的方法，比如：

```javascript
console.log(Math.PI);
console.log(Math.abs(-15));
```

#### 5.1 取整方法

* ceil() 向上取整
* floor() 向下取整
* round() 四舍五入

```javascript
console.log(Math.ceil(0.8));
console.log(Math.floor(0.8));
console.log(Math.round(0.8));
```

#### 5.2 随机数
random() 方法可返回介于 0 ~ 1（大于或等于 0 但小于 1 )之间的一个随机数。

```javascript
console.log((Math.random()) * 10);

//输出一个 0 至 10 之间的随机整数
console.log(Math.round((Math.random()) * 10));
```

#### 5.3 最大值最小值

```javascript
console.log(Math.min(0.8, 6.6, 5, 4.5, -5.1, -5.9));
console.log(Math.max(0.8, 6.6, 5, 4.5, -5.1, -5.9));
```

  [1]: https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String
  [2]: https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array
