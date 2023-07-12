import pygame


tecla_up_presionada = False
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

pygame.font.init()
pygame.init()

RELOJ = pygame.time.Clock() #NOS AYUDA A CONTROLAR LOS FRAMES


fuente = pygame.font.SysFont("helvetica",40)

imagen = pygame.image.load("Imagenes/Menu/Icon_Clock.png")
imagen = pygame.transform.scale(imagen,(50,50))

contador = 90

imagen_muerte = pygame.image.load("Imagenes/Menu/muerte.png")
imagen_muerte = pygame.transform.scale(imagen_muerte,(1200,750))

imagen_win = pygame.image.load("Imagenes/Menu/win.png")
imagen_win = pygame.transform.scale(imagen_win,(1200,750))


imagen_fondo = pygame.image.load("Imagenes/Menu/fondooo.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (1000,600))


pygame.display.set_caption("Juego de Aventura")

