import sys


def division(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            parts = line.split()
            if len(parts) != 2:
                print("Error: Too few numbers given")
                continue

            try:
                num1 = float(parts[0])
                num2 = float(parts[1])
                result = num1 / num2
                print(result)
            except ValueError:
                print("Error: line contains non digits")
            except ZeroDivisionError:
                print("Error: division by 0")
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    file = sys.argv[1]
    division(file)

if __name__ == "__main__":
    main()