"""
19) Leia um valor de um volume em litros e apresente-o
convertido em metros cúbicos m³. A fórmula de conversão é: M = L/1000,
sendo o L o volume em litros e M o volume em metros cúbicos.
"""

liters = float(input('Enter the value in liters: '))
meters = round(liters / 1000, 2)
print(f'The value of the liters {liters} for cubic meters is: {meters}')
