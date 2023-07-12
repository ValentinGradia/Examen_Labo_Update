import pygame
from Objeto import Objeto

class Plataforma(Objeto):
    def __init__(self, x, y, ancho, alto, path_image):
        super().__init__(x, y, ancho, alto, path_image)
        # self.path_image = pygame.image.load(self.imagen)
        # self.superficie_imagen = pygame.transform.scale(self.path_image, (self.ancho, self.alto))
        self.esta_visible = True

    def crear_superficies_x(self,columnas):
        self.lista_pisos = []

        for i in range(columnas):
            self.piso = Plataforma(self.rect.x,self.rect.y,
                            self.ancho,self.alto,self.path_image)
            self.rect.x += self.ancho
            self.lista_pisos.append(self.piso)

    def blitear_pisos(self, pantalla, lista_plataformas):
        for plataforma in lista_plataformas:
            self.draw(pantalla, plataforma)


plataforma_piso = Plataforma(0,600,150,150,"Imagenes/Terrain/Terrain/1.png")
plataforma_piso.crear_superficies_x(8)


plataforma_flotante = Plataforma(103,530,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante1 = Plataforma(194,481,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante2 = Plataforma(73,425,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante3 = Plataforma(20,368,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante4 = Plataforma(150,324,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante5 = Plataforma(735,235,100,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante6 = Plataforma(800,500,55,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante7 = Plataforma(730,400,55,12,"Imagenes/Terrain/Terrain/4.png")

plataforma_tierra = Plataforma(300,300,300,600,"Imagenes/Terrain/Terrain/bloque.png")

plataforma_ladrillo = Plataforma(900,300,150,150,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_ladrillo.crear_superficies_x(2)

plataforma_colision_enemigo_caracol = Objeto(300,265,20,30,"Imagenes/Terrain/Terrain/ladrillo.png")
plataforma_colision_enemigo_caracol2 = Objeto(570,265,20,30,"Imagenes/Terrain/Terrain/ladrillo.png")

plataforma_colision_enemigo_trunk = Objeto(1149,570,20,30,"Imagenes/Terrain/Terrain/ladrillo.png")

caja = Plataforma(248,545,60,60, "Imagenes/Boxes/Box1/Idle.png")
caja2 = Plataforma(207,545,60,60, "Imagenes/Boxes/Box1/Idle.png")
caja3 = Plataforma(248,497,60,60, "Imagenes/Boxes/Box1/Idle.png")

lista_cajas = [caja, caja2, caja3]



superficie_piso = Objeto(0,600,1200,150,"Imagenes/Boxes/Box1/Idle.png")
superficie_ladrillo = Objeto(900,300,300,150,"Imagenes/Boxes/Box1/Idle.png")

plataformas_flotantes = [plataforma_flotante,plataforma_flotante1,plataforma_flotante2
                         ,plataforma_flotante3,plataforma_flotante4,plataforma_flotante5,
                         plataforma_flotante6,plataforma_tierra, plataforma_flotante7, 
                         ]

lista_plataformas_colision_enemigo_caracol = [plataforma_colision_enemigo_caracol, 
                                             plataforma_colision_enemigo_caracol2]

lista_plataformas_colision_enemigo_trunk = [plataforma_colision_enemigo_trunk, plataforma_tierra]

plataformas_colision = [plataforma_flotante,plataforma_flotante1,plataforma_flotante2
                         ,plataforma_flotante3,plataforma_flotante4,plataforma_flotante5,
                         plataforma_tierra, superficie_piso,superficie_ladrillo, plataforma_flotante6
                         , plataforma_flotante7]




lista_blitear_plataformas = [caja,caja2,caja3,plataforma_flotante,plataforma_flotante1,
                             plataforma_flotante2, plataforma_flotante3, plataforma_flotante4,
                             plataforma_flotante5, plataforma_flotante6, plataforma_flotante7,
                             plataforma_ladrillo.lista_pisos, plataforma_tierra, 
                             plataforma_piso.lista_pisos]


