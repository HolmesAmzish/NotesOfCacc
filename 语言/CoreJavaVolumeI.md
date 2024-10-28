# Java 的基本程序设计结构

## 运算符

### 强制类型转换

```java
double x = 9.997;
int nx = (int) x;
```

对浮点数进行舍入运算，需要通过Math.round方法。由于round方法默认返回long类型，由于存在信息丢失的可能性，所以只有使用现实的强制类型转换才能够将long类型转换成int类型。

```java
double x = 9.997;
int nx = (int) Math.round(x);
```

## 字符串

### 子串

```java
String greeting = "Hello";
String s = greeting.substring(0, 3);
// 创建一个字符串“Hel”
```

### 拼接

```java
String expletive = "Expletive";
String PG13 = "deleted";
String message = expletive + PG13;
```

repeat方法

```java
String repeated = "Java".repeat(3); // repeated is "JavaJavaJava"
```



### 检测字符串是否相等

```java
s.equals(t);
"Hello".equalsIgnoreCase("hello")
```

### 代码点与代码单元

length 方法将返回采用UTF-16 编码表示给定字符串所需要的代码单元数量。

```java
String greeting = "Hello";
int n = greeting.length(); // is 5
```

要想得到实际长度，即代码点数量，可以调用：

```java
int cpCount = greeting.codePointCount(0, greeting.length());
```

调用s.charAt(n) 将返回位置n的代码单元

```java
char first = greeting.charAt(0); // first is 'H'
char last = greeting.charAt(4); // last is 'o'
```

要想得到第i个码点，应该使用下列语句：

```java
int index = greeting.offsetByCodePoints(0, i);
int cp = greeting.codePointAt(index);
```



## 输入与输出

### 读取输入

Scanner 类定义在`java.util`包中，当时用的类不是定义在基本`java.lang`包中时，一定要使用import来导入相应的包

```java
import java.util.*;
```



nextLine方法将读取一行输入

```java
Scanner in = new Scanner(System.in);
System.out.println("What is your name? ");
String name = in.next();
```

如果想要读取一个单词（以空白符作为分隔符）

```java
String firstName = in.next();
```

读取整数

```java
System.out.println("How old are you? ");
int age = in.nextInt();
```

```java
import java.util.*;

/**
 * This program demonstrates console input.
 * @version 1.10 2004-02-10
 * @author Cay Horstmann
 */
public class InputTest {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // get first input
        System.out.println("What is your name? ");
        String name = in.nextLine();

        // get second input
        System.out.println("How old are you? ");
        int age = in.nextInt();

        // display output on console
        System.out.println("Hello, " + name + ". Next year, you'll be " + (age + 1));
    }
}
```

## 数组

### 数组声明

在生命数组变量是，需要指出数组类型和数组变量的名字。

```java
int[] a;
```

不过这条语句只生命了变量a，并没有将a 初始化为一个真正的数组。应该使用new 操作符创建数组。

```java
int[] a = new int[100]; // or var a = new int[100];
```

### for each 循环

它定义一个变量用于暂存集合中的每一个元素，并执行相应的语句。collection 这一集合表达式必须是一个数组或者是一个实现了Iterable 接口的类对象，例如ArrayList。

```java
for (variable: collection) statement
```

### 数组拷贝

```java
int[] luckyNumbers = smallPrimes;
luckyNumbers[5] = 12; // now smallPrimes[5] is also 12
```

```java
// copy all elements from first array
int[] copiedLuckyNumbers = Arrays.copyOf(luckyNumbers, luckyNumbers.length);

// increase the length of the array
luckyNumbers = Array.copyOf(luckyNumbers, 2 * luckyNumbers.length);
```

### 命令行参数



# 对象与类

## 使用预定义类

### LocalDate 类

`static LocalDate now()`

构造一个表示当前日期的对象。

`static LocalDate of(int year, int month, int day)`

构造一个给定日期的对象

`int getYear()`

`int getMonthValue()`

`int getDayOfMonth()`

获取当前的年月日

```java
import java.time.*;

/**
 * @version 1.5 2015-05-08
 * @author Cay Horstmann
 */
public class CalendarTest {
    public static void main(String[] args) {
        LocalDate date = LocalDate.now();
        int month = date.getMonthValue();
        int today = date.getDayOfMonth();

        date = date.minusDays(today - 1); // set to start of month
        DayOfWeek weekday = date.getDayOfWeek();
        int value = weekday.getValue(); // 1 = Monday, . . . , 7 = Sunday

        System.out.println("Mon Tue Wed Thu Fri Sat Sun");
        for (int i = 1; i < value; i++)
            System.out.print("    ");
        while (date.getMonthValue() == month) {
            System.out.printf("%3d", date.getDayOfMonth());
            if (date.getDayOfMonth() == today)
                System.out.print("*");
            else
                System.out.print(" ");
            date = date.plusDays(1);
            if (date.getDayOfWeek().getValue() == 1)
                System.out.println();
        }
        if (date.getDayOfWeek().getValue() != 1) System.out.println();
    }
}
```

