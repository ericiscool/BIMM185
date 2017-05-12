

zcat data/Genomes/Agrobacterium_tumefaciens_LBA4213_\(Ach5\)/GCF_000576515.1_ASM57651v1/GCF_000576515.1_ASM57651v1_protein.faa.gz | makeblastdb -input_type fasta -dbtype prot -parse_seqids -hash_index -out $BLASTDB/atume -title "atume  04/27/2017A"  -in -
zcat data/Genomes/Escherichia_coli_str._K-12_substr._MG1655/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_protein.faa.gz | makeblastdb -input_type fasta -dbtype prot -parse_seqids -hash_index -out $BLASTDB/ecoli -title "ecoli  04/27/2017A"  -in -


