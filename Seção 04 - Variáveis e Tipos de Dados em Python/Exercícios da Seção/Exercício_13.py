"""
13) Leia uma distância em quilômetros e apresente-a
convertida em milhas. A fórmula de conversão é: M = K / 1.61,
sendo K a distância em quilômetros e M em milhas.
"""

km = float(input('Enter the speed in km: '))
miles = round(km / 1.61, 2)
print(f'The speed in km {km} to miles is: {miles}')
