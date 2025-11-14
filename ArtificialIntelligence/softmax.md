在数学中，尤其是概率论和相关领域中，Softmax 函数，或称**归一化指数函数**，它能将含任意实数的 K 维向量 $\mathbf{z}$ 压缩到另一个 K 维向量 $\sigma(\mathbf{z})$，使得每一个元素都在 $(0, 1)$ 之间，并且和等于1。

给定一个向量 $\mathbf{z} = [z_1, z_2, \dots, z_n]$，Softmax 输出：

$$
\text{softmax}(\mathbf z)_i = \frac{\exp(z_i)}{\sum_{j=1}^n\exp(z_j)}
$$

- 输出 $\text{softmax}(\mathbf z)_i \in [0, 1]$

- $\sum_{i=1}^n\text{softmax}(\mathbf{z})_i = 1$
