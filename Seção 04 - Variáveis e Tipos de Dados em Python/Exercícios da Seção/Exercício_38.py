"""
38) Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%.
"""

salary = float(input('Enter salary: '))
increase = salary + (salary * (25/100))
print('The salary with a 25% increase is: {:.2f}'.format(increase))
