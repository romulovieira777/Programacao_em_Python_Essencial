"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in intervalo:
    //execução do loop



Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em lista

#  Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)


#  Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

#  Exemplo de for 3 (Iterando sobre um range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
9
10 - Não
"""
for numero in range(1, 10):
    print(numero)

"""
Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'u')...)
"""
for i, v in enumerate(nome):
    print(nome[i])


for indice, letra in enumerate(nome):
    print(letra)

"""
Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
"""
for _, letra in enumerate(nome):
    print(letra)


for valor in enumerate(nome):
    print(valor)


qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


for letra in nome:
    print(letra, end='')


#  Original: U+1F60D
#  Modificado: U0001F60D

emoji = '\U0001F60D'

for _ in range(3):
    for num in range(1, 11):
        print(f'{emoji * num}')
