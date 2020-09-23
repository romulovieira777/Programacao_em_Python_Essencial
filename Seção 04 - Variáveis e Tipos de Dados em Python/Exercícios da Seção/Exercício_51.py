"""
51) Escreva um programa que leia as coordenadas x e y de pontos
no R² e calcule sua distância da origem (0, 0)
"""

x = int(input('Enter the number x: '))
y = int(input('Enter the number y: '))
result = (x ** 2 + y ** 2) ** 0.5
print(f'Your distance is {result:.2f}')
