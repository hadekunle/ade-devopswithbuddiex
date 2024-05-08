import sys 

def top_three_words(file):
    top_words = {}
    output_list = []
    with open(file, 'r') as words:
        for line in words:
            line = line.strip().split()
            for word in line:
                if word not in top_words:
                    top_words[word] = 1 
                else:
                    top_words[word] += 1
    top_words = dict(sorted(top_words.items(), key=lambda item: item[1], reverse=True))
    previous_count = 0
    for word, count in top_words.items():
        if len(output_list) < 3:
                output_list.append((word, count))
                previous_count = count
        elif len(output_list) >= 3 and previous_count == count:
            output_list.append((word, count))
    print(output_list)
    return 


def main():
    file = sys.argv[1]
    top_three_words(file)


if __name__=="__main__":
    main()