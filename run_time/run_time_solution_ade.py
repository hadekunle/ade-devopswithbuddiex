import os
import pandas as pd
os.system('reset')

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

df = pd.read_csv(path, sep='\s+')
df = df.reset_index()
df = df.rename(columns={"index": "time"})
df['timestamp'] = df['time'] + ' ' + df['timestamp']
df = df.drop(columns=['time'])

df_start = df[df['action']=='start']
df_exit = df[df['action']=='exit']

df = df_start.set_index('PID').join(df_exit.set_index('PID'),how='inner',lsuffix='_start',rsuffix='_exit')

df['timestamp_start'] = pd.to_datetime(df['timestamp_start'])
df['timestamp_exit'] = pd.to_datetime(df['timestamp_exit'])
# print(df.dtypes['timestamp_start'])
df['runtime'] = df['timestamp_exit'] - df['timestamp_start']
df = df[['runtime']]
df = df.reset_index()
print(df)
