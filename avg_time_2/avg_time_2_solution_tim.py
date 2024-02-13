import sys
from datetime import datetime, timedelta

def avg_time_calc(file):
    timespan = []
    try:
        with open(file, 'r') as avg_time_file:
            all_datetime = avg_time_file.readlines()
            for datetime_unit in all_datetime:
                datetime_unit = datetime_unit.strip('\n')
                interval, time1, date1, dash, time2, date2 = datetime_unit.split()
                date_time_1 = date1 + " " + time1
                date_time_2 = date2 + " " + time2
                format_str = "%m/%d/%Y %H:%M:%S"
                datetime_obj_1 = datetime.strptime(date_time_1, format_str)
                datetime_obj_2 = datetime.strptime(date_time_2, format_str)
                time_diff = datetime_obj_2 - datetime_obj_1
                timespan.append(time_diff)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Incorrect format in the file.")
        sys.exit(1)
    if not timespan:
        print("No time spans found in the file.")
        sys.exit(1)
    formatted_timespans = [format_timedelta(timedelta) for timedelta in timespan]
    average_timespan = format_timedelta(average_timedelta(timespan))
    return formatted_timespans, average_timespan

def format_timedelta(td):
    total_seconds = td.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def average_timedelta(timedeltas):
    if not timedeltas:
        return timedelta()
    total_timedelta = sum(timedeltas, timedelta())
    average_timedelta = total_timedelta / len(timedeltas)
    return average_timedelta

def main():
    if len(sys.argv) != 2:
        print("Usage: python avg_time_2_solution_tim.py <file>")
        sys.exit(1)
    file = sys.argv[1]
    formatted_timespans, average_timespan = avg_time_calc(file)
    print("All Timespans:", formatted_timespans)
    print("Average Timespan:", average_timespan)

if __name__ == "__main__":
    main()
