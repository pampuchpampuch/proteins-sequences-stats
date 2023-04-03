import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('datasets_stats.csv')

aa=[i for i in 'ACDEFGHIKLMNPQRSTVWY']

datasets=['swiss_prot','Bacteria','Viruses','Archaea','Eukaryota']
colors = []
organisms_aa={}

df = df[df['dataset'].isin(datasets)]

rows=[df[i] for i in aa]
for i in datasets:
    organisms_aa[i.replace("_"," ")]=list(df[df['dataset']==i].iloc[0,4:24])

df2 = df[df['dataset'].isin(datasets)]
cols = df2['dataset']
rows=[df2[i] for i in aa]
df2 = pd.DataFrame(rows)
df2['aminoacid'] = df2.index
df2.columns=list(cols)+['aminoacid']
df2 = df2.reindex(columns=['aminoacid']+list(cols))

plt.rc('axes', axisbelow=True)

df2.plot(x='aminoacid',kind='bar',stacked=False, title="Aminoacids' contens by dataset",figsize=(9,6))
plt.grid(axis='y')
plt.legend(loc='upper center',ncol=5)
plt.ylim(0,12)
plt.ylabel('content [%]')

plt.savefig("barplot_aa_uniprot.png")