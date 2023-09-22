import pygame
from background import Background
from constantes import *
import boton

class Main_Menu(Background):
    def __init__(self, x, y, widht, height, path):
        super().__init__(x, y, widht, height, path)

        self.__background_options = Background(x,y,widht, height, path="assets\menu\menu_options_def.png")
        self.__start_boton = boton.Boton(x=500, y=280, image=pygame.image.load("assets\menu\\boton_start.png").convert_alpha(), scale=P_SCALE)
        self.__exit_boton = boton.Boton(x=530, y=400, image=pygame.image.load("assets\menu\\boton_salir.png").convert_alpha(), scale=P_SCALE)
        self.__option_boton = boton.Boton(x=500, y=340, image=pygame.image.load("assets\menu\\boton_opciones.png").convert_alpha(), scale=P_SCALE)
        
        self.__back_boton = boton.Boton(x=1100, y=600, image=pygame.image.load("assets\menu\\boton_volver.png").convert_alpha(), scale=P_SCALE)
        self.__audio_boton = boton.Boton(x=600, y=300, image=pygame.image.load("assets\menu\\boton_sonido.png").convert_alpha(), scale=P_SCALE)
        
        self.__scoreboard_boton = boton.Boton(x=550, y=500, image=pygame.image.load("assets\menu\\boton_scoreboard.png").convert_alpha(), scale=P_SCALE)

        self.__estado = "menu"
        self.__retorno = False

    def draw(self, screen) -> str:
        
        if self.__estado == "menu":
            super().draw(screen)
            if self.__start_boton.draw(screen):
                self.__retorno = True
                return self.__retorno
            if self.__exit_boton.draw(screen):
                return self.__retorno
            if self.__option_boton.draw(screen):
                self.__estado = "opciones"

        if self.__estado == "opciones":
            self.__background_options.draw(screen)
            if self.__audio_boton.draw(screen):
                print("AUDIO")
            if self.__back_boton.draw(screen):
                self.__estado = "menu"
            if self.__scoreboard_boton.draw(screen):
                self.__estado = "scoreboard"
        
        if self.__estado == "scoreboard":
            super().draw(screen)
            if self.__back_boton.draw(screen):
                self.__estado = "opciones"

            

        
