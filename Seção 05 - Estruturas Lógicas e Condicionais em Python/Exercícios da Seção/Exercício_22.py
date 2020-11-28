"""
22) Leia a idade e o tempo de serviço de um trabalhador e escreva
se ele pode ou não se aposentar. As condições para posentadoria são
    - Ter pelo menos 64,
    - Ou ter trabalhado pelo menos 30 anos,
    - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
"""

age = int(input('Enter your age: '))
time = int(input('Enter your working time: '))

if (age >= 64) or (time >= 30) or ((age >= 60) and (time >= 25)):
    print('You can retire!')
else:
    print("Can't retire!")
