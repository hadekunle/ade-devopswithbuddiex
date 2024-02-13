import sys
from datetime import datetime


# Function to calculate average access time
def avg_access_time_calc(file):
    # Dictionary to store time data for each file
    time_dict = {}
    try:
        # Open the file for reading
        with open(file, 'r') as avg_access_time_file:
            # Iterate through each line in the file
            for line in avg_access_time_file:
                # Split the line into individual components
                time, date, userid, fileid, status = line.strip().split()
                # Concatenate time and date strings
                date_time_str = f"{time} {date}"
                # Define format for parsing datetime
                format_str = "%H:%M:%S %m-%d-%Y"
                # Parse datetime string into datetime object
                datetime_obj = datetime.strptime(date_time_str, format_str)

                # Update time data in dictionary
                if fileid in time_dict:
                    prev_datetime = time_dict[fileid]['datetime']
                    if status == 'close':
                        time_diff = datetime_obj - prev_datetime
                        time_dict[fileid]['total_time'] += time_diff
                    else:
                        time_dict[fileid]['datetime'] = datetime_obj
                else:
                    # Initialize dictionary entry for new file
                    time_dict[fileid] = {'datetime': datetime_obj, 'total_time': datetime.min - datetime.min}

    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Incorrect format in the file.")
        sys.exit(1)

    # Convert dictionary data to formatted string
    return convert_dict(time_dict)


# Function to convert dictionary data to formatted string
def convert_dict(data):
    output = ''
    for key, value in data.items():
        total_seconds = value['total_time'].total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        output += f"{key} {hours:02d}:{minutes:02d}:{seconds:02d}\n"

    return output.strip()


# Main function to handle command line arguments
def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python avg_access_time_solution_tim.py <file>")
        sys.exit(1)
    # Get file path from command line argument
    file = sys.argv[1]
    # Calculate and display average access time
    print(avg_access_time_calc(file))


# Entry point of the program
if __name__ == "__main__":
    main()
