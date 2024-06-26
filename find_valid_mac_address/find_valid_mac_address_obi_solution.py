import re
import sys
from pprint import pprint
def find_valid_mac_addresses(file_path):
    # Regular expression pattern for valid MAC addresses
    mac_pattern = re.compile(r'\\b([0-9A-F]{2}:){5}[0-9A-F]{2}\\b')

    valid_macs = []  

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Search for valid MAC addresses in each line
            search_result = mac_pattern.search(line)
            if search_result:
                # Split the line by spaces and get the server and MAC address
                server, mac_address = line.split()[0:2]
                valid_macs.append((server, mac_address))

    return valid_macs


# valid_macs = find_valid_mac_addresses('/Users/saitama/Documents/GitHub/WeeklyCode/find_valid_mac_address/file')
# print(valid_macs)


if __name__ == "__main__":
    valid_macs = find_valid_mac_addresses('/Users/saitama/Documents/GitHub/WeeklyCode/find_valid_mac_address/file')
    print(valid_macs)
    # if len(sys.argv) < 1:
    #     print("Usage: python3 script.py log_file")
    #     sys.exit(1)
    # for i in sys.argv:
    #     pprint(i)
    # file = sys.argv[0]
    
    # valid_macs = find_valid_mac_addresses(file)
    # pprint(valid_macs)