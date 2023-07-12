import pygame
from Plataforma import Plataforma
from Objeto import Objeto


plataforma_inicio = Plataforma(0,350,120,120,"Imagenes/Terrain/Terrain/ladrillo.png")


plataforma_arriba = Plataforma(250,175,120,120,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_arriba.crear_superficies_x(2)

superficie_arriba = Objeto(250,175,240,120, "Imagenes/Terrain/Terrain/ladrillo.png")

plataforma_arriba_2 = Plataforma(550,175,120,120,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_arriba_2.crear_superficies_x(2)

superficie_arriba2 = Objeto(550,175,240,120, "Imagenes/Terrain/Terrain/ladrillo.png")


plataforma_abajo = Plataforma(250,525,120,120,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_abajo.crear_superficies_x(2)

superficie_abajo= Objeto(250,525,240,120, "Imagenes/Terrain/Terrain/ladrillo.png")

plataforma_abajo_2 = Plataforma(550,525,120,120,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_abajo_2.crear_superficies_x(2)

superficie_abajo2= Objeto(550,525,240,120, "Imagenes/Terrain/Terrain/ladrillo.png")

plataforma_final = Plataforma(900,350,120,120,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_final.crear_superficies_x(3)

superficie_final = Objeto(900,350,300,120, "Imagenes/Terrain/Terrain/ladrillo.png")


#plataformas flotantes
plataforma_flotante = Plataforma(109,269,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante2 = Plataforma(179,213,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante3 = Plataforma(160,435,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante4 = Plataforma(805,425,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante5 = Plataforma(822,263,55,12,"Imagenes/Terrain/Terrain/4.png")


plataforma_colision_caracol = Plataforma(235,485,30,30,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_colision_caracol2 = Plataforma(479,485,30,30,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_colision_caracol3 = Plataforma(235,145,30,30,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_colision_caracol4 = Plataforma(479,145,30,30,"Imagenes/Terrain/Terrain/ladrillo.png")

lista_plataformas_colision_caracol = [plataforma_colision_caracol, plataforma_colision_caracol2,
                                      plataforma_colision_caracol3, plataforma_colision_caracol4]

plataforma_colision_trunk3 = Plataforma(900,310,30,30,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_colision_trunk4 = Plataforma(1180,310,30,30,"Imagenes/Terrain/Terrain/ladrillo.png")

lista_plataformas_colision_trunk = [plataforma_colision_trunk3,plataforma_colision_trunk4]

lista_plataformas_blitear = [plataforma_inicio, plataforma_arriba.lista_pisos, plataforma_abajo.lista_pisos,
                             plataforma_arriba_2.lista_pisos, plataforma_abajo_2.lista_pisos, plataforma_final.lista_pisos,
                             plataforma_flotante, plataforma_flotante2, plataforma_flotante3, plataforma_flotante4,
                             plataforma_flotante5]

lista_plataformas_colision = [plataforma_inicio, superficie_final, superficie_abajo, superficie_abajo2,
                              superficie_arriba, superficie_arriba2, plataforma_flotante,plataforma_flotante2
                              ,plataforma_flotante3,plataforma_flotante4,plataforma_flotante5]