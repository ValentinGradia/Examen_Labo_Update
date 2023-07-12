import pygame
from Enemigo import *
from Plataformas_nivel_dos import *

caracol = EnemigoCaracol(310,475,50,50,"Imagenes/Snail/Caminar/0.png",lista_animaciones_caracol, lista_plataformas_colision_caracol)
caracol2 = EnemigoCaracol(280,125,50,50,"Imagenes/Trunk/Caminar/0.png",lista_animaciones_caracol, lista_plataformas_colision_caracol)
trunk2 = EnemigoTrunk(950,300,50,50,"Imagenes/Trunk/Caminar/0.png",lista_animaciones_trunk, lista_plataformas_colision_trunk)

planta = EnemigoPlanta(750,475,50,50,"Imagenes/Planta/Ataque/0.png",lista_animaciones_planta)
planta2 = EnemigoPlanta(560,125,50,50,"Imagenes/Planta/Ataque/0.png",lista_animaciones_planta)