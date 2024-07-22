import os

import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
filename='newfile'
path = f'{directory}/{filename}'
os.system('clear')

df = pd.read_csv(path,names=['username','groupname','userid','homepath'],sep=' ', dtype= str )
df = df.sort_values(by=['groupname','userid'], ascending = [True,False])
df = df.reset_index().drop(columns=['index'])
print(df)

