"""
32) Leia um número inteiro e imprima a soma do sucessor
de seu triplo com o antecessor e seu dobro.
"""

number = int(input('Enter the whole number: '))
soma = ((number + 1) * 3) + (number - 1) * 2
print(soma)
