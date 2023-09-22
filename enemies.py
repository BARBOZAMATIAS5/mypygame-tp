import pygame
from constantes import *
from auxiliar import *
from bullets import *

class Enemy():
    def __init__(self, owner: str, x: int, y: int,hitbox_h: int, hitbox_w: int, speed_walk, gravity, frame_animation_ms, move_rate_ms, direction = None, p_scale = P_SCALE, count_cd = int):

        if owner == "flowergun":
            self.__walk_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flowergrun\walk\gruntflower_run_{0}.png", 1, 16, flip = False, step = 1, scale= p_scale)
            self.__walk_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flowergrun\walk\gruntflower_run_{0}.png", 1, 16, flip = True, step = 1, scale= p_scale)

            self.__actual_animation = self.__walk_r

        if owner == "mushroom":
            self.__idle_l= Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\idle\mushroom_idle_000{0}.png", 1, 9, flip=False, step = 1, scale= p_scale)
            self.__idle_r= Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\idle\mushroom_idle_000{0}.png", 1, 9, flip=True, step = 1, scale= p_scale)
            self.__shoot_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\\attack\mushroom_attack_00{0}.png", 1, 15, flip=False, step = 1, scale= p_scale)
            self.__shoot_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\\attack\mushroom_attack_00{0}.png", 1, 15, flip=True, step = 1, scale= p_scale)
            
            if direction == DIRECTION_L:
                self.__actual_animation = self.__idle_l
            else:
                self.__actual_animation = self.__idle_r
        
        if owner == "flapy_bird":
            self.__fly_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flappy_bird\\flappy_bird_fly_00{0}.png", 1, 16, flip=False, step = 1, scale= p_scale)
            self.__fly_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flappy_bird\\flappy_bird_fly_00{0}.png", 1, 16, flip=True, step = 1, scale= p_scale)

            self.__actual_animation = self.__fly_l
        
        if owner == "egghead":
            self.__idle_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\idle\egghead_idle_00{0}.png", 1, 16, flip=False, step = 1, scale= p_scale)
            self.__idle_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\idle\egghead_idle_00{0}.png", 1, 16, flip=True, step = 1, scale= p_scale)
            self.__shoot_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\shoot\egghead_shoot_00{0}.png", 1, 20, flip=False, step = 1, scale= p_scale)
            self.__shoot_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\shoot\egghead_shoot_00{0}.png", 1, 20, flip=True, step = 1, scale= p_scale)

            if direction == DIRECTION_L:
                self.__actual_animation = self.__idle_l
            else:
                self.__actual_animation = self.__idle_r

        self.__frame = 0
        self.__move_x = 0
        self.__move_y = 0
        self.__owner = owner
        self.direction = direction

        self.__contador = 0
        
        self.__speed_walk = speed_walk
        self.__gravity_enemy = gravity
        #self.__power_jumping = power_jump | cuantos pixeles se mueve cuando salta
        self.__image = self.__actual_animation[self.__frame]

        self.rect = self.__image.get_rect()
        self.rect.center = (x,y)
        self.rect.x = x
        self.rect.y = y

        #dibuja el rectangulo
        self.collition_rect = pygame.Rect(
            x+self.rect.width/3,
            y+self.rect.height,
            self.rect.width,
            self.rect.height)
        
        #transforma al rectangulo, dependiendo del ancho y alto que introducimos, a un tamaño especifico
        self.collition_rect.height = hitbox_h
        self.collition_rect.width = hitbox_w
        self.collition_rect.x = self.rect.x
        self.collition_rect.y = self.rect.y

        self.__floor_colision_rect = pygame.Rect(self.collition_rect)
        self.__floor_colision_rect.height = GROUND_COLLIDE_H
        self.__floor_colision_rect.y = y + self.collition_rect.height - GROUND_COLLIDE_H

        self.__roof_colision_rect = pygame.Rect(self.collition_rect)
        self.__roof_colision_rect.height = 10
        self.__roof_colision_rect.width = 30
        self.__roof_colision_rect.x = self.rect.x
        self.__roof_colision_rect.y = self.rect.y

        #self.__sound = pygame.mixer.Sound("ruta_a_audio.mp3/.wav")

        self.__is_walking = True
        self.__is_flying = True
        self.time_animation = frame_animation_ms
        self.move_rate_ms = move_rate_ms
        self.time_movement = 0

        self.__hit = 0

        self.__count_cd = count_cd
        self.cooldown_shoot = 0
        self.is_shoot = False
        self.interval_shoot = 600
        self.tiempo_transcurrido = 0
    
    #la llamo de esta forma y no es necesario usar los () porque es una property
    @property
    def rect_colision_enemy(self):
        '''
        
        
        
        '''
        return self.collition_rect
    #la llamo de esta forma y es necesario introducir un parametro
    def get_rect_colision(self) -> pygame.Rect:
        return self.collition_rect

    def walk(self, direction) -> None:
        '''
        
        
        
        '''
        self.direction = direction
        if self.direction == DIRECTION_R:
            self.__move_x = self.__speed_walk
            self.__actual_animation = self.__walk_r
        elif self.direction == DIRECTION_L:
            self.__move_x = -self.__speed_walk
            self.__actual_animation = self.__walk_l

    def stay(self, on_off= True) -> None:
        '''
        
        
        
        '''
        if self.is_shoot:
            return
        
        elif on_off and self.is_shoot == False:
            if(self.__actual_animation != self.__idle_r and self.__actual_animation != self.__idle_l):
                if self.direction == DIRECTION_R:
                    self.__actual_animation = self.__idle_r
                elif self.direction == DIRECTION_L:
                    self.__actual_animation = self.__idle_l
                self.__frame = 0

    def fly(self, direction) -> None:
        '''
        
        
        
        '''
        self.direction = direction
        if self.direction == DIRECTION_R:
            self.__actual_animation = self.__fly_r   
        elif self.direction == DIRECTION_L:
            self.__actual_animation = self.__fly_l

    def hit(self, bullet_list: list) -> None:
        '''
        
        
        
        '''
        for bullet in bullet_list:
            if self.collition_rect.colliderect(bullet.rect_colision_bullet) == True:
                self.__hit += 1
                return self.__hit
        return None
    
    def shoot(self, on_off = True):
            self.is_shoot = on_off
            if(self.is_shoot):
                if(self.__actual_animation != self.__shoot_r and self.__actual_animation != self.__shoot_l):
                    if(self.direction == DIRECTION_R):
                        self.move_x = 0
                        self.move_y = 0
                        self.__actual_animation = self.__shoot_r
                    elif(self.direction == DIRECTION_L):
                        self.move_x = 0
                        self.move_y = 0
                        self.__actual_animation = self.__shoot_l
                self.__frame = 0
            else:
                self.stay()

    def change_x(self, delta_x):
        '''
        
        
        
        '''
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.__floor_colision_rect.x += delta_x
        self.__roof_colision_rect.x += delta_x
    
    def change_y(self, delta_y):
        '''
        
        
        
        '''
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.__floor_colision_rect.y += delta_y
        self.__roof_colision_rect.y += delta_y

    def on_plataform(self, list_plataform) -> bool:
        '''
        
        
        
        '''
        retorno = False

        for plataform in list_plataform:
            if self.__floor_colision_rect.colliderect(plataform.ground_collition_rect):
                return True
            
        return retorno
    
    def do_movement(self, delta_ms, list_plataform):
        '''
        

        
        '''
        self.time_movement += delta_ms

        if self.time_movement >= self.move_rate_ms:
            self.time_movement = 0

            if self.__owner == "flowergun":
                if self.__is_walking:
                    self.__contador += 1
                    if self.__contador <= self.__count_cd:
                        self.walk(DIRECTION_R)
                    elif self.__contador <= self.__count_cd * 2:
                        self.walk(DIRECTION_L)
                    else:
                        self.__contador = -1
            
            elif self.__owner == "mushroom":
                self.__contador += 1
                if self.__contador == self.__count_cd:
                    self.shoot()
                    self.stay(False)
                elif self.__contador == self.__count_cd + 15:
                    self.shoot(False)
                    self.stay()
                    self.__contador = 0
            
            elif self.__owner == "flapy_bird":
                if self.__is_flying:
                    self.fly(self.direction)
                    self.__contador += 1
                    if self.__contador <= self.__count_cd:
                        self.__move_y = self.__speed_walk
                    elif self.__contador <= self.__count_cd * 2:
                        self.__move_y = -self.__speed_walk
                    else:
                        self.__contador = -1
            
            if not self.on_plataform(list_plataform):
                if self.__move_y == 0:
                    self.change_y(self.__gravity_enemy)

            self.change_x(self.__move_x)
            self.change_y(self.__move_y)

    def do_animation(self, delta_ms) -> None:
        '''
        
        
        
        '''
        self.time_animation += delta_ms
        if self.time_animation >= self.move_rate_ms:
            self.time_animation = 0
            if self.__frame < (len(self.__actual_animation) - 1):
                self.__frame += 1
            else:
                self.__frame = 0
    
    def update(self, delta_ms, list_plataform)-> None: #, list_plataform
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
        self.tiempo_transcurrido += delta_ms
        self.do_movement(delta_ms, list_plataform)
        self.do_animation(delta_ms)
        # self.consecutives_hits(delta_ms, list_players, list_bullets)
    
    def draw(self, display: pygame.Surface) -> None:
        if DEBUG:
            pygame.draw.rect(display, color = (255, 0, 0), rect= self.collition_rect)
        self.__image = self.__actual_animation[self.__frame]
        display.blit(self.__image,self.rect)
