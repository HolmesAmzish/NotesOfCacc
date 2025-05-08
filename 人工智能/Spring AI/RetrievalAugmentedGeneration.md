# Vector Databses

A vector database is a specialized type of database that plays an essential role in AI applications.

In vector databases, queries differ from traditional relational databases. Instead of exact matches, they perform similarity searches. When given a vector as a query, a vector database returns vectors that are “similar” to the query vector. Further details on how this similarity is calculated at a high-level is provided in a [Vector Similarity](https://docs.spring.io/spring-ai/reference/api/vectordbs/understand-vectordbs.html#vectordbs-similarity).

# Retriebal Augmented Generation

Retrieval Augmented Generation (RAG) is a technique useful to overcome the limitations of large language models that struggle with long-form content, factual accuracy, and context-awareness.

Spring AI supports RAG by providing a modular architecture that allows you to build custom RAG flows yourself or use out-of-the-box RAG flows using the `Advisor` API.

## Advisors

Spring AI provides out-of-the-box support for common RAG flows using the `Advisor` API.

To use the `QuestionAnswerAdvisor` or `RetrievalAugmentationAdvisor`, you need to add the `spring-ai-advisors-vector-store` dependency to your project:

```xml
<dependency>
   <groupId>org.springframework.ai</groupId>
   <artifactId>spring-ai-advisors-vector-store</artifactId>
</dependency>
```

