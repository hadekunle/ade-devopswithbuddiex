import os
import re

import pandas as pd

os.system('clear')

'''
Reminders:
remind all to check remove_soft_links folder
overloaded server bobjay soln
'''

def list_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if (re.findall(r'\blog\d+\b',str(file))):
                full_path = os.path.join(root, file)
                all_files.append(full_path)
    return all_files


def combine_logs(log_files):
    dataframes = [pd.read_csv(log_file, delim_whitespace=True, \
                names=['time', 'date', 'function', 'id', 'item1', 'item2', 'item3'], \
                header=None) for log_file in log_files]
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df


def rearrange_logs(directory,master_df,action):
    df = master_df
    df.fillna(value='',inplace=True)
    df['item'] = (df['item1']+' '+ df['item2']+' '+ df['item3'])
    df['item'] = df['item'].map(lambda x: x.strip())
    df_view = df[['time', 'date', 'function', 'id', 'item']]
    df_view = df_view[df_view['function'] == action ]
    df_view.to_csv(f'{directory}/pandas_{action.lower()}_log', sep=' ', index=False,mode='w',header=False) 

    print(df_view)
    return df_view


def clean_up_add_log(directory):
    file_path = f'{directory}/pandas_add_log'
    with open(file_path,'r') as file:
        lines = file.readlines()
        replaced_lines = [line.replace("\"",'') for line in lines]
    with open(file_path, 'w') as file:
        file.writelines(replaced_lines)


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    all_files = list_files(directory)
    master_df = combine_logs(all_files)
    
    for action in ('Get','Set','Add',):
        df_view = rearrange_logs(directory,master_df,action)

        date_counts = df_view.groupby('date').count()
        date_counts = date_counts['time']
        # print(type(date_counts))
        date_counts = date_counts.reset_index()
        date_counts.columns = [f'{action}', '']
        print(date_counts)

        date_counts.to_csv(f'{directory}/pandas_stats_log', sep=' ', index=False,mode='a',header=True) 

        if os.path.exists(f'{directory}/pandas_add_log'):
            clean_up_add_log(directory)
        else:
            print('No add log file to clean')

if __name__ == "__main__":
    main()