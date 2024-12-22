# 机器学习-识别MNIST手写数字

机器学习可以首先构建一个神经网络，用于识别手写数字。通过训练数据，优化神经网络的参数。再利用测试数据来测试训练完成后的神经网络的准确度。本次需要下载的库有tensorflow和matplotlib，keras和mnist数据集一般都被集成在tensorflow中了。

## MNIST手写数字数据

首先查看一下MNIST手写数字的数据是什么样子的。

```python
from tensorflow.keras.datasets import mnist

# 读取MNIST数据
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 查看训练数据
train_images.shape()

# 查看训练数据的标签
len(train_labels)
train_labels
```

```
# 训练数据
(60000, 28, 28)

# 训练标签
60000
array([5, 0, 4, ..., 5, 6, 8], dtype=uint8)
```

从上面可以看出，MNIST手写数字的数据，是28*28的灰度图片，并且在训练数据中，有一共60000张这样的手写数字图片。在训练标签中，一共有60000个对应的数字，作为训练数据的标签。

可以利用matplot去查看这些28*28的图片是什么样子。

```python
import matplotlib.pyplot as plt

plt.imshow(train_images[0], cmap='binary')
plt.show
```

![train_images[0]](../../../img/43.png)

可以清晰的看到，这个手写数字图片由28*28个像素组成，并且每个像素深度在0-255之间，组成的像素表达了一个人眼可以分辨的数字5。然而机器无法直接读取出这个数字，而是通过读取每个像素的数据，根据训练好的模型才能给出结果。

## 构建神经网络

```python
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten the input image to a vector of size 784
    layers.Dense(512, activation="relu"),
    layers.Dense(10, activation="softmax")
])

model.compile(optimizer="rmsprop",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
```

在这里可以看出，这个神经网络的结构比较简单，一共有三层。输入层，将`28*28`的矩阵展平为一维向量，并输入给第二层计算。第二层是一个激活函数为`ReLU`函数并含有512个节点的隐藏层。第三层输出层，激活函数为`softmax`用于多分类问题。而10个节点，也就代表了从零到九的十个数字。可以看出这个神经网络就是为了解决一个十种可能的多分类问题。

## 训练神经网络

在利用刚刚读取的MNIST手写数字数据集，对刚刚构建的神经网络进行训练

```python
# 将数据缩小到0-1，有利于神经网络的快速计算和训练
train_images = train_images.astype("float32") / 255
test_images = test_images.astype("float32") / 255

model.fit(train_images, train_labels, epochs=5, batch_size=128)
```

```
Epoch 1/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step - accuracy: 0.8727 - loss: 0.4416
Epoch 2/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - accuracy: 0.9664 - loss: 0.1143
Epoch 3/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - accuracy: 0.9795 - loss: 0.0703
Epoch 4/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - accuracy: 0.9841 - loss: 0.0521
Epoch 5/5
469/469 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - accuracy: 0.9892 - loss: 0.0369
```

可以看出随着五次的训练，准确率升高非常迅速，损失值也在减小。

## 预测结果

五个批次全部训练完成后，可以根据测试数据，来对神经网络的准确性进行判断。

```python
predictions = model.predict(test_images)

# 查看第一个测试数据的图像
plt.imshow(test_images[0], cmap='binary')
plt.show()

# 查看模型的预测结果
print(predictions[0])

# 查看模型预测结果，最可能的值
print(predictions[0].argmax())

# 查看正确的标签
print(test_labels[0])
```

![12](../../../img/44.png)

```
313/313 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step  
[2.4641224e-08 1.5685966e-08 4.7843769e-06 6.2090970e-05 5.8346529e-11
 9.6760395e-08 7.8394131e-11 9.9992907e-01 3.8257639e-08 3.8722346e-06]
7
7
```

在这里首先输出了模型的预测结果，是从0到9的可能性。模型的最后预测结果是7最大，所以输出了7，与正确的标签一致。