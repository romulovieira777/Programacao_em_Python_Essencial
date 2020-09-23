"""
28) Faça a leitura de três valores e apresente como resultado a
soma dos quadrados dos três valores lidos.
"""

number_1 = int(input('Enter the value: '))
number_2 = int(input('Enter the value: '))
number_3 = int(input('Enter the value: '))
high = pow(number_1, 2) + pow(number_2, 2) + pow(number_3, 2)
print(f'The value of the numbers in the table is: {high}!')
