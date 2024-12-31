from collections import defaultdict

from q4info import Forlogs


def highest_branch(Forlogs):
    branch_files = defaultdict(set)
    largest_branch = ("",0)
    for line in Forlogs:
        line = line.strip().split()
        cmd, file_name = line
        if cmd =='switch':
            branch_name = line[1]
        elif cmd =='push':
            branch_files[branch_name].add(file_name)
            count = len(branch_files[branch_name])
            if count > largest_branch[1]:
                largest_branch = (branch_name, count)

    return largest_branch[0]


print(highest_branch(Forlogs))