# PHP 访问 MySQL 数据库

## 连接数据库

`mysqli_connect()`函数用于连接数据库，该连接可以使用`mysqli_close()`关闭函数。如果连接成功，函数将返回一个表示数据库连接的对象`$link`；如果连接失败，函数将返回FALSE，并向Web服务器发送一条Warning级别的出错消息，

```php
mysqli_connect(host, username, password, db_name, port, socket);
```

除了使用mysqli_connect函数之外，还有面向对象的写法

```php
$conn = new mysqli($servername, $username, $password, $dbname);
```

| 参数     | 描述                         |
| -------- | ---------------------------- |
| host     | 主机名或IP地址               |
| username | MySQL用户名                  |
| password | MySQL密码                    |
| db_name  | 默认使用的数据库             |
| port     | 连接服务器的端口号           |
| socket   | 规定socket或使用已命名的pipe |

以下是连接数据库的基本语句

```php
$db_user = "root";
$db_pass = "20230612";
$db_host = "127.0.0.1"; // localhost
$db_name = "phpTutorial";
$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
if ($conn -> connect_error) {
    die ("link db failure: ".$conn -> connect_error);
} else {
    echo "Connect database [ ".$db_name." ] success<br>";
} // Build the connection between php and MySQL server
```

检查是否连接成功

```php
if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
}
```



## 执行数据库操作

连接MySQL数据库之后，首先需要通过`set_charset()`成员函数设置默认的客户端编码方式，然后通过`query()`成员函数以及其内嵌的SQL命令进行查询、插入、更新、删除等操作，语法结构如下。

```php
Mysqli_connection -> query(SQL command);
```

当通过`query()`函数执行`CREATE`, `INSERT`, `UPDATE`, `DELETE`等非查询语句时，执行成功会返回TRUE，否则返回FALSE。

```php
$conn = new mysqli();
$conn -> connect('localhost' ,'root' ,'password', 'database');
if ($conn -> connect_error) {
    die("mysqli_connect failed: ".$conn -> connect_error);
}
$conn -> set_charset('utf8');

$sql = "CREATE TABLE device (
			id INT PRIMARY KEY AUTO_INCREMENT,
			code VARCHAR(20),
			system VARCHAR(20)
		)";

if ($conn -> query($sql)) {
    echo "Table created successfully";
} else {
    echo "Table created unsuccessfully";
}
```

