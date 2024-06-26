# Linux 实训练习 - Day 2

1. 创建一个新用户（命名随意），修改其密码，请展示/etc/passwd文件中刚刚创建的用户信息，提供截图。

   ```bash
   useradd newuser
   # create new user
   
   passwd newuser
   ```

   

2. 创建一个新文件1.txt，对其权限进行修改。将其所有者更改为第一题创建的用户，让所有者拥有所有权限，所属组拥有可读可写权限，其他人拥有可读权限，请提供截图。

   ```bash
   touch 1.txt
   echo "Hello, World!" > 1.txt
   # create a file and write something
   
   chmod newuser 1.txt
   # change the owner of file
   
   chmod 764 1.txt
   ```

   

3. 查找系统中的sshd_config文件所在的位置，请提供截图

   ```bash 
   find / -name "sshd_config"
   # find file at root
   ```

   

4. 安装并使用cowsay命令，使用cowsay命令，用其他动物打印出一句话

   ```bash
   whereis cowsay
   export PATH=$PATH:/usr/games
   # add to path
   
   cowsay -f dragon "The quieter you become, the more you are able to hear."
   ```

   

5. 练习：Linux有一个命令可以在屏幕上跑小火车，请自行研究后，截图完成的成果

   ```bash
   apt install sl -y
   sl -a
   ```

   

6. 创建一个新的用户组test，再创建一个新用户testIT，将用户testIT添加进去

   ```bash
   groupadd test
   useradd testIT
   usermod -aG test testIT
   id testIT
   ```

   

7. 自行创建所需的文件和用户：将file1.txt的所有者更改为user1，所属组更改为group1（使用chown命令）。使用chmod命令将file1.txt的权限设置为所有者具有读写执行权限，所属组具有读执行权限，其他用户具有读权限（权限码为755）。

   ```bash
   touch file1.txt
   groupadd group1
   useradd -g group1 user1
   chown user1:group1 file1.txt
   chmod 755 file1.txt
   
   ls -l file1.txt
   ```

   

8. 在根目录下查找所有以.txt结尾的文件。

   ```bash
   find / -type f -name "*.txt"
   ```

   

9. 复制/etc/passwd文件到当前用户的家目录，并重命名为my_passwd.txt。将my_passwd.txt移动到/tmp目录下。

   ```bash
   cp /etc/passwd ~
   mv passwd my_passwd.txt
   mv ~/my_passwd.txt /tmp
   ```

   

10. 使用echo命令将“This line was added using echo.”追加到example.txt文件的末尾。使用sed命令将example.txt文件中所有的“old”替换为“new”。

    ```bash
    touch example.txt
    echo "This line was added using echo." > example.txt6
    sed 's/old/new/g' example.txt
    ```

    

