# Updates the genomes in the Genomes folder by querying the NCBI rsync database

import pandas as pd
from subprocess import call


euk = pd.read_table('data/ASSEMBLY_REPORTS/assembly_summary_refseq.txt', header=1, low_memory=False)
euk[['organism_name', 'taxid', 'ftp_path']]


# An example path
for i in range(10):
    ftp_str = euk.loc[i]['ftp_path']
    rsync_str = ftp_str.replace('ftp', 'rsync')
    command_str = 'rsync -avz ' + rsync_str + ' ' + str(euk.loc[i]['organism_name']).replace(' ', '_')
    call(["rsync", "-avz", rsync_str, 'data/Genomes/' + str(euk.loc[i]['organism_name']).replace(' ', '_')])
