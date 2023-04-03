import gzip
import shutil
from urllib import request
from random import sample
from Bio import SeqIO
from collections import Counter
import requests
from io import StringIO
import pandas as pd

def download_pdb():
    url = 'https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt.gz'
    local='pdb_seqres.txt.gz'
    request.urlretrieve(url, local)
    with gzip.open(local, 'rb') as f_in:
        with open('pdb.fasta', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def download_swiss_prot():
    url = 'https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz'
    local='uniprot_sprot.fasta.gz'
    request.urlretrieve(url, local)
    with gzip.open(local, 'rb') as f_in:
        with open('swiss_prot.fasta', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

A_organisms=['E._coli', 'Bacillus_subtilis', 'human', 'yeast',
            'A._thaliana', 'D._melanogaster', 'C._elegans', 'Mouse', 'Zebrafish']

A_proteoms_ids=['UP000000625','UP000001570','UP000005640','UP000002311','UP000006548','UP000000803','UP000001940','UP000000589','UP000000437']

#download A datasets
for i in range(len(A_organisms)):
    fasta = requests.get('https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=fasta&query=proteome:'+A_proteoms_ids[i]).text
    fasta_file = open(A_organisms[i]+'.fasta','w')
    fasta_file.write(fasta)
    fasta_file.close()

#download B dataset
download_pdb()

#download C datasets
download_swiss_prot()

C_organisms=['Bacteria','Viruses','Archaea','Eukaryota']
C_ids=["2","10239","2157","2759"]

url_1='https://rest.uniprot.org/proteomes/stream?compressed=false&fields=upid&format=tsv&query=%28%28taxonomy_id%3A'
url_2='%29%29%20AND%20%28proteome_type%3A1%29'

seq_lens={}
aa_content={}

for i in range(len(C_organisms)):
    proteoms_ids=requests.get(url_1+C_ids[i]+url_2).text.strip().split('\n')[1:]
    proteoms_ids=sample(proteoms_ids,100)
    query = '+OR+proteome:'.join(proteoms_ids)
    fasta = requests.get('https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=fasta&query=proteome:'+query).text
    fasta_file = open(C_organisms[i]+'.fasta','w')
    fasta_file.write(fasta)
    fasta_file.close()
