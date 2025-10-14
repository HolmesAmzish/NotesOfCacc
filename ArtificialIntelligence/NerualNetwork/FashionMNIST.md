---
title: PyTorch 识别预测 Fashion MNIST 数据集
date: 2025-02-07 13:37
tags: ['machine-learning', 'pytorch']
---

# Fashion-MNIST 数据集

Fashion-MNIST 是一个由 Zalando 提供的公开数据集，它是 MNIST 数据集的一个变种，用于图像分类任务。MNIST 数据集包含手写数字（0-9）的图像，而 Fashion-MNIST 数据集包含的是10 类时尚物品的灰度图像。这个数据集是为了作为深度学习、计算机视觉和机器学习研究中的标准数据集，提供比原始 MNIST 数据集更具有挑战性的问题。他提供 60,000 训练数据和 10,000 测试数据。其中，数据的 10 种标签分别是：

```
0 T-shirt/top
1 Trouser
2 Pullover
3 Dress
4 Coat
5 Sandal
6 Shirt
7 Sneaker
8 Bag
9 Ankle boot
```

<img src="../../img/fashion-mnist-dataset.png">

# 卷积神经网络

## 准备工作

导入相关库

```python
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor
import matplotlib
import matplotlib.pyplot as plt
import os
import random

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
matplotlib.use('TkAgg')
```

加载数据

```python
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

train_data = datasets.FashionMNIST(root='data', train=True, download=True, transform=transform)
test_data = datasets.FashionMNIST(root='data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64, shuffle=False)
```

## 神经网络

### 定义模型

```python
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()

        # Convolutional layers
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        # Pooling layers
        self.pool = nn.MaxPool2d(2, 2)

        # Full connected layers
        self.fc1 = nn.Linear(128 * 3 * 3, 512)
        self.fc2 = nn.Linear(512, 10)

        # Dropout layer
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = self.pool(torch.relu(self.conv3(x)))

        x = x.view(-1, 128 * 3 * 3)

        x = torch.relu(self.fc1(x))
        x = self.dropout(x)

        x = self.fc2(x)
        return x
```

### 设置优化参数

首先打印模型，然后检测使用 GPU 还是 CPU 来推理模型。然后设置损失函数和优化器。

```python
model = NeuralNetwork()
print(model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using {device} device")
model.to(device)

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

```
NeuralNetwork(
  (conv1): Conv2d(1, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv2): Conv2d(32, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (pool): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (fc1): Linear(in_features=1152, out_features=512, bias=True)
  (fc2): Linear(in_features=512, out_features=10, bias=True)
  (dropout): Dropout(p=0.5, inplace=False)
)
Using cuda device
```

## 训练

### 训练和测试函数

首先将每批次训练和测试的功能以函数编写出来

```python
def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Computer prediction error
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
```

### 开始训练

```python
epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_loader, model, loss_fn, optimizer)
    test(test_loader, model, loss_fn)
print("Done!")
```

```
Epoch 1
-------------------------------
loss: 2.302333  [   64/60000]
loss: 0.647033  [ 6464/60000]
loss: 0.580490  [12864/60000]
loss: 0.485724  [19264/60000]
loss: 0.545703  [25664/60000]
loss: 0.477990  [32064/60000]
loss: 0.333280  [38464/60000]
loss: 0.251924  [44864/60000]
loss: 0.278290  [51264/60000]
loss: 0.322126  [57664/60000]
Test Error: 
 Accuracy: 88.1%, Avg loss: 0.323977

Epoch 2
-------------------------------
loss: 0.460136  [   64/60000]
loss: 0.192585  [ 6464/60000]
loss: 0.198050  [12864/60000]
loss: 0.388034  [19264/60000]
loss: 0.303517  [25664/60000]
loss: 0.274965  [32064/60000]
loss: 0.389794  [38464/60000]
loss: 0.321096  [44864/60000]
loss: 0.327351  [51264/60000]
loss: 0.432855  [57664/60000]
Test Error: 
 Accuracy: 89.7%, Avg loss: 0.277630

Epoch 3
-------------------------------
loss: 0.248235  [   64/60000]
loss: 0.171419  [ 6464/60000]
loss: 0.281354  [12864/60000]
loss: 0.211329  [19264/60000]
loss: 0.168916  [25664/60000]
loss: 0.373718  [32064/60000]
loss: 0.296880  [38464/60000]
loss: 0.219861  [44864/60000]
loss: 0.300871  [51264/60000]
loss: 0.212363  [57664/60000]
Test Error: 
 Accuracy: 90.8%, Avg loss: 0.251683

Epoch 4
-------------------------------
loss: 0.266523  [   64/60000]
loss: 0.266919  [ 6464/60000]
loss: 0.186859  [12864/60000]
loss: 0.331688  [19264/60000]
loss: 0.250632  [25664/60000]
loss: 0.089399  [32064/60000]
loss: 0.321142  [38464/60000]
loss: 0.116718  [44864/60000]
loss: 0.230768  [51264/60000]
loss: 0.252787  [57664/60000]
Test Error: 
 Accuracy: 90.9%, Avg loss: 0.255058

Epoch 5
-------------------------------
loss: 0.208207  [   64/60000]
loss: 0.212660  [ 6464/60000]
loss: 0.228951  [12864/60000]
loss: 0.320543  [19264/60000]
loss: 0.187334  [25664/60000]
loss: 0.132721  [32064/60000]
loss: 0.228733  [38464/60000]
loss: 0.153230  [44864/60000]
loss: 0.180108  [51264/60000]
loss: 0.246346  [57664/60000]
Test Error: 
 Accuracy: 91.3%, Avg loss: 0.251047

Done!
```

## 模型的保存和预测

### 保存和加载模型

```python
# Save current model
torch.save(model.state_dict(), "models/fashion_mnist_model.pth")
print("Saved PyTorch Model State to fashion_mnist_model.pth")
```

```python
# Load model from pth file
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("models/fashion_mnist_model.pth"))
```

### 模型预测

```python
model.eval()

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

random_index = random.randint(0, len(test_data))
x, y = test_data[random_index][0], test_data[random_index][1]
with torch.no_grad():
    x = x.unsqueeze(0).to(device)
    pred = model(x)
    predicted_class = pred.argmax(1).item()

plt.imshow(x.squeeze().cpu(), cmap="gray")
plt.title(f"Predicted: {classes[predicted_class]}, Actual: {classes[y]}")
plt.show()
```

## 参考

Zalando Research. (2017). *Fashion-MNIST* [Data set]. Kaggle. https://www.kaggle.com/datasets/zalando-research/fashionmnist/data

Pytorch. *Introduction to PyTorch*. https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
