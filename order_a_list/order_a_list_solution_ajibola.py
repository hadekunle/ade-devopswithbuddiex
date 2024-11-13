def main():
    input_list = ['a1', 'b2', 'c1', 'd5', 'a3', 'b1', 'd1', 'b3'] 
    output_list = sorted(input_list, key=lambda x: (x[0], x[1]))
    print(output_list)

main()