"""
Entendendo Iterators e Iterables


Iterator ->
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma fun��o next() � chamada;

Iterable ->
    - Um objeto que ir� retornar um iterator quando a fun��o iter() for chamada.


nome = 'Geek'  # � um iterable mas n�o � um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # � um iterable mas n�o � um iterator.

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


nome = 'Geek'

for letra in nome:
    print(f'{letra}')

"""
