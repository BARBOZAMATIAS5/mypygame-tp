import pygame
from auxiliar import Auxiliar
from constantes import *

class Player():
    def __init__(self,x , y, speed_walk, gravity, jump, animation_rate_ms, move_rate_ms, jump_height, interval_time_jump, p_scale = P_SCALE) -> None:
        
        self.__stay_r = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\stay\cuphead_idle_{0}.png", 1, 9, flip= False, scale = p_scale)
        self.__stay_l = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\stay\cuphead_idle_{0}.png", 1, 9, flip= True, scale = p_scale)
        
        self.__walk_r = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\walk\cuphead_run_{0}.png", 1, 16, flip= False, scale = p_scale)
        self.__walk_l = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\walk\cuphead_run_{0}.png", 1, 16, flip= True, scale = p_scale)
        
        self.__jump_r = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\jump\cuphead_jump_{0}.png", 1, 8, flip = False, scale = p_scale)
        self.__jump_l = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\jump\cuphead_jump_{0}.png", 1, 8, flip = True, scale = p_scale)
        
        self.__shoot_r = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\shooting\cuphead_shoot_straight_{0}.png", 1, 5, flip = False, scale = p_scale)
        self.__shoot_l = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\shooting\cuphead_shoot_straight_{0}.png", 1, 5, flip = True, scale = p_scale)
        
        self.__auch_r = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\hit\cuphead_hit_000{0}.png", 1, 6, flip = False, scale = p_scale)
        self.__auch_l = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\hit\cuphead_hit_000{0}.png", 1, 6, flip = True, scale = p_scale)
        
        self.__death = Auxiliar.getSurfaceFromSeparateFiles(
            "assets\cuphead\ghost\cuphead_ghost_00{0}.png", 1, 24, flip = False, scale = p_scale)

        self.__frame = 0
        self.score = 0
        
        self.__move_x = 0
        self.__move_y = 0
        self.__speed_walk = speed_walk
        self.__gravity = gravity
        self.direction = DIRECTION_R
        self.__jumping = jump

        self.__animation = self.__stay_r
        self.__image = self.__animation[self.__frame]
        self.rect = self.__image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y+20,self.rect.width/2,self.rect.height-30)

        self.__ground_collition_rect = pygame.Rect(self.collition_rect)
        self.__ground_collition_rect.height = GROUND_COLLIDE_H
        self.__ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.__roof_colision_rect = pygame.Rect(self.collition_rect)
        self.__roof_colision_rect.height = 10
        self.__roof_colision_rect.width = 20
        self.__roof_colision_rect.x = self.rect.x
        self.__roof_colision_rect.y = self.rect.y

        self.__tiempo_transcurrido_animation = 0
        self.__frame_rate_ms = animation_rate_ms
        self.__move_rate_ms = move_rate_ms
        self.__y_start_jump = 0
        self.__jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time_jump
        self.interval_shoot = 300
        self.cooldown_shoot = 0

        self.have_coins = 0
        self.is_shoot = False
        self.__is_jump = False
        self.__is_falling = False
        self.__is_walking = False
        self.__is_alive = True
        self.__is_live = 5

    @property
    def rect_colision_player(self):
        '''
        
        
        
        '''
        return self.collition_rect
    #la llamo de esta forma y es necesario introducir un parametro
    
    def walk(self, direction):
        '''
        
        
        
        '''
        if (self.__is_walking == False and self.__is_jump == False and self.__is_falling == False):
            if (self.direction != direction or (self.__animation != self.__walk_r and self.__animation != self.__walk_l)):
                self.__frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.__move_x = self.__speed_walk
                    self.__animation = self.__walk_r
                elif(direction == DIRECTION_L):
                    self.__move_x = -self.__speed_walk
                    self.__animation = self.__walk_l

    def jump(self, on_off = True):
        '''
        
        
        
        '''
        if (on_off and self.__is_jump == False and self.__is_falling == False):
            self.__y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.__move_y = -self.__jumping
                self.__animation = self.__jump_r
            else:
                self.__move_y = -self.__jumping
                self.__animation = self.__jump_l
            self.__frame = 0
            self.__is_jump = True
            self.__is_falling = True
        if(on_off == False):
            self.__is_jump = False
            self.stay()

    def stay(self, on_off = True):
        '''
        
        
        
        '''
        if(self.is_shoot):
            return
        
        if (on_off and self.__animation != self.__stay_l and self.__animation != self.__stay_r):
            if(self.direction == DIRECTION_R):
                self.__animation = self.__stay_r            
            else:
                self.__animation = self.__stay_l
            self.__move_x = 0
            self.__move_y = 0
            self.__frame = 0

    def shoot(self, on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.__is_jump == False and self.__is_falling == False):
            self.__is_walking = True
            if(self.__animation != self.__shoot_r and self.__animation != self.__shoot_l):
                self.__frame = 0
                if(self.direction == DIRECTION_R):
                    self.__move_x = 0
                    self.__animation = self.__shoot_r
                elif(self.direction == DIRECTION_L):
                    self.__move_x = 0
                    self.__animation = self.__shoot_l
        else:
            self.__is_walking = False

    def death(self):
        self.frame = 0
        self.__move_y = -1
        self.__move_x = 0
        self.__animation = self.__death

    def hit(self, bullet_list_enemy, enemy_list):
        for bullet in bullet_list_enemy:
            if self.collition_rect.colliderect(bullet.rect_colision_bullet) == True:
                self.__is_live -= 1
                return self.__is_live
            
        for enemy in enemy_list:
            if self.collition_rect.colliderect(enemy.collition_rect) == True:
                self.__is_live -= 1
                return self.__is_live
        return None
    
    def check_death(self):

        if self.__is_live < 0 or self.rect.y > ALTO_VENTANA:
            self.__is_alive = False

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.__ground_collition_rect.x += delta_x
        self.__roof_colision_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.__ground_collition_rect.y += delta_y
        self.__roof_colision_rect.y += delta_y
    
    def out_display(self):
        '''
        
        
        
        '''
        if self.rect.x <= 0 or self.rect.x >= 1200:
            self.__move_x = 0
        if self.rect.y <= 0 or self.rect.y >= ALTO_VENTANA:
            self.__move_y = 0

    def is_on_plataform(self, plataform_list):
        retorno = False

        for plataform in plataform_list:
            if(self.__ground_collition_rect.colliderect(plataform.ground_collition_rect)):
                retorno = True
        return retorno

    def do_movement(self, delta_ms, plataform_list):
        self.__move_rate_ms += delta_ms
        if self.__is_alive:
            if(self.__move_rate_ms >= self.__frame_rate_ms):
                self.__move_rate_ms = 0
                if (abs(self.__y_start_jump) - abs(self.rect.y) > self.__jump_height and self.__is_jump):
                    self.__move_y = 0

                self.change_y(self.__move_y)
                self.change_x(self.__move_x)

                self.out_display()
                self.check_death()
                if (not self.is_on_plataform(plataform_list)):
                    if (self.__move_y == 0):
                        self.__is_falling = True
                        self.change_y(self.__gravity)
                else:
                    if (self.__is_jump):
                        self.jump(False)
                    self.__is_falling = False
  
        else:
            self.death()
            if self.rect.y == -150:
                self.__move_y = 0
                self.__move_x = 0
            self.change_y(self.__move_y)
            self.change_x(self.__move_x)

    def do_animation(self, delta_ms):
        self.__tiempo_transcurrido_animation += delta_ms
        if (self.__tiempo_transcurrido_animation >= self.__frame_rate_ms):
            self.__tiempo_transcurrido_animation = 0
            if(self.__frame < len(self.__animation) - 1):
                self.__frame += 1 
            else: 
                self.__frame = 0

    def update(self, delta_ms, plataform_list):
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms)

    def draw(self,screen: pygame.Surface):
        if DEBUG:
            pygame.draw.rect(screen, color = (255, 0, 0), rect= self.collition_rect)
        self.__image = self.__animation[self.__frame]
        screen.blit(self.__image,self.rect)

    def events(self, delta_ms, keys):
        self.tiempo_transcurrido += delta_ms
        if self.__is_alive:
            if (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                self.walk(DIRECTION_L)
            if (keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_SPACE]):
                self.walk(DIRECTION_R)
            if (not keys[pygame.K_a]):
                self.shoot(False)
            if (keys[pygame.K_a]):
                self.shoot()
            if (keys[pygame.K_SPACE]):
                if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                    self.jump(True)
                    self.tiempo_last_jump = self.tiempo_transcurrido
            if (not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_SPACE]):
                self.stay()
            if ((keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]) and not keys[pygame.K_SPACE]):
                self.stay()