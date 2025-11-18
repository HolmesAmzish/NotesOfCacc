# Vision Transformer（ViT）

在 Transformer 结构中，输入是一个 Token 序列。那么就需要将图像转换成对应形状，即 $Height \times Width \times Channel$ 直接分割成相同大小的 Patch 序列。然后经过可学习的线性投影层，得到输入 Embedding 向量。此时加入位置编码，并在头部加入一个 [CLS] Token，这个人为添加的 token 是为了通过 Transformer 机制把信息汇聚到这，最后把汇聚好的特征（或者说语义）输入给 MLP 分类器实现分类任务。

![vision-transformer](../assets/vision-transformer.png)

## 输入

### Patch Embedding

按照固定大小，将 H \times W 的图片分为 N 个 Patch，并将每个 Patch 输入进一个可学习的线性投射层。

$$
\mathbf{z}_0 = [\mathbf{x}_p^1 E; \mathbf{x}_p^2 E; \cdots; \mathbf{x}_p^N E]
$$

- $\mathbf{z_0}$ 投影后的 Patch 序列
- $\mathbf{E}$ 为可学习得到线性投影矩阵

### 加入 [CLS]Token 和位置编码

如图所示，形成以下内容

$$
\mathbf{z}_0 = [ \mathbf{z}_{\text{class}}; \mathbf{x}_p^1 E; \mathbf{x}_p^2 E; \cdots; \mathbf{x}_p^N E ] + \mathbf{E}_{\text{pos}}
$$

- $\mathbf{z}_{\text{class}} \in \mathbb{R}^{1 \times D}$：可学习分类 token
- $\mathbf{E}_{\text{pos}}$：可学习 1D 位置编码

## Transformer 编码器

在分类任务中，由于不需要生成内容，而是做一个分类判断，所以只引入了编码器而没有解码器。

Transformer Encoder Block 的公式如下

$$
\mathbf{z}'_\ell = \text{MSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1} \\
\mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell
$$

- 残差连接：+ 操作
- 共 $L=12$ 层

### 多头注意力（MSA, Multi-Head Self-Attention）

$$
\text{head}_i = \text{Attention}( \mathbf{z} W_i^Q, \mathbf{z} W_i^K, \mathbf{z} W_i^V ) \\
\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_{\text{head}}}} \right) V \\
\text{MultiHead}(\mathbf{z}) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O
$$

- $W_i^Q, W_i^K, W_i^V \in \mathbb{R}^{D \times d_{\text{head}}}$

- $W^O \in \mathbb{R}^{h d_{\text{head}} \times D}$

- $h=12, d_{\text{head}}=64, D=768$

### 前馈神经网络（MLP, Feed-Forward Network）

$$
\text{FFN}(x) = \text{GELU}(x W_1 + b_1) W_2 + b_2
$$

- $W_1 \in \mathbb{R}^{D \times 4D}, W_2 \in \mathbb{R}^{4D \times D}$

### Layer Normalization（LN, Norm）

$$
\text{LN}(\mathbf{x}_i) = \gamma \cdot \frac{\mathbf{x}_i - \mu_i}{\sqrt{\sigma_i^2 + \epsilon}} + \beta
$$

$\mu_i = \frac{1}{D} \sum_{j=1}^D x_{ij}, \quad \sigma_i^2 = \frac{1}{D} \sum_{j=1}^D (x_{ij} - \mu_i)^2$
$\gamma, \beta \in \mathbb{R}^D$：可学习

## MLP 分类头



$$
\mathbf{y} = \text{MLP}(\text{LN}(\mathbf{z}_L^0))
$$

- $\mathbf{z}_L^0$：Encoder 输出的 [CLS] token（第 0 个）

- $\mathbf{y} \in \mathbb{R}^{C}$，$C=1000$（ImageNet）

在 ViT 的图像分类任务中，所有 patch 的语义信息正是通过多层自注意力（MSA）机制，逐步“汇聚”（aggregate）到最前面的 [CLS] token，最终通过 MLP 分类头得出分类结果。