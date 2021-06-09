"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do móduo
os.

os -> Operating System - Sistema Operacional


# Fazer o import

import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())


# Fazer o import
import os

# Podemos checar se um diretótio é absoluto ou relativo

print(os.path.isabs('c:\Users\romul'))  # True


# Fazer o import
import os

# OBS: para usuários Windows
# Se você, infelizmentem estiver utilizando um computador com Windows, terá que ter cuidado ao verificar
# diretórios.

print(os.path.isabs(' C:\\Users\\romul'))


# Fazer o import
import os

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)


# Fazer o import
import os

# Podemos ter mais detalhes no sistema operacional
print(os.name)


# Fazer o import

import sys

print(sys.platform)


import os

# 'C:\Users\romul\PycharmProjects\'

print(os.getcwd())  # C:\Users\romul\PycharmProjects\guppe

res = os.path.join(os.getcwd(), 'guppe')

os.chdir(res)

print(os.getcwd())  # C:\Users\romul\PycharmProjects\guppe

# Veja que os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretótio que será juntado ao atual.


import os

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())


import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

arquivos = list(os.scandir())

print(arquivos)

print(arquivos[0])

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatísticas...

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()

"""
