import sys 

def sort_apple(file):
    apple_list = []
    with open(file, 'r') as lines:
        for line in lines:
            line_split = line.strip().split(',')
            apple_count = line_split.count('apple')
            apple_list.append((apple_count, line))
    sorted_list = sorted(apple_list, key=lambda x:x[0], reverse=True)
    
    with open('new_aji_file', 'w') as line:
        for lines in sorted_list:
            line.write(lines[1])

def main():
    file = sys.argv[1]
    sort_apple(file)

if __name__ == "__main__":
    main()