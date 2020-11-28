"""
36) Escreva um programa que, dado o valor da venda, imprima a comissão
que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

    | Venda mensal                                            | Comissão
    | Maior ou igual a R$100.000,00                           | R$700,00 + 16% das vendas
    | Menor que R$100.000,00 e maior ou igual a R$80.000,00   | R$650,00 + 14% das vendas
    | Menor que R$80.000,00 e maior ou igual a R$60.000,00    | R$600,00 + 14% das vendas
    | Menor que R$60.000,00 e maior ou igual a R$40.000,00    | R$550,00 + 14% das vendas
    | Menor que R$40.000,00 e maior ou igual a R&20.000,00    | R$500,00 + 14% das vendas
    | Menor que R$20.000,00                                   | R$400,00 + 14% das vendas

"""

sale_value = float(input('Enter the sale amount: '))

if sale_value >= 100000:
    commission = 700 + (sale_value * 0.16)
    print(f'Your commission is {commission:.2f}!')

elif (sale_value >= 80000) and (sale_value < 100000):
    commission = 650 + (sale_value * 0.14)
    print(f'Your commission is {commission:.2f}!')

elif (sale_value >= 60000) and (sale_value < 80000):
    commission = 600 + (sale_value * 0.14)
    print(f'Your commission is {commission:.2f}!')

elif (sale_value >= 40000) and (sale_value < 60000):
    commission = 550 + (sale_value * 0.14)
    print(f'Your commission is {commission:.2f}!')

elif (sale_value >= 20000) and (sale_value < 40000):
    commission = 500 + (sale_value * 0.14)
    print(f'Your commission is {commission:.2f}!')

elif (sale_value > 0) and (sale_value < 20000):
    commission = 400 + (sale_value * 0.14)
    print(f'Your commission is {commission:.2f}!')
