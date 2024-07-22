import os 
import re

folder =os.getcwd()
problem_file ="standardize_ips/file"
full_path = os.path.join(folder,problem_file)

def standardips(file):
    with open(file,"r") as prob:
        for x in prob:
            solu =[]
            split_line = re.split(r'[ ,.-]', x)
            for x in split_line:
                if len(x) > 1:
                    cleaned = x.lstrip('0')
                    solu.append(cleaned)
                else:
                    solu.append(x)
            print(f" {solu[0]}.{solu[1]}.{solu[2]}.{solu[3]}")
        
standardips(full_path)