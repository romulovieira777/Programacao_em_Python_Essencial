"""
32) Escrever um programa que leia o código do produto escolhido do cardápio
de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago
por aquele lanche. Considere que a cada execução somente será calculado um
pedido. O cardápio da lanchonete segue o padrão abaixo:

    | Especificação    | Código | Preço |
    | Cachorro Quente  |  100   | 1.20  |
    | Bauru Simples    |  101   | 1.30  |
    | Bauru com Ovo    |  102   | 1.50  |
    | Hamburguer       |  103   | 1.20  |
    | Cheeseburguer    |  104   | 1.70  |
    | Suco             |  105   | 2.20  |
    | Refrigerante     |  106   | 1.00  |
"""

code = int(input('Enter the code: '))
amount = int(input('Enter the quantity: '))

if code == 100:
    print(f'The total amount of your order is {amount * 1.20:.2f}')
elif code == 101:
    print(f'The total amount of your order is {amount * 1.30:.2f}')
elif code == 102:
    print(f'The total amount of your order is {amount * 1.50:.2f}')
elif code == 103:
    print(f'The total amount of your order is {amount * 1.20:.2f}')
elif code == 104:
    print(f'The total amount of your order is {amount * 1.70:.2f}')
elif code == 105:
    print(f'The toal amount of your order is {amount * 2.20:.2f}')
elif code == 106:
    print(f'The total amount of your order is {amount * 1.00:.2f}')
else:
    print('Invalid Code!!!')
