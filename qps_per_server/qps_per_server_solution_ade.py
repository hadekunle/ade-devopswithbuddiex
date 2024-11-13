import os

import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/log'
os.system('clear')

df = pd.read_csv(path,sep='\s+')
df = df.groupby('Server_ID').mean('Query_ID')
print(df)