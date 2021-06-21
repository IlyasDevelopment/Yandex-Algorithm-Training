customers = {}
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        customer, product, k = line.split()
        k = int(k)
        if customer not in customers:
            customers[customer] = {}
            customers[customer][product] = k
        elif product not in customers[customer]:
            customers[customer][product] = k
        else:
            customers[customer][product] += k

for key, value in sorted(customers.items()):
    print(f'{key}:')
    for product_key, product_value in sorted(value.items()):
        print(product_key, product_value)
