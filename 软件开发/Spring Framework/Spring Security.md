---
title: Spring Security
author: Cacc
date: 2025-06-15
---

# Basic 认证

![image-20250615220924338](/home/cacc/Documents/NotesOfCacc/软件开发/Spring Framework/assets/image-20250615220924338.png)

Basic 认证是

session 进行会话保存和用户管理

```java
package cn.arorms.security.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;

@Configuration // Use @Configuration instead of @Component with @EnableWebSecurity
@EnableWebSecurity
public class SecurityConfig {

    // 1. PasswordEncoder Bean (Highly Recommended!)
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    // 2. UserDetailsService for in-memory users (replaces auth.inMemoryAuthentication())
    @Bean
    public UserDetailsService userDetailsService(PasswordEncoder passwordEncoder) {
        UserDetails user = User.builder()
                .username("admin")
                .password(passwordEncoder.encode("admin")) // Always encode passwords!
                .roles("USER", "ADMIN") // Use roles instead of authorities directly for common use cases
                .build();
        return new InMemoryUserDetailsManager(user);
    }

    // 3. SecurityFilterChain Bean (replaces WebSecurityConfigurerAdapter's configure(HttpSecurity))
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests(authorize -> authorize // Modern way to configure authorization
                        .anyRequest().authenticated() // All requests require authentication
                )
                .httpBasic(org.springframework.security.config.Customizer.withDefaults()); // Enable HTTP Basic with defaults
        // If you need to disable CSRF for API endpoints (e.g., if you're building a REST API
        // consumed by a separate frontend and handling CSRF there), you might add:
        // .csrf(csrf -> csrf.disable());

        return http.build();
    }
}
```

