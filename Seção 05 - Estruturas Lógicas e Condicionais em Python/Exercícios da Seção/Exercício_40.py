"""
40) O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados
sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e
escreva o custo ao consumidor

    |      CUSTO DE FÁBRICA          | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
    | até R$12.000,00                |         5         |    isento      |
    | entre R$12.000,00 e 25.000,00  |        10         |      15        |
    | acima de R$25.000,00           |        15         |      20        |

"""

factory_cost = float(input('Enter the factory cost of the car: '))

if (factory_cost >= 0) and (factory_cost <= 12000):
    consumer_cost = factory_cost + (factory_cost * 0.05)
    print(f'Car value for the consumer is {consumer_cost:.2f}!')

elif (factory_cost > 12000) and (factory_cost <= 25000):
    consumer_cost = factory_cost + (factory_cost * 0.10) + (factory_cost * 0.15)
    print(f'Car value for the consumer is {consumer_cost:.2f}!')

elif factory_cost > 25000:
    consumer_cost = factory_cost + (factory_cost * 0.15) + (factory_cost * 0.20)
    print(f'Car value for the consumer is {consumer_cost:.2f}!')
