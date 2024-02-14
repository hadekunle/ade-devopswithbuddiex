from datetime import datetime, timedelta
import sys

def avg_time(file):
    """A function that aceepts a file of time intervals and calculates the average."""
    intervals = timedelta()
    no_of_intervals = 0
    with open (file, 'r') as time_intervals:
        for line in time_intervals:
            line = line.strip()
            _, start_time , start_date, _, end_time, end_date = line.split()
            start_interval = f"{start_time} {start_date}"
            end_interval = f"{end_time} {end_date}"
            start_interval = datetime.strptime(start_interval, "%H:%M:%S %m/%d/%Y")
            end_interval = datetime.strptime(end_interval, "%H:%M:%S %m/%d/%Y")
            difference = (end_interval - start_interval)
            intervals += difference
            no_of_intervals += 1
        average = intervals/no_of_intervals
        # average = round(average.total_seconds())
        # print(timedelta(seconds=average))
        return average


def main():
    """Main function"""
    file = sys.argv[1]
    if len(sys.argv) != 2:
        sys.exit("To calculate avg time, please provide one valid file")
    print(avg_time(file))

if __name__ == "__main__":
    main()