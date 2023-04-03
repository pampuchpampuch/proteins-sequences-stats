import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Bio import SeqIO

organisms = ['Bacteria','Viruses','Archaea','Eukaryota']

colors = [plt.cm.Dark2(i) for i in range(len(organisms))]

all_seq_lens=[]

for i in range(len(organisms)):
    dataset=organisms[i]
    seq_lens=[]
    fasta=open(dataset+'.fasta','r')
    for record in SeqIO.parse(fasta, "fasta"):
        seq_lens.append(len(record.seq))
    all_seq_lens.append(seq_lens)

organisms = [i.replace("_"," ") for i in organisms]
fig,ax = plt.subplots(figsize=(9,6))

bplot = ax.boxplot(all_seq_lens, showfliers=False,labels=organisms,patch_artist=True)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Lenghts of sequences from 100 proteoms for each kingdom',fontsize=12)
ax.set_ylabel('sequence length',fontsize=12)
ax.set_xlabel('kingdom',fontsize=12)

plt.savefig("boxplot_kingdoms.png")
