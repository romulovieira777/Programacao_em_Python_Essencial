"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Interar sobre dicionários

for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])


for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')


receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

print(receita.keys())


for chave in receita.keys():
    print(receita[chave])


receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Acessando os valores

print(receita.values())


for valor in receita.values():
    print(valor)


receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')


receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""
