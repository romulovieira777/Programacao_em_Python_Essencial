"""
12) Leu um número inteiro. Se o número lido for negativo, escreva a mensagem
'Número inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""

from math import log10

number = int(input("Enter a number: "))
if number < 0:
    print('Invalid number!')
else:
    print(f'The logarithm of this number is: {log10(number)}')
