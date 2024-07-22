import os

import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
os.system('clear')

df = pd.read_csv(path,names=['server','date','_','disk_usage'],sep=' ')
print(df[(df['disk_usage'].map(lambda x: float(x.strip('%')))) > 85].map(lambda x: str(x)+'%').reset_index().drop(columns=['index','_','date']))













# df = pd.read_csv(path,names=['server','date','_','disk_usage'],sep=' ')
# df['disk_usage'] = df['disk_usage'].map(lambda x: float(x.strip('%')))
# df = df[df['disk_usage'] > 85].map(lambda x: str(x)+'%')
# df = df.reset_index().drop(columns=['index','_','date'])
# print(df)

