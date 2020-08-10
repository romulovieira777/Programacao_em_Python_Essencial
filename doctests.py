"""
Doctests


Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um teste do doctest:

python -m doctest -v nome_do_modulo.py

# Saída

def soma(a, b):
    #Soma os números a e b

    #>>> soma(1, 2)
    #3
    #
    #return a + b


Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.



# Outro exemplo, aplicando o TDD


def duplicar(valores):
    #Duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    #[2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
        ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    #return [2 * elemento for elemento in valores]



def fala_oi():
    #Fala oi

    #>>> fala_oi()
    #'Oi'
    #
    #return "Oi"

OBS: Dentro do doctest, o Python não renconhece string com aspas duplas. Precisa ser aspas simples

"""

# Um último caso estranho...


def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
