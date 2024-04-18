# Data Types

```java
int myNum = 5;               // Integer (whole number)
float myFloatNum = 5.99f;    // Floating point number
char myLetter = 'D';         // Character
boolean myBool = true;       // Boolean
String myText = "Hello";     // String
```

Data types are divided into two groups:

- Primitive data types - includes `byte`, `short`, `int`, `long`, `float`, `double`, `boolean` and `char`
- Non-primitive data types - such as `String`, [Arrays](https://www.w3schools.com/java/java_arrays.asp) and [Classes](https://www.w3schools.com/java/java_classes.asp) (you will learn more about these in a later chapter)

## Primitive Data Types

A primitive data type specifies the size and type of variable values, and it has no additional methods.

There are eight primitive data types in Java:

| Data Type | Size    | Description                                                  |
| :-------- | :------ | :----------------------------------------------------------- |
| `byte`    | 1 byte  | Stores whole numbers from -128 to 127                        |
| `short`   | 2 bytes | Stores whole numbers from -32,768 to 32,767                  |
| `int`     | 4 bytes | Stores whole numbers from -2,147,483,648 to 2,147,483,647    |
| `long`    | 8 bytes | Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| `float`   | 4 bytes | Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits |
| `double`  | 8 bytes | Stores fractional numbers. Sufficient for storing 15 decimal digits |
| `boolean` | 1 bit   | Stores true or false values                                  |
| `char`    | 2 bytes | Stores a single character/letter or ASCII values             |

# String

## More String Methods

There are many string methods available, for example `toUpperCase()` and `toLowerCase()`:

```java
String txt = "Hello World";
System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
System.out.println(txt.toLowerCase());   // Outputs "hello world"
```

## Finding a Character in a String

The `indexOf()` method returns the **index** (the position) of the first occurrence of a specified text in a string (including whitespace):

```java
String txt = "Please locate where 'locate' occurs!";
System.out.println(txt.indexOf("locate")); // Outputs 7
```

## String Concatenation

The `+` operator can be used between strings to combine them. This is called **concatenation**

```java
String firstName = "John";
String lastName = "Doe";
System.out.println(firstName + " " + lastName);
```

You can also use the `concat()` method to concatenate two strings:

```java
String firstName = "John ";
String lastName = "Doe";
System.out.println(firstName.concat(lastName));
```