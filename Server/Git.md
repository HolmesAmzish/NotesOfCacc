# Git

Git 是一个版本控制系统，它可以帮你保管你提交的各种版本以供在你需要的时候回溯旧版。与此同时他还能提供远程仓库同步从而使多个机器的仓库同步。

## 下载 Git并设置

在[Git官网](https://git-scm.com/)上选择Download下载。下载时会默认将git添加至环境变量，安装完成后如果打开命令行窗口，输入`git`返回相应的参数，说明安装成功。设置提交代码仓库时的身份，包括了用户名和联络方式。

打开命令行（powershell 或者 cmd）

```powershell
git config --global user.name username
# 如果username包含空格，需要用双引号括起来，例如"Holme Amzish"

git config --global user.email username@email.com
# --global代表全局，意为对所有仓库的设置都是一样

git config --list
# 列出所有设置
```

## 创建本地仓库

在你需要创建仓库的文件夹根目录按住shift右键，打开命令行，或Git Bash。随后输入`git init`即可在本文件夹中创建仓库，可以看见本文夹多出了.git 这个文件夹，这就是本地仓库所在的位置。

![本地仓库](../../img/3.png)

创建完成后，会默认进入主分支也就是**master**，有些版本可能主分支叫做**main**。现在将文件全部添加至暂存区中然后保存至仓库。

```bash
git init
# 初始化仓库

git add .
# 添加所有改动的文件至暂存区

git add file.txt
# 如果你只想添加某个文件，可以指定这个文件

git commit -m <message>
# 将暂存区的文件全部添加至仓库
# -m 后的参数是每次提交时的信息，如果需要写多行，直接输入git commit后会进入vim来修改
```

首先按下 i 键进入到插入模式，写完你所要写的信息之后，按下Esc返回命令模式，输入`:wq `(意为write quit) 保存并退出，随后所有文件即被提交至本地仓库中。

更改上一次提交的信息

```bash
git commit --amend -m "new_message"
```



## 建立远程仓库

登录[Github主页](https://github.com/)并找到你的代码仓库页面，点击New创建新的代码仓库

![github](../../img/7.png)

之后找到刚创建的git仓库的地址，此处有两个URL地址，分别是HTTPS协议和SSH协议的地址，是远程仓库的链接。这里推荐使用SSH连接，更加安全。

![github](../../img/8.png)

## 配置SSH密钥并连接

现在需要将本地仓库连接到远程仓库，将本地仓库通过SSH连接的方式连接到远程仓库需要配置SSH密钥。通过命令行进行配置和获取SSH密钥。

```powershell
cd ~
# 直接转移到用户根目录的地址，“~”是在cd到用户根目录时常用快捷的方法

cd .ssh
# 进入SSH设置文件夹

ssh-keygen
# 生成SSH密钥
```

在这里会让你输入文件的名称，如果没有创建过SSH密钥可以直接回车使用默认文件名，随后需要你设置密码并重复，如果不输入则设置为没有密码。

![sshkey](../../img/9.png)

然后输入 ls 查看.ssh文件夹的文件，会看到一个以.pub扩展名结尾的SSH公钥文件，通过`cat filename.pub` 查看这个文件并将整个文件的内容复制下来

![sshkey](../../img/11.png)

将这个SSH公钥填入你的Github账号中。重新回到Github主页，点击头像并找到设置的选项，来到设置页面后可以在菜单栏里找到SSH密钥的设置（SSH and GPG keys）

![sshkey](../../img/10.png)

点击 New SSH key新建一个SSH密钥配置，名字自定，建议写机器的名字用于区分，下面内容填入刚刚复制过来的SSH公钥。

关联本地仓库和远程仓库

```bash
git remote add origin <url>
# origin是仓库的别称
# <url>是Github所复制下来的SSH链接

git remote -v
# 检查仓库关联的情况
```

![remote](../../img/12.png)

## 推送和拉取仓库

在本地完成操作并提交给本地仓库后，若需要同远程仓库同步，则需要推送仓库。

```bash
git push -u origin master
# 推送本地仓库到远程仓库主分支
```

如果你想要在其他机器，例如你的服务器将源码下载到本地，你可以通过克隆仓库和拉取仓库最新进度来将远程仓库的最新源码同步到服务器中。在这个步骤中不要忘了为服务器配置SSH密钥并添加到Github上。

```bash
git clone <url>
# 克隆远程仓库
```

抓取与拉取

```bash
git fetch
# 抓取远程仓库但不进行分支

git merge origin/master
# 将远程仓库的主分支合并到本地主分支上
```

```bash
git pull
# 拉取远程仓库并直接合并
```



## 创建与合并分支

```bash
git branch
# 查看分支

git branch <branch name>
# 创建分支
```

```bash
git checkout <branch name>
# 切换到分支

git checkout -b <branch name>
# 切换分支，如果不存在就创建
```

```bash
git merge <branch name>
# 将分支合并到本分支上

git branch -d <branch name>
# 删除分支

git branch -D <branch name>
# 强制删除分支
```



## 查看和回溯历史提交

查看历史提交

```bash
git log
# 查看历史提交

git log --pretty=oneline --abbrev-commit --all --graph
# --pretty=oneline 将每一次记录仅显示一行
# --abbrev-commit 优化提交信息
# --all 所有信息
# --graph 图像化开发线

alias "gitlog"="git log --pretty=oneline --abbrev-commit --all --graph"
# 将gitlog赋予后面一段命令的含义，查询时可直接用gitlog代替
```

## 开发流程

![git](../../img/15.jpg)

## 附录 指令速查

\- 基本操作

- git init 初始化仓库
- gitlog 显示提交记录
- git add <filename> 添加文件到暂存区
- git commit -m 'commit message' 提交更变

\- 分支切换类

- git checkout <branch name> 切换分支
- git checkout -b <branch name> 创建并切换到分支

\- 远程操作

- git clone <remote address> 克隆仓库
- git pull 拉取仓库的修改并合并
- git push [--set-upstream] origin <branch name> 推送本地仓库修改到远程分支
