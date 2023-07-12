from os import system 
system("cls")

import pygame, sys
from configuraciones import *
from modo import *
from Plataforma import *
from Personaje_principal import *
from Item import *
from Enemigo import *
from Trampa import *
from NivelUno import *
from NivelDos import *
from constantes import *
import os
from APIFORMS.GUI_Form_prueba import FormPrueba
    


ANCHO, ALTO = 1200, 750
FPS = 50

pygame.init()
pygame.font.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

fondo = pygame.image.load("Imagenes/Fondo/fondo4.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))


form_principal = FormPrueba(PANTALLA, 350, 100, 500, 600, "Green", 1, True)


while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            try:
                os.remove("Proyecto/APIFORMS/nivel_uno.json")
                os.remove("Proyecto/APIFORMS/nivel_dos.json")
                os.remove("Proyecto/APIFORMS/nivel_tres.json")
            except FileNotFoundError:
                pass

            pygame.quit()
            sys.exit()
            


    
    PANTALLA.blit(fondo, (0,0))
    form_principal.update(eventos)


        
    pygame.display.flip()