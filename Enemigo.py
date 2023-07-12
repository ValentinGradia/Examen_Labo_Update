import pygame
from configraciones_enemigos import *
from Personaje import *
from Plataforma import *
from Proyectil import *
from configuraciones import *
from random import randint 
import random

class EnemigoCaracol(Personaje):
    def __init__(self, x, y, ancho, alto, path_image, lista_animaciones, lista_plataformas_colision) -> None:
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones)
        self.vidas = 1
        self.lista_plataformas = lista_plataformas_colision #las plataformas con  las que va a chocar
        self.daño = 1
        self.dispara = False
        self.imagen_reescalada = reescalar_imagenes(lista_animaciones,self.ancho,self.alto)
        self.direccion_aleatoria = ["derecha", "izquierda"]
        self.direccion = random.randint(0, len(self.direccion_aleatoria)- 1)

    def update(self, pantalla):
        self.detectar_colisiones_enemigo(pantalla, self.lista_plataformas)

    def desaparecer_enemigo(self, pantalla, direccion):

        self.contador = 0
        if direccion == "derecha":
            for i in range(len(desaparecer_enemigo_caracol)):
                pantalla.blit(desaparecer_enemigo_caracol[int(self.contador)], self.rect)
                self.contador += 1
        else:
            for i in range(len(desaparecer_enemigo_caracol_izq)):

                pantalla.blit(desaparecer_enemigo_caracol_izq[int(self.contador)], self.rect)
                self.contador += 0.3
        


    def detectar_colisiones_enemigo(self,pantalla,lista_plataformas):
        for plataforma in lista_plataformas:
            if self.lados["right"].colliderect(plataforma.lados["left"]):

                self.direccion = "izquierda"
            elif self.lados["left"].colliderect(plataforma.lados["right"]):

                self.direccion = "derecha"

        if self.direccion == "izquierda":
            self.animar_movimiento(pantalla,enemigo_caracol_camina,1)
            self.mover(self.velocidad*-1)
        else:
            self.animar_movimiento(pantalla, enemigo_caracol_camina_izq,1)
            self.mover(self.velocidad)




class EnemigoTrunk(Personaje):
    def __init__(self, x, y, ancho, alto, path_image,lista_animaciones,lista_plataformas_colision) -> None:
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones)
        self.lista_plataformas = lista_plataformas_colision
        self.direccion_aleatoria = ["derecha", "izquierda"]
        self.direccion = random.randint(0, len(self.direccion_aleatoria)- 1)
        self.dispara = False
        self.vidas = 1
        self.imagen_reescalada = reescalar_imagenes(lista_animaciones,self.ancho,self.alto)


    def update(self, pantalla):
        self.detectar_colisiones_enemigo(pantalla, self.lista_plataformas)

    def desaparecer_enemigo(self, pantalla, direccion):
        self.contador = 0
        if direccion == "derecha":
            for i in range(len(desaparecer_enemigo_trunk)):

                pantalla.blit(desaparecer_enemigo_trunk[self.contador], self.rect)
                self.contador += 1
        else:
            for i in range(len(desaparecer_enemigo_trunk_izq)):

                pantalla.blit(desaparecer_enemigo_trunk_izq[self.contador], self.rect)
                self.contador += 1


    def detectar_colisiones_enemigo(self,pantalla,lista_plataformas):
        for plataforma in lista_plataformas:
            if self.lados["right"].colliderect(plataforma.lados["left"]):

                self.direccion = "izquierda"
            elif self.lados["left"].colliderect(plataforma.lados["right"]):

                self.direccion = "derecha"


        if self.direccion == "izquierda":
            self.animar_movimiento(pantalla,enemigo_trunk_camina,1)
            self.mover(self.velocidad*-1)
        else:
            self.animar_movimiento(pantalla, enemigo_trunk_camina_izq,1)
            self.mover(self.velocidad)


class EnemigoPlanta(Personaje):
    def __init__(self, x, y, ancho, alto, path_image,lista_animaciones) -> None:
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones)
        self.vidas = 1
        self.lista_disparo = []
        self.velocidad_disparo = 7
        self.rect.top = y
        self.rect.left = x
        self.lista_animaciones = reescalar_imagenes(lista_animaciones, ancho, alto)



    def desaparecer_enemigo(self, pantalla, direccion):
        self.contador_dos = 0
        for i in range(len(planta_hit)):

            pantalla.blit(planta_hit[self.contador_dos], self.rect)
            self.contador_dos += 1


    def update(self, pantalla):
        self.animar_movimiento(pantalla, ataque_planta, 0.1)
        self.atacar()
        if len(self.lista_disparo) > 0:
            for objeto in self.lista_disparo:
                objeto.update(pantalla)

    def atacar(self):
        if self.contador > 6:
            self.dispara()

    def dispara(self):
        x,y = self.rect.center
        mi_proyectil = Bala(x-25,y-15, 20,20, "Imagenes/Planta/Bullet.png",-1, bala)
        self.lista_disparo.append(mi_proyectil)

class EnemigoVolador(Personaje):
    def __init__(self, x, y, ancho, alto, path_image, lista_animaciones) -> None:
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones)
        self.vidas = 1
        self.lista_disparo = []
        self.velocidad_disparo = 7
        self.rect.top = y
        self.rect.left = x
        self.lista_animaciones = reescalar_animacion(lista_animaciones, ancho, alto)

    def desaparecer_enemigo(self, pantalla, direccion):
        pass

    def update(self, pantalla):
        self.animar_movimiento(pantalla, enemigo_pajaro, 0.4)
        self.atacar()
        if len(self.lista_disparo) > 0:
            for objeto in self.lista_disparo:
                objeto.update(pantalla)

    def atacar(self):
        if (randint(0,100)< 1):
            self.dispara()

    def dispara(self):
        x,y = self.rect.center
        mi_proyectil = Bullet(x,y, 20,20, "Imagenes/Bala/0.png",1, disparo_pajaro)
        self.lista_disparo.append(mi_proyectil)


class Jefe(Personaje):
    def __init__(self, x, y, ancho, alto, path_image, lista_animaciones) -> None:
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones)
        self.vidas = 60
        self.lista_disparo = []
        self.velocidad_disparo = 12
        self.rect.top = y
        self.rect.left = x
        self.lista_animaciones = reescalar_animacion(lista_animaciones, ancho, alto)

    def update(self, pantalla):
        self.animar_movimiento(pantalla, pig, 0.4)
        self.atacar()
        if len(self.lista_disparo) > 0:
            for objeto in self.lista_disparo:
                objeto.update(pantalla)

    def atacar(self):
        if (randint(0,100) < 1):
            self.dispara()

    def dispara(self):
        x,y = self.rect.center
        mi_proyectil = Poder(x,y, 90, 90, "Imagenes/Bolt/frames/bolt1.png",-1, poder)
        self.lista_disparo.append(mi_proyectil)

    def desaparecer_enemigo(self, pantalla, direccion):
        self.vivo = False
        self.contador = 0
 
        for i in range(len(pig_die)):

            pantalla.blit(pig_die[self.contador], self.rect)
            self.contador += 1



caracol = EnemigoCaracol(350,250,50,50,"Imagenes/Snail/Caminar/0.png",lista_animaciones_caracol, lista_plataformas_colision_enemigo_caracol)
trunk = EnemigoTrunk(600,550,50,50,"Imagenes/Trunk/Caminar/0.png",lista_animaciones_trunk, lista_plataformas_colision_enemigo_trunk)

lista_enemigos = [caracol, trunk]





          