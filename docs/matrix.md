# 矩阵

## 概念的背景

几何, 表格

## 运算

$$r(A+B) \leq r(A) + r(B)$$

解:

$A+B$即$\alpha + \beta$

$A$和$B$的极大线性无关组, 可以线性表出$A+B$

故

$$r(A+B) \leq r(A) + r(B)$$

---

转置

$$(AB)'=B'A'$$

## 行列式与秩

$$|AB| = |A||B|$$

---

退化的: $|A|=0$

---

$$r(AB) \leq min(r(A), r(B))$$

解:

将$B$看作向量的组合

$$AB = A \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}$$

与$Ax=b$同构, 得到的是关于$b$的线性组合, 即能被$B$线性表出

故

$$r(AB) \leq r(B)$$

同理,

$$r(AB) \leq r(A)$$

或者

$$r(AB)=r((AB)')=r(B'A') \leq r(A') =r(A)$$

## 逆

定义:

$$AB=BA=E$$

---

唯一的

$$B_2 = B_1 (A B) = (B_1 A) B = B$$

---

$$A=\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$$

伴随矩阵$A^*$

$$A^*=\begin{pmatrix} A_{11} & A_{21} & \cdots & A_{n1} \\ A_{12} & A_{22} & \cdots & A_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ A_{1n} & A_{2n} & \cdots & A_{nn} \end{pmatrix}$$

即是

$$\vec a \cdot \vec A = \begin{cases} d \\ 0 \end{cases}$$

的矩阵形式

刚好枚举了$n \times n$中情况

得

$$AA^* = dE$$

---

$$A可逆 \Leftrightarrow |A| \neq 0$$

解:

充分性:

取$$A^{-1}=\frac{1}{|A|}A^*$$

必要性:

$$|E| = |AA^{-1}| = |A||A^{-1}| \Rightarrow |A| \neq 0$$

---

$$(A')^{-1}=(A^{-1})'$$

解:

$$AA^{-1} = A^{-1}A = E$$

同时转置

$$(A^{-1})'A' = A'(A^{-1})' = E$$

即:

$$(A')^{-1}=(A^{-1})'$$

---

$$(AB)^{-1}=B^{-1}A^{-1}$$

解:

代入定义即可

---

若$P, Q$可逆, 则

$$r(A)=r(PA)=r(AQ)$$

解:

$$r(A)=r(P^{-1}PA) \leq r(PA) \leq r(A)$$

故:

$$r(A)=r(PA)$$

## 分块

即矩阵的元素可以为矩阵

满足矩阵的乘法

---

$$D=\begin{pmatrix} A & 0 \\ C & B \end{pmatrix}$$

则, 解方程可得:

$$D^{-1}=\begin{pmatrix} A^{-1} & 0 \\ -B^{-1}CA^{-1} & B^{-1} \end{pmatrix}$$

---

若$C=0$, 则:

$$\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}^{-1}=\begin{pmatrix} A^{-1} & 0 \\ 0 & B^{-1} \end{pmatrix}$$

---

对角矩阵: 只有对角线上有非零元素, 且元素不为矩阵

准对角矩阵: 元素为矩阵

## 初等矩阵

由$E$经过一次初等变换得到

|    symbol    |            row            |            col            |
| :----------: | :-----------------------: | :-----------------------: |
|  $P(i, j)$   |   交换第$i$行和第$j$行    |   交换第$i$列和第$j$列    |
|  $P(i(c))$   |      第$i$行乘以$c$       |      第$i$列乘以$c$       |
| $P(i, j(c))$ | 第$i$行加上第$j$行乘以$c$ | 第$i$列加上第$j$列乘以$c$ |

行和列的矩阵是一样的, 真正表现效果的是通过左乘还是右乘来作用行或者列

---

初等变换

行变换: 左乘初等矩阵

列变换: 右乘初等矩阵

记忆方法:

$$
PA=P \begin{pmatrix}
    A_1 \\ A_2 \\ \vdots \\ A_n
\end{pmatrix}
$$

只能操作行, 因而左乘是行变换

---

$$
\begin{aligned}
    P(i, j)^{-1} &= P(j, i) \\
    P(i(c))^{-1} &= P(i(\frac{1}{c})) \\
    P(i, j(c))^{-1} &= P(i, j(-c))
\end{aligned}
$$

---

等价: B 可由 A 经过一系列初等变换得到

---

标准形: 对角线上 r 个 1

任意矩阵与标准形等价

解:

数学归纳法

---

$$A, B等价 \Leftrightarrow A = P_1 \cdots P_l B Q_1 \cdots Q_t$$

特别的, A 可逆:

$$A=N_1 \cdots N_k$$

---

由于

$$A=N_1 \cdots N_k$$

$$A^{-1}=N_k^{-1} \cdots N_1^{-1}$$

故

$$N_k^{-1} \cdots N_1^{-1}A = E$$

此时是左乘, A 可以通过初等行变换即可变成标准形

---

求逆的方法: 利用 A 只需初等行变换即可变成$E$

$$P(A, E) = (PA, PE) = (E, A^{-1})$$

故, 对$(A, E)$ 进行初等行变换即可

## 应用

$$T = \begin{pmatrix} A & 0 \\ C & D \end{pmatrix}$$

行变换(借助 $E$ 来思考初等矩阵)

$$\begin{pmatrix} E & 0 \\ -CA^{-1} & E \end{pmatrix} T = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix}$$

---

证明:

$$|AB| = |A||B|$$

解:

引理:

$$
\begin{vmatrix}
    A & 0 \\
    C & B
\end{vmatrix}
= |A| |B|
$$

由:

$$
\begin{pmatrix}
    E & A \\
    0 & E
\end{pmatrix}
\begin{pmatrix}
    A & 0 \\
    -E & B
\end{pmatrix} =
\begin{pmatrix}
    0 & AB \\
    -E & B
\end{pmatrix}
$$

由于初等变换不改变行列式的值, 故:

$$
left=\begin{vmatrix}
    A & 0 \\
    -E & B
\end{vmatrix} = |A| |B|
$$

而另一边:

$$
\begin{aligned}
right &=\begin{vmatrix}
0 & AB \\
-E & B
\end{vmatrix} \\
&= (-1)^{n}
\begin{vmatrix}
    AB &  0 \\
    B & -E
\end{vmatrix} \\
&= (-1)^{n} |-E| |AB| \\
&= |AB|
\end{aligned}
$$

> 巧妙的是证明右边, 再次用了引理
