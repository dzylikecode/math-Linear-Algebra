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

$$P[x] = \{a_n x^n + \cdots + a_0 | a_0, \cdots, a_n \in P \}$$

有点类似于$a + b \sqrt{2}$构造的数域

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

是否能分解与数域相关

---

不可约多项式, 与其他多项式的关系只有两种: 互素或者整除

---

因式分解唯一定理

局限性: 没有给出具体的分解方法

---

标准分解式

$$
f(x) = c\prod_{i=1}^n p_i(x)^{r_i}
$$

其中$p_i(x)$的首项系数为 1

- 方便写出公因式

## 重因式

个人觉得核心是:

$$ (p(x), p^{\prime}(x)) = 1 $$

---

去除重因式

$$
\frac {f(x)} {(f(x), f^{\prime}(x))} = c \prod_{i=1}^n p_i(x)
$$

## 多项式函数

之前是纯形式的角度(即看作形式的表达式), 现在考虑函数的角度

可以证明形式的与函数的是等价的

> n 次多项式的函数的根不超过 n 个

## 复系数与实系数的因式分解

代数基本定理

$$f(x) = c \prod_{i=1}^n (x - r_i)$$

---

实系数多项式的复数根形成共轭对

$$f(x) = c \prod_{i=1}^n (x - r_i)\prod_{j=1}^m(x^2 + p_j x + q_j)$$

其中, ${p_j}^2 - 4 q_j < 0$

## 有理系数多项式

1. 可以归结为整系数多项式
2. 有任意次数的不可约多项式

---

本原多项式

高斯引理:

$$本原 \times 本原 = 本原$$

证明:

反证法, 存在公共因子$p$, 考察每项系数

$$d_{k} = \sum_{i=0}^k a_i \cdot b_{k-i}$$

考虑 $d_0 = a_0 \cdot b_0$, 则有 $p | a_0$或者$p | b_0$

需要考虑, p 与$a_i, b_j$的关系, 不妨规范为:

$a_i$与$b_j$是$p$第一个不能整除的

$$
d_{i+j} = a_i b_j + \sum_{k=0}^{i-1} a_k \cdot b_{i+j-k} + \sum_{k=0}^{j-1} a_{i+j-k} \cdot b_k
$$

> 还是惊叹这样的理解$d_{k}$, 如此巧妙地分割出结构

---

定理 11:

若

$$整 = 有理 \times 有理$$

必存在

$$ 整 = 整 \times 整$$

可以用高斯引理来证明

---

定理 11 推论:

$$整 = \frac {整} {本原}$$

证明与上面相似

---

若$\frac {r} {s}$是$f(x)$的有理根, 其中$(r,s)=1$, 则$s | a_n, r | a_0$

利用推论:

$$(x-\frac {r} {s}) \Rightarrow (sx -r)$$

因此, 可以通过枚举$a_n$和$a_0$的因子来测试有理根

---

艾森斯坦(Eisenstein)判别法

证明:

类似高斯引理

## 多元多项式

n 元多项式环, 环(ring) 一种抽象代数结构

---

字典排序法, 排列多项式

观察次数, 考虑$(k_1, \cdots, k_n)$

感觉:递归的主元法

好处: $\partial h = \partial f \cdot \partial g$, 首项等于分别的首项相乘

$$首项 = 首项 \times 首项$$

---

齐次多项式, $f_i$是次数为$i$的齐次多项式

于是一般的多元多项式可以看作

$$f = \sum_{i=0}^n f_i$$

同样有类似于卷积的结构

$$
h = f \cdot g \\
\Rightarrow h_k = \sum_{i+j=k} f_i \cdot g_{j}
$$

## 对称多项式

韦达定理: 系数对称地依赖方程的根, 称为**初等对称多项式**

观察次数, 则可以看到与组合数$C_n^k$的映射

$$\sigma_k = C_n^k$$

---

$$f(x_1, x_2, \cdots, x_n) = \varphi(\sigma_1, \sigma_2, \cdots, \sigma_n)$$

证明核心: 递归降次+$首项 \times 首项 = 首项$

$$
\begin{aligned}
  a x_1^{l_1} \cdots x_i^{l_i} \cdots x_n^{l_n} &= a (x_1)^{l_1-l_2}(x_1 x_2)^{l_2-l_3} \cdots (x_1 x_2 \cdots x_n)^{l_n} \\
  &= \partial (a \sigma_1^{l_1-l_2} \sigma_2^{l_2-l_3} \cdots \sigma_n^{l_n})
\end{aligned}
$$

还可以证明是唯一确定的

称为**对称多项式基本定理**

---

一元多项式的判别式, 可以用来判断是否有重根

$$D = \prod_{i<j}(x_i-x_j)^2$$

由韦达定理和对称多项式基本定理:

$$D(a_1, \cdots, a_n) = D$$

判断重根的充要条件

## reference

- Polynomial. (2022, October 27). In Wikipedia. https://en.wikipedia.org/wiki/Polynomial
- [抽象代数|笔记整理（6）——环，多项式环，理想](https://zhuanlan.zhihu.com/p/31441459)
