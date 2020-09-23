"""
7) Leia uma temperatura em graus Fahrenheit e apresente-a convertida
em graus Celsius. A fórmula de conversão é: C = (F-32.0)*5.0/9.0,
sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
celsius = round((fahrenheit - 32) * 5 / 9, 2)
print(f'The temperature in Celsius is: {celsius}')
