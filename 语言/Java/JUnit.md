# JUnit Java测试

<hr>

## 用途

JUnit是一个非常流行的单元测试框架，可以很容易的组织测试用例套件。

- **框架功能**：JUnit 提供了注解、断言和运行器，帮助开发者自动化测试过程。
- **设计理念**：通过框架驱动测试方法的运行，而不是依赖 `main` 方法手动调用。

当代码修改后，应该运行测试用例。如果发现 **bug**，需要补充新的测试用例以确保问题修复并避免重复出现。



## JUnit的核心

**`@Test` 注解**

- 标识某个方法为测试方法。
- JUnit 的运行器会扫描所有带有 `@Test` 注解的方法，并自动执行。

**断言（Assertion）**

- 用于验证测试结果是否与预期一致。
- 如果断言失败，测试标记为失败，并输出具体的错误信息。

### 常用的断言方法（Assertions API）

| 方法                                     | 功能说明                                   |
| ---------------------------------------- | ------------------------------------------ |
| `assertEquals(expected, actual)`         | 检查两个值是否相等。                       |
| `assertNotEquals(unexpected, actual)`    | 检查两个值是否不相等。                     |
| `assertTrue(condition)`                  | 检查条件是否为真。                         |
| `assertFalse(condition)`                 | 检查条件是否为假。                         |
| `assertNull(object)`                     | 检查对象是否为 `null`。                    |
| `assertNotNull(object)`                  | 检查对象是否不为 `null`。                  |
| `assertThrows(expectedType, executable)` | 检查是否抛出了指定类型的异常。             |
| `assertAll()`                            | 用于分组多个断言，确保所有断言都会被检查。 |

------

示例代码

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AssertionExample {

    @Test
    void testAssertions() {
        // 断言两个值相等
        assertEquals(4, 2 + 2, "Addition result is incorrect");

        // 断言条件为真
        assertTrue(5 > 3, "Expected condition to be true");

        // 断言对象不为空
        assertNotNull("Hello", "Object should not be null");

        // 断言抛出异常
        assertThrows(ArithmeticException.class, () -> {
            int result = 1 / 0;
        }, "Expected ArithmeticException");
    }
}
```

### 注意

- 在 JUnit 测试中，断言失败并不会终止程序，而是记录测试失败的结果。
- 断言通常用于测试环境，不建议直接在生产代码中使用（除了 `assert` 关键字，这是 Java 自带的断言机制）。

### 生命周期注解

JUnit 提供了多个注解来管理测试方法的生命周期，适用于复杂的测试场景。

| 注解          | 功能说明                                                     |
| ------------- | ------------------------------------------------------------ |
| `@BeforeAll`  | 在所有测试方法运行前执行，适用于初始化全局资源（需为静态方法）。 |
| `@AfterAll`   | 在所有测试方法运行后执行，适用于释放全局资源（需为静态方法）。 |
| `@BeforeEach` | 在每个测试方法运行前执行，用于设置测试环境。                 |
| `@AfterEach`  | 在每个测试方法运行后执行，用于清理测试环境。                 |

#### 生命周期示例

```java
import org.junit.jupiter.api.*;

public class LifecycleExample {

    @BeforeAll
    static void setupAll() {
        System.out.println("Setup for all tests");
    }

    @BeforeEach
    void setupEach() {
        System.out.println("Setup for each test");
    }

    @Test
    void testOne() {
        System.out.println("Running Test One");
    }

    @Test
    void testTwo() {
        System.out.println("Running Test Two");
    }

    @AfterEach
    void teardownEach() {
        System.out.println("Teardown for each test");
    }

    @AfterAll
    static void teardownAll() {
        System.out.println("Teardown for all tests");
    }
}
```

**输出示例：**

```
Setup for all tests
Setup for each test
Running Test One
Teardown for each test
Setup for each test
Running Test Two
Teardown for each test
Teardown for all tests
```

------

### 控制测试执行顺序

默认情况下，JUnit 不保证测试方法的执行顺序。如果需要控制顺序，可以使用 `@TestMethodOrder` 注解。

#### 按顺序执行示例

```java
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.MethodOrderer.OrderAnnotation;

@TestMethodOrder(OrderAnnotation.class)
public class OrderedTests {

    @Test
    @Order(1)
    void testFirst() {
        System.out.println("First test");
    }

    @Test
    @Order(2)
    void testSecond() {
        System.out.println("Second test");
    }
}
```