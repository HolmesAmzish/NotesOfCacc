# Transformer

## 背景

### RNN（Recurrent Neural Network）

现实世界中存在很多序列性质的数据，比如语言文字组成的话语，是一个序列信息。传统的神经网络假设输入是**独立同分布**的，比如图片等，无法捕捉前后依赖的关系。而 **RNN 循环神经网络** 就是为了记住过去的信息从而更好地理解当前输入。

RNN 引入了一个隐藏状态（hidden state）$h_t$ 他在每个时间布传递信息：

$$
h_t = \tanh (W_h h_{t-1} + W_x x_t + b) \\
y_t = W_y h_t + b_y
$$

其中：

- $x_t$ 是第 $t$ 步的输入，比如一个词向量

- $h_{t-1}$ 是上一时刻的隐藏状态（记忆）

- $h_t$ 为当前时刻的隐藏状态，融合了记忆与当前信息

- $y_t$ 当前输出

RNN 的优点在于，可以处理任意长度的序列，天然适合序列建模任务，比如语言模型和机器翻译的早期版本。

而 RNN 存在一些致命缺点，比如梯度消失和梯度爆炸。当序列很长时，反向传播的梯度会指数级衰减或爆炸，导致难以学习长期依赖。同时 RNN 无法并行计算，因为每一步都必须等前一步的 $h_{t-1}$ 算完才能算 $h_t$，训练速度很慢。

### 门控机制

**LSTM（Long Shot-Term Memory）**

LSTM 的核心思想即引入一条 **细胞状态（Cell State）** 作为门控。其含有四个关键组件，分别为遗忘门（Forget Gate）、输入门（Input Gate）、输出门（Output Gate）

**门控循环单元（GRU）**

GRU 为 LSTM 的简化机制，门控更少。

### 注意力机制

[注意力机制](https://zh.wikipedia.org/wiki/%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6)解决了上述这些问题。这一机制让模型得以提取序列中任意先前点的状态信息。注意力层能够访问所有先前的状态并根据学习到的相关性度量对其进行加权，从而提供相距很远的标记的相关信息。

假设有一个索引 i 排列的标记（token）序列，对于每一个标记 i，神经网络计算出每一个响应满足 $\sum_i w_i = 1$ 的非负软权重 $w_i$。每个标记都对应一个由词嵌入得到的向量 $v_i$。加权平均 $\sum_i w_i v_i$ 即是注意力机制的输出结果。

$$
c = \sum_{i=1}^N w_i \mathbf v_i
$$

## 架构

### 输入

输入文本使用字节对编码（Byte Pair Encoding，BPE）以进行标记化，这是一种子词标记化方法，假设输入如下：

```
"The transformer is powerful."
```

使用 BPE 标记化后：

```
tokens = ["The", "transform", "er", "is", "power", "ful", "."]
```

每个标记通过词嵌入（Embedding）转换为向量。然后，将标记的位置信息添加到嵌入向量中。词嵌入层（Token Embedding）是一个可学习的查找表，每个 token 对应一个固定维度的向量。

### 编码器 - 解码器架构

### 注意力

#### 缩放点积注意力

假设有一句话，经过词嵌入层形成了一个 token 序列 $X \in \mathbb R$，通过三个不同的线性投影矩阵得到三个向量 Q(query), K(key), V(value)：

$$
Q = X W^Q \\
K = X W^K \\
V = X W^V
$$

计算注意力分数矩阵

$$
E = QK^T
$$

$$
\text{Attention}(Q, K, V) = \text{softmax}(\frac{Q K^T}{\sqrt{d_k}})V
$$

#### 多头注意力

将上部分注意力计算过程看为一头，那么，对于同一个输入 X，用 h 组不同的投影矩阵生成 h 组独立的 QKV，每一组做一次缩放点积注意力，最后拼接起来。

$$
{head}_i = \text{Attention}(Q_i, K_i, V_i) = \text{softmax}(\frac{Q_i K_i^T}{\sqrt{d_k}})V_i
$$

随后拼接所有头

$$
\text{MultiHead}(X) = \text{Concat}(head_1, \dots, head_h)
$$
