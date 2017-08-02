---
title: CentOS 7搭建Node+MongoDB+Nginx环境
date: 2017-08-02 10:06:21
description: "CentOS 7搭建Node+MongoDB+Nginx环境"
layout: post
categories: Linux
tags: [Linux,Nginx,CentOS]
comments: true
pay: true
---

最近申请体验某云的云服务器，作为`Linux`小白的我，期间还是遇坑不少，这里就来记录一下安装的过程。


## 安装Node

### 准备
安装`gcc`和`gcc-c++`，因为Node依赖于`gcc`以及`gcc-c++`：

```
# yum -y install gcc gcc-c++ kernel-devel
```

### 下载Node安装包

下载安装包并解压：

```
# wget https://npm.taobao.org/mirrors/node/v6.10.2/node-v6.10.2.tar.gz
# tar -xf node-v6.10.2.tar.gz
# rm -f node-v6.10.2.tar.gz
```

如果想要**更高版本**的Node，可以自行到[淘宝镜像目录][1]寻找对应的镜像资源链接。
备选官方资源地址：`wget https://nodejs.org/dist/v6.10.2/node-v6.10.2.tar.gz`。


### 安装

上面做的事情就是将文件压缩包下载到安装目录，解压后，将压缩包删除，用`ls`查看下，安装目录下多了一个文件夹`node-v6.10.2`，进入到这个文件夹：

```
# cd node-v6.10.2
# ./configure
# make
# sudo make install
```

依次执行上面的指令，其中make过程可能会久一点，指令执行完毕，Node也就安装好了，可以用`node -v`和`npm -v`来检查下。

### 升级Node

如果你还需要升级Node，可以借助一个包：`n`

```
# npm install -g n
# n stable
```

这样我们的Node就是最新的稳定版本啦！
我的本地是Windows系统，推荐一个非常好用的命令行工具：`Cmder`

推荐几个**Windows**下的工具：

* `winscp`用来在服务器查看目录
* `Cmder` 或 `Xshell`操控远程服务器

## 安装MongoDB
MongoDB是可扩展的、高性能的开源NoSQL数据库，它用JASON格式保存数据。

### 添加MongoDB 3.2源

```
# vim /etc/yum.repos.d/mongodb-org.repo
```

写入如下内容：

```
[mongodb-org]
name=MongoDB 3.2 Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc
```

保存并关闭文件。
这里可以修改 `gpgcheck=0`, 省去gpg验证。

在继续之前，首先验证MongoDB存储库是否存在于yum实用程序中，`repolist`命令显示已启用的存储库的列表：

```
# yum repolist
```

### 开始安装

```
# yum install mongodb-org
```

执行后安装的软件包：

* mongodb-org-mongos
* mongodb-org-server
* mongodb-org-shell
* mongodb-org-tools

MongoDB安装完成后创建的文件：

`/etc/mongod.conf`－MongoDB配置文件，其中包含监听端口
`/var/lib/mongo`－MongoDB数据保存目录
`/var/log/mongodb/mongod.log`－MongoDB的日志文件


### 启动Mongodb

```
# systemctl start mongod.service
# systemctl enable mongod.service
```

如果执行`systemctl enable mongod.service`显示:

```
mongod.service is not a native service, redirecting to /sbin/chkconfig.
Executing /sbin/chkconfig mongod on
```

那就是需要关闭相关端口的防火墙：

> 如果显示`FirewallD is not running`，表示没有启动防火墙进程，如果没有启动防火墙程序，请先执行：`systemctl start firewalld`启动防火墙。

执行：（每一句执行成功会显示`success`）

```
# firewall-cmd --zone=public --add-port=27017/tcp --permanent
# firewall-cmd --reload
```


### 运行mongo

```
# mongo
```

注意：启动MongoDB Shell时，用户可能将看到一些警告：

* **如果显示以下警告：**

```
MongoDB shell version: 3.2.12
connecting to: test
Server has startup warnings: 
2015-09-08T14:29:50.163+0800 I CONTROL  [initandlisten] 
2015-09-08T14:29:50.163+0800 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
2015-09-08T14:29:50.163+0800 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2015-09-08T14:29:50.163+0800 I CONTROL  [initandlisten] 
2015-09-08T14:29:50.163+0800 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/defrag is 'always'.
2015-09-08T14:29:50.163+0800 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2015-09-08T14:29:50.163+0800 I CONTROL  [initandlisten] 
```

MongoDB建议关闭Linux系统默认开启的透明大页功能，我们可以执行下面内容将其关闭：

```
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
```

上面的配置重启会失效，要想永久生效可以把这两行写到 `/etc/rc.local` 文件中， 可编辑`rc.local`文件，使其在系统启动的时候关闭。


* **如果出现 rlimits 相关的警告, 如：**

```
** WARNING: soft rlimits too low. rlimits set to 4096 processes, 64000 files. Number of processes should be at least 32000 : 0.5 times number of files.
```

MongoDB是一个进程级应用程序，其可以通过新建其他进程来帮其分担其工作量。为了使MongoDB保持其最高效的状态，会有一个警告，其启动的进程数量应该是在任何给定时间可以打开文件数量的一半。要解决此警告，编辑20-nproc.conf文件更改mongod的过程soft rlimit值：

```
vim /etc/security/limits.d/20-nproc.conf
```

在文件中末尾添加如下配置：

```
mongod soft nproc 64000
```

要使用MongoDB的新限制，则使用`systemctl`实用程序重启MongoDB：

```
# systemctl restart mongod
```

#### 再次运行

```
[root@centos usr]# mongo
MongoDB shell version: 3.2.12
connecting to: test
```

当我们再次连接到MongoDB Shell时，警告就消失了。

#### 监听日志

```
# tail -f /var/log/mongodb/mongod.log
```

### 总结

```
// 检查 mongodb 是否允许系统启动
# systemctl is-enabled mongod

// 使 mongodb 系统启动
# systemctl enable mongod

// 启动
# systemctl start mongod

// 查看启动状态
# systemctl status mongod

// 停止
# systemctl stop mongod
```

### 配置说明

```
fork=true   ## 允许程序在后台运行
#auth=true  ## 开始认证
logpath=/data/db/mongodb/logs/mongodb.log   
logappend=true        # 写日志的模式：设置为true为追加。默认是覆盖
dbpath=/data/db/mongodb/data/    ## 数据存放目录
pidfilepath=/data/db/mongodb/logs/mongodb.pid    # 进程ID，没有指定则启动时候就没有PID文件。默认缺省。
port=27017
#bind_ip=192.168.2.73   # 绑定地址。默认127.0.0.1，只能通过本地连接
# 设置为true，修改数据目录存储模式，每个数据库的文件存储在DBPATH指定目录的不同的文件夹中。
# 使用此选项，可以配置的MongoDB将数据存储在不同的磁盘设备上，以提高写入吞吐量或磁盘容量。默认为false。
# 建议一开始就配置次选项
directoryperdb=true

# 禁止日志 
# 对应 journal 启用操作日志，以确保写入持久性和数据的一致性，会在dbpath目录下创建journal目录
nojournal = true   

## max connections
# 最大连接数。默认值：取决于系统（即的ulimit和文件描述符）限制。
# MongoDB中不会限制其自身的连接。当设置大于系统的限制，则无效，以系统限制为准。
# 设置该值的高于连接池和总连接数的大小，以防止尖峰时候的连接。
# 注意：不能设置该值大于20000。
maxConns=1024
```

### 卸载MongoDB
依次执行如下命令完全移除MongoDB：

```
# systemctl stop mongod
# yum erase $(rpm -qa | grep mongodb-org)
# rm -rf /var/log/mongodb
# rm -rf /var/lib/mongo
```

### 拓展阅读：

* [CentOS 7 安装 MongoDB 3.2][2]
* [如何在CentOS 7上安装MongoDB][3]
* [How to Install MongoDB 3.2 on CentOS 7.x and RHEL 7.x][4]
* [MongoDB, installation on CentOS 7.2][5]
* [centos安装mongodb3.2及配置远程连接小记][6]

## 安装Nginx

这里我们使用 yum 安装是在线安装，直接使用命令 `yum -y install nginx` 安装即可。自己如果想要采用源码安装也可以参考其他应用源码的安装方式。

安装完了之后直接执行`nginx`启动, 配置文件在`/etc/nginx/nginx.conf`。


## 安装Git

**CentOS 7.x**自带了Git，但是自带的版本比较低，我们可以通过自己下载Git源码包安装最新版本的，以下方法同样适用于CentOS 6.x系统。

> 说明：我们其实可以快捷的通过`yum install git`安装，但是通过yum方式安装，版本比较旧，CentOS7.2上安装好是1.8.3版。如果想安装最新版或其他版本，需要使用源码编译安装的方式。

### 准备
安装前先卸载系统自带的旧版本Git，使用`yum remove git`

### 安装依赖

```
# yum -y install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
# yum -y install gcc perl-ExtUtils-MakeMaker
```

### 下载&解压
分别执行以下命令：

```
# cd /usr/src
# wget https://www.kernel.org/pub/software/scm/git/git-2.12.2.tar.gz
# tar -zxvf git-2.12.2.tar.gz
```

想要其他最新的版本可以自行上[这里][7]寻找最新版本镜像源。
备用官网资源地址： `# wget https://github.com/git/git/archive/v2.5.0.tar.gz`, 如果有需要也可以从这个地址下载。

### 编译安装

```
# cd git-2.12.2
# make prefix=/usr/local/git all
# make prefix=/usr/local/git install
# echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/bashrc
# source /etc/bashrc
```

### 检查git版本

```
# git --version
git version 2.12.2
```



  [1]: https://npm.taobao.org/mirrors/node/
  [2]: http://blog.topspeedsnail.com/archives/6005
  [3]: http://www.pandacademy.com/%E5%A6%82%E4%BD%95%E5%9C%A8centos-7%E4%B8%8A%E5%AE%89%E8%A3%85mongodb/
  [4]: http://www.linuxtechi.com/install-mongodb-3-2-on-centos-7and-rhel-7/
  [5]: http://frederic-wou.net/mongodb-on-centos-7-2/
  [6]: http://hhxblog.leanote.com/post/centos%E5%AE%89%E8%A3%85mongodb3.2%E5%8F%8A%E9%85%8D%E7%BD%AE%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5%E5%B0%8F%E8%AE%B0
  [7]: https://www.kernel.org/pub/software/scm/git/
