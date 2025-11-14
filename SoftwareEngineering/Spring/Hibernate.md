# Hibernate in Spring Data JPA

Hibernate JPA + PostgreSQL

## Basic Configuration

**application.yaml**

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/<database_name>
    username: postgres
    password: <password>
    driver-class-name: org.postgresql.Driver

  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true
    database-platform: org.hibernate.dialect.PostgreSQLDialect
```

Then set repository for SQL operation, most method was implemented by default.

## Entity (Model)

```java

```

## Repository

**UserRepository.java**

```java
package cn.arorms.list.backend.repository;
import cn.arorms.list.backend.model.entity.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

/**
 * UserRepository
 * @version 1.0 2025-07-04
 * @author Cacciatore
 */
public interface UserRepository extends JpaRepository<UserEntity, Long> {
    Optional<UserEntity> findByUsername(String username);
}
```

Then you can use it in service

## Service

**UserService**

```java
package cn.arorms.list.backend.service;
import cn.arorms.list.backend.model.entity.UserEntity;
import cn.arorms.list.backend.repository.UserRepository;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

/**
 * UserService
 * @version 1.0 2025-07-04
 * @author Cacciatore
 */
@Service
public class UserService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public UserEntity getByUsername(String username) {
        return userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found"));
    }
}
```
