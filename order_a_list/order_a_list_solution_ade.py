to_order_list = ['a1', 'b2', 'c1', 'd5', 'a3', 'b1', 'd1', 'b3']
expected_output = ['a1', 'a3', 'b1', 'b2', 'b3', 'c1', 'd1', 'd5']

def order_list(sort_list :list):
    return sorted(sort_list)
        
print(order_list(to_order_list) == expected_output)