"""
StringIO

ATEN��O: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permiss�o:
    - Permiss�o de Leitura -> Para ler o arquivo.
    - Permiss�o de Escrita -> Para escrever o arquivo.


StringIO -> Utilizando para ler e criar arquivos em mem�ria.


# Primeiro fazemos o import

from io import StringIO

mensagem = 'Esse � apenas uma string normal'


# Podemos criar um arquivo em mem�ria j� com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# Agora tendo o arquivo, podemos utilizar tudo que j� sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('Outro Texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())

"""
