from os import path, system
from sys import argv as argument

import pandas as pd

system('clear')

def overload(log_file):
    df = pd.read_csv(log_file, delim_whitespace=True, names=['server', 'time', 'date', 'cpu_load', 'ram_load', 'disk_usage'], header=None)
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df['high_load'] = (df['cpu_load'] >= 0.80)
    # df_view = df[['datetime', 'cpu_load', 'high_load']]
    # print(df_view.head(10))

    for i in range(len(df) - 1):
        time_diff = df.iloc[i + 1]['datetime'] - df.iloc[i]['datetime']
        
        if df['high_load'].iloc[i] and df['high_load'].iloc[i + 1] \
            and (df.iloc[i]['server'] == df.iloc[i + 1]['server']) \
            and time_diff == pd.Timedelta(minutes=1):
            
            start_time = df.iloc[i]['datetime']
            end_time = df.iloc[i + 1]['datetime']
            server = df.iloc[i]['server']
            print(f"Warning: server {server} CPU load is over 80% from {start_time.strftime('%H:%M:%S %m/%d/%Y')} to {end_time.strftime('%H:%M:%S %m/%d/%Y')}")

def main():
    if len(argument) > 2:
        error_message="\nDon't forget to pass in the log file ONLY"
        raise ValueError(f"{error_message}")
    elif len(argument) == 2 :
        log_file = argument[1]
    else:
        log_file = './overloaded_servers/log'

    if not path.exists(log_file):
        raise FileNotFoundError(f"{log_file} does not exist")

    overload(log_file)

        
if __name__ == "__main__":
    main()