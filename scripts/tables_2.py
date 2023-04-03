import pandas as pd

df = pd.read_csv('datasets_stats.csv')

#part 1

df = df[df['dataset'].isin(['pdb'])]

#organisms - aa content

print('average aa content for pdb')

print(df[[i for i in 'ACDEFGHIKLMNPQRSTVWY']].transpose().reset_index().rename(columns=df['dataset']).rename(columns={'index':'aminoacid'}).to_markdown(index=False,tablefmt="github"))

#organisms - prot length


print('average protein length for pdb')

print(df[['mean seq. length']].transpose().rename(columns=df['dataset']).to_markdown(tablefmt="github"))