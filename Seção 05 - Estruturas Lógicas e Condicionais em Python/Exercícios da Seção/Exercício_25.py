"""
25) Calcule as raízes da equeção de 2° grau;.
    Lembrando que:
    x = – b ± √∆
          2∙a
        Onde:
    ∆ = b² - 4ac
    E ax² + bx + c = 0 representa uma equeção de 2° grau.
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem
"Não é equação de segundo grau."
    - Se ∆ < 0, não existe real. Imprima a mensagem Não existe raiz
    - Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
    - Se ∆ > 0, imprima as duas raízes reais.
"""

a = float(input('Enter the value of ax²: '))
b = float(input('Enter the value of bx: '))
c = float(input('Enter the value of c: '))

if a != 0:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('There is not root!')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'The single root is {x}')
    else:
        x1 = (-b + delta ** 0.5) / 2 * a
        x2 = (-b - delta ** 0.5) / 2 * a
        print(f'The root are {x1} and {x2}')
else:
    print("It's not a second degree equation!")
