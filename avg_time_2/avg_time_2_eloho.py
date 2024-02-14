from datetime import datetime, timedelta
import sys



def calculate_interval_duration(line):
    try:
        interval, start_time, start_date, _, end_time, end_date = line.split()
        start_timestamp = datetime.strptime(f"{start_date} {start_time}", "%m/%d/%Y %H:%M:%S")
        end_timestamp = datetime.strptime(f"{end_date} {end_time}", "%m/%d/%Y %H:%M:%S")

        duration = end_timestamp - start_timestamp
        return duration
    except ValueError:
        return None
   



def avg_interval(file):
    if len(sys.argv) != 2:
        print("Usage: python avg_access_time_eloho.py <log>")
        sys.exit(1)

    file = sys.argv[1]
    total_duration = timedelta()
    count = 0

    with open(file, 'r') as file:
        for line in file:
            if line.strip():
                if line.startswith('Interval'):
                    duration = calculate_interval_duration(line)
                    if duration is not None:
                        total_duration += duration
                        count += 1

    if count > 0:
        average_interval = total_duration / count
        print (type(average_interval))
        return average_interval
    else:
        return timedelta()

if __name__ == "__main__":
    print(avg_interval(sys.argv[1]))