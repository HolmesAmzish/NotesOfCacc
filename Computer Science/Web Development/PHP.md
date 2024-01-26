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

   ## 常量

   1. 定义常量

      常量一旦定义就不能修改或者却笑定义。按照惯例，常量名采用大写，但不需要添加`$`符号。与变量不同，常量贯穿整个脚本，是全局自动的。

      ```php
      define("PI", 3.14);
      echo "The value of const variable PI is: ", PI;
      ```

      
