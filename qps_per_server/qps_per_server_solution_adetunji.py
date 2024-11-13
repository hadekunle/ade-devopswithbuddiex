import os  

folder =os.getcwd()
problem_file ="log"
full_path = os.path.join(folder,problem_file)

def formated_file(input_file):
    formated =[]
    with open( full_path ,"r") as files :
        file = files.readlines()[1:]
        for x in file:
            listed = x.split(" ")
            formated.append(listed)
        return formated

def get_unique_server(input_file):
    allservers =[]
    with open( full_path ,"r") as files :
        file = files.readlines()[1:]
        for x in file:
            listed = x.split(" ")
            time=listed[1]
            allservers.append(time)
        unique_servers=list(set(allservers))
        return unique_servers
    
def solution(input_file):
    clean_data_set =formated_file(full_path)
    unique_servers=get_unique_server(full_path)
    final_result =[]
    for y in unique_servers:
        count = 0
        total =0
        avgg = 0
        for z in clean_data_set:
            if y == z[1]:
                #total = 0
                count = count +1
                val =int (z[2])
                total = total+ val
                avgg= round(total/count , 2)
            else:
                pass
        final_result.append((y,avgg))
    return final_result
                   
                    
sol = solution(full_path)
for x in sol:
    print(x)
