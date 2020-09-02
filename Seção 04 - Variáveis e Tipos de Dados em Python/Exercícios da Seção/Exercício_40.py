days = int(input('Enter days worked: '))
salary = 30.00 * days
discount = salary - (salary * 0.08)
print('The amount to be paid is: {:.2f}'.format(discount))
