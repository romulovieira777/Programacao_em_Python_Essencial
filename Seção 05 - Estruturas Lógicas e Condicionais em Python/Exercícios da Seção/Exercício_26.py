"""
26) Leia a distância em km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela abaixo:
    CONSUMO     |  (Km/l)  |   MENSAGEM
    menor que   |     8    |  Venda o carro!
    entre       |  8 e 12  |  Econômico!
    maior que   |    12    |  Super econômico!
"""

distance = float(input('Enter the distance of the  route in KM: '))
liters = float(input('Enter the amount of liters of gasoline consumed on the route: '))

consumption = (distance / liters)

if consumption <= 8:
    print(f'Sell the car!')
elif (consumption > 8) and (consumption <= 12):
    print('Economic!')
else:
    print('Super economic!')
