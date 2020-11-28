"""
31) Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostre qual a classificação
dessa pessoa.
    |    Altura    |                       Peso                       |
    |              |Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90  |
    |Menor que 1,20|   A   |             D             |      G       |
    |De 1,20 a 1,70|   B   |             E             |      H       |
    |Maior que 1,70|   C   |             F             |      I       |
"""

height = float(input("Enter your height: "))
weight = int(input("Enter yor weight: "))

if height < 1.20 and weight <= 60:
    print('Classification: A')
elif (height >= 1.20) and (height <= 1.70) and (weight <= 60):
    print('Claasification B')
elif (height > 1.70) and (weight <= 60):
    print('Classification C')
elif (height < 1.20) and (weight >= 60) and (weight <= 90):
    print('Classification D')
elif (height >= 1.20) and (height <= 170) and (weight >= 60) and (weight <= 90):
    print('Classification E')
