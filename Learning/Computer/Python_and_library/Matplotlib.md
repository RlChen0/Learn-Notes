# Matplotlib
## pyplot
### plot
```python
plt.plot(x, y , format_string, **kwarg)
```
* x:  列表或数组，可选。
* y: 列表或数组（一条曲线可省略x（index为x），多条曲线不可）
* format_string: 控制格式的字符串，可选f
  * 颜色字符
  * 风格字符：'-'实线, '--'破折线, '-.' , ':', '' '' 
* **kwargs 一组或更多组上述参数

### axis
```python
plt.axis([x_start, x_end, y_start, y_end])
```

### subplot

```python
plt.subplot(numrows, numcols, plot_index)
```

