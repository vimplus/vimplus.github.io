---
title: 玩转jekyll系列（一）之完善博客的分页功能
date: 2017-01-23 10:55:21
description: "玩转jekyll系列（一）之完善博客的分页功能"
layout: post
categories: jekyll
tags: [jekyll,blog,分页]
comments: true
---
前段时间教大家利用jekyll搭建了一个基本GitHub Pages博客。一个博客网站，一般都应该具备诸如列表、分类、标签、评论等功能。
博客的列表文章多了，自然需要分页，今天给大家先来分享在jekyll中添加分页功能。

## 准备
安装 gem 插件

```
sudo gem install jekyll-paginate
```

## 配置
在配置文件 `_config.yml` 中添加以下配置项：

```
gems: [jekyll-paginate]   #添加 gem 的 jekyll-paginate插件。

paginate: 5  # 每页显示的文章数量
paginate_path: "page:num"   #分页页面路径格式
```

## 使用分页

### 修改首页
在首页（index.html）中使用一下代码（自行修改样式吧）：
注意：使用时请去掉代码中的`\`

```html
<ul class="list-container">
  {\% for post in paginator.posts \%}
  <li class="list-item clearfix">
    <div class="list-content">
      <h2><a class="link-title" href="\{\{ post.url | prepend: site.baseurl \}\}">\{\{ post.title \}\}</a></h2>
      <div class="meta">
        <a class="category" href="/categories.html#\{\{post.categories\}\}">\{\{ post.categories \}\}</a>
        <time class="date">\{\{ post.date | date: "%Y-%m-%d" \}\}</time>
      </div>
    </div>
  </li>
  {\% endfor \%}
</ul>
```

### 新建分页文件
在`_includes`目录中新建`pagination.html`文件，添加一下代码：

```html
{\% if paginator.total_pages > 1 \%}
  <div class="pagination">
    {\% if paginator.previous_page \%}
      <a href="\{\{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' \}\}">&laquo; Prev</a>
    {\% else \%}
      <span>&laquo; Prev</span>
    {\% endif \%}

    {\% for page in (1..paginator.total_pages) \%}
      {\% if page == paginator.page \%}
        <em>\{\{ page \}\}</em>
      {\% elsif page == 1 \%}
        <a href="\{\{ '/index.html' | prepend: site.baseurl | replace: '//', '/' \}\}">
          \{\{ page \}\}
        </a>
      {\% else \%}
        <a href="\{\{ site.paginate_path | prepend: '/' | replace: '//', '/' | replace: ':num', page \}\}">
          \{\{ page \}\}
        </a>
      {\% endif \%}
    {\% endfor \%}

    {\% if paginator.next_page \%}
      <a href="\{\{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' \}\}">Next &raquo;</a>
    {\% else \%}
      <span>Next &raquo;</span>
    {\% endif \%}
  </div>
{\% endif \%}
```
然后引入在首页中或列表页引入分页代码：

```html
{\% include pagination.html \%}
```

## 分页参数
jekyll中的paginator 对象的一些参数：

|  属性	| 说明  |
|  ---  | ---   |
|  page	| 当前页码  |
|  per_page	| 每页文章数量  |
|  posts	| 当前页的文章列表  |
|  total_posts	| 总文章数  |
|  total_pages	| 总页数  |
|  previous_page	| 上一页页码 或 nil  |
|  previous_page_path	| 上一页路径 或 nil  |
|  next_page	| 下一页页码 或 nil  |
|  next_page_path	| 下一页路径 或 nil  |


## 结语
其实jekyll-paginate提供的分页已经满足了我们的基本需求了，分页的实现还是蛮简单的，自行修改分页的样式吧，如果还有什么不明白的欢迎在下面评论。
