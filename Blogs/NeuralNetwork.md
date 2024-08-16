# 神经网络

## 结构概念

**总体上**：神经网络是由多层节点组合而成的系统。*以一个简单的神经网络为例*，输入一组数据（一般称为特征向量），根据神经网络中多个节点的计算和组合，最后输出一个结果。其中间各层称为隐藏层，在神经网络负责计算输入的各项数据，不断进行信息蒸馏，最后传给输出层。这个神经网络负责一个二分类的任务，最后输出层的节点激活函数为sigmoid函数，输出了根据特征而判断的概率。

![network](../img/37.png)

**个体上**：神经网络由多层组成，而每一层由若干节点组成。每个节点都负责计算相关数据。由其中一个节点举例，根据前者节点（或者最初的输入）得到的向量，添加权重和偏值进行处理，然后经过神经元的激活函数，计算出输出向量。

![node](../img/38.png)

$$
z = \vec{w} \cdot \vec{x} + b \\
g(z) = \frac{1}{1+e^{-z}}
$$

由于特征经常是超过一个的，所以多个特征组成了一个特征向量，相对应的权重也是一个向量。其中权重和偏值都是可修改的参数，会根据训练数据来动态调整。激活函数有多种选择，例如`Sigmoid`, `tanh`, `ReLU`函数。这里的sigmoid只是其中的一种。同层节点的激活函数是一样的，层与层之间可以不同。不同的激活函数用处不同，尤其是随后输出层，需要根据问题所确定。

![sigmoid](../img/29.png)

![relu](../img/39.png)

并且由于，某个节点的前一层，有多个节点，虽然一个节点的输出并不是一个向量，但是多个节点再次组成一个向量。也因此向量个数在经过层层蒸馏后，越来越少，最后输出一个想要的结果。

## 构建步骤

### 问题

假设，现在有一组数据，分别是点的坐标，以及颜色。这里可以先手动创建一组数据。

```python
import random

points = []
for i in range(1000):
    x1 = random.randint(0, 1000)
    x2 = random.randint(0, 1000)
    if pow((x1 - 500), 2) + pow((x2 - 500), 2) <= 62500:
        tag = 1
    else:
        tag = 0
    points.append((x1, x2, tag))

with open('points.csv', 'w') as file:
    for point in points:
        file.write(str(point[0]) + ',' + str(point[1]) + ',' + str(point[2]) + '\n')

print("All points have been written to the file.")
```

这里在1000*1000的图中，随机生成散点，并且设置在以(500, 500)为圆心，250为半径的圆内的点为红色，设置为1，否则为0。

以这些点为数据，构建神经网络，然后训练。根据输入的特征向量，让神经网络判断这个点是否是红色的。

### 处理数据

神经网络在预测结果前，首先需要训练数据。训练数据包括特征和已经判断好的结果。因此，神经网络会根据特征向量，预测结果和实际数据结果来调整每个节点前的权重和偏置。因此首先需要将刚刚写入的数据，分开，并分为训练数据和测试数据。

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# 从文件中读取数据
data = pd.read_csv('points.csv', header=None, names=['x1', 'x2', 'label'])
X = data[['x1', 'x2']].values
y = data['label'].values

# 将数据分为训练和测试数据，设置比例和随机
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

在训练前，需要对数据进行**标准化**。标准化会对原始数据进行初次处理，让数据特征更快的收敛，并提高模型的性能。

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

根据`matplotlib.pyplot`生成训练数据的模型

```python
import matplotlib.pyplot as plt
color = {
    0: 'blue',
    1: 'red'
} # 创建一个颜色的字典用于将原来的数据标签转换成颜色字符
plt.figure(figsize=(12, 8))
colors = [color[label] for label in y_train]
plt.scatter(x=X_train[:, 0], y=X_train[:, 1], c=colors, alpha=0.5, label=colors)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Train data')
plt.show()
```

![train](../img/40.png)

### 构建模型

```python
from tensorflow import keras
from tensorflow.keras import layers

# Create the neural network
model = keras.Sequential([
    layers.Dense(16, activation='relu', input_shape=(2,)),
    layers.Dense(8, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

创建一个模型，很容易看出这里的神经网络，由三层构成。第一层是16个神经元组成的，激活函数为`ReLU`函数的输入层。其中`input_shape`就是表示，输入的是一组点坐标向量，一个点有两个坐标表示。第三层是一个激活函数为`Sigmoid`的神经元。这个二分类问题会根据模型输出的结果来确定是否是红色，最后的输出就是是否是红色的概率。

随后设置其他选项，比如优化器，损失函数，评估指标。其中这里比较重要的是损失函数，`binary_crossentropy`表示二元交叉熵，通常用于二分类问题。

### 训练模型

```python
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=4)
print("Training complete.\n")
```

使用训练数据对模型进行训练。这里设置10批次。

### 评估模型

评估模型就是根据测试数据与测试标签对照着模型输出的结果，来测试他的准确率，来看这个模型是否已经被训练好。

```python
loss, accuracy = model.evaluate(X_test, y_test)
y_hat_pred = model.predict(X_test)
y_hat = (y_hat_pred > 0.5).astype(int).flatten()
```

最后输出测试结果的图片来直观感受一下预测的准确率，这里对预测错误的数据进行了标注。

```python
shape = {
    True: 'o',
    False: 'x'
}

plt.figure(figsize=(12, 8))
colors = [color[label] for label in y_test]
shapes = [shape[y_ == y_hat_] for y_, y_hat_ in zip(y_test, y_hat)]

for x1, x2, c, s in zip(X_test[:, 0], X_test[:, 1], colors, shapes):
    plt.scatter(x1, x2, color=c, marker=s, alpha=0.5)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Test data')
plt.show()

print(f'Test Accuracy: {accuracy:.4f}')
```

![train](../img/42.png)

![train_point](../img/41.png)

根据输出，可以看出，随着训练批次不断增加，准确性程上升趋势。最后通过测试数据，评估模型的准确率为97.66%。损失函数也较小。则这样就可以判断这个模型比较适合这个问题。
