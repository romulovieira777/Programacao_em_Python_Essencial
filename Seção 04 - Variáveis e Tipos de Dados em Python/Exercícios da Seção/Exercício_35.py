"""
35) Sejam a e b os catetos de um triângulo, onde a hipotenusa
é obtida pela equação: hipotenusa = √a² + b². Faça um
programa que receba os valores de a e b e calcule o valor
da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

number1 = float(input('Enter the first value of the side: '))
number2 = float(input('Enter the second value of the side: '))
soma = round((number1 ** 2 + number1 ** 2) ** 0.5, 6)
print(f'The leg a {number1} and the leg b {number2} generate the hypotenuse: {soma}!')
