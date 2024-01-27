# Debian环境下配置code-server服务

## 在服务器下载code-server安装包

首先下载code-server安装包，网址为https://github.com/coder/code-server/releases。 选择对应的版本号，这里Debian使用的安装包是deb文件后缀，同时注意CPU的类型，amd64是amd的CPU，而arm64是intel的CPU，下载到本地。

上传安装包到Debian服务器上，可以通过SSH来进行上传,scp指令上传文件的方法如下：

```powershell
scp file username@hostname:/home/username
#将本地文件“file”上传到指定服务器的/home/username文件夹下
```

## 在服务器安装并设置code-server

首先远程登录服务器并安装code-server

```powershell
ssh username@hostname

cd /home/username
dpkg -i code-server_4.20.0_amd64.deb
#-i是install安装的意思，记得修改对应的版本，保证文件名一样
```

然后设置code-server的设置文件，文件在root/.config/code-server/ 这个文件夹下，名叫config.yaml，如果没有找到这个文件夹或文件，可能是因为没有运行而没有产生设置文件，可以在终端输入code-server启动这个服务再ctrl+c中断掉，对应的设置文件就会产生。然后使用nano打开这个文件进行编辑，修改成如下的样子。

```yaml
bind-addr: 0.0.0.0:8080
auth: password
password: 密码
cert: false
```

其中0.0.0.0是广播地址，意味所有IP都可以连接这台机器的code-server服务，如果有需要可以自己改。将密码改为自己能记住的密码，在稍后登录时需要用到。

## 启动code-server服务并登录

设置开机自启动并现在启动，由于code-server涉及根目录中文件的编辑上传，可以使用root账户进行登录，如果可以，建议设置一个其他账户进行登录。

```bash
systemctl enable --now code-server@root
```

这样，就开启了code-server服务。code-server服务器默认端口为8080，浏览器登录http:xxx.xxx.xxx.xxx:8080即可访问页面，输入密码即可进入code-server进行编辑。