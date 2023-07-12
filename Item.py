
from configuraciones_items import *
from constantes import *
from Objeto import *

class Item(Objeto):
    def __init__(self, x, y, ancho, alto,path_image, lista_animaciones, velocidad_animacion=1):
        super().__init__(x, y, ancho, alto, path_image)
        self.efecto = lista_animaciones
        self.contador = 0
        self.velocidad_animacion = velocidad_animacion
        self.animacion_reescalada = reescalar_animacion(lista_animaciones,self.ancho,self.alto)

    def blitear_items(self, pantalla, lista_items):
        for item in lista_items:
            item.animar_movimiento(pantalla, self.efecto, self.velocidad_animacion)
    
    def desaparecer_item(self, pantalla):
        self.contador = 0
        for i in range(len(desaparecer_item)):

            pantalla.blit(desaparecer_item[int(self.contador)], self.rect)
            self.contador += 0.1



cherry = Item(114,495,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry2 = Item(205,446,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry3 = Item(84,390,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry4 = Item(31,333,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry5 = Item(161,289,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry6 = Item(778,202,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry7 = Item(1053,267,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry8 = Item(1133,262,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry9 = Item(1124,564,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry10 = Item(817,466,30,30,"Imagenes/Fruits/2.png", cherrys)
cherry11 = Item(747,365,30,30,"Imagenes/Fruits/2.png", cherrys)


lista_items = [cherry,cherry2,cherry3,cherry4,cherry5,cherry6,
               cherry7,cherry8,cherry9, cherry10, cherry11]


