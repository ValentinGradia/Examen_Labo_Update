import pygame
from configuraciones import *
from constantes import *
from Personaje import *
from configraciones_enemigos import *
from configuraciones_items import *
from Proyectil import *

pygame.init()
pygame.font.init()

fuente = pygame.font.SysFont("helvetica",40)


class Personaje_Principal(Personaje):
    def __init__(self, x, y, ancho, alto, path_image, lista_animaciones) -> None:
        super().__init__(x, y, ancho, alto, path_image, lista_animaciones)
        self.posicion_x = x
        self.posicion_y = y
        self.que_hace = "quieto"
        self.esta_saltando = False
        self.flag = False #verificar doble salto
        self.en_plataforma = False
        self.chocado_derecha = False
        self.chocado_izq = False
        self.score = 0
        self.vidas = 3
        self.daño = 1
        self.direccion = "derecha"
        self.ejecutar_sonido = True
        self.lista_disparo = []
        self.lista_enemigos_muertos = []
        self.imagen_reescalada = reescalar_imagenes(lista_animaciones,self.ancho,self.alto)

    def aplicar_gravedad(self,pantalla, lista_plataformas): 
        if self.esta_saltando == True:

            for lados in self.lados:
                self.lados[lados].y += self.desplazamiento_y
            self.en_plataforma = False

            if (self.desplazamiento_y + self.gravedad) < self.limite_velocidad_caida:

                self.desplazamiento_y += self.gravedad

        for plataforma in lista_plataformas:
                if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                    self.esta_saltando  = False
                    self.desplazamiento_y = 0
                    self.en_plataforma = True   
                    self.lados["main"].bottom = plataforma.lados["main"].top
                    break
                elif self.lados["right"].colliderect(plataforma.lados["left"]):
                    self.chocado_derecha = True
                    self.chocado_izq = False
                elif self.lados["left"].colliderect(plataforma.lados["right"]):
                    self.chocado_derecha = False
                    self.chocado_izq = True
                else:
                    self.esta_saltando = True


    def detectar_colisiones_item(self,pantalla, lista_items:list):
        for item in lista_items:
            if self.lados["main"].colliderect(item.lados["main"]):
                if item.efecto == kiwis and self.vidas < 3:
                    if self.ejecutar_sonido:
                        self.sonido = pygame.mixer.Sound("Proyecto/APIFORMS/items.wav")
                        self.sonido.set_volume(0.1)
                        self.sonido.play()
                    lista_items.remove(item)
                    self.vidas += 1
                    break
                elif item.efecto != kiwis:
                    self.score += 1
                    item.desaparecer_item(pantalla)
                    lista_items.remove(item)
                break

    def detectar_colisiones_trampas(self, lista_trampas):
        for trampa in lista_trampas:
            if self.lados["main"].colliderect(trampa.lados["main"]):
                self.vidas = self.vidas -1
                self.reaparecer_personaje(self.lados)

    def detectar_colisiones_enemigo(self, pantalla, lista_enemigo):
        for enemigo in lista_enemigo:
            if self.lados["bottom"].colliderect(enemigo.lados["top"]):
                if self.ejecutar_sonido:
                    self.sonido = pygame.mixer.Sound("Proyecto/APIFORMS/coli.wav")
                    self.sonido.set_volume(0.1)
                    self.sonido.play()
                try:
                    enemigo.desaparecer_enemigo(pantalla, enemigo.direccion)
                except AttributeError:
                    pass
                lista_enemigo.remove(enemigo)
                self.lista_enemigos_muertos.append(enemigo)
                self.desplazamiento_y = -11
                for lados in self.lados:
                    self.lados[lados].y += self.desplazamiento_y
                
                if (self.desplazamiento_y + self.gravedad) < 11:
                    self.desplazamiento_y += self.gravedad

            elif self.lados["right"].colliderect(enemigo.lados["left"]):
                self.animar_movimiento(pantalla, personaje_hit, 1)
                self.reaparecer_personaje(self.lados)
                self.vidas = self.vidas -1

            elif self.lados["left"].colliderect(enemigo.lados["right"]):
                self.animar_movimiento(pantalla, personaje_hit_izq, 0.2)
                self.reaparecer_personaje(self.lados)
                self.vidas = self.vidas -1

    def detectar_colisiones_bala(self,pantalla, lista_balas:list):
        for bala in lista_balas:
            if self.lados["main"].colliderect(bala.lados["main"]):
                self.vidas = self.vidas -1
                if self.direccion == "derecha":
                    self.animar_movimiento(pantalla, personaje_hit, 0.2)
                else:
                    self.animar_movimiento(pantalla, personaje_hit_izq, 0.2)

                lista_balas.remove(bala)
                self.reaparecer_personaje(self.lados)


    def blitear_puntaje_vidas(self, pantalla):
        pantalla.blit(icono_fruits,(2,5))
        puntaje = fuente.render(" X {0}".format(self.score),True,("Black"))
        pantalla.blit(puntaje,(40,0))
        pantalla.blit(icono_vidas,(110,5))
        vidas = fuente.render(" X {0}".format(self.vidas),True,("Black"))
        pantalla.blit(vidas,(150,0))

    def disparar(self, x, y):

        if self.direccion == "derecha":
            mi_proyectil = Fuego(self.rect.x, self.rect.y, 45,45, "Imagenes/Fuego/1.png", 1,fuego)
        else:
            mi_proyectil = Fuego(self.rect.x, self.rect.y, 45,45, "Imagenes/Fuego/1.png", -1,fuego_izq)

        self.lista_disparo.append(mi_proyectil) 
    
    def recorrer_disparos(self, pantalla):
        if len(self.lista_disparo) > 0:
            for objeto in self.lista_disparo:
                objeto.update(pantalla)

    def detectar_colisiones_enemigos_disparo(self, pantalla, lista_enemigos:list):
        for disparos in self.lista_disparo:
            for enemigo in lista_enemigos:
                if disparos.lados["main"].colliderect(enemigo.lados["main"]):
                    enemigo.vidas = enemigo.vidas - 1
                    self.lista_disparo.remove(disparos)
                    if enemigo.vidas < 1:
                        lista_enemigos.remove(enemigo)
                        self.lista_enemigos_muertos.append(enemigo)
                        

    def detectar_colisiones_plataformas_disparo(self, pantalla, lista_plataformas):
        for disparos in self.lista_disparo:
            for plataforma in lista_plataformas:
                if disparos.lados["main"].colliderect(plataforma.lados["main"]):
                    self.lista_disparo.remove(disparos)

    def detectarl_colisiones_pantalla_disparo(self):
        for disparos in self.lista_disparo:
            if disparos.lados["main"].x > 1200 or disparos.lados["main"].x < 0:
                self.lista_disparo.remove(disparos)


    def reaparecer_personaje(self, rect_personaje:pygame.Rect):

        rect_personaje["main"].x = self.posicion_x
        rect_personaje["main"].y = self.posicion_y
        rect_personaje["top"].x = rect_personaje["main"].left
        rect_personaje["top"].y = rect_personaje["main"].top
        rect_personaje["bottom"].x = rect_personaje["main"].left
        rect_personaje["bottom"].y = rect_personaje["main"].bottom-6
        rect_personaje["left"].x = rect_personaje["main"].left
        rect_personaje["left"].y = rect_personaje["main"].top
        rect_personaje["right"].x = rect_personaje["main"].right-2
        rect_personaje["right"].y = rect_personaje["main"].top

    def obtener_score(self):
        return self.score
    
    def obtener_vidas(self):
        return self.vidas
    
    def obtener_lista_enemigos(self):
        return self.lista_enemigos_muertos


    def update(self, pantalla,lista_plataformas_blit,plataformas_colision,
               lista_items, lista_enemigos, lista_trampas):
        
        pygame.mixer.init()

        for plataformas in lista_plataformas_blit:
            if type(plataformas) == list:
                for plataforma in plataformas:
                    plataforma.draw(pantalla)
            else:
                plataformas.draw(pantalla)

        match self.que_hace:
            case "corre derecha":
                self.chocado_izq = False
                self.chocado_derecha = False
                self.direccion = "derecha"
                self.animar_movimiento(pantalla,personaje_corre_der,1)
                self.mover(self.velocidad)
            case "corre izquierda":
                self.chocado_izq = False
                self.chocado_derecha = False
                self.direccion = "izquierda"
                self.animar_movimiento(pantalla,personaje_corre_izq,1)
                self.mover(self.velocidad*-1)
            case "salta":
                self.flag = True
                if self.direccion == "derecha":
                    self.animar_movimiento(pantalla,personaje_salto,1)
                else:
                    self.animar_movimiento(pantalla,personaje_salta_izq,1)
                if self.en_plataforma:
                    if self.ejecutar_sonido:
                        self.sonido = pygame.mixer.Sound("Proyecto/APIFORMS/jump.wav")
                        self.sonido.set_volume(0.1)
                        self.sonido.play()
                    self.en_plataforma = False
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "doblesalto":
                if self.flag and self.esta_saltando:   
                    self.flag = False
                    if self.direccion == "derecha":
                        self.animar_movimiento(pantalla,personaje_doble_salto,0.5)
                    else:
                        self.animar_movimiento(pantalla,personaje_doble_salto_izq,0.5)
                    
                    self.desplazamiento_y = self.potencia_salto  

            case "quieto":
                if self.direccion == "derecha":
                    self.animar_movimiento(pantalla, personaje_quieto,1)
                else:
                    self.animar_movimiento(pantalla, personaje_quieto_izquierda,1)

        self.aplicar_gravedad(pantalla, plataformas_colision)
        self.detectar_colisiones_item(pantalla, lista_items)
        self.detectar_colisiones_enemigo(pantalla, lista_enemigos)
        self.detectar_colisiones_trampas(lista_trampas)
        self.blitear_puntaje_vidas(pantalla)
        self.recorrer_disparos(pantalla)
        self.detectar_colisiones_plataformas_disparo(pantalla, plataformas_colision)
        self.detectarl_colisiones_pantalla_disparo()
        self.detectar_colisiones_enemigos_disparo(pantalla, lista_enemigos)
        
        for item in lista_items:
            item.animar_movimiento(pantalla, item.efecto, item.velocidad_animacion)

        for trampa in lista_trampas:
            trampa.animar_movimiento(pantalla, trampa.efecto, trampa.velocidad_animacion)

        for enemigo in lista_enemigos:
            if enemigo.dispara:
                self.detectar_colisiones_bala(pantalla, enemigo.lista_disparo)
            enemigo.update(pantalla)




lista_animaciones_personaje_principal = [personaje_quieto, personaje_corre_der, personaje_corre_izq, personaje_salto, 
                        personaje_salta_izq, personaje_quieto_izquierda, personaje_doble_salto, 
                        personaje_doble_salto_izq, personaje_hit, personaje_hit_izq, personaje_caida, personaje_caida_izq]






        


                     

    
