# NumPy

## ndarray

### ndarray属性

```python
ndarray.ndim
ndarray.shape
ndarray.size# == .shape m*n
ndarray.dtype
ndarray.itemsize
```

### ndarray创建方法

* ```python
  np.array(list/tuple, dtype=np.float32)
  ```

* ```python
  np.arange(start, end, step)
  np.ones(shape)
  np.zeros(shape)
  np.full(shape, value) # 生成元素全为val的矩阵
  np.eye(n) # n by n identity matrix
  # shape为tuple 
  # 所有矩阵默认dtype为float32, 可通过dtype参数指定
  np.ones_like(ndarray)
  np.zeros_like(ndarray)
  np.full_like(ndarray, val)
  # 根据ndarray的性状产生矩阵
  ```

* ```python
  np.linspace(start, end, num, endpoint)
  np.concatenate((a, b))
  ```

### ndarray 维度变换

* ```python
  ndarray.reshape(shape) # 不改变原数组
  ndarray.resize(shape) # 改变原数组
  ndarray.swapaxes(ax1, ax2)
  ndarray.flatten()
  ```

### ndarray数据类型变换

```python
ndarray.astype()# np.float无需指定32或64，程序自动判断。
# astpye 会创建新数组
ndarray.tolist()
```

### ndarray 索引和切片

```python
ndarray[start:end:step] 
```

### ndarray运算

#### 一元函数

```python
np.abs(), np.fabs()
np.sqrt()
np.square()
np.log(), np.log10(), np.log2()
np.ceil()#向上取整
np.floor()#向下取整
```

```python
np.rint() #四舍五入
np.modf() #分别返回小数和整数部分
np.cos(), np.cosh()
np.sin(), np.sinh()
np.tan(), np.tanh()
np.exp() #计算指数
np.sign() #计算符号值
```

#### 二元函数

```python
+ - * / **
np.maximum(x, y) np.fmax()
np.minimum(x, y) np.fmin()
np.mod(x, y)
np.copysign() #将y中符号赋给x
> < >= <= == !=
```

## 数据存取

### 一二维

```python
np.savetxt(filename, array, format='%18e', delimiter=None) 
np.loadtxt(filename, array, format='%18e', delimiter=None, unpack=False) 
# 只能读取1,2维数据
```

### 多维数据

```python
ndarray.tofile("a.dat". sep='', format='%s') #无sep为二进制文件
np.fromfile(file, dtype, count=-1, sep='')
```

### 便捷存取

```python
np.save(file, array), np.savez(file, array) # .npy, .npz
np.load(file)
```



## 随机数子库

```python
np.random.*
```

```python
.rand(shape) # 均匀分布
.randn(shape) # 正态分布
.randint(low[,high, shape]) 
seed(s) 
```

```python
.shuffle(array) # 根据array第一轴随机排列, 改变数组
.permutation(array) # 与shuffle 类似但是不改变数组
.choice(a[, size, replace, p]) # 从array 中以概率p抽取元素,形成size array, replace 是否重用元素.
```

```python
.uniform(low, high, size)
.normal(mean, std, size)
.possion(lam, size)
```

## 统计函数

```python
 
```

