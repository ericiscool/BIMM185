blastp -query data/Genomes/Escherichia_coli_str._K-12_substr._MG1655/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_protein.faa -out OutputFiles/SQL/EvA.out -db atume -evalue 0.01 -outfmt '6 qseqid sseqid qlen slen bitscore evalue pident nident length qcovs qstat qend sstart send'

blastp -query data/Genomes/Agrobacterium_tumefaciens_LBA4213_\(Ach5\)/GCF_000576515.1_ASM57651v1/GCF_000576515.1_ASM57651v1_protein.faa -out OutputFiles/SQL/AvE.out -db ecoli -evalue 0.01 -outfmt '6 qseqid sseqid qlen slen bitscore evalue pident nident length qcovs qstat qend sstart send'
