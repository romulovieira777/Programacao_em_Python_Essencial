"""
20) Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K/0.45, snedo K a massa em quilogramas
e L a massa em libras.
"""

kilograms = float(input('Enter the value in kilograms: '))
pounds = round(kilograms / 0.45, 2)
print(f'The value of kilograms {kilograms} for pounds is: {pounds}')
