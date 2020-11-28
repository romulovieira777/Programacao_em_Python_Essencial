"""
8) Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas
e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente,
um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este
fato deve ser informado ao usuário e o programa termina.
"""

note_1 = float(input('Enter the first note: '))
note_2 = float(input('Enter the second note: '))
if (note_1 >= 0.0) and (note_1 <= 10.0) and (note_2 >= 0.0) and (note_2 <= 10.0):
   average = (note_1 + note_2) / 2
   print(f'The average student is {average}')
else:
    print(f'Please enter a valid note!')













