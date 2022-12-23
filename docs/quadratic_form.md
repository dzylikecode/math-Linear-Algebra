# 二次型

Quadratic form

## 矩阵表示

由 x 到 y 的 **线性替换**

$$
\begin{cases}
    x_1 = c_{11} y_1 + c_{12} y_2 + \cdots + c_{1n} y_n \\
    x_2 = c_{21} y_1 + c_{22} y_2 + \cdots + c_{2n} y_n \\
    \vdots \\
    x_n = c_{n1} y_1 + c_{n2} y_2 + \cdots + c_{nn} y_n \\
\end{cases}
$$

非退化的, 系数矩阵 $C$ 为**可逆矩阵**

$$X = CY$$

---

二次型矩阵:

$$A = A'$$

---

二次型与矩阵表示相互唯一确定

$$f(x_1, x_2, \cdots, x_n) = X' A X$$

---

考虑非退化的线性替换

$$X'AX=(CY)'A(CY)=Y'(C'AC)Y$$

设

$$B = C'AC$$

合并变换

有性质

$$B'=B$$

1. 自反性
2. 对称性: $A = (C^{-1})'A(C^{-1})$
3. 传递性

## 标准形

定理 1:

任何二次型都可以变成简单的平方和形式

$$d_1 x_1^2 + d_2 x_2^2 + \cdots + d_n x_n^2$$

解:

归纳法 + 主元法

1. 若$x_1^2$存在, 则直接主元配方
2. 若$x_1^2$不存在

   $$4x_1 x_2 = (x_1 + x_2)^2 - (x_1 - x_2)^2$$

   看作$y_1, y_2$, 于是回到了情况 1

---

定理 2: 定理 1 的矩阵描述

任意的对称矩阵都合同于对角矩阵

解:

情况 2:

$$
\begin{pmatrix}
    0 & a_{12} & \cdots & a_{1n} \\
    a_{12} & 0 & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & 0 \\
\end{pmatrix}
$$

通过

$$
C_1=
\begin{pmatrix}
    1 & 1 & 0 & \cdots & 0 \\
    1 & -1 & 0 &\cdots & 0 \\
    0 & 0 & 1 & \cdots & 0 \\
    \vdots & \vdots & \vdots& \ddots & \vdots \\
    0 & 0 & 0 & \cdots & 1 \\
\end{pmatrix}
$$
