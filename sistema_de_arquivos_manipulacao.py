"""
Sistema de Arquivos - Manipulação


import os

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True


# Diretório

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

# OBS: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError

# OBS: Se criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError


import os

# Criando diretórios

# Path Relativo
os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError


import os

# Criando diretórios

# Path Absoluto
os.mkdir('/home/geek/templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError


import os

# Criando diretórios

# Path Absoluto
os.mkdir('/etc/templates')

# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError


import os

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university/outro')

# OBS: Se já existir, teremos um FileExistsError


import os

os.makedirs('templates2/novo2/outro2', exist_ok=True)


import os

# Renomear arquivos e diretórios

os.rename('templates2', 'geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError


# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek.txt')


import os

# Renomear arquivos e diretórios

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')


import os

# Renomear arquivos e diretórios

# Arquivos
os.rename('frutas.txt', 'cesta.txt')


import os

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira. Eles somem.

# Removendo arquivos
os.remove('geek.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError


import os

# Removendo diretórios

os.rmdir('templates')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError


import os

# Removendo uma árvore de diretórios

for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)


import os

# Podemos remover uma árvore de diretórios vazios

os.removedirs('geek2')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.


import os

# ATENÇÃO! Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

send2trash('cesta2.txt')  # Vai para lixeira. Pode ser restaurado

send2trash('teste')

# OBS: Se o arquivo não existir, teremos OSError.


# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as temp:
    print(f'Crie o diretório temporário em {temp}')
    with open(os.path.join(temp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: Possivelmente, o código acima não irá funcionar se você estiver utilizando
# o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos temporários.


# Trabalhando com arquivos e diretórios temporários

import os
import tempfile


# Criando um arquivo temporário

with tempfile.TemporaryFile() as temp:
    temp.write(b'Geek University\n')
    temp.seek(0)
    print(temp.read())


# OBS: Em arquivos temporários só conseguimos escrever. bits. Por isso, utilizamos 'b'.

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
