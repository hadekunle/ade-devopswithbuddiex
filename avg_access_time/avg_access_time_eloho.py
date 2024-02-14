from datetime import datetime, timedelta
from collections import defaultdict
import sys

def process_file(file):
    file_access_times = defaultdict(list)
    
    file = sys.argv[1]

    with open(file) as f:
        for line in f:
            time_str, date_str, user_id, file_id, call= line.split()
            timestamp = datetime.strptime(f"{date_str} {time_str}", "%m-%d-%Y %H:%M:%S")

            if call == 'open':
                file_access_times[file_id].append(timestamp)
            elif call == 'close' and file_id in file_access_times:
                open_time = file_access_times[file_id][-1]
                close_time = timestamp
                access_time = close_time - open_time
                file_access_times[file_id].append({'close_time': timestamp, 'access_time': access_time})

    return file_access_times


def average_time(file_access_times):
    result = []

    for file_id, access_times in file_access_times.items():
        total_time = timedelta()

        for i in range(0, len(access_times), 2):
            if i + 1 < len(access_times):
                total_time += access_times[i + 1 ]['access_time']

        if len(access_times) // 2 > 0:
            average_time = total_time / (len(access_times) // 2)
        else:
            average_time = timedelta()
        result.append((file_id, average_time))
    sorted_access_times = sorted(result, key=lambda x: x[1])
    return sorted_access_times



def output_result(average_times):
    for file_id, average_time in average_times:
        print(f"{file_id}: {average_time}")


if __name__ == "__main__":
    output_result(average_time(process_file(sys.argv[1])))