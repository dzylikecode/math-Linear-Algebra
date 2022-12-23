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
A =
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

则:

$$
B = C_1'AC_1 =
\begin{pmatrix}
    2 a_{12} & 0 \\
    0 & -2 a_{12}
\end{pmatrix}
$$

> 可见习题的 python 计算结果

将情况 2, 化归为情况 1

对于情况 1:

运用分块矩阵

$$A = \begin{pmatrix} a & \alpha \\ \alpha' & A_1 \end{pmatrix}$$

取

$$
C_1 =
\begin{pmatrix} 1 & -a^{-1}\alpha' \\ 0 & E \end{pmatrix}
$$

则

$$
B = C_1'AC_1 =
\begin{pmatrix}
    a & 0 \\
    0 & A_1 - a^{-1} \alpha' \alpha
\end{pmatrix}
$$

满足递归性

## 唯一性

对角阵的非零元素的个数是唯一确定的, 但是系数不是唯一确定的

---

规范形

---

复数域的规范形:

$$z_1^2 + z_2^2 + \cdots + z_r^2$$

---

实数域的规范形:

$$x_1^2 + x_2^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_r^2$$

有$r, p$唯一确定

---

惯性定理:

$$r, p唯一确定$$

解:

反证法

设

$$f(x_1, x_2, \cdots, x_n) = y_1^2 + y_2^2 + \cdots + y_p^2 - y_{p+1}^2 - \cdots - y_n^2$$

$$f(x_1, x_2, \cdots, x_n) = z_1^2 + z_2^2 + \cdots + z_q^2 - z_{q+1}^2 - \cdots - z_n^2$$

知:

$$y_1^2 + y_2^2 + \cdots + y_p^2 - y_{p+1}^2 - \cdots - y_n^2 = z_1^2 + z_2^2 + \cdots + z_q^2 - z_{q+1}^2 - \cdots - z_n^2$$

不妨设

$$p > q$$

取$y_{p+1}, \cdots, y_n$和$z_1, \cdots, z_q$为 0, 其他存在非零, 即矛盾

注意到

$$CZ=BY \Rightarrow Z=C^{-1}BY$$

满足上述条件, 即

$$
\begin{cases}
    z_1 = g_{11} y_1 + g_{12} y_2 + \cdots + g_{1n} y_n = 0 \\
    z_2 = g_{21} y_1 + g_{22} y_2 + \cdots + g_{2n} y_n = 0 \\
    \vdots \\
    z_q = g_{q1} y_1 + g_{q2} y_2 + \cdots + g_{qn} y_n = 0 \\
    y_{p+1} = 0 \\
    \vdots \\
    y_n = 0
\end{cases}
$$

共$q+n-p=n-(p-q) < n$个, 存在非零解, 得证

---

正惯性指数:p

负惯性指数:r-p

符号差:$p-(r-p) = 2p-r$

## 正定

对任意不全为 0, 都有

$$f > 0$$

即

$$p=r=n$$

也即合同于$E$

---

正定矩阵

$$|A| > 0$$

解:

$$|A|=|C'C|=|C|^2 > 0$$

---

$$ A 正定 \Leftrightarrow \forall A 的主子式 >0$$

解:

必要性:

A 正定

而 k 阶主子式, 即

$$f(c_1, c_2, \cdots, c_k, 0, \cdots, 0) > 0$$

充分性:

归纳法

$$A = \begin{pmatrix} A_1 & \alpha \\ \alpha' & a \end{pmatrix}$$

则:

取

$$C_1 = \begin{pmatrix} G & 0 \\ 0 & 1 \end{pmatrix}$$

则:

$$
C_1'AC_1 = \begin{pmatrix}
    E & G' \alpha \\
    \alpha'G & a
\end{pmatrix}
$$

取

$$
C_2=
\begin{pmatrix}
    1 & -\alpha'G \\
    0 & E
\end{pmatrix}
$$

则:

$$
C_2'C_1'AC_1C_2 =
\begin{pmatrix}
    E & 0 \\
    0 & E - \alpha'GG'\alpha
\end{pmatrix}
$$

两边同时取行列式

$$|E-\alpha'GG'\alpha|=|C'AC|=|C|^2|A| >0$$

即矩阵为正定的

---

负定的

半正定的: $f \geq 0$

---

以下条件等价:

1. 半正定
2. $r=p$
3. 合同于非负对角阵
4. $A=C'C$($C$ 不一定可逆)
5. 所有主子式非负
