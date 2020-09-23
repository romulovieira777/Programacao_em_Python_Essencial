"""
24) Leia um valor de área em metros quadrados e m² e apresente-o
convertido em acres. A fórmula de conversão é: A = M * 0,000247, sendo M
a área em metros quadrados e A área em acres.
"""

sqaure_meters_area = float(input('Enter the area value in square meters: '))
acres = round(sqaure_meters_area * 0.000247, 2)
print(f'The area value in square meters {sqaure_meters_area} for acres is; {acres}')
