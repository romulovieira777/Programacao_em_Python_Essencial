"""
11) Leia uma velocidade em m/s (metros por segundo) e apresente-a
convertida em km/h (quilômetros por hora). A fórmula de conversão é: K = M * 3.6,
sendo K a velocidade km/h e M em m/s
"""

meters = float(input('Enter speed in meters: '))
km = round(meters * 3.6, 2)
print(f'The speed in meters {meters} to km is: {km}')
