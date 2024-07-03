# **Linux实训大作业**

1、请按照上课的讲解与笔记，搭建好个人博客，展示一下博客的首页与个人创建的文章截图

首先新增配置文件，并设置根目录和端口，为82。

```bash
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/wordpress.conf
vim /etc/nginx/sites-available/wordpress.conf
ln -s /etc/nginx/sites-available/wordpress.conf /etc/nginx/sites-enable/
nginx -t
systemctl reload nginx
```

其中，wordpress配置文件的内容为

```ini
server {
  listen 82;
  root /var/www/wordpress;
  
  location / {
    index index.php index.html;
  }
  
  location ~ \.php$ {
    fastcgi_pass 127.0.0.1:9000;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    include snippets/fastcgi-php.conf;
  }
}
```

然后下载wordpress到设置的根目录/var/www/wordpress

```bash
cd /var/www
wget https://cn.wordpress.org/latest-zh_CN.tar.gz
tar xzvf latest-zh_CN.tar.gz
```

设置数据库

```bash
mysqladmin password '123'
mysql -uroot -p123
```

```sql
CREATE DATABASE wordpress;
SHOW DATABASES;
```

最后打开浏览器通过浏览器访问82端口的页面，并进行设置。

博客首页截图：

![image-20240628150159319](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240628150159319.png)

个人文章截图：

![屏幕截图 2024-06-28 145919](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-28 145919.png)

![屏幕截图 2024-06-28 145928](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-28 145928.png)

2、按照LNMP架构，在下列开源项目中任选其一（也可自行选取其他开源项目），进行搭建，并截图，截图要展示搭建过程与最后结果

wecenter
typecho
zblog
kodbox
discuz
seafile
.......

首先搜索项目，我选择了typecho

![image-20240628150954744](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240628150954744.png)