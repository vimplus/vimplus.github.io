---
title: moment常用示例大全
date: 2017-11-07 12:15:21
description: "moment常用示例大全"
layout: post
categories: JavaScript
tags: [JavaScript,moment]
comments: true
pay: true
---
`moment`是一个功能非常强悍和全面的JavaScript日期、时间处理工具类，可以用在浏览器环境中使用，也可以在Node.js中。在`IE8`以上及其它浏览器的最新版本中都可以使用，具有良好的跨浏览器及跨系统的兼容性。

## 安装

moment支持多种安装方式，每一种方式都非常的方便。

### 在Node.js中安装使用

在`Node.js`中通过`npm`安装后，`require`引用即可，如：

```shell
npm install moment -S
```

#### 引入使用

```javascript
const moment = require('moment');
// or 
import moment from 'moment';

moment().format();
```

### 在浏览器中使用

```javascript
<script src="https://cdn.bootcss.com/moment.js/2.19.0/moment.min.js"></script>
<script>
    moment().format();
</script>
```

### 通过Bower安装

```shell
bower install --save moment
```

## 常用示例

### 设置全局语言 

默认的语言是: `moment.locale('en');`

```javascript
moment.locale('zh-CN');
```

### 当前时间

```javascript
var now = moment().format('YYYY-MM-DD HH:mm:ss');
console.log('------now:', now);     // now: 2017-11-06 15:25:36
```

### 将时间转化为时间戳

```javascript
var timestrapA = moment('2017年11月25日', 'YYYY年MM月DD日').format('X');
var timestrapB = moment('2017年11月25日', 'YYYY年MM月DD日').format('x');
console.log('------timestrapA:', timestrapA);   // timestrapA: 1511539200
console.log('------timestrapB:', timestrapB);   // timestrapB: 1511539200000
```

### 将时间转化为时间戳

```javascript
var timestrapA = moment('2017年11月25日', 'YYYY年MM月DD日').format('X');
var timestrapB = moment('2017年11月25日', 'YYYY年MM月DD日').format('x');
console.log('------timestrapA:', timestrapA);   // timestrapA: 1511539200
console.log('------timestrapB:', timestrapB);   // timestrapB: 1511539200000
```

### 往前推一天

相关的单位有: `years、month、days、hours、minutes、seconds`

```javascript
var offset1 = moment().subtract(1, 'days').format('YYYY-MM-DD');
var offset1A = moment().add(-1, 'days').format('YYYY-MM-DD');
console.log('------往前推一天:', offset1);    // 往前推一天: 2017-11-05
console.log('------往前推一天:', offset1A);   // 往前推一天: 2017-11-05
```

### 指定日期往前推一天

```javascript
var offset2 = moment('2017年11月25日', 'YYYY年MM月DD日').subtract(1, 'days').format('YYYY年MM月DD日');
var offset2A = moment('2017年11月25日', 'YYYY年MM月DD日').add(-1, 'days').format('YYYY年MM月DD日');
console.log('------指定日期往前推一天:', offset2);           // 指定日期往前推一天: 2017年11月24日
console.log('------指定日期往前推一天:', offset2A);           // 指定日期往前推一天: 2017年11月24日
console.log(`------指定日期往前推一天:${offset2} 23:59:59`);    // 指定日期往前推一天: 2017年11月24日
```

### 7天后

```javascript
var offset3 = moment().add(7, 'days').format('YYYY年MM月DD日');
console.log('------7天后:', offset3);     // 7天后: 2017年11月13日
```

### 6小时后

```javascript
var offset4 = moment().add(6, 'hours').format('HH:mm:ss');
console.log('------6小时后:', offset4);    // 6小时后: 21:25:49
```

### 相对时间

```javascript
var relative5 = moment("2015年10月10日", "YYYY年MM月DD日").fromNow();
console.log('------相对时间:', relative5);    // 相对时间: 2 年前
```

### 转换格式

```javascript
var transition = moment('2017/11/25', 'YYYY/MM/DD').format('YYYY年MM月DD日');
console.log('------转换格式:', transition);    // 转换格式: 2017年11月25日
```

### 时间戳转日期

```javascript
var format1 = moment(1510022715393).toDate();
var format2 = moment(1510022715393).format('YYYY-MM-DD HH:mm:ss');
console.log('------时间戳转日期-format1:', format1);    // 2017-11-07T02:45:15.393Z
console.log('------时间戳转日期-format2:', format2);    // 2017-11-07 10:45:15
```

经常用到的好像就是这些吧，希望能给你带来帮助，更多的接口和参数大家自行翻阅[官方文档](https://momentjs.com/)吧。

## 相关参数文档

**年、月、日，标识符**

| 输入         | 示例               | 说明            |
| ---------- | ---------------- | ------------- |
| `YYYY`     | `2014`           | 4或2位年         |
| `YY`       | `14`             | 2位年r          |
| `Q`        | `1..4`           | 季度。设置每季度的第一个月 |
| `M MM`     | `1..12`          | 表示月的数字        |
| `MMM MMMM` | `Jan..December`  | 月份名           |
| `D DD`     | `1..31`          | 每月的第几天        |
| `Do`       | `1st..31st`      | 每月的第几天的序数     |
| `DDD DDDD` | `1..365`         | 每年的第几天        |
| `X`        | `1410715640.579` | Unix时间戳       |
| `x`        | `1410715640579`  | Unix时间戳（毫秒级）  |

**周年、周、周日，标识符**

| 输入         | 示例             | 说明          |
| ---------- | -------------- | ----------- |
| `gggg`     | `2014`         | 本地 4位周年     |
| `gg`       | `14`           | 本地 2位周年     |
| `w ww`     | `1..53`        | 本地 年中第几周    |
| `e`        | `1..7`         | 本地 一周中的第几天  |
| `ddd dddd` | `Mon...Sunday` | 本地星期名       |
| `GGGG`     | `2014`         | ISO 4位周年    |
| `GG`       | `14`           | ISO 2位周年    |
| `W WW`     | `1..53`        | ISO 年中第几周   |
| `E`        | `1..7`         | ISO 一周中的第几天 |

**时、分、秒、毫秒、时差，标识符**

| 输入     | 示例           | 说明                                  |
| ------ | ------------ | ----------------------------------- |
| `H HH` | `0..23`      | 24 小时制 时                            |
| `h hh` | `1..12`      | 12 小时制 时`a A`.                      |
| `a A`  | `am pm`      | 上午和下午                               |
| `m mm` | `0..59`      | 分                                   |
| `s ss` | `0..59`      | 秒                                   |
| `S`    | `0..9`       | 十分之一秒                               |
| `SS`   | `0..99`      | 百分之一秒                               |
| `SSS`  | `0..999`     | 千分之一秒（毫秒）                           |
| `SSSS` | `0000..9999` | 微秒                                  |
| `Z ZZ` | `+12:00`     | 与UTC时间的时差，用`+-HH:mm`、`+-HHmm`或`Z`表示 |

## 拓展阅读

[官方中文文档](http://momentjs.cn/)


