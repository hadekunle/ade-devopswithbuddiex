import sys 
from datetime import datetime

def reasonable_cost(file):
    recommended_list = []

    with open(file, 'r') as lines:
        lines.readline()
        for line in lines:
            line = line.strip()
            day, _ , cost, recommendation = line.split()
            day = datetime.strptime(day, "%m/%d/%y")
            cost = float(cost[1:])
            if recommendation.lower() == 'yes' and cost >= 20 and cost <= 50:
                recommended_list.append((day, line))
    
    recommended_list = sorted(recommended_list, key=lambda item: item[0], reverse=True)
    for items in recommended_list:
        print (items[1])
    

def main():
    file = sys.argv[1]
    reasonable_cost(file)

if __name__ == "__main__":
    main()


