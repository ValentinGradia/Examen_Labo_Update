import pygame
import sys
from pygame.locals import *
from GUI_Form_prueba import FormPrueba

pygame.init()

WIDTH = 1200
HEIGHT = 600
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))

form_prueba = FormPrueba(pantalla, 200, 100, 900, 350, "gold", "Magenta", 5, True)

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("Black")
    
    form_prueba.update(eventos)

    pygame.display.flip()

