"""
27) Leia um  valor de área em hectares e apresente-o convertido em
metros quadrados m². A fórmula de conversão é: M = H * 10000,
sendo M a área em metros quadrados e H a área em hectares.
"""

acre = float(input('Enter the value in acre: '))
square_meters = round(acre * 10000, 2)
print(f'The value of {acre} acre for square meters is {square_meters}!')
