---
title: Git常用操作命令学习笔记
date: 2017-03-19 11:36:08
description: "Git常用操作学习笔记"
layout: post
categories: Git
tags: [Git,github]
comments: true
pay: true
---
Git是一款免费、开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。与常用的版本控制工具 CVS、Subversion等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

CVS、SVN属于集中式版本管理系统，Git属于分布式版本控制系统，Git凭借自身强大的分支管理特性，把SVN等远远抛在了后面，成为最流行的版本管理控制系统。

## 快速实例

```bash
echo "# git-Demo" >> README.md
git init
git add README.md
git commit -m "first commit"

git remote add origin https://github.com/vimplus/git-Demo.git
git push -u origin master
```

## 一、创建版本

### 【1.】新建目录

```
$ mkdir /e/WEB-Static/gitdemo
```

### 【2.】访问目录

进入到想要建立版本仓库的**【一个新项目的目录】**使用`cd /path`命令， `/path`是你想要访问的本地位置，该目录必须已存在）

```
//例如：
$ cd /E/WEB-Static/gitDemo

//执行完之后
Lxyweb@TXMS-PC ~ /E/WEB-Static/gitDemo
$ _
```

### 【3.】初始化目录
初始化刚刚选定的目录，使用`git init`命令，创建一个新的Git仓库

```
//初始化之后
Lxyweb@TXMS-PC ~ /E/WEB-Static/gitDemo
$ git init
Initialized empty Git repository in e:/git/.git/

Lxyweb@TXMS-PC ~ /E/WEB-Static/gitDemo (master)
$ _
```

### 【4.】添加文件
添加文件到Git仓库，分两步：

* 第一步，使用命令`git add <file>`，例如： git add index.html
注意，可反复多次使用，添加多个文件；
* 第二步，使用命令`git commit`，完成。

```
$ git commit -m "desc"
```

### 【5.】推送到远程
将本地新项目仓库传送到远程新仓库
如果还没有可克隆的现有仓库，并欲将你的仓库共享到某个远程服务器，你可以使用如下命令

```
$ git remote add origin <server>
//例如：
$ git remote add origin https://git.coding.net/Lxyour/gitDemo.git
$ git push -u origin master
```

## 二、时光穿梭

* 要随时掌握工作区的状态，使用`git status`命令。
* 如果**git status**告诉你有文件被修改过，用`git diff`可以查看修改内容。

### 版本回退

* HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令`git reset --hard commit_id`。
* 穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本。
* 要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本。

### 工作区与暂存区

* 暂存区是Git非常重要的概念，弄明白了暂存区，就弄明白了Git的很多操作到底干了什么。
* 每次修改，如果不add到暂存区，那就不会加入到commit中。

### 撤销

撤销`git add .`或`git add --all`添加的文件

```
//撤销所有添加
$ git rm -r --cached .
```

* 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- file`。
* 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD file`，就回到了场景1，第二步按场景1操作。
* 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

### 删除

命令`git rm`用于删除一个文件。

```
$ git rm  //删除一个文件

$ git add -u  //告诉git自动跟踪当前阶段文件,包括追踪以前删除的文件。
```

如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。

### 配置姓名、邮箱

```
git config --global user.name "txBoy"
git config --global user.email "txBoy@example.com"
```

### 保存用户名和密码
如果每次提交的时候需要用户名密码，可以输入以下命令，让Git配置文件记住。

```
$ git config --global credential.helper store
```

执行完后查看`C:\Users\Administrator`目录下的.gitconfig文件，会多了一项：

```
[credential]

    helper = store
```

下次git push时你会发现不用再输入用户名和密码。

## 三、分支

Git的分支相对于SVN有着强大的优势。
相关文章： [git分支及一些常用操作][2]

### 新建本地分支

通过`git branch`命令可创建一个新分支，具体参考如下：

```
$ git branch [name]  //创建后不会自动切换为当前分支
$ git checkout -b [name] //创建新分支并立即切换到新分支

//eg:
$ git branch member
$ git branch feature/member  //feature类似于一个文件夹
$ git checkout -b feature/version_1008

//推送到远程
$ git push origin feature/version_1008
```

`-b` 的意思是 base，以当前分支为基本点，新建一个名叫 `feature/version_1008` 的分支，这里当然也可以使用其他的命名。

### 查看分支

```
$ git branch     //查看本地分支
$ git branch -r  //查看远程分支
$ git branch -a  //查看所有分支（包含本地和远程）
```

### 本地分支推送到远程
将本地分支推送到远程（本地分支push到远程）

```
$ git push origin [name]
//示例
git push origin release/release_1018
```

### 切换本地分支（本地分支之间切换）
在本地的分支之间切换：

```
$ git checkout [branch_name]
```

### 切换到远程分支

切换到远程分支可使用`git checkout remotes/origin/分支名`，一般不采用这种方式，而是：

> git checkout -b [分支名] [远程名]/[分支名]

通过`git branch`可以查看本地分支，通过`git branch -a`可查看包含远程的所有分支
远程已经存在的分支，但是本地没有，可以:

> 以远程分支为基础拉取到本地，并创建相同的本地分支

使用如下命令：

```
$ git checkout -b experimental origin/experimental
//比如：
$ git checkout -b feature/cashier origin/feature/cashier
```
本地的分支名也可以与远程的不一样，比如：`git checkout -b localBranchName origin/branchName`

更推荐的便捷方式是使用：

```
git checkout --track origin/[branch_name]
```

上面这行命令的作用是： 

> **拉取远程分支到本地，建立一个和远程同名的分支到本地并跟踪远程分支**（具体可看下一节）

### 拉取并跟踪远程分支
如果想要拉取远程分支到本地并且直接跟踪该远程分支，可执行：

```
$ git checkout --track origin/[branch_name]
// 简化命令
$ git checkout -t origin/[branch_name]

//例如：拉取远程名为feature/react-router-object分支到本地
$ git checkout -t origin/feature/react-router-object
```

也就是当你`git push`的时候自动推送到对应的远程分支了。
更多可参考：[Git详解之三-Git分支][3]

### 合并分支
将A分支合并到B分支中来，需要先切换到B分支中。

```
$ git merge [name] ----将名称为[name]的分支与当前分支合并
```

更多可参考：[远程分支和本地分支的相互创建和跟踪][4]

### 跟踪分支

```
$ git push -u origin master //跟踪主分支
$ git push -u origin origin/feature/cashier  //跟踪指定的分支
$ git push -u origin --all //跟踪所有分支
```

更多可参考： [ Git 分支 - 远程分支][5]

### 删除分支

* 删除本地分支：

```
$ git branch -d [name]
```

-d选项只能删除已经参与了合并的分支，对于未有合并的分支是无法删除的。如果想强制删除一个分支，可以使用-D选项

* 删除远程分支：

```
$ git push origin [name]

//例如使用命令：
$ git push origin --delete Chapater6   //可以删除远程分支Chapater6  
```

再次使用命令 `git branch -a`   可以发现，远程分支`Chapater6`已经被删除。
更多可参考：[git删除远程分支和本地分支][6]

### 克隆指定分支
用`git clone`命令只能在本地创建`master`分支，想要直接clone指定的分支，可以执行：

```
git clone -b [branch_name] https://git.coding.net/Lxyour/gitDemo.git
```

## 四、忽略文件

忽略一些文件、文件夹不提交，在仓库根目录下创建名称为`.gitignore`的文件，写入不需要的文件夹名或文件，每个元素占一行即可，如:

```
*.seed
*.log
*.csv
*.dat
*.out
*.pid
*.gz
.DS_Store
.project
.idea/
/vendor
src/Tpl
logs
npm-debug.log
node_modules
```

## 问题总结

* 1、有时候执行git add --all 的时候总是有个提示：

```
warning: LF will be replaced by CRLF in package.json.
The file will have its original line endings in your working directory.
```

解决方案：`git config core.autocrlf true`  
参考：[LF will be replaced by CRLF in git - What is that and is it important?][7] 

## **附录 git帮助说明**
```
git --help 查看帮助

init       创建一个空库或重新引导当前的库
checkout   签出一个分支或路径到工作区
clone      克隆存储库到一个新的目录

status     显示工作目录当前状态
add        添加文件的内容到缓存区

commit     提交更改记录到储存库
push       用于将本地分支的更新,推送到远程主机

diff       显示工作目录与缓存区文件之间的差异等
fetch      从远程获取最新版本到本地，不会自动合并
pull       从远程获取最新版本并合并到本地

bisect     快速定位引入错误的版本 
branch     列出、创建或删除分支

log        显示提交日志
merge      合并2个或多个开发分支
rebase     合并分支，类似于git merge，但优于merge，rebase是逐个文件的合并
mv         移动或重命名一个文件、目录或符号链接

grep       文件内容搜索定位工具
reset      将当前的分支重设到指定的HEAD（默认）或者<commit>
rm         从工作区和索引删除文件
show       显示不同类型的对象

tag        创建、列出、删除、或验证一个标签对象与GPG签署
```

## 拓展阅读

[Git常用命令清单][1]

  [1]: https://github.com/jaywcjlove/handbook/blob/master/other/Git%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%E6%B8%85%E5%8D%95.md
  [2]: http://www.cnblogs.com/springbarley/archive/2012/11/03/2752984.html
  [3]: http://www.open-open.com/lib/view/open1328069889514.html#articleHeader12
  [4]: http://blog.csdn.net/xuzhaojia/article/details/16108723
  [5]: https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E8%BF%9C%E7%A8%8B%E5%88%86%E6%94%AF
  [6]: http://www.cnblogs.com/luosongchao/p/3408365.html
  [7]: http://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important

