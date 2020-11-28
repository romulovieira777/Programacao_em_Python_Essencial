"""
2) Leia um número fornecido pelo usuário. Se esse númerro for positivo,
calcule a raiz quadrada do número. Se o número for negativo, mostre
uma mensagem dizendo que o número é inválido.
"""

number = int(input('Enter a number: '))
if number >= 0:
    print(f'The square root of the number {number} is: {number ** 2}')
else:
    print(f'Invalid number!')
