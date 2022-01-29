

# Linux 基础

## 去可视化命令行

pwd：打印当前目录

echo：print

mkdir， -p

touch

cd, - 返回，~个人文件夹主目录

more q退出

less  q退出 -SN

history

\> 重定向

& 挂在后台

cat 查看文件

head tail 查看前四行，-1 查看第一行

## 文本处理

wc 查看文件的byte数，字数或列数

awk

```shell[xwli@mn02 test]$ cut -f 1-3 test.bed |awk '{print $1":"$2","$3}'
track:name="His,(@
chr1:9769,10673
chr1:9776,10481
chr1:9788,10497
chr1:9795,10434
chr1:9799,10446
chr1:9805,10419
chr1:9810,10438
chr1:9811,10465
chr1:9825,10306
```

sort

-k2,2第二列，n 作为数字排序，r 反转

```shell sort -k2,2nr test.bed |cut -f 1-3
chr1	9825	10306
chr1	9811	10465
chr1	9810	10438
chr1	9805	10419
chr1	9799	10446
chr1	9795	10434
chr1	9788	10497
chr1	9776	10481
chr1	9769	10673
track name="His (@ Brs) 50" url="http://chip-atlas.org/view?id=$$" gffTags="on"
```

grep

cut

- -b ：以字节为单位进行分割。这些字节位置将忽略多字节字符边界，除非也指定了 -n 标志。
- -c ：以字符为单位进行分割。
- -d ：自定义分隔符，默认为制表符。
- -f ：与-d一起使用，指定显示哪个区域。
- -n ：取消分割多字节字符。仅和 -b 标志一起使用。如果字符的最后一个字节落在由 -b 标志的 List 参数指示的
  范围之内，该字符将被写出；否则，该字符将被排除

bam和sam文件主要是bwa、bowtie、tophat等序列比对工具产生的

sam(Sequence Alignment Mapping) 序列比对映射

sam分为两部分，注释信息（header section）和比对结果部分（alignment section）

tr 将一组字符转变被另一组字符