import os

import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/log'
os.system('reset')

def qps():
    summary_dict = { }
    with open(path,'r') as file:
        next(file)
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            time, date, server, q = line.split()
            
            if server not in summary_dict.keys():
                summary_dict[server] = [0,0]
            summary_dict[server][0] += int(q)
            summary_dict[server][1] += 1
        
        for server in summary_dict.keys():
            qps = int(summary_dict[server][0])/int(summary_dict[server][1])
            summary_dict[server] = f'{qps:.2f}'
        return summary_dict

print(qps())

