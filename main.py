import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from level_1 import LevelGame1

flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()


form_game_l1= LevelGame1(name="form_game_l1", master_surface= screen, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=None,color_border=None,active=True)

while True:

    clock = pygame.time.Clock()

    lista_eventos =pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys= pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if (aux_form_active != None):
        aux_form_active.update(lista_eventos, keys, delta_ms)
        aux_form_active.draw()

    pygame.display.flip()
