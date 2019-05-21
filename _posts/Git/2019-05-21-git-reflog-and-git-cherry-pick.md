---
title: 使用git reflog与git cherry-pick找回丢失的代码
date: 2019-05-21 11:05:08
description: "使用git reflog与git cherry-pick找回丢失的代码"
layout: post
categories: Git
tags: [Git,reflog,cherry-pick]
comments: true
pay: true
---
在使用Git的过程中，有时候会因为一些误操作，比如reset、rebase、merge等丢失了某些提交。特别是在Commit之后又执行了`git reset --hard`，HEAD强制回滚本地记录以及文件到服务器版本，导致本地做的修改全部恢复到Git当前分支的服务器版本，同时自己的Commmit记录也消失了。

碰到这种情况，不要慌，我们在Git上做的任何操作都只是在原来之前的操作上做修改，并且都会被记录下来，也就是说无论你做了什么，对于Git来说都可以进行回滚操作。

## 找回丢失的commit
我们来通过以下示例演示下具体怎么进行操作：

```
$ git init
$ echo 1 >> index.txt
$ git add index.txt
$ git commit -m "commit-1"
```

再将`index.txt`文件修改如下：

```
1
2
```

然后继续提交：

```
$ git commit -a -m "commit-2"
```
我们现在通过`git log`查看日志，如下：

> 为了让日志简洁点我们可以执行命令：`git log --oneline --decorate`

```
5ef0d09 (HEAD -> master) commit-2
7c798fc commit-1
```

现在让我们来重置回到第一次提交的状态：

```
$ git reset --hard 7c798fc
$ git log
7c798fc (HEAD -> master) commit-1
```

这看起来我们是丢掉了我们第二次的提交，本地的修改也消失了，没有办法找回来了。但是`reflog` 就是用来解决这个问题的。简单的说，它会记录所有HEAD的历史，也就是说当你做 reset，checkout等操作的时候，这些操作会被记录在`reflog`中。

```
$ git reflog
7c798fc (HEAD -> master) HEAD@{0}: reset: moving to 7c798fc
5ef0d09 HEAD@{1}: commit: commit-2
7c798fc (HEAD -> master) HEAD@{2}: commit (initial): commit-1
```

所以，我们要找回我们第二commit，只需要做如下操作：

```
$ git reset --hard 5ef0d09
```

再来看一下 git 日志：

```
$ git log
5ef0d09 (HEAD -> master) commit-2
7c798fc commit-1
```

同时本地对`index.txt`做的修改也都恢复回来了。

## 合并某个commit

如果执行`git reset --hard`后又已经产生了新的提交，并且想要在当前新提交上找回之前的丢失的commit，这时候我们就要用到`git cherry-pick`命令了。

比如，我们仍然回退到`commit-1`:

```
$ git reset --hard 7c798fc
$ git log --oneline --decorate
7c798fc (HEAD -> master) commit-1
```

然后在此基础上继续修改`index.txt`文件：

```
1 
3
```

然后继续提交：

```
$ git commit -am "commit-3"
```

这时候再查看日志：

```
$ git log --oneline --decorate
81004de (HEAD -> master) commit-3
7c798fc commit-1
```

已经产生了新的提交，而这时候我们的`commit-2`看起来已经彻底丢失了，你开始慌了。

老铁别慌，接下来我们执行`git reflog`试试看：

```
$ git reflog
81004de (HEAD -> master) HEAD@{0}: commit: commit-3
7c798fc HEAD@{1}: reset: moving to 7c798fc
5ef0d09 HEAD@{2}: reset: moving to 5ef0d09
7c798fc HEAD@{3}: reset: moving to 7c798fc
5ef0d09 HEAD@{4}: commit: commit-2
7c798fc HEAD@{5}: commit (initial): commit-1
```

我们可以看到`commit-2`的`commit ID：5ef0d09`还完好的记录在那里，这时候如果我们希望在保留当前提交的基础上将`commit-2`的内容合并过来，可以执行：

```
$ git cherry-pick 5ef0d09
```

这时候可能会产生冲突，那么我们可以在解决冲突后执行：

```
$ git add index.txt
$ git cherry-pick --continue
```

再次查看日志：

```
$ git log
3559b85 (HEAD -> master) commit-2
81004de commit-3
7c798fc commit-1
```

会发现`commit-2`提交已经找回了，并产生了一条新的`commit ID：3559b85`，同时我们本地的代码也恢复过来了，现在我们可以继续欢快的搬砖了。

