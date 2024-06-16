import os
import re
from tkinter import filedialog as fd
import pandas as pd
os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
path = fd.askopenfilename(
        title='Select a file input',
        initialdir = directory,
        initialfile = path,
        )

def clean_ip(x):
    parts = re.split(r'[-.,\s]+',x)
    part_clean = [str(int(x)) for x in parts]
    combined = ".".join(part_clean)
    return combined

df = pd.read_csv(path,header=None,sep='@')
df['clean'] = df[0].map(lambda x: clean_ip(x))

clean_col = []
for col in range(4):
    new_col = f'col_{col}'
    clean_col.append(new_col)
    df[new_col] = df['clean'].map(lambda x: int(x.split(".")[col]))

df = df.sort_values(by=[*clean_col],ascending=True)
df = df.drop(columns=[0,*clean_col])
df = df.reset_index()
df.index += 1
df = df.drop(columns=['index'])
df = df.rename(columns={'clean': 'SORTED IP ADDRESSES'}) 
print(df)