import os

import pandas as pd

os.system('clear')

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/log'

df = pd.read_csv(path,header=0,sep=' ')
service_df = df.groupby('Service').sum()
print(service_df)

cell = df.groupby('Cell').sum()
print(cell)