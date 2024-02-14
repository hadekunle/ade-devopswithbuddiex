
import sys
from datetime import datetime

def average_time(file):
    access_times = {}  # Store total access time and count for each file

    with open(file, 'r') as file:
        for line in file:
            time_str, date_str, _, fileid, action = line.strip().split()
            datetime_str = f"{date_str} {time_str}"
            print(datetime_str)
            datetime_obj = datetime.strptime(datetime_str, "%d-%m-%Y %H:%M:%S")
            print(datetime_obj)

            if action == "open":
                if fileid not in access_times:
                    access_times[fileid] = {'open': datetime_obj, 'total_time': 0, 'count': 0}
                else:
                    access_times[fileid]['open'] = datetime_obj
            elif action == "close" and fileid in access_times and 'open' in access_times[fileid]:
                open_time = access_times[fileid]['open']
                access_duration = datetime_obj - open_time
                access_times[fileid]['total_time'] += access_duration.total_seconds()
                access_times[fileid]['count'] += 1
                del access_times[fileid]['open']

    # Calculating average access time
    average_access_times = {}
    for fileid, data in access_times.items():
        if data['count'] > 0:
            average_seconds = data['total_time'] / data['count']
            average_access_times[fileid] = average_seconds

    # Sorting by average access time
    sorted_average_times = sorted(average_access_times.items(), key=lambda x: x[1])

    # Formatting output
    formatted_output = []
    for fileid, seconds in sorted_average_times:
        average_time = str(datetime.utcfromtimestamp(seconds).time())
        formatted_output.append((fileid, average_time))

    return formatted_output


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py log_file")
        sys.exit(1)
    
    file = sys.argv[1]
    average_access_times = average_time(file)
    for entry in average_access_times:
        print(entry)
