import pygame

personaje_corre_der = [
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/0.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/1.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/2.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/3.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/4.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/5.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/6.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/7.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/8.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/9.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/10.png"),
    pygame.image.load("Imagenes/Ninja Frog/Corriendo/11.png"),
]

def girar_imagen(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

personaje_corre_izq = girar_imagen(personaje_corre_der, True, False)


personaje_quieto = [
    pygame.image.load("Imagenes/Ninja Frog/Quieto/0.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/1.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/2.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/3.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/4.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/5.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/6.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/7.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/8.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/9.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/10.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/11.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/12.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/13.png"),
    pygame.image.load("Imagenes/Ninja Frog/Quieto/14.png"),
]

personaje_quieto_izquierda = girar_imagen(personaje_quieto, True, False)



personaje_salto = [
    pygame.image.load("Imagenes/Ninja Frog/Salto/0.png"),
    pygame.image.load("Imagenes/Ninja Frog/Salto/1.png"),
]

personaje_doble_salto = [
    pygame.image.load("Imagenes/Ninja Frog/DobleSalto/0.png"),
    pygame.image.load("Imagenes/Ninja Frog/DobleSalto/1.png"),
    pygame.image.load("Imagenes/Ninja Frog/DobleSalto/2.png"),
]

personaje_hit = [
    pygame.image.load("Imagenes/Ninja Frog/Hit/0.png"),
    pygame.image.load("Imagenes/Ninja Frog/Hit/1.png"),
    pygame.image.load("Imagenes/Ninja Frog/Hit/2.png"),
    pygame.image.load("Imagenes/Ninja Frog/Hit/3.png"),
    pygame.image.load("Imagenes/Ninja Frog/Hit/4.png"),
    pygame.image.load("Imagenes/Ninja Frog/Hit/5.png"),
    pygame.image.load("Imagenes/Ninja Frog/Hit/6.png"),
     
]

personaje_caida = [
    pygame.image.load("Imagenes/Ninja Frog/Caida/0.png"),
     
]


personaje_salta_izq = girar_imagen(personaje_salto, True, False)
personaje_doble_salto_izq = girar_imagen(personaje_doble_salto,True, False)
personaje_hit_izq = girar_imagen(personaje_hit, True, False)
personaje_caida_izq = girar_imagen(personaje_caida, True, False)



def reescalar_imagenes(lista_animaciones, ancho, alto):
    for lista_imagen in lista_animaciones:
        for i in range(len(lista_imagen)): #-> range len para modificar la original
            imagen = lista_imagen[i]
            lista_imagen[i] = pygame.transform.scale(imagen, (ancho,alto))

def reescalar_animacion(lista_animacion, ancho, alto):
    for i in range(len(lista_animacion)):
        imagen = lista_animacion[i]
        lista_animacion[i] = pygame.transform.scale(imagen, (ancho,alto))

def obtener_rectangulo(principal:pygame.Rect)->dict:
        diccionario = {}
        diccionario['main'] = principal
        diccionario['top'] = pygame.Rect(principal.left, principal.top, principal.width, 9)
        diccionario['bottom'] = pygame.Rect(principal.left, principal.bottom-5, principal.width, 9)
        diccionario['left'] = pygame.Rect(principal.left, principal.top, 6, principal.height)
        diccionario['right'] = pygame.Rect(principal.right-2, principal.top, 6, principal.height)
        return diccionario

icono_fruits = pygame.image.load("Imagenes/Fruits/4.png")
icono_fruits = pygame.transform.scale(icono_fruits, (40,40))

icono_vidas = pygame.image.load("Imagenes/Menu/corazon.png")
icono_vidas = pygame.transform.scale(icono_vidas, (40,40))

fuego = [
     pygame.image.load("Imagenes/Fuego/1.png"),
     pygame.image.load("Imagenes/Fuego/2.png"),
     pygame.image.load("Imagenes/Fuego/3.png"),
     pygame.image.load("Imagenes/Fuego/4.png"),
     pygame.image.load("Imagenes/Fuego/5.png")
]

fuego_izq = girar_imagen(fuego, True, False)

bullet = [
        pygame.image.load("Imagenes/Planta/Bullet.png"),
     
]

poder = [
     pygame.image.load("Imagenes/Bolt/frames/bolt1.png"),
     pygame.image.load("Imagenes/Bolt/frames/bolt2.png"),
     pygame.image.load("Imagenes/Bolt/frames/bolt3.png"),
     pygame.image.load("Imagenes/Bolt/frames/bolt4.png"),
]


bala = [
     pygame.image.load("Imagenes/Planta/Bullet.png")
]