"""
41) Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua
classificação de acordo com a tabela abaixo:

    |     IMC      | Classificação
    | < 18,5       | Abaixo do Peso
    | 18,6 - 24,9  | Saudável
    | 25,0 - 29,9  | Peso em excesso
    | 30,0 - 34,9  | Obesidade Grau I
    | 35,0 - 39,9  | Obesidade Grau II(severa)
    | >= 40        | Obesidade Grau III(mórbida)

"""

height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in Kg: '))

imc = weight / (height * height)

if (imc >= 0) and (imc <= 18.5):
    print('Under Weight!')

elif (imc > 18.5) and (imc <= 24.9):
    print('Healthy!')

elif (imc > 24.9) and (imc <= 29.9):
    print('Excess Weight!')

elif (imc > 29.9) and (imc <= 34.9):
    print('Obesity Degree I')

elif (imc > 34.9) and (imc <= 39.9):
    print('Obesity Degree II - Severe!')

elif imc > 39.9:
    print('Obesity Degree III - Morbid!')
