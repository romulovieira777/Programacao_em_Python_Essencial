"""
44) Receba a altura do degrau de uma escada e a altura que o usuário
deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário
deverá subir para atingir seu objetivo.
"""

step = int(input('Enter the total of the step: '))
step_1 = int(input('Step where you want to get: '))
total_steps = step_1 / step
print('You most climb {} steps to reach a height of {} steps'.format(total_steps, step_1))
