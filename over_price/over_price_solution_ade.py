import os

os.system('clear')

def over_price(input_file):
    product_map = {}   
    '''
    This is the idea behind product_map
    {key: value}
    {product: [count_over_4 , count_total]} 
    '''
    with open (input_file,'r') as file:
        for line in file:
            product, _, price = line.strip().split()
            price = float(price[1:])

            if product not in product_map:
                product_map[product] = [0, 0]

            product_map[product][1] += 1
            
            if price > 4:
                product_map[product][0] += 1
    
    for product, value in product_map.items():
        percentage = (value[0] / value[1]) * 100
        print(f"{product}: {percentage:.2f}%")
    return product_map
    

def main():
    input_file = sys.argv[1]
    # over_price('./over_price/file')
    over_price(input_file)
        
if __name__ == "__main__":
    main()
