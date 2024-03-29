import sys
from datetime import datetime, timedelta

# Function to calculate the average timespan from intervals in a file
def avg_time(file):
    total_duration = timedelta(0)
    count = 0

    with open(file, 'r') as file:
        for line in file:
            start_str, end_str = line.strip().split(' - ')
            start_dt = datetime.strptime(start_str.split(' ', 1)[1], "%H:%M:%S %m/%d/%Y")
            end_dt = datetime.strptime(end_str.split(' ', 1)[0:2], "%H:%M:%S %m/%d/%Y")
            total_duration += (end_dt - start_dt)
            count += 1

    average_duration = total_duration / count
    return average_duration

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file")
        sys.exit(1)

    f = sys.argv[1]
    average_timespan = avg_time(f)

    # Output the average timespan in a readable format
    print(f"Average Timespan: {average_timespan}")
