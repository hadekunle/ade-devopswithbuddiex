import re
from pprint import pprint

def find_valid_ips(file_path):
    ip_pattern = re.compile(
        r"""
        \b                       # word boundary
        (?!0\d)                  # no leading zero unless the value is 0
        (?:                      # non-capturing group
        25[0-5]|                 # range 250-255
        2[0-4][0-9]|             # range 200-249
        1[0-9]{2}|               # range 100-199
        [1-9]?[0-9]              # range 0-99
        )                        # end of group
        (?:                      # non-capturing group
        \.                       # dot
        (?!0\d)                  # no leading zero unless the value is 0
        (?:                      # non-capturing group
        25[0-5]|                 # range 250-255
        2[0-4][0-9]|             # range 200-249
        1[0-9]{2}|               # range 100-199
        [1-9]?[0-9]              # range 0-99
        )                        # end of group
        ){3}                     # repeat 3 times
        \b                       # word boundary
        """, re.VERBOSE)

    
    
    valid_ips = []

    with open(file_path, 'r') as file:
        for line in file:
            possible_ips = ip_pattern.findall(line)
            valid_ips.extend(possible_ips)

    return valid_ips


valid_ips = find_valid_ips('find_valid_ips/file')
pprint(valid_ips)
