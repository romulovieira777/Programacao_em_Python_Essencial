"""
42) Receba o salário-base de um funcionário. Calcule e imprima o salário
a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""

salary = float(input('Enter salary amount: '))
gratification = (salary * 0.05)
taxes = (salary * 0.07)
payment = (salary + gratification) - taxes
print('The amount to be paid is: R$ {:.2f}'.format(payment))
