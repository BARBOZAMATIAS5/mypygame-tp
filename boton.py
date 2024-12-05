import pygame

class Boton:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int (height* scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        '''
        Dibuja en la pantalla una imagen la cual, cada vez que se haga click en la misma, retornará
        el booleano 'True', cada vez que no se haga click, retornará el booleano 'False'

        Parametros: surface (corresponde a la configuracion de resolucion de pygame)
        
        Retorna un booleano.
        '''
        action = False

        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image,(self.rect.x, self.rect.y))

        return action