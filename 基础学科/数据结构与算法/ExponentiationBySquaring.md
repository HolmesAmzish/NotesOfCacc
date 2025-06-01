---
title: 快速幂
date: 2025-03-07 19:31
author: Cacciatore
tags: ['algorithms']
---

**快速幂（Exponentiation by Squaring）**是一种用于计算大整数幂取模的算法，可以在 $O(\log n)$ 的时间复杂度内计算 $a^b \mod c$ 。

# 朴素幂运算

如果用普通的幂运算计算 a^b :

```python
def pow_naive(a, b, mod):
    result = 1
    for _ in range(b):
        result = (result * a) % mod
    return result
```

这种方法的时间复杂度是 O(b)，当 b 很大时，计算会非常慢。

# 快速幂的核心思想

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

