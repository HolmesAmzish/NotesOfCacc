# 数字

## 随机数



# 字符串

## 用字典对字符串字母计数

```python
def count_letters(text):
    letter_count = {}  # Create a new dict
    for char in text.lower():
        letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count
```

## 字符串排序

```python
string = input()
sorted_string = ''.join(sorted(string))  # sorted() return a list of char
print(sorted_string)
```





## 2.5 单字符串函数

```python
s = 'elephont'
if s[0].upper() in 'AEIOU':
    print('First char. is a vowel.')
```

遍历循环输出类型和ASCII码

```python
s = 'Cat'
for ch in s:
    print(ch, ', type:', type(ch))
    print(ord(ch), end=' ')
```

## 2.6 join函数

```python
separator_string.join(list)
```

```python
n = ord('A')
a_list = [ ]
for i in range(n, n + 26):
    a_list.append(chr(i))
s = ''.join(a_list)
```

## 2.7 字符串函数

```python
string = 'Wow,Bob,wow!'
a_str = ''.join(reversed(string))
b_str = ''.join(sorted(string))
```

## 2.11 字符串的搜索和替换

```python
str.startswith(substr)	# Return True if prefix is substr
str.endswith(substr)	# Return False if suffix is substr
```

```python
while romstr.startswith('M'):
	amt += 1000
	romstr = romstr[1:]
```

```python
str.count(substr [, beg [, end]])
str.find(substr [, beg [, end]])
str.index()
str.rfind()
str.replace(old, new [, count])
```

```python
frank_str = 'doo be doo be doo...'
n = franl_str.count('doo')	# n = 3
```

p48

# 标准库

## random

```python
ls = [random.randint(10, 99) for _ in range(10)] # Generate 10 random number from 10 to 99
sorted_ls = sorted(ls, reverse=True)
```

