from Bio import SeqIO
from collections import Counter
from numpy import median, std, sqrt, round
import pandas as pd

def get_stats(fasta):
    aminoacids='ACDEFGHIKLMNPQRSTVWY'
    seq_lens=[]
    seq_n=0
    aa_sum_avg={i:0 for i in aminoacids}
    n_term_aa={i:0 for i in aminoacids}
    for record in SeqIO.parse(fasta, "fasta"):
        seq_len=len(record.seq)
        seq_lens.append(seq_len)
        seq_n+=1
        if record.seq[0] in aminoacids:
            n_term_aa[record.seq[0]]+=1
        for aa in aminoacids:
            aa_sum_avg[aa]+=record.seq.count(aa)/seq_len
    seq_len_mean=sum(seq_lens)/seq_n
    mean_std=std(seq_lens)/sqrt(seq_n)
    seq_len_median=median(seq_lens)
    seq_aa_content=[round(aa_sum_avg[aa]*100/seq_n, decimals=1) for aa in aminoacids]
    n_term = max(n_term_aa, key=n_term_aa.get)
    
    return [seq_n, seq_len_mean, mean_std] + seq_aa_content + [n_term,seq_len_median]

A_organisms=['E._coli', 'Bacillus_subtilis', 'human', 'yeast',
            'A._thaliana', 'D._melanogaster', 'C._elegans', 'Mouse', 'Zebrafish']

C_organisms=['Bacteria','Viruses','Archaea','Eukaryota']

datasets=A_organisms+['pdb','swiss_prot']+C_organisms

dataset_stats=[]
for dataset in datasets:
    fasta=open(dataset+'.fasta','r')
    print(dataset)
    dataset_stats.append([dataset]+get_stats(fasta))
    fasta.close()

col_names=['dataset','no. of sequences', 'mean seq. length', 'error (std)']+[aa for aa in 'ACDEFGHIKLMNPQRSTVWY']+['n-terminus aa','median seq. length']

df = pd.DataFrame(dataset_stats,columns=col_names)
df.to_csv('datasets_stats.csv',index=False)



