---
title: Spring AI Model Context protocol
date: 2025-04-28
---

# Overview

The Model Context Protocol (MCP) is a standardized protocol that enbales AI models to interact with external tools and resources in a structured way. It supports multiple transport mechanisms to provide flexibility across different environments.

Spring AI MCP extends the MCP Java SDK with Spring Boot integration, providing both client and server starters. Bootstrap your AI applications with MCP support using Spring Initializer.

## MCP Java SDK Architecture

The Java MCP implementation follows a three-layer architecture

- Client/Server Layer: The McpClient handles client-side operations while the McpServer manages server-side protocol operations. Both utilize McpSession for communication management.
- Session Layer (McpSession): Manages communication patterns and state through the DefaultMcpSession implementation.
- Transport Layer (McpTransport): Handles JSON-RPC message serialization and deserialization with support for multiple transport implementations.

<img src="https://docs.spring.io/spring-ai/reference/_images/mcp/mcp-stack.svg" width=40%>

# MCP Client Boot Starter

The Spring AI MCP Client Boot Starter provides auto-configuration for MCP client functionality in Spring Boot applications. It supports both synchronous and asynchronous client implementations with various transport options.

## Starters

### Standard MCP client

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-client</artifactId>
</dependency>
```

The standard starter connects simulaneously to one or more MCP servers over `STDIO` (in-process) and/or `SSE` (remote) transports. The SSE connection uses the HttpClient-based transport implementation. Each connection to an MCP server creates a new MCP client instance. You can choose either SYNC or ASYNC MCP clients. For production deployment, we recommend using the WebFlux-based SSE connection with the `spring-ai-starter-mcp-client-webflux`.

### WebFlux Client

The WebFlux starter provides similar functionality to the standard starter but uses a WebFlux-based SSE transport implementation.

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-client-webflux</artifactId>
</dependency>
```

## Configuration Properties

### Common Properties

The common properties are prefixed with `spring.ai.mcp.client`:

| Property             | Description                                                  | Default Value        |
| -------------------- | ------------------------------------------------------------ | -------------------- |
| enabled              | Enable/disable the MCP client                                | true                 |
| name                 | Name of the MCP client instance                              | spring-ai-mcp-client |
| toolcallback.enabled | Enable/disable the MCP tool callback integration with Spring AI's tool excution framework | false                |

### Stdio Transport Poperties

Properties for Standard I/O transport are prefixed with `spring.ai.mcp.client.stdio`:

| Property                | Description                                                  | Default Value |
| :---------------------- | :----------------------------------------------------------- | :------------ |
| `servers-configuration` | Resource containing the MCP servers configuration in JSON format | -             |
| `connections`           | Map of named stdio connection configurations                 | -             |

Example configuration:

```properties
spring.ai.mcp.client.stdio.connections.ujs-mcp.command=uv
spring.ai.mcp.client.stdio.connections.ujs-mcp.args=--directory,/home/cacc/Repositories/ujs-mcp-server,run,bill_query.py
```

You can configure stdio connections using an external JSON file using the Claude Desktop format:

```properties
spring.ai.mcp.client.stdio.servers-configuration=classpath:mcp-servers.json
```

The Claude Desktop format looks like this:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Desktop",
        "/Users/username/Downloads"
      ]
    }
  }
}
```

Currently, the Claude Desktop format supports only STDIO connection types.

```java
/*
 * Copyright 2025-2025 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.springframework.ai.mcp.samples.brave;

import java.util.List;

import io.modelcontextprotocol.client.McpSyncClient;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.mcp.SyncMcpToolCallbackProvider;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}	

	@Bean
	public CommandLineRunner predefinedQuestions(ChatClient.Builder chatClientBuilder, List<McpSyncClient> mcpSyncClients,
			ConfigurableApplicationContext context) {

		return args -> {

			var chatClient = chatClientBuilder
					.defaultTools(new SyncMcpToolCallbackProvider(mcpSyncClients))
					.build();

			String question = "Does Spring AI support the Model Context Protocol? Please provide some references.";

			System.out.println("QUESTION: " + question);
			System.out.println("ASSISTANT: " + chatClient.prompt(question).call().content());

			context.close();
		};
	}
}
```



### SSE Transport Properties

Properties for Server-Sent Events (SSE) transport are prefixed with `spring.ai.client.sse`:

| Property                 | Description                                            |
| :----------------------- | :----------------------------------------------------- |
| `connections`            | Map of named SSE connection configurations             |
| `connections.[name].url` | URL endpoint for SSE communication with the MCP server |

Example configuration:

```properties
spring.ai.mcp.client.sse.connections.server1.url=http://localhost:8080
spring.ai.mcp.client.sse.connections.server2.url=http://otherserver:8081
```

## Features

### Sync/Async Client Types

The starter supports two types of clients:

- SYnchronous - default client type, suitable for traditional request-response patterns with blocking operations
- Asynchronous - suitable for reactive applications with non-blocking operations, configured using `spring.ai.mcp.client.type=ASYNC`

### Client Customization

The auto-configuration provides extensive client spec customization capabilities through callback interfaces. These customizers allow you to configure various aspects of the MCP client behavior, from request timeouts to event handling and message processing.

# MCP Utilities

The MCP utilities provide foundational support for integrating Model Context Protocal with Spring AI applications. These utilities enbale seamless communication between Spring AI's tool system and MCP servers, supporting both synchronous and asynchronous operations. They are typically used for programmatic MCP Client and Server configuration and interaction. For a more streamlined configuration, consider using the boot startes.

## ToolCallback Utility

### Tool Callback Adapter

Adapts MCP tools to Spring AI's tool interface with both synchronous and asynchronous execution support.

```java
McpSyncClient mcpClient = // obtain MCP client
Tool mcpTool = // obtain MCP tool definition
ToolCallback callback = new SyncMcpToolCallback(mcpClient, mcpTool);

// Use the tool through Spring AI's interfaces
ToolDefinition definition = callback.getToolDefinition();
String result = callback.call("{\"param\": \"value\"}");
```

## McpToolUtils

### ToolCallbacks to ToolSpecifications

Converting Spring AI tool callbacks to MCP tool specifications:

```java
List<ToolCallback> toolCallbacks = // obtain tool callbacks
List<SyncToolSpecifications> syncToolSpecs = McpToolUtils.toSyncToolSpecifications(toolCallbacks);
```

