import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    def __init__(self, owner: str, x: int, y: int,hitbox_h: int, hitbox_w: int, speed_walk, gravity, frame_animation_ms, move_rate_ms, direction = None, p_scale = P_SCALE, count_cd = int):

        if owner == "flowergun":
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flowergrun\walk\gruntflower_run_{0}.png", 1, 16, flip = False, scale= p_scale)
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flowergrun\walk\gruntflower_run_{0}.png", 1, 16, flip = True, scale= p_scale)

            self.actual_animation = self.walk_r

        if owner == "mushroom":
            self.idle_l= Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\idle\mushroom_idle_000{0}.png", 1, 9, flip=False, scale= p_scale)
            self.idle_r= Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\idle\mushroom_idle_000{0}.png", 1, 9, flip=True, scale= p_scale)
            self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\\attack\mushroom_attack_00{0}.png", 1, 15, flip=False, scale= p_scale)
            self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_mushroom\\attack\mushroom_attack_00{0}.png", 1, 15, flip=True, scale= p_scale)
            
            if direction == DIRECTION_L:
                self.actual_animation = self.idle_l
            else:
                self.actual_animation = self.idle_r
        
        if owner == "flapy_bird":
            self.fly_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flappy_bird\\flappy_bird_fly_00{0}.png", 1, 16, flip=False, scale= p_scale)
            self.fly_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_flappy_bird\\flappy_bird_fly_00{0}.png", 1, 16, flip=True, scale= p_scale)

            self.actual_animation = self.__fly_l
        
        if owner == "egghead":
            self.idle_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\idle\egghead_idle_00{0}.png", 1, 16, flip=False, scale= p_scale)
            self.idle_r = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\idle\egghead_idle_00{0}.png", 1, 16, flip=True, scale= p_scale)
            self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\shoot\egghead_shoot_00{0}.png", 1, 20, flip=False, scale= p_scale)
            self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("assets\enemies\enemy_egghead\shoot\egghead_shoot_00{0}.png", 1, 20, flip=True, scale= p_scale)

            if direction == DIRECTION_L:
                self.actual_animation = self.idle_l
            else:
                self.actual_animation = self.idle_r

        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.owner = owner
        self.direction = direction

        self.contador = 0
        
        self.speed_walk = speed_walk
        self.gravity_enemy = gravity
        #self.__power_jumping = power_jump | cuantos pixeles se mueve cuando salta
        self.image = self.actual_animation[self.frame]

        self.rect = self.image.get_rect()
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

        self.floor_colision_rect = pygame.Rect(self.collition_rect)
        self.floor_colision_rect.height = GROUND_COLLIDE_H
        self.floor_colision_rect.y = y + self.collition_rect.height - GROUND_COLLIDE_H

        self.roof_colision_rect = pygame.Rect(self.collition_rect)
        self.roof_colision_rect.height = 10
        self.roof_colision_rect.width = 30
        self.roof_colision_rect.x = self.rect.x
        self.roof_colision_rect.y = self.rect.y

        #self.__sound = pygame.mixer.Sound("ruta_a_audio.mp3/.wav")

        self.is_walking = True
        self.is_flying = True
        self.time_animation = frame_animation_ms
        self.move_rate_ms = move_rate_ms
        self.tiempo_transcurrido = 0
        self.hit = 0

        self.count_cd = count_cd
        self.is_shoot = False
    
    #la llamo de esta forma y no es necesario usar los () porque es una property
    @property
    def rect_colision_enemy(self):
        '''
        Devuelve las dimensiones de la imagen

        Parametros: -
        
        Retorna la dimension de la imagen, un rectangulo
        '''
        return self.collition_rect
    #la llamo de esta forma y es necesario introducir un parametro
    # def get_rect_colision(self) -> pygame.Rect:
    #     return self.collition_rect

    def getSelfHit(self):
        return self.hit

    def walk(self, direction: int) -> None:
        '''
        Se encarga de la accion caminar del enemigo teniendo en cuenta: la direccion (izquierda o derecha),
        animacion de la direccion y velocidad de movimiento
        
        Parametro: int (corresponde a la direccion del enemigo)
        
        No retorna nada
        '''
        self.direction = direction
        if self.direction == DIRECTION_R:
            self.move_x = self.speed_walk
            self.actual_animation = self.walk_r
        elif self.direction == DIRECTION_L:
            self.move_x = -self.speed_walk
            self.actual_animation = self.walk_l

    def stay(self, on_off = True) -> None:
        '''
        Se encarga de la accion estatica del enemigo teniendo en cuenta: si la accion de disparar (true o false)
        y la animacion
        
        Parametro: bool (corresponde a un booleano)
        
        No retorna nada
        '''
        if on_off and self.is_shoot == False:
            if(self.actual_animation != self.idle_r and self.actual_animation != self.idle_l):
                if self.direction == DIRECTION_R:
                    self.actual_animation = self.idle_r
                elif self.direction == DIRECTION_L:
                    self.actual_animation = self.idle_l
                self.frame = 0

    def fly(self, direction: int) -> None:
        '''
        Se encarga de la accion volar del enemigo teniendo en cuenta: la direccion (izquierda o derecha),
        animacion de la direccion
        
        Parametro: int (corresponde a la direccion del enemigo)
        
        No retorna nada
        '''
        self.direction = direction
        if self.direction == DIRECTION_R:
            self.actual_animation = self.fly_r   
        elif self.direction == DIRECTION_L:
            self.actual_animation = self.fly_l

    def hit_shoot(self, bullet_list: list):
        '''
        Se encarga de detectar si algun proyectil colisiono contra el enemigo, sumando +1 al
        atributo 'self.__hit' cada vez que se detecte
        
        Parametro: list (corresponde a la lista de proyectiles)
        
        Retorna el atributo self.__hit modificado siempre que se detecte una colision
        '''
        for bullet in bullet_list:
            if self.collition_rect.colliderect(bullet.rect_colision_bullet) == True:
                self.hit += 1
                print(self.hit)
    
    def shoot(self, on_off = True):
        '''
        Por defecto el parametro del metodo es True, modificando el atributo self.is_shoot por lo que,
        entra en la funcion if, encargandose de inmovilizar al enemigo y proceder a cambiar la animacion
        
        Parametro: bool (permite la entrada a la funcion o no, al igual que cambiar el estado del atributo)
        
        No retorna nada
        '''
        self.is_shoot = on_off
        if(self.is_shoot):
            if(self.actual_animation != self.shoot_r and self.actual_animation != self.shoot_l):
                if(self.direction == DIRECTION_R):
                    self.move_x = 0
                    self.move_y = 0
                    self.actual_animation = self.shoot_r
                elif(self.direction == DIRECTION_L):
                    self.move_x = 0
                    self.move_y = 0
                    self.actual_animation = self.shoot_l
            self.frame = 0

    def change_x(self, delta_x: int):
        '''
        Se encarga del movimiento rectangulo del enemigo en la posicion 'x' (vertical)

        Parametro: int (corresponde al atributo de movimiento en 'x' (self.move_x))

        No retorna nada
        '''
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.floor_colision_rect.x += delta_x
        self.roof_colision_rect.x += delta_x
    
    def change_y(self, delta_y: int):
        '''
        Se encarga del movimiento rectangulo del enemigo en la posicion 'y' (horizontal)

        Parametro: int (corresponde al atributo de movimiento en 'y' (self.move_y))

        No retorna nada
        
        '''
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.floor_colision_rect.y += delta_y
        self.roof_colision_rect.y += delta_y

    def on_plataform(self, list_plataform: list) -> bool:
        '''
        Corrobora si el enemigo se encuentra encima de una plataforma
        
        Parametro: list (lista de plataformas)
        
        Retorna un booleano
        '''
        retorno = False

        for plataform in list_plataform:
            if self.floor_colision_rect.colliderect(plataform.ground_collition_rect):
                return True
            
        return retorno
    
    def do_movement(self, delta_ms: int, list_plataform: list):
        '''
        Corresponde a las acciones (los metodos: walk, shoot, stay, fly) y movimientos de X e Y del
        enemigo (change_x, change_y), al igual que verificar si se encuentra sobre una plataforma 
        (on_plataform)
        
        Parametro: int (frames en que se ejecutará el juego), list (lista de plataformas)
        
        No retorna nada
        '''
        self.tiempo_transcurrido += delta_ms

        if self.tiempo_transcurrido >= self.move_rate_ms:
            self.tiempo_transcurrido = 0

            if self.owner == "flowergun":
                if self.is_walking:
                    self.contador += 1
                    if self.contador <= self.count_cd:
                        self.walk(DIRECTION_R)
                    elif self.contador <= self.count_cd * 2:
                        self.walk(DIRECTION_L)
                    else:
                        self.contador = -1
            
            elif self.owner == "mushroom":
                self.contador += 1
                if self.is_shoot == False and self.contador == self.count_cd:
                    self.shoot()
                    self.stay(False)
                elif self.contador == self.count_cd + 15:
                    self.shoot(False)
                    self.stay()
                    self.contador = 0
            
            elif self.owner == "flapy_bird":
                if self.is_flying:
                    self.fly(self.direction)
                    self.contador += 1
                    if self.contador <= self.count_cd:
                        self.move_y = self.speed_walk
                    elif self.contador <= self.count_cd * 2:
                        self.move_y = -self.speed_walk
                    else:
                        self.contador = -1
            
            if not self.on_plataform(list_plataform):
                if self.move_y == 0:
                    self.change_y(self.gravity_enemy)

            self.change_x(self.move_x)
            self.change_y(self.move_y)

    def do_animation(self, delta_ms) -> None:
        '''
        Se encarga del cambio de frame de la animacion del enemigo

        Parametro: int (corresponde a los frames en que se ejecutará el juego)

        No retorna nada
        '''
        self.time_animation += delta_ms
        if self.time_animation >= self.move_rate_ms:
            self.time_animation = 0
            if self.frame < (len(self.actual_animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
    
    def update(self, delta_ms: int, list_plataform: list)-> None:
        '''
        Actualiza el movimiento y animacion del enemigo.
        Param:
            delta_ms: tiempo transcurrido del juego.
            list_plataforms: es la lista de las plataformas disponible en el nivel.
            list_players: es la lista de los jugadores disponible en el nivel.
            list_bullets: es la lista de los proyectiles de los jugadores actuales en el nivel.
        Return: None
        '''
        self.do_movement(delta_ms, list_plataform)
        self.do_animation(delta_ms)
    
    def draw(self, display: pygame.Surface) -> None:
        '''
        Dibuja en la pantalla del juego al objeto, el proyectil. Posibilita tambien que se muestre
        el rectangulo
        que ocupa, diriase la 'hitbox'
        
        Parametro: surface (corresponde a la clase encargada de la pantalla, de la libreria de pygame)
        
        No retorna nada
        '''
        if DEBUG:
            pygame.draw.rect(display, color = (255, 0, 0), rect= self.collition_rect)
        self.__image = self.actual_animation[self.frame]
        display.blit(self.__image,self.rect)
