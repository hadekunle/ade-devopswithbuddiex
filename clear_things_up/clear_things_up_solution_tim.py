import sys
from datetime import datetime


def time_tracker(file):
    """
    Function to track time intervals for each PID.

    Args:
    file (str): Path to the input file.

    Returns:
    dict: A dictionary containing PID as keys and time intervals as values.
    """
    time_dict = {}
    try:
        with open(file, 'r') as time_tracking_file:
            all_time = time_tracking_file.readlines()
            for time_list in all_time:
                # Remove leading/trailing whitespaces and split the line into components
                time_list = time_list.strip()
                time, date, pid, action = time_list.split()
                date_time = date + " " + time
                if action == 'start':
                    # Store start time for the PID
                    time_dict[pid] = date_time
                elif action == 'end' and pid in time_dict.keys():
                    # Calculate time difference for the end action
                    try:
                        time_diff = time_calc(date_time, time_dict[pid])
                        print(f"{pid} {time_diff}")
                    except ValueError as e:
                        print(f"Error calculating time difference: {e}")
                        continue
        return time_dict
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)


def time_calc(date_time2, date_time1):
    """
    Function to calculate time difference between two date-time strings.

    Args:
    date_time2 (str): End date-time string.
    date_time1 (str): Start date-time string.

    Returns:
    str: Time difference in the format "X days, HH:MM:SS".
    """
    try:
        date1, time1 = date_time1.split()
        date2, time2 = date_time2.split()
        date_diff = (datetime.strptime(date2, "%m/%d/%Y") - datetime.strptime(date1, "%m/%d/%Y")).days
        time_diff = datetime.strptime(time2, "%H:%M:%S") - datetime.strptime(time1, "%H:%M:%S")
        return f"{date_diff} days, {time_diff}"
    except ValueError as e:
        raise ValueError(f"Error in date-time format: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "<file>")
        sys.exit(1)
    file = sys.argv[1]
    time_tracker(file)


if __name__ == "__main__":
    main()
