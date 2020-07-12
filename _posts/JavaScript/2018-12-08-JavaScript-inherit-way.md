---
title: JavaScript几种常见的继承方式
date: 2018-12-08 20:15:21
description: "JavaScript继承的几种常用方式"
layout: post
categories: JavaScript
tags: [JavaScript,继承,原型]
comments: true
pay: true
---

**继承就是一个对象可以访问另外一个对象中的属性和方法**。

继承方式有很多，但归根结底在 JavaScript 中是通过**原型**和**原型链**的方式来实现的继承特性。
下面我们来简单归纳几种常见的继承方式以及优缺点。

## 原型链继承（new）

```javascript
function Parent(addr) {
    this.surname = '王';
    this.addr = addr;
}

function Child(name) {
    this.name = name;
}

Child.prototype = new Parent('王家村');
Child.prototype.getName = function () {
    return this.surname + this.name;
}


const person = new Child('小明');
person.getName();
```

缺点：

* 多个实例对引用类型的操作会被篡改。

## 构造函数继承（call）

```javascript
function Parent(addr) {
    this.surname = '李';
    this.addr = addr;
}

function Child(name, surname) {
    Parent.call(this, surname);
    this.name = name;
    this.getName = function () {
        return this.surname + this.name;
    }
}


const person = new Child('小强');
person.getName();
```

缺点：

 * 1. 只能继承父类的实例属性和方法，不能继承原型属性/方法
 * 2. 无法实现复用，每个子类都有父类实例函数的副本，影响性能

## 组合式继承（构造函数 + 原型）

```javascript
function Animal(name, color) {
    this.name = name;
    this.color = color;
    this.foot = 4;
}

function Dog(name, color, age) {
    Animal.call(this, name, color);
    this.age = age;
}

Dog.prototype = new Animal();
Dog.prototype.constructor = Dog;


const dog = new Dog('小黑', '黑色', 3);
```

缺点：

 * 1. 两次调用父级
 * 2. 原型中会存在两份相同的属性/方法

## 原型式继承（模拟ES5中的 Object.create）

```javascript
function object(obj) {
    function F() {}
    F.prototype = obj;
    return new F();
}


const person = {
    name: '张三',
    friends: ['小明', '阿强']
}

const personA = object(person);
personA.name = '小华';
personA.friends.push('小军');

const personB = object(person);
personB.name = '阿珍';
personB.friends.push('小红');
```

缺点：

 * 1.原型链继承多个实例的引用类型属性指向相同，存在篡改的可能。
 * 2.无法传递参数

## 寄生式继承（建立在原型式继承基础上，调用object）

```javascript
function creatAnother(obj) {
    // 通过调用 object() 函数创建一个新对象
    const clone = object(obj);
    // 增强对象
    clone.sayHello = function () {
        console.log('Hello');
    }
    // 返回这个新对象
    return clone;
}
const person = {
    name: '张三',
    friends: ['小明', '阿强']
}

const personA = object(person);
personA.name = '小华';
personA.sayHello();
```

缺点：（同原型式继承）

## 寄生组合式继承(最推荐使用)

最推荐的一种方式，接近完美的继承，也是常见库中采用的方式。

```javascript
function inheritPrototype(superClass, subClass) {
    // 根据父级原型创建[备用prototype对象]
    var prototype = Object.create(superClass.prototype);
    // 替换构造器
    prototype.constructor = subClass;
    // 添加原型
    subClass.prototype = prototype;
}
function Parent() {
    this.name = 'txboy';
    this.play = [1, 2, 3, 4];
    this.fn = function (s) {
        console.log(s);
    }
}

function Child() {
    Parent.call(this);  // 相当于把父级的属性和方法赋给了Child的this上；
    this.type = 'child';
}

// 调用inheritPrototype
inheritPrototype(Parent, Child);
// 或者（以下两行代码同inheritPrototype）
Child.prototype = Object.create(Parent.prototype);
Child.prototype.constructor = Child;

const c = new Child();
```

优点：

* 只调用了一次父级构造函数，避免了创建不必要的、多余的属性。

## 混入方式继承多个对象

```javascript
function MyClass() {
    SuperClass.call(this);
    OtherSuperClass.call(this);
}

// 继承一个类
MyClass.prototype = Object.create(SuperClass.prototype);
// 通过Object.assign混入其他类
Object.assign(MyClass.prototype, OtherSuperClass.prototype);
// 重新指定constructor
MyClass.prototype.constructor = MyClass;
MyClass.prototype.addMethod = function() {
    // doSomething
}
```

## ES6中Class的继承（extends）

```javascript
class Parent {
    constructor(surname) {
        this.surname = surname;
    }
}

class Child extends Parent {
    constructor(surname, name, age) {
        // 实质是先创造父类的实例对象this（所以必须先调用super方法），然后再用子类的构造函数修改this。
        super(surname)
        this.name = name;
        this.age = age;
    }
    getName() {
        return this.surname + this.name;
    }
}

const person = new Child('张', '小明', 18);
```

## 总结

JavaScript的继承方法有很多，从最开始的使用`function`来模拟Java类的语法（如：`new`，`prototype`，`constructor`等），到ES5的`Object.create()`的出现，再到现在ES6的`class`和`extends`语法糖。随着标准的不断提出，也趋向于逐渐更加完善的状态。

不管是哪种方法，归根结底都是**基于原型的继承**，JavaScript的**原型链**是其中的关键所在。

### 函数声明和类声明的区别

函数声明**会提升**，类声明**不会提升**。首先需要声明你的类，然后再访问它，否则会抛出一个`ReferenceError`的错误。

### ES5继承和ES6继承的区别

* ES5的继承实质上是先创建子类的实例对象，然后再将父类的方法添加到this上（Parent.call(this)）.
* ES6的继承有所不同，实质上是先创建父类的实例对象`this`，然后再用子类的构造函数修改`this`。因为子类没有自己的`this`对象，所以必须先调用父类的`super()`方法，否则新建实例会报错。
* ES6 在继承的语法上不仅继承了类的原型对象，还继承了类的静态属性和静态方法


