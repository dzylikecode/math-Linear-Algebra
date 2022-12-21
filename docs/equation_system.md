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

---

齐次方程的个数$s$

当$ s \leq n$时, 必有非零解

---

增广矩阵

$$
\begin{bmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
    a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
    \vdots & \vdots & \ddots & \vdots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn} & b_n
\end{bmatrix}
$$

即

$$(A, b)$$

与线性方程组对应, 转化阶梯形的过程是等价的

## n-维向量空间

向量可以表达状态, 像物体的位置坐标

想到傅里叶变换也可以分解一个个简单的正弦

---

向量的运算

## 线性相关性

研究向量的关系:

成比例

$$\vec \alpha = k \vec \beta$$

线性组合:

$$\vec \alpha = k_1 \vec \alpha_1 + k_2 \vec \alpha_2 + \cdots + k_n \vec \alpha_n$$

> 想到用坐标系, 基的方式去理解, 本就是借助了更为高级的抽象, 没必要去纠结用更为基本的, 已知的, 低级的概念. 直接接受高级的概念

---

$\varepsilon$: 单位向量

0 向量任意向量组的线性组合

---

线性表出: 一组向量能完全由另一组向量表示

等价: 相互线性表出

---

线性表出的传递性

若:

$$\vec \alpha_i = \sum_{j=1}^s k_{ij} \vec \beta_j$$

$$\vec \beta_j = \sum_{m=1}^p k_{jm} \vec \gamma_m$$

则

$$
\begin{aligned}
  \vec \alpha_i &= \sum_{j=1}^s k_{ij} \sum_{m=1}^p k_{jm} \vec \gamma_m \\
  &= \sum_{m=1}^p (\sum_{j=1}^s k_{ij} k_{jm}) \vec \gamma_m
\end{aligned}
$$

> 可以看到矩阵的乘法

宏观考虑, 用矩阵思考

$$
\begin{aligned}
  \alpha &= A \beta \\
  \beta &= B \gamma \\
  \Rightarrow \alpha &= A B \gamma
\end{aligned}
$$

---

自反性

对称性

传递性

---

线性相关:

- 定义 1

  一个向量能被其他向量线性表出

- 定义 2

  存在不全为 0 的系数, 使得

  $$k_1 \vec \alpha_1 + k_2 \vec \alpha_2 + \cdots + k_n \vec \alpha_n = 0$$

几何含义: 共线或者共面

---

线性无关

---

部分线性相关 => 整体线性相关

整体线性无关 => (非空)部分线性无关

---

一维的线性相关: 必是 0 向量

单位向量线性无关

---

判定线性相关还是无关, 归结为解线性方程组的问题

$$x_1 \vec \alpha_1 + x_2 \vec \alpha_2 + \cdots + x_n \vec \alpha_n = 0$$

---

n 维向量线性无关, 则在此基础上添加一个维度的 n+1 维向量也是线性无关的

用方程组解释: n 组方程有唯一的一解, 则在此基础上添加的一个方程也只有一解

---

设

1. $\alpha_r$的向量组可以由$\beta_s$线性表出
2. r > s

则 $\alpha_r$向量组线性相关

解:

线性相关等价于

$$x \alpha = 0$$

存在非零解

又因为

$$\alpha = A \beta$$

即

$$x \alpha = x A \beta = 0$$

有非零解

又因为, $\beta$线性无关

即

$$x A = 0$$

有非零解

其中,

$$
\begin{aligned}
  x &: r \\
  A &: r \times s
\end{aligned}
$$

考虑:

$$A^T x = 0$$

有非零解

---

推论 1:

设 $\alpha_r$的向量组可以由$\beta_s$线性表出, 且 $\alpha_r$向量组线性无关, 则 $r \leq s$

---

推论 2:

n+1 个 n 维向量必定线性相关

---

推论 3:

等价的线性无关组, 必有$r=s$

证明:

仍然采用$r \leq s, s \leq r$的思路

---

> 对于以上的定理和推论, 可以更为抽象地概括为: n+1 维空间的基不能由 n 维空间的基表示, 否则该空间坍缩

---

极大线性无关组: 添加任意一个都将线性相关

基本性质: 与向量组本身等价

---

由推论 3: 一组向量组的极大线性无关组(可能有很多组)含有相同个数的向量

将个数定义为 **秩**

> 有种"千山鸟飞绝"的意境, 寥寥寒鸦飞过后, 引导我看到是背后一直存在, 此刻却是分外深远的天空

---

放入到方程组中观察:

用行向量来观看

线性组合不会改变方程的解

向量等价, 即两个方程组同解

## 矩阵的秩

行秩

列秩

---

引理

行秩$r \leq n$, 则有非零解

解:

向量与方程组对应,

考虑向量组, 等价于考虑极大线性无关组

对应的就是考虑同解的方程组

$$
\begin{cases}
  a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n = 0 \\
  a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n = 0 \\
  \vdots \\
  a_{r1} x_1 + a_{r2} x_2 + \cdots + a_{rn} x_n = 0
\end{cases}
$$

显然, 有非零解

---

行秩$r$和列秩$c$相等

解:

核心:

1. 如何用行向量, 列向量的角度观看

   行向量:

   $$\alpha = (a_{11}, a_{12}, \cdots, a_{1n}, 0)$$

   方程同解

   列向量:

   $$x_1 \vec \beta_1 + x_2 \vec \beta_2 + \cdots + x_n \vec \beta_n = 0$$

2. 如何将行列向量转化

   $$x_1 \vec \beta_1 + x_2 \vec \beta_2 + \cdots + x_n \vec \beta_n = 0$$

   与线性无关关联

3. 单射证明的思路

首先证明:

$$r \leq c$$

去除 r 个线性无关的行向量, 则有

$$x_1 \vec \alpha_1 + x_2 \vec \alpha_2 + \cdots + x_r \vec \alpha_r = 0$$

有唯一的零解, 对应的方程组:

$$
\begin{cases}
  a_{11} x_1 + a_{21} x_2 + \cdots + a_{r1} x_r = 0 \\
  a_{12} x_1 + a_{22} x_2 + \cdots + a_{r2} x_r = 0 \\
  \vdots \\
  a_{1n} x_1 + a_{2n} x_2 + \cdots + a_{rn} x_r = 0
\end{cases}
$$

此时将行向量转化为列向量, 列向量转化为了行向量

考虑此时的行向量, 由引理:

$$r' \geq r$$

取出$r'$个行向量, 不妨为

$$
\begin{cases}
  (a_{11}, a_{21}, \cdots, a_{r1}) \\
  (a_{12}, a_{22}, \cdots, a_{r2}) \\
  \vdots \\
  (a_{1, r'}, a_{2, r'}, \cdots, a_{r, r'})
\end{cases}
$$

扩展为

$$
\begin{cases}
  (a_{11}, a_{21}, \cdots, a_{n1}) \\
  (a_{12}, a_{22}, \cdots, a_{n2}) \\
  \vdots \\
  (a_{1, r'}, a_{2, r'}, \cdots, a_{n, r'})
\end{cases}
$$

仍然线性无关, 而此为列向量的部分向量组

故有

$$r \leq r' \leq c$$

---

$$D=0 \Leftrightarrow r < n$$

解:

数学归纳法

---

$$D=0 \Leftrightarrow r < n \Leftrightarrow 有非零解$$

解:

引用克拉默法则 => 唯一的一解

---

$$
\begin{cases}
  r(A) \geq r \Leftrightarrow \exists r级子式 \ne 0 \\
  r(A) \leq r \Leftrightarrow \forall r+1级子式=0
\end{cases}
$$

解:

$$r(A) \geq r \Rightarrow \exists r级子式 \ne 0$$

取出 r 个线性无关的行向量, 组成方程组

由于行秩等于列秩, 继而可以在方程组中取出 r 个 r 维的列向量线性无关

此时构成的 r 级子式不为 0

$$r(A) \leq r \Rightarrow \forall r+1级子式=0$$

取任意 r+1 个向量都线性相关, 由 n 维变成 r+1 维, 仍然线性相关

此时任意 r+1 级子式都为 0

$$r(A) \geq r \Leftarrow \exists r级子式 \ne 0$$

$$r(A) \leq r \Rightarrow \forall r+1级子式=0$$

利用上面反证:

由行列式的展开, 理解到:

$$\forall r = 0 \Rightarrow \forall r+1=0$$

> 这说明, $\forall r+1=0$ 本身有种$\leq$的意味在里面

---

初等变换$\Leftrightarrow$方程同解$\Leftrightarrow$向量等价

说明, 初等变换不改变秩

## 有解判别定理

向量形式:

$$x_1 \alpha_1 + x_2 \alpha_2 + \cdots + x_n \alpha_n = \beta \Leftrightarrow 有解$$

即: 有解等价于 $\beta$ 可由 $\alpha_1, \alpha_2, \cdots, \alpha_n$ 线性表出

用秩的观点来看:

$$r(\alpha_1, \alpha_2, \cdots, \alpha_n) = r(\alpha_1, \alpha_2, \cdots, \alpha_n, \beta) \Leftrightarrow 有解$$

解:

必要性:

$$r(\alpha_1, \alpha_2, \cdots, \alpha_n) = r(\alpha_1, \alpha_2, \cdots, \alpha_n, \beta)\Leftarrow 有解$$

有解, 即 $\beta$ 可由 $\alpha_1, \alpha_2, \cdots, \alpha_n$ 线性表出

可得 $\alpha_1, \alpha_2, \cdots, \alpha_n$与$\alpha_1, \alpha_2, \cdots, \alpha_n, \beta$等价, 则秩相等

充分性:

$$r(\alpha_1, \alpha_2, \cdots, \alpha_n) = r(\alpha_1, \alpha_2, \cdots, \alpha_n, \beta)\Rightarrow 有解$$

设$\alpha_1, \alpha_2, \cdots, \alpha_r$是$\alpha_1, \alpha_2, \cdots, \alpha_n$的极大线性无关组

易知, 是$\alpha_1, \alpha_2, \cdots, \alpha_n, \beta$的线性无关组

又因为个数为 r 个, 则为其极大线性无关组

故$\beta$能被其线性表出

---

用增广矩阵$\overline{A}$描述即

$$r(\overline{A})=r(A)$$

用消元法也可以证明

---

$$
\begin{cases}
    c_{11}x_1 + c_{12}x_2 + \cdots + c_{1n}x_n = d_1 - c_{1,r+1}x_{r+1} - \cdots - c_{1n}x_n\\
    c_{21}x_1 + c_{22}x_2 + \cdots + c_{2n}x_n = d_2 - c_{2,r+1}x_{r+1} - \cdots - c_{2n}x_n\\
    \vdots\\
    c_{r1}x_1 + c_{r2}x_2 + \cdots + c_{rn}x_n = d_r - c_{r,r+1}x_{r+1} - \cdots - c_{rn}x_n\\
\end{cases}
$$

将右边看作向量, 可用克拉默法来解

显然解就是向量形式

## 解的结构
