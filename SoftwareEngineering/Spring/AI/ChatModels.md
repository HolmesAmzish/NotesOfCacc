---
title: Spring AI API
date: 2025-04-28
---

# Overview

## Introduction

The Spring AI API covers a wide range of functionalities. Each major feature is detailed in its own dedicated section. To provide an overview, the following key functionalities are available.

## AI Model API

Portable Model API across AI providers for Chat, Text to Image, Audio Transcripyion, Text to Speech, and Embedding models. Both synchronous and stream API options are supported. Dropping down to access model specific features is also supported.

<img src="https://docs.spring.io/spring-ai/reference/_images/model-hierarchy.jpg">

With support for AI Models from OpenAI, Microsoft, Amazon, Google, Amazon Bedrock, Hugging Face and more.

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-chat-completions-clients.jpg">

## Vector Store API

Portable Vector Store API across multiple providers, including a novel SQL - like metadata filter API that is also portable. SUpport for 14 vector databases are available.

## Tool Calling API

Spring AI makes it easy to have the AI model invoke your services as `@Tool` - annotated methods or POJO `java.util.Function` objects.

<img src="https://docs.spring.io/spring-ai/reference/_images/tools/tool-calling-01.jpg" width=80%>

## Auto Configuration

Spring Boot Auto Configuration and Starters for AI Models and Vector Stores.

## ETL Data Engineering

ET framework for Data Engineering. This provides the basis of loading data into a vector daatabase, helping implement the Retrieval Augmented Generation pattern that enbales you to bring your daata to the AI modeel to incorporate into its response.

<img src="https://docs.spring.io/spring-ai/reference/_images/etl-pipeline.jpg">

# Chat Model API

The Spring AI Chat Model API is designed to be a simple and portable interface for interacting with various AI Models, allowing developers to switch between different models with minimal code changes. This design aligns with Spring's philosophy of modularity and interchangeabillity.

Also with the help of companion classes like `Prompt` for input encapsulation and `ChatREsponse` for output handling, the Chat Model API unifies the communication with AI Models. It manages the complexity of request preparation and response parsing, offerting a direct and simplified API interaction.

## API Overview

### ChatModel

ChatModel interface definition
```java
public interface ChatModel extends Model<Prompt, ChatResponse> {
    default String call(String message) {...}
    
    @Override
    ChatResponse call(Prompt prompt);
}
```

### StreamingChatModel

StreamingChatModel interface definition

```java
public interface StreamingChatModel extends StreamingModel<Prompt, ChatResponse> {
    default Flux<String> strea,(String message) {...}
    
    @Override
    Flux<ChatResponse> stream(Prompt prompt);
}
```

The `streaam()` method taakes a `String` or `Prompt` parameter similar to `ChatModel` but is streams the responses using the reactive Flux API.

### Prompt

The Prompt is a `ModelRequest` that encapsulates a list of Message objects and optional model request options. The following listing shows aa truncated version of the Prompt class, excluding constructors and other utility methods.

```java
public class Prompt implements ModelRequest<List<Message>> {
    private final List<Message> messaages;
    
    private ChatOptions modelOptions;
    
    @Override
    public ChatOPtions getOptions() {...}
    
    @Override
    public List<Message> getInstructions() {...}
    
    // constructors and utility methods omitted
}
```

### Message

The `Message` interface encapsulates a Prompt textual content, a collection of metadaataa attributes, aand a categorization known as `MessageType`. The interface is defined as follows:

```java
public interface Content {
    String getText();
    Map<String, Object> getMetadata();
}

public interface Message extends Content {
    MessageType getMessageType();
}
```

The multimodal message types implement also the `MediaContent` interface providing a list of `Media` content objects.

```java
public interface MediaCOntent extends Content {
    Collection<Media> getMedia();
}
```

The `Message` interface has various implementations that correspond to the categories of messages that an AI model can process:

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-message-api.jpg" width=100%>

### Chat Options

Represents the options that can be passed to the AI model. The `ChatOPtions` cllass is a subclass of `ModedlOptions` and is used to define few portable options that can be passed to the AI model. The `ChatOptions` class is ddefined as follows:

```java
public interface ChatOptions extends ModelOptions {
    String getModel();
    Float getFrequencyPenalty();
    Integer getMaxTOkens();
    Float getPresencePenalty();
    List<String> getStopSequences();
    Float getTemperature();
    Integer getTopK();
    Float getTopP();
    ChatPotions copy();
}
```

<img src="https://docs.spring.io/spring-ai/reference/_images/chat-options-flow.jpg">

### ChatResponse

The structure of the `ChatResponse` class is as follows:

```java
public class ChatResponse implements ModelResponse<Generation> {

    private final ChatResponseMetadata chatResponseMetadata;
	private final List<Generation> generations;

	@Override
	public ChatResponseMetadata getMetadata() {...}

    @Override
	public List<Generation> getResults() {...}

    // other methods omitted
}
```

The `ChatResponse` class holds the AI Model's output, with each `Generation` instance containing one of potentially multiple outputs resulting from a single prompt.

## Chat Models Comparison

https://docs.spring.io/spring-ai/reference/api/chat/comparison.html



# DeepSeek Chat

DeepSeek AI providees the open-source DeepSeek V3 model, renowned for its cutting-edge reasoning and problem-solving capabilities.

Spring AI integrates with DeepSeek AI by reusing the existing OpenAI client. To get started, you'll need to obtain a DeepSeek API Key, configure the base URL, and select one of the supported models.

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-deepseek-integration.jpg" width=100%>

## Auto-configuration

Example environment variables configuration:

```shell
export SPRING_AI_OPENAI_API_KEY=<INSERT DEEPSEEK API KEY HERE>
export SPRING_AI_OPENAI_BASE_URL=https://api.deepseek.com
export SPRING_AI_OPENAI_CHAT_MODEL=deepseek-chat
```

Maven dependency

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-model-openai</artifactId>
</dependency>
```

## Chat Properties

### Connection Properties

The prefix `spring.ai.openai` is used as the property prefix that lets you connect to OpenAI

| Property                  | Description                       | Default |
| ------------------------- | --------------------------------- | ------- |
| spring.ai.openai.base-url | Must be set to `api.deepseek.com` | -       |
| spring.ai.openai.api-key  | DeepSeek API Key                  | -       |

### Configuration Properties

The prefix `spring.ai.openai.chat` is the property prefix that lets you configure the chat model implementation for OpenAI.

| Property                       | Description                                      | Default |
| ------------------------------ | ------------------------------------------------ | ------- |
| spring.ai.model.chat           | Enable OpenAI chat model                         | openai  |
| spring.ai.openai.chat.base-url | Optional overrides the spring.ai.openai.base-url | -       |

## Runtime Options

The `OpenAiChatOptions.java` provides model configurations, such as the model to use, the temperature, the frequency penalty, etc.

On start-up, the default options can be configured with the `OpenAiChatModel(api, options)` constructor or the `spring.ai.openai.chat.options.*` properties.

At run-time you can override the default options by adding new, request specific, options to the Prompt call. For example to override the default model and temperature for a specific request:

```java
ChatResponse response = chatModel.call(
	new Prompt(
    	"Generate the names of 5 faamous pirates.",
        OpenAiChatOptions.builder()
        	.model("deepseek-chat")
        	.temperature(0.4)
        .build()
    )
);
```

## Sample Controller

[Create](https://start.spring.io/) a new Spring Boot project and add the `spring-ai-starter-model-openai` to your pom (or gradle) dependencies.

Add a `application.properties` file, under the `src/main/resources` directory, to enable and configure the OpenAi chat model:

```properties
spring.ai.openai.api-key=<DEEPSEEK_API_KEY>
spring.ai.openai.base-url=https://api.deepseek.com
spring.ai.openai.chat.options.model=deepseek-chat
spring.ai.openai.chat.options.temperature=0.7

# The DeepSeek API doesn't support embeddings, so we need to disable it.
spring.ai.openai.embedding.enabled=false
```

This will create a `OpenAiChatModel` implementation that you can inject into your class. Here is an example of a simple `@Controller` class that uses the chat model for text generations.

```java
@RestController
public class ChatController {

    private final OpenAiChatModel chatModel;

    @Autowired
    public ChatController(OpenAiChatModel chatModel) {
        this.chatModel = chatModel;
    }

    @GetMapping("/ai/generate")
    public Map generate(@RequestParam(value = "message", defaultValue = "Tell me a joke") String message) {
        return Map.of("generation", this.chatModel.call(message));
    }

    @GetMapping("/ai/generateStream")
    public Flux<ChatResponse> generateStream(@RequestParam(value = "message", defaultValue = "Tell me a joke") String message) {
        Prompt prompt = new Prompt(new UserMessage(message));
        return this.chatModel.stream(prompt);
    }
}
```



# Ollama Chat

You can pull the models you want to use in your application from the Ollama model library

```bash
ollama pull <model-name>
```

You can also pull any of the thousands, free, GGUF Hugging Face Models:

```bash
ollama pull hf.co/<username>/<model-repository>
```

Alternatively, you can enable the option to download automatically any needed model: Auto-pulling Models.

## Auto-configuration

```xml
<dependency>
   <groupId>org.springframework.ai</groupId>
   <artifactId>spring-ai-starter-model-ollama</artifactId>
</dependency>
```

### Base Properties

The prefix `spring.ai.ollama` is the property prefix to configure the connection to Ollama.

| Property                  | Description                                  | Default           |
| ------------------------- | -------------------------------------------- | ----------------- |
| spring.ai.ollama.base-url | Base URL where Ollama API server is running. | `localhost:11434` |

## Runtime Options



## Sample Controller

```properties
spring.ai.ollama.base-url=http://localhost:11434
spring.ai.ollama.chat.options.model=gemma3:1b
spring.ai.ollama.chat.options.temperature=0.7
```

This will create an `OllamaChatModel` implementation that you can inject into your classes. Here is an example of a simple `@RestController` class that uses the chat model for text generations.

```java
@RestController
public class ChatController {

    private final OllamaChatModel chatModel;

    @Autowired
    public ChatController(OllamaChatModel chatModel) {
        this.chatModel = chatModel;
    }

    @GetMapping("/ai/generate")
    public Map<String,String> generate(@RequestParam(value = "message", defaultValue = "Tell me a joke") String message) {
        return Map.of("generation", this.chatModel.call(message));
    }

    @GetMapping("/ai/generateStream")
	public Flux<ChatResponse> generateStream(@RequestParam(value = "message", defaultValue = "Tell me a joke") String message) {
        Prompt prompt = new Prompt(new UserMessage(message));
        return this.chatModel.stream(prompt);
    }

}
```



## Manual Configuration

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-ollama</artifactId>
</dependency>
```

Next, create an `OllamaChatModel` instance and use it to send requests for text generation:

```java
var ollamaApi = new OllamaApi();

var chatModel = OllamaChatModel.builder()
                    .ollamaApi(ollamaApi)
                    .defaultOptions(
                        OllamaOptions.builder()
                            .model(OllamaModel.MISTRAL)
                            .temperature(0.9)
                            .build())
                    .build();

ChatResponse response = this.chatModel.call(
    new Prompt("Generate the names of 5 famous pirates."));

// Or with streaming responses
Flux<ChatResponse> response = this.chatModel.stream(
    new Prompt("Generate the names of 5 famous pirates."));
```

