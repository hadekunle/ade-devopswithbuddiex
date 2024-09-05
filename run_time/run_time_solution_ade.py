import os

import pandas as pd

os.system('reset')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
df = pd.read_csv(path, sep='\s+')
df = df.reset_index()
df = df.rename(columns={"index": "time"})
df['timestamp'] = df['time'] + ' ' + df['timestamp']
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.drop(columns=['time'])
df = df.sort_values(by=['PID','timestamp'])
process = df['PID'].tolist()
process = sorted(list(set(process)))
for each in process:
    running_total = df.iloc[1]['timestamp'] - df.iloc[1]['timestamp']
    try:
        df_temp = (df[df['PID'] == each])
        if len(df_temp[df_temp['action']=='start']) != 1:
            continue
        if len(df_temp[df_temp['action']=='exit']) != 1:
            continue
        if len(df_temp[df_temp['action']=='pause']) == len(df_temp[df_temp['action']=='resume']) == 0:
            running_total += df_temp.iloc[1]['timestamp']  - df_temp.iloc[0]['timestamp'] 
        if len(df_temp[df_temp['action']=='pause']) !=  len(df_temp[df_temp['action']=='resume']):
            continue

        for i in range(len(df_temp) - 1):
            if (df_temp.iloc[i]['action'] == 'start') and (df_temp.iloc[i+1]['action'] == 'pause'):
                running_total += df_temp.iloc[i+1]['timestamp']  - df_temp.iloc[i]['timestamp'] 
            elif (df_temp.iloc[i]['action'] == 'pause') and (df_temp.iloc[i+1]['action'] == 'resume'):
                pass
            elif (df_temp.iloc[i]['action'] == 'resume') and (df_temp.iloc[i+1]['action'] == 'exit'):
                running_total += df_temp.iloc[i+1]['timestamp']  - df_temp.iloc[i]['timestamp'] 
        print(f'The runtime for PID {each} is {running_total}')
            
    except Exception as e:
        print(e)