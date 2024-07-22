# Function to filter and sort words
import sys


def filter_and_sort_words(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    
    # Remove newline characters and filter words
    filtered_words = [word.strip() for word in words if word.lower().startswith('he') and 'er' in word[2:].lower()]
    
    # Sort words alphabetically
    filtered_words.sort()
    
    # Print the filtered and sorted words
    for word in filtered_words:
        print(word)







def main():

    if len(sys.argv) != 2:
        print("Usage: Python traffic <file>")
        sys.exit(1)

    file = sys.argv[1]

    filter_and_sort_words(file)


# Entry point of the program
if __name__ == "__main__":
    main()
