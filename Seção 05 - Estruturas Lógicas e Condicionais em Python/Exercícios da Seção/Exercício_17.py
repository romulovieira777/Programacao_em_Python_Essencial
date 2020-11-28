"""
17) Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
    A = ((basemaior + basemenor) * altura) / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""

larger_base = float(input('Enter the value of the largest base: '))
smaller_base = float(input('Enter the lower base value: '))
height = float(input('Enter the height value: '))
if (larger_base > 0) and (smaller_base > 0):
    area = ((larger_base + smaller_base) * height) / 2
    print(f'Trapezoid area is {area:.2f}')
else:
    print('Invalid numbers!')
