import pygame,sys
from pygame.locals import *
from Item import *
from configraciones_enemigos import *
from configuraciones import *

class Bala(Item):
    def __init__(self, x, y, ancho, alto, path_image, direccion, lista_animaciones, velocidad_animacion=1):
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones, velocidad_animacion)

        self.velocidad = 12 * direccion
        self.rect.top = y
        self.rect.left = x
        self.direccion = direccion
        self.lista_animaciones = lista_animaciones

    def trayectoria(self):
        self.rect.left = self.rect.left + self.velocidad

    def update(self, pantalla):
        self.trayectoria()
        self.animar_movimiento(pantalla, bala, 1)




class Fuego(Item):
    def __init__(self, x, y, ancho, alto, path_image, direccion, lista_animaciones, velocidad_animacion=1):
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones, velocidad_animacion)

        self.velocidad = 12 * direccion
        self.rect.top = y
        self.rect.left = x
        self.direccion = direccion
        self.lista_animaciones = lista_animaciones

    def trayectoria(self):
        self.rect.left = self.rect.left + self.velocidad

    def update(self, pantalla):
        self.trayectoria()
        if self.direccion > 0:
            self.animar_movimiento(pantalla, fuego, 1)
        else:
            self.animar_movimiento(pantalla, fuego_izq, 1)



class Bullet(Item):
    def __init__(self, x, y, ancho, alto, path_image, direccion, lista_animaciones, velocidad_animacion=1):
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones, velocidad_animacion)

        self.velocidad = 7 * direccion
        self.rect.top = y
        self.rect.left = x
        self.direccion = direccion
        self.lista_animaciones = lista_animaciones

    def trayectoria(self):
        self.rect.left = self.rect.left + self.velocidad

    def update(self, pantalla):
        self.trayectoria()
        self.animar_movimiento(pantalla, disparo_pajaro, 1)

class Poder(Item):
    def __init__(self, x, y, ancho, alto, path_image, direccion, lista_animaciones, velocidad_animacion=1):
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones, velocidad_animacion)

        self.velocidad = 12 * direccion
        self.rect.top = y
        self.rect.left = x
        self.direccion = direccion
        self.lista_animaciones = lista_animaciones

    def trayectoria(self):
        self.rect.left = self.rect.left + self.velocidad

    def update(self, pantalla):
        self.trayectoria()
        self.animar_movimiento(pantalla, poder, 1)

