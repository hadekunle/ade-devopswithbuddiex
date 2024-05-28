import sys

def error_handling(file):
    with open(file, 'r') as lines:
        for line in lines:
            numerator, *denominator = line.strip().split()
            try:
                int(numerator)
            except ValueError:
                print("Error: line contains non digits")
                continue
            
            if not denominator:
                print("Error: Too few numbers given")
                continue
                 
            else:
                try:
                    int(denominator[0])
                except ValueError:
                    print("Error: line contains non digits")
                    continue
            
            if int(denominator[0]) <= 0:
                print(f"Error: division by {denominator[0]}")
                continue


            try:
                output = int(numerator) / int(denominator[0])
                print(output)

            except:
                print("Other uncaught error")
            
                 
            
def main():
    input_file = sys.argv[1]
    error_handling(input_file)


if __name__ == "__main__":
    main()