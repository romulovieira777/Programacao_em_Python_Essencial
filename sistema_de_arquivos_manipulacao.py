"""
Sistema de Arquivos - Manipula��o


import os

# Descobrindo se um arquivo ou diret�rio existe

# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True


# Diret�rio

# Path relativos
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('outro'))  # False


# Path absolutos
print(os.path.exists('/home/geek/university'))  # False
print(os.path.exists('/home/geek/imagens'))  # True
print(os.path.exists('/home/geek/imagens/wallpaler2.png'))  # True


import os

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


import os

# Criando arquivos

os.mknod('arquivo-teste4.txt')

os.mknod('/home/geek/university.txt')

# OBS: Se voc� estiver utilizando no Mac OS, pode haver um erro de PermissionError

# OBS: Se criando um arquivo via mknod() se o arquivo j� existir teremos o erro FileExistsError


import os

# Criando diret�rios

# Path Relativo
os.mkdir('templates')

# OBS: A fun��o mkdir() cria um diret�rio se este n�o existir. Caso exista, teremos FileExistsError


import os

# Criando diret�rios

# Path Absoluto
os.mkdir('/home/geek/templates')

# OBS: A fun��o mkdir() cria um diret�rio se este n�o existir. Caso exista, teremos FileExistsError


import os

# Criando diret�rios

# Path Absoluto
os.mkdir('/etc/templates')

# OBS: Se n�o tivermos permiss�o para criar o diret�rio teremos um PermissionError


import os

# Criando multi-diret�rios (�rvore de diret�rios)
os.makedirs('templates/geek/university/outro')

# OBS: Se j� existir, teremos um FileExistsError


import os

os.makedirs('templates2/novo2/outro2', exist_ok=True)


import os

# Renomear arquivos e diret�rios

os.rename('templates2', 'geek2')

# OBS: Se o diret�rio n�o existir teremos um FileNotFoundError

# OBS: Se o diret�rio que queremos renomear n�o estiver vazio, teremos um OSError


# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek.txt')


import os

# Renomear arquivos e diret�rios

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')


import os

# Renomear arquivos e diret�rios

# Arquivos
os.rename('frutas.txt', 'cesta.txt')


import os

# ATEN��O! Tome cuidado com os comandos de dele��o. Ao deletarmos um arquivo ou diret�rio, eles
# n�o v�o para a lixeira. Eles somem.

# Removendo arquivos
os.remove('geek.txt')

# OBS: Se voc� estiver no Windows e o arquivo que voc� for deletar estiver em uso, voc� ter� um erro.

# OBS: Caso o arquivo n�o exista, teremos o FileNotFoundError

# OBS: Se voc� informar um diret�rio ao inv�s de um arquivo, teremos um IsADirectoryError


import os

# Removendo diret�rios

os.rmdir('templates')

# OBS: Se o diret�rio tiver qualquer conte�do teremos um OSError

# OBS: Se o diret�rio n�o existir teremos um FileNotFoundError


import os

# Removendo uma �rvore de diret�rios

for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)


import os

# Podemos remover uma �rvore de diret�rios vazios

os.removedirs('geek2')

# Se algum dos diret�rios contiver arquivos ou outros diret�rios, o processo para.


import os

# ATEN��O! Ao remover arquivos e diret�rios com Python eles n�o v�o para a lixeira. Eles v�o embora!

# Importando a biblioteca send2trash (Envia arquivos e diret�rios para a lixeira)
from send2trash import send2trash

send2trash('cesta2.txt')  # Vai para lixeira. Pode ser restaurado

send2trash('teste')

# OBS: Se o arquivo n�o existir, teremos OSError.


# Trabalhando com arquivos e diret�rios tempor�rios

import os
import tempfile

# Criando um diret�rio tempor�rio
with tempfile.TemporaryDirectory() as temp:
    print(f'Crie o diret�rio tempor�rio em {temp}')
    with open(os.path.join(temp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diret�rio tempor�rio, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() s� para mantermos
# os arquivos tempor�rios 'vivos' dentro dos blocos with.

# OBS: Possivelmente, o c�digo acima n�o ir� funcionar se voc� estiver utilizando
# o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos tempor�rios.


# Trabalhando com arquivos e diret�rios tempor�rios

import os
import tempfile


# Criando um arquivo tempor�rio

with tempfile.TemporaryFile() as temp:
    temp.write(b'Geek University\n')
    temp.seek(0)
    print(temp.read())


# OBS: Em arquivos tempor�rios s� conseguimos escrever. bits. Por isso, utilizamos 'b'.

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()


arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

https://docs.python.org/3/library/os.html?highlight=os#module-os

"""
