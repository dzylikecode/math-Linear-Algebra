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

$$\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{vmatrix} = \sum_{j_1 j_2 \cdots j_n} (-1)^{\tau (j_1 j_2 \cdots j_n) } a_{1 j_1} a_{2 j_2} \cdots a_{n j_n}$$
