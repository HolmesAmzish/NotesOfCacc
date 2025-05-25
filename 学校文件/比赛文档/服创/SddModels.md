# 钢铁缺陷检测模型说明

## ResNet50 分类网络

**损失函数**：交叉熵损失（Cross Entropy Loss）
$$
\mathcal{L}_{CE} = -\sum_{c=1}^4 y_c \log(\mathrm{Softmax}(z)_c)
$$

- $z$: 模型输出的4维logits
- $y_c$: 真实类别标签（one-hot）

**优化器（AdamW）**：
$$
\theta_{t+1} = \theta_t - \eta \frac{\hat{m_t}}{\sqrt{\hat{v_t} + \epsilon}} - \eta\lambda\theta_t
$$

- $\lambda = 1e - 4$：权重衰减系数

**学习率调度（StepLR）**：
$$
\eta_t = \eta_{\mathrm{init}} \times 0.1^{[t/7]}
$$

ResNet50 通过四个阶段的残差块逐步提取从低级到高级的特征，最终输出四类缺陷的置信度。神经网络在浅中层聚焦局部纹理和几何特征（如列文轮廓），深层提取全局语义信息（如缺陷类型判别），结合Bottleneck 设计高效压缩计算量，并通过残差链接确保梯度稳定回传，避免深层网络退化。

本模型采用 ImageNet 预训练的 ResNet50 具有泛化性强和鲁棒性高的特点，其核心优势在于多尺度特征融合与结构创新，残差结构赋予模型对噪声（如反光）的鲁棒性，分阶段下采样平衡空间细节与语义抽象，Bottleneck 的卷积显著减少参数量，适合高分辨率输入。

## Efficient-B3 + Pyramid Attention Network 分割网络

**损失函数（多任务损失**：
$$
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{BCE}} + \lambda \mathcal{L}_{\text{Dice}}
$$
其中，**BCE With Logits Loss（多标签二分类）**:
$$
\mathcal{L}_{\text{BCE}} = -\frac{1}{4HW}\sum_{c=1}^{4}\sum_{i=1}^{H}\sum_{j=1}^{W} \left[y_{i,j,c} \log \sigma(x_{i,j,c}) + (1-y_{i,j,c}) \log(1-\sigma(x_{i,j,c}))\right]
$$

- $H,W$：特征图的高度和宽度
- $c$：类别索引（假设共4类）
- $y_{i,j,c}$：真实标签（0或1）
- $x_{i,j,c}$：模型输出的logits
- $\sigma$：Sigmoid函数

**Dice Loss（增强小目标分割）**：
$$
\mathcal{L}_{\text{Dice}} = 1 - \frac{2\sum_{i,j,c} p_{i,j,c} y_{i,j,c} + \epsilon}{\sum_{i,j,c} p_{i,j,c} + \sum_{i,j,c} y_{i,j,c} + \epsilon}
$$

- $p_{i, j, c}$：模型预测的概率（经过Sigmoid）
- $\epsilon = 1 \times 10^{-5}$：平滑项（避免除零）
- $\lambda = 0.8$：Dice Loss的权重系数

**优化器（AdamW）**：
$$
\theta_{t+1} = \theta_t - \eta_t \left(\frac{\hat{m_t}}{\sqrt{\hat{v_t} + \epsilon}} + \lambda_\omega\theta_t\right)
$$

- $\eta_t$：学习率（初始值 5×10−4）
- $\lambda_\omega = 1 \times 10 ^ {-4}$（权重衰减系数）

**学习率调度**：
$$
\eta_{t+1} = \begin{cases} 
0.5 \eta_t & \text{if } \mathcal{L}_{\text{val}} \text{ 3次未下降} \\
\eta_t & \text{otherwise}
\end{cases}
$$

在分割阶段，采用以EfficientNet-B3作为骨干网络，通过其深度可分离卷积与复合缩放机制高效提取多层级特征，结合PAN（Pyramid Attention Network）的多尺度特征融合与注意力机制，在保留空间细节的同时增强语义表征，从而精准分割出缺陷区域并实现细粒度缺陷类别判定。

EfficientNet的复合缩放策略平衡了计算效率与精度，PAN的注意力机制增强对小目标缺陷（如微米级裂纹）的敏感度，Dice系数较其他模型提升15%以上。



## 其他模型对比

| 模型                                 | DICE分数 |
| ------------------------------------ | -------- |
| 本模型（ResNet50 + EfficientB3-PAN） | 0.92171  |
| MobileNet2-UNet                      | 0.89802  |
| SE-ResNeXt50-UNet                    | 0.89230  |
| SE-UNet with ComboLoss Swish         | 0.87357  |
| EfficientNetB2-UNet++ TTA            | 0.87083  |
