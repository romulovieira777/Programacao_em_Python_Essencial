"""
33) Um produto vai sofrer aumento de acordo com a tabela abaixo.
Leia o preço antigo e calcule e escreva o preço novo, e escreva uma mensagem
em função do preço novo (de acordo com a segunda tabela).

    |     PREÇO ANTIGO     |   PERCENTUAL DE AUMENTO  |
    | até R$50             |            5%            |
    | entre R$50 e R$ 100  |           10%            |
    | acima de R$100       |           15%            |

    |          PREÇO NOVO              |   MENSAGEM   |
    | até R$80                         | Barato       |
    | entre R%80 e R$120 (inclusive)   | Normal       |
    | entre R$ 120 e R$200 (inclusive) | Caro         |
    | acima de R$200                   | Muito caro   |

"""

old_price = float(input('Enter the price: '))

if (old_price >= 0) and (old_price <= 50.00):
    new_price = old_price + (old_price * 0.05)

    if new_price <= 80:
        print(f'New price {new_price:.2f} is cheap!')

elif (old_price > 50) and (old_price <= 100):
    new_price = old_price + (old_price * 0.10)

    if new_price <= 80:
        print(f'New price {new_price:.2f} is cheap!')

    elif (new_price > 80) and (new_price <= 120):
        print(f'New price {new_price:.2f} is normal')

elif old_price > 100:
    new_price = old_price + (old_price * 0.15)

    if new_price <= 80:
        print(f'New price {new_price:.2f} is cheap!')

    elif (new_price > 80) and (new_price <= 120):
        print(f'New price {new_price:.2f} is normal')

    elif (new_price > 120) and (new_price <= 200):
        print(f'New price {new_price:.2f} is expensive')

    elif new_price > 200:
        print(f'New price {new_price:.2f} is very expensive')

else:
    print('Invalid value!!!')
