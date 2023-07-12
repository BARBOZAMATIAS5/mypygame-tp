from auxiliar import *
from constantes import *
from player import *


class Coin:
    def __init__(self, x: int, y: int, frame_animation_ms: int,move_rate_ms: int, p_scale= P_SCALE):
        
        self.__idle_coin = Auxiliar.getSurfaceFromSeparateFiles("assets\coin\\animation\shop_item_puff_fx_coin_a_000{0}.png", 1, 9, flip=False, scale= p_scale)
        self.__puff_coin = Auxiliar.getSurfaceFromSeparateFiles("assets\coin\puff\shop_item_coin_puff_fx_000{0}.png", 1, 10, flip=False, scale= p_scale)

        self.__frame = 0
        self.__move_x = 0
        self.__move_y = 0

        self.__actual_animation = self.__idle_coin
        self.__image = self.__actual_animation[self.__frame]
        
        self.__rect = self.__image.get_rect()
        self.__rect.x = x
        self.__rect.y = y

        self.__rect_colision = pygame.Rect(
            x+self.__rect.height/3,
            y,
            self.__rect.width/3,
            self.__rect.height)

        self.__tiempo_transcurrido_animacion = 0
        self.__tiempo_transcurrido_move = 0
        self.__frame_rate_ms = frame_animation_ms
        self.__move_rate_ms = move_rate_ms


    @property
    def rect_colision_enemy(self):
        '''
        
        
        
        '''
        return self.__rect_colision
#la llamo de esta forma y es necesario introducir un parametro
    def get_rect_colision(self) -> pygame.Rect:
        return self.__rect_colision
    

    def idle(self):
        '''
        
        
        
        '''
        self.__frame = 0
        self.__actual_animation = self.__idle_coin

    def gotcha(self,):
        '''
            
            
            
        '''
        self.__frame = 0
        self.__actual_animation = self.__puff_coin
    
    def do_movement(self, delta_ms, player):
        '''
        
        
        
        '''
        self.__tiempo_transcurrido_move += delta_ms
        if (self.__tiempo_transcurrido_move >= self.__frame_rate_ms):
            self.__tiempo_transcurrido_move = 0

            if self.__rect_colision == Player.get_rect_colision(player):
                self.gotcha()
    

    def do_animation(self, delta_ms):
        '''



        '''
        self.__tiempo_transcurrido_animacion += delta_ms
        if (self.__tiempo_transcurrido_animacion >= self.__frame_rate_ms):
            self.__tiempo_transcurrido_animacion = 0
            if(self.__frame < len(self.__actual_animation) - 1):
                self.__frame += 1 
            else: 
                self.__frame = 0
    
    def update(self, delta_ms, player):
        self.do_movement(delta_ms, player)
        self.do_animation(delta_ms)

    def draw(self, screen: pygame.Surface):
        ''''
        
        
        
        '''
        if DEBUG:
            pygame.draw.rect(screen, color = (255,0,0), rect= self.__rect_colision)
        self.__image = self.__actual_animation[self.__frame]
        screen.blit(self.__image, self.__rect)
    
