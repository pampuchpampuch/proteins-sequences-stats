import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('datasets_stats.csv')

aa=[i for i in 'ACDEFGHIKLMNPQRSTVWY']

datasets=['E._coli','human','yeast']
colors = []
organisms_aa={}

for i in datasets:
    organisms_aa[i.replace("_"," ")]=list(df[df['dataset']==i].iloc[0,4:24])

x = np.arange(len(aa))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(figsize=(8,7))

for attribute, measurement in organisms_aa.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1

ax.set_ylabel("content [%]")
ax.set_xlabel("aminoacid")
ax.set_title('Aminoacid contens by organism')
plt.xticks(x + width, labels=aa)
ax.legend(loc='upper left',ncol=3)
ax.set_ylim(0, 12)
ax.set_axisbelow(True)

plt.grid(axis='y')

plt.savefig("barplot_aa_organisms.png")
