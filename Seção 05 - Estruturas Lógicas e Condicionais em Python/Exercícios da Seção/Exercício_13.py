"""
13) Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

note_1 = int(input("Enter the first note: "))
note_2 = int(input("Enter the second note: "))
note_3 = int(input("Enter the third note: "))
weighted_average = (note_1 + note_2 + note_3) / (1 + 1 + 2)
if weighted_average >= 60:
    print(f'The average of your grades notes: {weighted_average:.2f}')
    print('You are approved!')
else:
    print(f'The average of your grades notes: {weighted_average:.2f}')
    print('You are disapproved!')
