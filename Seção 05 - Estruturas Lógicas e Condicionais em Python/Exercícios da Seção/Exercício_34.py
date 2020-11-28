"""
34) Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo
com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma reduçãoo
de conceito.

    |    NOTA       |  CONCEITO (ATÉ 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) |
    | 9.0 até 10.0  |             A             |              B               |
    | 7.5 até 8.9   |             B             |              C               |
    | 5.0 até 7.4   |             C             |              D               |
    | 4.0 até 4.9   |             D             |              E               |
    | 0.0 até 3.9   |             E             |              E               |

"""

note = float(input('Enter the note: '))
lack = int(input('Enter the fault: '))

if (note >= 9.0) and (note <= 10.0) and (lack >= 0) and (lack <= 20):
    print('Concept A')

elif (note >= 9.0) and (note <= 10.0) and (lack > 20):
    print('Concept B')

elif (note >= 7.5) and (note <= 8.9) and (lack >= 0) and (lack <= 20):
    print('Concept B')

elif(note >= 7.5) and (note <= 8.9) and (lack > 20):
    print('Concept C')

elif (note >= 5.0) and (note <= 7.4) and (lack >= 0) and (lack <= 20):
    print('Concept C')

elif (note >= 5.0) and (note <= 7.4) and (lack > 20):
    print('Concept D')

elif (note >= 4.0) and (note <= 4.9) and (lack >= 0) and (lack <= 20):
    print('Concept D')

elif (note >= 4.0) and (note <= 4.9) and (lack > 20):
    print('Concept E')

elif (note >= 0.0) and (note <= 3.9) and (lack >= 0) and (lack <= 20):
    print('Concept E')

elif (note >= 0.0) and (note <= 3.9) and (lack > 20):
    print('Concept E')

else:
    print('Please enter a valid note!!!')
