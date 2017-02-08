---
title: JavaScript正则表达式基础知识笔记
date: 2017-02-04 19:22:21
description: "JavaScript正则表达式基础知识笔记"
layout: post
categories: RegExp
tags: [RegExp,正则表达式]
comments: true
---
正则表达式一直给人的感觉是很强大、很难学、记不住，本文借助图形工具感受正则表达式，用通俗易懂的方式理解正则表达式，并记录学习笔记。

## 学习目标

* 了解正则表达式语法
* 在IDE中使用正则表达式处理规则复杂的字符串查找、替换需求
* 在JavaScript中使用正则表达式处理字符串

## 正则表达式简介

Regular Expression，即`正则表达式`。使用**单个字符串来描述**、匹配一系列符合**某个语法规则**的字符串。

简单来说就是：

> 按照某种规则去匹配符合条件的字符串。

比如：查找当前目录下所有的txt文本文档
```
find ./ -name *.txt
```

几乎任何计算机语言都可以使用正则表达式，只不过是不同的语言使用的方式稍微有点不同而已。

## 工具使用

### regexper
在线显示正则表达式的图形工具：[regexper官网][1]
无法访问官网的时候可以在本地搭建regexper，通过下载源码，然后按照官方文档构建。
官网源码：[https://github.com/javallone/regexper-static][2]

### IDE中使用正则
1、将`is`这个单词替换成`IS`
在Brackets中, 使用快捷键`Command + option + F`，再点击`.*`，这样就可以在查找或替换的时候使用正则表达式。

待处理字符串：

```
This is dog.
That is pig.
There isn't any cat here.
```

在输入框中输入：
![image_1b81m24vu9n1ree139m13r8uvn9.png-18.9kB][3]

正则表达式图形表达：![image_1b81m8kj91ak971o1pb8k7111eam.png-7.4kB][4]

成功处理字段：

```
This IS dog.
That IS pig.
There isn't any cat here.
```

2、去掉http协议的jpg文件协议头

```
http://www.baidu.com/abc.jpg
http://www.baidu.com/abc.png
https://www.baidu.com/abc.jpg
```
在输入框中输入：`http:\/\/(.+\.jpg)`
如图：
![image_1b81neubcnm4psgg301duvaq13.png-27kB][5]
处理后：

```
www.baidu.com/abc.jpg
http://www.baidu.com/abc.png
https://www.baidu.com/abc.jpg
```

正则表达式图形表示：
![image_1b81ni3q61b41ar861bkt2gi21g.png-11.9kB][6]

**备注：**
注意符号`/`要使用`\`来转义，即`\/`
`.` 表示any character，**任意字符**
`+`表示**不限量**
`()`内是第一个**分组**

3、日期翻转
例如：将`2016/12/15`换成`15-12-2016`

```
2016/12/15
test/03/25
2017-02-03
2018/05/20
23424/332/234568
1234/23/23456
123456/45/36
```
在输入框输入：`^(\d{4})[/-](\d{2})[/-](\d{2})$`
如图：
![image_1b81p0m8t1n2b1cdu1llc1f9r1smm1t.png-35.7kB][7]
正则表达式图形：
![image_1b81p2s7itei55lf81d0p15me2a.png-29kB][8]

## JS中RegExp对象

我们可以通过两种方法实例化RegExp对象，即 **字面量** 和 **构造函数**。

1. 字面量

```
var reg = /\bis\b/g;
'He is a boy.This is a dog'.replace(reg,'IS');
```
运行示例：
![image_1b826nekn12q91o3vln319acb7t2n.png-20kB][9]

2. 构造函数

```
var reg = new RegExp('\\bis\\b','g');
'He is a boy.This is a dog'.replace(reg,'IS');
```
备注： `\`要转义。

## 正则基本语法

### 元字符

正则表达式由两种基本字符类型组成：

* 原意文本字符
* **元字符**
  元字符是在正则表达式中有特殊含义的**非字母字符**：`*+?$^.|(){}[]`

| 字符 |	含义  |
| ---  |  ---      |
| \t   |	水平制表符 |
| \v   | 垂直制表符  |
| \n  | 	换行符  |
| \r  | 	回车符 |
| \0 | 	空字符null |
| \f | 	换页符 |
| \cX | 与X对应的控制字符（Ctrl+X） 如：`\cZ` 则最对应（Ctrl+Z） |

### 字符类

* 一般情况下正则表达式一个字符对应字符串一个字符
  例如：表达式`ab\t`的含义是![image_1b8276bse56q1hd445219vr6mr34.png-4.6kB][10]

* 我们可以使用元字符`[]`来构建一个简单的类

  所谓类是指符合某些特性的对象，一个泛指，而不是特指某个字符表达式[abc]，即把字符a或b或c归为一类，表达式可以匹配这类的字符。
  简单来说`[]`有点类似于`或者`的意思。

* 字符类取反：`[^abc]`
![image_1b827hgihuna5q017qg189jodu3h.png-22kB][11]

### 范围类

* `[a-z]` --- 闭区间
* `[a-zA-Z]` --- 可连写

示例：
![image_1b827qt8j1gp215m58m3qq51vpl3u.png-48.7kB][12]

### 预定义类

* 预定类

|  字符  |  	等价类	| 含义   |
| ---    |   ---      |   ---   |
|  .	|  [^\r\n]  |	除了回车符和换行符之外的所有字符   |
|  \d  |  	[0-9]	| 数字字符   |
|  \D  |  	[^0-9]	| 非数字字符   |
|  \s  |  	[\t\v\f\r\n]  |	空白符   |
|  \S  |  	[^\t\v\f\r\n]  |	非空白符   |
|  \w  |  	[a-zA-Z_0-9]  |	单词字符（包含字母、数字、下划线）   |
|  \W  |  	[^a-zA-Z_0-9]  |    非单词字符   |

备注：空白符为`[ \t\n\x0B\f\r]`，空字符为`\0`，\0代表查找`NULL`字符

示例：

```
var reg = /\0/;
reg.test('\0');  //true
reg.test(''); //false
reg.test(' ');  //false
```

* 边界

| 字符  |  含义  |
|  ---  |  ---   |
|   ^   |  开始符，以xxx开始  |
|   $   |  结束符，以xxx开始  |
|   \b   |  单词边界  |
|   \B   |  非单词边界 |

举例：

* `\b`与`\B`的使用

    ![image_1b83uv7ljb4c14mp1gfcihs10p14b.png-32.6kB][13]

* `^`与`$`的使用

    ![image_1b83v8fldpcp1o3p1r2u1i4i18hg4o.png-39kB][14]

* 多行匹配
    `/m`影响的是`^$`的分割方式

    ![image_1b83vmu1m16tm1h6ha8i1hv11ej755.png-30.7kB][15]

### 量词
我们希望匹配一个连续出现20次数字的字符串，原本可能是这样：

```
\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d
```
但是如果要匹配上百上千，甚至更多就尴尬了。
我们可以通过特殊的字符来表示数量：

| 字符  |  含义  |
|  ---  |  ---   |
|  ?    |  0次或者1次（最多一次） |
|  +    |  1次或者1次以上（最少一次） |
|  *    |  0次或者多次（任意次数） |
|  {n}    | 出现n次 |
|  {n,m}    | 出现n到m次 |
|  {n,}    | 至少出现n次，出现n次以上 |
|  {0,m}    | 最多出现m次 |

示例：`\d?\d+\d*\d{2}\d{2,10}\d{2,}\d{0,10}`
![image_1b8408ogh16is11hb1mau11dq1l165i.png-20.4kB][16]


### JS正则贪婪模式和非贪婪模式

* 贪婪模式
  默认情况下，正则表达式默认尽可能多的匹配，量词为`{n,m}`时，正则表达式尽可能多得往`m`匹配
* 非贪婪模式
  让正则表达式尽可能少的匹配，也就是说一旦匹配成功就不在继续尝试。
  做法：在量词`{n,m}`后面加上`?`

    示例：
    ![image_1b8418auv1a6g19dqg2sgsd1r5o5v.png-18.1kB][17]

### 分组

#### 1、分组

使用`()`来实现分组。

比如：
Byron{3}指的是n出现3次；
(Byron){3}指的是Byron出现3次。

图形示例：`/Byron{3}(Byron){3}/`
![image_1b841co04197p3i01j737rk1el36c.png-11.5kB][18]

#### 2、或

使用`|`可以达到或的效果。

比如：Byron|Casper和Byr(on|Ca)sper

```
'ByronCasper'.replace(/Byron|Casper/g, 'X');   //"XX"
'ByronsperByrCasper'.replace(/Byr(on|Ca)sper/g, 'X');   //"XX"
```

图形示例：`/Byr(on|Ca)sper/`
![image_1b8421b581c9s1eeq1rmr1vd8tij6p.png-11.1kB][19]

#### 3、反向引用

使用$符来引用到分组的内容：将2016-12-25转换为12/25/2016

```
'2016-12-25'.replace(/(\d{4})-(\d{2})-(\d{2})/g, '$2/$3/$1');  //"12/25/2016"
```

图形示例：
![image_1b842ls8diljsms1nc37v3jr76.png-22.6kB][20]

#### 4、忽略分组

不希望捕获某些分组。只需要在分组内加上`?:`

图形示例：`/(?:Byron).(ok)/`
![image_1b842tom39j31tg5p92ilp1jag7j.png-9.4kB][21]

### 前瞻

* 前瞻就是正则表达式匹配到规则的时候，向前检查是否符合断言。“前”指的是从文本 **头** 部到文本 **尾** 部的方向
* 后顾和前瞻方向相反，javascript中不支持后顾。
* 符合断言称为正向匹配或肯定匹配；不符合断言称为负向匹配或否定匹配
  比如: `\w(?=\d)`，()内的为断言部分，并不参与规则部分，在替换的时候也不会被匹配到

| 名称  |  正则  |  说明  |
|  ---  |  ---   |  ---   |
|  正向前瞻  |  exp(?=asset)  | |
|  负向前瞻  |  exp(?!asset)  | |
|  正向后瞻  |  exp(?<=asset)  | JS不支持 |
|  负向后瞻  |  exp(?<!asset)  | JS不支持 |

示例：
![image_1b843utm3adnis6qbrk0f17bm8d.png-40.3kB][22]

## RegExp对象属性

* global ：全局匹配，默认值为false
* ignoreCase ：忽略大小写，默认值为false
* multiline ：多行匹配，默认值为false
* lastIndex ：当前表达式匹配内容中最后一个字符的下一个位置
* source ：正则表达式的文本字符串

  演示示例：
  ![image_1b845kaf513insr31jdjt58i669k.png-24.9kB][23]

  备注：global、ignoreCase、multiline为只读。
  示例：
  ![image_1b844ujhg18kr1c081ciql1onv8q.png-33.8kB][24]

## test方法和exer方法

### test()
> RegExp.prototype.test(str);

用于`测试`字符串参数中是否存在匹配正则表达式模式的字符串。
![image_1b8462f6ausl1ns412p59b413q0a1.png-52.4kB][25]

可以发现，在全局调用下，即对于reg2，在第三次test匹配时出现了false，这是因为在全局调用下lastIndex不为0。
我们可以通过每次都实例化reg2可以使test匹配时不出现false，但这样**花费内存开销**。如下：
![image_1b84652ghu861n3m7vv1dho1qqaae.png-16.8kB][26]

**总结：** **当我们想用到test本义时（只想测试有没有匹配上），不用加上标识符`g`来进行全局匹配**

### exec()

> RegExp.prototype.exec(str);

* 使用正则表达式模式对字符串执行搜索，并将更新全局RegExp对象的属性以反映匹配结果
* 如果没有匹配的文本则返回null，否则返回一个结果数组：
    - index 声明匹配文本的第一个字符位置
    - input 存放被检索的字符串string

**两种调用方式：**

* **非全局调用**

> 调用非全局的RegExp对象的exec()时，返回数组。

* 第一个元素是与正则表达式相匹配的文本
* 第二个元素是与RegExpObject的第一个子表达式相匹配的文本（如果有的话）
* 第三个元素是与RegExpObject的第二个子表达式相匹配的文本（如果有的话），以此类推
* 在非全局调用下，**lastIndex不生效**，会被正则忽略，默认为0；

示例：
![image_1b847jrht2pm1c031f6dnk1mucar.png-45.5kB][27]

* **全局调用**

    > 与非全局调用类似，不同的是**lastIndex生效**

    示例：
    ![image_1b847to5m1m631miu2jksfbvi8b8.png-55.4kB][28]

## JS字符串对象方法

### search()

> String.prototype.search(reg)

* search()方法用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串
* 该方法返回第一个匹配结果的index，查找不到返回-1；
* search()方法不执行全局匹配，它将`忽略g`，并且总是从字符串的开始进行检索

备注：对于字符串或数字，search()方法会尝试转化为正则表达式
示例：
![image_1b849jkrt1v3mc2n1l6mitekqibl.png-24.5kB][29]

### match()
> String.prototype.match(reg)

* match()方法将检索字符串，用来查找 **一个或多个** 与regexp匹配的文本。
* RegExp是否具有`g`标识对结果影响很大

**两种调用方式：**

* **非全局调用**

    * 如果regexp没有标志g，那么match()方法就只能在字符串中执行一次匹配：
    (1) 如果没有找到任何匹配的文本，将返回null；
    (2) 否则它将返回一个数组，其中存放了与它找到的匹配文本有关的信息
    * 返回数组的第一个元素存放的是匹配文本，而其余的元素存放的是与正则表达式的子表达式匹配的文本
    * 除了常规的数组元素之外，返回的数组还含有2个对象属性：
    (1) index声明匹配文本的起始字符在字符串的位置（返回位置）；
    (2) input声明对stringObject的引用（返回该字符串）

    示例：
    ![image_1b84ai8eo33h10eb148k1sicknvc2.png-45.9kB][30]

    备注：与`exec()`的非全局调用方法类似，只不过：
    `match()`方法是`String.prototype.match(reg)`；
    `exec()`方法是`RegExp.prototype.match(str)`；
* **全局调用**
    * 如果regexp具有`g`标识，则match()方法将执行全局检索，找到字符串中的所有匹配子字符串：
    (1) 没有找到任何匹配的字串，则返回null；
    (2) 如果找到了一个或多个匹配字串，则返回一个数组；
    * 数组元素中存放的是字符串中所有的匹配子串，而且也 **没有index属性或input属性**

    示例：
    ![image_1b84ap7fg17hte2f1trq22n18rncf.png-48.9kB][31]

### split()

> String.prototype.split(reg);

`split()`方法使用字符串或正则表达式来将原字符串分割成字符数组。
示例：

```
'a,b,c,d'.split(',');   //["a", "b", "c", "d"]
'a,b,c,d'.split(/,/g);  //["a", "b", "c", "d"]
'a1b2c3d'.split(/\d/g); //["a", "b", "c", "d"]
```

备注： split()方法将字符串转换为对应正则表达式

### replace()
> String.prototype.replace

3种用法：

* String.prototype.replace(str,replaceStr)
* String.prototype.replace(reg,replaceStr)
* String.prototype.replace(reg,function)
    * `function`会在每次匹配替换的时候调用，有四个参数：
        * 匹配字符串 (match)
        * 正则表达式分组匹配到的内容，没有分组则没有该参数 (group1, group2……)
        * 匹配项在字符串中的index (index)
        * 原字符串 (origin)
示例：
无分组：
![image_1b84c1tgi1g191r461g6v6n46o7cs.png-42.6kB][32]
有分组：
![image_1b84d8kiv101f5p71jk111n1mr7d9.png-46.1kB][33]



  [1]: https://regexper.com/
  [2]: https://github.com/javallone/regexper-static
  [3]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020501.jpg
  [4]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020502.jpg
  [5]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020503.jpg
  [6]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020504.jpg
  [7]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020505.jpg
  [8]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020506.jpg
  [9]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020507.jpg
  [10]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020508.jpg
  [11]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020509.jpg
  [12]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020510.jpg
  [13]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020511.jpg
  [14]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020512.jpg
  [15]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020513.jpg
  [16]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020514.jpg
  [17]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020515.jpg
  [18]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020516.jpg
  [19]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020517.jpg
  [20]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020518.jpg
  [21]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020519.jpg
  [22]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020520.jpg
  [23]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020521.jpg
  [24]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020522.jpg
  [25]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020523.jpg
  [26]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020524.jpg
  [27]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020525.jpg
  [28]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020526.jpg
  [29]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020527.jpg
  [30]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020528.jpg
  [31]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020529.jpg
  [32]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020530.jpg
  [33]: https://thinktxt.static.lxyour.com/article/regexp_base_2017020531.jpg
