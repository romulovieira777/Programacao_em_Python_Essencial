"""
18) Leia um valor de um volume em metros cúbicos m³ e apresente-o
convertido em litros. A fórmula de conversão é: L = 1000 * M,
sendo L o volume em litros e M o volume em metros cúbicos
"""

meters = float(input('Enter the value in cubic meters: '))
liters = round(1000 * meters, 2)
print(f'The meter value {meters} for liters is: {liters}')
