import sys
from datetime import datetime


def read_file(filename):
    """Reads the content of the file and returns a list of lines."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)


def update_file(lines, filename):
    """
    Updates the file by removing completed binaries and sorting queued binaries.
    Sorts by status first (queued or running), then by time.
    """
    try:
        # Filter binaries
        updated_lines = []
        for line in lines:
            if 'running' in line or 'queued' in line:
                updated_lines.append(line)
        # Sort lines by status first and then by time
        updated_lines.sort(key=lambda x: (x.split()[3], datetime.strptime(x.split()[1], "%H:%M:%S")))

        # Write the updated content back to the file
        with open(filename, 'w') as file:
            for line in updated_lines:
                file.write(line)
    except IOError:
        print("Error: Unable to write to the file.")
        sys.exit(1)
    except ValueError:
        print("Error: Incorrect time format in the file.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file>")
        sys.exit(1)
    filename = sys.argv[1]
    lines = read_file(filename)
    update_file(lines, filename)


if __name__ == "__main__":
    main()
