"""
9) Leia o salário de um trabalhador e o valor da prestação
de um empréstimo. Se a prestação for maior que 20% do salário imprima:
'Empréstimo não concedido', caso contrário imprima: 'Empréstimo concedido'
"""

salary = float(input("Enter your salary: "))
loan = float(input("Enter the value of installment: "))
if loan / salary > 0.20:
    print(f"Loan not granted")
else:
    print(f"Loan granted")
