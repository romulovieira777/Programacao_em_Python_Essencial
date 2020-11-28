"""
15) Usando swith, escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2,
e assim por diante.
"""

day = int(input('Enter the number between 1 and 7: '))
if (day >= 1) and (day <= 7):
    if day == 1:
        print('Sunday')
    elif day == 2:
        print('Monday')
    elif day == 3:
        print('Tuesday')
    elif day == 4:
        print('Wednesday')
    elif day == 5:
        print('Thursday')
    elif day == 6:
        print('Friday')
    elif day == 7:
        print('Saturday')
else:
    print('Enter the correct number!')
