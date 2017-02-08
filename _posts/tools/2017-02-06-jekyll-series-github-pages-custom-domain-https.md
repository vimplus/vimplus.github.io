---
title: 玩转jekyll系列（三）- 之为GitHub Pages自定义域名配置HTTPS
date: 2017-02-06 18:55:23
description: "玩转jekyll系列（三）- 之为GitHub Pages自定义域名配置HTTPS"
layout: post
categories: jekyll
tags: [jekyll,GitHub-Pages,HTTPS]
comments: true
---
HTTPS 是 HTTP Secure，是一种更安全的 HTTP 协议，目前建议是所有的网络请求都能是 HTTPS 的，像Google，Facebook， Baidu，Taobao等公司，都已经全站启用 HTTPS ，可以在浏览器的地址栏看到一个绿色的锁的标志，而且 Google 会优先选择 HTTPS 网页而不是等效的 HTTP 网页作为规范网址，优先收录。

## 背景知识

> Google宣布了，从2017年1月份正式发布的Chrome 56开始，Google将把某些包含敏感内容的https页面标记为“不安全”。

HTTPS并非是一种新协议，而是对工作在——加密连接（TLS或SSL）上的常规HTTP协议的称呼，因此要使用HTTPS，我们实际上需要的是SSL或TLS服务。

**HTTP+加密+认证+完整性保护 = HTTPS**

更多知识请参考：[HTTP和HTTPS的区别][1]

## 选用方案
免费的SSL服务有很多，比如[Let’s Encrypt][2]，提供免费、自动化、开放的证书签发服务，得到了诸如Mozilla等众多知名互联网公司和机构的支持。
但是 Github Pages 不支持上传证书，且无法配置证书文件，所以无论你是 Jekyll，还是 Hexo，即使申请购买到了 HTTPS 的证书也无法使用。所以如果想要给你的网站配置 HTTPS ，就不能使用一般的静态证书，只能在 DNS 域名解析的时候给你提供一个动态的 HTTPS 证书。

> 那么我们可以采用的方案就是：[Cloudflare][3]

使用 Cloudflare 的 DNS 域名解析服务，并绑定动态 HTTPS ， 即不需要申请证书，也不用保存证书，所有的服务都是在 DNS 那里动态的加载 HTTPS ，而且更重要的是，这一切都是免费的，你可以在地址栏里看到我的网址前面有一个绿色的锁。

## 概述
1、在 github page 绑定自己的域名，参照上一节；
2、当然是注册Cloudflare账号，点击[这里注册][4]；
3、在 Cloudflare中添加你的域名，设置`2`个`A记录`和`1`个`CNAME记录`；
4、去你的域名注册商更改 DNS Server 成 Cloudflare 所提供的；
5、在 Cloudflare 中配置 Crypto ，选择 Full （这一步要一段时间才能起效）
6、在 Cloudflare 配置 Page Rules ，一个是 always use https ，一个是 redirect http 到 https 每一步的操作可能需要 5-30 分钟才能起效


## 开始
前面的2步自行完成，我们从第三步开始：

### 添加域名，设置解析记录

* 登录Cloudflare后，在这里 [添加][5] 你的域名，如下图，输入你的域名，例如 thinktxt.com 并点击`Begin Scan`开始扫描；

    ![image_1b8bkej1j1rva160r1vsqo3i1oqd9.png-76.5kB][6]
* 大约60秒即可完成域名解析扫描。完成后点击 `Continue Setup` 继续下一步；
* 看到DNS记录（包括子域）列表之后，按照下图提示设置后，点击 `Continue` 下一步（其中cname是为了重定向www准备的，彩色云朵表示Cloudflare的SSL）

    ![image_1b8bkn127vqd1m4pk9h1154cpsm.png-47.9kB][7]
* 选择免费服务计划，然后点击下一步

    ![image_1b8bl3r171n3o1n4o1n3413gljgm13.png-90.2kB][8]

### 更改DNS Server

* 完成上面的步骤后，到你的域名控制面板修改DNS服务；
  这里我以万网为例，找到你的域名，在该域名`管理`中选择`DNS修改/创建`，如下图：

    ![image_1b8blf9521li1jgl11fotgb1nsk1t.png-42.1kB][9]

* 在万网修改好DNS之后，在Cloudflare点击继续，如下图：

    ![image_1b8blcf4d1uuul5j171l1d0i1f921g.png-44.1kB][10]

注：官方说域名服务器修改最长需要72小时生效，根据我的经验事实上速度还是蛮快的，大约需要 5~30 分钟，显示 `Status: Active` 即可。
![image_1b8blt4kdfhc1v0c1r5f67n119v2a.png-32kB][11]

### 设置SSL
点击 Crypto 菜单 , 然后设置 Flexible SSL（你也可以保持Full），如下图：
![image_1b8bm0p9t38b1mtn1f551bu61nnp2n.png-57.3kB][12]

### 重定向
点击 Page Rules 菜单 , 然后点击 `Create Page Rule`

* 添加顶级域名重定向到`https://www.thinktxt.com`

    ![image_1b8bmomjc187q17pm17vb966os134.png-70.3kB][13]

* 添加自动使用HTTPS
  强制使用SSL，可以使用通配符`*`
    ![image_1b8bms37rnviqr71c8l1skhlri3h.png-68.6kB][14]

## 完成
完成上面的步骤后，你的博客就已经支持HTTPS啦，一般需要5~30分钟生效！！！
至此，你离装逼的最高境界又近了一步，咳咳~

## 优化

### SEO
网站支持了https，下面我们来加强一下 SEO ，告诉网站爬虫你的站已经全面升级为 HTTPS，不要再爬 HTTP 的站了，那就将下面一行代码添加你的网页 `<head>` 标签中。

```
<link rel="canonical" href=" { { site.url } }{ { page.url } }" />
```

### 多说评论
有些小伙伴的博客可能采用了多说评论，虽然多说评论自身能够支持https，但是头像就不是那么完美了，我采用的方案是这里提供的一个[git项目][15]。详细可以参考：
[多说评论支持HTTPS头像&表情][16]
[巧用七牛https域名,无需反代让多说支持SSL和CDN加速][17]

**解决方案：**
修改你引入的多说代码，将这一行：

```
ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
```

修改为：

```
ds.src = 'https://dn-hb0716.qbox.me/duoshuo.js';
```


  [1]: http://www.jianshu.com/p/37654eb66b58
  [2]: https://letsencrypt.org/
  [3]: https://www.cloudflare.com/
  [4]: https://www.cloudflare.com/a/sign-up
  [5]: https://www.cloudflare.com/a/add-site
  [6]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020501.jpg
  [7]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020502.jpg
  [8]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020503.jpg
  [9]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020504.jpg
  [10]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020505.jpg
  [11]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020506.jpg
  [12]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020507.jpg
  [13]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020508.jpg
  [14]: https://thinktxt.static.lxyour.com/article/github_custom_domain_https_2017020509.jpg
  [15]: https://github.com/rainwsy/duoshuo-https
  [16]: https://www.tiexo.cn/duoshuo-https/
  [17]: https://quericy.me/blog/788/
