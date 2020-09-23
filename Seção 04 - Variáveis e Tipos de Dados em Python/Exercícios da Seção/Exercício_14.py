"""
14) Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * r / 180, sendo G o ângulo em graus
e R em radianos e r = 3.14.
"""

angle = float(input('Enter the angle: '))
radian = round(angle * 3.14 / 180, 3)
print(f'The agle {angle} for radian is: {radian}')
