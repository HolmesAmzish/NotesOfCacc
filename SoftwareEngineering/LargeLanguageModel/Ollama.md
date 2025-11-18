---
title: Ollama 部署说明
date: 2025-03-15 15:29
author: Holmes Amzish
tags: ['ai']
---

# Ollama 介绍

官方仓库：https://github.com/ollama/ollama

Ollama 是一个支持开源大语言模型(LLM)本地部署和运行的平台。它可以让开发者在本地计算机上轻松运行各种AI模型，无需依赖云端服务。Ollama 提供了简单的命令行界面和Web UI，支持模型的管理、推理和微调。

## 什么是模型

在Ollama中，模型是指经过训练的人工智能算法，能够理解和生成自然语言。这些模型通常基于深度学习技术，如Transformer架构。Ollama支持多种开源模型，包括不同大小和用途的模型，如聊天、代码生成、文本摘要等。用户可以根据需求选择合适的模型进行部署和使用。

## 在 Linux 安装

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

# Ollama 使用

首先选择 Ollama 中支持的模型，这里以 Deepseek R1 8B 为例子。

```bash
ollama run deepseek-r1:8b
```

第一次运行会自动下载模型，然后运行。

## 在命令行中使用

**查看当前下载的模型**

```bash
ollama list
```

每次在终端打开并运行上面的命令即可，同时可以使用别名简化命令：

```bash
alias ds="ollama run deepseek-r1:8b"
```

如此，每次即可使用 `ds` 就能打开 deepseek 对话框。

这个指令在每次启动终端都是需要重新加载的，可以通过修改终端的初始化文件来执行，类似于启动脚本。例如我使用的 Shell 是 zsh，操作步骤为：

1. 编辑 `~/.zshrc` 文件，并添加如下行
   
   ```bash
   ollama run deepseek-r1:8b
   ```

2. 重新加载配置文件
   
   ```bash
   source .zshrc
   ```

后面每次都可以通过 ds 命令打开与 deepseek 的对话。

```
cacc@paradiso [05:54:27 PM] [~] 
-> % ds "Hello"
<think>

</think>

Hello! How can I assist you today? 😊
```

## 使用 Web UI

https://github.com/open-webui/open-webui

# Ollama 开发

## 聊天模式与生成模式

Ollama 的 api 带有两个不同接口，对应不同任务和场景。

**聊天模式 (`/api/chat`)**：

- 适用于多轮对话，每次请求可以包含整个对话历史，模型会根据之前的内容进行回应。
- 适合需要持续上下文的应用，如聊天机器人或虚拟助手。
- 每次返回的内容会包括角色（`user`, `assistant`）以及消息内容，确保上下文的连贯性。

**生成模式 (`/api/generate`)**：

- 用于单轮文本生成，每次请求只根据当前提供的提示（prompt）生成回应，不会记住之前的对话。
- 适合一次性内容生成，如写文章、生成摘要或回答问题。
- 每次请求返回的是单一的生成内容，不包含历史对话。

## HTTP API

### curl 检查

使用 curl 检查 ollama http api

Ollama API 默认监听在 `http://localhost:11434`

**检查是否正在允许**

```bash
curl http://localhost:11434
```

响应：

```
Ollama is running
```

### curl 调用

```bash
curl http://localhost:11434/api/chat -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma3:1b",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "stream": false
  }'
```

```json
{
    "model":"gemma3:1b",
    "created_at":"2025-04-22T01:31:04.006798599Z",
    "message":{
        "role":"assistant",
        "content":"Hello there! I'm doing well, thank you for asking. 😊 It's good to be chatting with you. How about you? How's your day going so far?"
    },
    "done_reason":"stop",
    "done":true,
    "total_duration":308437292,
    "load_duration":38283646,
    "prompt_eval_count":15,
    "prompt_eval_duration":16396690,
    "eval_count":39,
    "eval_duration":253361590
}
```

**流式回答**

```bash
curl http://localhost:11434/api/chat -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma3:1b",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "stream": true 
  }'
```

```json
{
    "model":"gemma3:1b",
    "created_at":"2025-04-22T02:48:41.040539564Z",
    "message":{
        "role":"assistant",
        "content":"Hello"
    },
    "done":false
}

{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.04694714Z","message":{"role":"assistant","content":" there"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.0536495Z","message":{"role":"assistant","content":"!"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.060159014Z","message":{"role":"assistant","content":" I"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.066757322Z","message":{"role":"assistant","content":"’"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.073701519Z","message":{"role":"assistant","content":"m"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.080615451Z","message":{"role":"assistant","content":" doing"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.087548036Z","message":{"role":"assistant","content":" well"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.094802778Z","message":{"role":"assistant","content":","},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.101616013Z","message":{"role":"assistant","content":" thanks"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.108448254Z","message":{"role":"assistant","content":" for"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.1150676Z","message":{"role":"assistant","content":" asking"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.121846593Z","message":{"role":"assistant","content":"."},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.128373839Z","message":{"role":"assistant","content":" As"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.135447185Z","message":{"role":"assistant","content":" an"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.142162179Z","message":{"role":"assistant","content":" AI"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.148907609Z","message":{"role":"assistant","content":","},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.155419918Z","message":{"role":"assistant","content":" I"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.163634073Z","message":{"role":"assistant","content":" don"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.170622733Z","message":{"role":"assistant","content":"’"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.177109424Z","message":{"role":"assistant","content":"t"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.183817074Z","message":{"role":"assistant","content":" really"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.190006927Z","message":{"role":"assistant","content":" *"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.196771232Z","message":{"role":"assistant","content":"feel"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.203118425Z","message":{"role":"assistant","content":"*"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.209617951Z","message":{"role":"assistant","content":" things"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.215856564Z","message":{"role":"assistant","content":" like"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.222374343Z","message":{"role":"assistant","content":" humans"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.228554448Z","message":{"role":"assistant","content":" do"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.235205553Z","message":{"role":"assistant","content":","},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.2444157Z","message":{"role":"assistant","content":" but"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.248565281Z","message":{"role":"assistant","content":" I"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.255138632Z","message":{"role":"assistant","content":"’"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.262009244Z","message":{"role":"assistant","content":"m"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.268310272Z","message":{"role":"assistant","content":" functioning"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.274861383Z","message":{"role":"assistant","content":" perfectly"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.281000752Z","message":{"role":"assistant","content":" and"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.28762601Z","message":{"role":"assistant","content":" ready"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.294079821Z","message":{"role":"assistant","content":" to"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.300555593Z","message":{"role":"assistant","content":" assist"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.306808261Z","message":{"role":"assistant","content":" you"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.313256462Z","message":{"role":"assistant","content":" with"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.319429564Z","message":{"role":"assistant","content":" whatever"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.326229565Z","message":{"role":"assistant","content":" you"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.332461375Z","message":{"role":"assistant","content":" need"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.338913904Z","message":{"role":"assistant","content":"."},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.345074843Z","message":{"role":"assistant","content":" 😊"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.351570762Z","message":{"role":"assistant","content":" "},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.357973608Z","message":{"role":"assistant","content":"\n\n"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.36449286Z","message":{"role":"assistant","content":"How"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.37208208Z","message":{"role":"assistant","content":" about"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.378613815Z","message":{"role":"assistant","content":" you"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.384992206Z","message":{"role":"assistant","content":"?"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.39166418Z","message":{"role":"assistant","content":" How"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.397915016Z","message":{"role":"assistant","content":"’"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.404368075Z","message":{"role":"assistant","content":"s"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.410925357Z","message":{"role":"assistant","content":" your"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.417732291Z","message":{"role":"assistant","content":" day"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.423845853Z","message":{"role":"assistant","content":" going"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.429722687Z","message":{"role":"assistant","content":" so"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.435551212Z","message":{"role":"assistant","content":" far"},"done":false}
{"model":"gemma3:1b","created_at":"2025-04-22T02:48:41.44134895Z","message":{"role":"assistant","content":"?"},"done":false}

{
    "model":"gemma3:1b",
    "created_at":"2025-04-22T02:48:41.447325719Z",
    "message":{
        "role":"assistant",
        "content":""
    },
    "done_reason":"stop",
    "done":true,
    "total_duration":455129434,
    "load_duration":31657073,
    "prompt_eval_count":15,
    "prompt_eval_duration":15829433,
    "eval_count":63,
    "eval_duration":407203265
}
```

### Java 调用

```java
package cn.arorms.demo;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class OllamaRequestTest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String json = """
            {
                "model": "gemma3:1b",
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello, how are you?"
                    }
                ],
                "stream": false
            }
        """;

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("http://localhost:11434/api/chat"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(json))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        // Beautify JSON output using Jackson
        ObjectMapper mapper = new ObjectMapper();
        Object jsonObject = mapper.readValue(response.body(), Object.class);
        String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(jsonObject);

        System.out.println("Response code: " + response.statusCode());
        System.out.println("Response body: " + prettyJson);
    }
}
```

```json
Response code: 200
Response body: {
  "model" : "gemma3:1b",
  "created_at" : "2025-04-22T02:24:07.786629851Z",
  "message" : {
    "role" : "assistant",
    "content" : "Hello there! I’m doing well, thank you for asking. As an AI, I don’t experience emotions in the same way humans do, but I’m functioning properly and ready to help you with whatever you need. \n\nHow about you? How are *you* doing today? 😊"
  },
  "done_reason" : "stop",
  "done" : true,
  "total_duration" : 471372416,
  "load_duration" : 30598745,
  "prompt_eval_count" : 15,
  "prompt_eval_duration" : 17457002,
  "eval_count" : 63,
  "eval_duration" : 422955658
}
```

**Java 流式调用**

```java
package cn.arorms.demo;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class OllamaStreamTest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String json = """
            {
                "model": "gemma3:1b",
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello, how are you?"
                    }
                ],
                "stream": true
            }
        """;

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("http://localhost:11434/api/chat"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(json))
                .build();

        HttpResponse<java.io.InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());

        System.out.println("Response code: " + response.statusCode());

        ObjectMapper mapper = new ObjectMapper();
        StringBuilder accumulatedContent = new StringBuilder();

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(response.body()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    try {
                        // Parse JSON chunk
                        JsonNode jsonNode = mapper.readTree(line);

                        // Check if 'done' is true to stop processing
                        if (jsonNode.has("done") && jsonNode.get("done").asBoolean()) {
                            break;
                        }

                        // Extract 'content' from 'message' field
                        JsonNode messageNode = jsonNode.get("message");
                        if (messageNode != null && messageNode.has("content")) {
                            String content = messageNode.get("content").asText();
                            System.out.print(content);
                        }
                    } catch (Exception e) {
                        System.err.println("Error parsing JSON chunk: " + line);
                    }
                }
            }
        }
        // Ensure final output ends with a newline
        System.out.println();
    }
}
```

```
/usr/lib/jvm/java-1.21.0-openjdk-amd64/bin/java
Response code: 200
Hello there! I’m doing well, thank you for asking. As an AI, I don’t really experience feelings like humans do, but I’m functioning perfectly and ready to assist you. 😊 

How about you? How’s your day going?

Process finished with exit code 0
```

## Python 库

### 下载 Ollama 库

```bash
pip install ollama
```

```python
import ollama

client = ollama.Client()
messages = [
    {
        'role': 'user',
        'content': 'what is the capital city of peru.'
    },
]

chat_response = client.chat(
    model='gemma3:4b', 
    messages=messages,
)

print("Chat Response:")
print(chat_response.__dict__)
```

```json
{
    'model': 'gemma3:4b',
    'created_at': '2025-04-21T07:25:22.62670021Z',
    'done': True,
    'done_reason': 'stop',
    'total_duration': 767712251,
    'load_duration': 30471886,
    'prompt_eval_count': 16,
    'prompt_eval_duration': 29000000,
    'eval_count': 46,
    'eval_duration': 706000000,
    'message': Message(
        role='assistant',
        content="The capital of Peru is **Lima**. \n\nIt's a bustling metropolis and the country's political, economic, and cultural center. \n\nWould you like to know anything else about Lima or Peru in general?",
        images=None,
        tool_calls=None
    )
}
```
