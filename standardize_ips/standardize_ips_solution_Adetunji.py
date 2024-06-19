import os 
import re

folder =os.getcwd()
problem_file ="standardize_ips/file"
full_path = os.path.join(folder,problem_file)

def sort_ips(file):
    with open(file,"r") as ips:
        ordered=[]
        for x in ips:
            split_line = re.split(r'[ ,.-]+', x)
            first =split_line[0]
            ordered.append(int(first))
        sorted_list = sorted(ordered)    
    return(sorted_list)
            
def standardips(file):
    sorted =sort_ips(full_path)
    solution=[]
    with open(file,"r") as prob:
        final=[]
        for x in prob:
            solu =[]
            split_line = re.split(r'[ ,.-]+', x)
            for x in split_line:
                if len(x) > 1:
                    cleaned = x.lstrip('0')
                    solu.append(cleaned)
                else:
                    solu.append(x)
            final.append(f" {solu[0]}.{solu[1]}.{solu[2]}.{solu[3]}")
 
        for x in sorted:
            for c in final:
                first_oct_= int(c.split(".")[0])
                if x == first_oct_:
                    #print (c)
                    solution.append(c)
        return solution
for x in standardips(full_path):
    print(x)

