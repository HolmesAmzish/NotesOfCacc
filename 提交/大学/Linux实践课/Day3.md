# **Linux实训练习-Day3**

1. 按照课件中的步骤，进行挂载一个新硬盘的操作，并展示最后成功的截图

   ```bash
   fdisk /dev/sda
   # 我添加的新硬盘是sda
   
   mkfs.ext4 /dev/sda
   # 格式化分区
   
   mkdir /data
   # 创建挂载点
   
   mount /dev/sda /data
   # 挂载
   
   # 后面设置默认挂载
   ```

   ![屏幕截图 2024-06-27 140933](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 140933.png)

   ![屏幕截图 2024-06-27 141120](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 141120.png)

   最后成功将新硬盘挂载到/data文件夹

2. 简述Http的工作流程

   客户端通过发送HTTP请求获取资源或提交数据，服务器接收请求后处理并返回HTTP响应，响应包括状态码表示请求处理结果和可能的资源内容。HTTP使用TCP连接，并支持持久连接和安全扩展如HTTPS来保护数据传输安全性，同时支持各种扩展如Cookie、缓存控制等以实现更丰富的功能。

3. 简述HTTP的POST与GET方法的区别

   **GET**：参数通过URL传递。GET请求的参数被附加在URL的末尾，并通过查询字符串传递。例如：

   ```http
   GET /search?q=example HTTP/1.1
   Host: www.example.com
   ```

   **POST**：参数通过请求体传递。POST请求的参数不会显示在URL中，而是在请求的主体中传递。例如：

   ```http
   POST /submit-form HTTP/1.1
   Host: www.example.com
   Content-Type: application/x-www-form-urlencoded
   
   field1=value1&field2=value2
   ```

4. 展示一下nginx的运行成功页面

   ```bash
   apt install -y nginx
   systemctl enable --now nginx
   ```

   ![屏幕截图 2024-06-27 141453](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 141453.png)

   这里由于debian自带了apache2作为http服务器，在开启nginx时发生了报错，故将apache2先停止。

   ```bash
   systemctl disable --now apache2
   systemctl restart nginx
   systemctl status nginx
   ```

   ![屏幕截图 2024-06-27 141621](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 141621.png)

   最后显示服务已开启，在浏览器输入地址后出现页面，同时由于前面的原因此处时apache2给的初始页面。

   ![屏幕截图 2024-06-27 141654](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 141654.png)

5. 完成练习：基础网页的搭建，将最后的XXX‘s换成你自己的名字；加分项：页面美观者酌情加分（对前端代码基础的可尝试）

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>个人页面</title>
       <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
       <style>
           body {
               font-family: 'Arial', sans-serif;
               line-height: 1.6;
           }
           .jumbotron {
               background: #333;
               color: #fff;
               padding: 50px 25px;
           }
           .nav-link {
               color: #fff !important;
           }
           .nav-link:hover {
               color: #f0ad4e !important;
           }
           .skills .progress-bar {
               background: #f0ad4e;
           }
           .project-img {
               max-height: 200px;
               object-fit: cover;
           }
       </style>
   </head>
   <body>
   
       <!-- 导航栏 -->
       <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
           <a class="navbar-brand" href="#">我的个人网站</a>
           <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
               <span class="navbar-toggler-icon"></span>
           </button>
           <div class="collapse navbar-collapse" id="navbarNav">
               <ul class="navbar-nav ml-auto">
                   <li class="nav-item">
                       <a class="nav-link" href="#about">关于我</a>
                   </li>
                   <li class="nav-item">
                       <a class="nav-link" href="#skills">技能</a>
                   </li>
                   <li class="nav-item">
                       <a class="nav-link" href="#projects">项目</a>
                   </li>
                   <li class="nav-item">
                       <a class="nav-link" href="#contact">联系我</a>
                   </li>
               </ul>
           </div>
       </nav>
   
       <!-- 个人简介 -->
       <div class="jumbotron text-center" id="about">
           <h1 class="display-4">你好，我是盛子涵</h1>
           <p class="lead">一名热爱编程的全栈开发者</p>
           <p>正在学习C++, Python, Java和机器学习</p>
           <a href="#" class="btn btn-primary btn-lg">下载简历</a>
       </div>
   
       <!-- 技能展示 -->
       <section class="container my-5" id="skills">
           <h2 class="text-center">我的技能</h2>
           <div class="row mt-4">
               <div class="col-md-6">
                   <h5>C++</h5>
                   <div class="progress mb-3">
                   </div>
                   <h5>Python</h5>
                   <div class="progress mb-3">
                   </div>
               </div>
               <div class="col-md-6">
                   <h5>HTML & CSS</h5>
                   <div class="progress mb-3">
                   </div>
                   <h5>SQL</h5>
                   <div class="progress mb-3">
                   </div>
               </div>
           </div>
       </section>
   
       <!-- 项目展示 -->
       <section class="container my-5" id="projects">
           <h2 class="text-center">我的项目</h2>
           <div class="row mt-4">
               <div class="col-md-4 mb-4">
                   <div class="card">
                       <div class="card-body">
                           <h5 class="card-title">在线社区</h5>
                           <p class="card-text">网络社区设计和运维。</p>
                           <a href="http://val.arorms.cn" class="btn btn-primary">查看项目</a>
                       </div>
                   </div>
               </div>
               <div class="col-md-4 mb-4">
                   <div class="card">
                       <div class="card-body">
                           <h5 class="card-title">深度学习演示系统</h5>
                           <p class="card-text">用于演示机器学习算法的一个网站。</p>
                           <a href="#" class="btn btn-primary">仍在进行</a>
                       </div>
                   </div>
               </div>
           </div>
       </section>
   
       <!-- 联系表单 -->
       <section class="container my-5" id="contact">
           <h2 class="text-center">联系我</h2>
           <form class="mt-4">
               <div class="form-row">
                   <div class="form-group col-md-6">
                       <label for="inputName">姓名</label>
                       <input type="text" class="form-control" id="inputName" placeholder="你的姓名">
                   </div>
                   <div class="form-group col-md-6">
                       <label for="inputEmail">邮箱</label>
                       <input type="email" class="form-control" id="inputEmail" placeholder="你的邮箱">
                   </div>
               </div>
               <div class="form-group">
                   <label for="inputMessage">信息</label>
                   <textarea class="form-control" id="inputMessage" rows="4" placeholder="你的信息"></textarea>
               </div>
               <button type="submit" class="btn btn-primary">发送</button>
           </form>
       </section>
   
       <!-- 页脚 -->
       <footer class="bg-dark text-white text-center py-3">
       </footer>
   
       <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
       <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
   </body>
   </html>
   ```

   由于还没有设置php等，也没有时间写了，先放在这。

   ![image-20240627150212669](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627150212669.png)

6. 通过编辑配置文件，在8000端口上开辟一个新页面，在页面上打印一个LOGO或简笔画。请提供截图并简述操作的过程。

   在相应位置首先准备好logo.png和html文件，用于显示。

   ```html
   <center><img src="logo-red.png" alt=""></center>
   ```

   然后到`/etc/nginx/sites-available/`编辑配置文件

   ```ini
   server {
       listen 8000;
       server_name example.com;
   
       # 网站根目录
       root /var/www/logo;
       index index.html index.htm;
   
       # 处理静态文件
       location / {
           try_files $uri $uri/ =404;
       }
   }
   ```

   ```bash
   ln -s /etc/nginx/sites-available/logo /etc/nginx/sites-enable/
   # 启用这个
   
   nginx -t
   # 测试配置文件
   
   systemctl reload nginx
   # 重新载入配置
   ```

   用浏览器打开地址并指定8000端口访问

   ![image-20240627152209649](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627152209649.png)

7. 通过编辑配置文件，在8001端口上开辟一个新页面，并要求它的页面文件要放在/tmp/html/下（没有目录自行创建）,页面内容随意。请提供截图并简述操作的过程。

   同上，首先在`/tmp/html`准备好相关文件，这里我复制了一个简单的烟花。

   `/tmp/html/index.html`

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Fireworks Display</title>
       <style>
           body, html {
               margin: 0;
               padding: 0;
               overflow: hidden;
               background: black;
           }
           #canvas {
               position: absolute;
               top: 0;
               left: 0;
           }
       </style>
   </head>
   <body>
       <canvas id="canvas"></canvas>
   
       <!-- 引用烟花效果的JavaScript文件 -->
       <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js"></script>
       <script>
           // 烟花效果脚本
           const canvas = document.getElementById('canvas');
           const ctx = canvas.getContext('2d');
           let width = canvas.width = window.innerWidth;
           let height = canvas.height = window.innerHeight;
           const particles = [];
   
           function createParticle(x, y) {
               const particle = {
                   x: x,
                   y: y,
                   alpha: 1,
                   color: `hsl(${Math.random() * 360}, 100%, 50%)`,
                   radius: Math.random() * 5 + 2,
                   vx: Math.random() * 4 - 2,
                   vy: Math.random() * 4 - 2
               };
               particles.push(particle);
           }
   
           function render() {
               ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
               ctx.fillRect(0, 0, width, height);
   
               particles.forEach((particle, index) => {
                   particle.x += particle.vx;
                   particle.y += particle.vy;
                   particle.alpha -= 0.01;
   
                   if (particle.alpha <= 0) {
                       particles.splice(index, 1);
                   } else {
                       ctx.globalAlpha = particle.alpha;
                       ctx.fillStyle = particle.color;
                       ctx.beginPath();
                       ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
                       ctx.fill();
                   }
               });
   
               requestAnimationFrame(render);
           }
           
           function launchFirework() {
               const x = Math.random() * width;
               const y = Math.random() * height;
               for (let i = 0; i < 100; i++) {
                   createParticle(x, y);
               }
           }
   
           setInterval(launchFirework, 500);
           render();
   
           window.addEventListener('resize', () => {
               width = canvas.width = window.innerWidth;
               height = canvas.height = window.innerHeight;
           });
       </script>
   </body>
   </html>
   ```

   到`/etc/nginx/sites-available/test`编辑

   ```ini
   server {
       listen 8001;
       server_name example.com;
   
       # 网站根目录
       root /tmp/html;
       index index.html index.htm;
   
       # 处理静态文件
       location / {
           try_files $uri $uri/ =404;
       }
   }
   ```

   ```bash
   ln -s /etc/nginx/sites-available/test /etc/nginx/sites-enable/
   nginx -t
   systemctl reload nginx
   ```

   浏览器访问ip地址并访问8001端口

   ![image-20240627154714969](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627154714969.png)

8. Nginx配置文件中的worker_processes指令是做什么用的？

   调整Nginx的工作进程数量，一个进程可以处理一定数量的并发数量。一般大于等于机器的CPU核数。

   ```ini
   worker_processes 4;
   ```

9. 在Nginx搭建的网页中，使用自签名证书，实现HTPPS访问，展示截图

   首先自己生成证书

   ```bash
   mkdir /etc/nginx/ssl
   cd /etc/nginx/ssl
   openssl genrsa -out selfsigned.key 2048
   openssl req -new -x509 -key selfsigned.key -out selfsigned.crt -days 365
   ```

   ![image-20240627163538359](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627163538359.png)

   然后回到配置文件去修改他的设置，设置他的HTTPS，以及证书的路径。

   ```ini
   server {
       listen 80;
       server_name example.com www.example.com;
   
       # 重定向HTTP到HTTPS
       return 301 https://$host$request_uri;
   }
   
   server {
       listen 443 ssl;
       server_name example.com www.example.com;
   
       # SSL证书文件路径
       ssl_certificate /etc/nginx/ssl/selfsigned.crt;
       ssl_certificate_key /etc/nginx/ssl/selfsigned.key;
   
       ssl_protocols TLSv1.2 TLSv1.3;
       ssl_prefer_server_ciphers on;
       ssl_ciphers "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:AES256+EECDH:AES256+EDH";
   
       root /var/www/html;
       index index.html index.htm;:
   
       location / {
           try_files $uri $uri/ =404;
       }
   
       # 自定义404错误页面
       error_page 404 /404.html;
       location = /404.html {
           internal;
       }
   }
   ```

   回到浏览器，通过IP地址访问，他会被重定向到https。

   ![image-20240627163401741](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627163401741.png)

10. 展示你的机器中Nginx的错误日志和访问日志

    ```bash
    tail -f /var/log/nginx/error.log
    ```

    ![image-20240627155633791](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627155633791.png)

    ```bash
    tail -f /var/log/nginx/access.log
    ```

    ![image-20240627155754424](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627155754424.png)

11. 将默认的Nginx错误日志和访问日志的路径修改为/tmp/log下，并展示配置截图与结果

    在配置文件添加修改路径

    ```ini
    server {
        listen 80;
        server_name example.com www.example.com;
        return 301 https://$host$request_uri;
    }
    
    server {
        listen 443 ssl;
        server_name example.com www.example.com;
        ssl_certificate /etc/nginx/ssl/selfsigned.crt;
        ssl_certificate_key /etc/nginx/ssl/selfsigned.key;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;
        ssl_ciphers "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:AES256+EECDH:AES256+EDH";
        root /var/www/html;
        index index.html index.htm;
        
    	access_log /tmp/log/access.log;
        error_log /tmp/log/error.log;
        # 修改路径
    
        location / {
            try_files $uri $uri/ =404;
        }
    
        error_page 404 /404.html;
        location = /404.html {
            internal;
        }
    }
    
    ```

    ![image-20240627164350586](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240627164350586.png)

12. 额外加分项：Nginx除了使用apt直接安装外，还可以使用编译的方式进行安装，请自行研究学习后进行安装，最后展示截图（提示：编译安装前记得卸载掉apt方式安装的Nginx）

    ```bash
    wget http://nginx.org/download/nginx-1.22.0.tar.gz
    tar -zxvf nginx-1.22.0.tar.gz
    cd nginx-1.22.0
    
    apt install build-essential libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev wget
    ./configure
    make
    make install
    # 编译安装nginx
    ```

    ![屏幕截图 2024-06-27 230235](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 230235.png)

    ![屏幕截图 2024-06-27 230356](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 230356.png)

    ```bash
    cd /usr/local/nginx/sbin
    ./nginx
    ```

    ![屏幕截图 2024-06-27 230407](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 230407.png)

    这里发现无法打开，提示地址已经被使用，则关闭冲突的进程。

    ```bash
    lsof -i :80
    kill pid
    
    ./nginx
    ```

    ![屏幕截图 2024-06-27 230421](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-27 230421.png)

    开启没有报错说明启动成功。后期如果需要设置成服务，则需要进入`/lib/systemd/system/`编辑service文件创建服务。