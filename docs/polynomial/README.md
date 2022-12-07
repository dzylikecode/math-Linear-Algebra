# 多项式

Polynomial

## 数域

数的概念不断扩展

$$i = \sqrt{-1}$$

$$
a + bi = \begin{bmatrix}
a & -b \\
b & a
\end{bmatrix}
$$

> 反映了人们对客观世界的认识不断加深

一元二次方程是否有解就与未知量所代表的对象有关, 也就是与未知量允许的取值范围有关

- 封闭

  如果数的集合 P 中任意两个数做某一运算的结果仍在 P 中, 我们就说数集 p 对这个运算是 `封闭的`

- 数域

  如果一个包含 0,1 在内的数集 P 对于加法、减法、乘法与除法(除数不为 0)是封闭的, 那么 p 就称为一个数域.

  > 显然, 包含有理数

  由此, 可以用矩阵构建数域

## 一元多项式

!> 数域 P 上的一元多项式, 指的是系数全属于 P, 与符号 x 无关, **只与系数有关**

所有的系数的一元多项式全体构成`多项式环`, `P[x]`

---

多项式里面的卷积结构:

$$f(x) \cdot g(x) = \sum_{s=0}^{n+m}(\sum_{i+j=s} a_i b_j) x^s$$

其中, $\sum_{i+j=s} a_i b_j$和卷积很相似

$$a_s b_0 + a_{s-1} b_1 + \cdots + a_1 b_{s-1} + a_0 b_s = \sum_{i+j=s} a_i b_j$$

恰好与$i+j=s$的整数(非负)分解相映射

## 整除的概念

带余除法的证明:

1. 归纳证明存在性
2. 反正存在多个矛盾, 证明唯一性

> 这样的分解清晰

$$(q(x) - q^{\prime}(x))g(x) = r^{\prime}(x) - r(x)$$

观察次数, 非常巧妙

$$\partial(q(x) - q^{\prime}(x)) + \partial(g(x)) = \partial(r^{\prime}(x) - r(x))$$

$$\partial(g(x)) > \partial(r^{\prime}(x) - r(x))$$

矛盾, 得证

对于整数带余除法, 就是对次数进行抽象把握. 或者应该对比较`>`这层次进一步思考, 如$(a-a')b= r'-r$. 从程序角度, 就是对$\partial$函数进行多态处理

---

次数的妙用

$$
h_1(x)h_2(x)=1\\
\Rightarrow \partial(h_1(x)) + \partial(h_2(x)) = 0 \\
\Rightarrow \partial(h_1(x)) = \partial(h_2(x)) = 0
$$

---

!> $g(x) | f(x)$ 是 $f(x) = g(x) h(x)$的简记形式, 故$g(x)=0$是可行的, 而带余除法不行

---

两个多项式之间的整除关系不会因为数域的扩大而改变

## 最大公因式

辗转相除

使用矩阵容易计算和理解

引理说明: 公因式是可以传递的, 状态转移

$$(f(x), g(x)) = (g(x), r(x))$$

使用矩阵描述这段变换

$$
(f, g) = (r, g) \begin{pmatrix}
1 & 0 \\
q & 1
\end{pmatrix}
$$

简记

$$
\begin{cases}
  r_0=r_1 A_1\\
  d(r_0) = d(r_1)
\end{cases}
$$

根据对次数的严格递减, 可以得到

$$r_n = (r_n(x), 0) = r_n(x)$$

此时

$$
\begin{cases}
  r_0=r_n A_n \cdots A_1 = (r_n(x), 0) A\\
  d(r_0) = d(r_n) = r_n(x)
\end{cases}
$$

A 是初等矩阵的乘积, 必然是可逆的

可得

$$
\begin{aligned}
(r_n(x), 0) &= r_0(x) A^{-1} = (f, g) A^{-1} \\
&= (f, g) \begin{pmatrix}
u & m \\
v & n
\end{pmatrix} \\
&= (u \cdot f + v \cdot g, m \cdot f + n \cdot g)
\end{aligned}
$$

即

$$d = u \cdot f + v \cdot g$$

> 计算的时候也可以通过矩阵来计算, 方便理解

---

更一般的, 考虑多个多项式的最大公因式

$$(f_1, f_2, \cdots, f_n) = (r_n, 0, \cdots, 0) = r_n$$

而, $A$仍然是初等矩阵变换, 与$c_i - k \cdot c_j$ ($c$代表矩阵的列)同构, 即线性变换

与矩阵的秩有关

也就是说明, 多项式的最大公因式在揭示向量相似于$(0, 0, \cdots, 0, r_n)$

---

互素, 即$(f, g)$相似于$(0, 1)$

---

定理 4: 如果$(f(x), g(x)) = 1$, 且$f(x)|g(x)h(x)$, 那么

$$f(x) | h(x)$$

证明:

观察 $f(x) | h(x) = 1 \cdot h(x) = (f, g) \cdot h = (f \cdot h, g \cdot h)$,

等价于证明

$$
\begin{cases}
f | g \cdot h \\
f | f \cdot h
\end{cases}
$$

或者观察

$$u \cdot f + v \cdot g = 1$$

$$u \cdot f \cdot h + v \cdot g \cdot h = h$$

左右两边同时被$f$整除, 得证

## 因式分解定理

## reference

- Polynomial. (2022, October 27). In Wikipedia. https://en.wikipedia.org/wiki/Polynomial
