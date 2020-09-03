salary = float(input('Enter salary amount: '))
gratification = (salary * 0.05)
taxes = (salary * 0.07)
payment = (salary + gratification) - taxes
print('The amount to be paid is: R$ {:.2f}'.format(payment))
