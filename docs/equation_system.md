# 线性方程组

linear system of equation

## 消元法

求解: 是求出解的集合

同解: 两个方程组的解的集合相同

---

消元法, 由三个基本的变换构成:

1. $x = k \times x$
2. $x = x + k \times y$
3. $x \leftrightarrow y$ :交换方程组

定义为**初等变换**

---

证明: 初等变换是把方程组变成同解的方程组

解:

利用

$$
\begin{cases}
    x \rightarrow y \\
    y \rightarrow x
\end{cases}
\Rightarrow x \leftrightarrow y
$$

只需要证明: 变换前的解也是变换后的解, 反之亦如此

---

消元法的目的是变成阶梯形矩阵, 保证同解

矩阵的秩$r$: 阶梯形矩阵的层数

- 若出现$0=d_{r+1}$

  无解

- 否则, 若$r=n$

  唯一的一解, 一直从简单方程回代即可

- 否则, $r < n$

  无穷解

  $$
  \begin{cases}
      &c_{11}x_1 &+ &c_{12}x_2 &+ &\cdots &+ &c_{1n}x_n = d_1 - c_{1,r+1}x_{r+1} - \cdots - c_{1n}x_n\\
      &          &  &c_{22}x_2 &+ &\cdots &+ &c_{2n}x_n = d_2 - c_{2,r+1}x_{r+1} - \cdots - c_{2n}x_n\\
      &          &  &          &  &       &  &\vdots                                                 \\
      &          &  &          &  &       &  &c_{rr}x_r = d_r - c_{r,r+1}x_{r+1} - \cdots - c_{rn}x_n
  \end{cases}
  $$

  用$(x_{r+1}, \cdots, x_{n})$表示$(x_1, \cdots, x_r)$, 称为**一般解**

  $(x_{r+1}, \cdots, x_{n})$: 自由未知量
