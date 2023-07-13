from plataform import Plataform
from player import Player
from constantes import *
from enemies import Enemy
from background import Background
from gui_form import Form
from bullets import Bullet
from coin import Coin

class LevelGame1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.static_background = Background(x= 0, y=0, widht=w, height=h, path="assets\maps\\background.png")

        self.player_1 = Player(x= 0, y = 500, speed_walk= 10, gravity=8, jump=30, animation_rate_ms=25, move_rate_ms=30, jump_height=150, interval_time_jump = 300)
        
        self.enemy_1= Enemy("flowergun",x= 0, y = 500,hitbox_h=170, hitbox_w=110, speed_walk= 8, gravity=8,frame_animation_ms=35, move_rate_ms=30)
        self.enemy_2= Enemy("mushroom",x= 500, y = 500,hitbox_h=100, hitbox_w=50, speed_walk= 1, gravity=8,frame_animation_ms=35, move_rate_ms=30)

        self.plataform_list = []
        self.plataform_list.append(Plataform(x = 0, y= 640,path="assets\plataform\\background_floor.png", width= 1280, height = 720, type=1))
        self.plataform_list.append(Plataform(x = 0, y= 450,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 150, y= 250,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 300, y= 450,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 450, y= 250,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 600, y= 450,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 750, y= 250,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 900, y= 450,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))
        self.plataform_list.append(Plataform(x = 1050, y= 250,path="assets\plataform\plataform_wood_01.png", width= 175, height = 63, type=1))

        self.bullet_list = []

        self.coin_list = []
        self.coin_list.append(Coin(x= 40, y= 400, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 190, y= 200, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 340, y= 400, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 490, y= 200, frame_animation_ms= 30, move_rate_ms= 30))
        self.coin_list.append(Coin(x= 640, y= 400, frame_animation_ms= 30, move_rate_ms= 30))
    
    def bullets_shoot(self):
        if self.player_1.is_shoot:
            if((self.tiempo_transcurrido - self.cooldown_shoot) > self.interval_shoot):
                self.shoot()
                self.cooldown_shoot = self.tiempo_transcurrido
            self.bullet_list.append(Bullet(x_init=self.player_1.rect.centerx + (0.8 * self.player_1.rect.size[0] * self.player_1.direction), y_init=self.player_1.rect.centery, frame_rate_ms=30, move_rate_ms=60, velocity_x=5, p_scale=0.5, direction=self.player_1.direction))

    def update(self, list_events, keys, delta_ms):

        self.bullets_shoot()
        for bullet in self.bullet_list:
                bullet.update(delta_ms)
        
        for coin in self.coin_list:
            coin.update(delta_ms, self.player_1)

        self.player_1.events(delta_ms, keys)
        self.player_1.update(delta_ms, self.plataform_list)

        self.enemy_1.update(delta_ms, self.plataform_list)
        self.enemy_2.update(delta_ms, self.plataform_list)

    def draw(self):
        super().draw()
        self.static_background.draw(self.surface)

        for plataform in self.plataform_list:
            plataform.draw(self.surface)

        for bullet in self.bullet_list:
            bullet.draw(self.surface)

        for coin in self.coin_list:
            coin.draw(self.surface)

        self.player_1.draw(self.surface)

        self.enemy_1.draw(self.surface)

        self.enemy_2.draw(self.surface)


        