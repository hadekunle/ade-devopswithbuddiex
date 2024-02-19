import sys
from datetime import datetime
from collections import defaultdict 

output_file = "binary_queue_eloho"

def process_file(file):
    data = defaultdict(list)
    file = sys.argv[1]

    with open(file) as f:
        next(f)
        for line in f:
            binary, time_str, date_str, status = line.strip().split()
            timestamp = datetime.strptime(f"{time_str} {date_str}", "%H:%M:%S %m/%d/%Y")
            data[binary].append((timestamp, status))
    return data


def check_status(data):
    ongoing_process = defaultdict(list)
    for binary, status in data.items():
        if status[0][1] == 'running' or status[0][1] == 'queued':
            ongoing_process[binary] = status
    return ongoing_process


def custom_sort(item):
    timestamp, status = item
    return(status, timestamp)

def output_result(data, output_file):
    sorted_items = sorted(data.items(), key=lambda x: custom_sort(x[1][0]))
    sorted_data = defaultdict(list, sorted_items)

    with open(output_file, "w") as f:
        f.write("binary created_at status")
        f.write("\n")
        for binary, status in sorted_data.items():
            f.write(f"{binary} {status[0][0].strftime('%H:%M:%S %m/%d/%Y')} {status[0][1]}")
            f.write("\n")        
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python binary_queue_solution_eloho.py <file1>")
        sys.exit(1)
    output_result(check_status(process_file(sys.argv[1])), output_file)