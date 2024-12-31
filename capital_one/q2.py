import os
from collections import defaultdict

from q2info import logs

os.system('clear')

logs = [
  ["supply", "item1", "2", "100"],
  ["supply", "item2", "3", "60"],
  ["sell", "item1", "1"],
  ["sell", "item1", "1"],
  ["sell", "item2", "2"],
  ["return", "item2", "1", "60", "40"],
  ["sell", "item2", "1"],
  ["sell", "item2", "1"]
]

def solution(logs):
    logging = {}
    sells = []
    for log in logs:
        if log[0]=='supply':
            type_, item, count, price = log
            count, price = int(count), int(price)
            logging[item]= { type_ : [count,price]}
        elif log[0]=='sell':
            type_, item, count = log
            count = int(count)
            # using returned price
            try:
                quantity = logging[item]['return'][0]
                return_price  = logging[item]['return'][1]

                if quantity - count >= 0 :
                    print('There is return available use discount price')
                    logging[item]['return'][0] = quantity - count
                    sells.append(return_price * count)
                    continue
            except:
                print('No return available use regular price')
            # using regular price
            quantity = logging[item]['supply'][0]
            sales_price  = logging[item]['supply'][1]
            if quantity - count >= 0 :
                sells.append(sales_price * count)
                logging[item]['supply'][0] = quantity - count 
            else:
                print('Not enough inventory')

        elif log[0]=='return':
            type_, item, count, sell_price, new_price = log
            item, count, price = item, int(count), int(new_price)
            logging[item][type_]= [count,price]
    return f'output: {sells}'

print(solution(logs))