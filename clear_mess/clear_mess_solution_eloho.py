import re
import sys


def clear_mess(file):
    username_pattern = r"([a-zA-Z])"
    phone_number_pattern = r"(\d{3}-\d{3}-\d{4})"
    start_date_pattern = r"(\d{2}\/\d{2}\/\d{4})"
    data = {}
    print("clearing mess!!!")
    with open(file) as f:
        for line in f:
            username_match = re.findall(username_pattern, line)
            phone_number_match = re.findall(phone_number_pattern, line)
            start_date_match = re.findall(start_date_pattern, line)
            username = "".join(username_match)
            phone_number = "".join(phone_number_match)
            start_date = "".join(start_date_match)
            if username and phone_number and start_date:
                data[username] = {"phone_number": phone_number, "start_date": start_date}
        sorted_data = dict(sorted(data.items()))
    return sorted_data


def output_file(data):
    print("writing to file > output!!!")
    header = "Username Phone_num Start_date\n"
    with open("output", "w") as f:
        f.write(header)
        for key, value in data.items():
            f.write(f"{key} {value['phone_number']} {value['start_date']}\n")






if __name__ == "__main__":
    if len(sys.argv) == 2:

        output_file(clear_mess(sys.argv[1]))
    else:
        print("Usage: python active_user_solution_eloho.py file")
        sys.exit(1)
    
    