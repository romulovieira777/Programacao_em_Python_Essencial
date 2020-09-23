"""
41) Faça um programa que leia o valor da hora de trabalho (em reais)
e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário.
Adicionando 10% sobre o valor calculado.
"""

hour_value = float(input('Enter hours value: '))
work_hours = float(input('Enter hours worked: '))
pay = (hour_value * work_hours) + (hour_value * work_hours * (10/100))
print('The amount to be paid is: R$ {:.2f}'.format(pay))
