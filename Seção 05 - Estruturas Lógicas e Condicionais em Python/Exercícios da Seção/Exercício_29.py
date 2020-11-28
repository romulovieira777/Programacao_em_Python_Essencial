"""
29) Faça uma prova de matemática para crianças que estão aprendendo
a somar números inteiros menores do que 100. Escolha números aleatórios
entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b,
onde a e b são os números aleatórios. Peça a resposta. Faça cinco
perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""

from random import randint

number_1 = randint(1, 100)
number_2 = randint(1, 100)

print(f"What is the sum of {number_1} + {number_2}? ")
result_1 = int(input(""))

number_3 = randint(1, 100)
number_4 = randint(1, 100)

print(f"What is the sum of {number_3} + {number_4}? ")
result_2 = int(input(""))

number_5 = randint(1, 100)
number_6 = randint(1, 100)

print(f"What is the sum of {number_5} + {number_6}? ")
result_3 = int(input(""))

number_7 = randint(1, 100)
number_8 = randint(1, 100)

print(f"What is the sum of {number_7} + {number_8}? ")
result_4 = int(input(""))

number_9 = randint(1, 100)
number_10 = randint(1, 100)

print(f"What is the sum of {number_9} + {number_10}? ")
result_5 = int(input(""))

hit_count = 0
print()
if result_1 == (number_1 + number_2):
    hit_count += 1

if result_2 == (number_3 + number_4):
    hit_count += 1

if result_3 == (number_5 + number_6):
    hit_count += 1

if result_4 == (number_7 + number_8):
    hit_count += 1

if result_5 == (number_9 + number_10):
    hit_count += 1

print("Respostas:")
print(f"{number_1} + {number_2} = {number_1 + number_2}")
print(f"{number_3} + {number_4} = {number_3 + number_4}")
print(f"{number_5} + {number_6} = {number_5 + number_6}")
print(f"{number_7} + {number_8} = {number_7 + number_8}")
print(f"{number_9} + {number_10} = {number_9 + number_10}")
print()

print(f"Number of correct answers: {hit_count}")
