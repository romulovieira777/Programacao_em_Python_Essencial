"""
3) Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""

number = float(input('Enter a number: '))
if number >= 0:
    print(f'The square root of the number {number} is: {number ** 2}')
else:
    print(f'The number {number} squared is: {number ** 0.5}')
