"""
14) A nota final de um estudante é calculada a partir de três notas atribuídas entre
o intervalo de 0 até 10, respectivamente, a trabalho do laboratório, a uma avaliação
semestral e a um exame final. A média das três notas mencionadaa anteriormente obdece aos
pesos: Trabalho de Laboratório: 2; Avaliaçõ Semestral: 3; Exame final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9),
de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

note_1 = float(input('Enter the first note: '))
note_2 = float(input('Enter the second note: '))
note_3 = float(input('Enter the third note: '))
weghted_average = (note_1 + note_2 + note_3) / (2 + 3 + 5)
if ((note_1 >= 0) and (note_1 <= 20)) and ((note_2 >= 0) and (note_2 <= 30)) and ((note_3 >= 0) and (note_3 <= 50)):
    print(f'The average of your grades note: {weghted_average:.2f}')
    if(weghted_average >= 0) and (weghted_average <= 2.9):
        print('You are disapproved!')
    elif (weghted_average > 2.9) and (weghted_average <= 4.9):
        print('You are recovery!')
    else:
        print('You are approved!')
else:
    print('Enter notes between 0 and 10!')
