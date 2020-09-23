"""
25) Leia um valor de área em acres e apresente-o convertido
em metros quadrados m². A fórmula da conversão é: M = A*4048.58,
sendo M a área em metros quadrados e A a área em acres
"""

acres = float(input('Enter the value of the acres: '))
square_meters_area = round(acres * 4048.58, 2)
print(f'The value of the acre {acres} for square meters area is: {square_meters_area}')
