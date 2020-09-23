"""
39) A importância de R$ 780.000,00 será dividida entre três
ganhadores de um concurso. Sendo que da quantia total:
 - O primeiro ganhador receberá 46%;
 - O segundo receberá 32%;
 - O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores
"""

value = 780.000
first_winner = value * 0.46
second_winner = value * 0.32
third_winner = value * 0.22
print('The value of the first winner {:.2f}, second winner {:.2f} and finally third winner {:.2f}'.
      format(first_winner, second_winner,third_winner))
