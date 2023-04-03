import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('datasets_stats.csv')

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

labels = list(groups.keys())
handles = [plt.Rectangle((0,0),1,1, color=plt.cm.Dark2(i)) for i in range(len(labels))]
plt.legend(handles, labels)

median_lens = [df[df['dataset']==i].iloc[0]['median seq. length'] for i in organisms]
organisms = [i.replace("_"," ") for i in organisms]
fig,ax = plt.subplots(figsize=(9,6))

rects = ax.bar(organisms,median_lens,color=colors)
ax.set_title('Median lenghts of sequences from proteoms',fontsize=12)
ax.set_ylabel('sequence length',fontsize=12)
ax.set_xlabel('organism',fontsize=12)
ax.legend(handles, labels, loc='upper left')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.25)

plt.savefig("barplot_median_organisms.png")
