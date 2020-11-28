"""
19) Faça um programa para verificar se um determinado número
inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""

number = int(input('Enter a number: '))
if (number % 3 == 0) and not (number % 5 == 0):
    print('Divisible by three!')
elif(number % 5 == 0) and not (number % 3 == 0):
    print('Divisible by five!')
else:
    print('Number is not divisible by three or five!')
