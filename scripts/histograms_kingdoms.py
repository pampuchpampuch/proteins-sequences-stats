import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO

organisms=['Bacteria','Viruses','Archaea','Eukaryota']


fig, axs = plt.subplots(2, 2, tight_layout=True,figsize=(8,8))

axs_idx=[(i,j) for i in range(2) for j in range(2)]

for i in range(len(organisms)):
    dataset=organisms[i]
    seq_lens=[]
    fasta=open(dataset+'.fasta','r')
    for record in SeqIO.parse(fasta, "fasta"):
        seq_lens.append(len(record.seq))
    
    counts, bins, other_ = axs[axs_idx[i]].hist(seq_lens, bins=40)
    axs[axs_idx[i]].set_title(organisms[i].replace("_"," "))
    axs[axs_idx[i]].set_ylabel('Frequency')
    axs[axs_idx[i]].set_xlabel('Sequence lenght')
    axs[axs_idx[i]].set_xticks([0,max(bins)/2,max(bins)])
    axs[axs_idx[i]].set_yticks([0,max(counts)/2,max(counts)])
    # axs[axs_idx[i]].locator_params
plt.savefig("histogram_kingdoms.png")

    



