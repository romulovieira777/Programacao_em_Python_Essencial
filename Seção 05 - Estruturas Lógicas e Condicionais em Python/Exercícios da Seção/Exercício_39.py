"""
39) Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
tabela que consideraa o salário atual e o tempo de serviço de cada funcionário.
Os funcionários com menor salário terão um aumento proporcionalmente maior do que
os funciopnários com um salário maior, e conforme o tempo de serviço na empresa, cada
funcionário irá receber um bônus adicional de salário. Faça um programa que leia:

    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
    empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima
o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha
direito a nenhum aumento.

    |   Salário Atual   |   Reajuste    | Tempo de Serviço |  Bônus     |
    | Até 500,00        |     25%       | Abaixo de 1 ano  | Sem bônus  |
    | Até 1000,00       |     20%       | De 1 a 3 anos    |  100,00    |
    | Até 1500,00       |     15%       | De 4 a 6 anos    |  200,00    |
    | Até 2000,00       |     10%       | De 7 a 10 anos   |  300,00    |
    | Acima de 2000,00  | Sem reajuste  | Mais de 10 anos  |  500,00    |

"""

current_wage = float(input("Enter the employee's salary: "))
service_time = int(input("Enter the employee's length of service in years: "))

if (current_wage > 0) and (current_wage <= 500) and (service_time >= 0) and (service_time < 1):
    new_salary = current_wage + (current_wage * 0.25)
    print(f'Your new salary is {new_salary:.2f}!')

elif (current_wage > 500) and (current_wage <= 1000) and (service_time >= 1) and (service_time <= 3):
    new_salary = current_wage + (current_wage * 0.20) + 100
    print(f'Your new salary is {new_salary:.2f}!')

elif (current_wage > 1000) and (current_wage <= 1500) and (service_time > 3) and (service_time <= 6):
    new_salary = current_wage + (current_wage * 0.15) + 200
    print(f'Your new salary is {new_salary:.2f}!')

elif (current_wage > 1500) and (current_wage <= 2000) and (service_time > 6) and (service_time <= 10):
    new_salary = current_wage + (current_wage * 0.10) + 300
    print(f'Your new salary is {new_salary:.2f}!')

elif (current_wage > 2000) and (service_time > 10):
    new_salary = current_wage + 500
    print(f'Your new salary is {current_wage:.2f}!')
