import pygame
from pygame.locals import *
import time

from APIFORMS.GUI_form import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_Form_opciones import *
from APIFORMS.GUI_picture_box import *
from APIFORMS.GUI_Form_pause import *

class FormContenedorNivel(Form):
    def __init__(self,pantalla:pygame.Surface,nivel):
        super().__init__(pantalla,0,0,pantalla.get_width(),pantalla.get_height(),"White")
        self.pantalla = pantalla
        nivel._slave = self._slave
        self.nivel = nivel
        self.sonido = True
        self.settings = False
        self.estrellas_nivel_uno = 0
        self.estrellas_nivel_dos = 0
        self.estrellas_nivel_tres = 0
        
        self.btn_home = Button_Image(screen=self._slave,
                                          master_x= self._x,
                                          master_y= self._y,
                                          x = self._w-100,
                                          y =self._h-100,
                                          w = 100,
                                          h = 100,
                                          path_image="Proyecto/APIFORMS/home.png",
                                          onclick= self.btn_home_click,
                                          onclick_param="",
                                          text="Home",
                                          font="Arial",
                                          )
        
        self.btn_opciones = Button_Image(screen=self._slave,
                                          master_x= self._x,
                                          master_y= self._y,
                                          x = self._w-300,
                                          y =self._h-100,
                                          w = 100,
                                          h = 100,
                                          path_image="Imagenes/Menu/Buttons/Settings.png",
                                          onclick= self.btn_opciones_click,
                                          onclick_param="",
                                          text="",
                                          font="Arial",
                                          )
        

        self.btn_pausa = Button_Image(screen=self._slave,
                                          master_x= self._x,
                                          master_y= self._y,
                                          x = self._w-500,
                                          y =self._h-100,
                                          w = 100,
                                          h = 100,
                                          path_image="Imagenes/Menu/Icon_Clock.png",
                                          onclick= self.btn_pause_click,
                                          onclick_param="",
                                          text="",
                                          font="Arial",
                                          )
        
        self.btn_mute = Button_Image(screen=self._slave,
                                          master_x= self._x,
                                          master_y= self._y,
                                          x = self._w-700,
                                          y =self._h-100,
                                          w = 100,
                                          h = 100,
                                          path_image="Imagenes/Menu/Icon_MusicOn.png",
                                          onclick= self.btn_mute_click,
                                          onclick_param="",
                                          text="",
                                          font="Arial",
                                          )
        

        
        
        
        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.btn_opciones)
        self.lista_widgets.append(self.btn_pausa)
        self.lista_widgets.append(self.btn_mute)


        
        
    def update(self, lista_eventos):
        
        if self.settings == False:
            self.nivel.update(lista_eventos)
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            if self.verificar_dialog_result():
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
            else:
                self.hijo.update(lista_eventos)

        self.verificar_valoracion()
        self.verificar_tiempo()

    

    def verificar_tiempo(self):
        if self.nivel.obtener_finalizo_tiempo():
            self.end_dialog()

    def verificar_valoracion(self):
        if self.nivel.nivel_actual() == 1:

            if os.path.exists("Proyecto/APIFORMS/nivel_uno.json"):

                if self.nivel.valoracion_nivel() == 1:
                    self.estrellas_nivel_uno = 1

                elif self.nivel.valoracion_nivel() == 2:

                    self.estrellas_nivel_uno = 2
                elif self.nivel.valoracion_nivel() == 3:

                    self.estrellas_nivel_uno = 3
        elif self.nivel.nivel_actual() == 2:

            if os.path.exists("Proyecto/APIFORMS/nivel_dos.json"):

                if self.nivel.valoracion_nivel_dos() == 1:
                    self.estrellas_nivel_dos = 1

                elif self.nivel.valoracion_nivel_dos() == 2:
                    self.estrellas_nivel_dos = 2

                elif self.nivel.valoracion_nivel_dos() == 3:

                    self.estrellas_nivel_dos = 3

        elif self.nivel.nivel_actual() == 3:

            if os.path.exists("Proyecto/APIFORMS/nivel_tres.json"):

                if self.nivel.valoracion_nivel_tres() == 3:
                    self.estrellas_nivel_tres = 3


    def obtener_estrellas_nivel_uno(self):
        return self.estrellas_nivel_uno
    
    def obtener_estrellas_nivel_dos(self):
        return self.estrellas_nivel_dos
    
    def obtener_estrellas_nivel_tres(self):
        return self.estrellas_nivel_tres

    def btn_opciones_click(self, text):
        formulario_opciones = FormOpciones(self._master,100, 25, 800, 550,"Black","Black",True,"Imagenes/Menu/celeste.png",self)
        self.settings = True
        self.show_dialog(formulario_opciones)

    def btn_pause_click(self,text):
        formulario_pausa = FormPausa(self._master,200,80,650,450,"Black","Black",True,"Imagenes/Menu/fondooo.png",self)
        self.settings = True
        self.show_dialog(formulario_pausa)

    def btn_mute_click(self,text):
        if self.sonido:
            imagen = pygame.image.load("Imagenes/Menu/Icon_MusicOff.png")
            imagen = pygame.transform.scale(imagen, (100,100)) 
            self.btn_mute._slave = imagen
        else:
            imagen = pygame.image.load("Imagenes/Menu/Icon_MusicOn.png")
            imagen = pygame.transform.scale(imagen, (100,100)) 
            self.btn_mute._slave = imagen

        self.sonido = not self.sonido
        self.nivel.jugador.ejecutar_sonido = not self.nivel.jugador.ejecutar_sonido

    def btn_home_click(self,param):
        self.end_dialog()
