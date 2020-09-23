"""
23) Leia um valro de comprimento em metros e apresente-o convertido em jardas.
a fórmula de conversão é: J = M/0.91, snedo J o comprimento em jardas e
M o comprimento em metros.
"""

meters = float(input('Enter the value in meters: '))
yards = round(meters / 0.91, 2)
print(f'The value in meters {meters} for yards is: {yards}')
