import pygame
from modo import *
from constantes import *
import json


class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas_colision_personaje,
                  lista_plataformas,lista_items,lista_enemigos, lista_trampas, fondo, nivel
                  ) -> None:

        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas_colision = lista_plataformas_colision_personaje
        self.plataformas = lista_plataformas
        self.items = lista_items
        self.enemigos = lista_enemigos
        self.trampas = lista_trampas
        self.imagen_fondo = fondo
        self.nivel = nivel
        self.estrellas = 0
        self.estrellas_dos = 0
        self.estrellas_tres = 0
        self.contador = 0
        self.contador_dos = 0
        self.contador_tres = 0
        self.segundos = 0
        self.segundos_dos = 0
        self.segundos_tres = 0
        self.acabo_tiempo = False

    def update(self, lista_eventos):
        
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()


        self.actualizar_pantalla()
        self.leer_inputs()
        self.dibujar_rectangulos()
        diccionario = {}
        # diccionario["Puntaje"] = [self.score_jugador()]

        # self._slave.blit(imagen,(600,0))

        if (self.contador or self.contador_dos or self.contador_tres) < 0:
            self.acabo_tiempo = True


        if self.nivel == 1:
            
            if self.score_jugador() == 11:
                self.segundos = 0
                if len(self.jugador.lista_enemigos_muertos) == 0:
                    self.estrellas = 1

                elif len(self.jugador.lista_enemigos_muertos) == 1:
                    self.estrellas = 2

                elif len(self.jugador.lista_enemigos_muertos) == 2:
                    self.estrellas = 3

                with open("Proyecto/APIFORMS/nivel_uno.json",'w') as archivo:
                    lista_datos = []
                    diccionario_puntaje = {}
                    diccionario_puntaje["Puntaje"] = self.score_jugador()
                    diccionario_puntaje["Valoracion"] = self.estrellas
                    lista_datos.append(diccionario_puntaje)
                    diccionario["Datos"] = lista_datos
                    
                    json.dump(diccionario,archivo, indent=4)

        elif self.nivel == 2:
            if self.score_jugador() == 8:
                if len(self.jugador.lista_enemigos_muertos) < 2:
                    self.estrellas_dos = 1

                elif len(self.jugador.lista_enemigos_muertos) < 5:
                    self.estrellas_dos = 2

                elif len(self.jugador.lista_enemigos_muertos) == 5:
                    self.estrellas_dos = 3

                with open("Proyecto/APIFORMS/nivel_dos.json",'w') as archivo:

                    lista_datos = []
                    diccionario_puntaje = {}
                    diccionario_puntaje["Puntaje"] = self.score_jugador()
                    diccionario_puntaje["Valoracion"] = self.estrellas_dos
                    lista_datos.append(diccionario_puntaje)
                    diccionario["Datos"] = lista_datos

                    json.dump(diccionario,archivo, indent=4)

        elif self.nivel == 3:
            if len(self.jugador.lista_enemigos_muertos) == 1:
                self._slave.blit(imagen_win,(0,0))
                self.estrellas_tres = 3

                lista_datos = []
                diccionario_puntaje = {}
                diccionario_puntaje["Puntaje"] = 1
                diccionario_puntaje["Valoracion"] = self.estrellas_tres
                lista_datos.append(diccionario_puntaje)
                diccionario["Datos"] = lista_datos
                
                with open("Proyecto/APIFORMS/nivel_tres.json",'w') as archivo:
                        json.dump(diccionario,archivo, indent=4)


    def actualizar_pantalla(self):
        self._slave.blit(self.imagen_fondo,(0,0))


        for plataformas in self.plataformas:
            if type(plataformas) == list:
                for plataforma in plataformas:
                    plataforma.draw(self._slave)
            else:
                plataformas.draw(self._slave)

        self.jugador.update(self._slave,self.plataformas, self.plataformas_colision,
                            self.items,self.enemigos, self.trampas)
    
    def score_jugador(self):
        return self.jugador.obtener_score()
    
    def vidas_jugador(self):
        return self.jugador.obtener_vidas()
    
    def valoracion_nivel(self):
        return self.estrellas
    
    def valoracion_nivel_dos(self):
        return self.estrellas_dos
    
    def valoracion_nivel_tres(self):
        return self.estrellas_tres
    
    def nivel_actual(self):
        return self.nivel
    
    def obtener_finalizo_tiempo(self):
        return self.acabo_tiempo
    

    def leer_inputs(self):
        self.segundos = pygame.time.get_ticks()/1000 - 2
        global tecla_up_presionada
        tecla = pygame.key.get_pressed()
        if self.jugador.vidas > 0:
            # self._slave.blit(imagen,(600,0))
            if (tecla[pygame.K_RIGHT] and self.jugador.lados["main"].x < 1200 - self.jugador.velocidad 
                - self.jugador.lados["main"].width and self.jugador.chocado_derecha == False):
                self.jugador.que_hace = "corre derecha"

            elif (tecla[pygame.K_LEFT] and self.jugador.lados["main"].x > 0 + self.jugador.velocidad 
                and self.jugador.chocado_izq == False):
                
                self.jugador.que_hace = "corre izquierda"

            elif tecla[pygame.K_UP] and self.jugador.en_plataforma:
                tecla_up_presionada = True
                if self.jugador.en_plataforma:
                    self.jugador.que_hace = "salta"

            elif tecla[pygame.K_SPACE] and tecla_up_presionada:
                tecla_up_presionada = False
                if self.jugador.en_plataforma == False:
                    self.jugador.que_hace = "doblesalto"

            else:
                self.jugador.que_hace = "quieto"

            if tecla[pygame.K_r]:
                if self.jugador.ejecutar_sonido:
                    self.sonido = pygame.mixer.Sound("Proyecto/APIFORMS/fuego.wav")
                    self.sonido.set_volume(0.1)
                    self.sonido.play()  
                x,y = self.jugador.rect.center
                self.jugador.disparar(x, y)
        else:
            self._slave.blit(imagen_muerte,(0,0))

    def dibujar_rectangulos(self):
        if get_mode() == True:
            for lado in self.jugador.lados:      
                pygame.draw.rect(self._slave, (255,0,0), self.jugador.lados[lado], 2)

            for plataforma in self.plataformas_colision:
                pygame.draw.rect(self._slave, (250,0,0),plataforma,2)

            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, (255,0,0), enemigo.lados[lado], 2)

            for trampa in self.trampas:
                for lado in trampa.lados:
                    pygame.draw.rect(self._slave, (255,0,0), trampa.lados[lado], 2)






