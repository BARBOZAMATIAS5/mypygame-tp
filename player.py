import pygame
from auxiliar import *
from constantes import *

class Player:
    def __init__(self,x , y, speed_walk, gravity, jump, animation_rate_ms, move_rate_ms, jump_height, interval_time_jump, p_scale = P_SCALE) -> None:
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\stay\cuphead_idle_{0}.png", 1, 9, flip= False,step=1, scale = p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\stay\cuphead_idle_{0}.png", 1, 9, flip= True,step=1, scale = p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\walk\cuphead_run_{0}.png", 1, 16, flip= False,step=1, scale = p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\walk\cuphead_run_{0}.png", 1, 16, flip= True,step=1, scale = p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\jump\cuphead_jump_{0}.png", 1, 8, flip = False,step=1, scale = p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\jump\cuphead_jump_{0}.png", 1, 8, flip = True,step=1, scale = p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\shooting\cuphead_shoot_straight_{0}.png", 1, 5, flip = False,step=1, scale = p_scale)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("assets\cuphead\shooting\cuphead_shoot_straight_{0}.png", 1, 5, flip = True,step=1, scale = p_scale)
        self.death = True

        self.frame = 0
        self.lives = 5
        self.score = 0
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.gravity = gravity
        self.direction = DIRECTION_R
        self.jumping = jump

        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.roof_colision_rect = pygame.Rect(self.collition_rect)
        self.roof_colision_rect.height = 10
        self.roof_colision_rect.width = 30
        self.roof_colision_rect.x = self.rect.x
        self.roof_colision_rect.y = self.rect.y

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = animation_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time_jump

        self.is_jump = False
        self.is_shoot = False
        self.is_falling = False
        self.is_walking = False

    @property
    def rect_colision_player(self):
        '''
        
        
        
        '''
        return self.collition_rect
    #la llamo de esta forma y es necesario introducir un parametro
    def get_rect_colision(self) -> pygame.Rect:
        return self.collition_rect

    def walk (self, direction):
        if (self.is_walking == False and self.is_jump == False and self.is_falling == False):
            if (self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                elif(direction == DIRECTION_L):
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def jump(self, on_off = True):
        if (on_off and self.is_jump == False and self.is_falling == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_y = -self.jumping
                self.animation = self.jump_r
            else:
                self.move_y = -self.jumping
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
            self.is_falling = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self, on_off = True):
        if(self.is_shoot):
            return

        if (on_off and self.animation != self.stay_l and self.animation != self.stay_r):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r            
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def shoot(self, on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_falling == False):
            self.is_walking = True
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.move_x = 0
                    self.animation = self.shoot_r
                elif(self.direction == DIRECTION_L):
                    self.move_x = 0
                    self.animation = self.shoot_l
        else:
            self.is_walking = False

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.roof_colision_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.roof_colision_rect.y += delta_y
    
    def out_display(self):
        '''
        
        
        
        '''
        

    def is_on_plataform(self, plataform_list):
        retorno = False

        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True
        else:
            for plataform in plataform_list:
                if(self.ground_collition_rect.colliderect(plataform.ground_collition_rect)):
                    retorno = True
        return retorno

    def do_movement(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.frame_rate_ms):
            self.tiempo_transcurrido_move = 0
            if (abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.change_y(self.move_y)
            self.change_x(self.move_x)

            if (not self.is_on_plataform(plataform_list)):
                if (self.move_y == 0):
                    self.is_falling = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump):
                    self.jump(False)
                self.is_falling = False
            
    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if (self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self, delta_ms, plataform_list):
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms)
        
    def draw(self,screen: pygame.Surface):
        if DEBUG:
            pygame.draw.rect(screen, color = (255, 0, 0), rect= self.collition_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def events(self,delta_ms, keys):
        self.tiempo_transcurrido += delta_ms

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