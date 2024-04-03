import sys



def create_usernames(args):
    data = {}
    with open(args) as f:
        counter = 2
        next(f)
        for line in f:
            firstname, lastname, emp_ID, startdate = line.strip().split()
            username = firstname[0].lower() + lastname.lower()
            if username not in data.keys():
                data[username] = {"firstname": firstname, "lastname": lastname, "emp_ID": emp_ID, "startdate": startdate, "username": username}
            elif username in data.keys():
                username = username + str(counter)
                data[username] = {"firstname": firstname, "lastname": lastname, "emp_ID": emp_ID, "startdate": startdate, "username": username}
                counter += 1
    return data



def output_file(data):
    header = "Firstname Lastname EmployeeID StartDate Username\n"
    with open("output", "w") as f:
        f.write(header)
        for key, value in data.items():
            f.write(f"{value['firstname']} {value['lastname']} {value['emp_ID']} {value['startdate']} {value['username']}\n")


def main():
    output_file(create_usernames(sys.argv[1]))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()   
        print("Usernames created!!!")
    else:
        print("Usage: python create_usernames_solution_eloho.py file")
        sys.exit(1)

