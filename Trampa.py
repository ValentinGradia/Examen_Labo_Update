from Item import *
from configuraciones_trampas import *
from Objeto import *

class Trampa(Item):
    def __init__(self, x, y, ancho, alto, path_image, lista_animaciones, velocidad_animacion=1):
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones, velocidad_animacion)
        self.daño = 1


sierra = Trampa(945,250,50,50,"Imagenes/Trampas/Saw/0.png", sierra_animacion)
sierra2 = Trampa(895,250,50,50,"Imagenes/Trampas/Saw/0.png", sierra_animacion)

lista_sierras = [ sierra , sierra2]

pinchos11 = Trampa(600,525,30,30, "Imagenes/Trampas/Idle.png", pinchos)



