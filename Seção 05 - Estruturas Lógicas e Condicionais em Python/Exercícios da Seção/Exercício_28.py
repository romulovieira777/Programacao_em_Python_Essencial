"""
28) Faça um programa que leia três números inteiros positivos e efetue
o cálculo de uma das seguintes médias de acordo com um valor numérico
digitado pelo usuário:
    (a) Geométrica: ³√x * y * z
    (b) Ponderada: (x + 2 * y + 3 * z) / 6
    (c) Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))
    (d) Aritmética: (x + y + z) / 3
"""

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the third number: '))

print("[1] Geométrica: ³√x * y * z\n"
      "[2] Ponderada: (x + 2 * y + 3 * z) / 6\n"
      "[3] Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))\n"
      "[4] Aritmética: (x + y + z) / 3")

choice = int(input("Escolha o tipo do cáculo [1][2][3][4]: "))

if choice == 1:
    result = (x * y * z) ** (1 / 3)
    print(f'The geometric mean is {result:.2f}')
elif choice == 2:
    result = (x + 2 * y + 3 * z) / 6
    print(f'The weighted averge is {result:.2f}')
elif choice == 3:
    result = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f'The harmonic mean is {result:.2f}')
elif choice == 4:
    result = (x + y + z) / 3
    print(f'The arithmetic mean is {result:.2f}')
else:
    print('Please enter a valid option!')
