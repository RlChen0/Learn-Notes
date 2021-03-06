#  Linear Algebra

## Lecture 1

* n linear equations, n unknowns
* Row picture
* Column picture
* Matrix form

### Example1

$$
2x-y=0\\-x+2y=3
$$

$$
\begin{bmatrix}
    2&-1\\-1&2
\end{bmatrix}
\begin{bmatrix}
    x\\y
\end{bmatrix}
=
\begin{bmatrix}
    0\\3
\end{bmatrix}
$$

$$
A\mathbf{x}=b
$$

#### Row Picture 1

![row picture1](../image/row_picture-16324013669961.png)

#### Column Picture 1

$$
x
\begin{bmatrix}
    2\\-1
\end{bmatrix}+y
\begin{bmatrix}
    -1\\2
\end{bmatrix}
=
\begin{bmatrix}
    0\\3
\end{bmatrix}
$$
this equation asking for finding the **linear combination** of columns

![column piture](../image/geogebra-16324022690272.png)
take all linear combination of col1 and col2 will get the whole plane.

### Example2

$$
\begin{cases}
    2x-y=0\\
    -x+2y-z=-1\\
    -3y+4z=4
\end{cases}
$$

$$
A=
\begin{bmatrix}
    2&-1&0\\-1&2&-1\\0&-3&4
\end{bmatrix},
b=
\begin{bmatrix}
    0\\-1\\4
\end{bmatrix}
$$

#### Row Picture 2

![row picture](../image/geogebra-16324030816973.png)

equation makes a plane, not important

#### Column Picture 2

$$
x
\begin{bmatrix}
    2\\-1\\0
\end{bmatrix}
+y
\begin{bmatrix}
    -1\\2\\-3
\end{bmatrix}
+z
\begin{bmatrix}
    0\\-1\\4
\end{bmatrix}
=
\begin{bmatrix}
    0\\-1\\4
\end{bmatrix}
$$

![column picture](../image/geogebra-16324034826314.png)

Can I solve $Ax=b$ for every b?$==$Do the linear combinations of the columns fill 3D space? $==$Do the matrix no single?$==$Do the matrix inverterable?

### Matrix $\times$ Vector

$$A\mathbf{x}=b$$

$$
\begin{bmatrix}
-&-&-\\-&-&-\\-&-&-
\end{bmatrix}
\begin{bmatrix}
3\\4\\6
\end{bmatrix}
=3\times\mathbf{col1}
+4\times\mathbf{col2}
+6\times\mathbf{col3}
$$

$A\times \mathbf{x}$  is a combenation of columns of $A$.

$$
\begin{bmatrix}
    1&2&7
\end{bmatrix}
\begin{bmatrix}
    -&-&-\\-&-&-\\-&-&-
\end{bmatrix}
=3\times\mathbf{col1}
+4\times \mathbf{col2}
+6\times\mathbf{col3}
$$

$$
m\times n\cdot n\times p = m\times p
$$

$\mathbf{x}\times A$ is combination of rows of $\mathbf{A}$

## Lecture2

$\begin{cases}x+2y+z=2\\3x+8y+z=12\\4y+z=2\end{cases}$

### Elimination

$$
\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix}\mathbb{A}\underset{(2,1)}\rightarrow\begin{bmatrix}1&2&1\\0&2&-2\\0&4&1\end{bmatrix}\underset{(3,2)}\rightarrow\begin{bmatrix}\mathbb{1}&2&1\\0&\mathbb{2}&-2\\0&0&\mathbb{5}\end{bmatrix}\mathbb{U}
$$

$\mathbb{1,2,5}$ are the three pivix and 0 can't be a pivix.
determinant is  product of pivix. 10 for this matrix.

Elimination failure when pivix is Zero and can't solve it by row exchange.

### Back-substitution

#### normal version

$$
\begin{bmatrix}
    1&2&1\\3&8&1\\0&4&1
\end{bmatrix}
\mathbb{A}
\begin{bmatrix}
    2\\12\\2
\end{bmatrix}
\mathbb{b}
\underset{(2,1)}\rightarrow
\begin{bmatrix}
    1&2&1\\0&2&-2\\0&4&1
\end{bmatrix}
\begin{bmatrix}
    2\\6\\2
\end{bmatrix}
\underset{(3,2)}\rightarrow
\begin{bmatrix}
    \mathbb{1}&2&1\\0&\mathbb{2}&-2\\0&0&\mathbb{5}
\end{bmatrix}
\mathbb{U}
\begin{bmatrix}
    2\\6\\-10
\end{bmatrix}
\mathbb{c}
$$

$\mathbb{Ab}$ is argument matrix.

$\mathbb{Ux=c}$ can easily solve.

#### matrices version

subtract $3\times\mathbb{row1}$ from $\mathbb{row2}$

$$
\mathbb{E_{21}}
\begin{bmatrix}
    1&0&0\\-3&1&0\\0&0&1
\end{bmatrix}
\begin{bmatrix}
    1&2&1\\3&8&1\\0&4&1
\end{bmatrix}
=
\begin{bmatrix}
    1&2&1\\0&2&-2\\0&4&1
\end{bmatrix}
$$

subtract $2\times\mathbb{row2}$ from $\mathbb{row3}$

$$
\mathbb{E_{32}}
\begin{bmatrix}
    1&0&0\\0&1&0\\0&-2&1
\end{bmatrix}
\begin{bmatrix}
    1&2&1\\0&2&-2\\0&4&1
\end{bmatrix}=
\begin{bmatrix}
    1&2&1\\0&2&-2\\0&0&5
\end{bmatrix}
$$

$$
\mathbb{E_{32}(E_{21}A)=U}
$$

$$
\mathbb{(E_{32}E_{21})A=U}
$$

### Permutation matrix

#### Exchange row

$$
\begin{bmatrix}
    0&1\\1&0
\end{bmatrix}
\begin{bmatrix}
    a&b\\c&d
\end{bmatrix}
=
\begin{bmatrix}
    c&d\\a&b
\end{bmatrix}
$$

#### Exchange column

$$
\begin{bmatrix}
    a&b\\c&d
\end{bmatrix}
\begin{bmatrix}
    0&1\\1&0
\end{bmatrix}
=
\begin{bmatrix}
    b&a\\d&c
\end{bmatrix}
$$

$$
\mathbb{E^{-1}E=I}
$$

## Lecture 3

### Product

condition for matrices product.

colnumber of first matrix == rownumber of second matrix.

$$
\mathbb{m\times n \cdot n\times p = m\times p}
$$

$$
\mathbb{A\cdot B=C}\\
$$

### method1

$$
\mathbb{C_{34}=(row3\ of\ A) \cdot (col4\ of\ B)}\\
=a_{31}b_{14}+a_{32}b_{23}+\cdots=\sum a_{3k}b_{k4}
$$

### method2

Column of C are combination of column of A, and column in B tells what's the combination.

$$
\mathbb{C\ cols=A \times B\ cols}
$$

### method3

Row of C are combination of row of B, and row in A tells what's the combination.

$$
\mathbb{C\ rows=A\ rows \times B}
$$

### method4

C is sum of cols of A $\times$ rows of B.

### Block product

divide matrix into blocks,and block in two matrices must match, can multiply matrices by block.

$$
\begin{bmatrix}
    A_1&A_2\\A_3&A_4
\end{bmatrix}
\times
\begin{bmatrix}
    B_1&B_2\\B_3&B_4
\end{bmatrix}
=
\begin{bmatrix}
    A_1B_1+A_2B_3&A_1B_2+A_2B_4\\A_3B_1+A_4B_3&A_3B_2+A_4B_4
\end{bmatrix}
$$

## Inverses

### For invertible,nonsingular matrix, Inverse is exsit.

column vector are point in different direction.Are linear indenpendent

$$
\mathbb{A^{-1}A=I}\\
and\ if\ A\ is\ Square\ \mathbb{AA^{-1}=I}
$$

### Singular, No inverses

$$
A=
\begin{bmatrix}
    1&3\\2&6
\end{bmatrix}
$$

#### prov1

product of A with another matrix, the result is the linear combination of A, and can't get Identity matrix from linear combination the column of A.

#### prov2

$$
\begin{bmatrix}
    1&3\\2&6
\end{bmatrix}
\begin{bmatrix}
    3\\-1
\end{bmatrix}
=
\begin{bmatrix}
    0\\0
\end{bmatrix}
$$

$$
\mathbb{Ax=0}
\rightarrow
\mathbb{A^{-1}Ax=0}
\rightarrow
\mathbb{Ix=0}
\rightarrow
\mathbb{x=0}
$$
but x is not Zero.

**Non-invertible, singular matrices some combination of the column can get 0.**
$\mathbb{Ax=0},x\not ={0}$

### compute Inverses

$$
\begin{bmatrix}
    1&3\\2&7
\end{bmatrix}
\begin{bmatrix}
    a&c\\b&d
\end{bmatrix}
=
\begin{bmatrix}
    1&0\\0&1
\end{bmatrix}
$$

#### method1
$$
\begin{bmatrix}
    1&3\\2&7
\end{bmatrix}
\begin{bmatrix}
    a\\b
\end{bmatrix}=
\begin{bmatrix}
    1\\0
\end{bmatrix}
\\
\begin{bmatrix}
    1&3\\2&7
\end{bmatrix}
\begin{bmatrix}
    c\\d
\end{bmatrix}=
\begin{bmatrix}
    0\\1
\end{bmatrix}
$$

compute the equations

#### method2 Gauss-Jordan(solve 2 eqns at once)

$$
\begin{bmatrix}
    1&3&1&0\\2&7&0&1
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    1&3&1&0\\0&1&-2&0
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    1&0&7&-3\\0&1&-2&0
\end{bmatrix}
$$

PROV

$$
E
\begin{bmatrix}
    A&I
\end{bmatrix}
=
\begin{bmatrix}
    I&E
\end{bmatrix}
\Rightarrow E==A^{-1}
$$

## Lecture 4

$$
ABB^{-1}A^{-1}=I
$$

$$
A^{-1}A=I
\rightarrow
A^{T}(A^{-1})^T=I
$$

A transpose inverse is A inverse transpose.

Order of Transpose and Inverse can be change.

$$
\mathbb{A=LU}
$$
If no row exchanges,multipliers go directly into $\mathbb{L}$.

$A\rightarrow U$ NEED $\frac{1}{3}n^3$ opeartion and for $\mathbb{b}$ need $n^2$

$n\times n\ matrix,\ n^2+(n-1)^2+\cdots1^2=\frac{1}{3}n^3(\frac{d}{dx}x^2)\\for\ b,\ 2\times[n+(n-1)\cdots1]=n^2$

### Permutation

matrix exchange rows.

$$
\mathbb{P^(-1)=P^T}\rightarrow P^TP=I
$$

$$
n \times n\ matrices\ has A^n_n\ \  permutation\ matrix
$$

for matrices needs row exchange.
$$
\mathbb{A=LU}\Rightarrow \mathbb{PA=LU}
$$

### Transpose

$$
(\begin{bmatrix}
    1&2\\3&4\\5&6
\end{bmatrix})^T
=
\begin{bmatrix}
    1&2&3\\4&5&6
\end{bmatrix}

(A)^T_{ij}=A_{ji}
$$

$$
Symmetic Matrix\\
\mathbb{A^T=A}
$$

$$
RR^T\ is\ always\ symmetric\ matrix.\\
(RR^T)^T=(R^T)^TR^T=RR^T
$$

## Lecture5

### Vector Space

Vector Space is a space closed for linear combination.(vectors in space after linear combinatin still in the spaces)

### Subspace

Subspace for $R^2$

* $R^2$
* line through $\begin{bmatrix}0\\0\end{bmatrix}$
* $\begin{bmatrix}0\\0\end{bmatrix}$

Subspace for $R^3$

* $R^3$
* plane through $\begin{bmatrix}0\\0\\0\end{bmatrix}$
* line through $\begin{bmatrix}0\\0\\0\end{bmatrix}$
* $\begin{bmatrix}0\\0\\0\end{bmatrix}$

#### $C(A),\ Column Space$

linear combination of columns and Zero vector.

## Lecture 6

$$
all\ combination\ cv+dw\ are\ all\ in\ the\ space.\\
intersection\ of\ Subspace\ is\ a\ subspacs.
$$

### Column Space

Column Space is linear combination of column in matrix.

### Null Space

$$
\mathbb{Ax=0},all\ x\ produce\ the\ null space.
$$

## Lecture 7

$$
\mathbb{A=}
\begin{bmatrix}
    1&2&2&2\\2&4&6&8\\3&6&8&10
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    1&2&2&2\\0&0&2&4\\0&0&2&4
\end{bmatrix}
\rightarrow
\mathbb{U=}
\begin{bmatrix}
    1&2&2&2\\0&0&2&4\\0&0&0&0
\end{bmatrix}
\\
The\ zero\ row\ tell\ row3\ is\ the\ linear\ combination\ of\ row1\ and\ 2.elimitaion\ will\ knock\ it\ out.
$$

elimination, get the number of pivots.

the rank of A = the number of pivits = A

the free variables = n-r = 4-2 = 2

free variables can be choose freely, and back subsititution to solve the eqution.

$$
\begin{bmatrix}
    1&2&2&2\\0&0&2&4\\0&0&0&0
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    1&2&0&-2\\0&0&2&4\\0&0&0&0
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    1&2&0&-2\\0&0&1&2\\0&0&0&0
\end{bmatrix}
=
\mathbb{R}
=rref(\mathbb{A})
$$

$$
\mathbb{A\rightarrow U\rightarrow R}\\
\mathbb{R}=
\begin{bmatrix}
    I&F\\0&0
\end{bmatrix}\\
\mathbb{Rx=0}
=
\begin{bmatrix}
    I&F\\0&0
\end{bmatrix}
\begin{bmatrix}
    -F\\I
\end{bmatrix}
\\
c\begin{bmatrix}
    -F\\I
\end{bmatrix}\ is\ the\ null\ space\ matrix
\\
\begin{bmatrix}
    -2&2\\0&-2\\1&0\\0&1
\end{bmatrix}
\rightarrow
c_1\begin{bmatrix}
    -2\\0\\1\\0
\end{bmatrix}+
c_2\begin{bmatrix}
    2\\-2\\0\\1
\end{bmatrix}\ are\ the\ solution.
$$

## Lecture 8

### solve Ax=b

$$
\begin{bmatrix}
    A&b
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    U&b
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    R&b
\end{bmatrix}
$$
get the $x_p$ through elimination. And add it with null space.

$$
Ax_p=b\\
Ax_n=0\\
A(x_p+x_n)=b
$$

$x_p+x_n$ is the complete solve of $Ax=b$ 

#### $r=m=n$

$$
R=I
$$

null space is 0, only 1 solution for Ax=b.

#### $r=m<n$

$$
R=
\begin{bmatrix}
    I&F
\end{bmatrix}
$$

null space is not only zero, $\inf$ solution.

#### $r=n<m$

$$
R=
\begin{bmatrix}
    I\\0
\end{bmatrix}
$$

null space is zero, 0 or 1 solution.

#### $r<n,r<m$

$$
R=
\begin{bmatrix}
    I&F\\0&0
\end{bmatrix}
$$

null space is not only 0, 0 or $\inf$ solution.

## Lecture 9

### Linear indenpedent

bunch of vector only times Zero vector get the Zero.

The null space of the matrix only have Zero.

### Span

all linear combination of vectors span a space.

### basis

a bunch of vector span a space and are indenpendent,

### Dimention

the number of basis vector.

rank of matrix = dim of C(A)
n-r = dim of N(A)