from datetime import datetime, timedelta
import sys

def clear_time(file):
    """A function that acepts a log file of processes and calculates time spent for each process."""
    interval_map = {}
    with open (file, 'r') as process_intervals:
        next(process_intervals)
        for line in process_intervals:
            line = line.strip()
            time, date, pid, action = line.split()
            time_date = f"{time} {date}"
            time_date = datetime.strptime(time_date, "%H:%M:%S %m/%d/%Y")
            if pid not in interval_map and action.lower() == "start":
                interval_map[pid] = [time_date, "process did not end"]
            elif pid in interval_map and action.lower() == "end":
                interval_map[pid][1] =  time_date - interval_map[pid][0]
        
        for pid, values in interval_map.items():
            print(f"{pid} {values[1]}")

def main():
    log_file = sys.argv[1]
    if len(sys.argv) != 2:
        sys.exit("please provide one valid log file")
    clear_time(log_file)

if __name__ == "__main__":
    main()
