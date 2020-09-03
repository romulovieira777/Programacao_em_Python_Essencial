hour_value = float(input('Enter hours value: '))
work_hours = float(input('Enter hours worked: '))
pay = (hour_value * work_hours) + (hour_value * work_hours * (10/100))
print('The amount to be paid is: R$ {:.2f}'.format(pay))
