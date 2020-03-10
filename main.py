from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

matrices = matGen.SigProfilerMatrixGeneratorFunc("./output/", "GRCh37", "./data/",plot=True, exome=False, bed_file=None, chrom_based=False, tsb_stat=False, seqInfo=False, cushion=100)
