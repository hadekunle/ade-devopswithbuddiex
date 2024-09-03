import os

import pandas as pd

os.system('reset')
base_directory = os.path.dirname(os.path.abspath(__file__))
file = f'{base_directory}/file'

column_names = ['permissions','user','date','filename']
df = pd.read_csv(file, sep='\s{2,}|\t', names = column_names, engine='python')
df['date'] = pd.to_datetime(df['date'])
df= df.sort_values(by=['date','filename'], ascending = [False,False])
df = df.reset_index().drop(columns=['index'])
df['date'] = df['date'].dt.strftime('%B %d, %Y')
df = df[['filename','date']]
print(df.head()) #only shows the top 5 rows by default