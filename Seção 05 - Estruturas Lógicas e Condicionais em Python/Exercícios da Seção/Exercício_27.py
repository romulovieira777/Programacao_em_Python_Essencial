"""
27) Excreva um programa que, dada a idade de um nadador, classique-o em
uma das seguintes categorias:
     Categoria   | Idade
     Infantil A  | 5 a 7
     Infantil B  | 8 a 10
     Juvenil A   | 11 a 13
     Juvenil B   | 14 a 17
     Sênior      | maiores de 18 anos
"""

age = int(input('Enter age: '))
if (age >= 5) and (age <= 7):
    print('Children A')
elif (age > 7) and (age <= 10):
    print('Children B')
elif (age > 10) and (age <= 13):
    print('Juvenile A')
elif (age > 13) and (age <= 17):
    print('Juvenile B')
elif age >= 18:
    print('Over 18')
else:
    print('Enter a higher age 4!')
