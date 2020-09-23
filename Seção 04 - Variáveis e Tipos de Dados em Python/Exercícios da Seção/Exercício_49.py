"""
49) Faça um programa para ler o horário (hora, minuto e segundo)
de ínicio e duração em segundos, de uma experiência biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
"""

hours, minutes, seconds = map(int, input('Enter the a hour, minute, and second of the start of the operation: ').split())
duration = int(input('Enter duration in seconds: '))
add_hours = duration // 3600
add_minutes = (duration - add_hours * 3600) // 60
add_seconds = duration - (add_hours * 3600 + add_minutes * 60)
hours += add_hours
minutes += add_minutes
seconds += add_seconds
print(f'Ending is: {hours:2}:{minutes:2}:{seconds:2}')
