---
title: HTML5 Application Cache离线缓存应用实践
date: 2017-04-01 18:45:21
description: "HTML5 Application Cache离线缓存应用实践"
layout: post
categories: WEB-Cache
tags: [Cache,Application Cache,离线存储]
comments: true
pay: true
---

HTML5的新增了很多浏览器本地存储的技术，Application Cache（简称 AppCache）使得基于web的应用程序可以离线运行，似乎是为支持 Web App 离线使用而开发的缓存机制。它的缓存机制类似于浏览器的缓存（Cache-Control 和 Last-Modified）机制，都是以文件为单位进行缓存，且文件有一定更新机制。但 AppCache 是对浏览器缓存机制的补充，不是替代。

## 离线存储的作用

* 离线浏览: 用户可以在离线状态下浏览网站内容。
* 更快的速度: 因为数据被存储在本地，所以速度会更快。
* 减轻服务器的负载: 浏览器只会下载在服务器上发生改变的资源。

## 如何应用

>  通过在站点根目录维护一个manifest文件，在需要缓存的html页面中引入这个文件。

`manifest `文件是简单的文本文件，它告知浏览器被缓存的内容（以及不缓存的内容），支持manifest的浏览器，会将按照`manifest`文件的规则，将文件保存在本地，从而在没有网络链接的情况下，也能访问页面。

## 实践示例

### manifest文件结构

假如我们在根目录下新建一个名为`manifest.appcache`的文件（该文件名和后缀名后可以自定义），配置内容如下：

```
CACHE MANIFEST
# version 1.0.0  以 # 声明注释，浏览器根据manifest文件变化来检测是否需要重新加载新文件。
# 注释：需要缓存的文件，无论在线与否，均从缓存里读取
/images/cached.png
/css/cached.css
/js/cached.js

# 需要特殊声明的缓存文件，也可以都在这里声明
CACHE:
/css/otherCached.css
/js/otherCached.js

# 注释：不缓存的文件，无论缓存中存在与否，均从新获取
NETWORK:
*

# 注释：获取不到资源时的备选路径，如index.html访问失败，则返回404页面
FALLBACK:
index.html 404.html
```

* 1、`CACHE MANIFEST` --- 文件开头第一行必须声明 `CACHE MANIFEST` 字段标识，然后紧接着声明需要缓存的文件路径，作用是标识出哪些文件需要缓存，可以是相对路径也可以是绝对路径；
* 2、`# ` --- `#`号开头的是注释，一般会在第二行写个`版本号`，用来在缓存的文件更新时，更改`manifest`的作用，可以是版本号，时间戳或者`md5码`等等；
* 3、`CACHE` --- 我们也可以在`CACHE`下面声明需要缓存的资源路径；
* 4、`NETWORK`可选，这一部分是要直接读取的文件，可以使用通配符 `*` ；
* 5、`FALLBACK`可选，指定了一个后备页面，当资源无法访问时，浏览器会使用该页面。

### HTML引入示例

在文档的 `<html>` 标签中添加 `manifest` 属性，将`manifest.appcache`文件引入:

```html
<!DOCTYPE HTML>
<html manifest="manifest.appcache">
<link rel="stylesheet" href="/css/cached.css"/>
<body>
	<p><img src="/images/cached.png"/></p>
  	<script src="/js/cached.js"></script>
</body>
</html>
```

这样浏览器在读取HTML页面时会将`manifest.appcache`中声明的资源下载并进行离线存储，下次请求直接使用离线存储中的资源，HTTP请求表现为：`200 (from disk cache)`

### 配置服务器

> 一般情况下，manifest 文件需要在web 服务器上配置正确的 `MIME-type`，即 "text/cache-manifest"，才能正常的被浏览器正常请求。

#### Nginx

打开Nginx配置文件目录下的`mine.types`文件，添加如下配置：

```
types {
    text/cache.manifest              manifest;
}
```

#### Apache

> 在 Apache 服务器上，若要设置适用于清单(.appcache)文件的 MIME 类型，可以向根目录或应用的同级目录下的一个 .htaccess 文件中增加 `AddType text/cache-manifest .appcache` 。

## 更新缓存资源

浏览器离线存储缓存机制示意图：

![img](https://ww1.sinaimg.cn/large/006tNbRwgy1fefm6heseij30i205ljrp.jpg)

* 用户初次访问网站，浏览器读取到`<html>`标签中`manifest`属性声明的`manifest.appcache`文件，根据`manifest`文件的内容下载相应的资源并进行离线存储。

  >  以Chrome浏览器为例，会在`Application` - `Application Cache`中展现当前站点已缓存的资源。

  如图：

  ![Markdown](https://ww3.sinaimg.cn/large/006tNbRwgy1fefm6gssb3j30jv0b4gnt.jpg)

* 资源已经离线存储后，用户再次访问时，浏览器就会使用离线的资源加载页面，然后浏览器会对比新的`manifest`文件与旧的`manifest`文件，如果文件没有发生改变，就不做任何操作，如果文件改变了，那么就会重新下载文件中的资源并进行离线存储。

  > 需要注意的是浏览器**下载新的更新资源后并不会立即使用**，需要刷新页面才有效果，我们可以利用JavaScript提供的接口监听浏览器是否更新了资源，如果更新了就通过`window.location.reload`刷新页面或通知用户有更新。


* 离线的情况下，浏览器就直接使用离线存储的资源。

## JavaScript监听更新

监听示例：

```javascript
var appCache = window.applicationCache;
    appCache.onupdateready = function(e) {
    appCache.swapCache();
    window.location.reload();
};
```

关于`window.applicationCache`对象的更多接口信息可参考以下表格内容：

### applicationCache对象

该对象是**window对象**的直接子对象`window.applicationCache`

基类：`DOMApplicationCache`

#### 事件列表

| 事件            | 接口              | 触发条件                                     | 后续事件                                     |
| ------------- | --------------- | ---------------------------------------- | ---------------------------------------- |
| `checking`    | `Event`         | 用户代理检查更新或者在第一次尝试下载manifest文件的时候，本事件往往是事件队列中第一个被触发的 | `noupdate`, `downloading`, `obsolete`, `error` |
| `noupdate`    | `Event`         | 检测出manifest文件没有更新                        | 无                                        |
| `downloading` | `Event`         | 用户代理发现更新并且正在取资源，或者第一次下载manifest文件列表中列举的资源 | `progress`, `error`, `cached`, `updateready` |
| `progress`    | `ProgressEvent` | 用户代理正在下载资源manifest文件中的需要缓存的资源            | `progress`, `error`, `cached`, `updateready` |
| `cached`      | `Event`         | manifest中列举的资源已经下载完成，并且已经缓存              | 无                                        |
| `updateready` | `Event`         | manifest中列举的文件已经重新下载并更新成功，接下来js可以使用[swapCache()](http://www.whatwg.org/specs/web-apps/current-work/multipage/offline.html#dom-appcache-swapcache)方法更新到应用程序中 | 无                                        |
| `obsolete`    | `Event`         | manifest的请求出现404或者410错误，应用程序缓存被取消        | 无                                        |

另外还有一个`error`事件，触发条件如下：

* manifest的请求出现404或者410错误，更新缓存的请求失败；
* 无manifest文件没有改变，但是页面引用的manifest 文件没有被正确地下载；
* 在取manifest列举的资源的过程中发生致命的错误；
* 在更新过程中manifest文件发生变化用户代理会尝试立即再次获取文件。

#### 属性

`status`属性返回缓存的状态

| 可选值  | 匹配常量                   | 描述   |
| ---- | ---------------------- | ---- |
| 0    | `appCache.UNCACHED`    | 未缓存  |
| 1    | `appCache.IDLE`        | 闲置   |
| 2    | `appCache.CHECKING`    | 检查中  |
| 3    | `appCache.DOWNLOADING` | 下载中  |
| 4    | `appCache.UPDATEREADY` | 已更新  |
| 5    | `appCache.OBSOLETE`    | 失效   |

#### 方法

| 方法名         | 描述           |
| ----------- | ------------ |
| update()    | 发起应用程序缓存下载进程 |
| abort()     | 取消正在进行的缓存下载  |
| swapcache() | 切换成本地最新的缓存环境 |

## Webpack中配置自动化

在使用webpack自动化构建的项目中，我们可以利用`appcache-webpack-plugin`这个插件轻松生成`manifest`文件，并将打包的资源路径更新到`manifest`文件中，配置如下：

```javascript
const AppCachePlugin = require('appcache-webpack-plugin');

plugins: [
 	new AppCachePlugin({
        cache: ['otherAsset.png'],
        network: ['*'],  // 除了声明的缓存资源其他都通过网络访问
        fallback: ['index.html', 'error.html'],
        settings: ['prefer-online'],
        exclude: ['file.txt', /.*\.html$/],  // Exclude file.txt and all .html files
        output: '/manifest.appcache'
   })
]
```

## 注意事项

* 已经被缓存的文件，无论在线与否，浏览器均从缓存里读取。
* 如果服务器更新了资源，一定要更新`manifest`文件，并且缓存的文件名也需要做相应的变化，这样新的资源才会被浏览器重新下载并更新到离线存储。如果没有更新`manifest`文件，浏览器将不会下载新的资源，继续使用离线存储中旧的资源。
* 不要对`manifest`文件设置缓存。因为有可能即使你对`manifest`文件进行了更新，但是由于HTTP的缓存规则告诉浏览器本地缓存`manifest`文件还未过期，并不会返回新的`manifest`文件。
* 浏览器在下载`manifest`中的文件时，会一次性下载所有的文件，一旦因为某些原因某一个资源下载失败，会导致所有的资源更新失败，浏览器继续适应旧的资源。
* `<html>` 属性中的manifest文件必须与该HTML页面同源。
* `FALLBACK`中声明的资源必须和`manifest`文件同源。
* 站点中的其他页面即使没有设置`manifest`属性，请求的资源如果在缓存中也从缓存中访问。
* 站点离线存储的容量限制是5M。
