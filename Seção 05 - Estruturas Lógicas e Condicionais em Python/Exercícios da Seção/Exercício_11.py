"""
11) Escreva um programa que leia um número inteiro maior do que zero
e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número
251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não dor maior do que
zero, programa terminará com a mensagem 'Número inválido'
"""

number = int(input("Enter a number greater than zero: "))
if number > 0:
    number = str(number)
    soma = 0
    for num in range(len(number)):
        soma += int(number[num])
    print(f'The sum of its algorithms is {soma}')
else:
    print(f"Invalid number!")
