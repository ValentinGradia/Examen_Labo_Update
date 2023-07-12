from Plataforma import Plataforma
from Objeto import Objeto


plataformas = Plataforma(0,600,150,150,"Imagenes/Terrain/Terrain/1.png")
plataformas.crear_superficies_x(8)

superficie_piso = Objeto(0,600,1200,150,"Imagenes/Boxes/Box1/Idle.png")

plataforma_colision_trampa2 = Objeto(750,550,40,40,"Imagenes/Terrain/Terrain/1.png")

plataforma_flotante111 = Plataforma(200,500,120,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante222 = Plataforma(500,500,120,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante333 = Plataforma(350,430,120,12,"Imagenes/Terrain/Terrain/4.png")
plataforma_flotante444 = Plataforma(250,330,70,12,"Imagenes/Terrain/Terrain/4.png")
