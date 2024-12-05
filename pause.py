import pygame
from menu_botons import *

class Pause():
    def __init__(self):

        self.__menu = Background(x=460, y=220, widht=432, height=253, path="assets\menu\menu_options.png")
        
    def backgroud_pause_draw(self, screen):
        self.__menu.draw(screen)