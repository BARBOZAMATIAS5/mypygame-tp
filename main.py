import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from levels import LevelGame
from menu_botons import *
from funciones import *

pygame.init()
pygame.display.set_caption('Cuphead: Las últimas monedas.')

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), DOUBLEBUF, 16)

menu_game = Boton_Menu(x=0, y=0, widht=ANCHO_VENTANA,
                             height=ALTO_VENTANA,path="assets\menu\\background_menu.png")

level_01= False
level_02= False
level_03= False

active_game = False

clock = pygame.time.Clock()

def main_menu_game(on_off):
    on_off = True
    while on_off:

        lista_eventos = pygame.event.get()

        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        menu_game.background_menu(screen)
        if menu_game.exit(screen):
            pygame.quit()
            sys.exit()

        if menu_game.options(screen):
            options_game(True)

        if menu_game.start(screen):
            start_game_init(True, True, "level_03")

        pygame.display.flip()
        pygame.display.update()

def start_game_init(on_off, active_game, level_now):

    form_game = LevelGame(name="cuphead_game", master_surface=screen, x=0, y=0,
                        w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, color_border=None, active=active_game, level= level_now)
    
    pause_game = False

    while on_off:
        
        lista_eventos = pygame.event.get()

        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_game = not pause_game

        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        
        if pause_game:
            menu_game.backgroud_pause(screen)
            if menu_game.retry(screen):
                active_game = False
                start_game_init(True,True, level_now)
                
            if menu_game.back_menu(screen):
                active_game = False
                main_menu_game(True)

        else:
            aux_form_active = form_game.get_active()
            if (aux_form_active != None):
                aux_form_active.update(keys, delta_ms)
                aux_form_active.draw()

        pygame.display.flip()
        pygame.display.update()


def options_game(on_off):
    menu = "option"
    while on_off:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if menu == "option":
            menu_game.backgroud_options(screen)
            if menu_game.sound(screen):
                print("AUDIO")

            if menu_game.scoreboard(screen):
                menu = "scoreboard"

            if menu_game.back(screen):
                main_menu_game(True)
                
        if menu == "scoreboard":
            menu_game.background_menu(screen)
            if menu_game.back(screen):
                menu = "option"

        pygame.display.flip()
        pygame.display.update()


def init_game():
    
    while True:
        main_menu_game(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        pygame.display.flip()
        pygame.display.update()

init_game()