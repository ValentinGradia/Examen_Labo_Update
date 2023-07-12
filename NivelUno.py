import pygame
from Nivel import Nivel
from constantes import *
from configuraciones import *
from Personaje_principal import *
from Plataforma import *
from Item import *
from Trampa import *
from Enemigo import *

class NivelUno(Nivel):
      def __init__(self, pantalla: pygame.Surface) -> None:
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load("Imagenes/Fondo/fondo.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))


        personaje_principal = Personaje_Principal(0,520,50,50,"Imagenes/Ninja Frog/Quieto/0.png",lista_animaciones_personaje_principal)


        lista_plataformas_colision_personaje = [plataforma_flotante,plataforma_flotante1,plataforma_flotante2
                         ,plataforma_flotante3,plataforma_flotante4,plataforma_flotante5,
                         plataforma_tierra, superficie_piso,superficie_ladrillo, plataforma_flotante6
                         , plataforma_flotante7]
        
        lista_plataformas = [caja,caja2,caja3,plataforma_flotante,plataforma_flotante1,
                             plataforma_flotante2, plataforma_flotante3, plataforma_flotante4,
                             plataforma_flotante5, plataforma_flotante6, plataforma_flotante7,
                             plataforma_ladrillo.lista_pisos, plataforma_tierra, 
                             plataforma_piso.lista_pisos]
        
        lista_trampas = [sierra, sierra2, pinchos11]


        
        super().__init__(pantalla, personaje_principal, lista_plataformas_colision_personaje, lista_plataformas, 
                             lista_items, lista_enemigos, lista_trampas, fondo, 1)
        
