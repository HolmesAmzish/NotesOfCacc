# C语言文件操作

## 打开文件

使用`fopen()`函数来创建一个新的文件或者打开一个已有的文件，这个调用会初始化类型**FILE**的一个对象，类型**FILE**包含了所有用来控制流的必要的信息。下面是这个函数待用的原型：

```c
FILE *fptr;
fptr = fopen(const char* filename, const char *mode);
```

在这里，**filename**是字符串，访问模式**mode**是以下字母中的一个：

| 模式 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| r    | 打开一个已有的文本文件，允许读取文件。                       |
| w    | 打开一个文本文件，允许写入文件。如果文件不存在，则会创建一个新文件。在这里，你的程序会从文件的开头写入内容。如果文件存在，则该会被截断为零长度，重新写入。 |
| a    | 打开一个文本文件，以追加模式写入文件。如果文件不存在，则会创建一个新文件。在这里，您的程序会在已有的文件内容中追加内容。 |
| r+   | 打开一个文本文件，允许读写文件。                             |
| w+   | 打开一个文本文件，允许读写文件。如果文件已存在，则文件会被截断为零长度，如果文件不存在，则会创建一个新文件。 |
| a+   | 打开一个文本文件，允许读写文件。如果文件不存在，则会创建一个新文件。读取会从文件的开头开始，写入则只能是追加模式。 |

如果不能打开文件，`fopen`函数将会带回一个出错信息。出错原因可能是用r方式打开一个并不存在的文件，又或者是磁盘出了故障，为了避免程序运行的错误，一般这么打开文件：

```c
FILE *file = fopen("vzjho.txt", "r");
if (file == NULL) {
    printf("Error!\n");
    exit(0);
}
```

即先检查打开文件的操作是否出错，如果出错则显示错误。`exit()`函数的作用是关闭所有文件，终止正在执行的程序。



## 关闭文件

关闭文件使用`fclose()`函数

```c
int fclose(FILE *p);
```

如果成功关闭文件，`fclose( )`函数返回零，如果关闭文件时发生错误，函数返回 **EOF**。这个函数实际上，会清空缓冲区中的数据，关闭文件，并释放用于该文件的所有内存。EOF 是一个定义在头文件 **stdio.h** 中的常量。

C 标准库提供了各种函数来按字符或者以固定长度字符串的形式读写文件。



## 写入文件

`fputc()`将字符写入到流中,函数`fputs()`把字符串 **s** 写入到 fp 所指向的输出流中。如果写入成功，它会返回一个非负值，如果发生错误，则会返回 **EOF**。您也可以使用 `int fprintf(FILE \*fp,const char \*format, ...)` 函数把一个字符串写入到文件中。

```c
int fputc(int c, FILE *fp);
```

函数 `fputc()` 把参数 c 的字符值写入到 fp 所指向的输出流中。如果写入成功，它会返回写入的字符，如果发生错误，则会返回 **EOF**。

同时可以用`fprintf()`和`fputs()`两个函数来将整行字符串写入文件中

```c
int fprintf(FILE *stream, const char *format, ...);
// 例如fprintf(fptr, "Hello, %s", string);
// fptr是输出流，string存放了字符串“world”的话，那么会将“Hello, world”写入文件

int fputs(const char *str, FILE *stream);
```



```c
#include <stdio.h>

int main（） {
    FILE *fp = NULL;
    // 初始化指针
    
    fp = fopen("/tmp/test.txt", "w+");
    fprintf(fp, "This is testing for fprintf...\n");
    // 以fprintf方式写入一行文字
    
    fputs("This is testing for fputs...\n", fp);
    // 以fputs方式写入一行文字
    fclose(fp);
}
```

## 读取文件

```c
int fgetc(FILE *p);
```

`fgetc()` 函数从 fp 所指向的输入文件中读取一个字符。返回值是读取的字符，如果发生错误则返回 **EOF**。下面的函数允许您从流中读取一个字符串：

```c
char *fgets(char *buf, int n, FILE *fp);
```

函数 `fgets()` 从 fp 所指向的输入流中读取 n - 1 个字符。它会把读取的字符串复制到缓冲区 **buf**，并在最后追加一个 **null** 字符来终止字符串。

如果这个函数在读取最后一个字符之前就遇到一个换行符 '\n' 或文件的末尾 EOF，则只会返回读取到的字符，包括换行符。您也可以使用 `int fscanf(FILE \*fp, const char \*format, ...)` 函数来从文件中读取字符串，但是在遇到第一个空格和换行符时，它会停止读取。

```c
#include <stdio.h>

int main() {
    FILE *fp = NULL;
    char buff[255];
    
    fp = fopen("/tmp/test.txt", "r");
    fscanf(fp, "%s", buff);
    printf("1: %s\n", buff);
    
    fgets(buff, 255, (FILE*)fp);
    printf("2: %s\n", buff);
    
    fgets(buff, 255, (FILE*)fp);
    printf("3: %s\n", buff);
    fclose(fp);
}
```

当以上代码被编译和执行，他会读取上一部分创建的文件，产生以下结果：

```
1: This
2: is testing for fprintf...

3: This is testing for fputs...
```

首先，`fscanf()`函数只读取了**This**，因为在这个单词后面遇到了空格作为分割符。其次，调用`fgtes`读取剩余的部分，直到行尾。最后，调用`fgets()`完整的读取了到了第二行



## 附录 所有的使用文件方式

| 文件使用方式 | 含义                                   | 如果指定文件不存在 |
| ------------ | -------------------------------------- | ------------------ |
| r 只读       | 为了输入数据，打开一个已存在的文本文件 | 出错               |
| w 只写       | 为了输出数据，打开一个文本文件         | 建立新文件         |
| a 追加       |                                        | 出错               |
| rb 只读      |                                        | 出错               |
| wb 只写      |                                        | 建立新文件         |
| ab 追加      |                                        | 出错               |
| r+ 读写      |                                        | 出错               |
| w+ 读写      |                                        | 建立新文件         |
| a+ 读写      |                                        | 出错               |
| rb+ 读写     |                                        | 出错               |
| wb+ 读写     |                                        | 建立新文件         |
| ab+ 读写     |                                        | 出错               |

# C++文件操作

C++ 中的文件操作是处理文件的基本操作之一，它允许你从文件中读取数据、向文件中写入数据以及进行文件的其他操作。在 C++ 中进行文件操作通常需要包含 `<fstream>` 头文件。下面是关于 C++ 文件操作的详细示例和说明：

## 文件的打开和关闭

```cpp
cppCopy code#include <iostream>
#include <fstream>

int main() {
    std::ofstream outputFile; // 文件输出流对象
    std::ifstream inputFile;  // 文件输入流对象

    // 打开文件以写入数据
    outputFile.open("output.txt");

    // 写入数据到文件
    outputFile << "Hello, File!\n";

    // 关闭输出文件
    outputFile.close();

    // 打开文件以读取数据
    inputFile.open("output.txt");

    // 读取数据
    std::string line;
    while (std::getline(inputFile, line)) {
        std::cout << line << '\n';
    }

    // 关闭输入文件
    inputFile.close();

    return 0;
}
```

## 写入文件

```cpp
cppCopy code#include <iostream>
#include <fstream>

int main() {
    std::ofstream outputFile("output.txt"); // 创建文件输出流对象并打开文件

    if (outputFile.is_open()) {
        outputFile << "This is a line.\n";
        outputFile << "This is another line.\n";
        outputFile.close(); // 关闭文件
    } else {
        std::cerr << "Failed to open the file!\n";
    }

    return 0;
}
```

## 读取文件

```cc
cppCopy code#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("input.txt"); // 创建文件输入流对象并打开文件
    std::string line;

    if (inputFile.is_open()) {
        while (std::getline(inputFile, line)) {
            std::cout << line << '\n';
        }
        inputFile.close(); // 关闭文件
    } else {
        std::cerr << "Failed to open the file!\n";
    }

    return 0;
}
```

## 二进制文件读写

```cc
cppCopy code#include <iostream>
#include <fstream>

struct Person {
    char name[50];
    int age;
    double salary;
};

int main() {
    Person p1 = {"John", 25, 50000.0};

    // 写入二进制文件
    std::ofstream outputFile("person.bin", std::ios::binary);
    if (outputFile.is_open()) {
        outputFile.write(reinterpret_cast<char*>(&p1), sizeof(Person));
        outputFile.close();
    } else {
        std::cerr << "Failed to open the file!\n";
        return 1;
    }

    // 读取二进制文件
    Person p2;
    std::ifstream inputFile("person.bin", std::ios::binary);
    if (inputFile.is_open()) {
        inputFile.read(reinterpret_cast<char*>(&p2), sizeof(Person));
        inputFile.close();

        // 输出读取的数据
        std::cout << "Name: " << p2.name << std::endl;
        std::cout << "Age: " << p2.age << std::endl;
        std::cout << "Salary: " << p2.salary << std::endl;
    } else {
        std::cerr << "Failed to open the file!\n";
        return 1;
    }

    return 0;
}
```

这些示例涵盖了 C++ 中常见的文件操作，包括打开、读取、写入和关闭文件，以及对二进制文件的读写。使用这些基本操作，你可以处理各种文件操作需求。
