"""
15) Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/r, sendo G o ângulo
em graus e R em radianos e r = 3.14.
"""

radian = float(input('Enter the radian: '))
angle = round(radian * 180 / 3.14, 3)
print(f'The radian {radian} for angle is: {angle}')
