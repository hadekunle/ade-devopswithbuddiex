import sys
from datetime import datetime

def calculate_pt(file_path):
    process_times = {}
    process_start = {}

    with open(file_path, 'r') as log_file:
        for line in log_file:
            parts = line.strip().split()
            if len(parts) == 4:
                time_str, date_str, pid, action = parts
                datetime_str = f"{date_str} {time_str}"
                try:
                    datetime_obj = datetime.strptime(datetime_str, "%m/%d/%Y %H:%M:%S")
                except ValueError as e:
                    print(f"Error parsing datetime from line: '{line.strip()}'. Error: {e}")
                    continue  # Skip to next line if there's an error
                
                if action == "start":
                    process_start[pid] = datetime_obj
                elif action == "end" and pid in process_start:
                    duration = datetime_obj - process_start[pid]
                    if pid not in process_times:
                        process_times[pid] = duration
                    else:
                        process_times[pid] += duration
                    del process_start[pid]

    return process_times

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py file")
        sys.exit(1)
    
    file_path = sys.argv[1]
    process_durations = calculate_pt(file_path)

    for pid, duration in process_durations.items():
        days, seconds = duration.days, duration.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{pid} {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}")
