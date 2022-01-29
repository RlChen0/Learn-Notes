# Pandas

## Series

### 索引

```python
pd.Series([], index=[]) # 通过index参数自定义索引，自动生成的索引和自定义索引并存，但是不用混合使用
```

### 创建方法

#### 标量

```python
pd.Series(25, index=['a', 'b', 'c']) # index 不能省略
```

#### 字典

```python
pd.Series({'a':9, 'b':8, 'c':10}) #直接创建， 也可指定index从而选取相关数据
```

#### ndarray

与NumPy连用

### 基本操作

```python
.index # 获得索引
.values # 获得数据
in
.get
Series + Series # 自动对齐数据，取索引并集，索引相同运算不同为NAN
.name .index.name
```

索引和切片 与ndarray类似

## Data Frame

共用索引的多列

