# Python

Latest update:	2024.1.15

## Data Types

### Type Conversion

```python
x = 1	# int

# Convert from int to float
a = float(x)

# Print the data type of a
print(type(a))
```

### Random Number

```python
import random

# Print a number range from 1 to 10
print(random.randrange(1, 10))
```

### Specify Type

```python
x = int(2.8)	# x will be 2
y = float(1)	# y will be 1.0
z = str(3.0)	# z will be '3.0'
```

### String

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

### Strings Arrays

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

