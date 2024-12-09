# LaTex 数学

## 希腊字母

|     字符     |   LaTeX    | 首字母大写 |   LaTeX    |    读音     |
| :----------: | :--------: | :--------: | :--------: | :---------: |
|  α  |  `\alpha`  |            |            |   /ˈælfə/   |
|  β  |  `\beta`   |            |            |  /ˈbeɪtə/   |
|  γ  |  `\gamma`  |  Γ         |  `\Gamma`  |   /ˈɡæmə/   |
|  δ  |  `\delta`  |  Δ         |  `\Delta`  |  /ˈdɛltə/   |
|  ϵ  | `\epsilon` |            |            | /ˈɛpsɪlɒn/  |
|  ζ  |  `\zeta`   |            |            |  /ˈzeɪtə/   |
|  η  |   `\eta`   |            |            |   /ˈeɪtə/   |
|  θ  |  `\theta`  |  Θ         |  `\Theta`  |  /ˈθiːtə/   |
|  ι  |  `\iota`   |            |            |  /aɪˈoʊtə/  |
|  κ  |  `\kappa`  |            |            |   /ˈkæpə/   |
|  λ  | `\lambda`  | Λ          | `\Lambda`  |  /ˈlæmdə/   |
|  μ  |   `\mu`    |            |            |   /mjuː/    |
|  ν  |   `\nu`    |            |            |   /njuː/    |
|  ξ  |   `\xi`    |   Ξ        |   `\Xi`    | /zaɪ, ksaɪ/ |
|  o  |     o      |   O        |     O      | /ˈɒmɪkrɒn/  |
|  π  |   `\pi`    |   Π    |   `\Pi`    ||
|  ρ  |   `\rho`   |            |            |    /roʊ/    |
|  σ  |  `\sigma`  |  Σ  |  `\Sigma`  |  /ˈsɪɡmə/   |
|  τ  |   `\tau`   |            |            | /taʊ, tɔː/  |
|  υ  | `\upsilon` | Υ | `\Upsilon` | /ˈʌpsɪlɒn/  |
|  ϕ  |   `\phi`   |   Φ   |   `\Phi`   |    /faɪ/    |
|  χ  |   `\chi`   |            |            |    /kaɪ/    |
|  ψ  |   `\psi`   |   Ψ   |   `\Psi`   |   /psaɪ/    |
|  ω  |  `\omega`  |  Ω  |  `\Omega`  | /oʊˈmeɪɡə/  |
|  ϝ  | `\digamma` |            |            | /daɪ'gæmə/  |

## 上下标

| 类型   | 符号             | LaTex        |
| ------ | ---------------- | ------------ |
| 上标   | $$a^2$$          | a^2          |
| 下标   | $$a_i$$          | a_i          |
| 上横线 | $$\overline{a}$$ | \overline{a} |
| 波浪   | $$\tilde{a}$$    | \tilde{a}    |

## 大型运算符

| 类型 | 符号          | LaTex       |
| ---- | ------------- | ----------- |
| 求和 | $$\sum$$      | `\sum`      |
| 求积 | $$\prod$$     | `\prod`     |
| 上积 | $$\coprod$$   | `\coprod`   |
| 并集 | $$\bigcup$$   | `\bigcup`   |
| 交集 | $$\bigcap$$   | `\bigcap`   |
| 析取 | $$\bigvee$$   | `\bigvee`   |
| 合取 | $$\bigwedge$$ | `\bigwedge` |

## 方程与方程组

```latex
\begin{cases}
3x + 5y + z \\
7x - 2y + 4z \\
-6x + 3y + 2z
\end{cases}
```

$$
\begin{cases}
3x + 5y + z \\
7x - 2y + 4z \\
-6x + 3y + 2z
\end{cases}
$$

### 条件表达式

```latex
f(n) = 
\begin{cases}
\frac{n}{2}, & \text{if } n \text{ is even} \\
3n + 1, & \text{if } n \text{ is odd}
\end{cases}
```

$$
f(n) = 
\begin{cases}
\frac{n}{2}, & \text{if } n \text{ is even} \\
3n + 1, & \text{if } n \text{ is odd}
\end{cases}
$$

### 多行等式

```latex
\begin{aligned}
f(x) & = (a+b)^2\\
& = a^2+2ab+b^2
\end{aligned}
```

$$
\begin{aligned}
f(x) & = (a+b)^2\\
& = a^2+2ab+b^2
\end{aligned}
$$

## 矩阵

|                          符号                          |                        LaTex                         |
| :----------------------------------------------------: | :--------------------------------------------------: |
|     $$\begin{matrix}a & b \\ c & d \end{matrix}$$      |     `\begin{matrix}a & b \\ c & d \end{matrix}`      |
|    $$\begin{vmatrix}a & b \\ c & d \end{vmatrix}$$     |    `\begin{vmatrix}a & b \\ c & d \end{vmatrix}`     |
|    $$\begin{Vmatrix}a & b \\ c & d \end{Vmatrix}$$     |    `\begin{Vmatrix}a & b \\ c & d \end{Vmatrix}`     |
|    $$\begin{bmatrix}a & b \\ c & d \end{bmatrix}$$     |    `\begin{bmatrix}a & b \\ c & d \end{bmatrix}`     |
|    $$\begin{Bmatrix}a & b \\ c & d \end{Bmatrix}$$     |    `\begin{Bmatrix}a & b \\ c & d \end{Bmatrix}`     |
|    $$\begin{pmatrix}a & b \\ c & d \end{pmatrix}$$     |    `\begin{pmatrix}a & b \\ c & d \end{pmatrix}`     |
| $$\begin{smallmatrix}a & b \\ c & d\end{smallmatrix}$$ | `\begin{smallmatrix}a & b \\ c & d\end{smallmatrix}` |

## 数组与表格

```latex
\begin{array}{c|lcr}
n & a & b & c \\
\hline
1 & 0.24 & 1 & 125 \\
2 & -1 & 189 & -8 \\
3 & -20 & 2000 & 1+10i
\end{array}
```

$$
\begin{array}{c|lcr}
n & a & b & c \\
\hline
1 & 0.24 & 1 & 125 \\
2 & -1 & 189 & -8 \\
3 & -20 & 2000 & 1+10i
\end{array}
$$

