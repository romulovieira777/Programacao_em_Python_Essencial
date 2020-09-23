"""
34) Leia o valor do raio de um círculo e calcule e imprima área do círculo
correspondente. A área do círculo é r * raio², conside r = 3.141592
"""

lightning = float(input('Enter the radius value: '))
circle = round(3.141592 * lightning ** 2, 2)
print(f'The radius of a circle {lightning} for area of the circle is: {circle}')
