import pygame
import sys
from pygame.locals import *
from APIFORMS.GUI_widget import *
from APIFORMS.GUI_button_image import *
from APIFORMS.GUI_button import *
from APIFORMS.GUI_label import *
from APIFORMS.GUI_slider import *
from APIFORMS.GUI_textbox import *
from APIFORMS.GUI_form import *
from APIFORMS.GUI import *
from APIFORMS.GUI_FormContenedor import *
from APIFORMS.GUI_FormMenu_Niveles import *
from APIFORMS.GUI_picture_box import *
from APIFORMS.GUI_Form_opciones import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        self.imagen = pygame.image.load("Imagenes/Menu/fondooo.png")
        self.superficie_imagen = pygame.transform.scale(self.imagen, (w, h))
        self.volumen = 0.2
        self.flag_play = True


        pygame.mixer.init()


        ### CONTROLES ###
        # self.boton_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "Proyecto/APIFORMS/Menu_BTN.png",self.boton_tabla_click, "juan")
        self.btn_niveles = Button_Image(self._slave,x,y,130,80,250,110,"Imagenes/Menu/Buttons/0.png",self.boton_imagen_click, "niveles")
        self.btn_opciones = Button_Image(self._slave,x,y,130,235,250,110,"Imagenes/Menu/Buttons/menu.png",self.boton_volumen_click, "niveles")
        self.btn_salir = Button_Image(self._slave,x,y,130,400,250,110,"Imagenes/Menu/Buttons/quit.png",self.boton_salir_click, "niveles")


        #Agrego los controlesa la lista###
        # self.lista_widgets.append(self.boton_play)
        # self.lista_widgets.append(self.label_volumen)
        # self.lista_widgets.append(self.slider_volumen)
        # self.lista_widgets.append(self.boton_tabla)
        self.lista_widgets.append(self.btn_niveles)
        self.lista_widgets.append(self.btn_opciones)
        self.lista_widgets.append(self.btn_salir)




        pygame.mixer.music.load("Proyecto/APIFORMS/Vengeance (Loopable).wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)


        self.render()


    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render() #Cada vez que se actualize tengo que volver a dibujar los elementos del formulario
                #Recorrer la lista de widgets para poder dibujarlo
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)


        else:
            self.hijo.update(lista_eventos)
           


    def render(self):
        self._slave.blit(self.superficie_imagen,(0,0))


    def boton_volumen_click(self,text):
        self.formulario_opciones = FormOpciones(self._master,100,25,800,550,"Black","Black",True,"Imagenes/Menu/celeste.png")
        self.show_dialog(self.formulario_opciones)

    def boton_salir_click(self,text):
        try:
            os.remove("Proyecto/APIFORMS/nivel_uno.json")
            os.remove("Proyecto/APIFORMS/nivel_dos.json")
            os.remove("Proyecto/APIFORMS/nivel_tres.json")
        except FileNotFoundError:
                pass

        pygame.quit()
        sys.exit()


    def boton_imagen_click(self,text):
        self.formulario_niveles = FormNiveles(self._master,100,25,800,550,"Black","Black",True,"Proyecto/APIFORMS/contenedor_niveles.png")
        self.show_dialog(self.formulario_niveles)


    # def boton_tabla_click(self, texto):
    #     dict_score = [{"Jugador": "Gio"," Score": 1000}]


    #     form_puntaje = FormMenuScore(self._master,250,25,500, 550, (220,0,220),"White", True, "Proyecto/APIFORMS/Window.png",dict_score,100,10,10)


    #     self.show_dialog(form_puntaje)







