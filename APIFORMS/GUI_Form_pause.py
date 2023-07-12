import pygame
from pygame.locals import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_picture_box import *
from constantes import *

class FormPausa(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, contenedor_nivel=None):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.pantalla = aux_image
        self.contenedor_nivel = contenedor_nivel


        self.pausa = PictureBox(self._slave, 100,100,350,100,"Imagenes/Menu/Buttons/pause.png")
        self.btn_home = Button_Image(screen=self._slave,
                                      master_x=self._x,
                                      master_y=self._y,
                                      x= 350,
                                      y=250,
                                      w=150,
                                      h=150,
                                      path_image="Imagenes/Menu/Buttons/Play.png",
                                      onclick=self.btn_home_click,
                                      onclick_param="",
                                      text="",
                                      font="Arial",
                                      )
        



        
        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.pausa)
        
        
    def update(self,lista_eventos):
            if self.verificar_dialog_result():
                if self.active:
                    self.draw()
                    self.render()
                    for widget in self.lista_widgets:
                        widget.update(lista_eventos)
            else:
                self.hijo.update(lista_eventos)

    def render(self):
        self._slave.blit(imagen_fondo,(0,0))

    
    def btn_home_click(self,param):
        if self.contenedor_nivel != None:
            self.contenedor_nivel.settings = False
            self.end_dialog()
             
        self.end_dialog()