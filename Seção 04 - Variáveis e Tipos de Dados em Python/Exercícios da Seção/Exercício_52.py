"""
52) Três amigos jogaram na loteria. Caso eles ganhem,
o prêmio deve ser repartido porporcionalmente ao valor
que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

friend_1 = float(input('Enter stake: '))
friend_2 = float(input('Enter stake: '))
friend_3 = float(input('Enter stake: '))
prize_amount = float(input('Enter the prize amount: '))
player_1 = prize_amount * (friend_1 / prize_amount)
player_2 = prize_amount * (friend_2 / prize_amount)
player_3 = prize_amount * (friend_3 / prize_amount)
print(f'The player 1 won R$ {player_1:.2f}, player 2 R$ {player_2:.2f} finally player 3 R$ {player_3:.2f}')
