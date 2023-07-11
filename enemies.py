import pygame
from constantes import *
from auxiliar import *

class Enemy:
    def __init__(self, x: int, y: int,hitbox_h: int, hitbox_w: int, speed_walk, gravity, frame_animation_ms, move_rate_ms, p_scale = P_SCALE):

        self.__walk_l = Auxiliar.getSurfaceFromSeparateFiles("assets_2\enemies\enemy_flowergrun\walk\gruntflower_run_{0}.png", 1, 16, flip = False, step = 1, scale= p_scale)
        self.__walk_r = Auxiliar.getSurfaceFromSeparateFiles("assets_2\enemies\enemy_flowergrun\walk\gruntflower_run_{0}.png", 1, 16, flip = True, step = 1, scale= p_scale)
        self.__hit_r = Auxiliar.getSurfaceFromSeparateFiles("assets_2\enemies\enemy_flowergrun\hit\gruntflower_hit_{0}.png", 1, 7, flip = False, step = 1, scale= p_scale)
        self.__hit_l = Auxiliar.getSurfaceFromSeparateFiles("assets_2\enemies\enemy_flowergrun\hit\gruntflower_hit_{0}.png", 1, 7, flip = True, step = 1, scale= p_scale)

        self.__frame = 0
        self.__move_x = 0
        self.__move_y = 0

        self.__cadencia = 0
        self.__last_shoot = pygame.time.get_ticks() #cada cuanto tiempo dispara
        self.__contador = 0
        
        self.__speed_walk = speed_walk
        self.__gravity_enemy = gravity
        #self.__power_jumping = power_jump | cuantos pixeles se mueve cuando salta
        self.__actual_animation = self.__walk_r
        self.__image = self.__actual_animation[self.__frame]

        self.__rect = self.__image.get_rect()
        self.__rect_x = 0
        self.__rect_y = 0
        self.__rect.x = x
        self.__rect.y = y
        


        #dibuja el rectangulo
        self.__rect_colision = pygame.Rect(
            x+self.__rect.width/3,
            y+self.__rect.height/3,
            self.__rect.width,
            self.__rect.height)
        
        #transforma al rectangulo, dependiendo del ancho y alto que introducimos, a un tamaño especifico
        self.__rect_colision.height = hitbox_h
        self.__rect_colision.width = hitbox_w
        self.__rect_colision.x = self.__rect.x
        self.__rect_colision.y = self.__rect.y

        self.__floor_colision_rect = pygame.Rect(self.__rect_colision)
        self.__floor_colision_rect.height = GROUND_COLLIDE_H
        self.__floor_colision_rect.y = y + self.__rect_colision.height - GROUND_COLLIDE_H

        self.__roof_colision_rect = pygame.Rect(self.__rect_colision)
        self.__roof_colision_rect.height = 10
        self.__roof_colision_rect.width = 30
        self.__roof_colision_rect.x = self.__rect.x
        self.__roof_colision_rect.y = self.__rect.y

        #self.__sound = pygame.mixer.Sound("ruta_a_audio.mp3/.wav")

        self.__is_walking = True
        self.__is_flying = True
        self.__is_idle = True
        self.__time_animation = frame_animation_ms
        self.__move_rate_ms = move_rate_ms
        self.__y_start_jump = 0

        self.__tiempo_transcurrido = 0
        self.__time_last_jump = 0
    
    #la llamo de esta forma y no es necesario usar los () porque es una property
    @property
    def rect_colision_enemy(self):
        '''
        
        
        
        '''
        return self.__rect_colision
    #la llamo de esta forma y es necesario introducir un parametro
    def get_rect_colision(self) -> pygame.Rect:
        return self.__rect_colision


    def walk(self, direction = DIRECTION_R) -> None:
        '''
        
        
        
        '''
        if direction == DIRECTION_R:
            self.__move_x = self.__speed_walk
            self.__actual_animation = self.__walk_r
        else:
            self.__move_x = -self.__speed_walk
            self.__actual_animation = self.__walk_l
            
    def hit(self, direction: int) -> None:
        '''
        
        
        
        '''
        match direction:
            case 0:
                self.__actual_animation = self.__hit_r
            case 1:
                self.__actual_animation = self.__hit_l
        self.__move_x = 0
        self.__move_y = 0
        self.__frame = 0
    
    def shoot(self, on_off = True):
        self.is_shoot = on_off
        if(on_off == True):
            if(self.animation != self.__walk_r and self.animation != self.__walk_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.move_x = 0
                    self.animation = self.__walk_r
                elif(self.direction == DIRECTION_L):
                    self.move_x = 0
                    self.animation = self.__walk_l
        else:
            self.is_walking = False
    
    # def jump(self, on_off = True) -> None:
    #     '''
        
        
        
    #     '''
    #     if on_off and not self.__is_jumping and not self.__falling:
    #         self.__y_start_jump = self.__rect.y
    #         self.__move_x = int(self.__move_x / 2)
    #         if self.__direction == DIRECTION_R:
    #             self.__move_y = self.__power_jumping
    #             self.__actual_animation = "self.__jump_r"
    #         else:
    #             self.__move_y = -self.__power_jumping
    #             self.__actual_animation = "self.__jump_l"
    #         self.__frame = 0
    #         self.__is_jumping = True

    #     if not on_off:
    #         self.__is_jumping = on_off
    #         self.__stay()

    # def stay(self) -> None:
    #     '''
        
        
        
    #     '''
    #     if self.__actual_animation != self.__stay_r and self.__actual_animation != self.__stay_l:
    #         if self.__direction == DIRECTION_R:
    #             self.__actual_animation = self.__stay_r
    #         else:
    #             self.__actual_animation = self.__stay_l
    #         self.__frame = 0 
    #         self.__move_x = 0 
    #         self.__move_y = 0

    # def movement_random(self) -> None:
    #     '''
        
        
        
    #     '''
    #     if self.__direction == DIRECTION_R:
    #         self.walk(self.__direction)
    #         if self.__rect.x >= (ANCHO_VENTANA) - 20:
    #             self.attack(self.__direction)

    #     elif(self.__direction == DIRECTION_L):
    #         self.walk(self.__direction)
    #         if self.__rect.x == 40:
    #             self.attack(self.__direction)
    
    # def movement_to_player(self, list_player):
    #     '''
        
        
        
    #     '''
    #     for player in list_player:
    #         if self.__rect_x <= player.rect.x:
    #             self.__orientation = DIRECTION_R
    #             self.__actual_animation = self.__stay_r
    #         if self.__rect_x > player.rect.x:
    #             self.__orientation = DIRECTION_L
    #             self.__actual_animation = self.__stay_l
    
    def change_x(self, delta_x):
        '''
        
        
        
        '''
        self.__rect.x += delta_x
        self.__rect_colision.x += delta_x
        self.__floor_colision_rect.x += delta_x
        self.__roof_colision_rect.x += delta_x
    
    def change_y(self, delta_y):
        '''
        
        
        
        '''
        self.__rect.y += delta_y
        self.__rect_colision.y += delta_y
        self.__floor_colision_rect.y += delta_y
        self.__roof_colision_rect.y += delta_y

    def be_on_plataform(self, list_plataform) -> bool:
        '''
        
        
        
        '''
        if self.__floor_colision_rect.bottom >= GROUND_LEVEL:
            return True
        else:
            for plataform in list_plataform:
                if self.__floor_colision_rect.colliderect(plataform):
                    return True
        return False
    
    def generate_movement(self, delta_ms): #list_plataform
        '''
        

        
        '''
        self.__tiempo_transcurrido += delta_ms

        if self.__tiempo_transcurrido >= self.__move_rate_ms:
            self.__tiempo_transcurrido = 0

            # #chequear algo del salto
            # if abs(self.__y_start_jump - self.__rect.y) > self.__height_jump and self.__is_jumping:
            #     self.__move_y = 0

            self.change_y(self.__move_y)

            if self.__is_walking:
                self.__contador += 1
                if self.__contador <= 50:
                    self.walk(DIRECTION_R)
                elif self.__contador <= 100:
                    self.walk(DIRECTION_L)
                else:
                    self.__contador = -1
                self.change_x(self.__move_x)
                
            # if not self.be_on_plataform(list_plataform):
            #     if self.__move_y == 0:
            #         self.__falling = True
            #         self.change_y(self.__gravity_enemy)
            #     else: 
            #         if (self.__is_jumping):
            #             self.jump(False)
            #         self.__falling = False
    
    def consecutives_hits(self, list_player, list_bullets)-> bool:
        '''
        
        
        
        '''
        retorno = False
        #chequear impacto con un proyectil
        for player in list_player:
            for bullet in list_bullets:
                if self.__rect_colision.colliderect(bullet.rect_colision_bullet):
                    self.hit(self.__direction)
                    retorno = True

            if self.__roof_colision_rect.colliderect(player.__floor_colision_rect):
                self.hit(self.__direction)
                retorno = True
        # chequeamos que el player nos esta pisando
        return retorno
    
    def do_animation(self, delta_ms) -> None:
        '''
        
        
        
        '''
        self.__time_animation += delta_ms
        if self.__time_animation >= self.__move_rate_ms:
            self.__time_animation = 0
            if self.__frame < (len(self.__actual_animation) - 1):
                self.__frame += 1
            else:
                self.__frame = 0
    
    def update(self, delta_ms)-> None: #, list_plataform, list_players, list_bullets
        '''
        Actualiza el movimiento y animacion del enemigo, en caso de haber impactado, realizara la animacion
        y movimiento de golpear/atacar.
        Param:
            delta_ms: tiempo transcurrido del juego.
            list_plataforms: es la lista de las plataformas disponible en el nivel.
            list_players: es la lista de los jugadores disponible en el nivel.
            list_bullets: es la lista de los proyectiles de los jugadores actuales en el nivel.
        Return: None
        '''
        self.generate_movement(delta_ms)
        self.do_animation(delta_ms)
        # self.consecutives_hits(delta_ms, list_players, list_bullets)
    
    def draw(self, display: pygame.Surface) -> None:
        if DEBUG:
            pygame.draw.rect(display, color = (255, 0, 0), rect= self.__rect_colision)
        self.__image = self.__actual_animation[self.__frame]
        display.blit(self.__image,self.__rect)
