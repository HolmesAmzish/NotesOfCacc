# Python操作

## pip 工具

查看当前安装的Python包

```bash
pip list

pip list --outdated
# 查看过时的包
```



# Data Types

------

## Built-in Data Types

In programming, data type is an important concept. Variables can store data of different types, and different types can do different things. Python has the following data types built-in by default, in these categories:

| Text Type:      | `str`                              |
| --------------- | ---------------------------------- |
| Numeric Types:  | `int`, `float`, `complex`          |
| Sequence Types: | `list`, `tuple`, `range`           |
| Mapping Type:   | `dict`                             |
| Set Types:      | `set`, `frozenset`                 |
| Boolean Type:   | `bool`                             |
| Binary Types:   | `bytes`, `bytearray`, `memoryview` |
| None Type:      | `NoneType`                         |

## Getting the Data Type

```python
x = 5
print(type(x))
```

## Type Conversion

```python
x = 1	# int

# Convert from int to float
a = float(x)

# Print the data type of a
print(type(a))
```



## Random Number

```python
import random

# Print a number range from 1 to 10
print(random.randrange(1, 10))
```



## Specify Type

```python
x = int(2.8)	# x will be 2
y = float(1)	# y will be 1.0
z = str(3.0)	# z will be '3.0'
```



## String

Strings in python are surrounded by either single quotation marks, or double quotation marks. You can display a string literal with the print() function.

```python
print("Hello")
print('Hello')
```

Assigning a string to a variable is done with the variable name followed by an equal sign and the string

```python
string = "Hello"
print(string)
```

You can assign a multiline string to a variable by using three quotes. You can use single quotation marks or double quotation marks.

```python
string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore megna aliqua."""
print(string)
```



## Strings Arrays

Get the character at position 1 (remember that the first character has the position 0).

```python
string = "Hello, World!"
print(string[0])
# The result will be 'e'
```

Since strings are arrays, we can loop through the characters in string, with a `for` loop.

```python
for x in "Hello, World!":
    print(x)
	
    print(x, end = '')
    # Ensure all the characters are printed in the same line
```



# Strings

## String Length

```python
a = "Hello, World!"
print(len(a))
```

## Check String

To check if a certain phrase or character is present in a string, we can use the keyword `in`.

```python
txt = "The best things in life are free!"
print("free" in txt)
```

Use it in an `if` statement

```python
txt = "The best things in life are free!"
if "free" in txt:
    print("YES, 'free' is present.")
```

To check if a certain phrase of character is NOT present in a string, we can use the keyword `not in`

```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```

Use it in an `if` statement. Print only if "expensive" is NOT present.

```python
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
```

## Slicing

You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string. Get the characters from position 2 to position 5 (not included):

```python
b = "Hello, World!"
print(b[2:5])

print(b[2:])
# Slice to the end
```

字符串类型

```python
msg = 'he is pReparing you'
msg.upper()			# 全部大写
msg.lower()			# 全部小写
msg.capitalize()	# 首字母大写
msg.title()			# 每个单词首字母大写
```



## Modify Strings

### Upper Case and Lower Case

```python
a = "Hello, World!"
print(a.upper())
# Print upper case of a
print(a.lower())
# Print lower case of a
```

### Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space. The `strip()` method removes any whitespace from the beginning or the end:

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

### Replacing String

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

### Split String

```python
a = "Hello, World!"
print(a.split(","))
# returns ['Hello', ' World!']
```

## String Concatenation

To concatenate, or combine, two strings you can use the + operator. Merge variable `a` with variable `b` into variable `c`:
```python
a = "Hello"
b = "World"
c = a + b
print(c)
```
To add a space between them, add a `" "`:
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```

## Format Strings

### F-Strings

F-String was introduced in Python 3.6, and is now the preferred way of formatting strings. To specify a string as an f-string, simply put an `f` in front of the string literal, and add curly brackets `{}` as placeholders for variables and other operations.

```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```

A placeholder can contain Python code, like math operations:

```python
txt = f"The price is {20 * 59} dollars"
print(txt)
```

## Escape Characters

| Code   | Result          |
| :----- | :-------------- |
| `\'`   | Single Quote    |
| `\\`   | Backslash       |
| `\n`   | New Line        |
| `\r`   | Carriage Return |
| `\t`   | Tab             |
| `\b`   | Backspace       |
| `\f`   | Form Feed       |
| `\ooo` | Octal value     |
| `\xhh` | Hex value       |

## String Methods

Python has a set of build-in methods that you can use on strings

| Method                                                       | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [capitalize()](https://www.w3schools.com/python/ref_string_capitalize.asp) | Converts the first character to upper case                   |
| [casefold()](https://www.w3schools.com/python/ref_string_casefold.asp) | Converts string into lower case                              |
| [center()](https://www.w3schools.com/python/ref_string_center.asp) | Returns a centered string                                    |
| [count()](https://www.w3schools.com/python/ref_string_count.asp) | Returns the number of times a specified value occurs in a string |
| [encode()](https://www.w3schools.com/python/ref_string_encode.asp) | Returns an encoded version of the string                     |
| [endswith()](https://www.w3schools.com/python/ref_string_endswith.asp) | Returns true if the string ends with the specified value     |
| [expandtabs()](https://www.w3schools.com/python/ref_string_expandtabs.asp) | Sets the tab size of the string                              |
| [find()](https://www.w3schools.com/python/ref_string_find.asp) | Searches the string for a specified value and returns the position of where it was found |
| [format()](https://www.w3schools.com/python/ref_string_format.asp) | Formats specified values in a string                         |
| format_map()                                                 | Formats specified values in a string                         |
| [index()](https://www.w3schools.com/python/ref_string_index.asp) | Searches the string for a specified value and returns the position of where it was found |
| [isalnum()](https://www.w3schools.com/python/ref_string_isalnum.asp) | Returns True if all characters in the string are alphanumeric |
| [isalpha()](https://www.w3schools.com/python/ref_string_isalpha.asp) | Returns True if all characters in the string are in the alphabet |
| [isascii()](https://www.w3schools.com/python/ref_string_isascii.asp) | Returns True if all characters in the string are ascii characters |
| [isdecimal()](https://www.w3schools.com/python/ref_string_isdecimal.asp) | Returns True if all characters in the string are decimals    |
| [isdigit()](https://www.w3schools.com/python/ref_string_isdigit.asp) | Returns True if all characters in the string are digits      |
| [isidentifier()](https://www.w3schools.com/python/ref_string_isidentifier.asp) | Returns True if the string is an identifier                  |
| [islower()](https://www.w3schools.com/python/ref_string_islower.asp) | Returns True if all characters in the string are lower case  |
| [isnumeric()](https://www.w3schools.com/python/ref_string_isnumeric.asp) | Returns True if all characters in the string are numeric     |
| [isprintable()](https://www.w3schools.com/python/ref_string_isprintable.asp) | Returns True if all characters in the string are printable   |
| [isspace()](https://www.w3schools.com/python/ref_string_isspace.asp) | Returns True if all characters in the string are whitespaces |
| [istitle()](https://www.w3schools.com/python/ref_string_istitle.asp) | Returns True if the string follows the rules of a title      |
| [isupper()](https://www.w3schools.com/python/ref_string_isupper.asp) | Returns True if all characters in the string are upper case  |
| [join()](https://www.w3schools.com/python/ref_string_join.asp) | Joins the elements of an iterable to the end of the string   |
| [ljust()](https://www.w3schools.com/python/ref_string_ljust.asp) | Returns a left justified version of the string               |
| [lower()](https://www.w3schools.com/python/ref_string_lower.asp) | Converts a string into lower case                            |
| [lstrip()](https://www.w3schools.com/python/ref_string_lstrip.asp) | Returns a left trim version of the string                    |
| [maketrans()](https://www.w3schools.com/python/ref_string_maketrans.asp) | Returns a translation table to be used in translations       |
| [partition()](https://www.w3schools.com/python/ref_string_partition.asp) | Returns a tuple where the string is parted into three parts  |
| [replace()](https://www.w3schools.com/python/ref_string_replace.asp) | Returns a string where a specified value is replaced with a specified value |
| [rfind()](https://www.w3schools.com/python/ref_string_rfind.asp) | Searches the string for a specified value and returns the last position of where it was found |
| [rindex()](https://www.w3schools.com/python/ref_string_rindex.asp) | Searches the string for a specified value and returns the last position of where it was found |
| [rjust()](https://www.w3schools.com/python/ref_string_rjust.asp) | Returns a right justified version of the string              |
| [rpartition()](https://www.w3schools.com/python/ref_string_rpartition.asp) | Returns a tuple where the string is parted into three parts  |
| [rsplit()](https://www.w3schools.com/python/ref_string_rsplit.asp) | Splits the string at the specified separator, and returns a list |
| [rstrip()](https://www.w3schools.com/python/ref_string_rstrip.asp) | Returns a right trim version of the string                   |
| [split()](https://www.w3schools.com/python/ref_string_split.asp) | Splits the string at the specified separator, and returns a list |
| [splitlines()](https://www.w3schools.com/python/ref_string_splitlines.asp) | Splits the string at line breaks and returns a list          |
| [startswith()](https://www.w3schools.com/python/ref_string_startswith.asp) | Returns true if the string starts with the specified value   |
| [strip()](https://www.w3schools.com/python/ref_string_strip.asp) | Returns a trimmed version of the string                      |
| [swapcase()](https://www.w3schools.com/python/ref_string_swapcase.asp) | Swaps cases, lower case becomes upper case and vice versa    |
| [title()](https://www.w3schools.com/python/ref_string_title.asp) | Converts the first character of each word to upper case      |
| [translate()](https://www.w3schools.com/python/ref_string_translate.asp) | Returns a translated string                                  |
| [upper()](https://www.w3schools.com/python/ref_string_upper.asp) | Converts a string into upper case                            |
| [zfill()](https://www.w3schools.com/python/ref_string_zfill.asp) | Fills the string with a specified number of 0 values at the beginning |

# List

## Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range.When specifying a range, the return value will be a new list with the specified items.

Return the third, fourth, and fifth item:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```

> [!NOTE]
>
> The search will start at index 2 (included) and end at index 5 (not included).

### Check

To determine if a specified item is present in a list use the `in` keyword:

Check if "apple" is present in the list:

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
 print("Yes, 'apple' is in the fruits list")
```