import pygame
from background import Background
from constantes import *
import boton

class Boton_Menu(Background):
    def __init__(self, x, y, widht, height, path):
        super().__init__(x, y, widht, height, path)

        self.__background_options = Background(x,y,widht, height, path="assets\menu\menu_options_def.png")
        self.__background_pause = Background(x=1280/2 - 216, y=720/2 - 128, widht=432, height=253, path="assets\menu\menu_options.png")
        self.__start_boton = boton.Boton(x=500, y=280, image=pygame.image.load("assets\menu\\boton_empezar.png").convert_alpha(), scale=P_SCALE)
        self.__exit_boton = boton.Boton(x=530, y=400, image=pygame.image.load("assets\menu\\boton_salir.png").convert_alpha(), scale=P_SCALE)
        self.__option_boton = boton.Boton(x=500, y=340, image=pygame.image.load("assets\menu\\boton_opciones.png").convert_alpha(), scale=P_SCALE)

        self.__back_boton = boton.Boton(x=1100, y=640, image=pygame.image.load("assets\menu\\boton_volver.png").convert_alpha(), scale=P_SCALE)
        self.__audio_boton = boton.Boton(x=560, y=290, image=pygame.image.load("assets\menu\\boton_sonido.png").convert_alpha(), scale=P_SCALE)
        self.__reintentar_boton = boton.Boton(x=560, y=280, image=pygame.image.load("assets\menu\\boton_reintentar.png").convert_alpha(), scale=P_SCALE)
        self.__back_menu_boton = boton.Boton(x=500, y=400, image=pygame.image.load("assets\menu\\boton_volver_al_menu.png").convert_alpha(), scale=P_SCALE)

        self.__world_1 =boton.Boton(x=500, y=240, image=pygame.image.load("assets\hud\world_01.png").convert_alpha(), scale=P_SCALE)
        self.__world_2 =boton.Boton(x=500, y=340, image=pygame.image.load("assets\hud\world_02.png").convert_alpha(), scale=P_SCALE)
        self.__world_3 =boton.Boton(x=500, y=440, image=pygame.image.load("assets\hud\world_03.png").convert_alpha(), scale=P_SCALE)

        self.__scoreboard_boton = boton.Boton(x=510, y=400, image=pygame.image.load("assets\menu\\boton_scoreboard.png").convert_alpha(), scale=P_SCALE)

    def start(self, screen) -> str:
        
        if self.__start_boton.draw(screen):
            return True

    def exit(self, screen):

        if self.__exit_boton.draw(screen):
            return True

    def options(self, screen):
        
        if self.__option_boton.draw(screen):
            return True

    def back(self, screen):

        if self.__back_boton.draw(screen):
            return True

    def sound(self, screen):

        if self.__audio_boton.draw(screen):
            return True
    
    def scoreboard(self, screen):

        if self.__scoreboard_boton.draw(screen):
            return True
    
    def retry(self, screen):
        if self.__reintentar_boton.draw(screen):
            return True
    
    def back_menu(self, screen):
        if self.__back_menu_boton.draw(screen):
            return True
    
    def world_01(self, screen):

        if self.__world_1.draw(screen):
            return True
    
    def world_02(self, screen):

        if self.__world_2.draw(screen):
            return True
    
    def world_03(self, screen):

        if self.__world_3.draw(screen):
            return True
        
    def background_menu(self, screen):
        super().draw(screen)

    def backgroud_options(self, screen):
        self.__background_options.draw(screen)

    def backgroud_pause(self, screen):
        self.__background_pause.draw(screen)
    
        
