import sys
from datetime import datetime, timedelta

def run_time(inputfile):
    process_map = {}
    with open(inputfile, 'r') as lines:
        next(lines)
        for line in lines:
            time, data, pid, action = line.strip().split()
            time_and_date = datetime.strptime(" ".join([time, data]), "%H:%M:%S %m/%d/%Y")
            if pid not in process_map and action == "start":
                process_map[pid] = [time_and_date, timedelta(0), timedelta(0), timedelta(0)]
            elif pid in process_map and action == "pause":
                process_map[pid][1] = time_and_date
            elif pid in process_map and action == "resume":
                process_map[pid][2] = time_and_date
            elif pid in process_map and action == "exit":
                process_map[pid][3] = time_and_date

        for pid, value in process_map.items():
            if value[3] != timedelta(0):
                if value[2] != timedelta(0) and value[1] != timedelta(0):
                    runtime = (value[1] - value[0]) + (value[3] - value[2])
                    print(f"pid {pid}: runtime {runtime}")
                else:
                    runtime = (value[3] - value[0])
                    print(f"pid {pid}: runtime {runtime}")


def main():
    input_file = sys.argv[1]
    run_time(input_file)

if __name__ == "__main__":
    main()