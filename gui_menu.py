import pygame
from boton import Boton


start_image = pygame.image.load("assets\menu\start.png").convert_alpha()
# options_image = pygame.image.load("assets\menu\start.png").convert_alpha()
exit_image = pygame.image.load("assets\menu\exit.png").convert_alpha()

class Menu():
    def __init__(self):
        start_boton = Boton(x=50, y=120, image=start_image,scale= 1)
        exit_boton = Boton(x=50, y=120, image=exit_image,scale= 1)
