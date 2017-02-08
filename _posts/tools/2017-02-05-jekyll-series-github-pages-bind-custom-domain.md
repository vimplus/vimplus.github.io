---
title: 玩转jekyll系列（二）之为GitHub Pages博客绑定自定义域名
date: 2017-02-05 15:55:23
description: "玩转jekyll系列（一）之为GitHub Pages博客绑定自定义域名"
layout: post
categories: jekyll
tags: [jekyll,GitHub-Pages,自定义域名]
comments: true
---
在GitHub Pages上搭建好了自己的博客后，你一定也很想绑定自己的域名，毕竟github的二级域名用起来不那么高大上，绑定自己的域名对博客的收录也有很大的帮助，下面就让我们一起来继续捣腾吧。

## 准备
申请好一个自己满意的域名。不会申请？自行百度。

## 绑定域名

## Setting
在你的`username.github.io`仓库设置中添加你的自定义域名。
如图：
![image_1b89e26ml61r1dqs1u1h10vd1ggt1g.png-54.9kB][1]

拉到下面一点，添加自己的域名，比如我的：
![image_1b89e5sp01c2t167mbhp174i11f01t.png-23.3kB][2]

### CANME

* 1、在你的仓库根目录创建一个名为`CNAME`的文件。
* 2、在`CNAME`中添加你的域名，比如我的`www.thinktxt.com`。
* 3、推送到你的`username.github.io`仓库。

### DNS解析
将你的域名DNS解析到GitHub，具体操作如下：

* 设置两个 **CANME记录**，一个顶级(@)：`example.com` 和一个www: `www.example.com`，都指向`username.github.io`

* 如果你的域名解析商不支持CANME记录解析到顶级域名，则配置两个 **A记录** 分别指向：
    - A记录 —— `192.30.252.153`
    - A记录 —— `192.30.252.154`

* 配置顶级域名的话同时还要给`www.example.com`子域名配置一个CNAME记录，指向`username.github.io`或者`example.com`，这样方便别人输入`www.example.com`也是可访问的。

* 如果你只是想解析单个二级域名，如`blog.example.com`，只需配置一个 **CNAME记录** 即可：
    - CANME记录 —— `username.github.io`

如图：
![image_1b89av1da1e3n1s1mt301ie3qhsm.png-48.4kB][3]

备注：github推荐使用二级域名，一来如果github服务器ip变了对于顶级域名你得去修改它的A记录，二来可以更有效抵御DoS和利用CDN加速。

## 等待
大约等到5分钟到24小时内，你的解析就生效了。
也可以使用`dig`命令检查解析情况：

```
dig yourdomain.com +nostats +nocomments +nocmd
```

## 访问
在浏览器输入你的域名访问试试，一般没什么问题就可以成功访问啦。
到这里我们就完成了自定义域名的绑定，为你的博客继续增添装逼的能量吧。

## 最后
需要注意的是，如果开启了自定义域名支持，GitHub 提供的子域名 `username.github.io` 的 HTTPS 就无法生效了，仍然想要支持https的话可以参考：[为GitHub Pages自定义域名配置HTTPS][4]。

## 拓展阅读
[Custom domain for GitHub project pages][5]



  [1]: https://thinktxt.static.lxyour.com/article/github_item_setting_20170205.jpg
  [2]: https://thinktxt.static.lxyour.com/article/github_custom_domain_20170205.jpg
  [3]: https://thinktxt.static.lxyour.com/article/domain_dns_20170205.jpg
  [4]: https://www.thinktxt.com/jekyll/2017/02/06/jekyll-series-github-pages-custom-domain-htt.html
  [5]: http://stackoverflow.com/questions/9082499/custom-domain-for-github-project-pages
