"""
10) Faça um porgrama que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as sequintes fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 58
"""

height = float(input("Enter your height: "))
sex = str(input("Enter your sex: ")).strip()
if sex.lower() == 'm':
    print(f"Your ideal weight is: {(72.7 * height) - 58:.2f}")
else:
    print(f"Your ideal weight is: {(62.1 * height) - 44.7:.2f}")
