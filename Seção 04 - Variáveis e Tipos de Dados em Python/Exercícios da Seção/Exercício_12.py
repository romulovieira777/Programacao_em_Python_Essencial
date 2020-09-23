"""
12) Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros
e M em milhas.
"""

miles = float(input('Enter the speed in miles: '))
km = round(1.61 * miles, 2)
print(f'The spped in miles {miles} to km is: {km}')
