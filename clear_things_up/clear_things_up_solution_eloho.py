from datetime import datetime, timedelta
import sys
from collections import defaultdict

def process_file(file):
    data = defaultdict(list)
    file = sys.argv[1]

    with open(file) as f:
        next(f)
        for line in f:
            time_str, date_str, pid, action = line.strip().split()
            timestamp = datetime.strptime(f"{date_str} {time_str}", "%m/%d/%Y %H:%M:%S")
            
            if action == 'start':
                data[pid].append(timestamp)
            elif action == 'end' and pid in data:
                start_time = data[pid][0]
                end_time = timestamp
                time_spent = end_time - start_time
                data[pid].append({'time_spent': time_spent})
    sorted_data = defaultdict(list, sorted(data.items(), key=lambda x: x[0]))
    return sorted_data


def output_result(data):
    for pid, time in data.items():
        if len(time) > 1 and 'time_spent' in time[1]:
            print(f"{pid} {time[1]['time_spent']}")
    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clear_things_up_solution_eloho.py <file1>")
        sys.exit(1)
    output_result(process_file(sys.argv[1]))