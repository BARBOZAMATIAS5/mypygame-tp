from auxiliar import *
from constantes import *
from player import *


class Coin():
    def __init__(self, x: int, y: int, frame_animation_ms: int,move_rate_ms: int, p_scale= P_SCALE):
        
        self.__idle_coin = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\coin\\animation\shop_item_puff_fx_coin_a_000{0}.png", 1, 9, flip=False, scale= p_scale)
        self.__puff_coin = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\coin\puff\shop_item_coin_puff_fx_000{0}.png", 1, 10, flip=False, scale= 0.2)

        self.__frame = 0

        self.__actual_animation = self.__idle_coin
        self.__image = self.__actual_animation[self.__frame]

        self.__rect = self.__image.get_rect()
        self.__rect.x = x
        self.__rect.y = y

        self.__rect_colision = pygame.Rect(
            x+self.__rect.height/3,
            y,
            (self.__rect.width/3),
            self.__rect.height-15)

        self.__animation_time = 0
        self.__frame_rate_ms = frame_animation_ms

    @property
    def rect_colision_coin(self) -> pygame.Rect:
        '''
        Devuelve las dimensiones de la imagen

        Parametros: -
        
        Retorna la dimension de la imagen, un rectangulo
        '''
        return self.__rect_colision

    def idle(self):
        '''
        Se encarga de la animacion contenida en 'self.__idle_coin'
        
        Parametros: -

        No retorna nada
        '''
        self.__frame = 0
        self.__actual_animation = self.__idle_coin

    def puff(self):
        '''
        Se encarga de la animacion contenida en 'self.__puff_coin'
        
        Parametros: -

        No retorna nada
        '''
        self.__frame = 0
        self.__actual_animation = self.__puff_coin

    def check_take(self, player) -> bool:
        '''
        Chequea si la hitbox de la moneda colisono con la del jugador, devolviendo un bool
        
        Parametro: any (corresponde al atributo que contiene la informacion del jugador)
        
        Retorna un booleano
        '''
        retorno = False
        
        if(self.__rect_colision.colliderect(player.collition_rect)):
            retorno = True
        
        return retorno
    
    def do_animation(self, delta_ms):
        '''
        Se encarga del cambio de frame de la animacion de la moneda

        Parametro: int (corresponde a los frames en que se ejecutará el juego)

        No retorna nada
        '''
        self.__animation_time += delta_ms
        if (self.__animation_time >= self.__frame_rate_ms):
            self.__animation_time = 0
            if(self.__frame < len(self.__actual_animation) - 1):
                self.__frame += 1 
            else: 
                self.__frame = 0

    # def do_movement(self, player):
    #     '''
    #     Delimita la velocidad del movimiento del proyectil y el movimiento en las posiciones 'x' e 'y', usando las los metodos: 
    #     'self.change_x', 'self.change_y'
        
    #     Parametro: int (corresponde a los frames en que se ejecutará el juego)
        
    #     No retorna nada
    #     '''
    #     if self.check_take(player):
    #         self.puff()
            
    def update(self, delta_ms):
        '''
        Actualiza la animacion de la moneda entorno a los FPS del juego.
        
        Parametro: int (corresponde a los frames que se ejecutará el juego)
        
        No retorna nada
        '''
        self.do_animation(delta_ms)

    def draw(self, screen: pygame.Surface):
        '''
        Dibuja en la pantalla del juego al objeto, la moneda. Tambien posibilita que se muestre
        el rectangulo que ocupa, diriase la 'hitbox'
        
        Parametro: surface (corresponde a la clase encargada de la pantalla, de la libreria de pygame)
        
        No retorna nada
        '''
        if DEBUG:
            pygame.draw.rect(screen, color = (255,0,0), rect= self.__rect_colision)
        self.__image = self.__actual_animation[self.__frame]
        screen.blit(self.__image, self.__rect)
    
