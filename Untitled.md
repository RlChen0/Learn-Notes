```python
def main():
  usage = 'usage: %prog [options] <model_file> <bed_file>'
  parser = OptionParser(usage)
  parser.add_option('-b', dest='bigwig_indexes',
      default=None, help='Comma-separated list of target indexes to write BigWigs')
  parser.add_option('-e', dest='embed_layer',
      default=None, type='int',
      help='Embed sequences using the specified layer index.')
  parser.add_option('-f', dest='genome_fasta',
      default=None,
      help='Genome FASTA for sequences [Default: %default]')
  parser.add_option('-g', dest='genome_file',
      default=None,
      help='Chromosome length information [Default: %default]')
  parser.add_option('-l', dest='site_length',
      default=None, type='int',
      help='Prediction site length. [Default: model seq_length]')
  parser.add_option('-o', dest='out_dir',
      default='pred_out',
      help='Output directory [Default: %default]')
  # parser.add_option('--plots', dest='plots',
  #     default=False, action='store_true',
  #     help='Make heatmap plots [Default: %default]')
  parser.add_option('-p', dest='processes',
      default=None, type='int',
      help='Number of processes, passed by multi script')
  parser.add_option('--rc', dest='rc',
      default=False, action='store_true',
      help='Ensemble forward and reverse complement predictions [Default: %default]')
  parser.add_option('-s', dest='sum',
      default=False, action='store_true',
      help='Sum site predictions [Default: %default]')
  parser.add_option('--shifts', dest='shifts',
      default='0',
      help='Ensemble prediction shifts [Default: %default]')
  parser.add_option('--species', dest='species',
      default='human')
  parser.add_option('-t', dest='targets_file',
      default=None, type='str',
      help='File specifying target indexes and labels in table format')
  (options, args) = parser.parse_args()

```

python sonnet_predict_bed.py -f ../data/refgenome/MH63RS3/MH63RS3.fasta --species mh63 -o ./ppi/r1_Anchor_pos/	./save_model/mh63_768_0.005_mmt_182/	/public/home/xwli/xfchen/PPI_dataset/H3K4me3_MH63_r1_Anchor_positive_sequences.bed





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