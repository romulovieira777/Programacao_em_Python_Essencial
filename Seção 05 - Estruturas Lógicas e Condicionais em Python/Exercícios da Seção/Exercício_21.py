"""
21) Escreva o menu de opções abaixo. Leia a opção do usuário e
execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
    Escolha a opção:
    1 - Soma de 2 números.
    2 - Diferença entre 2 número (maior pelo menor).
    3 - Produto entre 2 números.
    4 - Divisão entre 2 números (o denominador não pode ser zero).
    Opção
"""

print('1 - Sum of two numbers\n'
      '2 - Difference between two numbers (heighest to lowest\n'
      '3 - Produtc between two numbers\n'
      '4 - Division between two numbers (the denominator cannot be zero\n')
option = int(input('Choose an option: \n'))
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
if option == 1:
    print(f'The sum of two numbers is {number_1 + number_2}')
elif option == 2:
    print(f'The difference between the two numbers is {number_1 - number_2}')
elif option == 3:
    print(f'The product of the two numbers is {number_1 * number_2}')
elif option == 4:
    if number_1 != 0:
        print(f'The division of the two number is {number_1 / number_2}')
    else:
        print('The denominator cannot be zero!')
else:
    print('Invalid option!')
