"""
18) Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas(as básicas, por exemplo). O suário escolhe uma das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o
resultado e saindo.
"""

operation = input("Choose the operation: ['*'] ['/'] ['+'] ['-']: ")
number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))
if operation == '*':
    print(f'The result of mutiplication is {number_1 * number_2}')
elif operation == '/':
    print(f'The result of the division is {number_1 / number_2}')
elif operation == '+':
    print(f'The sum result is {number_1 + number_2}')
elif operation == '-':
    print(f'The sult of subtraction is {number_1 - number_2}')
else:
    print('Invalid operation!')
