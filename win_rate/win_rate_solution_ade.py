import os

import pandas as pd

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
team_name = 'ABC'

df = pd.read_csv(path,header=0,sep=' ')
df = df.rename(columns={'Guest': 'Away'}) 
df['Home_Score'] = df['Result'].map(lambda x:int(x.split('-')[0]))
df['Away_Score'] = df['Result'].map(lambda x:int(x.split('-')[1]))
df['Win'] = 0
df['Win_Streak'] = 0

for i in range(len(df)):
    if True and \
        ((df.iloc[i]['Home'] == team_name.upper()) and (df.iloc[i]['Home_Score'] > df.iloc[i]['Away_Score'])) or \
        ((df.iloc[i]['Away'] == team_name.upper()) and (df.iloc[i]['Away_Score'] > df.iloc[i]['Home_Score'])):
        
        df.loc[i, 'Win'] = 1

win_ratio = df['Win'].mean() * 100

if df.iloc[0]['Win'] == 1:
    df.loc[0, 'Win_Streak'] = 1

for i in range(1,len(df)):
    if df.iloc[i]['Win'] and df.iloc[i-1]['Win']:
        df.loc[i, 'Win_Streak'] = 1 + df.loc[i-1, 'Win_Streak']
    elif df.iloc[i]['Win'] and not df.iloc[i-1]['Win']:
        df.loc[i, 'Win_Streak'] = 1

winning_streak = df['Win_Streak'].max()

df.index += 2
print(df)
print(f"\nTeam {team_name}'s win percentage is {win_ratio:.2f}%")
print(f"Team {team_name}'s longest winning streak is {winning_streak} win(s)!")











# win_rate = df.groupby('Win').count()['Result']
# win_rate = win_rate.reset_index()['Result']
# win_ratio = win_rate[1]/(win_rate[0]+win_rate[1]) * 100
