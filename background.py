import pygame
from constantes import *

class Background():
    def __init__(self, x, y, widht, height, path):
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(widht, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect= pygame.Rect(x+self.rect.width,y,self.rect.width,self.rect.height)

    def draw(self, screen):
        '''
        Dibuja en la pantalla el escenario de fondo del nivel

        Parametros: surface (corresponde a la configuracion de resolucion de pygame)
        
        No retorna nada
        '''
        screen.blit(self.image, self.rect)
        if (DEBUG):
            pygame.draw.rect(screen,color=(255,0,0), rect=self.collition_rect)