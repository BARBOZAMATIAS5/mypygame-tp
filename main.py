import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from level_1 import LevelGame1
from level_2 import LevelGame2
from level_3 import LevelGame3
from background import Background
from main_menu import *
import boton
pygame.init()
pygame.display.set_caption('Cuphead: Las últimas monedas.')
flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)

form_game_l3 = LevelGame3(name="form_game_l3", master_surface=screen, x=0, y=0,
                          w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, color_border=None, active=True)

menu_game = Main_Menu(x=0, y=0, widht=ANCHO_VENTANA,
                             height=ALTO_VENTANA, path="assets\menu\\background_menu.png")

clock = pygame.time.Clock()

run = True
start_game = False

while run:

    lista_eventos = pygame.event.get()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    
    if start_game == False:

        if menu_game.draw(screen):
            start_game = True

        if menu_game.draw(screen) == False:
            run = menu_game.draw(screen)

    else:
        aux_form_active = Form.get_active()
        if (aux_form_active != None):
            aux_form_active.update(lista_eventos, keys, delta_ms)
            aux_form_active.draw()

    pygame.display.flip()
