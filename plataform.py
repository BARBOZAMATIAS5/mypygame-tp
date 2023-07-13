import pygame
from auxiliar import *
from constantes import *


class Plataform:
    def __init__(self, x, y, path, width, height,  type=1):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(path,1,2,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)