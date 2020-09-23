"""
37) Faça um programa que leia o valor de um produto e imprima
o valor com desconto, tendo em vista que o desconto foi de 12%.
"""

product = float(input('Enter product value: '))
discount = product - round(product * (12/100), 2)
print(f'The value of the discounted product is: {discount}')
