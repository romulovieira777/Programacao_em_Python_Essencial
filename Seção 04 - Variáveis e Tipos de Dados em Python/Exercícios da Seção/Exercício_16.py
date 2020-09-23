"""
16) Leia um valor de comprimento em polegadas e apresente-o convertido
em centímetros. A fórmula de conversão é: P = C / 2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""

inches = float(input('Enter the in Inches: '))
centimeters = round(inches * 2.54, 2)
print(f'The inches {inches} for centimeters is: {centimeters}')
