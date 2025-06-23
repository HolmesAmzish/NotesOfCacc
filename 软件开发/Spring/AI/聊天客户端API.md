# 聊天客户端 API

这`ChatClient`提供用于与 AI 模型通信的 Fluent API。 它支持同步和流式编程模型。

|      | 请参阅本文档底部的[实现说明](https://www.spring-doc.cn/spring-ai/1.0.0/api_chatclient.html#_implementation_notes)，该说明与命令式和响应式编程模型的组合使用相关。`ChatClient` |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

Fluent API 具有构建 [Prompt](https://www.spring-doc.cn/spring-ai/1.0.0/api_prompt.html#_prompt) 的组成部分的方法，这些部分作为输入传递给 AI 模型。 这`Prompt`包含指导 AI 模型的输出和行为的说明文本。从 API 的角度来看，提示由一组消息组成。

AI 模型处理两种主要类型的消息：用户消息（来自用户的直接输入）和系统消息（由系统生成以指导对话）。

这些消息通常包含占位符，这些占位符在运行时根据用户输入进行替换，以自定义 AI 模型对用户输入的响应。

还有一些可以指定的 Prompt 选项，例如要使用的 AI 模型的名称以及控制生成输出的随机性或创造性的温度设置。

## 创建 ChatClient

这`ChatClient`是使用`ChatClient.Builder`对象。 您可以获取自动配置的`ChatClient.Builder`[实例，](https://www.spring-doc.cn/spring-ai/1.0.0/api_chatmodel.html)或者以编程方式创建一个。

### 使用自动配置的 ChatClient.Builder

在最简单的用例中， Spring AI 提供 Spring Boot 自动配置，创建一个原型`ChatClient.Builder`bean 中，以便注入到你的类中。 下面是一个检索`String`对简单用户请求的响应。

```java
@RestController
class MyController {

    private final ChatClient chatClient;

    public MyController(ChatClient.Builder chatClientBuilder) {
        this.chatClient = chatClientBuilder.build();
    }

    @GetMapping("/ai")
    String generation(String userInput) {
        return this.chatClient.prompt()
            .user(userInput)
            .call()
            .content();
    }
}
```

在这个简单的示例中，用户输入设置用户消息的内容。 这`call()`method 向 AI 模型发送请求，并且`content()`方法将 AI 模型的响应作为`String`.

### 使用多个聊天模型

在以下几种情况下，您可能需要在单个应用程序中使用多个聊天模型：

- 对不同类型的任务使用不同的模型（例如，用于复杂推理的强大模型和用于简单任务的更快、更便宜的模型）
- 当一个模型服务不可用时实现回退机制
- A/B 测试不同的型号或配置
- 为用户提供基于其偏好的模型选择
- 组合专用模型（一个用于代码生成，另一个用于创意内容等）

默认情况下，Spring AI 会自动配置单个`ChatClient.Builder`豆。但是，您可能需要在应用程序中使用多个聊天模型。以下是处理此情况的方法：

在所有情况下，您都需要禁用`ChatClient.Builder`autoconfiguration 通过设置属性`spring.ai.chat.client.enabled=false`.

这允许您创建多个`ChatClient`实例。

#### 具有单个模型类型的多个 ChatClient

本节介绍了一个常见的使用案例，您需要创建多个 ChatClient 实例，这些实例都使用相同的底层模型类型，但具有不同的配置。

```java
// Create ChatClient instances programmatically
ChatModel myChatModel = ... // already autoconfigured by Spring Boot
ChatClient chatClient = ChatClient.create(myChatModel);

// Or use the builder for more control
ChatClient.Builder builder = ChatClient.builder(myChatModel);
ChatClient customChatClient = builder
    .defaultSystemPrompt("You are a helpful assistant.")
    .build();
```

#### 不同模型类型的 ChatClients

使用多个 AI 模型时，您可以定义单独的`ChatClient`每个模型的 bean：

```java
import org.springframework.ai.chat.ChatClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ChatClientConfig {

    @Bean
    public ChatClient openAiChatClient(OpenAiChatModel chatModel) {
        return ChatClient.create(chatModel);
    }

    @Bean
    public ChatClient anthropicChatClient(AnthropicChatModel chatModel) {
        return ChatClient.create(chatModel);
    }
}
```

然后，您可以使用`@Qualifier`注解：

```java
@Configuration
public class ChatClientExample {

    @Bean
    CommandLineRunner cli(
            @Qualifier("openAiChatClient") ChatClient openAiChatClient,
            @Qualifier("anthropicChatClient") ChatClient anthropicChatClient) {

        return args -> {
            var scanner = new Scanner(System.in);
            ChatClient chat;

            // Model selection
            System.out.println("\nSelect your AI model:");
            System.out.println("1. OpenAI");
            System.out.println("2. Anthropic");
            System.out.print("Enter your choice (1 or 2): ");

            String choice = scanner.nextLine().trim();

            if (choice.equals("1")) {
                chat = openAiChatClient;
                System.out.println("Using OpenAI model");
            } else {
                chat = anthropicChatClient;
                System.out.println("Using Anthropic model");
            }

            // Use the selected chat client
            System.out.print("\nEnter your question: ");
            String input = scanner.nextLine();
            String response = chat.prompt(input).call().content();
            System.out.println("ASSISTANT: " + response);

            scanner.close();
        };
    }
}Copied!
```

#### 多个兼容 OpenAI 的 API 终端节点

这`OpenAiApi`和`OpenAiChatModel`类提供了一个`mutate()`方法，该方法允许您创建具有不同属性的现有实例的变体。当您需要使用多个与 OpenAI 兼容的 API 时，这尤其有用。

```java
@Service
public class MultiModelService {

    private static final Logger logger = LoggerFactory.getLogger(MultiModelService.class);

    @Autowired
    private OpenAiChatModel baseChatModel;

    @Autowired
    private OpenAiApi baseOpenAiApi;

    public void multiClientFlow() {
        try {
            // Derive a new OpenAiApi for Groq (Llama3)
            OpenAiApi groqApi = baseOpenAiApi.mutate()
                .baseUrl("https://api.groq.com/openai")
                .apiKey(System.getenv("GROQ_API_KEY"))
                .build();

            // Derive a new OpenAiApi for OpenAI GPT-4
            OpenAiApi gpt4Api = baseOpenAiApi.mutate()
                .baseUrl("https://api.openai.com")
                .apiKey(System.getenv("OPENAI_API_KEY"))
                .build();

            // Derive a new OpenAiChatModel for Groq
            OpenAiChatModel groqModel = baseChatModel.mutate()
                .openAiApi(groqApi)
                .defaultOptions(OpenAiChatOptions.builder().model("llama3-70b-8192").temperature(0.5).build())
                .build();

            // Derive a new OpenAiChatModel for GPT-4
            OpenAiChatModel gpt4Model = baseChatModel.mutate()
                .openAiApi(gpt4Api)
                .defaultOptions(OpenAiChatOptions.builder().model("gpt-4").temperature(0.7).build())
                .build();

            // Simple prompt for both models
            String prompt = "What is the capital of France?";

            String groqResponse = ChatClient.builder(groqModel).build().prompt(prompt).call().content();
            String gpt4Response = ChatClient.builder(gpt4Model).build().prompt(prompt).call().content();

            logger.info("Groq (Llama3) response: {}", groqResponse);
            logger.info("OpenAI GPT-4 response: {}", gpt4Response);
        }
        catch (Exception e) {
            logger.error("Error in multi-client flow", e);
        }
    }
}Copied!
```

## ChatClient Fluent API

这`ChatClient`Fluent API 允许您使用重载的`prompt`启动 Fluent API 的方法：

- `prompt()`：这种不带参数的方法允许您开始使用 Fluent API，从而允许您构建 user、system 和 prompt的其他部分。
- `prompt(Prompt prompt)`：此方法接受`Prompt`参数，允许您传入`Prompt`实例。
- `prompt(String content)`：这是一种类似于前面的重载的便捷方法。它获取用户的文本内容。

## ChatClient 响应

这`ChatClient`API 提供了多种使用 Fluent API 格式化来自 AI 模型的响应的方法。

### 返回 ChatResponse

来自 AI 模型的响应是由类型定义的丰富结构`ChatResponse`. 它包括有关响应生成方式的元数据，还可以包含多个响应，称为 [Generation](https://www.spring-doc.cn/spring-ai/1.0.0/api_chatmodel.html#Generation)s，每个响应都有自己的元数据。 元数据包括用于创建响应的标记数（每个标记大约是一个单词的 3/4）。 此信息非常重要，因为托管 AI 模型根据每个请求使用的Tokens数量收费。

返回`ChatResponse`对象通过调用`chatResponse()`在`call()`方法。

```java
ChatResponse chatResponse = chatClient.prompt()
    .user("Tell me a joke")
    .call()
    .chatResponse();Copied!
```

### 返回实体

您通常希望返回一个实体类，该实体类是从返回的`String`. 这`entity()`method 提供此功能。

例如，给定 Java 记录：

```java
record ActorFilms(String actor, List<String> movies) {}
Copied!
```

您可以使用`entity()`方法，如下所示：

```java
ActorFilms actorFilms = chatClient.prompt()
    .user("Generate the filmography for a random actor.")
    .call()
    .entity(ActorFilms.class);Copied!
```

还有一个重载的`entity`方法，签名`entity(ParameterizedTypeReference<T> type)`，它允许您指定类型，例如泛型 List：

```java
List<ActorFilms> actorFilms = chatClient.prompt()
    .user("Generate the filmography of 5 movies for Tom Hanks and Bill Murray.")
    .call()
    .entity(new ParameterizedTypeReference<List<ActorFilms>>() {});Copied!
```

### 流式响应

这`stream()`method 允许你获得异步响应，如下所示：

```java
Flux<String> output = chatClient.prompt()
    .user("Tell me a joke")
    .stream()
    .content();Copied!
```

您还可以流式传输`ChatResponse`使用方法`Flux<ChatResponse> chatResponse()`.

将来，我们将提供一个便捷的方法，让你返回一个带有响应式`stream()`方法。 同时，您应该使用 [Structured Output Converter](https://www.spring-doc.cn/spring-ai/1.0.0/api_structured-output-converter.html#StructuredOutputConverter) 来转换聚合响应的显式性，如下所示。 这也演示了 Fluent API 中参数的使用，这将在文档的后面部分更详细地讨论。

```java
var converter = new BeanOutputConverter<>(new ParameterizedTypeReference<List<ActorsFilms>>() {});

Flux<String> flux = this.chatClient.prompt()
    .user(u -> u.text("""
                        Generate the filmography for a random actor.
                        {format}
                      """)
            .param("format", this.converter.getFormat()))
    .stream()
    .content();

String content = this.flux.collectList().block().stream().collect(Collectors.joining());

List<ActorFilms> actorFilms = this.converter.convert(this.content);Copied!
```

## 提示模板

这`ChatClient`Fluent API 允许您将用户和系统文本作为模板提供，其中包含在运行时替换的变量。

```java
String answer = ChatClient.create(chatModel).prompt()
    .user(u -> u
            .text("Tell me the names of 5 movies whose soundtrack was composed by {composer}")
            .param("composer", "John Williams"))
    .call()
    .content();Copied!
```

在内部，ChatClient 使用`PromptTemplate`类来处理用户和系统文本，并将变量替换为运行时提供的值，具体取决于给定的`TemplateRenderer`实现。 默认情况下，Spring AI 使用`StTemplateRenderer`实现，它基于 Terence Parr 开发的开源 [StringTemplate](https://www.stringtemplate.org/) 引擎。

Spring AI 还提供了一个`NoOpTemplateRenderer`适用于不需要模板处理的情况。

Spring AI 还提供了一个`NoOpTemplateRenderer`.

|      | 这`TemplateRenderer`直接在`ChatClient`（通过`.templateRenderer()`） 仅适用于直接在`ChatClient`Builder Chain （例如，通过`.user()`,`.system()`). 它**不会影响** [Advisor](https://www.spring-doc.cn/spring-ai/1.0.0/api_retrieval-augmented-generation.html#_questionansweradvisor) 内部使用的模板，例如`QuestionAnswerAdvisor`，它们有自己的模板自定义机制（请参阅[自定义顾问模板](https://www.spring-doc.cn/spring-ai/1.0.0/api_retrieval-augmented-generation.html#_custom_template)）。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

如果您更愿意使用不同的模板引擎，则可以提供`TemplateRenderer`接口直接连接到 ChatClient。您也可以继续使用默认的`StTemplateRenderer`，但具有自定义配置。

例如，默认情况下，模板变量由语法标识。如果您计划在提示中包含 JSON，则可能需要使用不同的语法以避免与 JSON 语法冲突。例如，您可以使用 和 分隔符。`{}``<``>`

```java
String answer = ChatClient.create(chatModel).prompt()
    .user(u -> u
            .text("Tell me the names of 5 movies whose soundtrack was composed by <composer>")
            .param("composer", "John Williams"))
    .templateRenderer(StTemplateRenderer.builder().startDelimiterToken('<').endDelimiterToken('>').build())
    .call()
    .content();Copied!
```

## call（） 返回值

指定`call()`method 开启`ChatClient`，则响应类型有几种不同的选项。

- `String content()`：返回响应的 String 内容
- `ChatResponse chatResponse()`： 返回`ChatResponse`对象，其中包含多个代以及有关响应的元数据，例如用于创建响应的Tokens数。
- `ChatClientResponse chatClientResponse()`：返回`ChatClientResponse`对象，其中包含`ChatResponse`对象和 ChatClient 执行上下文，从而使您能够访问在执行 advisor 期间使用的其他数据（例如，在 RAG 流中检索的相关文档）。
- `entity()`返回 Java 类型
  - `entity(ParameterizedTypeReference<T> type)`：用于返回`Collection`的实体类型。
  - `entity(Class<T> type)`：用于返回特定实体类型。
  - `entity(StructuredOutputConverter<T> structuredOutputConverter)`：用于指定`StructuredOutputConverter`要将`String`设置为实体类型。

您还可以调用`stream()`method 而不是`call()`.

## stream（） 返回值

指定`stream()`method 开启`ChatClient`，则响应类型有几个选项：

- `Flux<String> content()`：返回`Flux`由 AI 模型生成的字符串。
- `Flux<ChatResponse> chatResponse()`：返回`Flux`的`ChatResponse`对象，其中包含有关响应的其他元数据。
- `Flux<ChatClientResponse> chatClientResponse()`：返回`Flux`的`ChatClientResponse`对象，其中包含`ChatResponse`对象和 ChatClient 执行上下文，从而使您能够访问在执行 advisor 期间使用的其他数据（例如，在 RAG 流中检索的相关文档）。

## 使用默认值

创建`ChatClient`在`@Configuration`类简化了运行时代码。 通过设置默认值，您只需在调用`ChatClient`，无需为运行时代码路径中的每个请求设置系统文本。

### 默认系统文本

在以下示例中，我们将系统文本配置为始终以海盗的声音回复。 为了避免在运行时代码中重复系统文本，我们将创建一个`ChatClient`实例中`@Configuration`类。

```java
@Configuration
class Config {

    @Bean
    ChatClient chatClient(ChatClient.Builder builder) {
        return builder.defaultSystem("You are a friendly chat bot that answers question in the voice of a Pirate")
                .build();
    }

}Copied!
```

以及`@RestController`要调用它：

```java
@RestController
class AIController {

	private final ChatClient chatClient;

	AIController(ChatClient chatClient) {
		this.chatClient = chatClient;
	}

	@GetMapping("/ai/simple")
	public Map<String, String> completion(@RequestParam(value = "message", defaultValue = "Tell me a joke") String message) {
		return Map.of("completion", this.chatClient.prompt().user(message).call().content());
	}
}Copied!
```

通过 curl 调用应用程序端点时，结果为：

```bash
❯ curl localhost:8080/ai/simple
{"completion":"Why did the pirate go to the comedy club? To hear some arrr-rated jokes! Arrr, matey!"}Copied!
```

### 带参数的默认系统文本

在以下示例中，我们将在系统文本中使用占位符来指定在运行时（而不是设计时）完成的声音。

```java
@Configuration
class Config {

    @Bean
    ChatClient chatClient(ChatClient.Builder builder) {
        return builder.defaultSystem("You are a friendly chat bot that answers question in the voice of a {voice}")
                .build();
    }

}Copied!
@RestController
class AIController {
	private final ChatClient chatClient;

	AIController(ChatClient chatClient) {
		this.chatClient = chatClient;
	}

	@GetMapping("/ai")
	Map<String, String> completion(@RequestParam(value = "message", defaultValue = "Tell me a joke") String message, String voice) {
		return Map.of("completion",
				this.chatClient.prompt()
						.system(sp -> sp.param("voice", voice))
						.user(message)
						.call()
						.content());
	}

}Copied!
```

通过 httpie 调用应用程序终端节点时，结果为：

```none
http localhost:8080/ai voice=='Robert DeNiro'
{
    "completion": "You talkin' to me? Okay, here's a joke for ya: Why couldn't the bicycle stand up by itself? Because it was two tired! Classic, right?"
}Copied!
```

### 其他默认值

在`ChatClient.Builder`级别，您可以指定默认提示配置。

- `defaultOptions(ChatOptions chatOptions)`：传入`ChatOptions`类或特定于模型的选项，例如`OpenAiChatOptions`.有关特定于模型的更多信息`ChatOptions`implementations，请参阅 JavaDocs。
- `defaultFunction(String name, String description, java.util.function.Function<I, O> function)`：这`name`用于在用户文本中引用函数。这`description`解释函数的用途，并帮助 AI 模型选择正确的函数以获得准确的响应。这`function`argument 是模型将在必要时执行的 Java 函数实例。
- `defaultFunctions(String… functionNames)`：在应用程序上下文中定义的 'java.util.Function' 的 bean 名称。
- `defaultUser(String text)`,`defaultUser(Resource text)`,`defaultUser(Consumer<UserSpec> userSpecConsumer)`：这些方法允许您定义用户文本。这`Consumer<UserSpec>`允许您使用 Lambda 指定用户文本和任何默认参数。
- `defaultAdvisors(Advisor… advisor)`：顾问程序允许修改用于创建`Prompt`.这`QuestionAnswerAdvisor`implementation 启用`Retrieval Augmented Generation`通过在 Prompt 中附加与用户文本相关的上下文信息。
- `defaultAdvisors(Consumer<AdvisorSpec> advisorSpecConsumer)`：此方法允许您定义`Consumer`要使用`AdvisorSpec`.顾问可以修改用于创建最终`Prompt`.这`Consumer<AdvisorSpec>`允许您指定一个 Lambda 来添加顾问程序，例如`QuestionAnswerAdvisor`，它支持`Retrieval Augmented Generation`通过根据用户文本在提示后附加相关上下文信息。

您可以在运行时使用相应的方法覆盖这些默认值，而无需`default`前缀。

- `options(ChatOptions chatOptions)`
- `function(String name, String description, java.util.function.Function<I, O> function)`
- `functions(String… functionNames)`
- `user(String text)`,`user(Resource text)`,`user(Consumer<UserSpec> userSpecConsumer)`
- `advisors(Advisor… advisor)`
- `advisors(Consumer<AdvisorSpec> advisorSpecConsumer)`

## 顾问

[Advisors API](https://www.spring-doc.cn/spring-ai/1.0.0/api_advisors.html) 提供了一种灵活而强大的方法来拦截、修改和增强 Spring 应用程序中的 AI 驱动的交互。

使用用户文本调用 AI 模型时，一种常见模式是使用上下文数据附加或增强提示。

此上下文数据可以是不同的类型。常见类型包括：

- **您自己的数据**：这是 AI 模型尚未训练的数据。即使模型看到了类似的数据，附加的上下文数据在生成响应时也优先。
- **对话历史记录**：聊天模型的 API 是无状态的。如果您告诉 AI 模型您的名字，它将在后续交互中不会记住它。必须随每个请求发送对话历史记录，以确保在生成响应时考虑以前的交互。

### ChatClient 中的 Advisor 配置

ChatClient Fluent API 提供了一个`AdvisorSpec`用于配置 advisor 的接口。此接口提供了添加参数、一次设置多个参数以及将一个或多个 advisor 添加到链的方法。

```java
interface AdvisorSpec {
    AdvisorSpec param(String k, Object v);
    AdvisorSpec params(Map<String, Object> p);
    AdvisorSpec advisors(Advisor... advisors);
    AdvisorSpec advisors(List<Advisor> advisors);
}Copied!
```

|      | 将 advisor 添加到链中的顺序至关重要，因为它决定了它们的执行顺序。每个 advisor 都以某种方式修改 prompt 或 context，并且一个 advisor 所做的更改将传递给链中的下一个 advisor。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

```java
ChatClient.builder(chatModel)
    .build()
    .prompt()
    .advisors(
        MessageChatMemoryAdvisor.builder(chatMemory).build(),
        QuestionAnswerAdvisor.builder(vectorStore).build()
    )
    .user(userText)
    .call()
    .content();Copied!
```

在此配置中，`MessageChatMemoryAdvisor`将首先执行，并将对话历史记录添加到提示符中。然后，`QuestionAnswerAdvisor`将根据用户的问题和添加的对话历史记录执行搜索，从而可能提供更相关的结果。

[了解 Question Answer Advisor](https://www.spring-doc.cn/spring-ai/1.0.0/api_retrieval-augmented-generation.html#_questionansweradvisor)

### 检索增强生成

请参阅 [Retrieval Augmented Generation](https://www.spring-doc.cn/spring-ai/1.0.0/api_retrieval-augmented-generation.html) 指南。

### Logging

这`SimpleLoggerAdvisor`是一个 advisor，它会记录`request`和`response`的数据`ChatClient`. 这对于调试和监控 AI 交互非常有用。

|      | Spring AI 支持 LLM 和向量存储交互的可观察性。有关更多信息，请参阅 [可观测性](https://www.spring-doc.cn/spring-ai/1.0.0/observability_index.html)指南 。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

要启用日志记录，请添加`SimpleLoggerAdvisor`添加到 advisor 链中。 建议将其添加到链的末尾：

```java
ChatResponse response = ChatClient.create(chatModel).prompt()
        .advisors(new SimpleLoggerAdvisor())
        .user("Tell me a joke?")
        .call()
        .chatResponse();Copied!
```

要查看日志，请将 advisor 包的日志记录级别设置为`DEBUG`:

```
logging.level.org.springframework.ai.chat.client.advisor=DEBUG
```

将此添加到您的`application.properties`或`application.yaml`文件。

您可以自定义来自哪些数据`AdvisedRequest`和`ChatResponse`使用以下构造函数进行记录：

```java
SimpleLoggerAdvisor(
    Function<AdvisedRequest, String> requestToString,
    Function<ChatResponse, String> responseToString
)Copied!
```

用法示例：

```java
SimpleLoggerAdvisor customLogger = new SimpleLoggerAdvisor(
    request -> "Custom request: " + request.userText,
    response -> "Custom response: " + response.getResult()
);Copied!
```

这允许您根据自己的特定需求定制记录的信息。

|      | 在生产环境中记录敏感信息时要小心。 |
| ---- | ---------------------------------- |
|      |                                    |

## 聊天记忆

界面`ChatMemory`表示聊天对话内存的存储。它提供了向对话添加消息、从对话中检索消息以及清除对话历史记录的方法。

目前有一个内置实现：`MessageWindowChatMemory`.

`MessageWindowChatMemory`是一种聊天内存实现，用于维护消息窗口，最大为指定的最大大小（默认值：20 条消息）。当消息数量超过此限制时，将驱逐较旧的消息，但会保留系统消息。如果添加了新的系统消息，则所有以前的系统消息都将从内存中删除。这可确保最新的上下文始终可用于会话，同时保持内存使用受限。

这`MessageWindowChatMemory`由`ChatMemoryRepository`abstraction 的 API 为 Chat 对话内存提供存储实现。有几种可用的实现，包括`InMemoryChatMemoryRepository`,`JdbcChatMemoryRepository`,`CassandraChatMemoryRepository`和`Neo4jChatMemoryRepository`.

有关更多详细信息和使用示例，请参阅 [Chat Memory](https://www.spring-doc.cn/spring-ai/1.0.0/api_chat-memory.html) 文档。

## 实施说明

命令式和响应式编程模型的组合使用`ChatClient`是 API 的一个独特方面。 通常，应用程序要么是响应式的，要么是命令式的，但不能同时是两者。

- 在自定义 Model 实现的 HTTP 客户端交互时，必须同时配置 RestClient 和 WebClient。

|      | 由于 Spring Boot 3.4 中的一个错误，必须设置“spring.http.client.factory=jdk”属性。否则，默认情况下，它设置为 “reactor”，这会破坏某些 AI 工作流，如 ImageModel。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

- 流仅支持通过 Reactive 堆栈。因此，命令式应用程序必须包含 Reactive 堆栈（例如 spring-boot-starter-webflux）。
- 非流式处理仅支持 Servlet 堆栈。出于这个原因，响应式应用程序必须包含 Servlet 堆栈（例如 spring-boot-starter-web），并预期某些调用会阻塞。
- 工具调用势在必行，这会导致工作流受阻。这也会导致部分/中断的 Micrometer 观察（例如，ChatClient span 和工具调用 span 未连接，由于该原因，第一个 span 保持不完整）。
- 内置顾问程序对标准调用执行阻塞作，对流式调用执行非阻塞作。的 Reactor Scheduler 用于 advisor 流式调用，可以通过每个 Advisor 类上的 Builder 进行配置。