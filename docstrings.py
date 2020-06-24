"""
Documentação funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentação com a função help()


# Exemplos


def diz_oi():
    '''Uma função simples que retorna a string 'Oi!''''
    return 'Oi!'


print(diz_oi())

print(help(diz_oi()))

print(diz_oi.__doc__)

# Exemplos


def exponencial(numero, potencia=2):
    '''
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    :param numero: Número que desejamos gerar exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    '''

    return numero ** potencia
    
"""
