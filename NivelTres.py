import pygame
from Nivel import Nivel
from constantes import *
from configuraciones import *
from Personaje_principal import *
from Plataformas_nivel_tres import *
from Items_nivel_tres import *
from Trampas_nivel_tres import *
from Enemigos_nivel_tres import *

class NivelTres(Nivel):
      def __init__(self, pantalla: pygame.Surface) -> None:
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load("Imagenes/Fondo/fondo3.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        personaje_principal = Personaje_Principal(250,275,50,50,"Imagenes/Ninja Frog/Quieto/0.png",lista_animaciones_personaje_principal)
        
        lista_plataformas_colision_personaje = [superficie_piso, plataforma_flotante111, plataforma_flotante222,
                                                plataforma_flotante333, plataforma_flotante444]
        
        lista_plataformas = [plataformas.lista_pisos, plataforma_flotante111, plataforma_flotante222,
                             plataforma_flotante333, plataforma_flotante444]
        
        lista_items = [kiwi, kiwi2, kiwi3]
        
        lista_enemigos = [pajaro,pajaro2,pajaro3, jefe]

        lista_trampas = [sierra, sierra2, sierra3, sierra4, sierra5]
        
        super().__init__(pantalla, personaje_principal, lista_plataformas_colision_personaje, lista_plataformas, 
                             lista_items, lista_enemigos, lista_trampas, fondo,3)