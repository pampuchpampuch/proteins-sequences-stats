import pandas as pd

df = pd.read_csv('datasets_stats.csv')

organisms=['E._coli', 'Bacillus_subtilis', 'human', 'yeast',
            'A._thaliana', 'D._melanogaster', 'C._elegans', 'Mouse', 'Zebrafish']

kingdoms = ['swiss_prot','Bacteria','Viruses','Archaea','Eukaryota']

#part 1

df_org = df[df['dataset'].isin(organisms)]

#organisms - aa content

print('average aa content for (a)')

print(df_org[[i for i in 'ACDEFGHIKLMNPQRSTVWY']].transpose().reset_index().rename(columns=df_org['dataset']).rename(columns = {'index':'aminoacid','Bacillus_subtilis': 'B._subtilis','D._melanogaster':'D._melanog.'}).to_markdown(index=False,tablefmt="github"))

#organisms - prot length


print('average protein length for (a)')

print(df_org[['mean seq. length']].transpose().rename(columns=df_org['dataset']).rename(columns = {'index':'aminoacid','Bacillus_subtilis': 'B._subtilis','D._melanogaster':'D._melanog.'}).to_markdown(tablefmt="github"))

#swiss + kingdoms - aa content

df_uniprot = df[df['dataset'].isin(kingdoms)]

print('average aa content for (c)')

print(df_uniprot[[i for i in 'ACDEFGHIKLMNPQRSTVWY']].transpose().reset_index().rename(columns=df_uniprot['dataset']).rename(columns = {'index':'aminoacid','Bacillus_subtilis': 'B._subtilis','D._melanogaster':'D._melanog.'}).to_markdown(index=False,tablefmt="github"))
#swiss + kingdoms - prot length

print('average protein length for (c)')

print(df_uniprot[['mean seq. length']].transpose().rename(columns=df_uniprot['dataset']).to_markdown(tablefmt="github"))
#part 2

#pdb - aa content

#pdb - prot length