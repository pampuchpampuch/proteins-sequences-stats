import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Bio import SeqIO

groups={'vertebrates':['human','Mouse','Zebrafish'],
        'bacteria':['E._coli','Bacillus_subtilis'],
        'invertebrates':['D._melanogaster','C._elegans'],
        'fungi':['yeast'],
        'green plants':['A._thaliana']}

colors = []
organisms=[]
for i,k in enumerate(groups.keys()):
    colors+=[plt.cm.Dark2(i) for j in groups[k]]
    organisms+=groups[k]

all_seq_lens=[]

for i in range(len(organisms)):
    dataset=organisms[i]
    seq_lens=[]
    fasta=open(dataset+'.fasta','r')
    for record in SeqIO.parse(fasta, "fasta"):
        seq_lens.append(len(record.seq))
    all_seq_lens.append(seq_lens)

labels = list(groups.keys())
handles = [plt.Rectangle((0,0),1,1, color=plt.cm.Dark2(i)) for i in range(len(labels))]
plt.legend(handles, labels)

organisms = [i.replace("_"," ") for i in organisms]
fig,ax = plt.subplots(figsize=(9,6))

bplot = ax.boxplot(all_seq_lens, showfliers=False,labels=organisms,patch_artist=True)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Lenghts of sequences from proteoms',fontsize=12)
ax.set_ylabel('sequence length',fontsize=12)
ax.set_xlabel('organism',fontsize=12)
ax.legend(handles, labels, loc='upper left')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.25)

plt.savefig("boxplot_organisms.png")
