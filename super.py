"""
POO - O método super()



class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie) possível fazer
        super().__init__(nome, especie) # Recomendado usar nesse modelo
        super().faz_som('auauauauau')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')

"""
