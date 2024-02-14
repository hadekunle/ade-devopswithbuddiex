import os
default_number = "444-123-1233"



def readfiles(file):
    # check if file exist
    if file is None:
        print("Error: No file")
    else:
        with open(file, "r") as file:
            rows = (line.split(" ", 1) for line in file) #lpalmer@hotmail.com, (258) 549-4757
            dict = {row[0]: row[1].strip() for row in rows}
            for key, value in dict.items():
                print(f"{key}: {value}")
            return dict


result = {}


def isactive(activeA, activeB):
    for key, value in activeB.items():
        if value == "Yes":
            partial_string = key
            for k, v in activeA.items():
                if partial_string in k:
                    if v is None:
                        v = default_number
                    result[key] = v

    return result


# def checkforfiles():
#     thisdir = os.getcwd()

#     #check for files in the directory
#     for f in os.walk(thisdir):
#         for file in f


def checkIffilesexist():
    try:
        arr = os.listdir("active_users")
        
        for n in arr:
            if "file" in n:
                print(n)
                currentdir = os.path.join("active_users", n)
                with open(currentdir, 'r') as file:
                    f = file.read()
                    print(f)
                search_word = "@"
                search_word2 = "Username"
                if search_word in f:
                    fir = currentdir
                    
                if search_word2 in f:
                    t =currentdir 
        filea = readfiles(fir)
        fileb = readfiles(t)
        res = isactive(filea,fileb) 
        with open("active_users/Obi_answer", 'w') as final:
            for key, value in res.items():
                print(f"{key} {value}") 
                final.write('{0}, {1}\n'.format(key,value))                 
    except FileNotFoundError:
        print("Doesn't exist")

         


def main():
    print("welcome")
    checkIffilesexist()
   

    


if __name__ == "__main__":
    main()
