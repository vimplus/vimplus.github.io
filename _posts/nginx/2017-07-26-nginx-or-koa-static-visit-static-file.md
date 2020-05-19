---
title: 利用Nginx或koa-static托管静态文件
date: 2017-07-26 20:36:21
description: "利用Nginx或koa-static托管静态文件"
layout: post
categories: Nginx
tags: [nginx,koa-static,静态资源]
comments: true
pay: true
---

最近在做上传的图片的需求，思考上传之后的图片怎么访问的问题，因为后端是Node，一开始尝试写一个专门的接口通过传入图片的path来查找，试了一下感觉并不理想，因为要为每种类型的文件设置`Content-Type`，不然浏览器会直接下载该文件。

## koa-static方案

后端框架因为使用的是koa，采用`koa-static`实现如下:

```javascript
import staticServer from 'koa-static';

app.use(staticServer(__dirname, '/upload'));
```

假如`upload`目录中有`logo.png`文件，就可以通过URL`http://cms.thinktxt.com/logo.png`访问到。

## Nginx方案

Nginx天生擅长托管静态资源，最终选用的方案是通过Nginx托管，这样还可以解放Node的服务压力，配置如下：

```nginx
server {
    listen          80;
    server_name     cms.thinktxt.com;

    location / {
        proxy_pass  http://127.0.0.1:8080;
        client_max_body_size    1000m;
    }

    location /images {
        root e:/WorkSpace/Thinktxt-CMS/upload/;
    }
}
```

假如`upload`目录下的`images`目录中有`logo.png`文件，就可以通过URL`http://cms.thinktxt.com/images/logo.png`访问到。

如果别的别的系统想要访问该站点目录下的资源，也可以做转发：

```nginx
server {
    listen          80;
    server_name     static.thinktxt.com;

    location /images {
        proxy_pass http://cms.thinktxt.com/images;
    }
}
```
