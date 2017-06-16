---
title: 采用Git-flow方式打造简单高效的Git工作流
date: 2017-06-16 09:06:08
description: "Git-flow打造简单高效的Git工作流"
layout: post
categories: Git
tags: [Git,gitflow,gitflow]
comments: true
pay: true
---
Git是一款免费、开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。与常用的版本控制工具 CVS、Subversion等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

CVS、SVN属于集中式版本管理系统，Git属于分布式版本控制系统，Git凭借自身强大的分支管理特性，把SVN等远远抛在了后面，成为最流行的版本管理控制系统。



> Git是目前世界上最先进的分布式版本控制系统（没有之一）。



Git有什么特点？简单来说就是：**高端大气上档次！**

## SVN 与 Git

### 分布式与集中式

Subversion 是一个**集中式（centralized）**的版本控制系统，Git 是一个**分布式（distributed）**的版本控制系统。

![git and svn](https://www.git-tower.com/learn/content/01-git/01-ebook/cn/01-command-line/07-appendix/03-from-subversion-to-git/centralized-vs-distributed.png)

### 分支

正如刚才提到的， Subversion 的分支仅仅是一些有特殊含义的目录。在创建一个新的分支时，你只是把项目的当前状态完完整整地拷贝到这个新的分支目录中。

**Git 的分支技术**是它的设计核心，因此它拥有一个完全不同的概念。一个在 Git 中的分支就是一个指向一个特定版本的指针：不拷贝任何文件；不创建任何目录；没有任何额外的操作。
在 Git 中你 *永远* 工作在一个分支上，至少工作在那个系统默认创建的 “master” 分支上。在你的工作副本上只包括你当前的活动分支中的文件（ Git 称之为 “HEAD”）。 所有其他的版本和分支都被保存在你的本地仓库中， 并且随时都可以非常快速地恢复到一个旧的版本。

> 一定要记住 Git 的分布式特性：分支可以被发布到在远程服务器上，但是本地上的分支对于日常的工作更加重要。

更多请参考：[从 Subversion 过渡到 Git](https://www.git-tower.com/learn/git/ebook/cn/command-line/appendix/from-subversion-to-git#start)

## 为什么选择 Git？

- 节省时间
- 离线工作
- 撤销错误操作
- 可靠性高
- 让提交更有意义
- 更高的自由度
- 避免混乱
- 顺应潮流

详细参考：[为什么选择 Git](https://www.git-tower.com/learn/git/ebook/cn/command-line/appendix/why-git).

## 快速实例

```bash
echo "# git-Demo" >> README.md
git init
git add README.md
git commit -m "first commit"

git remote add origin https://github.com/vimplus/git-Demo.git
git push -u origin master
```

![git](http://static.zybuluo.com/Lxyour/z117s663guvp6vl50xnkaomi/Git%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%E6%B5%81%E7%A8%8B%E5%9B%BE.png)

## 日常命令

```bash
$ git add .
$ git commit -m "本次提交的描述"
$ git pull
$ git push
```

## Git-flow分支介绍

### master

【线上的分支】 - 是线上版本分支，也可以理解为随时可以发布的稳定版本，要求在每次版本封版后由主程序员合并`release`分支代码进来，开发人员不可以随意操作。

### develop

【开发基础分支】 -  包含待上线的新内容，是你进行任何新的开发的基础分支。当你开始一个新的功能分支时，它将是**开发的基础**，由此拉出`feature`分支准备新功能开发。另外，该分支也汇集所有已经完成的功能，并等待经过`release`分支测试通过后最终被整合到 `master` 分支中。

### release

【上线分支】 - 当开发结束后用来提测并且为本次版本最终上线的分支，所有测试阶段的bug全部在此分支修复，测试结束后合并到 `master` 和 `develop` 分支中。

当准备将develop上的新内容发布到生产环境时，需要拉release分支。release分支可以隔离develop后续对本次上线的影响。当release拉出来后，不用担心其它的东西会合过来，只需要在这上面专注测试和修复bug。

### feature

【新功能开发分支】 - 开发新功能时以develop分支为基础建立新的feature分支进行单独开发。当需要此功能的时候，只需要将该 `feature` 分支合并入 `develop` 分支，下次一并提测即可。

这样设计可以避免这个功能在尚未开发完成或者通过测试的时候混入发布的版本，而导致不可预知的不稳定。当然也可以同时开启多个 `feature` 分支进行不同新功能开发，在合适的时候合并提测即可。

### hotfix

【线上紧急bug分支】 - 用来修复线上的紧急bug，应由 `master` 拉出，并在修复完成后合并入 `master` 和 `develop` 保证两分支的bug已修复。

### 工作流示意图

![git-flow](http://static.zybuluo.com/Lxyour/7ajn21pjpr6dofck0hanqu4s/git-flow.jpg)

`master`和`develop`这两个分支被称作为 `长期分支`，它们会存活在项目的整个生命周期中。而其他的分支，例如针对功能的分支，针对发行的分支，仅仅只是临时存在的。它们是根据需要来创建的，当它们完成了自己的任务之后就会被删除掉。



## 常见的场景和操作规范

### 开发新功能

1. 从`develop`拉一个`feature`分支。

2. 在`feature`分支上做开发。

3. `feature`开发完成后，需要提交测试，

   有两种场景：

   一种是该feature功能不复杂，测试点不多，自测充分后可以直接完成`feature`；

   另一种是`feature`功能非常复杂，测试点也很多。这个时候不要马上完成`feature`，前期让QA直接在`feature`分支上测试，等测得比较稳定后再完成`feature`。因为功能复杂的feature，自测完成后肯定还是有很多问题，过早合到`develop`，`develop`将有很长一段时间不能上线，会影响到其它的发布。

4. 完成`feature`将`feature`分支合并到`develop`，删除原分支。

### 上线

- `develop`会不断累积新内容等待上线。上线时，准备一个`release`分支，准备`release`分支时需要搞清楚这次上线新增的内容，列给QA，让QA有针对性的测试。

- 在打包机器上打包对应的`release`分支，部署到应用服务器让QA测试，发现bug直接在`release`上修改。
- `release`测试通过后，可以上线了，则将`release`合到`master`和`develop`，删除该`release`分支。
- 线上部署的时候，从`master`打一个包，先部署到预发，在预发上简单回归测试，没问题后发布到线上服务器，上线完成。

### 紧急修复

- 对于一些需要马上修改并尽快上线的内容，走`hotfix`分支。

- 从最新的`master`拉`hotfix`分支并在`hotfix`分支上修改。
- 在打包机器上打包对应的`hotfix`分支，部署到应用服务器给qa测试，发现bug直接在`hotfix`分支上修改。
- `hotfix`测试通过后，可以上线了，则将`hotfix`合并到`master`和`develop`，删除该`hotfix`原分支。

### 一些注意事项

- 每一个流程完成后一定要记得合代码和推代码，不然会坑到后面的人。
- 及时在群里同步信息。
- `release`分支最好一天不超过一个，如果需要上线多次，可以合并到一起。
- 拉分支前记得`pull`新代码。

