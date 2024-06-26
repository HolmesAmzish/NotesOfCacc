# **Linux实训练习-Day1**

1. 将主机名称修改为自己的学号，并提供截图

   ```bash
   hostnamectl set-hostname 3230611081
   ```

   ![屏幕截图 2024-06-25 145024](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-25 145024.png)

2. 展示一下/etc目录下的所有文件和目录信息，提交截图

   ```bash
   ls /etc
   ```

   ![image-20240625145112217](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240625145112217.png)

3. 修改命令别名，能够使用showip命令查看当前ip地址，提交截图

   ```bash
   alias showip="ip addr"
   ```

   ![屏幕截图 2024-06-25 144908](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-25 144908.png)

4. 简述vim编辑器的三种模式，并在Linux系统上操作，并上传三种模式的截图

   简述：命令模式，插入模式，底线命令模式

   截图：

   ![屏幕截图 2024-06-25 144658](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-25 144658.png)

   ![屏幕截图 2024-06-25 144721](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-25 144721.png)

   ![屏幕截图 2024-06-25 144746](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-25 144746.png)

5. 使用vim编辑进入远程连接工具的初始显示页面，展示截图

第一行文本：

Welcome To xxx's Host!

第二行：输入一个Logo

你的截图：

```bash
vim .bashrc
```

```bash
echo "Welcome to nulla's host!"
cat freebsd_logo.txt
echo ""
```

```txt
                 ,        ,
                /(        )`
                \ \___   / |
                /- _  `-/  '
               (/\/ \ \   /\
               / /   | `    \
               O O   ) /    |
               `-^--'`<     '
              (_.)  _  )   /
               `.___/`    /
                 `-----' /
    <----.     __ / __   \
    <----|====O)))==) \) /====
    <----'    `--' `.__,' \
                 |        |
                  \       /       /\
             ______( (_  / \______/
           ,'  ,-----'   |
           `--{__________)
```



![屏幕截图 2024-06-25 143810](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-06-25 143810.png)