"""
21) Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

pounds = float(input('Enter the amount in pounds: '))
kilograms = round(pounds * 0.45, 2)
print(f'The value of pounds {pounds} for kilograms is: {kilograms}')
