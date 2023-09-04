from animales import *
from random import choice
class Tienda:
    def __init__(self):
        self.animales= []
    def agregar_animal(self, animal):
        self.animales.append(animal)

    def entregar_animal(self):
        return choice(self.animales)