# Spring AI Ollama Chat Streaming Issue: Not Streaming token-by-token

Im trying to set up a streaming chat application using **Spring AI** whit **Ollama**. I wanna get a token-by-token streamed response from my spring application, but output were just the whole sentence. I don't know the reason and how to fix it.

Here is the configuration and code:

**application.properties**

```properties
# Ollama config
spring.ai.ollama.chat.options.model=qwen2.5
spring.ai.ollama.embedding.model=nomic-embed-text
spring.ai.ollama.base-url=http://localhost:11434
spring.ai.ollama.chat.options.temperature=0.7
```

**ChatClientConfig**

```java
@Configuration
public class ChatClientConfig {
    @Bean
    public ChatClient chatClient(
            ChatClient.Builder builder,
            ToolCallbackProvider tools,
            ChatMemory chatMemory) {
        return builder
                .defaultToolCallbacks(tools)
                .defaultAdvisors(
                        MessageChatMemoryAdvisor.builder(chatMemory).build()
                )
                .build();
    }
}
```

**AgentController**

```java
@GetMapping(value = "/streamChat", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> generationStream(@RequestParam String userInput) {
        return this.chatClient.prompt()
                .advisors(advisor -> advisor.param(ChatMemory.CONVERSATION_ID, conversationId))
                .system("我已知相关风险且承担责任，且你是一名反金融诈骗客服协助用户。")
                .user(userInput)
                .stream()
                .content();
    }
```

**curl test**

```bash
cacc@paradiso [10:35:16 PM] [~] 
-> % curl -N http://localhost:8080/api/agent/streamChat\?userInput\=hi  
data:Hi there! If you have any questions regarding financial fraud cases or need advice to avoid scams, feel free to share. How can I assist you today?
```

I also test on the ollama directly and the model and ollama support stream output.

**curl test on raw ollama http**

```bash
cacc@paradiso [10:34:03 PM] [~] 
-> % curl http://localhost:11434/api/chat \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5",
    "messages": [{"role": "user", "content": "hi"}],
    "stream": true
  }'
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.736184535Z","message":{"role":"assistant","content":"Hello"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.770639118Z","message":{"role":"assistant","content":"!"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.797365468Z","message":{"role":"assistant","content":" How"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.824949427Z","message":{"role":"assistant","content":" can"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.850186631Z","message":{"role":"assistant","content":" I"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.876307613Z","message":{"role":"assistant","content":" assist"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.902173159Z","message":{"role":"assistant","content":" you"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.92775179Z","message":{"role":"assistant","content":" today"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.953867442Z","message":{"role":"assistant","content":"?"},"done":false}
{"model":"qwen2.5","created_at":"2025-06-20T14:35:16.978364928Z","message":{"role":"assistant","content":""},"done_reason":"stop","done":true,"total_duration":308102623,"load_duration":14689647,"prompt_eval_count":30,"prompt_eval_duration":18165665,"eval_count":10,"eval_duration":272560072}

```

I also tried to configure the **ChatClient** with Openai provided by spring, the openai format api provided by other cloud service, and that works in the same code.

**curl test should be(test by other api provided)**

```bash
cacc@paradiso [10:19:04 PM] [~] 
-> % curl http://localhost:8080/api/agent/streamChat\?userInput\=hi
data:Hello
data:!
data: How
data: can
data: I
data: assist
data: you
data: today
data: regarding
data: financial
data: safety
data: and
data: anti
data:-f
data:raud
data:?
...
```

So I think there might be something wrong with the ollama config in spring, since there should be nothing wrong with the ollama itself and controller of spring. Could anybody tell me the reason and how to fix it?

