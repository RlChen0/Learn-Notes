# SAMPLE Picking

## Sample txt

```shell
sed 's/\/home\/WBXie\/rice3k\/raw_data\/all_fq\//\/public\/home\/software\/opt\/public\/rice3k\/raw_data\/all_fq\//g' Sample_fastq_info.txt > Sample_fastq.txt
sed '/2.fq.gz/d' Sample.txt > Sample_1.txt
cut -f2 Sample_1.txt > ./Sample/Sample_1.txt

```

