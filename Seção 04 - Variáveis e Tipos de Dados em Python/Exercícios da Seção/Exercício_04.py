"""
4) Leia um número real e imprima o resultado do quadrado desse número.
"""

number = int(input('Enter the number: '))
square = round(pow(number, 2), 2)
print(f'{number} squared is {square}')
