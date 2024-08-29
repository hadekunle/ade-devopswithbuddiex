import os

import pandas as pd

os.system('reset')
base_directory = os.path.dirname(os.path.abspath(__file__))
file1 = f'{base_directory}/file1'
file2 = f'{base_directory}/file2'

df1 = pd.read_csv(file1, delim_whitespace=True)
df2 = pd.read_csv(file2, delim_whitespace=True)
df = df1.set_index('Server').join(df2.set_index('Server'),how='inner')
df['disk_usage%'] = round(df['Space_used(TB)'] / df['Total_space(TB)'] *100 ,2)
df = df.sort_values(by=['disk_usage%'], ascending = True)
df = df.reset_index()
df.index += 1
print(df)