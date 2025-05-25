<center><h1>Python 上机报告</h1></center>
<center>班级：物联网2303  学号：3230611081   姓名：盛子涵</center>

## 1.1 找素数

输出101到200之间的素数，要求每行输出10个，多余换行。


```python
"""
problem: find prime number between 101 and 200
date: 2024-09-26
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(101, 200):
    if is_prime(i):
        print(i, end=' ')
        count += 1
        if count % 10 == 0:
            print()
```
<hr>

```
101 103 107 109 113 127 131 137 139 149 
151 157 163 167 173 179 181 191 193 197 
199
```

## 1.2 计算n阶调和数

先一个定义计算并返回第n阶调和数（1 + 1/2 + 1/3 + … + 1/n）的函数，然后在命令行中输入参数n，调用函数计算前n个调和数之和，并将每次函数调用的结果放入一个列表，最后输出该列表，以及列表中所有元素之和（精确到小数点后面一位）。


```python
"""
problem: Harmonic numbers
date: 2024-09-26
"""

def harmonic_number(n):
    return round(sum(1 / i for i in range(1, n + 1)), 1)

n = int(input("Enter an integer: "))
harmonic_numbers = [harmonic_number(i) for i in range(1, n + 1)]

print("The list of Harmonic numbers: ", harmonic_numbers)
print("The sum of the list: ", sum(harmonic_numbers))
```
<hr>

```
Enter an integer:  9
The list of Harmonic numbers:  [1.0, 1.5, 1.8, 2.1, 2.3, 2.5, 2.6, 2.7, 2.8]
The sum of the list:  19.3
```

## 1.3 列表操作

由用户输入n个整数，将这些整数构成一个列表。要求显示出该列表的元素个数、最大值、最小值、所有元素之和、平均值。请思考用多种方法来实现。


```python
"""
problem: Operation of List
date: 2024-09-26
"""

input_numbers = input('Enter the list of number: ')
numbers = list(map(int, input_numbers.split()))

length = len(numbers)
max_value = max(numbers)
min_value = min(numbers)
sum_value = sum(numbers)
average_value = sum_value / length

print('Length =', length, '\n'
      'Max =', max_value, '\n'
      'Min =', min_value, '\n'
      'Sum =', sum_value, '\n'
      'Average =', average_value)
```
<hr>

```
Enter the list of number:  5 6 4 8 4 2 5 6 4 9
Length = 10 
Max = 9 
Min = 2 
Sum = 53 
Average = 5.3
```

## 1.4 利用循环语句求和

分别利用for循环和while循环求1~100中所有数之和，以及所有奇数的和、所有偶数的和。


```python
print("Find the sum by using 'for'")

sum = 0
sum_odd = 0
sum_even = 0

for i in range(1, 101):
    sum += i

for i in range(1, 101, 2):
    sum_odd += i

for i in range(2, 101, 2):
    sum_even += i

print('Sum:', sum, '\n', 'Sum of odd:', sum_odd, '\n', 'Sum of even:', sum_even)

print("Find the sum by using 'while'")

sum = 0
sum_odd = 0
sum_even = 0

i = 0
while(i <= 100):
    sum += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
    i += 1

print('Sum:', sum, '\n', 'Sum of odd:', sum_odd, '\n', 'Sum of even:', sum_even)
```
<hr>

```
Find the sum by using 'for'
Sum: 5050 
 Sum of odd: 2500 
 Sum of even: 2550
Find the sum by using 'while'
Sum: 5050 
 Sum of odd: 2500 
 Sum of even: 2550
```

## 1.5 判断闰年

至少使用2种方法编写一个函数来判断某一年是否为闰年。
年份数据由用户输入，调用该函数，函数调用完毕后，输出判断结果。


```python
"""
problem: determing leap years
date: 2024-09-26
"""

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is leap year")
else:
    print(year, "is not a leap year")
```
<hr>

```
Enter a year:  2004
2004 is leap year
```

## 1.6 判断回文

编写程序，判断用户输入的一个字符串是否为回文。如果是则输出True，否则输出Flase


```python
def is_parlindrom(string):
    return string == string[::-1]

string = input('Enter a string: ')
if is_parlindrom(string):
    print('The input is a parlindrom')
else:
    print('The input is not a parlindrom')
```
<hr>

```
Enter a string:  beeb
The input is a parlindrom
```

## 1.7 计算三角形面积

由用户输入三角形的三条边的边长a、b和c，计算并输出三角形的面积。提示:利用三角形周长的一半h来计算面积。

在写出基本程序之后建议尝试增加如下一些功能：

1. 使用2种输出格式控制方式。
2. 若由用户输入三角形的三条边的边长（即a、b、c），则必须对三角形的边长小于或等于0和两边之和小于或等于第三边的情况识别出来，并提示用户。

请思考下面两种解决方案：

1. 用while循环语句进行判断，出现上述错误会提示并要求用户重新输入三条边长，直到用户输入合法边长之后计算并输出三角形的面积。
2. 用异常处理机制（raise语句和ValueError对象）来终止程序并提醒用户错误的原因。（注意：可以在学完异常处理之后再来完善该题）



```python
"""
problem: Find the area of the triangle
date: 2024-09-26
"""

def caculate_triangle_area(a, b, c):
    h = (a + b + c) / 2
    return (h * (h - a) * (h - b) * (h - c)) ** 0.5

def get_triangle_sides():
    while True:
        try:
            a = int(input('Enter a side:'))
            b = int(input('Enter b side:'))
            c = int(input('Enter c side:'))
            if a < 0 and b < 0 and c < 0 and a + b < c and a + c < b and b + c < a:
                print('Invalid sides, pls retry.')
                continue
            return a, b, c

        except ValueError:
            print('Input value invalid!')

a, b, c = get_triangle_sides()
area = caculate_triangle_area(a, b, c)

print('The are of the triangle is:', round(area, 2))
```
<hr>

```
Enter a side: 12
Enter b side: 23
Enter c side: 12
The are of the triangle is: 39.42
```

## 2.1 求阶乘

编写程序，定义一个求阶乘的函数fact(n)，并编写测试代码，要求输入整数n（n>=0）。请分别使用递归和非递归方式实现


```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print(factorial(n))
```
<hr>

```
Enter a number:  6
720
```


```python
def factorial(n):
    if n == 1 or n == 2:
        return n
    else:
        return factorial(n-1) * n
    
n = int(input("Enter a number: "))
print(factorial(n))
```
<hr>

```
Enter a number:  6
720
```

## 2.2 折半查找

用折半查找法查33和58在列表[1,13,26,33,45,55,68,72,83,99]中的位置，

要求：分别用递归和非递归的方法来实现。

输出结果是：

关键字33在列表中的索引是：3

关键字58不在该列表中


```python
"""
non-recursive solution
"""
def find_by_mid(n, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == n:
            return mid
        if array[mid] > n:
            right = mid
        else:
            left = mid + 1
    return -1

array = [1, 13, 26, 33, 45, 55, 68, 72, 83, 99]
n = int(input("Enter a number: "))

if find_by_mid(n, array) == -1:
    print(f"{n} not found")
else:
    print(f"The index of {n} is: {find_by_mid(n,array)}")
```
<hr>

```
Enter a number:  33
The index of 33 is: 3
```


```python
"""
recursive solution
"""

def find_by_mid(n, array, left, right):
    if left <= right:
        mid = (left + right) // 2
        if array[mid] == n:
            return mid
        if array[mid] > n:
            return find_by_mid(n, array, left, mid - 1)
        else:
            return find_by_mid(n, array, mid + 1, right)
        
    if left >= right:
        return -1
    
left = 0
right = len(array) - 1

n = int(input("Enter a number: "))
index = find_by_mid(n, array, left, right)
if index == -1:
    print(f"{n} not found")
else:
    print(f"The index of {n} is: {index}")
```
<hr>

```
Enter a number:  33
The index of 33 is: 3
```

## 2.3 文本文件

1.打开该文件file2.txt，并将元组t = "spring", "summer", "autumn"写入到文件中，要求元组中每个元素单独放在一行中，建议使用for循环语句。
2.打开该文件并字符串" winter"追加到文件最后一行下面的一行，使得文件中的内容包括如下4行文字：

```
spring
summer
autumn
winter
```

3.打开该文件并将其中的最后两行文字显示到屏幕上。
4.思考：若一开始文件file2.txt不存在，一定要先创建该文件？若要在读取文件的过程中增加异常处理的代码，以便在文件不存在或打开失败的异常情况下，向用户提示“文件file2.txt打开失败！”，应该怎么修改代码



```python
t = ('spring', 'summer', 'autumn')
with open("file2.txt", "w") as file:
    for i in t:
        file.write(f'{i}\n')
```

<hr>


```python
with open("file2.txt", "a") as file:
    file.write(f'winter\n')
```

<hr>


```python
with open("file2.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-2:]:
        print(line, end='')
```

<hr>


```python
try:
    with open ("file2.txt") as file:
        for i in t:
            file.write(f'{i}\n')
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error, {e}")
```

## 2.4 二进制文件读写

打开一个空的随机文件my.dat，往里面写入下面2行字节数据：

```
Xiaoming
student
```

然后读入该文件的后7个字节并输出到屏幕上。


```python
with open('my.dat', 'wb') as file:
    file.write(b'Xiaoming\n')
    file.write(b'student\n')

with open('my.dat', 'rb') as file:
    file.seek(-8, 2)
    output = file.read(7)
    
print(output)

```
<hr>

```
b'student'
```

## 2.5 类的继承

通过继承，派生类继承基类中除构造方法之外的所有成员。如果在子类类中重新定义从基类继承的方法，则派生类中定义的方法覆盖从基类中继承的方法，即子类同名方法优先。反之，若子类没有重新定义，则使用从父类继承过来的方法。

先定义父类Dimension，在类中定义计算面积的函数area，该函数就输出一行话“形状没定，无法计算面积！”。然后定义Dimension的一个子类Triangle（表示三角形），在其中定义构造函数、计算面积的函数area。
之后再按照类似的方式分别创建圆形、矩形的类。
最后分别创建上述3种对象，然后输出它们的面积。


```python
%reset -f

import math


class Dimension:
    def area(self):
        print('Shape is undefined')


class Triangle(Dimension):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


class Circle(Dimension):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Dimension):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


triangle = Triangle(10, 5)
circle = Circle(7)
rectangle = Rectangle(8, 6)

print("Triangle Area:", triangle.area())
print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
```
<hr>

```
Triangle Area: 25.0
Circle Area: 153.93804002589985
Rectangle Area: 48
```

## 2.7 创建MyMath类

编写程序，创建类MyMath，计算圆的周长和面积以及球的表面积和体积，并编写测试代码，结果均保留两位小数。    


```python
import math

class MyMath:
    @staticmethod
    def circle_area(radius):
        area = math.pi * (radius ** 2)
        return round(area, 2)
    
    @staticmethod
    def circle_circumference(radius):
        circumference = 2 * math.pi * radius
        return round(circumference, 2)

    @staticmethod
    def sphere_surface_area(radius):
        surface_area = 4 * math.pi * (radius ** 2)
        return round(surface_area, 2)

    @staticmethod
    def sphere_volume(radius):
        volume = 4 / 3 * math.pi * (radius ** 3)
        return round(volume, 2)


if __name__ == "__main__":
    r = 5

    circle_circumference = MyMath.circle_circumference(r)
    circle_area = MyMath.circle_area(r)
    sphere_surface_area = MyMath.sphere_surface_area(r)
    sphere_volume = MyMath.sphere_volume(r)

    print(f"The radius: {r}")
    print(f"Circle circumference: {circle_circumference}")
    print(f"Circle area: {circle_area}")
    print(f"Sphere surface area: {sphere_surface_area}")
    print(f"Sphere volume: {sphere_volume}")

```
<hr>

```
The radius: 5
Circle circumference: 31.42
Circle area: 78.54
Sphere surface area: 314.16
Sphere volume: 523.6
```

## 2.8 学校信息管理系统

建立学校信息管理系统：
建立Person类，包括：姓名name、性别sex、年龄age这3个数据成员，一个构造函数、一个输出信息的printInfo函数。
建立Student类，该类继承自Person类，并且新增数据成员：班级classes（用string类型）、学号studentID（用int类型）、成绩score（用字典类型，可以自己定义三门课程，比如语数外）、总人数count（用int类型，这是静态属性，即类属性），和一个构造函数、一个输出信息的printInfo函数。
建立Teacher类，该类也继承自Person类，并且新增：部门department（用string类型）、工号teacherID（用int类型）、讲授课程course（用列表类型）、薪水salary（用int类型，这是私有数据）这4个数据成员，和一个构造函数、一个输出信息的printInfo函数（这里不输出私有数据，但可以考虑一下如何提供私有数据的输出方法）。
然后创建2个学生对象和1个教师对象，然后分别调用这3个对象的printInfo函数输出各自的（非私有）数据信息。在学生的构造函数中让count自增，在析构函数中让count自减。
（说明：上面已经规定的内容在自己编程时也允许灵活调整，没有规定的更是可以自由发挥，主要是必须学会类的定义和使用）


```python
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def printInfo(self):
        print(f"姓名: {self.name}, 性别: {self.sex}, 年龄: {self.age}")


class Student(Person):
    count = 0

    def __init__(self, name, sex, age, classes, studentID, scores):
        super().__init__(name, sex, age)
        self.classes = classes
        self.studentID = studentID
        self.scores = scores
        Student.count += 1

    def printInfo(self):
        super().printInfo()
        print(f"班级: {self.classes}, 学号: {self.studentID}, 成绩: {self.scores}")

    def __del__(self):
        Student.count -= 1


class Teacher(Person):
    def __init__(self, name, sex, age, department, teacherID, course, salary):
        super().__init__(name, sex, age)
        self.department = department
        self.teacherID = teacherID
        self.course = course
        self.__salary = salary

    def printInfo(self):
        super().printInfo()
        print(f"部门: {self.department}, 工号: {self.teacherID}, 讲授课程: {', '.join(self.course)}")

    def getSalary(self):
        return self.__salary
```
<hr>

```
student1 = Student("张三", "男", 18, "高一", 1001, {"语文": 90, "数学": 85, "英语": 88})
student2 = Student("李四", "女", 19, "高二", 1002, {"语文": 92, "数学": 87, "英语": 90})

teacher1 = Teacher("王老师", "男", 35, "数学组", 2001, ["数学", "物理"], 6000)

print("学生信息：")
student1.printInfo()
student2.printInfo()

print("\n教师信息：")
teacher1.printInfo()

print(f"\n当前学生总人数: {Student.count}")

```
<hr>

```
学生信息：
姓名: 张三, 性别: 男, 年龄: 18
班级: 高一, 学号: 1001, 成绩: {'语文': 90, '数学': 85, '英语': 88}
姓名: 李四, 性别: 女, 年龄: 19
班级: 高二, 学号: 1002, 成绩: {'语文': 92, '数学': 87, '英语': 90}

教师信息：
姓名: 王老师, 性别: 男, 年龄: 35
部门: 数学组, 工号: 2001, 讲授课程: 数学, 物理

当前学生总人数: 2
```

## 3.1 用两个列表来生成字典

编写程序，输入2个列表，以第一个列表中的元素为“键”，以第二个列表中的元素为“值”创建字典。若两个列表长度不等，则以短的为准而丢弃较长列表中后面的元素。最后输出字


```python
"""
program: dict.py
date: 2024-11-14
"""


def create_dict(list1, list2):
    length = min(len(list1), len(list2))
    result = dict(zip(list1[:length], list2[:length]))
    return result


l1 = input("Enter first list: ").split()
l2 = input("Enter second list: ").split()
dictionary = create_dict(l1, l2)
print(dictionary)

```
<hr>

```
Enter first list:  a b c d e
Enter second list:  1 2 3 4 5

{'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}
```

## 3.2 猜数字

随机产生一个0到100之间（包括0和100）的偶数，请用户猜测具体是哪个数，即：不断从标准输入读取用户的猜测值（用户每次输入一个偶数），并根据猜测值给出提示信息：“太大”、“太小”或“正确!”


```python
"""
program: guess.py
date: 2024-11-14
"""
import random

# Generate a random even number
target = random.choice(range(0, 101, 2))
while True:
    guess = int(input("Guess a number: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    if guess == target:
        print("You got it!")
        break
```
<hr>

```
Guess a number:  50
Too high!
Guess a number:  25
Too low!
Guess a number:  37
Too high!
Guess a number:  27
Too low!
Guess a number:  30
You got it!
```

## 3.3 用迭代器和生成器函数来输出斐波那契数列

分别用迭代器和生成器函数来输出斐波那契数列的第10项~第20项


```python
"""
program: fibonacci_generator.py
date: 2024-11-14
"""


def fibonacci_generator(start, end):
    a, b = 0, 1
    count = 0
    while count < end:
        if count >= start:
            yield b
        a, b = b, a + b
        count += 1


for fib_num in fibonacci_generator(10, 20):
    print(fib_num)
```
<hr>

```
89
144
233
377
610
987
1597
2584
4181
6765
```

<hr>


```python
"""
program: get list of specialized fibonacci numbers list
date: 2024-11-14
"""


class FibonacciIterator:
    def __init__(self, start, end):
        self.a, self.b = 0, 1
        self.start = start
        self.end = end
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.end:
            raise StopIteration
        while self.count < self.start:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a


fibonacci_iterator = FibonacciIterator(10, 20)
for num in fibonacci_iterator:
    print(num)

```
<hr>

```
89
144
233
377
610
987
1597
2584
4181
6765
```

## 3.4 获取系统当前时间

编写一个程序，获取系统当前的时间等信息，输出格式如下面方框里所示。然后将这些信息写入一个文本文件，最后将文件中的内容读出来后显示在屏幕上。
说明：第一行是时间和日期，第二行是星期几，第三行是本月有几天。
2021-11-09 21:19:43
Tuesday
There are 30 days in this month.

```python
"""
program: get system time and save to file
date: 2024-11-14
"""

import time


def system_info():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    weekday = time.strftime("%A", time.localtime())
    days_in_month = time.strftime("%d", time.localtime())
    return current_time, weekday, f"There are {days_in_month} days in this month."


time_info = system_info()
with open("time_info.txt", "w") as file:
    file.write("\n".join(time_info))

with open("time_info.txt", "r") as file:
    print(file.read())

```
<hr>

```
2024-12-04 23:27:28
Wednesday
There are 04 days in this month.
```

## 3.5 集合及其程序关系

随机生成10个从0~10区间内（包含0和10）的整数，分别组成集合A、集合B，输出A和B的内容、长度、最大值、最小值，以及A和B的并集、交集和差集


```python
"""
program:
date: 2024-11-14
"""

import random

A = {random.randint(0, 10) for _ in range(10)}
B = {random.randint(0, 10) for _ in range(10)}

print(f'''
        A: {A}
        B: {B}
        Length of A: {len(A)}
        Length of B: {len(B)}
        Max of A: {max(A)}
        Min of A: {min(A)}
        Max of B: {max(B)}
        Min of B: {min(B)}
        Union of A and B: {A | B}
        Intersection of A and B: {A & B}
        Difference of A and B: {A - B}
''')
```
<hr>

```
A: {3, 5, 6, 8, 9}
B: {1, 5, 8, 9, 10}
Length of A: 5
Length of B: 5
Max of A: 9
Min of A: 3
Max of B: 10
Min of B: 1
Union of A and B: {1, 3, 5, 6, 8, 9, 10}
Intersection of A and B: {8, 9, 5}
Difference of A and B: {3, 6}
```

## 3.6 整数排序和计算平均值

随机产生10个两位的正整数，存入列表ls中，然后对该列表中的数进行排序（由小到大），最后分别输出：排序后的列表、这10个数的平均数，以及大于平均值的数的个数。



```python
"""
date: 2024-11-14
"""

import random

ls = [random.randint(10, 99) for _ in range(10)]
sorted_ls = sorted(ls, reverse=True)
print(sorted_ls)

average = sum(ls) / len(ls)
print('The average:', average)

for i in ls:
    if i >= average:
        print(i, end=' ')
```
<hr>

```
[98, 91, 90, 74, 74, 48, 47, 45, 37, 35]
The average: 63.9
74 90 74 91 98 
```

## 3.7 根据奖金计算利润

企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


```python
"""
program: bonus.py
date: 2024-11-14
"""

def calculate_bonus(profit):
    if profit <= 100000:
        return profit * 0.1
    elif profit <= 200000:
        return 100000 * 0.1 + (profit - 100000) * 0.075
    elif profit <= 400000:
        return 100000 * 0.1 + 100000 * 0.075 + (profit - 200000) * 0.05
    elif profit <= 600000:
        return 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
    elif profit <= 1000000:
        return 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit - 600000) * 0.015
    else:
        return 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit - 1000000) * 0.01

profit = float(input("Enter the profit: "))
bonus = calculate_bonus(profit)
print(f"Bonus: {bonus}")
```
<hr>

```
Enter the profit:  598679
Bonus: 33460.37
```

## 3.8 求s=a+aa+aaa+aaaa+aa...a的值

求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

2 = 0 + 2*100
22 = 2 + 2*101
222 = 22 + 2*102



```python
"""
date: 2024-11-14
"""


def sum_repeat(a, n):
    result, term = 0, 0
    for i in range(n + 1):
        term += term * 10 + a
        result += term

    return result


a = int(input("Enter a number: "))
n = int(input("Enter time: "))
print("Result: ", sum_repeat(a, n))
```
<hr>

```
Enter a number:  2
Enter time:  20
Result:  1628054987736795222262
```

## 3.9 对文本文件进行统计

参考例15.14编写一个文本统计程序，利用正则表达式对文本文件“abstract.txt”中读取字符串序列，统计文本文件“abstract.txt”中包含的段落数、行数、句数、单词数，以及统计各单词出现的频率。abstract.txt文件的内容如下面框中所示，要事先创建该文件。
Cloud services are exploding, and organizations are converging their data centers in order to take advantage of the predictability, continuity, and quality of service delivered by virtualization technologies.

In parallel, energy-efficient and high-security networking is of increasing importance. Network operators, and service and product providers require a new network solution to efficiently tackle the increasing demands of this changing network landscape. Software-defined networking has emerged as an efficient network technology capable of supporting the dynamic nature of future network functions and intelligent applications while lowering operating costs through simplified hardware, software, and management.

In this article, the question of how to achieve a successful carrier grade network with software-defined networking is raised. Specific focus is placed on the challenges of network performance, scalability, security, and interoperability with the proposal of potential solution directions.



```python
"""
program: text statistics
date: 2024-11-16
"""
import re


def text_statistics(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    paragraphs = text.split('\n\n')
    lines = text.splitlines()
    sentences = re.findall(r'[.!?]', text)
    words = re.findall(r'\w+', text)

    word_count = {word: words.count(word) for word in set (words)}

    print("Paragraph:", len(paragraphs))
    print("Lines:", len(lines))
    print("Sentences:", len(sentences))
    print("Words:", len(words))
    print("Word count:", len(word_count))


text_statistics("abstract.txt")

```
<hr>

```
Paragraph: 1
Lines: 3
Sentences: 6
Words: 137
Word count: 94
```

## 3.10 单词的去重与排序

编写一个程序，接收一系列单个空格分隔的单词作为输入，在删除所有重复的单词并按各单词的首字母的升序排序后，打印这些单词。
假设向程序提供以下输入:
hello world and practice makes perfect and hello world again
则输出为:
again and hello makes perfect practice world



```python
"""
program: deduplication.py
date: 2024-11-16
"""


def unique_sorted(sentence):
    words = sentence.split()
    unique_words = sorted(set(words))

    return unique_words


sentence = "hello world and practice makes perfect and hello world again"
print(unique_sorted(sentence))
print(" ".join(unique_sorted(sentence)))

```
<hr>

```
['again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world']
again and hello makes perfect practice world
```

## 4.1 利用多线程和多进程统计素数的个数

参照教材P278和P286的代码，分别利用threading模块和multiprocessing模块，实现以多线程和多进程方式统计10000000以内的素数的个数，并输出计算处理所耗费的时间。


```python
"""
file: find_prime_threading.py
find prime by using threading
date: 2024-11-21
"""

import threading
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def count_primes(start, end, result, index):
    count = sum(1 for i in range(start, end) if is_prime(i))
    result[index] = count


def main():
    start_time = time.time()
    num_threads = 16
    limit = 10000000
    range_size = limit // num_threads
    threads = []
    result = [0] * num_threads

    for i in range(num_threads):
        start = i * range_size
        end = (i + 1) * range_size if i != num_threads - 1 else limit
        thread = threading.Thread(target=count_primes, args=(start, end, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    prime_count = sum(result)
    print(f"Prime count: {prime_count}")
    print(f"Time taken: {time.time() - start_time}")


if __name__ == "__main__":
    main()
```
<hr>

```
Prime count: 4999998
Time taken: 5.018513917922974
```


```python
"""
file: find_prime_mutiprocessing.py
find primes by using mutiprocessing module
date: 2024-11-21
"""

import multiprocessing
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def count_primes(start, end):
    return sum(1 for i in range(start, end) if is_prime(i))


def main():
    start_time = time.time()
    num_processes = 16
    limit = 10000000
    range_size = limit // num_processes
    pool = multiprocessing.Pool(num_processes)

    results = []
    for i in range(num_processes):
        start = i * range_size
        end = (i + 1) * range_size if i != num_processes - 1 else limit
        results.append(pool.apply_async(count_primes, (start, end)))

    pool.close()
    pool.join()

    prime_count = sum(result.get() for result in results)
    print(f"Prime count: {prime_count}")
    print(f"Time taken: {time.time() - start_time}")
```
<hr>

```
Prime count: 4999998
Time taken: 2.4153504371643066
```

## 4.2 在学校信息系统中实现多重继承

继续编写学校信息系统的程序
在题目2-6中学生类教师类程序的基础上，再创建一个特殊的类：stu_teacher，该类同时继承自学生类和教师类，同时在该类中定义输出其数据的函数，然后创建该类的对象，并调用输出函数显示对象的数据。输出格式自定。



```python
"""
file: school_info.py
date: 2024-11-21
"""


class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def show_student(self):
        return f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}"


class Teacher:
    def __init__(self, name, age, teacher_id, course):
        self.name = name
        self.age = age
        self.teacher_id = teacher_id
        self.course = course

    def show_teacher(self):
        return f"Teacher: {self.name}, Age: {self.age}, ID: {self.teacher_id}"


class StuTeacher(Student, Teacher):
    def __init__(self, name, age, student_id, teacher_id, course):
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, name, age, teacher_id, course)

    def show(self):
        return f"{self.show_student()}, {self.show_teacher()}"


stu_teacher = StuTeacher("John Doe", 24, "S123", "T456", "Math")
print(stu_teacher.show())

```
<hr>

```
Student: John Doe, Age: 24, ID: S123, Teacher: John Doe, Age: 24, ID: T456
```

## 4.3 学校信息系统的数据库操作

利用一种SQLite数据库管理工具，创建学校信息管理系统的数据库文件school.db，然后用Python程序在其中创建两个表：
学生信息表（表名为student）,其中包括5个字段：姓名name、性别sex、年龄age、学号studentID、成绩score。
教师信息表（表名为teacher）,其中包括7个字段：姓名name、性别sex、年龄age、部门department、工号teacherID、讲授课程course、薪水salary。
然后尝试用sqlite3模块中的相关函数，实现对上述两个表进行：增删改查，也就是是添加数据、删除数据、修改数据、查询表中数据等操作。



```python
"""
file: school_info_db.py
date: 2024-11-21
"""
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    name TEXT,
    sex TEXT,
    age INTEGER,
    student_id TEXT PRIMARY KEY,
    score REAL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teacher (
    name TEXT,
    sex TEXT,
    age INTEGER,
    department TEXT,
    teacher_id TEXT PRIMARY KEY,
    course TEXT,
    salary REAL
)''')

cursor.execute("INSERT INTO student (name, sex, age, student_id, score) VALUES ('Alice', 'F', 20, 'S001', 85)")
cursor.execute("INSERT INTO teacher (name, sex, age, department, teacher_id, course, salary) "
               "VALUES ('Bob', 'M', 40, 'Math', 'T001', 'Math', 5000)")
conn.commit()

cursor.execute("SELECT * FROM student")
students = cursor.fetchall()
print("Students:", students)

cursor.execute("SELECT * FROM teacher")
teachers = cursor.fetchall()
print("Teachers:", teachers)

cursor.execute("UPDATE student SET score = 90 WHERE student_id = 'S001'")
conn.commit()

cursor.execute("DELETE FROM teacher WHERE teacher_id = 'T001'")
conn.commit()

conn.close()

```
<hr>

```
Students: [('Alice', 'F', 20, 'S001', 85.0)]
Teachers: [('Bob', 'M', 40, 'Math', 'T001', 'Math', 5000.0)]
```
