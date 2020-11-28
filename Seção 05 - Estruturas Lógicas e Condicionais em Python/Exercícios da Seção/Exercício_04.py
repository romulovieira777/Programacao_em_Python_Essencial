"""
4) Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada ao número digitado
"""

number = int(input('Enter a number: '))
if number >= 0:
    print(f'The number {number} squared is: {number ** 0.5:.2f}')
    print(f'The square root of the number {number} is: {number ** 2}')
else:
    print(f'Negative number, please enter a positive number!')
