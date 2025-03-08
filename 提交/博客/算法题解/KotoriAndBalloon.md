---
title: kotori 和气球
date: 2025-03-07
author: Cacciatore
tags: ['algorithms']
---

链接：https://ac.nowcoder.com/acm/problem/50039
题号：NC50039
时间限制：C/C++/Rust/Pascal 1秒，其他语言2秒
空间限制：C/C++/Rust/Pascal 32 M，其他语言64 M
64bit IO Format: %lld

# 题目描述

kotori最近迷上了摆气球的游戏。她一共有n种气球，每种气球有无数个。她要拿出若干个气球摆成一排。 但是，由于气球被施放了魔法，同样种类的气球如果相邻会发生爆炸，因此若两个相邻的气球种类相同被视为不合法的。

kotori想知道，摆成一排m个一共有多少种不同的方案？ 

由于该数可能过大，只需要输出其对109取模的结果。

**输入描述**

```
输入仅有一行，为两个整数n和m(1≤n,m≤100)
```

**输出描述**

```
输出一个整数，为方案数对109取模的结果。
```

## 示例1

输入

```
3 2
```

输出

```
6
```

说明

```
假设3种气球标记为1、2、3，那么共有以下6种方案：[1,2] [1,3] [2,1] [2,3] [3,1] [3,2]。
```



# 题解

## 动态规划

我们用 $f(m)$ 表示长度为 m 的序列的合法方案数：

- 第一个位置可以放 n 种气球。
- 第二个位置可以放的气球种类是 **除了前一个位置的气球种类外的其他 n - 1 种**。
- 第三个位置可以放 n - 1 种，依此类推。

因此，对于长度为 m 的排列方案，我们可以递推：
$$
f(m) = n \times (n - 1)^{(m  - 1)}
$$

## 快速幂计算

问题转换为**快速幂计算**：
$$
f(m) = n \times (n - 1)^{(m  - 1)} \mod 109
$$
这里补充一下快速幂运算的笔记：

### 朴素幂运算

如果用普通的幂运算计算 a^b

```python
def pow_naive(a, b, mod):
    result = 1
    for _ in range(b):
        result = (result * a) % mod
    return result
```

这种方法的时间复杂度是 O(b)，当 b 很大时，计算会非常慢。

### 快速幂的核心思想

快速幂的关键思想是将指数 b 分为二分之一然后通过平方累乘来减少计算次数。

- 假设 b 是偶数：
  $$
  a^b = (a^{b/2}) \times (a^{b/2})
  $$

- 假设 b 是奇数：
  $$
  a^b = a \times (a^{(b - 1)/2}) \times (a^{(b - 1)/2})
  $$

```python
def fast_pow(a, b, mod):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result
```

## 最终题解

```cpp
/**
 * Kotori and balloon
 * @date: 2025-03-07
 */

#include <iostream>
using namespace std;

int fast_pow(int base, int exp, int mod) {
    int result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main(void) {
    int n, m;
    cin >> n >> m;
    const int MOD = 109;
    if (m == 1) {
        cout << n % MOD << endl;
    } else {
        cout << (n * fast_pow(n - 1, m - 1, MOD)) % MOD << endl;
    }
    return 0;
}
```

