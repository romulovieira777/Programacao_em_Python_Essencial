"""
53) Faça umm programa para ler as dimensões de um terreno
(comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela.
"""

width = float(input('Enter the width: '))
lenght = float(input('Enter the lenght: '))
price = float(input('Enter the price of the meter: '))
total = price * (width ** 2 + lenght ** 2)
print(f'The value to surround the terrain is R$ {total:.2f}')
