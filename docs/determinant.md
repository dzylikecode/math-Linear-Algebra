# Determinant

行列式

## 排列

逆序

考虑每一对数, 共有 $C_n^2$ 对, 如果前面的数大于后面的数, 则称为逆序.

---

逆序数

逆序的个数

符号:

$$\tau(j_1 j_2 \cdots j_n)$$

---

偶排列

奇排列

---

### 对换

将其中两个数的位置进行互换

---

对换改变奇偶性

证明:

考虑最简单的情形:

$$\cdots j k \cdots$$

易知, 奇偶性变化

考虑一般的情形:

$$\cdots j i_1 \cdots i_s k \cdots$$

- 直接计算

  先进行$s+1$次对换

  $$\cdots k j i_1 \cdots i_s \cdots$$

  然后进行$s$次对换

  $$\cdots k i_1 \cdots i_s j \cdots$$

  共$2s+1$次对换, 奇偶性变化

- 递归

  先用简单的情形:

  $$\cdots j i_1 \cdots i_{s-1} k i_s \cdots$$

  1. 奇偶性变化

  然后使用$s-1$的情形:

  $$\cdots k i_1 \cdots i_{s-1} j i_s \cdots$$

  2. 奇偶性变化

  最后再使用简单的情形:

  $$\cdots k i_1 \cdots i_{s-1} i_s j \cdots$$

  3. 奇偶性变化

  共 3 次奇偶性变化, 奇偶性变化

> 递归的方法, 很有函数式编程的影子, 新的函数尽可能用已有的函数来组合, 高级的抽象由基本的抽象组合而成.

这个定理, 说明了考量逆序数的奇偶性, 可以转变为考量对换次数的奇偶性

---

奇排列与偶排列的个数相等, 均为 $\frac {1} {2} n!$

证明:

设奇排列的个数为 $s$, 偶排列的个数为 $t$

利用单射

将奇排列的前两个数对换, 变为偶排列, 可证明是单射

$$ s \leq t$$

同理

$$ t \leq s$$

故

$$s = t = \frac {1} {2} (s+t) = \frac {1} {2} n!$$

### n-级行列式

$$
\begin {aligned}
\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{vmatrix}
&=\sum_{j_1 j_2 \cdots j_n} (-1)^{\tau (j_1 j_2 \cdots j_n) } a_{1 j_1} a_{2 j_2} \cdots a_{n j_n} \\
&=\sum (-1)^{\tau (i_1 i_2 \cdots i_n) + \tau (j_1 j_2 \cdots j_n) } a_{i_1 j_1} a_{i_2 j_2} \cdots a_{i_n j_n}
\end{aligned}
$$

第二种形式更为对称, 对换后, $-1$ 的次数的奇偶性不变

---

性质 1:

由第二种形式容易证明: 行列式转置后, 值不变

说明的行和列的地位是对称的

## n-级行列式的性质

由定义式入手:

对确定的一行而言, 每一项都含有这一行的唯一的一个元素, 因此可以将展开式划分为 $n$ 个部分

$$
\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{vmatrix} = a_{i 1} A_{i 1} + a_{i 2} A_{i 2} + \cdots + a_{i n} A_{i n}
$$

其中 $A_{i_j}$ 是与 $a_{i_j}$ 无关

> 从左往右是展开, 从右往左是合并

非常容易证明以下性质

---

性质 2:

$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
k a_{i1} & k a_{i2} & \cdots & k a_{in} \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} = k
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
a_{i1} & a_{i2} & \cdots & a_{in} \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}
$$

记作:

$$ r_i(k) = k r_i $$

---

性质 3:

$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
b_1 + c_1 & b_2 + c_2 & \cdots & b_n + c_n \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} =
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
b_1 & b_2 & \cdots & b_n \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} +
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
c_1 & c_2 & \cdots & c_n \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}
$$

记作:

$$ r_i(\vec b + \vec c) = r_i(\vec b) + r_i(\vec c) $$

---

性质 7:

交换行列式中的两行, 行列式符号相反

证明: 对每一项进行对换操作, 符号相反

> 对排列的对换, 变成了对行列式的行交换. 一个是微观形式, 一个是宏观表现

记作:

$$r_{ij} = - r_{ji}$$

---

性质 4:

行列式中两行相同, 行列式$D = 0$

证明: 交互相同的两行, 行列式的值符号改变, 而交换相同两行, 行列式不变, 即

$$D = - D$$

记作:

$$
\begin{cases}
\vec a_i = \vec a_j \\
r(\vec a_i, \vec a_j) = 0 \\
\end{cases}
$$

---

性质 5:

行列式中两行成比例(线性相关), 行列式$D = 0$

证明:

由性质 2 和性质 4 得证

记作:

$$
\begin{cases}
\vec a_i = k \vec a_j \\
r(\vec a_i, \vec a_j) = 0 \\
\end{cases}
$$

---

性质 6:

把行列式某一行加上另一行的倍数, 行列式不变

记作:

$$
r(\vec a_i + k \vec a_j, \vec a_j) = r(\vec a_i, \vec a_j)
$$

## 行列式的计算

矩阵的初等行变换

1. 性质 2: $\vec a_i = k \vec a_i$
2. 性质 6: $\vec a_i = \vec a_i + k \vec a_j$
3. 性质 7: $\vec a_i \leftrightarrow \vec a_j$(交换两行)

---

通过初等变换, 变成阶梯形矩阵

## 按行展开

$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
a_{i1} & a_{i2} & \cdots & a_{in} \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} =
a_{i1} A_{i1} + a_{i2} A_{i2} + \cdots + a_{in} A_{in}
$$

研究 $A_{i1}, A_{i2}, \cdots, A_{in}$的结构

---

余子式: 除去第 $i$ 行和第 $j$ 列的行列式

$$
M_{ij} = \begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots & \vdots &        & \vdots \\
a_{i-1,1} & a_{i-1,2} & \cdots & a_{i-1,j-1} & a_{i-1,j+1} & \cdots & a_{i-1,n} \\
a_{i+1,1} & a_{i+1,2} & \cdots & a_{i+1,j-1} & a_{i+1,j+1} & \cdots & a_{i+1,n} \\
\vdots & \vdots &        & \vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{nn}
\end{vmatrix}
$$

---

引理:

$$
\begin{vmatrix}
A & \vec a \\
0 & 1
\end{vmatrix} = A
$$

解:

由行列式定义式, 得证

---

证明:

$$A_{ij} = (-1)^{i+j} M_{ij}$$

解:

由性质 3:

$$
\begin {aligned}
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
a_{i1} & a_{i2} & \cdots & a_{in} \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} &=
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
a_{i1} & 0 & \cdots & 0 \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} + \cdots +
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
0 & 0 & \cdots & a_{in} \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} \\
&= a_{i1}
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
1 & 0 & \cdots & 0 \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} + \cdots +
a_{in}
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots &        & \vdots \\
0 & 0 & \cdots & 1 \\
\vdots & \vdots &        & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix} \\
&= a_{i1} A_{i1} + \cdots + a_{in} A_{in}
\end{aligned}
$$

可得:

$$
\begin {aligned}
A_{ij} &=
\begin{vmatrix}
a_{1,1} & \cdots & a_{1,j-1} & a_{1,j} & a_{1,j+1} & \cdots & a_{1n} \\
\vdots &        &   \vdots  & \vdots  & \vdots    &        & \vdots \\
a_{i-1,1} & \cdots & a_{i-1,j-1} & a_{i-1,j} & a_{i-1,j+1} & \cdots & a_{i-1,n} \\
0 & \cdots & 0 & 1 & 0 & \cdots & 0 \\
a_{i+1,1} & \cdots & a_{i+1,j-1} & a_{i+1,j} & a_{i+1,j+1} & \cdots & a_{i+1,n} \\
\vdots &        &   \vdots  & \vdots  & \vdots    &        & \vdots \\
a_{n,1} & \cdots & a_{n,j-1} & a_{n,j} & a_{n,j+1} & \cdots & a_{n,n}
\end{vmatrix} \\
&= (-1)^{n-i}
\begin{vmatrix}
a_{1,1} & \cdots & a_{1,j-1} & a_{1,j} & a_{1,j+1} & \cdots & a_{1n} \\
\vdots &        &   \vdots  & \vdots  & \vdots    &        & \vdots \\
a_{i-1,1} & \cdots & a_{i-1,j-1} & a_{i-1,j} & a_{i-1,j+1} & \cdots & a_{i-1,n} \\
a_{i+1,1} & \cdots & a_{i+1,j-1} & a_{i+1,j} & a_{i+1,j+1} & \cdots & a_{i+1,n} \\
\vdots &        &   \vdots  & \vdots  & \vdots    &        & \vdots \\
a_{n,1} & \cdots & a_{n,j-1} & a_{n,j} & a_{n,j+1} & \cdots & a_{n,n} \\
0 & \cdots & 0 & 1 & 0 & \cdots & 0 \\
\end{vmatrix} \\
&= (-1)^{n-i + n-j}
\begin{vmatrix}
a_{1,1} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n} & a_{1,j}\\
\vdots  &        &   \vdots  & \vdots    &        & \vdots & \vdots\\
a_{i-1,1} & \cdots & a_{i-1,j-1} & a_{i-1,j+1} & \cdots & a_{i-1,n} & a_{i-1,j} \\
a_{i+1,1} & \cdots & a_{i+1,j-1} & a_{i+1,j+1} & \cdots & a_{i+1,n} & a_{i+1,j} \\
\vdots   &         & \vdots     & \vdots      &       & \vdots  & \vdots\\
a_{n,1} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{n,n} & a_{n,j}\\
0 & \cdots & 0 & 0 & \cdots & 0 & 1\\
\end{vmatrix} \\
&= (-1)^{2n-i-j} M_{ij}\\
&= (-1)^{i+j} M_{ij}
\end{aligned}
$$

称$A_{ij}$为代数余子式

---

结合性质 4，可得：

$$
a_{k1} A_{i1} + \cdots + a_{kn} A_{in} =
\begin{cases}
d, & k = i \\
0, & k \neq i
\end{cases}
$$

向量形式

$$
\vec{a_k} \cdot \vec{A_i} = \begin{cases}
d, & k = i \\
0, & k \neq i
\end{cases}
$$

---

$n=3$时, 有几何意义:

$$
A =
\begin{pmatrix}
\alpha_1 \\
\alpha_2 \\
\alpha_3
\end{pmatrix}
$$

知:

$$
|A| = \vec \alpha_i \cdot \vec A_i = \alpha_1 \cdot (\alpha_2 \times \alpha_3)
$$

说明:

$$\alpha_2 \times \alpha_3 = \vec A_1$$

也可得

$$\alpha_2 \cdot (\alpha_2 \times \alpha_3) = 0$$

---

范德蒙德(Vandermonde)行列式

$$
\begin{vmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{vmatrix}
= \prod_{1 \leq j < i \leq n} (x_i - x_j)
$$

解:

$$
\begin{aligned}
d &=
\begin{vmatrix}
1 & 0 & 0 & \cdots & 0 \\
1 & x_2 - x_1 & x_2^2 - x_1 x_2 & \cdots & x_2^{n-1} - x_1 x_2^{n-2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n - x_1 & x_n^2 - x_1 x_n & \cdots & x_n^{n-1} - x_1 x_n^{n-2}
\end{vmatrix} \\
&= \prod_{i = 2}^n(x_i - x_1)
\begin{vmatrix}
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\
1 & x_3 & x_3^2 & \cdots & x_3^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{vmatrix} \\
&= \prod_{i = 2}^n(x_i - x_1) \prod_{2 \leq j < i \leq n} (x_i - x_j) \\
&= \prod_{1 \leq j < i \leq n} (x_i - x_j)
\end{aligned}
$$

> 消去第一行的关键, 在于突破主元法消去其他项的思维定式, 利用行列式的特殊结构, 比如用倒数第二列消去倒数第一列

说明行列式为 0, 则必有两项相等

---

上述等式的一些思考

按第一列展开

$$d = 1 \cdot A_{11} + \cdots + 1 \cdot A_{n1} $$

考虑第一项$M_{11}$

$$
\begin{aligned}
\begin{vmatrix}
x_2 & x_2^2 & \cdots & x_2^{n-1} \\
x_3 & x_3^2 & \cdots & x_3^{n-1} \\
\vdots & \vdots & \ddots & \vdots \\
x_n & x_n^2 & \cdots & x_n^{n-1}
\end{vmatrix}
&= \prod_{i \neq 1}^n x_i
\begin{vmatrix}
1 & x_2 & x_2^2 & \cdots & x_2^{n-2} \\
1 & x_3 & x_3^2 & \cdots & x_3^{n-2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^{n-2}
\end{vmatrix} \\
&= \prod_{i \neq 1}^n x_i \prod_{1 \leq j < i \leq n}^{i, j \neq 1} (x_i - x_j) \\
\end{aligned}
$$

考虑任意一项$A_{k1}$

$$
A_{k1} = (-1)^{k+1} M_{k1} = (-1)^{k+1} \prod_{j \neq k} x_j \prod_{1 \leq j < i \leq n}^{i, j \neq k} (x_i - x_j)
$$

考虑

$$
\begin{aligned}
  \frac {A_{k1}} {d}
  &= (-1)^{k+1} \frac {\prod_{j \neq k} x_j} {\prod_{k < i \leq n}(x_i - x_k) \prod_{1 \leq j < k}(x_k - x_j)} \\
  &= (-1)^{k+1} \frac {\prod_{j \neq k} x_j} {(-1)^{n-k} \prod_{k < i \leq n}(x_k - x_i) \prod_{1 \leq j < k}(x_k - x_j)} \\
  &= (-1)^{n-1} \frac {\prod_{j \neq k} x_j} {\prod_{k < i \leq n}(x_k - x_i) \prod_{1 \leq j < k}(x_k - x_j)} \\
  &= (-1)^{n-1} \frac {\prod_{j \neq k} x_j} {\prod_{1 \leq i \leq n}^{i \neq k} (x_k - x_i)}
\end{aligned}
$$

即证明

$$
\sum_{k=0}^{n}(-1)^{n-1} \frac {\prod_{j \neq k} x_j} {\prod_{1 \leq i \leq n}^{i \neq k} (x_k - x_i)} = 1
$$

由拉格朗日插值定理:

取:

$$ f(x) \equiv 1 $$

取$x = 0$, $f(0) = 1$即等上述等式

---

证明:

$$
\begin{vmatrix}
A & 0 \\
C & B
\end{vmatrix}
= |A| \cdot |B|
$$

其中, $A$ 为 $k \times k$, $B$ 为$r \times r$, $C$ 为 $r \times k$

解:

归纳法, 对 k 进行归纳

对第一行展开

$$
\begin{aligned}
d_m &= a_{1, 1} D_{1, 1} + \cdots + a_{k} D_{1, k} + 0 D_{1, k+1} + \cdots + 0 D_{1, k+r}\\
&= a_{1, 1} D_{1, 1} + \cdots + a_{k} D_{1, k} \\
&= a_{1, 1} A_{1, 1} |B| + \cdots + a_{k} A_{1, k} |B| \\
&= (a_{1, 1} A_{1, 1} + \cdots + a_{k} A_{1, k}) |B| \\
&= |A| \cdot |B|
\end{aligned}
$$

## 克拉默法则

Cramer

Cramer's rule. (2022, December 12). In Wikipedia. https://en.wikipedia.org/wiki/Cramer%27s_rule

1. 方程组有解, ($d = |A| \neq 0$)
2. 解是唯一的
3. 解为 $(\frac {d_1} {d}, \cdots, \frac {d_n} {d})$

解:

从矩阵的角度来看:

$$ A x = b $$

则可得:

$$ x = A^{-1} b $$

注意到伴随矩阵

$$x = \frac {1} {d} A^* b $$

所以:

$$(\frac {d_1} {d}, \cdots, \frac {d_n} {d}) = \frac {1} {d} A^* b$$

证明: 解的存在性

$(\frac {d_1} {d}, \cdots, \frac {d_n} {d})$代入方程组

即:

$$A \frac {1} {d} A^* b = b$$

> 用展开的方式去描述这一个过程

证明: 解的唯一性

解矩阵方程的过程

$$
A^* A x = A^* b \\
\Rightarrow d x = A^* b \\
\Rightarrow x = \frac {1} {d} A^* b
$$

> 依然是, 用展开的方式去描述这一个过程

!> 行列式不为 0

---

上述证明, 尤其是唯一性, 不从矩阵出发, 而从展开式出发, 很难理解为什么要乘以代数余子式, 又为什么需要累加

若要合理地理解, 就需要后面的矩阵知识, 而让自己又喜欢钻牛角尖, 追求自然而然, 深入的理解. 要是没有矩阵知识, 会卡在这儿老半天, 不愿意往后学.

需要一个良好的机制和心态, 让我带着问题前进, 能放下一时的纠结

---

齐次方程组, 当$d \neq 0$时, 有唯一解$(0, \cdots, 0)$

## Laplace expansion

$M$: k 级子式

$M^{\prime}$: k 级子式的余子式

$A$: 代数余子式

$$A = (-1)^{\sum_{s=1}^{k} i_s+j_s} M^{\prime}$$

其中, $i_s, j_s$ 为 $M$ 的所选取的行号和列号

---

引理:

$M \cdot A$的每一项都属于$D$

---

Laplace

$$D = M_1 A_1 + \cdots + M_t A_t$$

证明:

易知, $M_i A_i$ 与 $M_j A_j 没有公共项

根据引理, 只需证明项数个数相等

其中, $t = C_n^k$

即

$$C_n^k \cdot k! \cdot (n-k)! = n!$$

---

证明:

$$|AB| = |A| \cdot |B|$$

解:

构造一个矩阵 $C$

$$
C =
\begin{pmatrix}
A & 0 \\
-E & B
\end{pmatrix}
$$

由 Laplace 知

$$|C| = |A| \cdot |B|$$

由初等行变换, 不改变行列式的值

$$
D =
\begin{pmatrix}
0 & AB \\
-E & B \\
\end{pmatrix}
$$

由 Laplace

$$|D| = (-1)^{\sum_i(i+n+i)} |-E| \cdot |B| = |AB|$$

故

$$|AB| = |D| = |C| = |A| \cdot |B|$$

一点收获: 初等变换与一些特殊的矩阵关联

$$
\begin{pmatrix}
 E & A \\
 0 & E
\end{pmatrix}
\cdot C = D
$$
