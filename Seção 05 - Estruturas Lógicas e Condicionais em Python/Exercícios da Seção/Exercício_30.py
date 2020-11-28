"""
30) Faça um programa que receba três números e mostre-o em ordem crescente.
"""
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if (number_1 > number_2) and (number_2 > number_3):
    print(f'The list in ascending order {number_3} {number_2}  {number_1}')

elif (number_1 >= number_3) and (number_3 >= number_2):
    print(f'The list in ascending order {number_2} {number_3}  {number_1}')

elif (number_2 >= number_1) and (number_1 >= number_3):
    print(f"The list in ascending order {number_3}-{number_1}-{number_2}")

elif (number_2 >= number_3) and (number_3 >= number_1):
    print(f"The list in ascending order {number_1}-{number_3}-{number_2}")

elif (number_3 >= number_1) and (number_1 >= number_2):
    print(f"The list in ascending order {number_2}-{number_1}-{number_3}")

elif (number_3 >= number_2) and (number_2 >= number_1):
    print(f"The list in ascending order {number_1}-{number_2}-{number_3}")

else:
    print("Unexpected Error!")
