product = float(input('Enter product value: '))
discount = product - round(product * (12/100), 2)
print(f'The value of the discounted product is: {discount}')
