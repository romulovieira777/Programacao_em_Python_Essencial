"""
16) Usando switch, escreva um programa que leia um inteiro entre 1 e 12
e imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2,
e assim por diante.
"""

month = int(input('Enter the number between 1 and 12: '))
if (month > 0) and (month < 13):
    if month == 1:
        print('January')
    elif month == 2:
        print('February')
    elif month == 3:
        print('March')
    elif month == 4:
        print('April')
    elif month == 5:
        print('May')
    elif month == 6:
        print('June')
    elif month == 7:
        print('July')
    elif month == 8:
        print('August')
    elif month == 9:
        print('September')
    elif month == 10:
        print('October')
    elif month == 11:
        print('November')
    elif month == 12:
        print('December')
else:
    print('Enter the correct number!')
