"""
6) Leia uma temperatura em gruas Celsius e apresente-a convertida
em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

celsius = float(input('Enter the temperature in Celsius: '))
fahrenheit = round(celsius * (9/5) + 32, 2)
print(f'The temperature in Fahrenheit is: {fahrenheit}')
