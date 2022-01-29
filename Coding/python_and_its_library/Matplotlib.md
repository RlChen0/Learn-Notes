# Matplotlib
## pyplot
### plot
```python
plt.plot(x, y , format_string, **kwarg)
```
* x:  列表或数组，可选。

* y: 列表或数组（一条曲线可省略x（index为x），多条曲线不可）

* format_string: 控制格式的字符串 
  
  * ![image-20211210131633490](https://cdn.jsdelivr.net/gh/BioJokar/PicGo@main/img/image-20211210131633490.png)
  
  * ![image-20211210142020802](https://cdn.jsdelivr.net/gh/BioJokar/PicGo@main/img/202112101420873.png)
  * ![image-20211210142122021](https://cdn.jsdelivr.net/gh/BioJokar/PicGo@main/img/202112101421195.png)
  * ![image-20211210142537233](https://cdn.jsdelivr.net/gh/BioJokar/PicGo@main/img/202112101425587.png)
  
* **kwargs 一组或更多组上述参数

### axis
```python
plt.axis([x_start, x_end, y_start, y_end])
```

### subplot

```python
plt.subplot(numrows, numcols, plot_index)
```

