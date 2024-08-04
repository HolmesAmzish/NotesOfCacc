# C 语言标准库

## stdio.h

| printf  | printf()          |               |
| ------- | ----------------- | ------------- |
| scanf   | scanf()           |               |
| gets    | gets(char string) | 输入字符串         |
| puts    | puts(string)      | 输出字符串         |
| sprintf | sprintf(str,%d,i) | 将整数i转换为字符串str |

## stdlib.h

| rand   | int rand(void)       | 产生0~32767随机整数                  |
| ------ | -------------------- | ------------------------------ |
| abort  | void abort(void)     | 异常终止一个进程                       |
| exit   | void exit(int state) | 程序终止执行，返回调用过程（0为正常终止，非0为非正常终止） |
| system | system()             | 执行dos或shell命令                  |

## math.h

| abs   | int abs(int x)                | 求整数x的绝对值    |
| ----- | ----------------------------- | ----------- |
| fabs  | double fabs(double x)         | 求实型x的绝对值    |
| cos   | double cos(double x)          | 计算cosx的值    |
| sin   | double sin(double x)          | 计算sinx的值    |
| tan   | double tan(double x)          | 计算tanx的值    |
| floor | double floor(double x)        | 求出不大于x的最大整数 |
| sqrt  | double sqrt(double x)         | 计算x的开方      |
| pow   | double pow(double x,double y) | 计算x的y次方     |

## ctype.h

| 函数                  | 作用          |
| ------------------- | ----------- |
| int isalnum(int c)  | 检查是否是字母或数字  |
| int isalpha(int c)  | 检查是否是字母     |
| int iscntrl(int c)  | 检查是否是控制字符   |
| int isdigit(int c)  | 检查是否是数字     |
| int islower(int c)  | 检查是否是小写     |
| int isprint(int c)  | 检查是否是可打印符号  |
| int ispunct(int c)  | 检查是否是标点     |
| int isspace(int c)  | 检查是否是空格     |
| int isupper(int c)  | 检查是否是大写     |
| int isxdigit(int c) | 检查是否是十六进制数字 |

此外，标准库还包含两个转换函数，他们接受并返回一个整型数值。

| 函数                 | 作用      |
| ------------------ | ------- |
| int tolower(int c) | 转换成小写字母 |
| int toupper(int c) | 转换成大写字母 |

## string.h

| strlen  | strlen(string)          | 计算字符串s的长度         |
| ------- | ----------------------- | ----------------- |
| strcpy  | strcpy(string1,string2) | 复制string2到string1 |
| strncpy |                         | 复制前n字符            |
| strcat  |                         | 字符串连接             |
| strcmp  | strcmp(string1,string2) | 字符串比较函数（区分大小写）    |
| stricmp |                         | 字符串比较函数（不区分大小写）   |
| strncmp |                         | 比较前n个元素           |
| strstr  | strstr(string1,string2) | 字符串搜索函数           |
| strchr  |                         | 字符搜索函数            |
| strlwr  |                         | 字符串转小写            |
| strupr  |                         | 字符串转大写            |
| strrev  |                         | 字符串反转             |

## time.h

# C 语言数据类型

## 整型

| 类型             | 储存大小 | 值范围          |
| -------------- | ---- | ------------ |
| (signed) char  | 1    | -128~127     |
| unsigned char  | 1    | 0~255        |
| (signed) int   | 4    | -2^31~2^31-1 |
| unsigned int   | 4    | 2^32 -1      |
| (signed) short | 2    | -2^15~2^15-1 |
| unsigned short | 2    | 2^16-1       |
| (signed) long  | 4    | -2^31~2^31-1 |
| unsigned long  | 4    | 2^32-1       |

## 浮点

| 类型     | 存储大小 | 值范围               | 精度    |
| ------ | ---- | ----------------- | ----- |
| float  | 4    | 1.2e-38~3.4e+38   | 6位小数  |
| double | 8    | 2.3e-308~1.7e+308 | 15位小数 |
