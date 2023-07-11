from player import *
from auxiliar import Auxiliar
from constantes import *

class Bullet:
    def __init__(self, x_init: int, y_init: int, frame_rate_ms: int, move_rate_ms: int, velocity_x: float, p_scale: float, direction: int) -> None:

        self.__bullet_r = Auxiliar.getSurfaceFromSeparateFiles("assets_2\cuphead\\bullet\peashooter_0{0}.png", 1, 13, False, scale=p_scale)
        self.__bullet_l = Auxiliar.getSurfaceFromSeparateFiles("assets_2\cuphead\\bullet\peashooter_0{0}.png", 1, 13, True, scale=p_scale)

        self.__frame_actual = 0
        self.__direction = direction
        self.__actual_animation = self.__bullet_r
        self.__actual_image = self.__actual_animation[self.__frame_actual]
        self.__rect_bullet = self.__actual_image.get_rect()
        self.__rect_bullet.center = (x_init,y_init)
        self.__bullet_velocity_x = velocity_x

        self.__move_x = 0
        self.__move_y = 0
        self.__collition_rect = pygame.Rect(self.__rect_bullet)

        self.__animation_time = 0
        self.__frame_rate_ms = frame_rate_ms
        self.__movement_time = 0
        self.__move_rate_ms = move_rate_ms
    
    @property
    def rect_colision_bullet(self) -> pygame.Rect:
        return self.__colision_rect
    
    def move_bullet(self, direction) -> None:
        '''
        
        
        
        '''
        self.__frame_actual = 0
        self.__move_x += (direction * self.__bullet_velocity_x)
        if direction == DIRECTION_R:
            self.__actual_animation = self.__bullet_r
        if direction == DIRECTION_L:
            self.__actual_animation = self.__bullet_l
    
    def destroy_bullet(self):
        '''
        
        
        
        '''
        if self.__rect_bullet.right < 0 or self.__rect_bullet.left > ANCHO_VENTANA:
            self.kill()
    
    def change_x(self,delta_x):
        self.__rect_bullet.x += delta_x
        self.__collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.__rect_bullet.y += delta_y
        self.__collition_rect.y += delta_y

    def do_animation(self, delta_ms):
        self.__animation_time += delta_ms
        if self.__animation_time >= self. __frame_rate_ms:
            self.__animation_time = 0
            if self.__frame_actual < (len(self.__actual_animation) - 1):
                self.__frame_actual += 1
            else:
                self.__frame_actual = 0
    
    def do_movement(self, delta_ms)-> None:
        '''
        
        
        
        '''
        self.__movement_time += delta_ms
        if self.__movement_time >= self.__move_rate_ms:
            self.__movement_time = 0         

            self.change_x(self.__move_x) 
            self.change_y(self.__move_y)

    def update(self, delta_ms):
        '''
        
        
        
        '''
        self.move_bullet(self.__direction)
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)

    def draw(self, display: pygame.Surface):
        if DEBUG:
            pygame.draw.rect(display, color = (255, 0, 0), rect = self.__collition_rect)
        self.__actual_image = self.__actual_animation[self.__frame_actual]
        display.blit(self.__actual_image,self.__rect_bullet)


        