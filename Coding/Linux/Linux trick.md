替换一列内容

```shell
 awk '$2="s"' file.txt > new.txt # 第二列替换为s
 awk -F '\t' '$2=$1' file.txt > new.txt # -F 分隔符， d
```

查找替换

```shell
# 替换 gene 为 GENE
sed 's/gene/GENE/g' file
```

删除特定行

```shell
sed '/xxx/d' file
```

tar.gz 解压

tar xz

批量修改分隔符

```shell
awk 'BEGIN{ FS=" ";OFS="," }{ print $1,$2,$3,$4 }' file2.txt
```

basename

```shell
basename [pathname] [suffix]
basename [string] [suffix]

basename /tmp/test/file.txt
file.txt
basename /tmp/test/file.txt .txt
file
```

反选删除

```shell
shopt -s extglob（打开extglob模式）
rm -rf !(file1)
```

