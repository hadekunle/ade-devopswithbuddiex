import os

import pandas as pd

os.system('clear')

base_directory = os.path.dirname(os.path.abspath(__file__))
file = f'{base_directory}/fileA'
valid_data_types = ['int64','float64','datetime64[ns]','timedelta',]

def my_sort(file,col):
    df = pd.read_csv(file,header=None, sep=' ')
    data_type = df.dtypes[col]

    if data_type in valid_data_types:
        df= df.sort_values(by=col)
        df = df.reset_index()
        df = df.drop(columns=['index'])
        print(df)
    else:
        print(f'Column {col} has d.type of {data_type}\nNot in valid d.type(s)\n{valid_data_types}')

my_sort(file,0)








# df[1] = pd.to_datetime(df[1])
# print('Data type of each column\n')
# print(df.info())
