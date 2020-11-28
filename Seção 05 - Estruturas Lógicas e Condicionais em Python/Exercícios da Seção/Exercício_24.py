"""
24) Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%;
SP 12%; RJ %15; MS 8%). Faça um programa em que o usuário entre com o valor
e o estado destino do produto e o programa retorne o preço final do produto
acrescido do imposto do estado em que ele será vendido. Se o estado digitado
não for válido, mostrar uma mensagem de erro.
"""

value = float(input('Enter the value: '))
state = str(input('Enter the state: ')).strip()

if state.lower() == 'mg':
    print(f'The price of the product with tax applied is {value + value * 0.07:.2f}')
elif state.lower() == 'sp':
    print(f'The price of the product with tax applied is {value + value * 0.12:.2f}')
elif state.lower() == 'rj':
    print(f'The price of the product with tax applied is {value + value * 0.15:.2f}')
elif state.lower() == 'ms':
    print(f'The price of the product with tax applied is {value + value * 0.08:.2f}')
else:
    print('Invalid state!')
