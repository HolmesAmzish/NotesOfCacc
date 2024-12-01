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