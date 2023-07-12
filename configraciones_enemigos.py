import pygame
from configuraciones import *

desaparecer_enemigo_caracol = [
    pygame.image.load("Imagenes/Snail/Desaparecer/0.png"),
    pygame.image.load("Imagenes/Snail/Desaparecer/1.png"),
    pygame.image.load("Imagenes/Snail/Desaparecer/2.png"),
    pygame.image.load("Imagenes/Snail/Desaparecer/3.png"),
    pygame.image.load("Imagenes/Snail/Desaparecer/4.png"),
    
]

enemigo_caracol_camina = [
    pygame.image.load("Imagenes/Snail/Caminar/0.png"),
    pygame.image.load("Imagenes/Snail/Caminar/1.png"),
    pygame.image.load("Imagenes/Snail/Caminar/3.png"),
    pygame.image.load("Imagenes/Snail/Caminar/4.png"),
    pygame.image.load("Imagenes/Snail/Caminar/5.png"),
    pygame.image.load("Imagenes/Snail/Caminar/6.png"),
    pygame.image.load("Imagenes/Snail/Caminar/7.png"),
    pygame.image.load("Imagenes/Snail/Caminar/8.png"),
]

enemigo_caracol_hit = [
    pygame.image.load("Imagenes/Snail/Hit/0.png"),
    pygame.image.load("Imagenes/Snail/Hit/1.png"),
    pygame.image.load("Imagenes/Snail/Hit/2.png"),
    pygame.image.load("Imagenes/Snail/Hit/3.png"),
    pygame.image.load("Imagenes/Snail/Hit/4.png"),
     
]
desaparecer_enemigo_caracol_izq = girar_imagen(desaparecer_enemigo_caracol, True, False)
enemigo_caracol_camina_izq = girar_imagen(enemigo_caracol_camina,True,False)
enemigo_caracol_hit_izq = girar_imagen(enemigo_caracol_hit,True,False)

lista_animaciones_caracol = [enemigo_caracol_camina,enemigo_caracol_camina_izq,enemigo_caracol_hit
                             ,enemigo_caracol_hit_izq]

enemigo_trunk_camina = [
    pygame.image.load("Imagenes/Trunk/Caminar/0.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/1.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/2.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/3.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/4.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/5.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/6.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/7.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/8.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/9.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/10.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/11.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/12.png"),
    pygame.image.load("Imagenes/Trunk/Caminar/13.png"),
]

desaparecer_enemigo_trunk = [
    pygame.image.load("Imagenes/Trunk/Hit/0.png"),
    pygame.image.load("Imagenes/Trunk/Hit/1.png"),
    pygame.image.load("Imagenes/Trunk/Hit/2.png"),
    pygame.image.load("Imagenes/Trunk/Hit/3.png"),
    pygame.image.load("Imagenes/Trunk/Hit/4.png"),
]

ataque_planta = [
    pygame.image.load("Imagenes/Planta/Ataque/0.png"),
    pygame.image.load("Imagenes/Planta/Ataque/1.png"),
    pygame.image.load("Imagenes/Planta/Ataque/2.png"),
    pygame.image.load("Imagenes/Planta/Ataque/3.png"),
    pygame.image.load("Imagenes/Planta/Ataque/4.png"),
    pygame.image.load("Imagenes/Planta/Ataque/5.png"),
]


planta_hit = [
    pygame.image.load("Imagenes/Planta/Hit/0.png"),
    pygame.image.load("Imagenes/Planta/Hit/1.png"),
    pygame.image.load("Imagenes/Planta/Hit/2.png"),
    pygame.image.load("Imagenes/Planta/Hit/3.png"),
    pygame.image.load("Imagenes/Planta/Hit/4.png"),

]

enemigo_trunk_camina_izq = girar_imagen(enemigo_trunk_camina, True, False)
desaparecer_enemigo_trunk_izq = girar_imagen(desaparecer_enemigo_trunk, True, False)

lista_animaciones_trunk = [enemigo_trunk_camina, enemigo_trunk_camina_izq, desaparecer_enemigo_trunk
                           , desaparecer_enemigo_trunk_izq]

lista_animaciones_planta = [ planta_hit, ataque_planta]


enemigo_pajaro = [
    pygame.image.load("Imagenes/Pajaro/0.png"),
    pygame.image.load("Imagenes/Pajaro/1.png"),
    pygame.image.load("Imagenes/Pajaro/2.png"),
    pygame.image.load("Imagenes/Pajaro/3.png"),
    pygame.image.load("Imagenes/Pajaro/4.png"),
    pygame.image.load("Imagenes/Pajaro/5.png")
]

disparo_pajaro = [
    pygame.image.load("Imagenes/Bala/0.png"),
    pygame.image.load("Imagenes/Bala/1.png"),
    pygame.image.load("Imagenes/Bala/2.png"),
]

pig = [
    pygame.image.load("Imagenes/Pig/0.png"),
    pygame.image.load("Imagenes/Pig/1.png"),
    pygame.image.load("Imagenes/Pig/2.png"),
    pygame.image.load("Imagenes/Pig/3.png"),
    pygame.image.load("Imagenes/Pig/4.png"),
    pygame.image.load("Imagenes/Pig/5.png"),
    pygame.image.load("Imagenes/Pig/6.png"),
    pygame.image.load("Imagenes/Pig/7.png"),
    pygame.image.load("Imagenes/Pig/8.png"),
]

pig_die = [
    pygame.image.load("Imagenes/Pig/Die/0.png"),
    pygame.image.load("Imagenes/Pig/Die/1.png"),
    pygame.image.load("Imagenes/Pig/Die/2.png"),
]
