"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA

OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou {num}')


# Finally

try:
    num = int(input('Informe o número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')


# OBS: O bloco finally é SEMPRE esxecutado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.


# Exemplo mais complexo ERRADO


def dividir(a, b):
    return round(a / b, 2)


num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')



# Exemplo mais complexo CORRETO

# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return round(a / b, 2)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar a divisão por zero'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))

"""
