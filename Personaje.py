import pygame
from configuraciones import *
from constantes import *
from Objeto import *

class Personaje(Objeto):
    def __init__(self, x, y, ancho, alto, path_image, lista_animaciones) -> None:
        super().__init__(x, y, ancho, alto, path_image)
        self.gravedad = 1.5
        self.desplazamiento_y = 0
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.velocidad = 7

    def mover(self, vel):
        for lado in self.lados:
            self.lados[lado].x += vel



