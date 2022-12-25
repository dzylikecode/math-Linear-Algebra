# 线性空间

## 集合与映射

恒等映射, 单位映射: 记作$1_M$(在集合 M 上的)

---

映射的乘积

$$(\sigma \tau)(a) = \sigma(\tau (a) )$$

结合律:

$$(\phi \sigma)\tau = \phi(\sigma \tau)$$

解:

由定义可证, 均为$\phi(\sigma (\tau (a)))$

---

满射

单射

一一映射

逆映射

## 线性空间的定义与简单性质

线性空间的定义

加法:

1. 交换律
2. 结合律
3. $0+\alpha=\alpha$
4. $\alpha + \beta = 0$

数量乘法:

5. $1 \alpha = \alpha$
6. $k(l\alpha) = (kl)\alpha$

加法与数乘:

7. $(k+l)\alpha = k\alpha + l\alpha$
8. $k(\alpha + \beta) = k\alpha + k\beta$

---

线性空间的元素: 向量

线性空间也称: 向量空间

---

性质:

1. 零元素唯一

   利用$0+\alpha=\alpha$可证

2. 负元素唯一

   $$\beta = \beta + 0 = \beta + (\beta_1 + \alpha) = (\beta + \alpha) + \beta_1 = \beta_1$$

3. $0 \alpha = 0$

   $$0\alpha = (1-1)\alpha = \alpha - \alpha = 0$$

4. $k 0 = 0$

   $$k0 = k(\alpha-\alpha) = k\alpha - k\alpha = 0$$

5. $(-1)\alpha=-\alpha$

## 维数-基与坐标

n 维: 线性空间里的极大线性无关组

---

无限维: 无限多个线性无关向量

eg. 所有实系数多项式所构成的实线性空间

---

坐标:

$$\alpha = \sum_{i=1}^n a_i \epsilon_i$$

记为:

$$\alpha = (a_1, a_2, \cdots, a_n)$$

---

若线性空间$V$能被 n 个线性无关的向量线性表出, 则$V$为 n 维的, 且这 n 个向量为$V$的一个基

---

多项式的不同基:

1. 普通形式
2. 泰勒展开
3. 拉格朗日插值

---

复数是复数的一维空间, 是实数的二维空间

维数与考虑的数域有关

## 基变换与坐标变换

基的关系

$$\epsilon' = A \epsilon$$

不同坐标下的表示:

$$
\xi = x_1 \epsilon_1 + x_2 \epsilon_2 + \cdots + x_n \epsilon_n = x_1' \epsilon_1' + x_2' \epsilon_2' + \cdots + x_n' \epsilon_n'
$$

矩阵形式

$$x \epsilon = x' \epsilon'$$

代入基的关系, 得

$$x = x' A$$

故

$$x'= x A^{-1}$$

## 线性子空间

线性子空间$W$: 线性空间$V$的子集, 且构成线性空间

显然, 子集满足性质 1, 2, 5, 6, 7, 8

只需要考虑运算具有封闭性以及 3, 4:

而封闭性是包含 3, 4 的

若有$\alpha$, 则$k \alpha$存在, 特别的, 取$k=0, -1$

---

定理 2: $W$是线性空间$V$的子集, 且加法和数乘封闭, 则为线性子空间

---

零子空间

本身

以上两者称为 **平凡子空间**

其他称为 **非平凡子空间**

eg. 实系数多项式是实系数函数的一个线性子空间

---

齐次方程组的解构成一个线性子空间, 称为 **解空间**

n-r 维

---

$$k_1 \alpha_1 + k_2 \alpha_2 + \cdots + k_r \alpha_r$$

由$\alpha_1, \alpha_2, \cdots, \alpha_r$构成的线性子空间

记作:

$$L(\alpha_1, \alpha_2, \cdots, \alpha_r)$$

---

定理 3:

$$两个向量组生成的子空间相等 \Leftrightarrow 向量组等价$$

子空间的维数等于向量组的秩

---

子空间的基可以经过扩展成为原空间的基

## 子空间的交与和

交为子空间

矩阵描述:

$$
C =
\begin{pmatrix}
   A \\ B
\end{pmatrix}
$$

同时满足的解

---

和也为子空间

$$\alpha, \beta \in V_1 + V_2$$

则:

$$
\alpha = \alpha_1 + \alpha_2\\
\beta = \beta_1 + \beta_2
$$

特别的, 可以令$\alpha_2$为 0, 表示完全来自于$V_1$

> 和有并的意思

eg. 一个平面与一条垂直于平面的直线的和为整个三维空间

$$
L(\alpha_1, \alpha_2, \cdots, \alpha_s) + L(\beta_1, \beta_2, \cdots, \beta_t) \\
= L(\alpha_1, \alpha_2, \cdots, \alpha_s, \beta_1, \beta_2, \cdots, \beta_t)
$$

---

维数公式:

$$dim(W_1 \cap W_2) + dim(W_1 + W_2) = dim(W_1) + dim(W_2)$$

解:

即证明

$$dim(W_1 + W_2) = n_1+n_2 - m$$

设

$$W_1 \cap W_2 = L(\alpha_1, \alpha_2, \cdots, \alpha_m)$$

根据扩充定理:

$$W_1 = L(\alpha_1, \alpha_2, \cdots, \alpha_m, \beta_1, \beta_2, \cdots, \beta_{n_1- m})$$

$$W_2 = L(\alpha_1, \alpha_2, \cdots, \alpha_m, \gamma_1, \gamma_2, \cdots, \gamma_{n_2- m})$$

则:

$$W_1 + W_2 = L(\alpha_1, \alpha_2, \cdots, \alpha_m, \beta_1, \beta_2, \cdots, \beta_{n_1- m}, \gamma_1, \gamma_2, \cdots, \gamma_{n_2- m})$$

只需证明: $\alpha_1, \alpha_2, \cdots, \alpha_m, \beta_1, \beta_2, \cdots, \beta_{n_1- m}, \gamma_1, \gamma_2, \cdots, \gamma_{n_2- m}$线性无关
