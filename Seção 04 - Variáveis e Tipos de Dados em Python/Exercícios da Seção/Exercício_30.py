"""
30) Leia um valor em real e a cotação do dólar. Em sequida,
imprima o valor correspondente em dólares
"""

real = float(input('Enter the amount in real: '))
dolar = round(real * 5.57, 2)  # Cotação em 27/08/2020
print(f'The amount in reais {real} for dollar is: {dolar}')
