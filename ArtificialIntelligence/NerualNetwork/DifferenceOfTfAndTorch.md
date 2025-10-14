---
title: 如何选择 Tensorflow 与 Pytorch
date: 2025-02-04 09:39
tags: ['machine-learning']
---

# 背景

TensorFlow 与 PyTorch 都是比较流行的深度学习框架。tf 由谷歌在 2015 年发布，而 PyTorch 则是 Facecbook AI 研究团队 2016 年在原来 Torch 的基础上发布的。

tf 采用的是静态计算图。这意味着在执行任何计算之前，你需要先定义好整个计算图，之后再执行。这种方式适合大规模生产环境，可以优化计算图以提高效率。tf 的早期版本比较复杂，但在集成 Keras 库之后相当容易上手。

PyTorch 的设计目标是提供一个易于使用、灵活且高效的框架，所以采用的是动态图，特别适合研究人员和开发人员进行快速实验和原型设计。它强调灵活性和易用性，采用了动态图机制，使得代码更接近于 Python 原生风格，便于调试和修改。PyTorch 使用更加像原来的 Python 代码。

总体来说，TensorFlow 更加容易上手，PyTorch 更加灵活且需要自己操作，例如 tf 提供了训练的方法，而 PyTorch 则需要手动训练：

```python
# TensorFlow
model.fit(train_images, train_labels, epochs=5, batch_size=128)
```

而 PyTorch 需要先手动将数据分批，然后自己编写训练和测试函数，函数详细内容后面会写：

```python
# PyTorch
epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model, loss_fn)
print("Done!")
```

# 示例

## MNIST 数据集

对于两者的示例，仍然使用 MNIST 手写数字集来做演示。MNIST 是 28 * 28 大小的单通道（黑白）手写数字图片，每个像素亮度值为 0 ~ 255。

首先加载数据集：

```python
# TensorFlow
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
```

PyTorch 除了加载数据，还需要定义 DataLoader，因为其提供的框架更加底层，需要自己定义加载器，包括数据打包，转换等更加灵活的功能。

```python
# PyTorch
to_tensor = transforms.Compose([transforms.ToTensor()])
training_data = datasets.MNIST(root="data", train=True, download=True, transform=to_tensor)
test_data = datasets.MNIST(root="data", train=False, download=True, transform=to_tensor)

train_dataloader = DataLoader(training_data, batch_size=128, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=128, shuffle=True)
```

## 定义神经网络

TensorFlow 集成了 Keras，这里可以看见对神经网络的定义非常简洁明了：

```python
# TensorFlow
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten the input image to a vector of size 784
    layers.Dense(512, activation="relu"),
    layers.Dense(10, activation="softmax")
])
```

在 PyTorch 中，更倾向于将神经网络打包成一个类，这个类由框架提供的网络模型继承。

```python
# PyTorch
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(in_features=28 * 28, out_features=512)
        # Output layer with 10 neurous for classification
        self.fc2 = nn.Linear(in_features=512, out_features=10)

    def forward(self, x):
        x = self.flatten(x) # Flatten the input tensor
        x = nn.functional.relu(self.fc1(x)) # ReLU activation after first layer
        x = self.fc2(x)
        return x

print(model)
```

PyTorch 可以检查神经网络模型

```
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (fc1): Linear(in_features=784, out_features=512, bias=True)
  (fc2): Linear(in_features=512, out_features=10, bias=True)
)
```

## 训练

TensorFlow 在网络模型定义完成后，指定损失函数和优化器，来使模型训练让参数收敛。

```python
model.compile(optimizer="rmsprop",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=5, batch_size=128)
```

```
Epoch 1/5
469/469 [==============================] - 3s 5ms/step - loss: 5.4884 - accuracy: 0.8992
Epoch 2/5
469/469 [==============================] - 2s 4ms/step - loss: 0.6828 - accuracy: 0.9538
Epoch 3/5
469/469 [==============================] - 2s 4ms/step - loss: 0.4634 - accuracy: 0.9662
Epoch 4/5
469/469 [==============================] - 2s 4ms/step - loss: 0.3742 - accuracy: 0.9730
Epoch 5/5
469/469 [==============================] - 2s 4ms/step - loss: 0.2930 - accuracy: 0.9774
```

而在 PyTorch 中则更加复杂，需要自己定义训练函数和测试函数，并不断训练，框架只提供了一些基础的训练所需函数：

```python
# Define loss function and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.RMSprop(model.parameters(), lr=0.001)

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {100*(correct):>0.1f}%, Avg loss: {test_loss:>8f}\n")

epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model, loss_fn)
print("Done!")
```

```
Epoch 1
-------------------------------
loss: 2.319496  [  128/60000]
loss: 0.443893  [12928/60000]
loss: 0.253097  [25728/60000]
loss: 0.106967  [38528/60000]
loss: 0.208099  [51328/60000]
Test Error: 
 Accuracy: 95.9%, Avg loss: 0.136413

Epoch 2
-------------------------------
loss: 0.102781  [  128/60000]
loss: 0.089506  [12928/60000]
loss: 0.177988  [25728/60000]
loss: 0.058250  [38528/60000]
loss: 0.131542  [51328/60000]
Test Error: 
 Accuracy: 97.3%, Avg loss: 0.087681

Epoch 3
-------------------------------
loss: 0.100185  [  128/60000]
loss: 0.021117  [12928/60000]
loss: 0.058108  [25728/60000]
loss: 0.070415  [38528/60000]
loss: 0.050509  [51328/60000]
Test Error: 
 Accuracy: 97.7%, Avg loss: 0.075040

Epoch 4
-------------------------------
loss: 0.051223  [  128/60000]
loss: 0.049627  [12928/60000]
loss: 0.025712  [25728/60000]
loss: 0.090960  [38528/60000]
loss: 0.046523  [51328/60000]
Test Error: 
 Accuracy: 97.9%, Avg loss: 0.066997

Epoch 5
-------------------------------
loss: 0.012129  [  128/60000]
loss: 0.019118  [12928/60000]
loss: 0.057839  [25728/60000]
loss: 0.031959  [38528/60000]
loss: 0.020570  [51328/60000]
Test Error: 
 Accuracy: 98.0%, Avg loss: 0.062022

Done!
```
