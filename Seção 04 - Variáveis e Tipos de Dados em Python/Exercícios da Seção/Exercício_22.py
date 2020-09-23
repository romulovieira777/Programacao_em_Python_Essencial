"""
22) Leia um valor de comprimeto em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimeto emm jardas
e M o comprimeto em metros.
"""

yards = float(input('Etner the value in yards: '))
meters = round(0.91 * yards, 2)
print(f'The value in yards {yards} for meters is: {meters}')
