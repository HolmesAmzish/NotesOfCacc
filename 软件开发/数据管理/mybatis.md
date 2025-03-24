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

设置项目数据库

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/database_name
spring.datasource.username=username
spring.datasource.password=password
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.jpa.hibernate.ddl-auto=update
spring.jpa.database-platform=org.hibernate.dialect.MySQL5InnoDBDialect
```

## 实体类

```java
@
```

