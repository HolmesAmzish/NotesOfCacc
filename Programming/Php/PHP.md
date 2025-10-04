# 基本

## PHP 程序中的注释

| 代码         | 效果     |
| ------------ | -------- |
| // commit    | 单行注释 |
| # commit     | 单行注释 |
| /* commit */ | 多行注释 |



## PHP 中的输出方法

1. echo

   ```php
   echo "<h2>Hello world</h2>";
   echo "This", "string", "was", "made", "with multiple parameters.";
   ```

2. print

   ```php
   print "<h2>Hello world</h2>";
   print "My name is nulla";
   ```

3. var_dump()

   ```php
   $boolVar = TRUE;
   $strVar = "apple";
   $intVar = 1;
   $cars = array("Volvo", "BMW", "SAAB");
   
   var_dump($boolVar);
   var_dump($strVar);
   var_dump($intVar);
   var_dump($cars);
   ```



## 常量

1. 定义常量

   常量一旦定义就不能修改或者却笑定义。按照惯例，常量名采用大写，但不需要添加`$`符号。与变量不同，常量贯穿整个脚本，是全局自动的。

   ```php
   define("PI", 3.14);
   echo "The value of const variable PI is: ", PI;
   ```



## 变量数据类型

1. 布尔型

   - 整型值和浮点型：0为FALSE，非0为TRUE。
   - 字符串：空字符串和“0”为FALSE，其他为TRUE。
   - 数组：无成员变量的数组为FALSE，其他为TRUE。
   - 特殊类型：NULL为FALSE，包括尚未设定的变量。

2. 整型

   ```php
   $intVar = 123;
   $intVar = 0123;
   $intVar = 0x1A;
   ```

3. 浮点型

   ```php
   $floatVar = 1.234;
   $floatVar = 1.2e3;
   ```

4. 字符串

   ```php
   $str = "PHP Words";
   
   $v = "string";
   $s = "PHP $v";
   
   // add '/' to out put the original string
   $v = "string";
   $s = "PHP \$v";
   ```

   | 转义字符 | 含义       |
   | -------- | ---------- |
   | `\n`     | 换行符     |
   | `\r`     | 回车符     |
   | `\t`     | 水平制表符 |
   | `\\`     | 反斜线     |
   | `\$`     | 美元符号   |
   | `\"`     | 双引号     |

5. 数组

   ```php
   $subjects = array("Maths", "History", "Physics");
   var_dump($subects)
   
   $user = array("name"=>"Tom", "age"=>20);
   var_dump($user);
   ```

6. 对象

   ```php
   class Student{
       var $name;
       var $age;
       function printStudent(){
           echo 'Name: '.$this->name.', Age: '.$this->age;
       }
   }
   
   $s = new Student;
   $s->name = 'John';
   $s->age = 19;
   $s->printStudent();
   ```

7. 资源

   资源是一种特殊类型的变量，保存了到外部资源的一个引用。资源常用来保存打开文库、数据库连接和图形画布等句柄。

   ```php
   $link = mysql_connect("localhost", "root", "1");
   var_dump($link);
   ```



## 变量类型转换

| 关键字                    | 转换类型     |
| ------------------------- | ------------ |
| (int), (integer)          | 转换成整型   |
| (bool), (boolean)         | 转换成布尔型 |
| (float), (double), (real) | 转换成浮点型 |
| (string)                  | 转换成字符串 |
| (array)                   | 转换成数组   |
| (object)                  | 转换成对象   |



## PHP 对变量的操作

1. 判断类型

   - `is_integer()`
   - `is_string()`
   - `is_double()`
   - `is_array()`

2. 获取变量的类型

   使用预定义函数`gettype()`取得一个变量的类型，它接受一个变量作为参数，返回这个变量的类型。

   ```php
   $s = "This is a string";
   $i = 10;
   echo 'The data type of $s is', gettype($s).'<br>';
   ```

3. 判断一个变量是否已被定义

   使用预定义函数`isset()`判断一个变量是否已被定义，他接受一个变量作为参数，如果返回值为`TRUE`,则说明这个变量被定义过。

4. 删除一个变量

   使用`unset()`函数删除指定的变量。

   ```php
   $a = 12;
   if (isset($a)) {
       echo '$a is a ', gettype($a), ', variable type, the value of it is ', $a, '<br>';
   } else echo 'There is no variable $a<br>';
   unset($a);
   if (isset($a)) {
       echo '$a is a ', gettype($a), ', variable type, the value of it is ', $a, '<br>';
   } else echo 'There is no variable $a<br>';
   ```




## PHP运算符

| 运算符 | 描述       |
| ------ | ---------- |
| x + y  | 和         |
| x - y  | 差         |
| x * y  | 积         |
| x / y  | 商         |
| x % y  | 取余       |
| -x     | 相反数     |
| ~x     | 二进制取反 |
| a . b  | 连接字符串 |

## 文件包含

`require_once` 和 `require` 在PHP中都是文件包含指令，它们的主要区别在于处理重复包含同一文件的行为上：

1. **require**：
   - 当使用 `require` 语句时，如果指定的文件存在，则将其内容包含并执行。
   - 如果所包含的文件在当前脚本执行期间已经包含了该文件，并且再次遇到 `require`，则该文件会再次被包含和执行。
   - 若所包含的文件不存在或者在包含过程中发生了错误（如语法错误），`require` 将导致一个致命错误（E_COMPILE_ERROR）并停止脚本执行。
2. **require_once**：
   - 类似于 `require`，但它具有额外的检查功能。
   - 使用 `require_once`，即使在同一脚本中多次遇到相同的文件包含指令，该文件也只会被包含一次。
   - 这样可以防止由于重复包含而引发的问题，例如函数或类定义的重复，以及可能由此带来的不可预知的副作用。

总结来说，当确保某个文件在整个脚本生命周期内只被包含一次时，通常推荐使用 `require_once`。这有助于避免因意外重复包含而导致的逻辑错误或资源浪费。



# 流程控制

## 数组

```php
$str = "";
$hobby = array('Art', 'Photography', 'Sports');
foreach ($hobby as $key => $value) {
    $str .= $value;
    if ($key < count($hobby) - 1) 
        $str .= ', ';
}
echo $str, '<br>';
```

foreach遍历$hobby数组，并将$hobby数组中的键值赋予$key，每个键值相对应的数组的值赋予$value。



# 网页交互

## 预定义数组

### $_POST

当表单被提交时，表单中具有name属性的表单元素会将用户填写的内容提交给服务器，PHP会将表单数据保存在`$_POST`数组中。他是一个关联数组，数组的键名对应表单元素的name属性，值是用户填写的内容。

```php+HTML
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
Username: <input type="text" name="username">
Passowrd: <input type="password" name="password">
<input type="submit" value="Login">
</form>
<?php
if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    echo "Your username is".$username.'<br>';
    echo "Your password is".$password;
}
?>
```

其中form的action属性设置为`<?php echo $_SERVER['PHP_SELF'];?>`，也就是将表单提交给自己处理，还可以将其设置成`action=""`或者不设置action属性，使其默认提交给自己。而method属性赋予post，就是以post方式将表单信息提交，如果不填，那么默认属性将是get方式。

### $_GET

```PHP+HTML
<form>
Username: <input type="text" name="username">
Passowrd: <input type="password" name="password">
<input type="submit" value="Login">
</form>
<?php
if (isset($_GET['username']) && isset($_GET['password'])) {
    $username = $_GET['username'];
    $password = $_GET['password'];
    echo "Your username is".$username.'<br>';
    echo "Your password is".$password;
}
?>
```

其中，GET传参会显示在URL中，使得传输的数据可见，其次长度也有限制，所以一般适合一些小型且不敏感的数据传输。



# 文件上传



