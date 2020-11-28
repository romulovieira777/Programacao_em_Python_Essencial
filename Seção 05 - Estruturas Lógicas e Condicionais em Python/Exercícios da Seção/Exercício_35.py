"""
35) Leia uma data e determine se ela é válida. Ou seja, verifique se o
mês está entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem
29 dias em anos bissextos, e 28 dias em anos não bissextos.

"""

day = int(input('Enter the day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))

if year != 0:
    if month == 1:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 2:
        if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
            if (day >= 1) and (day <= 29):
                print('Valid Date!')
            else:
                print('Invalid Date!')
        else:
            if (day >= 1) and (day <= 28):
                print('Valid Date!')
            else:
                print('Invalid Date!')

    elif month == 3:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 4:
        if (day >= 1) and (day <= 30):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 5:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 6:
        if (day >= 1) and (day <= 30):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 7:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 8:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 9:
        if (day >= 1) and (day <= 30):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 10:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 11:
        if (day >= 1) and (day <= 30):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 12:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

else:
    print('The year cannot be zero!')
