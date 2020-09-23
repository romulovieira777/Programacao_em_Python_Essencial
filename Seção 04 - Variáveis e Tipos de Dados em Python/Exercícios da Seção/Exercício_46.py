"""
46) Faça um programa que leia um número inteiro positivo de
três digitos (de 100 a 999). Gere outro número formado pelos
dígitos invertidos do número lido. Exemplo:
    NúmeroLido = 123
    NúmeroGerado = 321
"""

number = int(input('Enter the number: '))
reverse = str(number)[::-1]
print('The number entered {} inverted is {}'.format(number, reverse))
