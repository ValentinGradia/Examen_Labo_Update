import pygame
from pygame.locals import *
import os

from APIFORMS.GUI_form import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_label import *
from Manejador_Niveles import Manejador_Niveles
from APIFORMS.GUI_FormContenedor import FormContenedorNivel
from APIFORMS.GUI_picture_box import *

flag_nivel_uno = False
flag_nivel_dos = False
flag_nivel_tres = False

class FormNiveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_Niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self.valoracion_nivel_uno = 0
        self.valoracion_nivel_dos = 0
        self.valoracion_nivel_tres = 0

        
        self.btn_nivel_uno = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 100,
                                          y =120,
                                          w = 100,
                                          h = 100,
                                          path_image="Imagenes/Menu/Levels/01.png",
                                          onclick= self.entrar_nivel,
                                          onclick_param="nivel_uno",
                                          text="",
                                          font="Arial")
        
        self.btn_nivel_dos = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 300,
                                          y =120,
                                          w = 100,
                                          h = 100,
                                          path_image="Imagenes/Menu/Levels/02.png",
                                          onclick= self.entrar_nivel,
                                          onclick_param="nivel_dos",
                                          text="",
                                          font="Arial")

        self.btn_nivel_tres = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 500,
                                          y =120,
                                          w = 100,
                                          h = 100,
                                          color_background=(255,0,0),
                                          color_border=(255,0,255),
                                          path_image="Imagenes/Menu/Levels/03.png",
                                          onclick= self.entrar_nivel,
                                          onclick_param="nivel_tres",
                                          text="",
                                          font="Arial",
                                          font_size= 15,
                                          font_color=(0,255,0))

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
        
        self.estrella_1_1 = PictureBox(screen=self._slave,
                                       x=20,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_1_2 = PictureBox(screen=self._slave,
                                       x=90,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_1_3 = PictureBox(screen=self._slave,
                                       x=160,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_2_1 = PictureBox(screen=self._slave,
                                       x=250,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_2_2 = PictureBox(screen=self._slave,
                                       x=320,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_2_3 = PictureBox(screen=self._slave,
                                       x=390,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_3_1 = PictureBox(screen=self._slave,
                                       x=480,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_3_2 = PictureBox(screen=self._slave,
                                       x=550,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")
        
        self.estrella_3_3 = PictureBox(screen=self._slave,
                                       x=620,
                                       y=240,
                                       w=60,
                                       h=60,
                                       path_image="Imagenes/Menu/Icon_Star.png")


        
        
        self.lista_widgets.append(self.btn_nivel_uno)
        self.lista_widgets.append(self.btn_nivel_dos)
        self.lista_widgets.append(self.btn_nivel_tres)
        self.lista_widgets.append(self.btn_home)

        
    def on(self,parametro):
        print("hola",parametro)
        
    def update(self, lista_eventos):
        global flag_nivel_dos,flag_nivel_tres
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.verificar_valoracion_nivel_uno()
            if flag_nivel_dos:
                self.verificar_valoracion_nivel_dos()
            if flag_nivel_tres:
                self.verificar_valoracion_nivel_tres()
            self.hijo.update(lista_eventos)

            if self.valoracion_nivel_uno == 3:

                self.lista_widgets.append(self.estrella_1_1)
                self.lista_widgets.append(self.estrella_1_2)
                self.lista_widgets.append(self.estrella_1_3)

            elif self.valoracion_nivel_uno == 2:

                self.lista_widgets.append(self.estrella_1_1)
                self.lista_widgets.append(self.estrella_1_2)

            elif self.valoracion_nivel_uno == 1:

                self.lista_widgets.append(self.estrella_1_1)

            match self.valoracion_nivel_dos:
                case 1:
                    self.lista_widgets.append(self.estrella_2_1)

                case 2:
                    self.lista_widgets.append(self.estrella_2_1)
                    self.lista_widgets.append(self.estrella_2_2)

                case 3:
                    self.lista_widgets.append(self.estrella_2_1)
                    self.lista_widgets.append(self.estrella_2_2)
                    self.lista_widgets.append(self.estrella_2_3)

            if self.valoracion_nivel_tres == 3:
                self.lista_widgets.append(self.estrella_3_1)
                self.lista_widgets.append(self.estrella_3_2)
                self.lista_widgets.append(self.estrella_3_3)

                          
    
    def entrar_nivel(self,nombre_nivel):
        match nombre_nivel:
            case "nivel_uno":
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                self.form_contenedor_nivel_uno = FormContenedorNivel(self._master,nivel)
                self.show_dialog(self.form_contenedor_nivel_uno)
            case "nivel_dos":
                if os.path.exists("Proyecto/APIFORMS/nivel_uno.json"):
                    global flag_nivel_dos
                    flag_nivel_dos = True
                    nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                    self.form_contenedor_nivel_dos = FormContenedorNivel(self._master,nivel)
                    self.show_dialog(self.form_contenedor_nivel_dos)
                else:
                    print("Debes completar el nivel uno")
            case "nivel_tres":
                if os.path.exists("Proyecto/APIFORMS/nivel_dos.json"):
                    global flag_nivel_tres
                    flag_nivel_tres = True
                    nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                    self.form_contenedor_nivel_tres = FormContenedorNivel(self._master,nivel)
                    self.show_dialog(self.form_contenedor_nivel_tres)
                else:
                    print("Debes completar el nivel dos")

    def verificar_valoracion_nivel_uno(self):
        self.valoracion_nivel_uno = self.form_contenedor_nivel_uno.obtener_estrellas_nivel_uno()
        
    def verificar_valoracion_nivel_dos(self):
        self.valoracion_nivel_dos = self.form_contenedor_nivel_dos.obtener_estrellas_nivel_dos()

    def verificar_valoracion_nivel_tres(self):
        self.valoracion_nivel_tres = self.form_contenedor_nivel_tres.obtener_estrellas_nivel_tres()


    
    def btn_home_click(self,param):
        self.end_dialog()