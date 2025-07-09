添加引用

```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.8.5</version>
</dependency>
```

在项目设置 `application.properties` 中添加：

```properties
springdoc.api-docs.enabled=true
springdoc.api-docs.title=<your_title>
springdoc.api-docs.description=<your_description>
springdoc.api-docs.version=OPENAPI_3_1
springdoc.swagger-ui.enabled=true
springdoc.swagger-ui.path=/swagger-ui.html
```



以下是一个简单的 Controller 类，返回 Hello World，或者根据 GET 方法传入的参数返回名字。

```java
package cn.arorms.sdd.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * HelloController.java
 * @version 1.0 2025-02-24
 * @author Holmes Amzish
 */

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String sayHello(
            @RequestParam(value = "name", defaultValue = "World") String name
    ) {
        return String.format("Hello %s!", name);
    }
}

```

添加引用，并为函数和参数添加解释。

```java
package cn.arorms.sdd.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * HelloController.java
 * @version 1.0 2025-02-24
 * @author Holmes Amzish
 */

@RestController
public class HelloController {

    @Operation(summary = "Say hello", description = "Returns a personalized hello message")
    @GetMapping("/hello")
    public String sayHello(
            @Parameter(description = "Name of the person to greet", example = "Alice")
            @RequestParam(value = "name", defaultValue = "World") String name
    ) {
        return String.format("Hello %s!", name);
    }
}
```

