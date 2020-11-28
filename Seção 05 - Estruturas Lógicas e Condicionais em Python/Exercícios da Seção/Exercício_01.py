"""
1) Faça um programa que receba dois números e mostre qual deles é o maior.
"""

number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
if number_1 > number_2:
    print(f'The number one {number_1} greater than the number two {number_2}')
elif number_2 > number_1:
    print(f'The number two {number_2} greater then the number on {number_1}')
else:
    print(f'The numbers have the same value')
