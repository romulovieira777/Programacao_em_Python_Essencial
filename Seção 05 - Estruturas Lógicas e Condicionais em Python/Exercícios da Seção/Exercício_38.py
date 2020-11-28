"""
38) Leia uma data de nascimento de uma pessoa fornecida através de três números
inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma
data válida. Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês
(29 se o ano for bissexto), dia <= 30 em abril, junho, setembro e novembro,
dia <= 31 nos outros meses. Teste a validade do mês: mês > 0 e mês <13. Teste a
validade do ano: ano <= ano atual (use uma constante definida com o valor igual a 2008).
Imprimir: "data válida" ou "data inválida" no final da execução.

"""

year = int(input('Enter the year of your birth: '))
month = int(input('Enter the month of your birth: '))
day = int(input('Enter the day of your birth: '))

current_year = 2008

if year <= current_year:
    if month == 1:

        if (day >= 1) and (day <= 31):
            print('Valid Date!')

        else:
            print('Invalid Date!')

    elif month == 2:
        if (year % 400 == 0) and ((year % 4 == 0) and not (year % 100 == 0)):
            if (day >= 1) and (day <= 29):
                print('Valid Date!')
            else:
                print('Invalid Date!')
        else:
            if (day >= 1) and (day <= 28):
                print('Valid Date!')
            else:
                print('invalid Date!')

    elif month == 3:
        if (day >= 1) and (day <= 31):
            print('Valid Date!')
        else:
            print('Invalid Date!')

    elif month == 4:
        if (day >= 1) and (day <= 30):
            print('Valid Date!')
        else:
            print('Invalid Date"')

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
        print('Invalid Date!')

else:
    print('Invalid Date!')
