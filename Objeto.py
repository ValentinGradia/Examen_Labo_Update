import pygame
from configuraciones import *

class Objeto():
    def __init__(self,x, y, ancho, alto, path_image):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.ancho = ancho
        self.alto = alto
        self.path_image = path_image
        self.contador = 0
        self.imagen = pygame.image.load(self.path_image)
        self.superficie_imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.rectangulo = self.superficie_imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lados = obtener_rectangulo(self.rect)

    def draw(self, pantalla):
        pantalla.blit(self.superficie_imagen, self.rect)

    def animar_movimiento(self, pantalla, lista_animaciones, velocidad_animacion):
        largo = len(lista_animaciones)

        if self.contador>= largo:
            self.contador = 0
        pantalla.blit(lista_animaciones[int(self.contador)], self.lados["main"])
        self.contador += velocidad_animacion  




    

