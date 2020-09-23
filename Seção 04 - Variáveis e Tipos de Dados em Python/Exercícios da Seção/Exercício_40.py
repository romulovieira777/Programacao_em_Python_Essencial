"""
40) Uma empresa contrata um encanador a R$30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
a quantida liquida que deverá ser paga. Sabendo-se que são descontandos 8% para imposto de renda.
"""

days = int(input('Enter days worked: '))
salary = 30.00 * days
discount = salary - (salary * 0.08)
print('The amount to be paid is: {:.2f}'.format(discount))
