---
title: Maven
author: Holmes Amzish
date: 2025-03-30 19:29
---

# Maven

## 1. 什么是 Maven？
Maven 是一个广泛使用的构建自动化工具，主要用于 Java 项目。它通过标准化构建过程，简化依赖管理和项目配置。Maven 的核心理念是“约定优于配置”（Convention over Configuration），它提供了一个统一的构建系统。

### 核心功能
- **依赖管理**：自动下载和管理项目所需的库（jar 文件）。

- **构建生命周期**：定义了标准的构建阶段（如编译、测试、打包、部署）。

  仅需要通过简单的操作，既可以完成对项目的各种操作。

- **项目管理**：通过一个简单的 `pom.xml` 文件管理项目信息。

---

## 2. 安装 Maven

在 idea 中，IDE基本上已经存在了一个 Maven 依赖管理工具，但是只共 IDE 自己使用，并没有为系统环境提供 Maven 工具。一般需要另外手动安装。

### 安装步骤（以 Linux 为例）
1. **下载 Maven**：
   
   - 访问官网：https://maven.apache.org/download.cgi
   - 下载最新版本的二进制文件（如 `apache-maven-3.9.6-bin.tar.gz`）。
2. **解压文件**：
   ```bash
   tar -xzf apache-maven-3.9.6-bin.tar.gz -C /opt
   ```
3. **设置环境变量**：
   编辑 `~/.bashrc` 或 `/etc/profile`，添加以下内容：
   ```bash
   export MAVEN_HOME=/opt/apache-maven-3.9.9
   export PATH=$MAVEN_HOME/bin:$PATH
   ```
   保存后运行：
   ```bash
   source ~/.bashrc
   ```
4. **验证安装**：
   ```bash
   mvn -version
   ```
   输出类似：
   ```
   Apache Maven 3.9.6
   Java version: 11.0.15
   ```

---

## 3. Maven 的核心文件：POM 文件
POM（Project Object Model）是 Maven 的核心配置文件，文件名固定为 `pom.xml`。它定义了项目的元数据、依赖和构建规则。

### 一个简单的 `pom.xml` 示例
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- 项目坐标 -->
    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <!-- 项目名称和描述 -->
    <name>My First Maven Project</name>
    <description>A simple Maven project</description>

    <!-- 依赖 -->
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

- **groupId**：项目的组织标识，通常是公司或组织名称。
- **artifactId**：项目名称。
- **version**：项目版本，`SNAPSHOT` 表示开发中版本。
- **packaging**：打包类型（`jar`、`war` 等）。
- **dependencies**：定义项目依赖的库。

---

## 4. Maven 项目结构
Maven 默认遵循以下目录结构（约定优于配置）：
```
my-app/
├── pom.xml
└── src
    ├── main
    │   ├── java                # 源代码
    │   └── resources           # 资源文件（如配置文件）
    └── test
        ├── java                # 测试代码
        └── resources           # 测试资源文件
```

如果需要自定义目录结构，可以在 `pom.xml` 中配置，但建议遵循默认约定。

---

## 5. 常用 Maven 命令
Maven 通过命令行操作，以下是常用命令：

| 命令          | 作用                          |
| ------------- | ----------------------------- |
| `mvn clean`   | 清理项目（删除 target 目录）  |
| `mvn compile` | 编译源代码                    |
| `mvn test`    | 运行测试                      |
| `mvn package` | 打包项目（生成 jar/war 文件） |
| `mvn install` | 安装到本地仓库                |
| `mvn deploy`  | 部署到远程仓库                |

### 示例
1. 编译项目：
   ```bash
   mvn compile
   ```
   输出编译后的类文件到 `target/classes`。
2. 打包项目：
   ```bash
   mvn package
   ```
   生成 `my-app-1.0-SNAPSHOT.jar` 在 `target` 目录。

---

## 6. 依赖管理
Maven 的依赖管理是其最强大的功能之一。依赖通过 `<dependency>` 标签定义，Maven 会从中央仓库（默认是 Maven Central）下载。

### 添加依赖
例如，添加 Spring Boot Starter：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>3.2.4</version>
</dependency>
```

### 依赖范围（scope）
- `compile`：默认范围，编译和运行时都需要。
- `test`：仅用于测试（如 JUnit）。
- `provided`：编译时需要，运行时由容器提供（如 Servlet API）。
- `runtime`：运行时需要，编译时不需要（如 JDBC 驱动）。

### 更新依赖
运行以下命令更新本地依赖：
```bash
mvn dependency:resolve
```

---

## 7. 构建生命周期
Maven 定义了三个标准生命周期：
1. **clean**：清理项目。
2. **default**：核心构建过程（编译、测试、打包等）。
3. **site**：生成项目文档。

每个生命周期包含多个阶段（phase），例如 `default` 生命周期的主要阶段：
- `validate`：验证项目配置。
- `compile`：编译源代码。
- `test`：运行测试。
- `package`：打包。
- `install`：安装到本地仓库。
- `deploy`：部署到远程仓库。

运行某个阶段会自动执行其之前的所有阶段。例如：
```bash
mvn package
```
会依次执行 `validate`、`compile`、`test` 和 `package`。

---

## 8. 配置远程仓库
默认情况下，Maven 从 Maven Central 下载依赖。如果需要使用其他仓库（如公司私有仓库），可以在 `pom.xml` 中配置：

```xml
<repositories>
    <repository>
        <id>my-repo</id>
        <name>My Repository</name>
        <url>https://my.repo.com/repository</url>
    </repository>
</repositories>
```

---

## 9. 使用插件
Maven 的功能通过插件扩展。例如，编译 Java 代码使用的是 `maven-compiler-plugin`。

### 配置编译器版本
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.12.1</version>
            <configuration>
                <source>11</source>
                <target>11</target>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 常用插件
- `maven-surefire-plugin`：运行测试。
- `maven-war-plugin`：打包 WAR 文件。
- `spring-boot-maven-plugin`：Spring Boot 项目打包。

---

## 10. 创建一个 Maven 项目
使用 Maven 的 archetype 快速生成项目：
```bash
mvn archetype:generate \
  -DgroupId=com.example \
  -DartifactId=my-app \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DinteractiveMode=false
```
这会生成一个基本的 Java 项目。

---

## 11. 最佳实践
1. **保持 POM 文件简洁**：避免冗余配置。
2. **使用版本管理**：通过 `<properties>` 定义版本号，例如：
   ```xml
   <properties>
       <spring.version>5.3.27</spring.version>
   </properties>
   ```
3. **依赖冲突处理**：
   - 使用 `mvn dependency:tree` 查看依赖树。
   - 通过 `<exclusions>` 排除冲突依赖。
4. **缓存清理**：定期清理本地仓库（`~/.m2/repository`）以避免问题。

---

## 12. 常见问题与解决
- **依赖下载失败**：
  - 检查网络连接。
  - 使用 `mvn -U` 强制更新。
- **编译错误**：
  - 确认 JDK 版本与 `maven-compiler-plugin` 配置一致。
- **找不到命令 `mvn`**：
  - 检查环境变量是否正确配置。

---

## 13. 学习资源
- **官方文档**：https://maven.apache.org/guides/
- **Maven 实战**：推荐书籍《Maven 实战》（作者：许晓斌）。
- **在线教程**：Baeldung 的 Maven 系列（https://www.baeldung.com/maven）。

---

这份教程涵盖了 Maven 的基础到中级内容。如果你需要更深入的主题（如多模块项目、自定义插件开发），可以告诉我，我会进一步扩展！希望这份教程对你学习 Maven 有所帮助。