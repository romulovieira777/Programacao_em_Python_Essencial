"""
37) As tarifas de certo parque de estacionamento são as seguintes:
    - 1ª e 2ª hora - R$1,00 cada
    - 3ª e 4ª hora - R$1,40 cada
    - 5ª hora e seguintes - R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por execesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste
são apresentados na forma de pares de inteiros, representando horas e minutos.

Por exemplo, o par 12,50 representará 'dez para a uma da parte'. Pretende-se
criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva
na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida
se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada
for supeiror à da partida, isso não é uma situação de erro, antes siginificará que
a partida ocorreu no dia seguinte ao chegada.

"""

arrival_time = int(input('Enter arrival time: ')) # chegada hora
arrival_minute = int(input('Enter the arrival minute: ')) # chegada minuto

departure_time = int(input('Enter departure time:  ')) # partida hora
match_minute = int(input('Enter the minute of departure: ')) # partida minuto

hour_interval = 0

if (arrival_time >= 0) and (arrival_time < 24) and (departure_time >= 0) and (departure_time < 24):
    if (arrival_minute >= 0) and (arrival_minute < 60) and (match_minute >= 0) and (match_minute < 60):

        if departure_time == arrival_time and match_minute == arrival_minute:
            hour_interval += 1

        elif departure_time == arrival_time and match_minute < arrival_minute:
            hour_interval = 24

        elif departure_time > arrival_time:
            hour_interval = departure_time - arrival_time

            if arrival_minute >= match_minute:
                pass

            else:
                hour_interval += 1

        else:
            hour_interval = 24 - (arrival_time - departure_time)

            if arrival_minute >= match_minute:
                pass

            else:
                hour_interval += 1

    else:
        print('Minutes out of range 0 to 59')

else:
    print('Time out of range 0 to 23')

if hour_interval > 0:
    print(f'Parking time: {hour_interval} hours')

    if (hour_interval >= 1) and (hour_interval <= 2):
        print(f'Must pay R$1,00')

    elif (hour_interval >= 3) and (hour_interval <= 4):
        print('Must pay R$1,40')

    elif hour_interval > 5:
        print('Must pay R$2,00')

    else:
        print("Error")
