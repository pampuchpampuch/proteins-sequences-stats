import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('datasets_stats.csv')

organisms = ['Bacteria','Viruses','Archaea','Eukaryota']

colors = [plt.cm.Dark2(i) for i in range(len(organisms))]

median_lens = [df[df['dataset']==i].iloc[0]['median seq. length'] for i in organisms]
organisms = [i.replace("_"," ") for i in organisms]
fig,ax = plt.subplots(figsize=(9,6))

rects = ax.bar(organisms,median_lens,color=colors)
ax.set_title('Median lenghts of sequences from 100 proteoms for each kingdom',fontsize=12)
ax.set_ylabel('sequence length',fontsize=12)
ax.set_xlabel('kingdom',fontsize=12)

plt.savefig("barplot_median_kingdoms.png")