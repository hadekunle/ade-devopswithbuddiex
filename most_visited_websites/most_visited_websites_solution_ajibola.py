import sys

def most_visited(file):
    website_count = {}
    output_list = []
    with open(file, 'r') as fp:
        for line in fp:
            line = line.strip().split()
            for website in line[1:]:
                if website not in website_count:
                    website_count[website] = 0
                else:
                    website_count[website] += 1
        website_count = dict(sorted(website_count.items(), key=lambda item: item[1], reverse=True))
    previous_count = 0
    for website, count in website_count.items():
        if len(output_list) < 5:
                output_list.append(website)
                previous_count = count
        elif len(output_list) >= 5 and previous_count == count:
            output_list.append(website)
    
    print(output_list)
    return output_list

            



def main():
    file = sys.argv[1]
    most_visited(file)

if __name__== "__main__":
    main()