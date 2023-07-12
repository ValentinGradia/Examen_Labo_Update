import pygame
from Nivel import Nivel
from constantes import *
from configuraciones import *
from Personaje_principal import *
from Plataformas_nivel_dos import *
from Items_nivel_dos import *
from Trampas_nivel_dos import *
from Enemigos_nivel_dos import *

class NivelDos(Nivel):
      def __init__(self, pantalla: pygame.Surface) -> None:
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fondo = pygame.image.load("Imagenes/Fondo/fondo2.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))


        personaje_principal = Personaje_Principal(0,300,50,50,"Imagenes/Ninja Frog/Quieto/0.png",lista_animaciones_personaje_principal)
        
        lista_plataformas_colision_personaje = [plataforma_inicio, superficie_final, superficie_abajo, superficie_abajo2,
                              superficie_arriba, superficie_arriba2, plataforma_flotante,plataforma_flotante2
                              ,plataforma_flotante3,plataforma_flotante4,plataforma_flotante5]
        
        lista_plataformas = [plataforma_inicio, plataforma_arriba.lista_pisos, plataforma_abajo.lista_pisos,
                             plataforma_arriba_2.lista_pisos, plataforma_abajo_2.lista_pisos, plataforma_final.lista_pisos,
                             plataforma_flotante, plataforma_flotante2, plataforma_flotante3, plataforma_flotante4,
                             plataforma_flotante5]
        
        lista_items = [cherry11,cherry22,cherry33,cherry44,cherry55,cherry66,
                      cherry77, cherry88,kiwi11, kiwi22]
        
        lista_enemigos = [caracol,caracol2, trunk2, planta, planta2]

        lista_trampas = [ pinchos1, pinchos2, pinchos3,pinchos4, pinchos5, pinchos6,
                 pinchos7, pinchos8, pinchos9, pinchos10,pinchos11,pinchos12, 
                 pinchos13,pinchos14,pinchos15,pinchos16 ]
      
        
        super().__init__(pantalla, personaje_principal, lista_plataformas_colision_personaje, lista_plataformas, 
                             lista_items, lista_enemigos, lista_trampas, fondo,2)
