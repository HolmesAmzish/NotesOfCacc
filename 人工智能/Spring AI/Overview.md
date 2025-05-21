---
title: Spring AI
date: 2025-04-28
---



# AI Concepts

## Models

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-concepts-model-types.jpg" width=80%>

## Embeddings

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-embeddings.jpg" width=100%>

## Tokens

Tokens serve as the building blocks of how an AI model works. On input, models convert words to tokens. On output, they convert tokens back to words.

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-concepts-tokens.png" width=60%>

## Bringing Your Data & APIs to the AI Model

Three techniques exist for customizing the AI model to incorporate your data:

**Fine Tuning**: This traditional machine learning technique involves tailoring the model and changing its internal weighting. However, it is a challenging process for machine learning experts and extremely resource-intensive for models like GPT due to their size. Additionally, some models might not offer this option.

### Retrieval Augmented Generation

**Pormpt Stuffing**: A more practical alternative involves embedding your data within the prompt provided to the model. Given a model's token limits, techniques are required to present relevand data within the model's context window. This approach is colloquially referred to as "stuffing the prompt." The Spring AI library helps you implement solutions based on the "stuffing the prompt" technique otherwise known as **Retrieval Augmented Generation (RAG)**.

提示词填充：一种更实用的方法是将您的数据嵌入到提供给模型的提示词中。由于模型存在令牌（token）限制，需要通过技术手段在模型的上下文窗口内呈现相关数据。这种方法被通俗地称为"填充提示词"。Spring AI 库可帮助您实现基于提示词填充（**检索增强生成**，RAG）的解决方案。

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-prompt-stuffing.jpg" width=100%>

A technique termed Retrieval Augmented Generateion (RAG) has emerged to address the challenge of incorporating relevant data into prompts for accurate AL model responses.

The approach involves a batch processing style programming model, where the job reads unstructured data from your documents, transforms it, and then writes it into a vector database. At a high level, this is an ETL (Extract, Transform and Load) pipeline. The vector database is used in the retrieval part of RAG technique.

When a user's question is to be answered by an AI model, the question and all the "similar" document pieces are placed into the prompt that is sent to the AI model. This is the reason to use a vector database. It is very good at finding similar content.

<img src="https://docs.spring.io/spring-ai/reference/_images/spring-ai-rag.jpg">

### Tool Calling

**Tool Calling**: This technique allows registering tools (user-defined services) that connect the large language models to the APIs of external systems. Spring AI greatly simplifies code you need to write to support tool calling.

<img src="https://docs.spring.io/spring-ai/reference/_images/tools/tool-calling-01.jpg" width=70%>

