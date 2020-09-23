"""
36) Leia a altura e o raio de um cilindro círcular e imprima
o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = r * raio² * altura, onde r = 3.141592
"""

height = float(input('Enter the height value: '))
lightning = float(input('Enter the value of a circle radius: '))
cylinder = round(3.141592 * lightning ** 2 * height, 2)
print(f'The height {height} and o radius value {lightning} result in the cylinder value: {cylinder}!')
