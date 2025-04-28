# SpringBoot 的配置与环境

通过 Idea 创建 SpringBoot 项目，会首先通过 SpringBoot Initializer 来配置 SpringBoot 的基础依赖。创建后的项目文件结构如下：

```
cacc@paradiso [03:02:05 PM] [~/Repositories/SDDAnalyzer] [master *]
-> % tree
.
├── HELP.md
├── mvnw
├── mvnw.cmd
├── pom.xml  # 依赖配置文件
└── src
    ├── main
    │   ├── java
    │   │   └── cn
    │   │       └── arorms
    │   │           └── sddanalyzer
    │   │               └── SddAnalyzerApplication.java  # 程序启动入口
    │   └── resources
    │       └── application.properties  # 服务器设置文件
    └── test
        └── java
            └── cn
                └── arorms
                    └── sddanalyzer
                        └── SddAnalyzerApplicationTests.java

12 directories, 7 files
```

如果在创建完项目后还需要通过 Initializer 添加依赖，可以到 pom.xml 文件内手动添加依赖，例如:

```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter-test</artifactId>
    <version>3.0.4</version>
	<scope>test</scope>
</dependency>
```

也可以通过点击 dependencies 标签旁边的 Edit Starters... ，这是 Idea 快速编辑 SpringBoot 依赖的一个额外入口。