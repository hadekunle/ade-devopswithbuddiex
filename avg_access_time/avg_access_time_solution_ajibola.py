from datetime import datetime, timedelta
import sys

def avg_time(file):
    """A function that acepts a log file of access times and computes the average access time."""
    access_map = {}
    intervals_map = {}
    with open (file, 'r') as access_intervals:
        for line in access_intervals:
            line = line.strip()
            time , date, _, fileid, call = line.split()
            if call.lower() == "open" and fileid not in access_map:
                open_time = f"{time} {date}"
                open_time = datetime.strptime(open_time, "%H:%M:%S %m-%d-%Y")
                access_map[fileid] = open_time
                intervals_map[fileid] = [timedelta(), 0]
            elif call.lower() == "open" and fileid in access_map:
                open_time = f"{time} {date}"
                open_time = datetime.strptime(open_time, "%H:%M:%S %m-%d-%Y")
                access_map[fileid] = open_time
            elif call.lower() == "close" and fileid in access_map:
                close_time = f"{time} {date}"
                close_time = datetime.strptime(close_time, "%H:%M:%S %m-%d-%Y")
                intervals_map[fileid][0] += close_time - access_map[fileid]
                intervals_map[fileid][1] += 1
        return intervals_map


def main():
    """Main function"""
    file = sys.argv[1]
    if len(sys.argv) != 2:
        sys.exit("To calculate average access time, please provide one valid log file")
    output = avg_time(file)
    for key, values in output.items():
        print(key, values[0]/values[1])

if __name__ == "__main__":
    main()