import pygame
from pygame.locals import *
import os

from APIFORMS.GUI_form import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_slider import *
from APIFORMS.GUI_checkbox import *
flag = False

class FormOpciones(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, contenedor_nivel=None):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.pantalla = aux_image
        self.volumen = 0.2
        self.flag_play = True
        self.contenedor_nivel = contenedor_nivel


        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "20%","Comic Sans",15,"White","Proyecto/APIFORMS/Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200,500,15,self.volumen,"Blue","White")
        self.boton_mute = Button_Image(self._slave,x,y,300,60,200,100,"Imagenes/Menu/Buttons/Play.png",self.btn_play_click, "hola")
        self.btn_home = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 300,
                                          y =300,
                                          w = 100,
                                          h = 100,
                                          path_image="Imagenes/Menu/Buttons/Settings.png",
                                          onclick= self.btn_home_click,
                                          onclick_param="",
                                          text="",
                                          font="Arial",
                                          )
        
        
        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.boton_mute)
        

    def btn_play_click(self, texto):
            if self.flag_play:
                pygame.mixer.music.pause()
                imagen = pygame.image.load("Imagenes/Menu/Buttons/Volume.png")
                imagen = pygame.transform.scale(imagen, (200,100))                
                self.boton_mute._slave = imagen
            else:
                pygame.mixer.music.unpause()
                imagen = pygame.image.load("Imagenes/Menu/Buttons/Play.png")
                imagen = pygame.transform.scale(imagen, (200,100))
                self.boton_mute._slave = imagen

                    
            self.flag_play = not self.flag_play


    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen) 

    # def get_volumen(self):
    #     return self.slider_volumen.value
        
        
    def update(self,lista_eventos):
            if self.verificar_dialog_result():
                if self.active:
                    self.draw()
                    self.render()
                    for widget in self.lista_widgets:
                        widget.update(lista_eventos)
                        self.update_volumen(lista_eventos)
            else:
                self.hijo.update(lista_eventos)

    def render(self):
        self._slave.blit(self.pantalla,(0,0))

    def btn_home_click(self,param):
        if self.contenedor_nivel != None:
            self.contenedor_nivel.settings = False
            self.end_dialog()
             
        self.end_dialog()