---
title: Ollama 部署说明
date: 2025-03-15 15:29
author: Holmes Amzish
tags: ['ai']
---

# Ollama 介绍

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
