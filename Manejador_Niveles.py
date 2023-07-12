from pygame.locals import *
from NivelUno import *
from NivelDos import *
from NivelTres import *



class Manejador_Niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla

        self.niveles = {"nivel_uno":NivelUno , "nivel_dos":NivelDos, "nivel_tres":NivelTres}


    def get_nivel(self, nombre_nivel):

        return self.niveles[nombre_nivel](self._slave)
    
    


    





