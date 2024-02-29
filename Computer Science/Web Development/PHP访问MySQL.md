# PHP 访问 MySQL 数据库

## 一般步骤

1. 安装并配置MySQL服务器
2. 创建数据库
3. 创建数据库用户
4. 编写PHP代码以连接到MySQL数据库
   1. 创建一个mysqli对象，用于连接到MySQL数据库服务器
   2. 使用链接对象的方法执行查询或者其他数据库操作
   3. 处理返回的结果或者错误消息
   4. 关闭数据库连接释放资源

## 连接数据库

`mysqli_connect()`函数用于连接数据库，该连接可以使用`mysqli_close()`关闭函数。如果连接成功，函数将返回一个表示数据库连接的对象`$link`；如果连接失败，函数将返回FALSE，并向Web服务器发送一条Warning级别的出错消息，

```php
mysqli_connect(host, username, password, db_name, port, socket);
```

除了使用mysqli_connect函数之外，还有面向对象的写法

```php
$conn = new mysqli($servername, $username, $password, $dbname);

$conn = new mysqli;
$conn->connect("host", "username", "password", "database");
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
$conn -> query(SQL command);
```

当通过`query()`函数执行`CREATE`, `INSERT`, `UPDATE`, `DELETE`等非查询语句时，执行成功会返回TRUE，否则返回FALSE。

```php
$conn = new mysqli();
$conn -> connect('localhost' ,'root' ,'password', 'database');
if ($conn->connect_error) {
    die("mysqli_connect failed: ".$conn -> connect_error);
}
$conn->set_charset('utf8');

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

> [!NOTE]
> 在使用 `mysqli::query()` 执行查询时，返回的结果取决于查询的类型：
>
> 1. **对于 SELECT 查询：** 如果查询成功并返回一个结果集，则返回一个对象，可以通过该对象访问查询结果。
> 2. **对于 INSERT、UPDATE、DELETE 查询：** 如果查询成功，则返回 `TRUE`。如果查询失败，则返回 `FALSE`。



## MySQL错误信息

在应用MySQL错误信息查看之前，需要在服务器环境上开启报错，因为报错可以用作SQL注入，默认是关闭的。如果要开启，则前往`/etc/php/8.2/apache2/php.ini`修改，然后重启apache2即可。

```ini
error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT
display_errors = On
```

mysqli创建的对象有以下属性与方法：

- error 用于显示最近一次操作产生的错误信息
- connect_error 用于判断是否连接成功，如果失败会包含一个描述连接错误的字符串
- die() 用于显示错误信息，同时直接中止程序

如果将sql查询结果存入$result中，那么如果$result为空，则表示查询失败了。

```php
<link rel="stylesheet" href="phpstyle.css">
<?php
$db_host = "localhost";
$db_user = "root";
$db_pass = "20230612";
$db_name = "phpTutorial";

$conn = new mysqli;
$conn->connect($db_host, $db_user, $db_pass, $db_name);

if ($conn->connect_error) {
    die("connect failed: " . $conn->connect_error);
} else {
    echo "MySQL connected successfully<br>";
}
// Check the MySQL connection

$sql = "SELECT * FROM user";
$result = $conn->query($sql);

if (!$result) {
    die("Query failed: " . $conn->error);
} else {
    echo "Query successful<br>";
}
// Check the MySQL query

$conn->close();
?>
```

