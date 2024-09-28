# K近邻算法

## 算法思想

算法主要思路：如果一个样本在特征空间中k个实例最为相似，即特征空间中最邻近，那么这k个实例中大多数属于哪个类别，则该样本也属于这个类别。

### 算法流程

1. 计算测试对象到训练集中每个对象的距离；
2. 按照距离的远近排序；
3. 选取与当前测试对象最近的k的训练对象，作为该测试对象的邻居；
4. 统计这k个邻居的类别频次；
5. k个邻居中频次最高的类别，即为测试对象的类别。

### 关键要素

1. 距离度量：特征空间中样本点的距离是样本点间向此程度的反应。
2. 算法超参数k的取值
3. 决策规则：对于分类任务，采取少数服从多数；对于回归任务，采用平均值规则。

## Matlab函数

`fitcknn()` fit classification KNN，拟合分类K近邻。主要参数包括训练数据集，训练标签和邻居数量K

```matlab
trainedModel = fitcknn(trainX, trainY, 'NumNeihbors', k);
```



## 鸢尾花分类

```matlab
clc; clear; clf;

load fisheriris

X = meas;       % features
Y = species;    % label

C = randperm(size(X, 1));
trainX = X(C(1:130), :);
trainY = Y(C(1:130));
testX = X(C(131:150), :);
testY = Y(C(131:150));

accuracy = zeros(1, 50);

tic;
for k = 1:200
    model = fitcknn(trainX, trainY, 'NumNeighbors', k);
    predictY = predict(model, testX);
    accuracy(k) = sum(strcmp(predictY, testY)) / length(testY);
end

toc;

% plot the accuracy
plot(1:200, accuracy);
xlabel('Number of Neighbors (k)');
ylabel('Accuracy');
title('K-NN Accuracy for Different k Values');
```

