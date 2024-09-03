import os
import pandas as pd
os.system('reset')

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/log.txt'

column_names = ['user','date','score','color']
df = pd.read_csv(path, sep=',', names=column_names)
df = df[df['score'] >= 85]
df = df[['user','color']]
df = df.reset_index()
df = df.drop(columns=['index'])

print(df)
