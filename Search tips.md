# 生信

##### GC偏好

测序中的GC偏好指的是基因组上GC含量在50%左右的区域更容易被测到，产生的reads更多，这些区域的覆盖度更高，在高GC或者低GC区域，不容易被测到，产生较少的reads，这些区域的覆盖度更少

[Accessing Public Genomic Data | Tutorials on accessing public reference and genomic data (hbctraining.github.io)](https://hbctraining.github.io/Accessing_public_genomic_data/lessons/accessing_public_experimental_data.html)

* 将染色体划分成20bp 间隔, 10bp步长

* ```bash
  bedtools makewindows -g  chrom.size -w 20 -s 10
  ```

gff2gtf

* ```bash
  gffread gencode.v19.annotation.gff3 -T -o gencode.v19.gtf
  ```

* ```bash
  gffread gencode.vM13.annotation.gtf -o gencode.vM13.annotation.gff3
  ```

# Python library

## Pandas

```python
df[(df[""]==)&(df[""])]
```

```python
Series.unique()
# Return unique values of Series object.
# Returns
# ndarray or ExtensionArray
# The unique values returned as a NumPy array
```



无限迭代器

```python
import itertools
itertools.conut() 
itertools.cycle() #cycle()会把传入的一个序列无限重复下去
itertools.repeat() #repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
itertools.takewhile() #可以把一组迭代对象串联起来，形成一个更大的迭代器
```



sonnet_sad.py -f ../data/refgenome/NIP/IRGSP-1.0_genome.fasta -o sad_test --species nip save_model/nip_768_0.001_mmt_203/ ../data/vcf_samples/180.vcf

# Linux

```shell
# 替换 gene 为 GENE
sed 's/gene/GENE/g' file
```

[linux tar 解压命令总结_Young的专栏-CSDN博客_linux tar解压](https://blog.csdn.net/imyang2007/article/details/7634470)
