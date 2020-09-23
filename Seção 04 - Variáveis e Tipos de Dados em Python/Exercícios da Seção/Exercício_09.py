"""
9) Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Kelvin. A fórmula de conversão é: K = C + 273.15,
sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

celsius = float(input('Enter the temperature in celsius: '))
kelvin = round(celsius + 273.15, 2)
print(f'The temperatre in Celsius is: {kelvin}')
