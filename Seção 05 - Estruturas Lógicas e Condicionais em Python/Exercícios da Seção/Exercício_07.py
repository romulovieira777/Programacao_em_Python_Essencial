"""
7) Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima a mensagem
'Números iguais'.
"""

number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
if number_1 > number_2:
    print(f'The first number {number_1} greater then the second number {number_2}')
elif number_2 > number_1:
    print(f'The second number {number_2} greater then the first number {number_1}')
else:
    print(f'The numbers have the same value!')
