---
title: Java 数据库
date: 2025-05-17
author: Holmes Amzish
---

# Java 数据库概览

## Jdbc

## MyBatis





创建项目mybatis项目，首先需要使用maven导入mybatis库

poml.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.arorms</groupId>
    <artifactId>MybatisDemo</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.16</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.33</version>
        </dependency>
    </dependencies>

</project>
```

```
your-project/
├── src/main/java/
│   └── com/yourcompany/yourproject/
│       ├── config/             // 配置相关
│       │   └── MyBatisConfig.java  // Spring 配置类，用于集成 MyBatis
│       ├── dao/                // 数据访问对象 (DAO) 或 Mapper 接口
│       │   └── UserMapper.java
│       ├── entity/             // 实体类 (Entities)
│       │   └── User.java
│       ├── service/            // 业务逻辑层 (Services)
│       │   └── UserService.java
│       │   └── UserServiceImpl.java
│       ├── controller/         // 控制器 (Controllers)
│       │   └── UserController.java
│       └── App.java            // Spring Boot 启动类 (如果使用 Spring Boot)
├── src/main/resources/
│   ├── application.properties  // Spring Boot 配置文件
│   ├── mybatis-config.xml      // MyBatis 全局配置文件
│   └── mapper/               // MyBatis 映射文件
│       └── UserMapper.xml
└── pom.xml                     // Maven 项目配置文件 (如果使用 Maven)
    # 或 build.gradle             // Gradle 项目配置文件 (如果使用 Gradle)
```



编写mybatis设置

resources\mybatis-config.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
  <environments default="development">
    <environment id="development">
      <transactionManager type="JDBC"/>
      <dataSource type="POOLED">
        <property name="driver" value="${driver}"/>
        <property name="url" value="${url}"/>
        <property name="username" value="${username}"/>
        <property name="password" value="${password}"/>
      </dataSource>
    </environment>
  </environments>
  <mappers>
    <mapper resource="org/mybatis/example/BlogMapper.xml"/>
  </mappers>
</configuration>
```

resources\mapper\flightMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.arorms.mapper.FlightMapper">
    <select id="getByFlightAll" resultType="cn.arorms.entity.FlightEntity">
        SELECT id,
               flight_id as flightId,
               company,
               departure_airport as departureAirport,
               arrive_airport as arrivalAirport,
               departure_time as departureTime,
               arrive_time as arrivalTime,
               model,
               is_delete as isDelete
        FROM flight;
    </select>
</mapper>
```



## resultMap

```xml
    <select id="getByFlightAll" resultType="cn.arorms.entity.FlightEntity">
        SELECT id,
               flight_id as flightId,
               company,
               departure_airport as departureAirport,
               arrive_airport as arrivalAirport,
               departure_time as departureTime,
               arrive_time as arrivalTime,
               model,
               is_delete as isDelete
        FROM flight;
    </select>
```



定义数据库表中字段名称与类中成员属性名称，创建关联映射。

src\main\resources\mapper\flightMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.arorms.mapper.FlightMapper">
    <!-- SQL语句更改 -->
    <resultMap id="flightEntityMap" type="cn.arorms.entity.FlightEntity">
    	<id column="id" property="id"></id>
        <result column="flight_id" property="flightId"></result>
        <result column="company" property="company"></result>
        <result column="departure_airport" property="departureAirport"></result>
        <result column="arrive_airport" property="arrivalAirport"></result>
        <result column="departure_time" property="departureTime"></result>
        <result column="arrive_time" property="arrivalTime"></result>
        <result column="model" property="model"></result>
        <result column="is_delete" property="isDelete"></result>
    </resultMap>
    <!-- 创建关系映射 -->
    <select id="getByFlightAll" resultType="cn.arorms.entity.FlightEntity">
        SELECT id,
               flight_id as flightId,
               company,
               departure_airport as departureAirport,
               arrive_airport as arrivalAirport,
               departure_time as departureTime,
               arrive_time as arrivalTime,
               model,
               is_delete as isDelete
        FROM flight;
    </select>
    
    <select id="getByFlightAll" resultMap="flightEntityMap">
        SELECT * FROM flight;
    </select>
</mapper>
```



# Spring Boot Starter MyBatis

**Spring Boot Starter MyBatis** 是由 MyBatis 社区为 Spring Boot 提供的集成库，简化了 MyBatis 与 Spring Boot 的结合。它通过自动配置功能，减少了手动配置 SqlSessionFactory 和 Mapper 的工作，支持注解和 XML 两种方式定义 SQL。你只需要添加依赖、配置数据源和 Mapper，就能快速上手。

如果你想用**注解方式**替代 XML 文件来定义 SQL 操作，Spring Boot Starter MyBatis 完全支持这种方式。注解方式更简洁，适合简单的 CRUD 操作，尤其当你不想维护额外的 XML 文件时。

### **一、注解方式的特点**
- 使用 MyBatis 提供的注解（如 `@Select`、`@Insert`、`@Update`、`@Delete`）直接在 Mapper 接口中定义 SQL。
- 不需要 `UserMapper.xml` 文件，配置中也无需指定 `mybatis.mapper-locations`。
- 适合简单查询，复杂查询仍推荐 XML。

### **二、构建和编写过程**

#### **1. 项目依赖和配置**
- **POM 文件**：保持不变，前述依赖已足够。
- **application.properties**：
  - 删除 `mybatis.mapper-locations`，因为不再使用 XML。
  - 保留其他配置：
    ```properties
    spring.datasource.url=jdbc:mysql://localhost:3306/mydb?useSSL=false&serverTimezone=UTC
    spring.datasource.username=root
    spring.datasource.password=yourpassword
    spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
    mybatis.type-aliases-package=com.example.demo.model
    mybatis.configuration.map-underscore-to-camel-case=true
    ```

#### **2. 项目结构**
- 删除 `resources/mapper/UserMapper.xml`，所有 SQL 移到 Mapper 接口中。
- 其他结构不变：
  ```
  com.example.demo
  ├── model
  │   └── User.java
  ├── mapper
  │   └── UserMapper.java
  ├── service
  │   └── UserService.java
  ├── controller
  │   └── UserController.java
  ├── DemoApplication.java
  └── resources
      └── application.properties
  ```

#### **3. 编写代码**

##### **3.1 实体类 (`User.java`)**
保持不变：
```java
package com.example.demo.model;

import lombok.Data;

@Data
public class User {
    private Long id;
    private String name;
    private String email;
}
```

##### **3.2 Mapper 接口 (`UserMapper.java`)**
使用注解定义 SQL：
```java
package com.example.demo.mapper;

import com.example.demo.model.User;
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface UserMapper {
    @Select("SELECT id, name, email FROM users")
    List<User> findAll();

    @Select("SELECT id, name, email FROM users WHERE id = #{id}")
    User findById(Long id);

    @Insert("INSERT INTO users (name, email) VALUES (#{name}, #{email})")
    @Options(useGeneratedKeys = true, keyProperty = "id")  // 自增主键回填
    void insert(User user);

    @Update("UPDATE users SET name = #{name}, email = #{email} WHERE id = #{id}")
    void update(User user);

    @Delete("DELETE FROM users WHERE id = #{id}")
    void delete(Long id);
}
```
- **注解说明**：
  - `@Select`：查询语句。
  - `@Insert`：插入语句，`@Options` 用于处理自增主键。
  - `@Update`：更新语句。
  - `@Delete`：删除语句。
  - 参数使用 `#{}` 绑定，字段名与实体类属性一致（驼峰映射已启用）。

##### **3.3 服务层 (`UserService.java`)**
不变，仍调用 Mapper 接口：
```java
package com.example.demo.service;

import com.example.demo.mapper.UserMapper;
import com.example.demo.model.User;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {
    private final UserMapper userMapper;

    public UserService(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    public List<User> getAllUsers() {
        return userMapper.findAll();
    }

    public User getUserById(Long id) {
        return userMapper.findById(id);
    }

    public void createUser(User user) {
        userMapper.insert(user);
    }

    public void updateUser(User user) {
        userMapper.update(user);
    }

    public void deleteUser(Long id) {
        userMapper.delete(id);
    }
}
```

##### **3.4 控制器 (`UserController.java`)**
不变，仍提供 REST API：
```java
package com.example.demo.controller;

import com.example.demo.model.User;
import com.example.demo.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public List<User> getAll() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @PostMapping
    public void create(@RequestBody User user) {
        userService.createUser(user);
    }

    @PutMapping("/{id}")
    public void update(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        userService.updateUser(user);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

##### **3.5 主应用类 (`DemoApplication.java`)**
不变，仍需扫描 Mapper：
```java
package com.example.demo;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.example.demo.mapper")
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

---

#### **4. 运行和测试**
- **启动**：运行 `DemoApplication.java` 或 `mvn spring-boot:run`。
- **测试**：与 XML 方式相同，使用 Postman：
  - GET `http://localhost:8080/users`
  - GET `http://localhost:8080/users/1`
  - POST `http://localhost:8080/users`（`{"name": "Alice", "email": "alice@example.com"}`）
  - PUT `http://localhost:8080/users/1`
  - DELETE `http://localhost:8080/users/1`

---

### **三、注解方式的优缺点**
- **优点**：
  - 代码更集中，无需维护 XML 文件。
  - 适合简单 CRUD，开发效率高。
- **缺点**：
  - 复杂查询（多表联查、动态 SQL）编写困难，注解支持有限。
  - SQL 可读性不如 XML。

**解决复杂查询**：
- 使用 `@SelectProvider` 或混合 XML：
  ```java
  @SelectProvider(type = UserSqlProvider.class, method = "getDynamicSql")
  List<User> findByCondition(String condition);
  ```
  - 但通常建议复杂逻辑仍用 XML。

你说得对，MyBatis 的注解方式在处理复杂查询（如动态 SQL、多表联查、条件分支等）时确实不如 XML 灵活，但通过 **`@SelectProvider`（以及类似的 `@InsertProvider`、`@UpdateProvider`、`@DeleteProvider`）** 可以很好地解决这个问题。`Provider` 机制允许你在 Java 代码中动态生成 SQL，从而结合注解的简洁性和动态 SQL 的灵活性，非常适合复杂场景。

下面我会基于之前的项目，详细讲解如何使用 `Provider` 来处理复杂查询，并提供完整的代码示例和笔记式指导。假设我们需要实现一个动态条件查询用户（例如根据名字或邮箱模糊搜索），我会展示全过程。

---

### **一、`Provider` 机制简介**
- **`@SelectProvider`** 等注解允许你指定一个类和方法，由该方法动态返回 SQL 语句。
- **优点**：
  - 动态生成 SQL，支持条件分支、循环等逻辑。
  - 保持注解方式，避免 XML。
- **适用场景**：复杂查询、动态条件、多表操作。

---

### **二、修改后的项目实现**

#### **1. 项目依赖和配置**
- **POM 文件**：无需改动，前述依赖已足够。
- **application.properties**：保持不变：
  ```properties
  spring.datasource.url=jdbc:mysql://localhost:3306/mydb?useSSL=false&serverTimezone=UTC
  spring.datasource.username=root
  spring.datasource.password=yourpassword
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  mybatis.type-aliases-package=com.example.demo.model
  mybatis.configuration.map-underscore-to-camel-case=true
  ```

#### **2. 项目结构**
新增一个 `Provider` 类，其他保持不变：
```
com.example.demo
├── model
│   └── User.java
├── mapper
│   ├── UserMapper.java
│   └── UserSqlProvider.java  # 新增，提供动态 SQL
├── service
│   └── UserService.java
├── controller
│   └── UserController.java
├── DemoApplication.java
└── resources
    └── application.properties
```

#### **3. 编写代码**

##### **3.1 实体类 (`User.java`)**
不变：
```java
package com.example.demo.model;

import lombok.Data;

@Data
public class User {
    private Long id;
    private String name;
    private String email;
}
```

##### **3.2 新增 Provider 类 (`UserSqlProvider.java`)**
这个类负责动态生成 SQL：
```java
package com.example.demo.mapper;

public class UserSqlProvider {
    // 动态查询用户的 SQL
    public String findByCondition(String name, String email) {
        StringBuilder sql = new StringBuilder("SELECT id, name, email FROM users WHERE 1=1");
        
        // 动态添加条件
        if (name != null && !name.trim().isEmpty()) {
            sql.append(" AND name LIKE CONCAT('%', #{name}, '%')");
        }
        if (email != null && !email.trim().isEmpty()) {
            sql.append(" AND email LIKE CONCAT('%', #{email}, '%')");
        }
        
        return sql.toString();
    }
}
```
- **说明**：
  - 使用 `StringBuilder` 构建 SQL。
  - `WHERE 1=1` 避免后续条件拼接时需要判断是否加 `WHERE`。
  - `#{name}` 和 `#{email}` 是 MyBatis 参数占位符，与方法参数对应。

##### **3.3 Mapper 接口 (`UserMapper.java`)**
添加使用 `@SelectProvider` 的方法，其他方法保持简单注解：
```java
package com.example.demo.mapper;

import com.example.demo.model.User;
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface UserMapper {
    @Select("SELECT id, name, email FROM users")
    List<User> findAll();

    @Select("SELECT id, name, email FROM users WHERE id = #{id}")
    User findById(Long id);

    @Insert("INSERT INTO users (name, email) VALUES (#{name}, #{email})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    void insert(User user);

    @Update("UPDATE users SET name = #{name}, email = #{email} WHERE id = #{id}")
    void update(User user);

    @Delete("DELETE FROM users WHERE id = #{id}")
    void delete(Long id);

    // 新增动态查询方法
    @SelectProvider(type = UserSqlProvider.class, method = "findByCondition")
    List<User> findByCondition(@Param("name") String name, @Param("email") String email);
}
```
- **注解说明**：
  - `@SelectProvider` 指定 `UserSqlProvider` 类的 `findByCondition` 方法生成 SQL。
  - `@Param` 为参数命名，确保 Provider 方法能正确获取。

##### **3.4 服务层 (`UserService.java`)**
新增动态查询方法：
```java
package com.example.demo.service;

import com.example.demo.mapper.UserMapper;
import com.example.demo.model.User;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {
    private final UserMapper userMapper;

    public UserService(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    public List<User> getAllUsers() {
        return userMapper.findAll();
    }

    public User getUserById(Long id) {
        return userMapper.findById(id);
    }

    public void createUser(User user) {
        userMapper.insert(user);
    }

    public void updateUser(User user) {
        userMapper.update(user);
    }

    public void deleteUser(Long id) {
        userMapper.delete(id);
    }

    // 新增动态查询
    public List<User> searchUsers(String name, String email) {
        return userMapper.findByCondition(name, email);
    }
}
```

##### **3.5 控制器 (`UserController.java`)**
新增搜索接口：
```java
package com.example.demo.controller;

import com.example.demo.model.User;
import com.example.demo.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public List<User> getAll() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @PostMapping
    public void create(@RequestBody User user) {
        userService.createUser(user);
    }

    @PutMapping("/{id}")
    public void update(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        userService.updateUser(user);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        userService.deleteUser(id);
    }

    // 新增搜索接口
    @GetMapping("/search")
    public List<User> search(@RequestParam(required = false) String name,
                             @RequestParam(required = false) String email) {
        return userService.searchUsers(name, email);
    }
}
```

##### **3.6 主应用类 (`DemoApplication.java`)**
不变：
```java
package com.example.demo;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.example.demo.mapper")
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

---

#### **4. 运行和测试**
- **启动**：运行 `DemoApplication.java` 或 `mvn spring-boot:run`。
- **测试动态查询**：
  - **GET** `http://localhost:8080/users/search?name=Alice`：搜索名字含 "Alice" 的用户。
  - **GET** `http://localhost:8080/users/search?email=example.com`：搜索邮箱含 "example.com" 的用户。
  - **GET** `http://localhost:8080/users/search?name=Alice&email=example.com`：组合条件搜索。
  - （留空参数则返回所有用户，因为 `WHERE 1=1`）。

---

### **三、`Provider` 的更多用法**
1. **复杂条件**：
   - 在 `UserSqlProvider` 中添加更多逻辑：
     ```java
     public String findByCondition(String name, String email, Integer limit) {
         StringBuilder sql = new StringBuilder("SELECT id, name, email FROM users WHERE 1=1");
         if (name != null && !name.trim().isEmpty()) {
             sql.append(" AND name LIKE CONCAT('%', #{name}, '%')");
         }
         if (email != null && !email.trim().isEmpty()) {
             sql.append(" AND email LIKE CONCAT('%', #{email}, '%')");
         }
         if (limit != null && limit > 0) {
             sql.append(" LIMIT #{limit}");
         }
         return sql.toString();
     }
     ```
   - Mapper 接口：
     ```java
     @SelectProvider(type = UserSqlProvider.class, method = "findByCondition")
     List<User> findByCondition(@Param("name") String name, @Param("email") String email, @Param("limit") Integer limit);
     ```

2. **多表联查**：
   - 示例：
     ```java
     public String findUserWithOrders(Long userId) {
         return "SELECT u.id, u.name, u.email, o.order_id " +
                "FROM users u LEFT JOIN orders o ON u.id = o.user_id " +
                "WHERE u.id = #{userId}";
     }
     ```

3. **防止 SQL 注入**：
   - `Provider` 中只拼接 SQL 结构，参数仍用 `#{}` 绑定，避免直接拼接值。

---

### **四、笔记总结**
- **依赖和配置**：不变。
- **新增**：
  - `UserSqlProvider`：动态生成 SQL。
  - Mapper：用 `@SelectProvider` 调用 Provider。
  - Service 和 Controller：增加搜索方法。
- **测试**：验证动态条件生效。

**优点**：
- 灵活性接近 XML，但保持注解方式。
- 适合复杂查询，又不失代码可控性。

如果需要更复杂的例子（比如嵌套查询、分页），告诉我，我可以进一步扩展！
