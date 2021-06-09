"""
Sistema de Arquivos e Navega��o

Para fazer uso de manipula��o de arquivos do sistema operacional, precisamos importar e fazer uso do m�duo
os.

os -> Operating System - Sistema Operacional


# Fazer o import

import os

# getcwd() -> pega o current work directory - diret�rio de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diret�rio, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())


# Fazer o import
import os

# Podemos checar se um diret�tio � absoluto ou relativo

print(os.path.isabs('c:\Users\romul'))  # True


# Fazer o import
import os

# OBS: para usu�rios Windows
# Se voc�, infelizmentem estiver utilizando um computador com Windows, ter� que ter cuidado ao verificar
# diret�rios.

print(os.path.isabs(' C:\\Users\\romul'))


# Fazer o import
import os

# Podemos identificar o sistema operacional com o m�dulo os
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

# Veja que os.path.join() recebe dois par�metros, sendo o primeiro o diret�rio atual e o segundo o
# diret�tio que ser� juntado ao atual.


import os

# Podemos listar os arquivos e diret�rios com o listdir()

print(os.listdir())


import os

# Podemos listar os arquivos e diret�rios com mais detalhes com scandir()

arquivos = list(os.scandir())

print(arquivos)

print(arquivos[0])

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # � um diret�rio? False
print(arquivos[0].is_file())  # � um arquivo? True
print(arquivos[0].is_symlink())  # � um link simb�lico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho at� o arquivo
print(arquivos[0].stat())  # Estat�sticas...

# OBS: Quando utilizamos a fun��o scandir() n�s precisamos fech�-la, assim quando abrimos um arquivo.

scanner.close()

"""
