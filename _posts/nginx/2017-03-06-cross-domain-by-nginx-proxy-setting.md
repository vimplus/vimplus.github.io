---
title: 通过 Nginx 代理转发配置实现跨域（API代理转发）
date: 2017-03-06 12:45:21
description: "通过 Ngin 代理转发配置实现跨域（API代理转发）"
layout: post
categories: Nginx
tags: [nginx,代理,跨域,API转发]
comments: true
pay: true
---
在WEB开发中，我们经常涉及到跨域的请求，解决跨域问题的方式有很多，比如有`window.name`、`iframe`、`JSONP`、`CORS`等等，就不详细展开了，涉及到 **协议**、**端口** 不一样的跨域请求方式是采用代理，这里我们重点聊聊Nginx代理的方式。

## 场景

本地启动了一个前后端分离的WEB应用，端口为：`3000`，可以通过`http://127.0.0.1:3000`访问前端页面，页面中有些Ajax请求的地址为`http://127.0.0.1:3000/api/getList`，一般情况下肯定是404或者请求失败，如下图：

![API请求404][1]

这种后端服务的接口存放在于其他的服务器中，比如在公司内网可以通过`http://172.30.1.123:8081/api/getList`访问到测试环境中的服务接口。

这种情况的请求就涉及到端口不一样的跨域了，那么我们可以利用Nginx代理请求。

## Nginx代理配置参考
首先找到Nginx配置文件：

* Windows下路径就是你安装Nginx目录下找，比如我的放在C盘根目录，那就是：`c:\nginx\conf\nginx.conf`
* Mac系统配置文件路径在: `/usr/local/etc/nginx/nginx.conf`, Finder下通过`Shift+Command+G`，输入`/usr/local/etc/nginx/`进入该目录。

在Nginx配置文件中添加如下配置：

```nginx
server {
    listen  80;
    server_name 127.0.0.1;

    location / {
        proxy_pass  http://127.0.0.1:3000;
    }

    location ~ /api/ {
        proxy_pass  http://172.30.1.123:8081;
    }
}
```

上面的配置的可以理解为：

> 监听80端口（Nginx默认启动了80端口），将`http://127.0.0.1`的所有请求服务转发到`127.0.0.1`端口为`3000`；
> 将`http://127.0.0.1/api/`或者`http://127.0.0.1/api/getList`请求转发到`http://172.30.1.123:8081`

## 完成

经过上面的配置我们可以直接通过`http://127.0.0.1`访问我们的WEB应用（如果采用IP访问），而相关的API请求也会根据我们的Nginx配置进行相应的请求，浏览器端看到的`/api/getList`请求的是127.0.0.1端口为80的端口，但是实际上这个请求已经被我们的Nginx转发指向`http://172.30.1.123:8081/api/getList`

**优化：**

> 基本的代理功能就像上面如此简单的配置即可。
>
> 但是，当我们需要获取真实IP的业务时，还需要添加关于真实IP的配置，如下：

```nginx
server {
    listen  80;
    server_name 127.0.0.1;

    location / {
        proxy_pass  http://127.0.0.1:3000;
    	proxy_set_header Host $host:80;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location ~ /api/ {
        proxy_pass  http://172.30.1.123:8081;
    	proxy_set_header Host $host:80;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

`proxy_set_header`这个配置是改变`HTTP`的**请求头**，而`Host`是请求的主机名，`X-Real-IP`是请求的真实IP，`X-Forwarded-For`表示请求是由谁发起的。

>  因为我们的Nginx在这里属于代理服务器，通过`proxy_set_header`配置这些信息目的是让服务端获取到真实的请求头。

**友情提示：**

> Nginx每一条配置语句后面都必须要加分好`;`  否则会报配置错误，自己还一脸懵逼。

## 拓展

### 绑定host

如果你觉得输入IP访问不爽那你可以自己修改host，推荐host修改神器：[SwitchHosts][2]。
**host修改参考：**

```
127.0.0.1 www.domain.com  #改成你需要的任何域名
```

如果绑定了host，在Nginx配置中当然也可以直接配置你指定的域名，譬如：

```nginx
server {
    listen  80;
    server_name www.domain.com;  #这里将IP改成你的域名
    #...
}
```

修改host后你可以直接通过你的域名访问，如：`http://www.domain.com`

### 关于location

上面的配置你可能会对`localtion`后面的配置感到疑惑，关于`localtion`后面的常用的需求有：

```nginx
localtion / {
    # 所有请求都匹配以下规则
    # 因为所有的地址都以 / 开头，所以这条规则将匹配到所有请求
    # xxx 你的配置写在这里
}

location = / {
    # 精确匹配 / ，后面带任何字符串的地址都不符合
}

localtion /api {
    # 匹配任何 /api 开头的URL，包括 /api 后面任意的, 比如 /api/getList
    # 匹配符合以后，还要继续往下搜索
    # 只有后面的正则表达式没有匹配到时，这一条才会采用这一条
}

localtion ~ /api/abc {
    # 匹配任何 /api/abc 开头的URL，包括 /api/abc 后面任意的, 比如 /api/abc/getList
    # 匹配符合以后，还要继续往下搜索
    # 只有后面的正则表达式没有匹配到时，这一条才会采用这一条
}
```

* 以`/` 通用匹配, 如果没有其它匹配,任何请求都会匹配到
* `=`开头表示精确匹配
    如 A 中只匹配根目录结尾的请求，后面不能带任何字符串。
* `^~` 开头表示uri以某个常规字符串开头，不是正则匹配
* `~` 开头表示区分大小写的正则匹配;
* `~*` 开头表示不区分大小写的正则匹配

更多详细localtion的正则匹配规则可参考：[nginx配置location总结及rewrite规则写法][3]

## 后记

笔者也是Nginx的初级使用者，希望通过通俗易懂的方式记录这些知识，分享给有需要的人，一起钻研学习，如有纰漏，欢迎指正，谢谢！


[1]: https://ww3.sinaimg.cn/large/006tNc79gy1fden48rih7j30j6084myh.jpg
[2]: https://github.com/oldj/SwitchHosts
[3]: https://segmentfault.com/a/1190000002797606
