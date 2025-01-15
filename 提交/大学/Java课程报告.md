# 一、问题概述

聊天室系统由客户端和服务端两部分组成。服务端程序负责监听客户端发来的消息，并处理用户的连接、消息传递以及在线用户管理等功能。客户端则需要通过登录服务端来参与聊天，并能够发送和接收消息。以下是服务器和客户端的主要功能描述：

## 1.1 服务器的主要功能

1. **监听客户端连接**，服务器在特定的端口上进行监听，等待客户端的连接请求。一旦客户端成功连接，服务器将保持与该客户端的通信通道，以便实时传递消息。
   
2. **发送系统消息**，服务器可以向所有已连接的客户端发送系统消息，例如通知用户加入或离开聊天室，或者广播重要的系统公告。
   
3. **统计在线人数**，服务器需要实时统计当前在线的用户数量，并将这一信息广播给所有客户端，以便用户了解聊天室的活跃情况。
   
4. **断开用户连接**，当服务器停止服务时，需要主动断开所有已连接用户的连接，并通知用户服务已终止。

## 1.2 客户端的主要功能

1. **连接服务器**，客户端需要能够连接到已开启聊天服务的服务器，并建立稳定的通信通道，以便发送和接收消息。
   
2. **配置用户名**，用户在连接服务器后，可以配置自己的显示名称。这个名称将用于标识用户在聊天室中的身份。
   
3. **登录与注销**，当服务器处于运行状态时，用户可以随时登录或注销。登录后，用户可以参与聊天；注销后，用户将退出聊天室。
   
4. **发送消息**，用户可以向聊天室中的所有用户发送公共消息，也可以选择向特定用户发送私密消息。系统需要支持这两种消息传递方式。

聊天室系统的设计目标是实现一个高效、稳定且易于扩展的实时通信平台。通过合理的技术选型和模块化设计，系统能够支持多用户同时在线，并确保消息的实时传递。同时，系统还需要具备良好的安全性和可维护性，以应对实际应用中的各种需求。

# 二、基本概念和原理

在设计和实现聊天室系统时，我们需要理解一些基本概念和原理，这些概念和原理是构建实时通信系统的基础。以下是本系统中涉及的主要概念和原理：

## 2.1 WebSocket 协议

WebSocket 是一种在单个 TCP 连接上进行全双工通信的协议。与传统的 HTTP 请求-响应模式不同，WebSocket 允许服务器和客户端之间进行实时、双向的通信。这使得 WebSocket 非常适合用于实时聊天应用。

利用 WebSocket 的的优势有实时性，允许服务器与客户端之间实时传递消息，无需客户端频繁轮询服务器。而由于连接是持久的，消息可以在连接建立后立即传递，减少了延迟。与 HTTP 轮询想必，WebSocket 减少了不必要的请求头和数据传输，节省了带宽。

WebSocket 连接的建立始于一个 HTTP 握手请求。客户端发送一个带有 `Upgrade: websocket` 头的 HTTP 请求，服务器如果支持 WebSocket，则会返回一个 `101 Switching Protocols` 响应，表示协议升级成功。此后，客户端和服务器之间的通信将通过 WebSocket 协议进行。

## 2.2 STOMP 协议

STOMP（Simple Text Oriented Messaging Protocol）是一种基于文本的协议，用于在客户端和服务器之间传递消息。协议定义了一种简单的消息格式，使得客户端和服务器可以通过 WebSocket 进行消息的发布和订阅。

STOMP 协议通常与 WebSocket 结合使用，以提供更高级的消息传递功能。通过 STOMP，客户端可以订阅特定的消息通道，并在消息到达时接收通知。服务器也可以将消息发送到特定的通道，客户端只需订阅该通道即可接收消息。

## 2.3 Spring Boot 和 WebSocket 集成

Spring Boot 提供了对 WebSocket 和 STOMP 协议的支持，使得开发者可以轻松地构建实时通信应用。Spring Boot 的 WebSocket 配置主要包括以下几个部分：

### 2.3.1 WebSocket 配置类

通过 `@EnableWebSocketMessageBroker` 注解，Spring Boot 可以启用 WebSocket 消息代理。配置类需要实现 `WebSocketMessageBrokerConfigurer` 接口，并重写 `registerStompEndpoints` 和 `configureMessageBroker` 方法。

**registerStompEndpoints**：用于注册 STOMP 端点，客户端通过该端点连接到 WebSocket 服务器。在这个方法中，我们可以指定 WebSocket 的端点路径，并可以选择启用 SockJS 支持。SockJS 是一个备选方案，当浏览器不支持 WebSocket 时，它会自动降级为其他协议（如 HTTP 长轮询），以确保兼容性。例如，`registry.addEndpoint("/ws").withSockJS();` 表示在 `/ws` 路径上启用 WebSocket，并支持 SockJS。

**configureMessageBroker**：用于配置消息代理，包括应用程序目的地前缀和消息代理前缀。在这个方法中，我们可以设置消息代理的前缀（如 `/topic` 或 `/queue`），以及应用程序目的地的前缀（如 `/app`）。消息代理前缀用于标识消息的广播通道，而应用程序目的地前缀用于标识客户端发送消息的目标路径。例如，`registry.setApplicationDestinationPrefixes("/app");` 表示客户端发送的消息将以 `/app` 为前缀，而 `registry.enableSimpleBroker("/topic");` 表示服务器将使用 `/topic` 作为消息广播的前缀。

### 2.3.2 WebSocket 控制器

WebSocket 控制器用于处理客户端发送的消息，并将消息转发到指定的目的地。通过 `@MessageMapping` 注解，控制器可以处理特定目的地的消息，并通过 `@SendTo` 注解将消息发送到指定的主题。

**@MessageMapping**：该注解用于映射客户端发送的消息到控制器的方法。例如，`@MessageMapping("/chat.sendMessage")` 表示当客户端向 `/app/chat.sendMessage` 发送消息时，该方法将被调用。方法参数可以通过 `@Payload` 注解绑定到消息的主体内容。

**@SendTo**：该注解用于指定消息的发送目的地。例如，`@SendTo("/topic/public")` 表示处理完消息后，服务器会将消息广播到 `/topic/public` 主题，所有订阅了该主题的客户端都会收到这条消息。

WebSocket 控制器的设计使得消息的处理和转发变得非常简单。开发者只需关注业务逻辑的实现，而无需关心底层的通信细节。

### 2.3.3 WebSocket 事件监听

Spring Boot 提供了 `@EventListener` 注解，用于监听 WebSocket 事件，如连接建立、断开连接等。通过监听这些事件，服务器可以在用户连接或断开时执行相应的操作，如更新在线用户列表。

**SessionConnectEvent**：当客户端成功连接到 WebSocket 服务器时触发。可以通过监听该事件来记录用户的连接信息，例如将用户名存储在会话属性中。

**SessionDisconnectEvent**：当客户端断开连接时触发。可以通过监听该事件来清理用户的相关信息，例如从在线用户列表中移除该用户。

**StompHeaderAccessor**：用于访问 WebSocket 会话的头部信息。通过该对象，可以获取会话中的自定义属性，例如用户名、用户 ID 等。

通过 WebSocket 事件监听，服务器可以实时感知用户的状态变化，并根据这些变化执行相应的逻辑。例如，当用户断开连接时，服务器可以广播一条系统消息，通知其他用户该用户已离开。

## 2.4 数据库与用户验证

为了实现用户登录和验证功能，系统需要与数据库进行交互。本系统使用 MariaDB 作为数据库，并通过 MyBatis 框架进行数据库操作。通过 `application.properties` 文件配置数据库连接信息，包括数据库 URL、用户名、密码等。MyBatis 的映射文件用于定义 SQL 查询和结果映射。用户实体类 `User` 用于表示用户的基本信息，包括用户名、密码和电子邮件。MyBatis 的映射文件 `UserMapper.xml` 定义了查询用户信息的 SQL 语句。用户服务类 `UserService` 负责调用 MyBatis 映射接口，执行数据库查询操作。登录控制器 `AuthController` 处理用户登录请求，并调用用户服务进行验证。

## 2.5 实时消息处理

实时消息处理是聊天室系统的核心功能。通过 WebSocket 和 STOMP 协议，系统可以实现消息的实时收发。

消息实体类 `ChatMessage` 用于表示聊天消息的基本属性，包括消息内容、发送者和消息类型。消息类型通过枚举类 `MessageType` 定义，包括普通聊天消息、用户加入和用户离开。

通过 `SimpMessageSendingOperations` 接口，服务器可以将消息广播到指定的主题。客户端订阅该主题后，即可接收服务器发送的消息。

通过 `OnlineUserTracker` 类，系统可以跟踪在线用户的数量，并在用户连接或断开时更新在线用户列表。服务器可以通过 WebSocket 将在线用户数量广播给所有客户端。

通过理解 WebSocket、STOMP 协议以及 Spring Boot 的集成方式，我们可以构建一个功能完善的实时聊天室系统。系统不仅需要处理实时消息的收发，还需要考虑用户验证、在线用户统计以及安全性等问题。通过合理的设计和实现，系统可以提供稳定、安全的实时通信服务。

# 三、系统整体设计

聊天室系统的整体设计分为客户端和服务端两部分。服务端负责处理客户端的连接请求、消息的接收与广播、用户验证以及在线用户的管理。客户端则负责与服务端建立连接，发送和接收消息，并提供用户界面供用户交互。以下是系统的整体设计思路和模块划分：

## 3.1 系统架构

聊天室系统采用 **C/S（客户端/服务器）架构**，客户端通过 WebSocket 协议与服务端建立长连接，实现实时通信。服务端使用 Spring Boot 框架搭建，集成了 WebSocket 和 STOMP 协议，支持高并发的消息处理。数据库使用 MariaDB，通过 MyBatis 框架进行数据持久化操作。

### 3.1.1 服务端架构

服务端的主要模块包括：**WebSocket 配置模块**：负责配置 WebSocket 和 STOMP 协议，定义消息代理和端点。**消息处理模块**：负责接收客户端发送的消息，并根据消息类型进行处理和广播。**用户验证模块**：负责用户的登录验证，确保只有合法用户才能进入聊天室。**在线用户管理模块**：负责维护在线用户列表，并在用户连接或断开时更新列表。**数据库模块**：负责与数据库交互，存储用户信息和消息记录。

### 3.1.2 客户端架构

客户端的主要模块包括**连接管理模块**：负责与服务端建立 WebSocket 连接，并处理连接状态的变化。**消息发送与接收模块**：负责发送用户输入的消息，并接收服务端广播的消息。**用户界面模块**：提供用户交互界面，显示聊天内容、在线用户列表和系统消息。

## 3.2 模块划分与交互

### 3.2.1 服务端模块

1. **WebSocket 配置模块**，负责配置 WebSocket 端点（如 `/ws`）和消息代理（如 `/topic` 和 `/app`）。支持 SockJS，确保在不支持 WebSocket 的浏览器中也能正常使用。
   
2. **消息处理模块**，通过 `@MessageMapping` 注解处理客户端发送的消息。使用 `@SendTo` 注解将消息广播到指定的主题（如 `/topic/public`）。
   
3. **用户验证模块**，通过 REST API 接收客户端的登录请求。调用数据库模块验证用户信息，并返回验证结果。
   
4. **在线用户管理模块**，使用 `OnlineUserTracker` 类维护在线用户列表。通过 WebSocket 事件监听器（如 `SessionConnectEvent` 和 `SessionDisconnectEvent`）更新在线用户列表。
   
5. **数据库模块**，使用 MyBatis 框架进行数据库操作。定义用户实体类和映射文件，执行 SQL 查询。

### 3.2.2 客户端模块

1. **连接管理模块**，使用 WebSocket API 或 SockJS 与服务端建立连接。处理连接成功、断开和错误事件。
   
2. **消息发送与接收模块**，使用 STOMP 协议发送消息到服务端（如 `/app/chat.sendMessage`）。订阅服务端的消息主题（如 `/topic/public`），接收广播消息。
   
3. **用户界面模块**，提供输入框、按钮等控件，供用户输入消息和操作。实时显示聊天内容、在线用户列表和系统消息。

## 3.3 数据流设计

### 3.3.1 消息发送流程

用户在客户端输入消息并点击发送按钮。客户端通过 STOMP 协议将消息发送到服务端的 /app/chat.sendMessage 端点。服务端的 `ChatController` 接收到消息后，将其广播到 `/topic/public` 主题。所有订阅了 `/topic/public` 主题的客户端都会收到这条消息，并在界面上显示。

### 3.3.2 用户登录流程

用户在客户端输入用户名和密码，点击登录按钮。客户端通过 REST API 将登录请求发送到服务端的 /api/auth/login 端点。服务端的 AuthController 接收到请求后，调用 `UserService` 进行用户验证。如果验证成功，客户端与服务端建立 WebSocket 连接，并进入聊天室。

### 3.3.3 在线用户更新流程

当用户成功连接到服务端时，触发 SessionConnectEvent 事件。服务端的 WebSocketEventListener 监听该事件，并将用户添加到在线用户列表。服务端将更新后的在线用户数量广播到 `/topic/onlineCount` 主题。所有订阅了 `/topic/onlineCount` 主题的客户端都会收到更新后的在线用户数量，并在界面上显示。

## 3.4 数据库设计

### 3.4.1 用户表设计

用户表 `users` 用于存储用户的基本信息，包括用户名、密码和电子邮件。表结构如下：

| 字段名   | 类型         | 描述           |
| -------- | ------------ | -------------- |
| username | VARCHAR(50)  | 用户名（主键） |
| password | VARCHAR(50)  | 密码           |
| email    | VARCHAR(100) | 电子邮件       |

### 3.4.2 消息表设计

消息表 `messages` 用于存储聊天记录，包括消息内容、发送者和发送时间。表结构如下：

| 字段名    | 类型        | 描述           |
| --------- | ----------- | -------------- |
| id        | BIGINT      | 消息ID（主键） |
| content   | TEXT        | 消息内容       |
| sender    | VARCHAR(50) | 发送者         |
| timestamp | DATETIME    | 发送时间       |

## 3.6 总结

通过合理的系统设计和模块划分，聊天室系统能够实现高效的实时通信功能。服务端通过 WebSocket 和 STOMP 协议处理消息的收发，客户端通过简洁的用户界面与用户交互。数据库模块和用户验证模块确保了系统的安全性和数据的持久化。通过进一步优化和扩展，系统可以支持更多功能，如私聊、消息记录查询等。

# 四、主要模块的设计和实现

## 4.1 实时消息

实时消息模块是聊天室系统的核心功能之一，负责处理用户发送的消息并将其广播给所有在线用户。该模块的设计包括消息实体的定义、WebSocket 服务器的配置、事件监听以及消息控制器的实现。

### 4.1.1 消息实体

消息实体是系统中消息传递的基本数据结构，用于封装消息的内容、发送者以及消息类型。通过定义消息实体，系统可以统一管理不同类型的消息，并方便后续的扩展。

消息实体类 `ChatMessage`

```java
package cn.arorms.chat.model;

import lombok.Builder;
import lombok.Data;

/**
 * Message entity
 * @version 1.0 2025-01-10
 */
@Data
@Builder
public class ChatMessage {

    private String content;  // 消息内容
    private String sender;   // 发送者
    private MessageType type; // 消息类型
}
```

- **`content`**：消息的具体内容，通常是用户输入的文本。
- **`sender`**：消息的发送者，通常是用户的用户名。
- **`type`**：消息的类型，用于区分普通聊天消息、用户加入和用户离开等不同场景。

消息类型枚举 `MessageType`

```java
package cn.arorms.chat.model;

public enum MessageType {
    CHAT,  // 普通聊天消息
    JOIN,  // 用户加入聊天室
    LEAVE  // 用户离开聊天室
}
```

- **`CHAT`**：表示普通的聊天消息。
- **`JOIN`**：表示用户加入聊天室时的系统消息。
- **`LEAVE`**：表示用户离开聊天室时的系统消息。

通过消息实体和消息类型的定义，系统可以清晰地处理不同类型的消息，并在客户端进行相应的展示。

### 4.1.2 WebSocket 服务器设置

为了实现实时消息的收发，系统需要配置 WebSocket 服务器。Spring Boot 提供了对 WebSocket 和 STOMP 协议的支持，使得开发者可以轻松地搭建实时通信服务。

WebSocket 配置类 `WebSocketConfig`

```java
package cn.arorms.chat.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;
import org.springframework.web.socket.config.annotation.StompEndpointRegistry;
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer;

@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        // 注册 STOMP 端点，客户端通过该端点连接到 WebSocket 服务器
        registry.addEndpoint("/ws").withSockJS();
    }

    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        // 设置应用程序目的地前缀，客户端发送的消息将以 /app 为前缀
        registry.setApplicationDestinationPrefixes("/app");
        // 启用简单的消息代理，客户端可以订阅 /topic 主题以接收广播消息
        registry.enableSimpleBroker("/topic");
    }
}
```

- **`registerStompEndpoints`**：注册 STOMP 端点 `/ws`，并启用 SockJS 支持。SockJS 是一个备选方案，当浏览器不支持 WebSocket 时，它会自动降级为其他协议（如 HTTP 长轮询），以确保兼容性。
- **`configureMessageBroker`**：配置消息代理，设置应用程序目的地前缀为 `/app`，并启用简单的消息代理，客户端可以订阅 `/topic` 主题以接收广播消息。

### 4.1.3 WebSocket 事件监听

WebSocket 事件监听器用于监听客户端的连接和断开事件，并在这些事件发生时执行相应的操作，例如更新在线用户列表。

WebSocket 事件监听类 `WebSocketEventListener`

```java
package cn.arorms.chat.config;

import cn.arorms.chat.service.OnlineUserTracker;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.event.EventListener;
import org.springframework.messaging.simp.SimpMessageSendingOperations;
import org.springframework.messaging.simp.stomp.StompHeaderAccessor;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.messaging.SessionDisconnectEvent;

/**
 * WebSocket event listener
 * @version 1.0 2025-01-10
 * @since 2025-01-10
 * @author Holmes Amzish
 */
@Component
@RequiredArgsConstructor
@Slf4j
public class WebSocketEventListener {

    private final SimpMessageSendingOperations messagingTemplate;
    private final OnlineUserTracker onlineUserTracker;

    @EventListener
    public void handleWebSocketDisconnectListener(SessionDisconnectEvent event) {
        // 获取断开连接的用户的用户名
        StompHeaderAccessor headerAccessor = StompHeaderAccessor.wrap(event.getMessage());
        String username = (String) headerAccessor.getSessionAttributes().get("username");
        if (username != null) {
            // 从在线用户列表中移除该用户
            onlineUserTracker.removeUser(username);
            // 广播更新后的在线用户数量
            broadcastOnlineUserCount();
        }
    }

    @EventListener
    public void handleWebSocketConnectListener(StompHeaderAccessor accessor) {
        // 获取新连接用户的用户名
        String username = (String) accessor.getSessionAttributes().get("username");
        if (username != null) {
            // 将用户添加到在线用户列表
            onlineUserTracker.addUser(username);
            // 广播更新后的在线用户数量
            broadcastOnlineUserCount();
        }
    }

    private void broadcastOnlineUserCount() {
        // 获取当前在线用户数量
        int count = onlineUserTracker.getOnlineUserCount();
        // 将在线用户数量广播到 /topic/onlineCount 主题
        messagingTemplate.convertAndSend("/topic/onlineCount", count);
    }
}
```

- **`handleWebSocketDisconnectListener`**：监听用户断开连接事件，从在线用户列表中移除该用户，并广播更新后的在线用户数量。
- **`handleWebSocketConnectListener`**：监听用户连接事件，将用户添加到在线用户列表，并广播更新后的在线用户数量。
- **`broadcastOnlineUserCount`**：将当前在线用户数量广播到 `/topic/onlineCount` 主题，所有订阅了该主题的客户端都会收到更新后的在线用户数量。

### 4.1.4 控制器

控制器负责处理客户端发送的消息，并将消息转发到指定的目的地。通过 `@MessageMapping` 注解，控制器可以处理特定目的地的消息，并通过 `@SendTo` 注解将消息发送到指定的主题。

消息控制器 `ChatController`

```java
package cn.arorms.chat.controller;

import cn.arorms.chat.model.ChatMessage;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessageHeaderAccessor;
import org.springframework.stereotype.Controller;

/**
 * Chat controller
 * @version 0.1 2025-01-08
 * @since 2025-01-08
 * @author Holmes Amzish
 */
@Controller
public class ChatController {

    @MessageMapping("/chat.sendMessage")
    @SendTo("/topic/public")
    public ChatMessage sendMessage(@Payload ChatMessage chatMessage) {
        // 处理普通聊天消息，并将其广播到 /topic/public 主题
        return chatMessage;
    }

    @MessageMapping("/chat.addUser")
    @SendTo("/topic/public")
    public ChatMessage addUser(@Payload ChatMessage chatMessage, SimpMessageHeaderAccessor headerAccessor) {
        // 将用户名存储在 WebSocket 会话属性中
        headerAccessor.getSessionAttributes().put("username", chatMessage.getSender());
        // 广播用户加入消息到 /topic/public 主题
        return chatMessage;
    }
}
```

- **`sendMessage`**：处理客户端发送的普通聊天消息，并将其广播到 `/topic/public` 主题。
- **`addUser`**：处理用户加入聊天室的请求，将用户名存储在 WebSocket 会话属性中，并广播用户加入消息到 `/topic/public` 主题。

通过控制器的设计，系统可以高效地处理客户端发送的消息，并将消息广播给所有在线用户。

---

## 4.2 用户验证

用户验证模块负责处理用户的登录请求，并验证用户提供的用户名和密码是否合法。该模块的设计包括数据库的配置、用户实体的定义、MyBatis 映射文件的编写、用户服务的实现以及登录控制器的开发。

### 4.2.1 数据库的设置

为了实现用户验证功能，系统需要与数据库进行交互。本系统使用 MariaDB 作为数据库，并通过 MyBatis 框架进行数据库操作。

数据库配置文件 `application.properties`

```properties
spring.datasource.url=jdbc:mariadb://localhost:3306/chat
spring.datasource.username=root
spring.datasource.password=password
spring.datasource.driver-class-name=org.mariadb.jdbc.Driver

mybatis.mapper-locations=classpath:mapper/*.xml
mybatis.type-aliases-package=cn.arorms.chat.model
```

- **`spring.datasource.url`**：指定数据库的连接 URL。
- **`spring.datasource.username`** 和 **`spring.datasource.password`**：指定数据库的用户名和密码。
- **`mybatis.mapper-locations`**：指定 MyBatis 映射文件的位置。
- **`mybatis.type-aliases-package`**：指定 MyBatis 实体类的包路径。

### 4.2.2 用户实体的定义

用户实体类 `User` 用于表示用户的基本信息，包括用户名、密码和电子邮件。

用户实体类 `User`

```java
package cn.arorms.chat.model;

import lombok.Data;

/**
 * User entity
 * @version 1.0 2025-01-10
 * @since 2025-01-10
 * @author Holmes Amzish
 */
@Data
public class User {
    private String username; // 用户名
    private String password; // 密码
    private String email;    // 电子邮件
}
```

- **`username`**：用户的唯一标识。
- **`password`**：用户的密码。
- **`email`**：用户的电子邮件地址。

### 4.2.3 映射类

MyBatis 映射文件用于定义 SQL 查询语句和结果映射。

MyBatis 映射文件 `UserMapper.xml`

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="cn.arorms.chat.mapper.UserMapper">
    <select id="validateUser" resultType="cn.arorms.chat.model.User">
        SELECT * FROM users WHERE username = #{username} AND password = #{password}
    </select>
</mapper>
```

- **`validateUser`**：根据用户名和密码查询用户信息。

MyBatis 映射接口 `UserMapper`

```java
package cn.arorms.chat.mapper;

import cn.arorms.chat.model.User;
import org.apache.ibatis.annotations.Mapper;

/**
 * User mapper
 * @version 1.0 2025-01-10
 * @since 2025-01-10
 * @author Holmes Amzish
 */
@Mapper
public interface UserMapper {
    User validateUser(String username, String password);
}
```

- **`validateUser`**：调用 MyBatis 映射文件中的 SQL 查询，验证用户提供的用户名和密码是否合法。

### 4.2.4 服务类

用户服务类 `UserService` 负责调用 MyBatis 映射接口，执行数据库查询操作。

用户服务类 `UserService`

```java
package cn.arorms.chat.service;

import cn.arorms.chat.mapper.UserMapper;
import cn.arorms.chat.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;

    public boolean validateUser(String username, String password) {
        // 调用 MyBatis 映射接口验证用户信息
        User user = userMapper.validateUser(username, password);
        return user != null;
    }
}
```

- **`validateUser`**：调用 `UserMapper` 接口的 `validateUser` 方法，验证用户提供的用户名和密码是否合法。

### 4.2.5 登录控制器

登录控制器 `AuthController` 负责处理客户端的登录请求，并调用用户服务进行验证。

登录控制器 `AuthController`

```java
package cn.arorms.chat.controller;

import cn.arorms.chat.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
public class AuthController {
    @Autowired
    private UserService userService;

    @PostMapping("/login")
    public boolean login(@RequestBody UserLoginRequest request) {
        // 调用用户服务验证用户信息
        return userService.validateUser(request.getUsername(), request.getPassword());
    }

    public static class UserLoginRequest {
        private String username;
        private String password;

        // Getters and setters
        public String getUsername() { return username; }
        public void setUsername(String username) { this.username = username; }
        public String getPassword() { return password; }
        public void setPassword(String password) { this.password = password; }
    }
}
```

- **`login`**：处理客户端的登录请求，调用 `UserService` 的 `validateUser` 方法进行用户验证，并返回验证结果。

通过用户验证模块的设计，系统可以确保只有合法用户才能进入聊天室，从而保障系统的安全性。

通过实时消息模块和用户验证模块的设计与实现，聊天室系统能够高效地处理用户的消息传递和登录验证。实时消息模块通过 WebSocket 和 STOMP 协议实现了消息的实时收发，而用户验证模块通过 MyBatis 和 Spring Boot 实现了用户的安全登录。这两个模块共同构成了聊天室系统的核心功能，为用户提供了稳定、安全的实时通信服务。

# 五、遇到问题及心得体会

在开发聊天室系统的过程中，我遇到了一些技术难题和挑战，同时也积累了许多宝贵的经验。以下是我在开发过程中遇到的主要问题以及解决这些问题的心得体会。

## 5.1 遇到的问题

### 5.1.1 SpringBoot 与其他框架冲突

之前在利用 Maven 配置依赖的时候，没有仔细检查依赖之间版本的兼容性。在编写的时候总是无法将数据库的映射注册成 Bean 对象。一开始一直在找定义的 Bean 是哪里写错了。最后发现是依赖之间版本有不兼容性，更改了 pom.xml 并刷新一下 Maven 才解决问题。

### 5.1.2 WebSocket 连接不稳定

在开发初期，我发现 WebSocket 连接在某些情况下会不稳定，尤其是在网络环境较差的情况下，客户端和服务端之间的连接可能会频繁断开。这导致用户在使用聊天室时经常遇到连接中断的问题。

为了解决这个问题，启用了 SockJS：为了解决 WebSocket 连接不稳定的问题，我引入了 SockJS 作为备选方案。SockJS 能够在浏览器不支持 WebSocket 时自动降级为其他协议（如 HTTP 长轮询），从而确保连接的稳定性。

## 5.2 心得体会

### 5.2.1 技术选型的重要性

在开发聊天室系统的过程中，我深刻体会到技术选型的重要性。选择合适的框架和协议（如 Spring Boot、WebSocket、STOMP）能够大大简化开发流程，提高系统的稳定性和可扩展性。例如，Spring Boot 提供了对 WebSocket 和 STOMP 协议的内置支持，使得开发者能够快速搭建实时通信系统。

### 5.2.2 模块化设计的优势

通过将系统划分为多个模块（如实时消息模块、用户验证模块、在线用户管理模块等），我能够更清晰地组织代码结构，降低系统的复杂性。模块化设计不仅提高了代码的可读性和可维护性，还使得系统更容易扩展和优化。

## 5.3 总结

通过开发聊天室系统，我不仅掌握了 WebSocket、STOMP、Spring Boot 等技术的应用，还积累了丰富的项目经验。在解决问题的过程中，我学会了如何分析问题、寻找解决方案，并将其应用到实际开发中。这些经验将对我未来的开发工作产生深远的影响。

# 六、附录

## 6.2 项目结构

```
├─src
│  ├─main
│  │  ├─java
│  │  │  └─cn
│  │  │      └─arorms
│  │  │          └─chat
│  │  │              │  RealTimeChatApplication.java
│  │  │              │
│  │  │              ├─config
│  │  │              │      WebSocketConfig.java
│  │  │              │      WebSocketEventListener.java
│  │  │              │
│  │  │              ├─controller
│  │  │              │      AuthController.java
│  │  │              │      ChatController.java
│  │  │              │      StatsController.java
│  │  │              │
│  │  │              ├─mapper
│  │  │              │      UserMapper.java
│  │  │              │
│  │  │              ├─model
│  │  │              │      ChatMessage.java
│  │  │              │      MessageType.java
│  │  │              │      User.java
│  │  │              │
│  │  │              └─service
│  │  │                      OnlineUserTracker.java
│  │  │                      UserService.java
│  │  │
│  │  └─resources
│  │      │  application.properties
│  │      │
│  │      ├─mapper
│  │      │      UserMapper.xml
│  │      │
│  │      ├─static
│  │      │  │  index.html
│  │      │  │
│  │      │  ├─css
│  │      │  │      main.css
│  │      │  │
│  │      │  └─js
│  │      │          main.js
│  │      │
│  │      └─templates
│  └─test
│      └─java
│          └─cn
│              └─arorms
│                  └─chat
│                          MapperTestRunner.java
│                          RealTimeChatApplicationTests.java
│
└─target
```



