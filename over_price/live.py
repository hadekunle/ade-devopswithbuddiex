import sys 

def overprice(input_file):
    product_map = {}
    with open(input_file, 'r') as fp:
        for line in fp:
            product, _ , price = line.strip().split()
            price = float(price[1:])
            if product not in product_map:
                product_map[product] = [0, 1]
                if price > 4:
                    product_map[product] = [1, 1]
            else:
                product_map[product][1] += 1
                if price > 4:
                    product_map[product][0] += 1
    
    for product, value in product_map.items():
        percentage = value[0] / value[1] * 100
        print(f"{product}: {percentage:.2f}%")
    return product_map
    

def main():
    input_file = sys.argv[1]
    overprice(input_file)
        
if __name__ == "__main__":
    main()