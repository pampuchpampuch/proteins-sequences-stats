import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('datasets_stats.csv')

organisms = ['swiss_prot','Bacteria','Viruses','Archaea','Eukaryota']

colors = [plt.cm.Dark2(i) for i in range(len(organisms))]

mean_lens = [df[df['dataset']==i].iloc[0]['mean seq. length'] for i in organisms]
error_est = [df[df['dataset']==i].iloc[0]['error (std)'] for i in organisms]
organisms = [i.replace("_"," ") for i in organisms]
fig,ax = plt.subplots(figsize=(9,6))

rects = ax.bar(organisms,mean_lens,yerr=error_est,capsize=3,color=colors)
ax.set_title('Mean lenghts of sequences from different data sets',fontsize=12)
ax.set_ylabel('sequence length',fontsize=12)
ax.set_xlabel('data set',fontsize=12)

plt.savefig("barplot_mean_uniprot.png")