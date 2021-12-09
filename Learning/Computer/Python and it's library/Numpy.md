# NumPy

## ndarray属性

```python
ndarray.ndim
ndarray.shape
ndarray.size# == .shape m*n
ndarray.dtype
ndarray.itemsize
```

## ndarray创建方法

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

## ndarray 维度变换

* ```python
  ndarray.reshape(shape) # 不改变原数组
  ndarray.resize(shape) # 改变原数组
  ndarray.swapaxes(ax1, ax2)
  ndarray.flatten()
  ```

## ndarray数据类型变换

```python
ndarray.astype()# np.float 程序自动判断为32 还是64
```

