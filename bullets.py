import pygame
from auxiliar import Auxiliar
from constantes import *

class Bullet():
    def __init__(self, owner, x_init: int, y_init: int, frame_rate_ms: int, move_rate_ms: int, velocity_x: float, p_scale: float, direction: int) -> None:
        
        if owner == "player":
            self.__bullet_r = Auxiliar.getSurfaceFromSeparateFiles(
                "assets\cuphead\\bullet\peashoot\peashooter_0{0}.png", 1, 13, False, scale=p_scale)
            self.__bullet_l = Auxiliar.getSurfaceFromSeparateFiles(
                "assets\cuphead\\bullet\peashoot\peashooter_0{0}.png", 1, 13, True, scale=p_scale)
        elif owner == "enemy":
            self.__bullet_r = Auxiliar.getSurfaceFromSeparateFiles(
                "assets\enemies\enemy_mushroom\\bullet\mushroom_poison_cloud_00{0}.png", 1, 12, False, scale=p_scale)
            self.__bullet_l = Auxiliar.getSurfaceFromSeparateFiles(
                "assets\enemies\enemy_mushroom\\bullet\mushroom_poison_cloud_00{0}.png", 1, 12, True, scale=p_scale)
        elif owner == "enemy_2":
            self.__bullet_r = Auxiliar.getSurfaceFromSeparateFiles(
                "assets\enemies\enemy_egghead\bullet\egghead_bullet_00{0}.png", 1, 8, True, scale=p_scale)
            self.__bullet_l = Auxiliar.getSurfaceFromSeparateFiles(
                "assets\enemies\enemy_egghead\bullet\egghead_bullet_00{0}.png", 1, 8, False, scale=p_scale) 

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

        self.__is_shooting = True

    @property
    def rect_colision_bullet(self) -> pygame.Rect:
        '''
        Devuelve las dimensiones de la imagen

        Parametros: -
        
        Retorna la dimension de la imagen, un rectangulo
        '''
        return self.__collition_rect

    def move_bullet(self, direction: int) -> None:
        '''
        Controla la animacion, velocidad y direccion del proyectil

        Parametro: int (corresponde a la direccion del proyectil (derecha o izquierda))
        
        No retorna nada
        '''
        # self.__move_x += (direction * self.__bullet_velocity_x)
        if direction == DIRECTION_R:
            self.__actual_animation = self.__bullet_r
            self.__move_x = self.__bullet_velocity_x
        if direction == DIRECTION_L:
            self.__actual_animation = self.__bullet_l
            self.__move_x = -self.__bullet_velocity_x

    def check_collition(self, hit, enemy_list: list, player) -> bool:
        '''
        Verifica si el proyectil colisiona contra el rectangulo de un enemigo, jugador o extremos de
        la pantalla
        
        Parametro: any (metodo 'hit' dentro de las clases 'player' y 'enemy'), list (lista de enemigos),
        any (atributo que conserva la informacion del jugador)
        
        Retorna un booleano
        '''
        collition = False

        if hit == 'player':
            if (self.__collition_rect.colliderect(player.collition_rect)):
                collition = True

        if hit == 'enemy':
            for enemy in enemy_list:
                if (self.__collition_rect.colliderect(enemy.collition_rect)):
                    collition = True
        
        if (self.__rect_bullet.x < 0 or self.__rect_bullet.x > ANCHO_VENTANA):
                collition = True
        
        return collition
    
    def change_x(self,delta_x = int):
        '''
        Se encarga del movimiento rectangulo del proyectil en la posicion 'x' (vertical)

        Parametro: int (corresponde al atributo de movimiento en 'x' (self.__move_x))

        No retorna nada
        '''
        self.__rect_bullet.x += delta_x
        self.__collition_rect.x += delta_x

    def change_y(self,delta_y = int):
        '''
        Se encarga del movimiento rectangulo del proyectil en la posicion 'y' (horizontal)

        Parametro: int (corresponde al atributo de movimiento en 'y' (self.__move_y))

        No retorna nada
        '''
        self.__rect_bullet.y += delta_y
        self.__collition_rect.y += delta_y

    def do_animation(self, delta_ms = int):
        '''
        Se encarga del cambio de frame de la animacion del proyectil

        Parametro: int (corresponde a los frames en que se ejecutará el juego)

        No retorna nada
        '''
        self.__animation_time += delta_ms
        if self.__animation_time >= self.__frame_rate_ms:
            self.__animation_time = 0
            if self.__frame_actual < (len(self.__actual_animation) - 1):
                self.__frame_actual += 1
            else:
                self.__frame_actual = 0

    def do_movement(self, delta_ms)-> None:
        '''
        Delimita la velocidad del movimiento del proyectil y el movimiento en las posiciones 'x' e 'y',
        usando las los metodos: 'self.change_x', 'self.change_y'
        
        Parametro: int (corresponde a los frames en que se ejecutará el juego)
        
        No retorna nada
        '''
        self.__movement_time += delta_ms
        if self.__movement_time >= self.__move_rate_ms:
            self.__movement_time = 0  

            self.change_y(self.__move_y)
            
            if self.__is_shooting:
                self.move_bullet(self.__direction)

            self.change_x(self.__move_x)

    def update(self, delta_ms):
        '''
        Actualiza la informacion del movimiento y la animacion del proyectil entorno a los frames
        del juego.
        
        Parametro: int (corresponde a los frames que se ejecutará el juego)
        
        No retorna nada
        '''
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)

    def draw(self, display: pygame.Surface):
        '''
        Dibuja en la pantalla del juego al objeto, el proyectil. Posibilita tambien que se muestre
        el rectangulo
        que ocupa, diriase la 'hitbox'
        
        Parametro: surface (corresponde a la clase encargada de la pantalla, de la libreria de pygame)
        
        No retorna nada
        '''
        if DEBUG:
            pygame.draw.rect(display, color = (255, 0, 0), rect = self.__rect_bullet)
        self.__actual_image = self.__actual_animation[self.__frame_actual]
        display.blit(self.__actual_image,self.__rect_bullet)

