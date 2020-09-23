"""
10) Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida
em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade
em km/h e M em m/s.
"""

velocity = float(input('Enter speed in Km: '))
meters = round(velocity / 3.6, 2)
print(f'The speed in km {velocity} to meters is: {meters}')
