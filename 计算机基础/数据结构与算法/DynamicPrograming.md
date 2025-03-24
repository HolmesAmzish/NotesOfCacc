---
title: 动态规划
date: 2025-03-16 23:30
author: Cacciatore
tags: ['algorithms']
---

## DP 背包

### 0-1 背包问题

有 *N* 件物品和一个容量是 W 的背包。每件物品只能使用一次。第 *i* 件物品的重量是 $w_i$，价值是 $v_i$。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。

维护一个 DP 数组，每一列表示背包的容量，假设有 i 个物品，那么通过 i 次循环依次找到每次情况下相应背包容量的最大价值。设 DP 状态 f_{i, j} 为在只能放前 i 个物品的情况下过，容量为 j 的背包所能达到的最大总价值。那么：
$$
f_{i, j} = \max(f_{i - 1, j}, f_{i - 1, j - w_i} + v_i)
$$

#### 输入样例

```
4 5
1 2
2 4
3 4
4 5
```

#### 输出样例

```
8
```

#### 答案

倒序遍历，因为每一次遍历时 dp[i - weight] 都是没有遍历过的，所以在遍历完后保证只使用了一次该物品。

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      | 0    | 0    | 0    | 0    | 0    | 0    |
| 1, 2 | 0    | 2    | 2    | 2    | 2    | 2    |
| 2, 4 | 0    | 2    | 4    | 6    | 6    | 6    |
| 3, 4 | 0    | 2    | 4    | 6    | 6    | 8    |
| 4, 5 | 0    | 2    | 4    | 6    | 6    | 8    |



```python
n, max_weight = map(int, input().split())
items = []

for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

dp = [0] * (max_weight + 1)

for weight, value in items:
    for i in range(max_weight, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)
    #print(dp)

print(dp[max_weight])
```



### 完全背包问题

有 *N* 种物品和一个容量是 *V*

 的背包，每种物品都有无限件可用。

第 *i*

 种物品的体积是 *v**i*，价值是 *w**i*

。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
 输出最大价值。





#### 输入样例

```
4 5
1 2
2 4
3 4
4 5
```

#### 输出样例

```
10
```

#### 答案

正序遍历让每次遍历在先前的基础上求出最优解，每一个物品使用了若干次。

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      | 0    | 0    | 0    | 0    | 0    | 0    |
| 1, 2 | 0    | 2    | 4    | 6    | 8    | 10   |
| 2, 4 | 0    | 2    | 4    | 6    | 8    | 10   |
| 3, 4 | 0    | 2    | 4    | 6    | 8    | 10   |
| 4, 5 | 0    | 2    | 4    | 6    | 8    | 10   |

```python
n, max_weight = map(int, input().split())
items = []

for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

dp = [0] * (max_weight + 1)

for weight, value in items:
    for i in range(weight, max_weight + 1):
        dp[i] = max(dp[i], dp[i - weight] + value)

    print(dp)

print(dp[max_weight])
```

