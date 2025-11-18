# 流

# 输入与输出

# XML

# 网络

## 连接服务器

### telnet

```bash
telnet time-a.nist.gov 13
```

### 套接字

```java
var s = new Socket("time-a.nist.gov", 13);
```

用于打开一个套接字，负责启动该程序内部和外部之间的通信。如果连接失败，会抛出一个`UnknownHostException`，如果存在其他异常，则会抛出`IOException`。

> [!NOTE]
> 
> `java.net.Socket`
> 
> - Socket(String host, int port)
>   
>   构建一个套接字，用来连接给定的主机和端口
> 
> - InputStream getInputStream()
> 
> - OutputStream getOutputStream()
>   
>   获取可以从套接字中读取的数据流和可以写出的数据流

### 套接字超时

```java
var s = new Socket(. . .);
s.setSoTimeout(10000); // time out after 10 seconds
```

如果已经为套接字设置了超时值，并且之后的读操作和写操作在没有完成之前就超过了时间限制，那么这些操作就会抛出`SocketTimeoutException`异常，可以捕获这个异常对超时作出反应。

```java
try {
    InputStream in = s.getInputStream();
    . . .
} catch (SocketTimeoutException) {
    react to timeout
}
```

> [!NOTE]
> 
> `java.net.Socket`
> 
> - Socket()
>   
>   创建一个还未被连接的套接字
> 
> - void connect(SocketAddress address)
>   
>   将该套接字连接到给定地址
> 
> - void connect(SocketAddress address, int timeoutInMilliseconds)
>   
>   如果给定时间没有响应则返回
> 
> - void setSoTimeout(int timeoutInMilliseconds)
> 
> - boolean isConnected()
>   
>   判断是否已经连接
> 
> - boolean isClosed()

### 因特网地址

一个因特网地址由4个字节组成（IPv6是16个字节）。如果需要主机名和因特网地址之间进行转换，需要使用`InetAddress`类。

```java
InetAddress address = InetAddress.getByName("cn.bing.com");
```

> [!NOTE]
> 
> `java.net.InetAddress`
> 
> - static InetAddress getByName(String host)
> 
> - static InetAddress[] getByName(String host)
> 
> - static InetAddress getLocalHost()
>   
>   为本地主机创建一个InetAddress对象
> 
> - byte[] getAddress()
>   
>   返回一个包含数字型地址的字节数组。
> 
> - String getHostAddress()
>   
>   返回一个十进制数组成的字符串
> 
> - String getHostName()
>   
>   返回主机名

```java
import java.net.InetAddress;

/**
 * This program demonstrates thee InetAddress class. Supply a host name as command-line
 * argument, or run without command-line arguments to see the address of the local host.
 * @version 1.02 2012-06-05
 * @author Cay Horstmann
 */

public class InetAddressTest {
    public static void main(String[] args) throws Exception {
        if (args.length > 0) {
            String host = args[0];
            InetAddress[] addresses = InetAddress.getAllByName(host);
            for (InetAddress addr : addresses) {
                System.out.println(addr);
            }
        } else {
            InetAddress addr = InetAddress.getLocalHost();
            System.out.println(addr);
        }
    }
}
```

## 实现服务器

### 服务器套接字

一旦启动了服务器程序，他便会等待某个客户端连接到他的端口。

```java
var s = new ServerSocket(8189);
Socket incoming = s.accept();
```

建立一个负责监控端口8189的服务器，并告诉服务器不停地等待，直到由客户端连接到这个端口。一旦有人通过网络发送了正确的请求连接，并一次连接到了端口上，该方法就返回一个表示链接已经建立的Socket对象。

```java
InputStream inStream = incoming.getInputStream();
OutputStream outStream = incoming.getOutputStream();
```

服务器发送给服务器输出流的所有信息都会成为客户端程序的输入，停驶来自客户端程序的所有输出都会被包含在服务器输入流中。

```java
var in = new Scanner(inStream, StandardCharset.UTF_8);
var out = new PrintWriter(new OutputStreamWriter(OutStream, StandardCharsets.UTF_8),
                         true /* autoFlush */);
```

```java
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

/**
 * This program implements a simple server that listens to port 8189 and echoes back all
 * client input.
 * @version 1.22 2018-03-17
 * @author Cay Horstmann
 */
public class EchoServer {
    public static void main(String[] args) throws IOException {
        // establish server socket
        try (var s = new ServerSocket(8189)) {
            // wait for client connection
            try (Socket incoming = s.accept()) {
                InputStream inStream = incoming.getInputStream();
                OutputStream outStream = incoming.getOutputStream();
                try (var in = new Scanner(inStream, StandardCharsets.UTF_8)) {
                    var out = new PrintWriter(new OutputStreamWriter(outStream, StandardCharsets.UTF_8), true);
                    out.println("Hello! Enter BYE to exit.");
                    
                    // echo client input
                    boolean done = false;
                    while (!done && in.hasNext()) {
                        String line = in.nextLine();
                        out.println("Echo: " + line);
                        if (line.trim().equals("BYE")) {
                            done = true;
                        }
                    }
                }
            }
        }
    }
}

```

> ![NOTE]
> 
> `java.net.ServerSocket`
> 
> - ServerSocket(int port)
>   
>   创建一个监听端口的服务器套接字
> 
> - Socket accept()
>   
>   等待连接，该方法阻塞当前线程直到建立连接未知。该方法返回一个 Socket 对象，程序可以通过这个对象与连接中的客户端进行通信。
> 
> - void close()
>   
>   关闭服务器套接字。

# 数据库

# 日期和时间API

## 本地日期

LocalDate是带有年月日的日期。通过哦构建LocalDate对象，使用now或者of静态方法。

```java
LocalDate today = LocalDate.now(); // Today's date
LocalDate alonzosBirthday = LocalDate.of(1903, 6, 13);
alonzosBirthday = LocalDate.of(1903, Month.JUNE, 14); // Uses the Month enumeration
```

> [!NOTE]
> 
> `java.time.LocalDate`
> 
> - static LocalDate now()
> - static LocalDate of(int year, int month, int dayOfMonth)
> - LocalDate plus(TemporalAmount amountToAdd)
> - LocalDate minus(TemporalAmount amountToSubtract)

## 本地时间

```java
LocalTime rightNow = LocalTime.now();
LocalTime bedtime = LocalTime.of(22, 30); // or LocalTime.of(22, 30, 0)

LocalTime wakeup = bedtime.plusHour(8); // wakeup is 6:30:00
```

> [!NOTE]
> 
> `java.time.LocalTime`
> 
> - static LocalTime now()
> - static LocalTime of(int hour, int minute, int second)
> - LocalTime (plus|minus)(Hours|Minutes|Seconds|Nanos)(long number)
> - int getHour()
> - int getMinute()
> - int getSecond()
> - boolean isBefore(LocalTime other)
> - boolean isAfter(LocalTime other)

## 本地日期时间

`LocalDateTime` 是带有日期（年、月、日）和时间（时、分、秒）的日期时间对象。可以通过 `now` 方法获取当前的日期时间，或者通过 `of` 方法自定义创建。

```
java复制代码LocalDateTime now = LocalDateTime.now(); // 当前日期和时间
LocalDateTime customDateTime = LocalDateTime.of(2024, 11, 25, 10, 15, 30); // 自定义日期和时间
LocalDateTime anotherDateTime = LocalDateTime.of(2024, Month.NOVEMBER, 25, 10, 15); // 使用 Month 枚举
```

时间操作

```
java复制代码LocalDateTime futureDateTime = now.plusDays(10).plusHours(3); // 当前时间加10天3小时
LocalDateTime pastDateTime = customDateTime.minusWeeks(2).minusMinutes(15); // 自定义时间减2周15分钟
```

```
java复制代码boolean isBefore = now.isBefore(futureDateTime); // 判断当前时间是否在未来时间之前
boolean isAfter = now.isAfter(pastDateTime); // 判断当前时间是否在过去时间之后
```

可以从 `LocalDateTime` 对象中提取日期和时间部分，分别生成 `LocalDate` 和 `LocalTime`。

```
java复制代码LocalDate datePart = customDateTime.toLocalDate(); // 提取日期部分
LocalTime timePart = customDateTime.toLocalTime(); // 提取时间部分
```

> [!NOTE]
> 
> `java.time.LocalDateTime`
> 
> - static LocalDateTime now() 
>   
>   获取当前日期时间。
> 
> - static LocalDateTime of(int year, int month, int dayOfMonth, int hour, int minute, int second)
>   
>   根据指定的日期和时间创建对象。
> 
> - LocalDateTime plus(TemporalAmount amountToAdd)
>   
>   在当前时间加上指定时间量。
> 
> - LocalDateTime minus(TemporalAmount amountToSubtract)
>   
>   从当前时间减去指定时间量。
> 
> - boolean isBefore(LocalDateTime other)
>   
>   判断当前日期时间是否早于另一个日期时间。
> 
> - boolean isAfter(LocalDateTime other)
>   
>   判断当前日期时间是否晚于另一个日期时间。
> 
> - LocalDate toLocalDate()
>   
>   转换为 `LocalDate`。
> 
> - LocalTime toLocalTime()
>   
>   转换为 `LocalTime`。

# 国际化

# 脚本编译与注解处理

# 高级Swing和图形化编程

# 本地方法
