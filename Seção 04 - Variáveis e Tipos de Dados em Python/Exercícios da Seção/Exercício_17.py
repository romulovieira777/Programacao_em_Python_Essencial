"""
17) Leia um valor de comprimento em centímetros e apresente-o convertida
em centímetros. A fórmula de conversão é: P = C/2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""

centimeters = float(input('Enter the in centimeters: '))
inches = round(centimeters / 2.54, 2)
print(f'The centimeters {centimeters} for inches is: {inches}')
